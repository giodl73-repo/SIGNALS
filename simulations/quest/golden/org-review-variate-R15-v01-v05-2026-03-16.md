# org-review Variations R15 V-01 through V-05
# Rubric: v11 (225 pts max, gold >= 190)
# Date: 2026-03-16

---

## V-01 -- Single-axis: Role Sequence (Lifecycle-First)

**Variation axis**: Role sequence -- LIFECYCLE runs before DOMAIN.

**Hypothesis**: Running the commitment/program reviewer before the technical domain reviewer
surfaces strategic blockers early. If G_lifecycle=FAIL, domain review scope can be narrowed.
g_null progression stages are reordered: Stage 2 = post-lifecycle, Stage 3 = post-domain.
Primary Driver derivation (§16) fires on different gates when lifecycle is the first domain-
type evaluator, potentially changing attribution patterns versus domain-first ordering.

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
DISPOSITION_CONTRACT v1-LS (lifecycle-sequence variant)
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§17;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE (cited in §5.5 SCOPE COVERAGE RECONCILIATION and §11 FINDING-SURFACE LINKAGE):
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
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
  These definitions apply universally.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_lifecycle, G_domain_agg, GClose}
  BLOCKED      <-- GClose=FAIL OR exists Gi=FAIL
  CONDITIONAL  <-- no Gi=FAIL AND exists Gi=CONDITIONAL
  READY        <-- all Gi=PASS

§3a -- LIFECYCLE-AGGREGATE FORMULA [IMMUTABLE -- lifecycle-sequence variant]
  G_lifecycle from the single lifecycle reviewer is used directly.
  (deep: G_lifecycle_agg = worst(all G_lifecycle rows). FAIL>CONDITIONAL>PASS.)

§3b -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain rows). FAIL>CONDITIONAL>PASS.
  Single domain: G_domain_agg = G_domain (direct pass-through).

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1-LS"
  A missing cite is an audit-trail gap.

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, ...).
  Every downstream section carries a mandatory CH-ID response table.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  EXCLUDED (no row emitted): §3.5L, §3.8, §4.5, §5.5.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE -- lifecycle-sequence variant]
  1. ROLE MANIFEST (APPLICABILITY MATRIX required before BRACKET OPENING)
  2. BRACKET OPENING
  3. LIFECYCLE
  3.5L. LIFECYCLE-AGGREGATE CHECKPOINT
  3.8. CH-ID SATURATION CHECK (pre-domain)
  4. DOMAIN(s)
  4.5. DOMAIN-AGGREGATE CHECKPOINT
  5. BRACKET CLOSING
  5.5. SCOPE COVERAGE RECONCILIATION (surface table + DOMAIN COVERAGE GAP-CHECK)
  6. GATE VECTOR TABLE
  7. CROSS-ROLE SIGNALS
  8. DISPOSITION
  9. ACTION ITEM REGISTER
  Reordering any section violates this contract.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  FULLY SATURATED: CH-ID has received LIFECYCLE + DOMAIN responses before BRACKET CLOSING.
  PASS from BRACKET CLOSING is prohibited without full saturation or a stated waiver.
  Waiver: "CH-XXX WAIVER: [reason]"
  Waivers -> ACTION ITEM REGISTER as ADVISORY.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE -- lifecycle-sequence variant]
  Stage 1: g_null(initial) = output of §17 formula [emitted at BRACKET OPENING]
           [If §17 inactive: g_null(initial) = GOpen verdict directly]
  Stage 2: g_null(post-lifecycle) [emitted at §3.5L]:
    G_lifecycle=FAIL        -> g_null(post-lifecycle)=FAIL
    G_lifecycle=CONDITIONAL -> g_null(post-lifecycle)=max(g_null(initial), CONDITIONAL)
    G_lifecycle=PASS        -> g_null(post-lifecycle)=g_null(initial)
  Stage 3: g_null(final) [emitted at BRACKET CLOSING]:
    G_domain_agg=FAIL        -> g_null(final)=FAIL
    G_domain_agg=CONDITIONAL -> g_null(final)=max(g_null(post-lifecycle), CONDITIONAL)
    G_domain_agg=PASS        -> g_null(final)=g_null(post-lifecycle)
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
  Step 1: Group §1 IN-SCOPE surfaces into ARTIFACT DOMAINS (logical groupings).
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
    g_null(initial) | g_null(post-lifecycle) | g_null(final) | Trajectory
  Labels: MONOTONIC-PASS / MONOTONIC-FAIL / LIFECYCLE-DEGRADED / DOMAIN-DEGRADED /
          LIFECYCLE-RECOVERED / DOMAIN-RECOVERED. Informational only.

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
  BRACKET OPENING challenger evaluates the null hypothesis via a dedicated per-dimension table
  before stating challenge claims. Table is SEPARATE from the §16 C-16 alternatives table.

  Table format:
    | Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
  NH Verdict: pos Differential -> FAVORS-BUILD; zero -> NEUTRAL; neg -> OPPOSES-BUILD.
  MUST-CLEAR dimensions marked (*). Minimum 3 dimensions.

  g_null derivation rule (pre-committed; apply mechanically):
    HOLDS      <-- any MUST-CLEAR row has NH Verdict = OPPOSES-BUILD
    CONDITIONAL <-- no MUST-CLEAR OPPOSES-BUILD AND count(OPPOSES-BUILD) >= count(FAVORS-BUILD)
    DEFEATED   <-- no MUST-CLEAR OPPOSES-BUILD AND count(FAVORS-BUILD) > count(OPPOSES-BUILD)

  DEFEATED -> GOpen = PASS; CONDITIONAL -> GOpen = CONDITIONAL; HOLDS -> GOpen = FAIL.

  BRACKET CLOSING re-applies §17 rule to the REVISED NULL HYPOTHESIS DIMENSION TABLE
  (lifecycle + domain re-scores aggregated). The revised table's NH Verdict column is the
  sole input to the closing g_null derivation.

  §9 Stage 1 g_null(initial) = §17 formula output; NOT equal to GOpen unless formula agrees.
  A scorer verifying g_null reads only the NH Verdict column. No prose needed.

======================================================================
END DISPOSITION_CONTRACT v1-LS
======================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE -- runs first; commitment-frame] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE -- runs after lifecycle] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3. Each adds rows to APPLICABILITY MATRIX.)*

### APPLICABILITY MATRIX

*(REQUIRED before BRACKET OPENING executes. Complete this matrix now. It is locked at this
point and may not be modified by any downstream section. Referenced by §15 and §10a.)*

For each assigned reviewer role, list every `lens.verify` entry and assign:
- **HIGH**: lens dimension directly relevant to this artifact type. Finding expected.
  OPEN in §15 -> ADVISORY-OPEN-LENS-REQUIRED in ACTION ITEM REGISTER.
- **MEDIUM**: lens dimension tangentially relevant. Finding expected.
  OPEN in §15 -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.
- **LOW**: lens dimension not applicable to this artifact type. OPEN acceptable.
  State basis. Cite row ID in §15 Finding Reference column.

Also note the ARTIFACT DOMAIN each lens entry targets -- used by §10a DOMAIN COVERAGE GAP-CHECK.

| Row ID | Role | lens.verify Entry | Artifact Domain Covered | Artifact Applicability | Basis for Rating |
|--------|------|------------------|------------------------|----------------------|------------------|
| AM-01 | [LIFECYCLE ROLE] | [Full text lens.verify entry 1] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-02 | [LIFECYCLE ROLE] | [Full text lens.verify entry 2] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-03 | [DOMAIN ROLE] | [Full text lens.verify entry 1] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-04 | [DOMAIN ROLE] | [Full text lens.verify entry 2] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-05 | [DOMAIN ROLE] | [Full text lens.verify entry 3 if present] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |

*(Add rows for every lens.verify entry from every assigned role. APPLICABILITY MATRIX is now
locked. No reviewer section may alter these values.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1-LS

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]

**Alternatives comparison table** *(per §16 C-16 -- >= 3 dimensions; distinct from §17 below)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17 -- g_null derivable from NH Verdict column alone)*:

| Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
|-----------|--------------------------|----------------------------|--------------|------------|
| [DIM-A*]  | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

*(Dimensions marked * are MUST-CLEAR. Add rows as needed.)*

**Applying §17 g_null derivation rule**:
```
MUST-CLEAR rows with OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD) = [N]
count(NEUTRAL)      = [N]
count(OPPOSES-BUILD) = [N]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null(initial)** *(output of §17 formula; carried to §9 Stage 1)*: [HOLDS / CONDITIONAL / DEFEATED]

**Challenge claims** *(assign CH-IDs per §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL -- consistent with §17 g_null result]
**GOpen Reason**: [One sentence.]
**g_null(initial)** *(§9 Stage 1)*: [copy from §17 derivation above]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-LS
Received GOpen: [copy from BRACKET OPENING]
*(Note: LIFECYCLE runs before DOMAIN in v1-LS. Domain findings are not yet available.)*

**CH-ID Response Table** *(mandatory per §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph. Reference GOpen and g_null(initial) explicitly.
Note: domain technical assessment has not yet run -- state any assumptions made.]

**Null hypothesis status**: [yes / partial / no -- reference g_null(initial). One sentence.]

**Additional Findings** *(per §14 and §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1 -- commitment, program, or decision concerns.] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**Lens Coverage Table** *(per §15 -- cite APPLICABILITY MATRIX row IDs)*:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [Full text lens.verify entry 1] | AM-01: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or cite AM-01] |
| Q-2 | [Full text lens.verify entry 2] | AM-02: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or cite AM-02] |

*(HIGH/MEDIUM+OPEN -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5L LIFECYCLE-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6 -- no verdict emitted.)*

**Applying §3a formula**:
```
G_lifecycle rows collected:
  LIFECYCLE -- [ROLE_NAME]: [verdict]
G_lifecycle (direct pass-through for single reviewer) = [PASS / CONDITIONAL / FAIL]
```
**G_lifecycle value**: [PASS / CONDITIONAL / FAIL]

**Applying §9 Stage 2 formula**:
```
g_null(initial) = [copy from BRACKET OPENING] | G_lifecycle = [copy]
  FAIL->FAIL | CONDITIONAL->max(initial,CONDITIONAL) | PASS->g_null(initial)
g_null(post-lifecycle) = [result]
```
**g_null(post-lifecycle)**: [FAIL / CONDITIONAL / PASS]

*Both carry forward to §3.8, DOMAIN, §4.5, and BRACKET CLOSING.*

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger. Runs after §3.5L, before DOMAIN.)*

| CH-ID | LIFECYCLE Response Status | Pre-DOMAIN Saturation |
|-------|--------------------------|----------------------|
| CH-001 | [copy from LIFECYCLE] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED or N/A] |

**Pre-DOMAIN unsaturated CH-IDs**: [List or "None"]
*DOMAIN may proceed. Full saturation check executes at BRACKET CLOSING.*

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-LS
Received GOpen: [copy from BRACKET OPENING]
Received G_lifecycle: [copy from §3.5L]
Received g_null(post-lifecycle): [copy from §3.5L]

**CH-ID Response Table** *(mandatory per §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

*(PARTIAL requires named resolution path. OPEN = claim not addressable from this role's frame.)*

**Domain re-score** *(same dimensions as BRACKET OPENING alternatives table)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| [DIM-1] | [revised] | [revised] | [revised] | [reason] |
| [DIM-2] | [revised] | [revised] | [revised] | |
| [DIM-3] | [revised] | [revised] | [revised] | |

**Additional Findings** *(per §14 and §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**Lens Coverage Table** *(per §15 -- cite APPLICABILITY MATRIX row IDs)*:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [Full text lens.verify entry 1] | AM-03: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or cite AM-03] |
| Q-2 | [Full text lens.verify entry 2] | AM-04: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or cite AM-04] |
| Q-3 | [Full text if present] | AM-05: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or cite AM-05] |

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §4.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6.)*

**Applying §3b formula**:
```
G_domain rows collected:
  DOMAIN -- [ROLE_NAME]: [verdict]
G_domain_agg = worst([list]) = [PASS / CONDITIONAL / FAIL]
```
**G_domain_agg**: [PASS / CONDITIONAL / FAIL]

**Applying §9 Stage 3 formula**:
```
g_null(post-lifecycle) = [copy from §3.5L] | G_domain_agg = [copy]
  FAIL->FAIL | CONDITIONAL->max(post-lifecycle,CONDITIONAL) | PASS->g_null(post-lifecycle)
g_null(final) [provisional] = [result]
```
**g_null(final) provisional**: [FAIL / CONDITIONAL / PASS]
*Carries forward to BRACKET CLOSING for final confirmation.*

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1-LS
*Full record received: scope declaration, APPLICABILITY MATRIX, G_lifecycle, G_domain_agg,
all CH-ID tables, all verdicts.*

**Applying §9 Stage 3 formula**:
```
g_null(post-lifecycle) = [copy from §3.5L]
G_domain_agg           = [copy from §4.5]
  FAIL->FAIL | CONDITIONAL->max(post-lifecycle,CONDITIONAL) | PASS->g_null(post-lifecycle)
g_null(final) = [result]
```
**g_null(final)**: [FAIL / CONDITIONAL / PASS]
*GClose must equal g_null(final) per §9.*

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(per §17 -- aggregate lifecycle + domain re-scores)*:

| Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
|-----------|--------------------------|----------------------------|--------------|------------|
| [DIM-A*]  | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

**Applying §17 g_null derivation rule to revised table**:
```
MUST-CLEAR rows with OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD) = [N] | count(OPPOSES-BUILD) = [M]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```

**Revised alternatives table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Agg Rationale |
|-----------|---------------|-----------|----------------------|--------------|
| [DIM-1] | [agg] | [agg] | [agg] | [reason] |
| [DIM-2] | [agg] | [agg] | [agg] | |

**Full CH-ID Saturation Check** *(per §8)*:

| CH-ID | LIFECYCLE Status | DOMAIN Status | Full Saturation | Waiver (if needed) |
|-------|-----------------|--------------|-----------------|---------------------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |

**CH-ID Final Assessment**:

| CH-ID | G_lifecycle Status | G_domain Status | Final Status | Notes |
|-------|-------------------|----------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [All defeated, or list.]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A -- formula applied | or: override justification]
**GClose Rationale**: [2-3 sentences. Reference g_null(final), CH-ID saturation, trajectory.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6. Applies §10, §10a, §11.)*

### Surface Coverage *(per §10)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [LIFECYCLE F-n / DOMAIN F-n / etc.] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [ref] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [ref] | [COVERED / GAP] |

**Surface coverage gate signal**: [COVERED / PARTIAL -- [N] surface(s) not addressed]

### Domain Coverage Gap-Check *(per §10a)*

| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|----------|
| [DOMAIN-1] | [AM-0n: [ROLE] -- "[lens entry summary]" / "none"] | [COVERED / ADVISORY-GAP] |
| [DOMAIN-2] | [AM-0n / "none"] | [COVERED / ADVISORY-GAP] |

**§11 ADVISORY-ORPHAN check**: [List or "None detected."]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen -- bracket opening | [CHALLENGER_ROLE] | [copy] | DISPOSITION_CONTRACT v1-LS |
| G_lifecycle -- lifecycle | [LIFECYCLE_ROLE] | [copy] | DISPOSITION_CONTRACT v1-LS |
| G_domain_agg -- domain aggregate | [DOMAIN_ROLE] | [copy] | DISPOSITION_CONTRACT v1-LS |
| GClose -- bracket closing | [CHALLENGER_ROLE] | [copy] | DISPOSITION_CONTRACT v1-LS |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Two reviewers with incompatible CH-ID responses or findings. If none: "None detected."]

**Convergence**: [Any concern named independently by two or more reviewers.]

**Scope coverage**: [Any §1 surface not covered. If all covered: "None."]

**§13 PROGRESSION LEDGER**:
```
g_null(initial)       = [copy from BRACKET OPENING §17 formula]
g_null(post-lifecycle) = [copy from §3.5L]
g_null(final)         = [copy from BRACKET CLOSING §9 Stage 3]
Trajectory:           [MONOTONIC-PASS / MONOTONIC-FAIL / LIFECYCLE-DEGRADED / DOMAIN-DEGRADED /
                       LIFECYCLE-RECOVERED / DOMAIN-RECOVERED]
```

---

## DISPOSITION

**Gate vector**:
- GOpen = [copy]
- G_lifecycle = [copy]
- G_domain_agg = [copy]
- GClose = [copy]

**Apply contract §3 formula**:
```
G = {GOpen=[_], G_lifecycle=[_], G_domain_agg=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Applying §16 rule**: [rule number fired and why]
**Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**Conditions** *(CONDITIONAL only)*:
1. [Condition.]

**Blocker** *(BLOCKED only)*: [Specific finding from FAIL gate.]

**RESOLUTION REGISTRY** *(CONDITIONAL only)*:
| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [one sentence] | [role] | [falsifiable test] | OPEN |

*If not CONDITIONAL: "RESOLUTION REGISTRY: N/A -- disposition is [value]"*

---

## ACTION ITEM REGISTER

*Assembly rule per §6: copy all local gate ledger rows verbatim. Then add CH-ID items,
ADVISORY-OPEN-LENS items, ADVISORY-GAP items (§10 + §10a), ADVISORY-ORPHAN items (§11).*

| Source | CH-ID / Finding | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|--------|----------------|-----------------|------------------|------------|---------------------|
| [gate ledger copy] | -- | [verbatim: Section / Gate / Verdict / Class] | [BLOCKED/CONDITIONAL/ADVISORY] | [ROLE] | [criterion] |
| [CH-ID item] | CH-00n | [What must be done] | [class] | [ROLE] | [criterion] |
| [lens gap HIGH] | AM-0n / Q-n | ADVISORY-OPEN-LENS-REQUIRED: [entry] | ADVISORY | [ROLE] | Produce finding. |
| [lens gap MED] | AM-0n / Q-n | ADVISORY-OPEN-LENS: [entry] | ADVISORY | [ROLE] | Address or justify. |
| [scope gap] | -- | ADVISORY-GAP: §1 surface [name] not covered | ADVISORY | [ROLE] | Assign reviewer. |
| [domain gap] | -- | ADVISORY-GAP (DOMAIN COVERAGE): [domain] no HIGH-applicability reviewer | ADVISORY | [ROLE] | Add reviewer or justify. |

---

**Artifact to review:**

{{artifact}}

---
---

## V-02 -- Single-axis: Output Format (Evidence Quality Column + Mandatory Minimums)

**Variation axis**: Output format -- Lens Coverage Table gains an "Evidence Quality" column
(DIRECT / INFERRED / ABSENT). All finding rows mandatory with minimum counts enforced.
No "(optional)" markers anywhere. Finding tables add a "Root Cause" column.

**Hypothesis**: Explicit evidence quality tagging forces the model to distinguish between
findings that directly test a lens dimension (DIRECT) versus findings that partially address
it by implication (INFERRED). INFERRED creates a middle-ground state that surfaces coverage
gaps more precisely than binary ADDRESSED/OPEN. ABSENT makes "no coverage" explicit without
requiring a separate ADVISORY entry. Mandatory minimums prevent the model from emitting
trivial single-finding sections that pass §14 mechanically.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
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

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. If a field cannot be filled, write
`[N/A -- reason]`. Minimum finding counts are enforced: each DOMAIN section emits >= 3 findings;
LIFECYCLE emits >= 2 findings. Each finding includes a Root Cause column.

---

```
======================================================================
DISPOSITION_CONTRACT v1-EQ (evidence-quality variant)
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§17;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE (cited in §5.5 and §11):
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
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
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1-EQ"

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
  5.5. SCOPE COVERAGE RECONCILIATION
  6. GATE VECTOR TABLE
  7. CROSS-ROLE SIGNALS
  8. DISPOSITION
  9. ACTION ITEM REGISTER

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  FULLY SATURATED: CH-ID has received DOMAIN + LIFECYCLE responses before BRACKET CLOSING.
  PASS from BRACKET CLOSING is prohibited without full saturation or a stated waiver.
  Waiver: "CH-XXX WAIVER: [reason]" -> ACTION ITEM REGISTER as ADVISORY.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = output of §17 formula [BRACKET OPENING]
  Stage 2: g_null(post-domain) [§3.5]:
    G_domain_agg=FAIL        -> g_null(post-domain)=FAIL
    G_domain_agg=CONDITIONAL -> g_null(post-domain)=max(g_null(initial), CONDITIONAL)
    G_domain_agg=PASS        -> g_null(post-domain)=g_null(initial)
  Stage 3: g_null(final) [BRACKET CLOSING]:
    G_lifecycle=FAIL         -> g_null(final)=FAIL
    G_lifecycle=CONDITIONAL  -> g_null(final)=max(g_null(post-domain), CONDITIONAL)
    G_lifecycle=PASS         -> g_null(final)=g_null(post-domain)
  GClose must equal g_null(final). Override: "g_null OVERRIDE: [justification]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  After BRACKET CLOSING, §5.5 maps each §1 IN-SCOPE surface to reviewer findings.
  COVERED (>=1 finding) or GAP (no finding). GAP -> ADVISORY-GAP in ACTION ITEM REGISTER.
  §5.5 ALSO runs DOMAIN COVERAGE GAP-CHECK per §10a.

§10a -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  Embedded in §5.5, after the surface coverage table.
  Step 1: Group §1 IN-SCOPE surfaces into ARTIFACT DOMAINS.
  Step 2: For each domain, look up ROLE MANIFEST APPLICABILITY MATRIX rows where
          Artifact Domain Covered matches AND Artifact Applicability = HIGH.
  Step 3: COVERED = at least one HIGH row. ADVISORY-GAP = no HIGH row.
  Step 4: ADVISORY-GAP domains -> ACTION ITEM REGISTER (Attribution: "DOMAIN COVERAGE
          GAP-CHECK / [domain] / no HIGH-applicability reviewer"). Class: ADVISORY.
  Table: | Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding carries "[§1:S-n]" citation. Missing = ADVISORY-ORPHAN -> register.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit RESOLUTION REGISTRY (Gate/Condition/Owner/Criterion/OPEN).
  Else: "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS §13 PROGRESSION LEDGER:
    g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory
  Labels: MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
          DOMAIN-RECOVERED / LIFECYCLE-RECOVERED. Informational only.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE -- v1-EQ: minimum counts enforced]
  Findings table: | # | §1 Surface | Finding | Root Cause | Severity |
  Minimum: DOMAIN >= 3 findings. LIFECYCLE >= 2 findings.
  Section Severity = worst(all severities). HIGH>MEDIUM>LOW.
  No findings: Section Severity = LOW (only valid if minimum waived).

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE -- v1-EQ: Evidence Quality column added]
  Each DOMAIN and LIFECYCLE section addresses ALL lens.verify entries.
  After findings, emit LENS COVERAGE TABLE:
    | # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Evidence Quality | Status | Finding Reference |

  Applicability column: cite APPLICABILITY MATRIX row ID and tier. Value locked from ROLE MANIFEST.
  Evidence Quality: DIRECT (finding directly tests this dimension) /
                    INFERRED (finding partially addresses it by implication) /
                    ABSENT (no evidence; must be justified).
  Status: ADDRESSED (Evidence Quality = DIRECT or INFERRED) / OPEN (Evidence Quality = ABSENT).
  HIGH applicability + OPEN -> ADVISORY-OPEN-LENS-REQUIRED.
  MEDIUM applicability + OPEN -> ADVISORY-OPEN-LENS.
  LOW applicability + OPEN -> cite AM row; no register entry.
  INFERRED + HIGH applicability -> ADVISORY-OPEN-LENS (partial coverage; direct evidence preferred).

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  1. GClose=FAIL        -> Primary Driver = BRACKET CLOSING
  2. G_domain_agg=FAIL  -> Primary Driver = DOMAIN
  3. G_lifecycle=FAIL   -> Primary Driver = LIFECYCLE
  4. GOpen=FAIL         -> Primary Driver = BRACKET OPENING
  5. GClose=CONDITIONAL -> Primary Driver = BRACKET CLOSING
  6. G_domain_agg=CONDITIONAL -> DOMAIN
  7. G_lifecycle=CONDITIONAL  -> LIFECYCLE
  8. GOpen=CONDITIONAL        -> BRACKET OPENING
  9. all PASS           -> N/A
  Emit: **Applying §16 rule**: [n + reason]  **Primary Driver**: [result]

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]
  BRACKET OPENING challenger evaluates null hypothesis via per-dimension table before claims.
  Table: | Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
  NH Verdict: pos -> FAVORS-BUILD; zero -> NEUTRAL; neg -> OPPOSES-BUILD.
  MUST-CLEAR marked (*). Minimum 3 dimensions.
  g_null rule: HOLDS (any MUST-CLEAR OPPOSES) / CONDITIONAL (no MC-OPPOSES, OPPOSES>=FAVORS) /
               DEFEATED (no MC-OPPOSES, FAVORS>OPPOSES).
  BRACKET CLOSING re-applies to revised aggregate table.

======================================================================
END DISPOSITION_CONTRACT v1-EQ
======================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3.)*

### APPLICABILITY MATRIX

*(REQUIRED before BRACKET OPENING. Locked on completion.)*

| Row ID | Role | lens.verify Entry | Artifact Domain Covered | Artifact Applicability | Basis for Rating |
|--------|------|------------------|------------------------|----------------------|------------------|
| AM-01 | [DOMAIN ROLE] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-02 | [DOMAIN ROLE] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-03 | [DOMAIN ROLE] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-04 | [LIFECYCLE ROLE] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-05 | [LIFECYCLE ROLE] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [One sentence] |

*(Add rows for every lens.verify entry. Matrix locked after this point.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1-EQ

**Null hypothesis**: [One sentence.]

**Alternatives comparison table** *(>= 3 dimensions)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17)*:

| Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
|-----------|--------------------------|----------------------------|--------------|------------|
| [DIM-A*]  | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

**Applying §17 g_null derivation rule**:
```
MUST-CLEAR rows with OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD) = [N] | count(OPPOSES-BUILD) = [N]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null(initial)**: [HOLDS / CONDITIONAL / DEFEATED]

**Challenge claims**:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3] | [HIGH / MEDIUM / LOW] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)** *(§9 Stage 1)*: [copy from §17]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-EQ
Received GOpen: [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | Technical Response | Status |
|-------|----------------------|-------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Domain re-score**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| [DIM-1] | [revised] | [revised] | [revised] | [reason] |
| [DIM-2] | [revised] | [revised] | [revised] | |
| [DIM-3] | [revised] | [revised] | [revised] | |

**Findings** *(minimum 3 required per §14 v1-EQ)*:

| # | §1 Surface | Finding | Root Cause | Severity |
|---|-----------|---------|-----------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [ROOT_CAUSE_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [ROOT_CAUSE_2] | [HIGH / MEDIUM / LOW] |
| F-3 | [§1:S-n] | [FINDING_3] | [ROOT_CAUSE_3] | [HIGH / MEDIUM / LOW] |

*(Additional rows required if warranted by artifact.)*

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], F-3=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**Lens Coverage Table** *(per §15 v1-EQ -- includes Evidence Quality)*:

| # | lens.verify Entry | Applicability | Evidence Quality | Status | Finding Reference |
|---|------------------|--------------|-----------------|--------|-------------------|
| Q-1 | [Full text entry 1] | AM-01: [HIGH/MED/LOW] | [DIRECT / INFERRED / ABSENT] | [ADDRESSED / OPEN] | [F-n or AM-cite] |
| Q-2 | [Full text entry 2] | AM-02: [HIGH/MED/LOW] | [DIRECT / INFERRED / ABSENT] | [ADDRESSED / OPEN] | [F-n or AM-cite] |
| Q-3 | [Full text entry 3] | AM-03: [HIGH/MED/LOW] | [DIRECT / INFERRED / ABSENT] | [ADDRESSED / OPEN] | [F-n or AM-cite] |

*(HIGH+ABSENT -> ADVISORY-OPEN-LENS-REQUIRED. HIGH+INFERRED -> ADVISORY-OPEN-LENS. LOW+ABSENT -> cite AM row.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from lens.simplify.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger.)*

```
G_domain_agg = worst([G_domain verdict(s)]) = [PASS / CONDITIONAL / FAIL]
```
**G_domain_agg**: [PASS / CONDITIONAL / FAIL]

```
g_null(initial) = [copy] | G_domain_agg = [copy]
g_null(post-domain) = [result]
```
**g_null(post-domain)**: [FAIL / CONDITIONAL / PASS]

---

## §3.8 CH-ID SATURATION CHECK

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | [copy] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy] | [SATURATED / UNSATURATED] |

**Pre-LIFECYCLE unsaturated**: [List or "None"]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-EQ
Received GOpen: [copy]
Received G_domain_agg: [copy]
Received g_null(post-domain): [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | Commitment-Frame Response | Status |
|-------|----------------------|--------------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph. Reference GOpen, G_domain_agg, g_null(post-domain).]

**Null hypothesis status**: [yes / partial / no -- reference g_null(post-domain).]

**Findings** *(minimum 2 required per §14 v1-EQ)*:

| # | §1 Surface | Finding | Root Cause | Severity |
|---|-----------|---------|-----------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [ROOT_CAUSE_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [ROOT_CAUSE_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**Lens Coverage Table** *(per §15 v1-EQ)*:

| # | lens.verify Entry | Applicability | Evidence Quality | Status | Finding Reference |
|---|------------------|--------------|-----------------|--------|-------------------|
| Q-1 | [Full text] | AM-04: [HIGH/MED/LOW] | [DIRECT / INFERRED / ABSENT] | [ADDRESSED / OPEN] | [F-n or AM-cite] |
| Q-2 | [Full text] | AM-05: [HIGH/MED/LOW] | [DIRECT / INFERRED / ABSENT] | [ADDRESSED / OPEN] | [F-n or AM-cite] |

**Recommendation**: [One concrete action.]
**Simplify**: [One from lens.simplify.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1-EQ

```
g_null(post-domain) = [copy] | G_lifecycle = [copy]
g_null(final) = [result]
```
**g_null(final)**: [FAIL / CONDITIONAL / PASS]

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(per §17)*:

| Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
|-----------|--------------------------|----------------------------|--------------|------------|
| [DIM-A*]  | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

```
count(FAVORS-BUILD) = [N] | count(OPPOSES-BUILD) = [M]
Revised result: [HOLDS / CONDITIONAL / DEFEATED]
```

**Revised alternatives table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Agg Rationale |
|-----------|---------------|-----------|----------------------|--------------|
| [DIM-1] | [agg] | [agg] | [agg] | [reason] |
| [DIM-2] | [agg] | [agg] | [agg] | |

**Full CH-ID Saturation Check**:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver |
|-------|--------------|-----------------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-003 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |

**CH-ID Final Assessment**:

| CH-ID | G_domain | G_lifecycle | Final Status | Notes |
|-------|---------|------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-003 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A or justification]
**GClose Rationale**: [2-3 sentences.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger.)*

### Surface Coverage

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [SURFACE_1] | [ROLE] | [F-n] | [COVERED / GAP] |
| [SURFACE_2] | [ROLE] | [F-n] | [COVERED / GAP] |

**Surface coverage gate signal**: [COVERED / PARTIAL]

### Domain Coverage Gap-Check *(per §10a)*

| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|----------|
| [DOMAIN-1] | [AM-0n / "none"] | [COVERED / ADVISORY-GAP] |
| [DOMAIN-2] | [AM-0n / "none"] | [COVERED / ADVISORY-GAP] |

**§11 ADVISORY-ORPHAN check**: [List or "None detected."]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER_ROLE] | [copy] | DISPOSITION_CONTRACT v1-EQ |
| G_domain_agg | [DOMAIN_ROLE] | [copy] | DISPOSITION_CONTRACT v1-EQ |
| G_lifecycle | [LIFECYCLE_ROLE] | [copy] | DISPOSITION_CONTRACT v1-EQ |
| GClose | [CHALLENGER_ROLE] | [copy] | DISPOSITION_CONTRACT v1-EQ |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Incompatible responses. "None detected." if none.]
**Convergence**: [Findings named independently by 2+ reviewers.]
**Scope coverage**: [Uncovered §1 surfaces or "None."]

**§13 PROGRESSION LEDGER**:
```
g_null(initial)     = [copy]
g_null(post-domain) = [copy]
g_null(final)       = [copy]
Trajectory: [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
             DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

---

## DISPOSITION

**Gate vector**:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

```
GClose=FAIL? -> BLOCKED | Any Gi=FAIL? -> BLOCKED | Any CONDITIONAL? -> CONDITIONAL | All PASS? -> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Applying §16 rule**: [rule + reason]
**Primary Driver**: [result]

**Conditions** *(CONDITIONAL only)*: [list]
**Blocker** *(BLOCKED only)*: [specific finding]

**RESOLUTION REGISTRY** *(CONDITIONAL only)*:
| Gate | Condition | Owner | Resolution Criterion | Status |
|------|-----------|-------|---------------------|--------|
| [gate] | [sentence] | [role] | [falsifiable test] | OPEN |

*If not CONDITIONAL: "RESOLUTION REGISTRY: N/A -- disposition is [value]"*

---

## ACTION ITEM REGISTER

| Source | CH-ID / Finding | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|--------|----------------|-----------------|------------------|------------|---------------------|
| [gate ledger] | -- | [verbatim Section / Gate / Verdict / Class] | [class] | [ROLE] | [criterion] |
| [CH-ID] | CH-00n | [action required] | [class] | [ROLE] | [criterion] |
| [lens HIGH ABSENT] | AM-0n / Q-n | ADVISORY-OPEN-LENS-REQUIRED: [entry] not addressed | ADVISORY | [ROLE] | Produce direct finding. |
| [lens HIGH INFERRED] | AM-0n / Q-n | ADVISORY-OPEN-LENS: [entry] has INFERRED coverage only; direct evidence preferred | ADVISORY | [ROLE] | Produce direct finding. |
| [lens MED ABSENT] | AM-0n / Q-n | ADVISORY-OPEN-LENS: [entry] absent; MEDIUM applicability | ADVISORY | [ROLE] | Address or justify. |
| [scope gap] | -- | ADVISORY-GAP: surface [name] not covered | ADVISORY | [ROLE] | Assign reviewer. |
| [domain gap] | -- | ADVISORY-GAP (DOMAIN COVERAGE): [domain] no HIGH reviewer | ADVISORY | [ROLE] | Add reviewer. |

---

**Artifact to review:**

{{artifact}}

---
---

## V-03 -- Single-axis: Lifecycle Emphasis (NH Sub-Evaluation in Lifecycle)

**Variation axis**: Lifecycle emphasis -- LIFECYCLE section gains a dedicated NULL HYPOTHESIS
LIFECYCLE ASSESSMENT sub-section. The lifecycle role evaluates the null hypothesis from a
commitment-readiness perspective, emitting a g_null_lifecycle signal before its gate verdict.
§9 Stage 3 is modified to incorporate g_null_lifecycle as a second input.

**Hypothesis**: Lifecycle reviewers hold commitment-frame evidence structurally distinct from
technical domain evidence. A PM/program reviewer who sees the null hypothesis as viable from
a roadmap perspective may flag a dimension the domain reviewer missed. By surfacing
g_null_lifecycle explicitly, the three-stage NH progression gains a fourth data point: the
lifecycle role's independent assessment of whether the null holds from a commitment-readiness
perspective. This can produce LIFECYCLE-RECOVERED or LIFECYCLE-NH-BLOCKED trajectories that
are invisible in the baseline.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. If a field cannot be filled, write
`[N/A -- reason]`.

---

```
======================================================================
DISPOSITION_CONTRACT v1-LC (lifecycle-challenge variant)
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§17;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]

§1 COMPLETE -- role selection, APPLICABILITY MATRIX, and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks. MEDIUM = Conditions. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED <-- GClose=FAIL OR exists Gi=FAIL
  CONDITIONAL <-- no FAIL AND exists CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(G_domain rows). Single domain: direct pass-through.

§4 -- CONTRACT CITE [IMMUTABLE]
  Each reviewer section: "Contract: DISPOSITION_CONTRACT v1-LC"

§5 -- CH-ID TRACING [IMMUTABLE]
  BRACKET OPENING claims -> CH-IDs. Every downstream section: mandatory CH-ID response table.
  PASS prohibited if any CH-ID OPEN.

§6 -- LOCAL GATE LEDGER [IMMUTABLE]
  Row: | Section | Gate | Verdict | Class |
  FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  EXCLUDED: §3.5, §3.8, §5.5.

§7 -- SECTION ORDER [IMMUTABLE]
  1. ROLE MANIFEST (APPLICABILITY MATRIX first)
  2. BRACKET OPENING
  3. DOMAIN(s)
  3.5. DOMAIN-AGGREGATE CHECKPOINT
  3.8. CH-ID SATURATION CHECK
  4. LIFECYCLE (includes §4a NH LIFECYCLE ASSESSMENT sub-section)
  5. BRACKET CLOSING
  5.5. SCOPE COVERAGE RECONCILIATION
  6. GATE VECTOR TABLE
  7. CROSS-ROLE SIGNALS
  8. DISPOSITION
  9. ACTION ITEM REGISTER

§8 -- CH-ID SATURATION [IMMUTABLE]
  FULLY SATURATED: DOMAIN + LIFECYCLE responses before BRACKET CLOSING.
  PASS prohibited without full saturation or stated waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE -- v1-LC: four-signal variant]
  Stage 1: g_null(initial) = §17 formula output [BRACKET OPENING]
  Stage 2: g_null(post-domain) [§3.5]:
    G_domain_agg=FAIL        -> FAIL
    G_domain_agg=CONDITIONAL -> max(g_null(initial), CONDITIONAL)
    G_domain_agg=PASS        -> g_null(initial)
  Stage 2b: g_null_lifecycle [§4a]:
    Derived from §4a LIFECYCLE NH TABLE using §17 rule on commitment dimensions.
    Informational signal. Feeds Stage 3 override rule only.
  Stage 3: g_null(final) [BRACKET CLOSING]:
    G_lifecycle=FAIL         -> FAIL
    G_lifecycle=CONDITIONAL  -> max(g_null(post-domain), CONDITIONAL)
    G_lifecycle=PASS         -> g_null(post-domain)
    THEN: if g_null_lifecycle=FAIL AND g_null(final)!=FAIL -> g_null(final)=FAIL with note
  GClose = g_null(final). Override: "g_null OVERRIDE: [justification]"
  Note: g_null_lifecycle=FAIL forces g_null(final)=FAIL regardless of G_lifecycle.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps surfaces to findings. GAP -> ADVISORY-GAP. Also runs §10a.

§10a -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  Step 1: Group §1 surfaces into ARTIFACT DOMAINS.
  Step 2: APPLICABILITY MATRIX rows where domain matches AND Applicability=HIGH.
  Step 3: COVERED or ADVISORY-GAP.
  Step 4: ADVISORY-GAP -> ACTION ITEM REGISTER (Class: ADVISORY).
  Table: | Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |

§11 -- FINDING-SURFACE LINKAGE [IMMUTABLE]
  Each finding: "[§1:S-n]". Missing -> ADVISORY-ORPHAN -> register.

§12 -- CONDITIONAL RESOLUTION REGISTRY [IMMUTABLE]
  CONDITIONAL -> RESOLUTION REGISTRY. Else: "N/A -- [value]"

§13 -- g_null PROGRESSION LEDGER [IMMUTABLE -- v1-LC: four signals]
  §13 PROGRESSION LEDGER in CROSS-ROLE SIGNALS:
    g_null(initial) | g_null(post-domain) | g_null_lifecycle | g_null(final) | Trajectory
  Labels: MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
          LIFECYCLE-NH-BLOCKED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED.

§14 -- FINDING SEVERITY AGGREGATION [IMMUTABLE]
  | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all). No findings = LOW.

§15 -- LENS EXHAUSTION [IMMUTABLE]
  All lens.verify addressed. LENS COVERAGE TABLE:
    | # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
  Cite APPLICABILITY MATRIX row ID + tier. Value locked.
  HIGH+OPEN -> ADVISORY-OPEN-LENS-REQUIRED. MEDIUM+OPEN -> ADVISORY-OPEN-LENS.
  LOW+OPEN -> cite AM row; no register entry.

§16 -- PRIMARY DRIVER DERIVATION [IMMUTABLE]
  1. GClose=FAIL -> BRACKET CLOSING
  2. G_domain_agg=FAIL -> DOMAIN
  3. G_lifecycle=FAIL -> LIFECYCLE
  4. GOpen=FAIL -> BRACKET OPENING
  5-8: same for CONDITIONAL in order above.
  9. all PASS -> N/A
  Emit: **Applying §16 rule**: [n]  **Primary Driver**: [result]

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]
  BRACKET OPENING: per-dimension NH table before challenge claims.
  | Dimension | Current-State (0-10) | Proposed-State (0-10) | Differential | NH Verdict |
  MUST-CLEAR (*). Min 3 dimensions. FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD.
  g_null rule: HOLDS / CONDITIONAL / DEFEATED.
  BRACKET CLOSING re-applies to revised aggregate table.
  §4a LIFECYCLE NH TABLE uses same format and rule with commitment-readiness dimensions.

======================================================================
END DISPOSITION_CONTRACT v1-LC
======================================================================
```

---

## ROLE MANIFEST

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

### APPLICABILITY MATRIX

*(Complete before BRACKET OPENING. Locked on completion.)*

| Row ID | Role | lens.verify Entry | Artifact Domain Covered | Artifact Applicability | Basis for Rating |
|--------|------|------------------|------------------------|----------------------|------------------|
| AM-01 | [DOMAIN] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [sentence] |
| AM-02 | [DOMAIN] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [sentence] |
| AM-03 | [DOMAIN] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [sentence] |
| AM-04 | [LIFECYCLE] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [sentence] |
| AM-05 | [LIFECYCLE] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [sentence] |

*(Add rows for every lens.verify entry. Matrix locked.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1-LC

**Null hypothesis**: [One sentence -- what team does today instead of building this.]

**Alternatives comparison table** *(>= 3 dimensions)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17)*:

| Dimension | Current-State (0-10) | Proposed-State (0-10) | Differential | NH Verdict |
|-----------|--------------------|-----------------------|--------------|------------|
| [DIM-A*]  | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

*(Dimensions marked * are MUST-CLEAR.)*

```
MUST-CLEAR OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD) = [N] | count(OPPOSES-BUILD) = [N]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null(initial)** *(§9 Stage 1)*: [copy result]

**Challenge claims**:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [H/M/L] |
| CH-002 | [CLAIM_2] | [H/M/L] |
| CH-003 | [CLAIM_3 -- optional] | [H/M/L] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)**: [copy]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-LC
Received GOpen: [copy]

**CH-ID Response Table**:

| CH-ID | Claim (copy) | Technical Response | Status |
|-------|-------------|-------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Domain re-score**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| [DIM-1] | [revised] | [revised] | [revised] | [reason] |
| [DIM-2] | [revised] | [revised] | [revised] | |
| [DIM-3] | [revised] | [revised] | [revised] | |

**Findings**:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING] | [H/M/L] |
| F-2 | [§1:S-n] | [FINDING] | [H/M/L] |

```
Section Severity = worst([]) = [H/M/L]
```

**Lens Coverage Table**:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [text] | AM-01: [H/M/L] | [ADDRESSED / OPEN] | [F-n or cite] |
| Q-2 | [text] | AM-02: [H/M/L] | [ADDRESSED / OPEN] | [F-n or cite] |
| Q-3 | [text] | AM-03: [H/M/L] | [ADDRESSED / OPEN] | [F-n or cite] |

**Recommendation**: [One concrete action.]
**Simplify**: [One from lens.simplify.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger.)*

```
G_domain_agg = worst([G_domain verdict(s)]) = [PASS / CONDITIONAL / FAIL]
g_null(initial) = [copy] | G_domain_agg = [copy]
g_null(post-domain) = [result]
```
**g_null(post-domain)**: [FAIL / CONDITIONAL / PASS]

---

## §3.8 CH-ID SATURATION CHECK

| CH-ID | DOMAIN Status | Pre-LIFECYCLE Saturation |
|-------|--------------|--------------------------|
| CH-001 | [copy] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED] |

**Pre-LIFECYCLE unsaturated**: [List or "None"]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-LC
Received GOpen: [copy]
Received G_domain_agg: [copy from §3.5]
Received g_null(post-domain): [copy from §3.5]

**CH-ID Response Table**:

| CH-ID | Claim (copy) | Commitment-Frame Response | Status |
|-------|-------------|--------------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph. Reference GOpen, G_domain_agg, g_null(post-domain).]

### §4a NULL HYPOTHESIS LIFECYCLE ASSESSMENT *(per §9 Stage 2b and §17)*

*(Evaluate whether the null hypothesis holds from a commitment-readiness perspective.
Use dimensions distinct from BRACKET OPENING -- these are program and roadmap signals.
Apply the §17 g_null derivation rule mechanically.)*

**Commitment-readiness NH dimensions**:

| Dimension | Current-State (0-10) | Proposed-State (0-10) | Differential | NH Verdict |
|-----------|--------------------|-----------------------|--------------|------------|
| [LC-DIM-A* -- roadmap fit] | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [LC-DIM-B* -- team capacity] | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [LC-DIM-C -- timeline alignment] | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

*(Dimensions marked * are MUST-CLEAR for lifecycle NH derivation. Add rows as needed.)*

```
LC MUST-CLEAR OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD) = [N] | count(OPPOSES-BUILD) = [N]
Applying §17 rule to commitment dimensions:
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null_lifecycle** *(§9 Stage 2b -- informational signal)*: [HOLDS / CONDITIONAL / DEFEATED]

*(If g_null_lifecycle=HOLDS: per §9, this forces g_null(final)=FAIL at BRACKET CLOSING
regardless of G_lifecycle verdict. State this explicitly if applicable.)*

**Null hypothesis status**: [yes / partial / no -- reference both g_null(post-domain) and g_null_lifecycle.]

**Additional Findings**:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING] | [H/M/L] |
| F-2 | [§1:S-n] | [FINDING] | [H/M/L] |

```
Section Severity = worst([]) = [H/M/L]
```

**Lens Coverage Table**:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [text] | AM-04: [H/M/L] | [ADDRESSED / OPEN] | [F-n or cite] |
| Q-2 | [text] | AM-05: [H/M/L] | [ADDRESSED / OPEN] | [F-n or cite] |

**Recommendation**: [One concrete action.]
**Simplify**: [One from lens.simplify.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence. If g_null_lifecycle=HOLDS and G_lifecycle!=FAIL:
state that g_null_lifecycle forces g_null(final)=FAIL per §9.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1-LC
*Full record received: scope, APPLICABILITY MATRIX, all CH-ID tables, all verdicts.*

```
g_null(post-domain) = [copy from §3.5]
G_lifecycle         = [copy from LIFECYCLE ledger]
g_null_lifecycle    = [copy from §4a]
Applying §9 Stage 3:
  G_lifecycle path: [describe FAIL/CONDITIONAL/PASS application]
  Interim g_null(final) = [result]
  g_null_lifecycle=FAILS override: [APPLIES -- g_null(final) forced to FAIL | NOT APPLICABLE]
g_null(final) = [final result]
```
**g_null(final)**: [FAIL / CONDITIONAL / PASS]
*GClose must equal g_null(final) per §9.*

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(per §17 -- aggregate all re-scores)*:

| Dimension | Current-State (0-10) | Proposed-State (0-10) | Differential | NH Verdict |
|-----------|--------------------|-----------------------|--------------|------------|
| [DIM-A*]  | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

```
count(FAVORS-BUILD) = [N] | count(OPPOSES-BUILD) = [M]
Revised result: [HOLDS / CONDITIONAL / DEFEATED]
```

**Revised alternatives table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Agg Rationale |
|-----------|---------------|-----------|----------------------|--------------|
| [DIM-1] | [agg] | [agg] | [agg] | [reason] |
| [DIM-2] | [agg] | [agg] | [agg] | |

**Full CH-ID Saturation Check** *(per §8)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver |
|-------|--------------|-----------------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |

**CH-ID Final Assessment**:

| CH-ID | G_domain | G_lifecycle | Final Status | Notes |
|-------|---------|------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A -- formula applied | or: justification]
**GClose Rationale**: [2-3 sentences. Note g_null_lifecycle trajectory if HOLDS/CONDITIONAL.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger. Applies §10, §10a, §11.)*

### Surface Coverage

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [SURFACE_1] | [ROLE] | [F-n] | [COVERED / GAP] |
| [SURFACE_2] | [ROLE] | [F-n] | [COVERED / GAP] |
| [SURFACE_3] | [ROLE] | [F-n] | [COVERED / GAP] |

**Surface coverage gate signal**: [COVERED / PARTIAL]

### Domain Coverage Gap-Check *(per §10a)*

| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|----------|
| [DOMAIN-1] | [AM-0n: [ROLE] -- "[lens summary]" / "none"] | [COVERED / ADVISORY-GAP] |
| [DOMAIN-2] | [AM-0n / "none"] | [COVERED / ADVISORY-GAP] |

**§11 ADVISORY-ORPHAN check**: [List or "None detected."]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER] | [copy] | DISPOSITION_CONTRACT v1-LC |
| G_domain_agg | [DOMAIN] | [copy] | DISPOSITION_CONTRACT v1-LC |
| G_lifecycle | [LIFECYCLE] | [copy] | DISPOSITION_CONTRACT v1-LC |
| GClose | [CHALLENGER] | [copy] | DISPOSITION_CONTRACT v1-LC |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Or "None detected."]
**Convergence**: [Independent findings from 2+ reviewers. Name highest-confidence signal.]
**Scope coverage**: [Uncovered surfaces or "None."]

**§13 PROGRESSION LEDGER**:
```
g_null(initial)       = [copy from BRACKET OPENING §17]
g_null(post-domain)   = [copy from §3.5]
g_null_lifecycle      = [copy from §4a -- lifecycle NH signal]
g_null(final)         = [copy from BRACKET CLOSING §9 Stage 3]
Trajectory: [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
             LIFECYCLE-NH-BLOCKED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```
*Trajectory is informational. No gate ledger row emitted.*

---

## DISPOSITION

**Gate vector**:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose=FAIL? -> BLOCKED
Any Gi=FAIL? -> BLOCKED
No FAIL, any CONDITIONAL? -> CONDITIONAL
All PASS? -> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Applying §16 rule**: [rule number + reason]
**Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**Conditions** *(CONDITIONAL only)*:
1. [Condition from first CONDITIONAL gate.]

**Blocker** *(BLOCKED only)*: [Specific finding from FAIL gate.]

**RESOLUTION REGISTRY** *(CONDITIONAL only)*:
| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [one sentence] | [role] | [falsifiable test] | OPEN |

*If not CONDITIONAL: "RESOLUTION REGISTRY: N/A -- disposition is [value]"*

---

## ACTION ITEM REGISTER

| Source | CH-ID / Finding | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|--------|----------------|-----------------|------------------|------------|---------------------|
| [gate ledger copy] | -- | [verbatim Section / Gate / Verdict / Class] | [class] | [ROLE] | [criterion] |
| [CH-ID] | CH-00n | [action required] | [class] | [ROLE] | [criterion] |
| [lens HIGH OPEN] | AM-0n / Q-n | ADVISORY-OPEN-LENS-REQUIRED: [entry] | ADVISORY | [ROLE] | Produce finding. |
| [lens MED OPEN] | AM-0n / Q-n | ADVISORY-OPEN-LENS: [entry] | ADVISORY | [ROLE] | Address or justify. |
| [scope gap] | -- | ADVISORY-GAP: §1 surface [name] not covered | ADVISORY | [ROLE] | Assign reviewer. |
| [domain gap] | -- | ADVISORY-GAP (DOMAIN COVERAGE): [domain] no HIGH reviewer | ADVISORY | [ROLE] | Add reviewer or justify. |

---

**Artifact to review:**

{{artifact}}

---
---

## V-04 -- Combined: Phrasing Register (Imperative) + Inertia Framing (NH Front-loaded)

**Variation axes**: (1) Phrasing register -- imperative/directive field labels throughout;
(2) Inertia framing -- NULL HYPOTHESIS stated as a STANDING ASSUMPTION in §1 before scope
enumeration; all reviewer section headers framed as responses to the null hypothesis.

**Hypothesis**: Placing the null hypothesis as a standing assumption before scope enumeration
changes the epistemic stance of all downstream evaluations. Domain and lifecycle roles
respond TO the null hypothesis rather than generating independent findings that only
indirectly address it. The challenger is no longer a special-case section -- the null
hypothesis challenge is the organizing frame of the entire review. Imperative field labels
("State the ...", "Identify all ...", "Apply mechanically ...") reduce ambiguous field fills
compared to descriptive labels.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

**Instructions**: Complete every field. Do not alter, reorder, or omit any heading, label,
formula, or structural element. If a field cannot be completed, write `[N/A -- reason]`.
Every section responds to the standing null hypothesis stated in §0.

---

```
======================================================================
DISPOSITION_CONTRACT v1-IF (inertia-framing variant)
[IMMUTABLE BLOCK -- complete §0 null hypothesis and §1 scope fields;
do not alter §2-§17; reviewer sections may not execute until
§1 COMPLETE marker is reached]
======================================================================

§0 -- STANDING NULL HYPOTHESIS [NEW -- complete before §1]
  State the null hypothesis in one sentence:
  NULL HYPOTHESIS: [What the team does today instead of building this. One sentence.]

  This is the standing assumption of the review. Every reviewer section challenges or
  confirms this assumption from their frame. The review is complete when the null hypothesis
  has been evaluated by all roles and a final verdict emitted.

§1 -- SCOPE ENUMERATION
  The following surfaces are the evidence pool for defeating or confirming the null hypothesis:
  IN-SCOPE:
    1. [SURFACE_1]
    2. [SURFACE_2]
    3. [SURFACE_3]
    (Add rows. Be exhaustive.)

  OUT-OF-SCOPE:
    1. [SURFACE -- REASON_EXCLUDED]

  Scope Amendment Protocol:
    SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]

§1 COMPLETE -- role selection, APPLICABILITY MATRIX, and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions commitment. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED <-- GClose=FAIL OR exists Gi=FAIL
  CONDITIONAL <-- no FAIL AND exists CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain rows). Single domain: direct pass-through.

§4 -- CONTRACT CITE [IMMUTABLE]
  Each reviewer section: "Contract: DISPOSITION_CONTRACT v1-IF"

§5 -- CH-ID TRACING [IMMUTABLE]
  BRACKET OPENING claims -> CH-IDs. Every downstream section: mandatory CH-ID response table.
  PASS prohibited if any CH-ID OPEN.

§6 -- LOCAL GATE LEDGER [IMMUTABLE]
  Row: | Section | Gate | Verdict | Class |
  FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  EXCLUDED: §3.5, §3.8, §5.5.

§7 -- SECTION ORDER [IMMUTABLE]
  1. ROLE MANIFEST (APPLICABILITY MATRIX required before BRACKET OPENING)
  2. BRACKET OPENING -- NULL HYPOTHESIS CHALLENGE
  3. DOMAIN(s) -- NULL HYPOTHESIS DOMAIN RESPONSE
  3.5. DOMAIN-AGGREGATE CHECKPOINT
  3.8. CH-ID SATURATION CHECK
  4. LIFECYCLE -- NULL HYPOTHESIS COMMITMENT RESPONSE
  5. BRACKET CLOSING -- NULL HYPOTHESIS FINAL VERDICT
  5.5. SCOPE COVERAGE RECONCILIATION
  6. GATE VECTOR TABLE
  7. CROSS-ROLE SIGNALS
  8. DISPOSITION
  9. ACTION ITEM REGISTER

§8 -- CH-ID SATURATION [IMMUTABLE]
  FULLY SATURATED: DOMAIN + LIFECYCLE responses before BRACKET CLOSING.
  PASS prohibited without full saturation or stated waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = §17 formula output [BRACKET OPENING]
  Stage 2: g_null(post-domain) [§3.5]:
    G_domain_agg=FAIL        -> FAIL
    G_domain_agg=CONDITIONAL -> max(g_null(initial), CONDITIONAL)
    G_domain_agg=PASS        -> g_null(initial)
  Stage 3: g_null(final) [BRACKET CLOSING]:
    G_lifecycle=FAIL         -> FAIL
    G_lifecycle=CONDITIONAL  -> max(g_null(post-domain), CONDITIONAL)
    G_lifecycle=PASS         -> g_null(post-domain)
  GClose = g_null(final). Override: "g_null OVERRIDE: [justification]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps surfaces to findings. GAP -> ADVISORY-GAP. Also runs §10a.

§10a -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  Step 1: Group §1 surfaces into ARTIFACT DOMAINS.
  Step 2: APPLICABILITY MATRIX rows where domain matches AND Applicability=HIGH.
  Step 3: COVERED or ADVISORY-GAP.
  Step 4: ADVISORY-GAP -> ACTION ITEM REGISTER (Class: ADVISORY).
  Table: | Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |

§11 -- FINDING-SURFACE LINKAGE [IMMUTABLE]
  Each finding: "[§1:S-n]". Missing -> ADVISORY-ORPHAN -> register.

§12 -- CONDITIONAL RESOLUTION REGISTRY [IMMUTABLE]
  CONDITIONAL -> RESOLUTION REGISTRY. Else: "N/A -- [value]"

§13 -- g_null PROGRESSION LEDGER [IMMUTABLE]
  §13 PROGRESSION LEDGER in CROSS-ROLE SIGNALS:
    g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory
  Labels: MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
          DOMAIN-RECOVERED / LIFECYCLE-RECOVERED.

§14 -- FINDING SEVERITY AGGREGATION [IMMUTABLE]
  | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all). No findings = LOW.

§15 -- LENS EXHAUSTION [IMMUTABLE]
  All lens.verify addressed. LENS COVERAGE TABLE:
    | # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
  Cite APPLICABILITY MATRIX row ID + tier. Value locked from ROLE MANIFEST.
  HIGH+OPEN -> ADVISORY-OPEN-LENS-REQUIRED. MEDIUM+OPEN -> ADVISORY-OPEN-LENS.
  LOW+OPEN -> cite AM row; no register entry.

§16 -- PRIMARY DRIVER DERIVATION [IMMUTABLE]
  1. GClose=FAIL -> BRACKET CLOSING
  2. G_domain_agg=FAIL -> DOMAIN
  3. G_lifecycle=FAIL -> LIFECYCLE
  4. GOpen=FAIL -> BRACKET OPENING
  5-8: same for CONDITIONAL.
  9. all PASS -> N/A
  Emit: **Applying §16 rule**: [n]  **Primary Driver**: [result]

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]
  BRACKET OPENING: per-dimension NH table before challenge claims.
  | Dimension | Current-State (0-10) | Proposed-State (0-10) | Differential | NH Verdict |
  MUST-CLEAR (*). Min 3 dimensions. FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD.
  g_null rule: HOLDS / CONDITIONAL / DEFEATED.
  BRACKET CLOSING re-applies to revised aggregate table.

======================================================================
END DISPOSITION_CONTRACT v1-IF
======================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3.)*

### APPLICABILITY MATRIX

*(Complete this matrix before BRACKET OPENING. It is locked on completion and may not be
modified by any downstream section.)*

| Row ID | Role | lens.verify Entry | Artifact Domain Covered | Artifact Applicability | Basis for Rating |
|--------|------|------------------|------------------------|----------------------|------------------|
| AM-01 | [DOMAIN] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-02 | [DOMAIN] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-03 | [DOMAIN] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-04 | [LIFECYCLE] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-05 | [LIFECYCLE] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [One sentence] |

*(Add rows for every lens.verify entry from every assigned role. Matrix locked.)*

---

## BRACKET OPENING -- NULL HYPOTHESIS CHALLENGE

Contract: DISPOSITION_CONTRACT v1-IF

**Confirm the standing null hypothesis from §0**:
NULL HYPOTHESIS (confirmed): [Copy from §0. One sentence.]

**Dimension table for the null hypothesis** *(per §17 -- apply mechanically)*:

| Dimension | Current-State (0-10) | Proposed-State (0-10) | Differential | NH Verdict |
|-----------|--------------------|-----------------------|--------------|------------|
| [DIM-A* -- name the dimension] | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B* -- name the dimension] | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C -- name the dimension]  | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

*(Mark MUST-CLEAR dimensions with *. Add rows as needed.)*

**Derive g_null(initial) -- apply §17 rule mechanically**:
```
State each MUST-CLEAR dimension and its NH Verdict: [list]
MUST-CLEAR OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD) = [N]
count(NEUTRAL)      = [N]
count(OPPOSES-BUILD) = [N]
Apply rule: HOLDS / CONDITIONAL / DEFEATED -> [result]
```
**g_null(initial)** *(§9 Stage 1)*: [HOLDS / CONDITIONAL / DEFEATED]

**Compare alternatives** *(>= 3 dimensions; distinct from §17 NH table above)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**State challenge claims that must be defeated for the build to proceed** *(assign CH-IDs)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [State what evidence would need to be true to defeat this claim.] | [H/M/L] |
| CH-002 | [State the claim.] | [H/M/L] |
| CH-003 | [State the claim -- optional if warranted.] | [H/M/L] |

**State one verify question from your lens**: [Question.]
**State one simplify question from your lens**: [Question.]

**Emit gate verdict consistent with g_null(initial)**:
GOpen Verdict: [PASS / CONDITIONAL / FAIL]
GOpen Reason: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- NULL HYPOTHESIS DOMAIN RESPONSE: [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-IF
Received GOpen: [copy]
Received standing null hypothesis: [copy from §0]

**Respond to each challenge claim**:

| CH-ID | Challenge Claim (copy) | Technical Response to this Challenge | Status |
|-------|----------------------|-------------------------------------|--------|
| CH-001 | [copy] | [State your technical response.] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [State your technical response.] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [State your technical response.] | [ADDRESSED / PARTIAL / OPEN] |

*(PARTIAL: state the resolution path. OPEN: state why this is outside your technical frame.)*

**Revise the alternative scores based on technical evidence**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Technical Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| [DIM-1] | [revised] | [revised] | [revised] | [State evidence.] |
| [DIM-2] | [revised] | [revised] | [revised] | |
| [DIM-3] | [revised] | [revised] | [revised] | |

**Identify findings that bear on the null hypothesis**:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [State finding. Explain how it bears on the null hypothesis.] | [H/M/L] |
| F-2 | [§1:S-n] | [State finding.] | [H/M/L] |

**Aggregate finding severity -- apply mechanically**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**Confirm lens coverage for every lens.verify entry**:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [Full text] | AM-01: [H/M/L] | [ADDRESSED / OPEN] | [F-n or cite AM-01] |
| Q-2 | [Full text] | AM-02: [H/M/L] | [ADDRESSED / OPEN] | [F-n or cite AM-02] |
| Q-3 | [Full text] | AM-03: [H/M/L] | [ADDRESSED / OPEN] | [F-n or cite AM-03] |

**State one concrete recommendation**: [Recommendation.]
**State one simplify question**: [Question from lens.simplify.]

**Emit domain gate verdict**:
G_domain Verdict: [PASS / CONDITIONAL / FAIL]
G_domain Reason: [One sentence referencing the null hypothesis.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger.)*

**Aggregate domain verdicts -- apply §3a mechanically**:
```
G_domain_agg = worst([G_domain verdict(s)]) = [PASS / CONDITIONAL / FAIL]
```
**G_domain_agg**: [PASS / CONDITIONAL / FAIL]

**Propagate null hypothesis -- apply §9 Stage 2 mechanically**:
```
g_null(initial) = [copy] | G_domain_agg = [copy]
g_null(post-domain) = [result]
```
**g_null(post-domain)**: [FAIL / CONDITIONAL / PASS]

---

## §3.8 CH-ID SATURATION CHECK

| CH-ID | DOMAIN Response | Pre-LIFECYCLE Saturation |
|-------|----------------|--------------------------|
| CH-001 | [copy status] | [SATURATED / UNSATURATED] |
| CH-002 | [copy status] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None"]

---

## LIFECYCLE -- NULL HYPOTHESIS COMMITMENT RESPONSE: [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-IF
Received GOpen: [copy]
Received G_domain_agg: [copy]
Received g_null(post-domain): [copy]
Received standing null hypothesis: [copy from §0]

**Respond to each challenge claim from a commitment-readiness frame**:

| CH-ID | Challenge Claim (copy) | Commitment-Frame Response | Status |
|-------|----------------------|--------------------------|--------|
| CH-001 | [copy] | [State your commitment-frame response.] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [State your commitment-frame response.] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [State your response.] | [ADDRESSED / PARTIAL / OPEN] |

**Assess decision-readiness** *(reference GOpen, G_domain_agg, g_null(post-domain) explicitly)*:
[One paragraph.]

**State the null hypothesis status from your frame** *(reference g_null(post-domain))*:
[yes / partial / no -- one sentence.]

**Identify findings that bear on commitment to proceed**:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [State finding referencing null hypothesis.] | [H/M/L] |
| F-2 | [§1:S-n] | [State finding.] | [H/M/L] |

```
Section Severity = worst([]) = [H/M/L]
```

**Confirm lens coverage**:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [Full text] | AM-04: [H/M/L] | [ADDRESSED / OPEN] | [F-n or cite AM-04] |
| Q-2 | [Full text] | AM-05: [H/M/L] | [ADDRESSED / OPEN] | [F-n or cite AM-05] |

**State one concrete recommendation**: [Recommendation.]
**State one simplify question**: [Question.]

**Emit lifecycle gate verdict**:
G_lifecycle Verdict: [PASS / CONDITIONAL / FAIL]
G_lifecycle Reason: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## BRACKET CLOSING -- NULL HYPOTHESIS FINAL VERDICT

Contract: DISPOSITION_CONTRACT v1-IF
*Full record received. Apply §9 Stage 3 mechanically to derive g_null(final). GClose must match.*

**Derive g_null(final) -- apply §9 Stage 3 mechanically**:
```
g_null(post-domain) = [copy from §3.5]
G_lifecycle         = [copy from LIFECYCLE ledger]
Apply: FAIL->FAIL | CONDITIONAL->max(post-domain,CONDITIONAL) | PASS->g_null(post-domain)
g_null(final) = [result]
```
**g_null(final)**: [FAIL / CONDITIONAL / PASS]

**Re-evaluate the null hypothesis with revised scores** *(per §17)*:

| Dimension | Current-State (0-10) | Proposed-State (0-10) | Differential | NH Verdict |
|-----------|--------------------|-----------------------|--------------|------------|
| [DIM-A*]  | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

```
count(FAVORS-BUILD) = [N] | count(OPPOSES-BUILD) = [M]
Revised §17 result: [HOLDS / CONDITIONAL / DEFEATED]
```

**Revise the alternatives comparison**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Aggregate Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| [DIM-1] | [agg] | [agg] | [agg] | [State reason.] |
| [DIM-2] | [agg] | [agg] | [agg] | |

**Confirm full CH-ID saturation -- apply §8 mechanically**:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver |
|-------|--------------|-----------------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |

**State the final status of each challenge claim**:

| CH-ID | G_domain | G_lifecycle | Final Status | Notes |
|-------|---------|------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |

**Remaining undefeated claims**: [All defeated, or list.]

**Emit GClose consistent with g_null(final)**:
GClose Verdict: [PASS / CONDITIONAL / FAIL]
Override invoked: [YES / NO]
g_null Override: [N/A -- formula applied | or: state justification]
GClose Rationale: [2-3 sentences. State whether the null hypothesis was ultimately defeated,
conditional, or holds. Reference g_null trajectory.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger. Applies §10, §10a, §11.)*

### Surface Coverage *(per §10)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [SURFACE_1] | [ROLE or "none"] | [F-n or "none"] | [COVERED / GAP] |
| [SURFACE_2] | [ROLE or "none"] | [F-n or "none"] | [COVERED / GAP] |
| [SURFACE_3] | [ROLE or "none"] | [F-n or "none"] | [COVERED / GAP] |

**Surface coverage gate signal**: [COVERED / PARTIAL]

### Domain Coverage Gap-Check *(per §10a)*

| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|----------|
| [DOMAIN-1] | [AM-0n: [ROLE] -- "[lens summary]" / "none"] | [COVERED / ADVISORY-GAP] |
| [DOMAIN-2] | [AM-0n / "none"] | [COVERED / ADVISORY-GAP] |

**§11 ADVISORY-ORPHAN check**: [List or "None detected."]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER] | [copy] | DISPOSITION_CONTRACT v1-IF |
| G_domain_agg | [DOMAIN] | [copy] | DISPOSITION_CONTRACT v1-IF |
| G_lifecycle | [LIFECYCLE] | [copy] | DISPOSITION_CONTRACT v1-IF |
| GClose | [CHALLENGER] | [copy] | DISPOSITION_CONTRACT v1-IF |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Two reviewers with incompatible CH-ID responses. "None detected." if none.]
**Convergence**: [Any concern named independently by two or more reviewers. State why it is the
highest-confidence null hypothesis signal in this review.]
**Scope coverage**: [Uncovered §1 surfaces or "None."]

**§13 PROGRESSION LEDGER**:
```
g_null(initial)     = [copy from BRACKET OPENING §17]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING §9 Stage 3]
Trajectory: [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
             DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

---

## DISPOSITION

**Gate vector**:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply §3 formula mechanically -- do not reason editorially**:
```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose=FAIL? -> BLOCKED (null hypothesis holds -- challenger override)
Any other Gi=FAIL? -> BLOCKED
No FAIL, any CONDITIONAL? -> CONDITIONAL
All PASS? -> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Apply §16 rule mechanically**:
Applying §16 rule: [rule number + reason]
Primary Driver: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**State conditions** *(CONDITIONAL only)*:
1. [State condition precisely.]

**State blocker** *(BLOCKED only)*:
[Name the specific finding from the FAIL gate. If GClose=FAIL: state the null hypothesis
remains undefeated and reference GClose Rationale.]

**RESOLUTION REGISTRY** *(CONDITIONAL only)*:
| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [one sentence] | [role] | [falsifiable test] | OPEN |

*If not CONDITIONAL: "RESOLUTION REGISTRY: N/A -- disposition is [value]"*

---

## ACTION ITEM REGISTER

*Copy all local gate ledger rows verbatim. Add CH-ID items, ADVISORY-OPEN-LENS items,
ADVISORY-GAP items, ADVISORY-ORPHAN items.*

| Source | CH-ID / Finding | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|--------|----------------|-----------------|------------------|------------|---------------------|
| [gate ledger] | -- | [verbatim Section / Gate / Verdict / Class] | [class] | [ROLE] | [criterion] |
| [CH-ID item] | CH-00n | [State what must be done.] | [class] | [ROLE] | [criterion] |
| [lens HIGH OPEN] | AM-0n / Q-n | ADVISORY-OPEN-LENS-REQUIRED: [entry] not addressed | ADVISORY | [ROLE] | Produce finding. |
| [lens MED OPEN] | AM-0n / Q-n | ADVISORY-OPEN-LENS: [entry] not addressed | ADVISORY | [ROLE] | Address or justify. |
| [scope gap] | -- | ADVISORY-GAP: §1 surface [name] not covered | ADVISORY | [ROLE] | Assign reviewer. |
| [domain gap] | -- | ADVISORY-GAP (DOMAIN COVERAGE): [domain] no HIGH reviewer | ADVISORY | [ROLE] | Add reviewer or justify. |

---

**Artifact to review:**

{{artifact}}

---
---

## V-05 -- Full Integration: Lifecycle-First + NH Sub-Eval + Inertia Front-loading

**Variation axes**: (1) Role sequence -- LIFECYCLE before DOMAIN (from V-01);
(2) Lifecycle emphasis -- §4a NULL HYPOTHESIS LIFECYCLE ASSESSMENT sub-section (from V-03);
(3) Inertia framing -- NULL HYPOTHESIS as STANDING ASSUMPTION in §0, all section headers
framed as null hypothesis responses (from V-04).

**Hypothesis**: Full combination maximizes null hypothesis signal density. Inertia front-loading
(§0 NH statement before scope) + lifecycle-first ordering means the strongest commitment
blockers are evaluated first. The §4a lifecycle NH sub-evaluation runs BEFORE domain, meaning
g_null_lifecycle can alert the challenger before domain evidence is weighted. Combined with
g_null four-stage progression and imperative phrasing, this produces the richest possible
g_null trajectory and surfaces LIFECYCLE-NH-BLOCKED as a first-class pattern visible from
the progression ledger alone. §13 carries five signals: initial, post-lifecycle, g_null_lifecycle,
post-domain-final, and final.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

**Instructions**: Complete every field. Do not alter, reorder, or omit any heading, label,
formula, or structural element. If a field cannot be completed, write `[N/A -- reason]`.
Every section responds to the standing null hypothesis stated in §0.

---

```
======================================================================
DISPOSITION_CONTRACT v1-FI (full-integration variant)
[IMMUTABLE BLOCK -- complete §0 null hypothesis and §1 scope fields;
do not alter §2-§17; reviewer sections may not execute until
§1 COMPLETE marker is reached]
======================================================================

§0 -- STANDING NULL HYPOTHESIS [complete before §1]
  NULL HYPOTHESIS: [What the team does today instead of building this. One sentence.]
  This standing assumption governs the entire review. All roles respond to it.

§1 -- SCOPE ENUMERATION
  IN-SCOPE:
    1. [SURFACE_1]
    2. [SURFACE_2]
    3. [SURFACE_3]
    (Add rows. Be exhaustive.)

  OUT-OF-SCOPE:
    1. [SURFACE -- REASON_EXCLUDED]

  Scope Amendment Protocol:
    SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]

§1 COMPLETE -- role selection, APPLICABILITY MATRIX, and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks. MEDIUM = Conditions. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_lifecycle, G_domain_agg, GClose}
  BLOCKED <-- GClose=FAIL OR exists Gi=FAIL
  CONDITIONAL <-- no FAIL AND exists CONDITIONAL
  READY <-- all PASS

§3a -- LIFECYCLE value [IMMUTABLE -- full-integration variant]
  G_lifecycle from the single lifecycle reviewer is used directly.
  (deep: G_lifecycle_agg = worst(all G_lifecycle rows).)

§3b -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain rows). Single domain: direct pass-through.

§4 -- CONTRACT CITE [IMMUTABLE]
  Each reviewer section: "Contract: DISPOSITION_CONTRACT v1-FI"

§5 -- CH-ID TRACING [IMMUTABLE]
  BRACKET OPENING claims -> CH-IDs. Every downstream section: mandatory CH-ID response table.
  PASS prohibited if any CH-ID OPEN.

§6 -- LOCAL GATE LEDGER [IMMUTABLE]
  Row: | Section | Gate | Verdict | Class |
  FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  EXCLUDED: §3.5L, §3.8, §4.5, §5.5.

§7 -- SECTION ORDER [IMMUTABLE -- full-integration variant]
  1. ROLE MANIFEST (APPLICABILITY MATRIX required before BRACKET OPENING)
  2. BRACKET OPENING -- NULL HYPOTHESIS CHALLENGE
  3. LIFECYCLE -- NULL HYPOTHESIS COMMITMENT RESPONSE (includes §3a NH sub-section)
  3.5L. LIFECYCLE-AGGREGATE CHECKPOINT
  3.8. CH-ID SATURATION CHECK (pre-domain)
  4. DOMAIN(s) -- NULL HYPOTHESIS DOMAIN RESPONSE
  4.5. DOMAIN-AGGREGATE CHECKPOINT
  5. BRACKET CLOSING -- NULL HYPOTHESIS FINAL VERDICT
  5.5. SCOPE COVERAGE RECONCILIATION
  6. GATE VECTOR TABLE
  7. CROSS-ROLE SIGNALS
  8. DISPOSITION
  9. ACTION ITEM REGISTER

§8 -- CH-ID SATURATION [IMMUTABLE]
  FULLY SATURATED: LIFECYCLE + DOMAIN responses before BRACKET CLOSING.
  PASS prohibited without full saturation or stated waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE -- full-integration: five signals]
  Stage 1: g_null(initial) = §17 formula output [BRACKET OPENING]
  Stage 2: g_null(post-lifecycle) [§3.5L]:
    G_lifecycle=FAIL        -> FAIL
    G_lifecycle=CONDITIONAL -> max(g_null(initial), CONDITIONAL)
    G_lifecycle=PASS        -> g_null(initial)
  Stage 2b: g_null_lifecycle [§3a NH sub-section]:
    Derived from lifecycle NH TABLE using §17 rule on commitment dimensions.
    Informational signal. Feeds Stage 3 override rule.
  Stage 3: g_null(post-domain-final) [§4.5]:
    G_domain_agg=FAIL        -> FAIL
    G_domain_agg=CONDITIONAL -> max(g_null(post-lifecycle), CONDITIONAL)
    G_domain_agg=PASS        -> g_null(post-lifecycle)
    THEN: if g_null_lifecycle=FAIL AND g_null(post-domain-final)!=FAIL
          -> g_null(post-domain-final)=FAIL with note
  Stage 4: g_null(final) [BRACKET CLOSING]:
    = g_null(post-domain-final) unless g_null OVERRIDE.
  GClose = g_null(final). Override: "g_null OVERRIDE: [justification]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps surfaces. GAP -> ADVISORY-GAP. Also runs §10a.

§10a -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  Step 1: Group §1 surfaces into ARTIFACT DOMAINS.
  Step 2: APPLICABILITY MATRIX rows where domain matches AND Applicability=HIGH.
  Step 3: COVERED or ADVISORY-GAP.
  Step 4: ADVISORY-GAP -> ACTION ITEM REGISTER (Class: ADVISORY).
  Table: | Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |

§11 -- FINDING-SURFACE LINKAGE [IMMUTABLE]
  Each finding: "[§1:S-n]". Missing -> ADVISORY-ORPHAN -> register.

§12 -- CONDITIONAL RESOLUTION REGISTRY [IMMUTABLE]
  CONDITIONAL -> RESOLUTION REGISTRY. Else: "N/A -- [value]"

§13 -- g_null PROGRESSION LEDGER [IMMUTABLE -- full-integration: five signals]
  §13 PROGRESSION LEDGER in CROSS-ROLE SIGNALS:
    g_null(initial) | g_null(post-lifecycle) | g_null_lifecycle | g_null(post-domain-final) | g_null(final) | Trajectory
  Labels: MONOTONIC-PASS / MONOTONIC-FAIL / LIFECYCLE-DEGRADED / LIFECYCLE-NH-BLOCKED /
          DOMAIN-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED.

§14 -- FINDING SEVERITY AGGREGATION [IMMUTABLE]
  | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all). No findings = LOW.

§15 -- LENS EXHAUSTION [IMMUTABLE]
  All lens.verify addressed. LENS COVERAGE TABLE:
    | # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
  Cite APPLICABILITY MATRIX row ID + tier. Value locked.
  HIGH+OPEN -> ADVISORY-OPEN-LENS-REQUIRED. MEDIUM+OPEN -> ADVISORY-OPEN-LENS.
  LOW+OPEN -> cite AM row; no register entry.

§16 -- PRIMARY DRIVER DERIVATION [IMMUTABLE]
  1. GClose=FAIL -> BRACKET CLOSING
  2. G_domain_agg=FAIL -> DOMAIN
  3. G_lifecycle=FAIL -> LIFECYCLE
  4. GOpen=FAIL -> BRACKET OPENING
  5-8: same for CONDITIONAL.
  9. all PASS -> N/A
  Emit: **Applying §16 rule**: [n]  **Primary Driver**: [result]

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]
  BRACKET OPENING: per-dimension NH table. Min 3 dimensions. MUST-CLEAR (*).
  | Dimension | Current-State (0-10) | Proposed-State (0-10) | Differential | NH Verdict |
  FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD.
  g_null rule: HOLDS / CONDITIONAL / DEFEATED.
  BRACKET CLOSING re-applies to revised aggregate.
  §3a LIFECYCLE NH TABLE uses same format with commitment-readiness dimensions.

======================================================================
END DISPOSITION_CONTRACT v1-FI
======================================================================
```

---

## ROLE MANIFEST

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE -- runs first] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE -- runs after lifecycle] |

### APPLICABILITY MATRIX

*(Complete before BRACKET OPENING. Locked on completion. Lifecycle role rows listed first.)*

| Row ID | Role | lens.verify Entry | Artifact Domain Covered | Artifact Applicability | Basis for Rating |
|--------|------|------------------|------------------------|----------------------|------------------|
| AM-01 | [LIFECYCLE] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-02 | [LIFECYCLE] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-03 | [DOMAIN] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-04 | [DOMAIN] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-05 | [DOMAIN] | [Full text] | [domain] | [HIGH / MEDIUM / LOW] | [One sentence] |

*(Add rows for all lens.verify entries. Matrix locked.)*

---

## BRACKET OPENING -- NULL HYPOTHESIS CHALLENGE

Contract: DISPOSITION_CONTRACT v1-FI

**Confirm the standing null hypothesis from §0**:
NULL HYPOTHESIS (confirmed): [Copy from §0.]

**Dimension table for the null hypothesis** *(per §17)*:

| Dimension | Current-State (0-10) | Proposed-State (0-10) | Differential | NH Verdict |
|-----------|--------------------|-----------------------|--------------|------------|
| [DIM-A*]  | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

```
MUST-CLEAR OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD) = [N] | count(OPPOSES-BUILD) = [N]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null(initial)** *(§9 Stage 1)*: [copy result]

**Compare alternatives** *(>= 3 dimensions; distinct from §17 NH table)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**Challenge claims**:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [H/M/L] |
| CH-002 | [CLAIM_2] | [H/M/L] |
| CH-003 | [CLAIM_3 -- optional] | [H/M/L] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**g_null(initial)**: [copy]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## LIFECYCLE -- NULL HYPOTHESIS COMMITMENT RESPONSE: [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-FI
Received GOpen: [copy]
Received standing null hypothesis: [copy from §0]
*(Note: DOMAIN has not yet run. Lifecycle runs first.)*

**Respond to each challenge claim from a commitment-readiness frame**:

| CH-ID | Challenge Claim (copy) | Commitment-Frame Response | Status |
|-------|----------------------|--------------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Assess decision-readiness** *(reference GOpen and g_null(initial); domain not yet evaluated)*:
[One paragraph.]

### §3a NULL HYPOTHESIS LIFECYCLE ASSESSMENT *(per §9 Stage 2b and §17)*

*(Evaluate whether the null hypothesis holds from a commitment-readiness perspective.
Use dimensions distinct from BRACKET OPENING -- commitment and program-readiness signals.)*

| Dimension | Current-State (0-10) | Proposed-State (0-10) | Differential | NH Verdict |
|-----------|--------------------|-----------------------|--------------|------------|
| [LC-DIM-A* -- roadmap fit] | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [LC-DIM-B* -- team capacity] | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [LC-DIM-C -- timeline alignment] | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

```
LC MUST-CLEAR OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD) = [N] | count(OPPOSES-BUILD) = [N]
Applying §17 rule to commitment dimensions:
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null_lifecycle** *(§9 Stage 2b)*: [HOLDS / CONDITIONAL / DEFEATED]

**Null hypothesis status**: [yes / partial / no -- reference g_null(initial) and g_null_lifecycle.]

**Findings**:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING] | [H/M/L] |
| F-2 | [§1:S-n] | [FINDING] | [H/M/L] |

```
Section Severity = worst([]) = [H/M/L]
```

**Lens Coverage Table**:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [Full text] | AM-01: [H/M/L] | [ADDRESSED / OPEN] | [F-n or cite] |
| Q-2 | [Full text] | AM-02: [H/M/L] | [ADDRESSED / OPEN] | [F-n or cite] |

**Recommendation**: [One concrete action.]
**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence. If g_null_lifecycle=HOLDS: note §9 override implication.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5L LIFECYCLE-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger.)*

```
G_lifecycle = [copy from LIFECYCLE ledger]
Applying §9 Stage 2:
g_null(initial) = [copy] | G_lifecycle = [copy]
g_null(post-lifecycle) = [result]
```
**g_null(post-lifecycle)**: [FAIL / CONDITIONAL / PASS]
*g_null_lifecycle = [copy from §3a -- informational, not formula input at this stage]*

---

## §3.8 CH-ID SATURATION CHECK

| CH-ID | LIFECYCLE Status | Pre-DOMAIN Saturation |
|-------|-----------------|----------------------|
| CH-001 | [copy] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED] |

**Pre-DOMAIN unsaturated**: [List or "None"]

---

## DOMAIN -- NULL HYPOTHESIS DOMAIN RESPONSE: [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-FI
Received GOpen: [copy]
Received G_lifecycle: [copy from §3.5L]
Received g_null(post-lifecycle): [copy from §3.5L]
Received standing null hypothesis: [copy from §0]

**Respond to each challenge claim**:

| CH-ID | Challenge Claim (copy) | Technical Response | Status |
|-------|----------------------|-------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Revise the alternative scores**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Technical Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| [DIM-1] | [revised] | [revised] | [revised] | [reason] |
| [DIM-2] | [revised] | [revised] | [revised] | |
| [DIM-3] | [revised] | [revised] | [revised] | |

**Findings**:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING] | [H/M/L] |
| F-2 | [§1:S-n] | [FINDING] | [H/M/L] |

```
Section Severity = worst([]) = [H/M/L]
```

**Lens Coverage Table**:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [Full text] | AM-03: [H/M/L] | [ADDRESSED / OPEN] | [F-n or cite] |
| Q-2 | [Full text] | AM-04: [H/M/L] | [ADDRESSED / OPEN] | [F-n or cite] |
| Q-3 | [Full text] | AM-05: [H/M/L] | [ADDRESSED / OPEN] | [F-n or cite] |

**Recommendation**: [One concrete action.]
**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §4.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger.)*

```
G_domain_agg = worst([G_domain verdict(s)]) = [PASS / CONDITIONAL / FAIL]
Applying §9 Stage 3:
g_null(post-lifecycle) = [copy] | G_domain_agg = [copy]
Interim: [result]
g_null_lifecycle override: [APPLIES -- g_null(post-domain-final)=FAIL | NOT APPLICABLE]
g_null(post-domain-final) = [final result]
```
**g_null(post-domain-final)**: [FAIL / CONDITIONAL / PASS]

---

## BRACKET CLOSING -- NULL HYPOTHESIS FINAL VERDICT

Contract: DISPOSITION_CONTRACT v1-FI

```
g_null(post-domain-final) = [copy from §4.5]
Applying §9 Stage 4:
g_null(final) = g_null(post-domain-final) [unless override]
```
**g_null(final)**: [FAIL / CONDITIONAL / PASS]

**Re-evaluate the null hypothesis with all revised scores** *(per §17)*:

| Dimension | Current-State (0-10) | Proposed-State (0-10) | Differential | NH Verdict |
|-----------|--------------------|-----------------------|--------------|------------|
| [DIM-A*]  | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

```
count(FAVORS-BUILD) = [N] | count(OPPOSES-BUILD) = [M]
Revised §17 result: [HOLDS / CONDITIONAL / DEFEATED]
```

**Revised alternatives table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Agg Rationale |
|-----------|---------------|-----------|----------------------|--------------|
| [DIM-1] | [agg] | [agg] | [agg] | [reason] |
| [DIM-2] | [agg] | [agg] | [agg] | |

**Full CH-ID Saturation** *(per §8)*:

| CH-ID | LIFECYCLE Status | DOMAIN Status | Full Saturation | Waiver |
|-------|-----------------|--------------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |

**CH-ID Final Assessment**:

| CH-ID | G_lifecycle | G_domain | Final Status | Notes |
|-------|------------|---------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A -- formula applied | or: justification]
**GClose Rationale**: [2-3 sentences. Reference g_null trajectory, g_null_lifecycle if HOLDS,
and final null hypothesis verdict.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger. Applies §10, §10a, §11.)*

### Surface Coverage

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [SURFACE_1] | [ROLE or "none"] | [LIFECYCLE F-n / DOMAIN F-n] | [COVERED / GAP] |
| [SURFACE_2] | [ROLE or "none"] | [ref] | [COVERED / GAP] |
| [SURFACE_3] | [ROLE or "none"] | [ref] | [COVERED / GAP] |

**Surface coverage gate signal**: [COVERED / PARTIAL]

### Domain Coverage Gap-Check *(per §10a)*

| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|----------|
| [DOMAIN-1] | [AM-0n: [ROLE] -- "[lens summary]" / "none"] | [COVERED / ADVISORY-GAP] |
| [DOMAIN-2] | [AM-0n / "none"] | [COVERED / ADVISORY-GAP] |

**§11 ADVISORY-ORPHAN check**: [List or "None detected."]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER] | [copy] | DISPOSITION_CONTRACT v1-FI |
| G_lifecycle | [LIFECYCLE] | [copy] | DISPOSITION_CONTRACT v1-FI |
| G_domain_agg | [DOMAIN] | [copy] | DISPOSITION_CONTRACT v1-FI |
| GClose | [CHALLENGER] | [copy] | DISPOSITION_CONTRACT v1-FI |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Or "None detected."]
**Convergence**: [Independent signals from 2+ reviewers. State highest-confidence NH signal.]
**Scope coverage**: [Uncovered surfaces or "None."]

**§13 PROGRESSION LEDGER**:
```
g_null(initial)           = [copy from BRACKET OPENING §17]
g_null(post-lifecycle)    = [copy from §3.5L]
g_null_lifecycle          = [copy from §3a -- commitment NH signal]
g_null(post-domain-final) = [copy from §4.5]
g_null(final)             = [copy from BRACKET CLOSING §9 Stage 4]
Trajectory: [MONOTONIC-PASS / MONOTONIC-FAIL / LIFECYCLE-DEGRADED / LIFECYCLE-NH-BLOCKED /
             DOMAIN-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

---

## DISPOSITION

**Gate vector**:
- GOpen = [copy]
- G_lifecycle = [copy]
- G_domain_agg = [copy]
- GClose = [copy]

```
G = {GOpen=[_], G_lifecycle=[_], G_domain_agg=[_], GClose=[_]}
GClose=FAIL? -> BLOCKED (null hypothesis holds)
Any Gi=FAIL? -> BLOCKED
No FAIL, any CONDITIONAL? -> CONDITIONAL
All PASS? -> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Applying §16 rule**: [rule number + reason]
**Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**Conditions** *(CONDITIONAL only)*:
1. [State condition.]

**Blocker** *(BLOCKED only)*: [State specific finding from FAIL gate.]

**RESOLUTION REGISTRY** *(CONDITIONAL only)*:
| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [sentence] | [role] | [falsifiable test] | OPEN |

*If not CONDITIONAL: "RESOLUTION REGISTRY: N/A -- disposition is [value]"*

---

## ACTION ITEM REGISTER

| Source | CH-ID / Finding | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|--------|----------------|-----------------|------------------|------------|---------------------|
| [gate ledger] | -- | [verbatim Section / Gate / Verdict / Class] | [class] | [ROLE] | [criterion] |
| [CH-ID item] | CH-00n | [action required] | [class] | [ROLE] | [criterion] |
| [lens HIGH OPEN] | AM-0n / Q-n | ADVISORY-OPEN-LENS-REQUIRED: [entry] | ADVISORY | [ROLE] | Produce finding. |
| [lens MED OPEN] | AM-0n / Q-n | ADVISORY-OPEN-LENS: [entry] | ADVISORY | [ROLE] | Address or justify. |
| [scope gap] | -- | ADVISORY-GAP: §1 surface [name] | ADVISORY | [ROLE] | Assign reviewer. |
| [domain gap] | -- | ADVISORY-GAP (DOMAIN COVERAGE): [domain] no HIGH reviewer | ADVISORY | [ROLE] | Add reviewer or justify. |

---

**Artifact to review:**

{{artifact}}
