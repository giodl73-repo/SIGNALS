## V-05 -- Full Integration: §17 NH Table + ROLE MANIFEST Applicability + §5.5 Gap-Check (C-35 + C-33 + C-34)

**Variation axis**: Full integration of all three new criteria using the structural encoding
from V-04 (ROLE MANIFEST APPLICABILITY MATRIX + §5.5 DOMAIN COVERAGE GAP-CHECK) combined with
the §17 NULL HYPOTHESIS DIMENSION TABLE (C-35) from V-01. This is the Round 14 candidate
for 225/225.

**Hypothesis**: The difference from R13 V-05 is structural: R13 V-05 encodes C-33 as §18
LENS APPLICABILITY CONTRACT (a new IMMUTABLE contract section) and C-34 as §19 DOMAIN COVERAGE
GAP-CHECK CONTRACT (another new section) added to the already-large DISPOSITION_CONTRACT block.
Round 14 V-05 hypothesis: ROLE MANIFEST front-loading + §5.5 integration is a simpler encoding
that achieves the same C-33/C-34 coverage with less structural overhead. The DISPOSITION_CONTRACT
stays at §17 sections; no §18/§19 needed. The information lives where it is most naturally
actionable: applicability in the ROLE MANIFEST (before any reviewer runs), gap-check in §5.5
(at the natural reconciliation point).

Key traceability chain:
  ROLE MANIFEST APPLICABILITY MATRIX (pre-committed)
    -> §15 LENS COVERAGE TABLE (cites AM row per lens entry) [C-33]
    -> §5.5 DOMAIN COVERAGE GAP-CHECK (references APPLICABILITY MATRIX HIGH rows) [C-34]
  BRACKET OPENING §17 NULL HYPOTHESIS DIMENSION TABLE [C-35]
    -> §9 g_null(initial) formula
    -> BRACKET CLOSING revised §17 table -> g_null(final) formula

All three criteria are simultaneously active. The scorer can verify:
- C-33: each §15 row has an AM-row citation with HIGH/MEDIUM/LOW. Basis = APPLICABILITY MATRIX.
- C-34: §5.5 DOMAIN COVERAGE GAP table names every artifact domain; HIGH-applicability AM rows
  identified; ADVISORY-GAP domains without HIGH-applicability reviewer are in ACTION ITEM REGISTER.
- C-35: BRACKET OPENING §17 table has current-state/proposed-state per dimension; NH Verdict
  column is the sole input to g_null derivation formula; g_null(initial) derivable from table alone.

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
  (domain re-scores aggregated). The revised table's NH Verdict column is the sole input
  to the closing g_null derivation.

  §9 Stage 1 g_null(initial) = §17 formula output; NOT equal to GOpen unless formula agrees.
  A scorer verifying g_null reads only the NH Verdict column. No prose needed.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

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
| AM-01 | [DOMAIN ROLE] | [Full text lens.verify entry 1] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-02 | [DOMAIN ROLE] | [Full text lens.verify entry 2] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-03 | [DOMAIN ROLE] | [Full text lens.verify entry 3 if present] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-04 | [LIFECYCLE ROLE] | [Full text lens.verify entry 1] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-05 | [LIFECYCLE ROLE] | [Full text lens.verify entry 2] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |

*(Add rows for every lens.verify entry from every assigned role. APPLICABILITY MATRIX is now
locked. No reviewer section may alter these values. The "Artifact Domain Covered" column is
the input to §10a DOMAIN COVERAGE GAP-CHECK in §5.5.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

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
| [DIM-D -- optional] | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

*(Dimensions marked * are MUST-CLEAR. Add rows as needed -- each is an independent NH signal.)*

**Applying §17 g_null derivation rule**:
```
MUST-CLEAR rows with OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD) = [N]
count(NEUTRAL)      = [N]
count(OPPOSES-BUILD) = [N]
Total rows = [N]
Majority check: FAVORS-BUILD majority AND no MUST-CLEAR OPPOSES -> DEFEATED
                No majority (FAVORS <= OPPOSES) -> CONDITIONAL
                Any MUST-CLEAR OPPOSES -> HOLDS
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null(initial)** *(output of §17 formula; carried to §9 Stage 1)*: [HOLDS / CONDITIONAL / DEFEATED]

**NULL HYPOTHESIS DERIVATION RULE** *(pre-committed per §9; BRACKET CLOSING re-applies)*:
  g_null confirmed by §17 table. BRACKET CLOSING re-applies to revised aggregate table.

**Challenge claims** *(assign CH-IDs per §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction. One sentence.] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL -- consistent with §17 g_null result]
**GOpen Reason**: [One sentence. If g_null=HOLDS: GOpen=FAIL; if CONDITIONAL: GOpen=CONDITIONAL.]
**g_null(initial)** *(§9 Stage 1 -- §17 formula output)*: [copy from §17 derivation above]

*GOpen, g_null(initial), and all CH-IDs carry forward to every downstream section.*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]

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

**Additional Findings** *(per §14: per-finding severity; per §11: each finding cites §1 surface)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1 -- from this role's `lens.verify` and `expertise.depth`.] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-3 | [§1:S-n -- optional] | [FINDING_3] | [HIGH / MEDIUM / LOW] |

*(Findings without a valid §1:S-n citation are ADVISORY-ORPHAN per §11.)*

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] -- mechanical result; do not assign editorially.

**Lens Coverage Table** *(per §15 -- cite APPLICABILITY MATRIX row IDs; do not reassign tiers)*:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [Full text lens.verify entry 1] | AM-01: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n, or "AM-01: LOW -- [basis]" if LOW+OPEN] |
| Q-2 | [Full text lens.verify entry 2] | AM-02: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n, or cite AM-02] |
| Q-3 | [Full text if present] | AM-03: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n, or cite AM-03] |

*(Add rows for every lens.verify entry. Applicability is locked from ROLE MANIFEST; citing
the AM row is mandatory. HIGH/MEDIUM+OPEN -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.
LOW+OPEN -> cite AM row in Finding Reference; no register entry.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence. If CONDITIONAL: name condition. If FAIL: name gap.]

*(For `--depth deep`: repeat as DOMAIN-2, DOMAIN-3. Each emits its own local ledger row,
domain re-score, and lens coverage table citing APPLICABILITY MATRIX rows.)*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6 -- no verdict emitted.)*

**Applying §3a formula**:
```
G_domain rows collected:
  DOMAIN -- [ROLE_NAME]: [verdict]
G_domain_agg = worst([list]) = [PASS / CONDITIONAL / FAIL]
```
**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

**Applying §9 Stage 2 formula**:
```
g_null(initial) = [copy from BRACKET OPENING] | G_domain_agg = [copy]
  FAIL->FAIL | CONDITIONAL->max(initial,CONDITIONAL) | PASS->g_null(initial)
g_null(post-domain) = [result]
```
**g_null(post-domain)**: [FAIL / CONDITIONAL / PASS]

*Both carry forward to §3.8, LIFECYCLE, and BRACKET CLOSING.*

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger. Runs after §3.5, before LIFECYCLE.)*

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | [copy from DOMAIN] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED or N/A] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None"]
*LIFECYCLE may proceed. Full saturation check executes at BRACKET CLOSING.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]
Received G_domain Aggregate: [copy from §3.5]
Received g_null(post-domain): [copy from §3.5]

**CH-ID Response Table** *(mandatory per §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph referencing GOpen, G_domain Aggregate, and
g_null(post-domain) explicitly.]

**Null hypothesis status**: [yes / partial / no -- reference g_null(post-domain). One sentence.]

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
| Q-1 | [Full text lens.verify entry 1] | AM-04: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or cite AM-04] |
| Q-2 | [Full text lens.verify entry 2] | AM-05: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or cite AM-05] |

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

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(per §17 -- aggregate domain re-scores; re-derive g_null)*:

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

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Domain Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| [DIM-1] | [agg] | [agg] | [agg] | [reason] |
| [DIM-2] | [agg] | [agg] | [agg] | |

**Full CH-ID Saturation Check** *(per §8 -- PASS prohibited without full saturation)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver (if needed) |
|-------|--------------|-----------------|-----------------|---------------------|
| CH-001 | [copy from DOMAIN] | [copy from LIFECYCLE] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy from DOMAIN] | [copy from LIFECYCLE] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [All defeated, or list.]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A -- formula applied | or: override justification one sentence]
**GClose override authority**: GClose=FAIL overrides all prior verdicts per §3.
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
| [§1 SURFACE_1] | [ROLE or "none"] | [DOMAIN F-n / etc.] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [ref] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [ref] | [COVERED / GAP] |

**Surface coverage gate signal** *(§10 -- informational)*:
[COVERED -- all surfaces addressed | PARTIAL -- [N] surface(s) not addressed]

### Domain Coverage Gap-Check *(per §10a -- references APPLICABILITY MATRIX)*

*(Group §1 IN-SCOPE surfaces into artifact domains. Look up APPLICABILITY MATRIX "Artifact Domain
Covered" column for each domain. Identify rows with HIGH applicability covering that domain.)*

| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|----------|
| [DOMAIN-1 -- logical grouping of §1 surfaces] | [AM-0n: [ROLE] -- "[lens entry summary]" / "none"] | [COVERED / ADVISORY-GAP] |
| [DOMAIN-2] | [AM-0n: [ROLE] / "none"] | [COVERED / ADVISORY-GAP] |
| [DOMAIN-3 if applicable] | [AM-0n or "none"] | [COVERED / ADVISORY-GAP] |

*(ADVISORY-GAP domains -> ACTION ITEM REGISTER with:
Attribution: "DOMAIN COVERAGE GAP-CHECK / [domain] / no HIGH-applicability reviewer in APPLICABILITY MATRIX"
Class: ADVISORY)*

**§11 ADVISORY-ORPHAN check** *(findings lacking §1:S-n citation)*:
[List orphaned findings with their section, or "None detected."]

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

**Conflicts**: [Two reviewers with incompatible CH-ID responses or findings. If none: "None detected."]

**Convergence**: [Any CH-ID or concern named independently by two or more reviewers. Name it
and state why it is the highest-confidence signal in this review.]

**Scope coverage**: [Any in-scope §1 surface not covered by any reviewer. If all covered: "None."]

**§13 PROGRESSION LEDGER**:
```
g_null(initial)     = [copy from BRACKET OPENING §17 formula]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING §9 Stage 3]
Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
                     DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```
*Trajectory is informational. No gate ledger row emitted.*

---

## DISPOSITION

**Gate vector** *(fill from GATE VECTOR TABLE)*:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula** *(do not reason editorially -- evaluate mechanically)*:
```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Applying §16 rule**: [rule number fired and why]
**Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**Conditions** *(complete only if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate -- what must be resolved. Gate order: GOpen before G_domain before G_lifecycle before GClose.]
2. [Additional conditions if present.]

**Blocker** *(complete only if BLOCKED)*: [Specific finding from FAIL gate. If GClose=FAIL:
"Challenger final verdict HOLDS -- [GClose Rationale summary]."]

**RESOLUTION REGISTRY** *(complete only if CONDITIONAL)*:
| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [one sentence] | [role] | [falsifiable test -- observable from outside review] | OPEN |

*If not CONDITIONAL: "RESOLUTION REGISTRY: N/A -- disposition is [value]"*

---

## ACTION ITEM REGISTER

*Assembly rule per §6: copy all local gate ledger rows verbatim. Then add CH-ID items,
ADVISORY-OPEN-LENS items (HIGH/MEDIUM applicability OPEN in §15), ADVISORY-GAP items
(§10 surface gaps + §10a domain gaps), ADVISORY-ORPHAN items (§11), and ADVISORY-OBS items.*

| Source | CH-ID / Finding | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|--------|----------------|-----------------|------------------|------------|---------------------|
| [gate ledger copy] | -- | [verbatim: Section / Gate / Verdict / Class] | [BLOCKED/CONDITIONAL/ADVISORY] | [ROLE] | [criterion] |
| [CH-ID item] | CH-00n | [What must be done from PARTIAL/HOLDS status in BRACKET CLOSING] | [BLOCKED/CONDITIONAL/ADVISORY] | [ROLE] | [criterion] |
| [lens gap HIGH] | AM-0n / Q-n | ADVISORY-OPEN-LENS-REQUIRED: [lens entry text] not addressed; HIGH applicability | ADVISORY | [ROLE] | Produce a finding addressing [lens entry] for this artifact. |
| [lens gap MED] | AM-0n / Q-n | ADVISORY-OPEN-LENS: [lens entry text] not addressed; MEDIUM applicability | ADVISORY | [ROLE] | Address [lens entry] or provide justification for non-applicability. |
| [scope gap] | -- | ADVISORY-GAP: §1 surface [surface name] not covered by any reviewer | ADVISORY | [ROLE] | Assign reviewer with relevant lens to address [surface]. |
| [domain gap] | -- | ADVISORY-GAP (DOMAIN COVERAGE): [domain name] has no HIGH-applicability reviewer in APPLICABILITY MATRIX | ADVISORY | [ROLE] | Add a reviewer with HIGH applicability for [domain] or justify waiver. |
| [orphan] | -- | ADVISORY-ORPHAN: finding [F-n] from [SECTION] lacks §1:S-n citation | ADVISORY | [ROLE] | Re-assign to valid §1 surface or remove finding. |

*Every row traces to a source. The register is navigable in both directions without
cross-referencing reviewer sections separately.*

---

**Artifact to review:**

{{artifact}}
