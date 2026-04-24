## V-02 -- Single Axis: Role Manifest Applicability Pre-Rating (C-33, Front-Loaded)

**Variation axis**: Artifact applicability ratings for each role's lens dimensions are
pre-committed in the ROLE MANIFEST table before any reviewer section executes. The §15 LENS
COVERAGE TABLE references the manifest-assigned applicability tier via row ID rather than
assigning it inline.

**Hypothesis**: V-01 assigns applicability inline within each §15 table. Risk: reviewers may
retroactively justify LOW to skip inconvenient lens dimensions, or assign inconsistently across
sections. V-02 front-loads the commitment: an APPLICABILITY MATRIX is completed in the ROLE
MANIFEST before BRACKET OPENING runs. The matrix is locked there. Downstream §15 tables cite
matrix row IDs -- they cannot deviate. This is a stronger encoding for C-33 because applicability
is a pre-run commitment, not a per-section fill-in. The scorer can verify C-33 by checking
(a) the APPLICABILITY MATRIX in ROLE MANIFEST contains HIGH/MEDIUM/LOW per lens entry, and
(b) §15 tables cite the matrix row and match its tier. The chain is forward-traceable from
ROLE MANIFEST to each §15 row.

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
IN-SCOPE:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Cited in §5.5 SCOPE COVERAGE RECONCILIATION and §11 FINDING-SURFACE LINKAGE.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

Scope Amendment: "SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]"
§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks commitment. MEDIUM=Conditions commitment. LOW=Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED: GClose=FAIL OR any Gi=FAIL
  CONDITIONAL: no FAIL AND any CONDITIONAL
  READY: all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain rows). FAIL>CONDITIONAL>PASS.

§4 -- CONTRACT CITE [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING [IMMUTABLE]
  Challenge claims -> CH-IDs. Every downstream section: mandatory CH-ID response table.
  PASS prohibited if any CH-ID = OPEN.

§6 -- LOCAL GATE LEDGER [IMMUTABLE]
  Row: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  EXCLUDED: §3.5, §3.8, §5.5.

§7 -- SECTION ORDER [IMMUTABLE]
  1.ROLE MANIFEST  2.BRACKET OPENING  3.DOMAIN(s)
  3.5.DOMAIN-AGGREGATE  3.8.CH-ID SATURATION  4.LIFECYCLE
  5.BRACKET CLOSING  5.5.SCOPE COVERAGE  6.GATE VECTOR TABLE
  7.CROSS-ROLE SIGNALS  8.DISPOSITION  9.ACTION ITEM REGISTER

§8 -- CH-ID SATURATION [IMMUTABLE]
  FULLY SATURATED: DOMAIN + LIFECYCLE responses. PASS prohibited without full saturation or waiver.
  Waiver: "CH-XXX WAIVER: [reason]"

§9 -- NULL HYPOTHESIS PROGRESSION [IMMUTABLE]
  Stage 1: g_null(initial) = §17 formula output [BRACKET OPENING]
  Stage 2: g_null(post-domain) [§3.5] -- FAIL if G_domain=FAIL; else max formula.
  Stage 3: g_null(final) [BRACKET CLOSING] -- FAIL if G_lifecycle=FAIL; else max formula.
  GClose must equal g_null(final). Override: "g_null OVERRIDE: [justification]"

§10 -- SCOPE COVERAGE GATE [IMMUTABLE]
  §5.5 maps §1 surfaces to findings. GAP -> ADVISORY-GAP in register. Informational only.

§11 -- FINDING-SURFACE LINKAGE [IMMUTABLE]
  Each finding carries [§1:S-n] citation. Missing = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY [IMMUTABLE]
  DISPOSITION=CONDITIONAL: emit RESOLUTION REGISTRY table (Gate/Condition/Owner/Criterion/Status=OPEN).
  Else: "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER [IMMUTABLE]
  CROSS-ROLE SIGNALS: §13 PROGRESSION LEDGER with initial/post-domain/final + trajectory label.
  Labels: MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
          DOMAIN-RECOVERED / LIFECYCLE-RECOVERED.

§14 -- FINDING SEVERITY AGGREGATION [IMMUTABLE]
  Findings table: | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all severities). Apply mechanically.

§15 -- LENS EXHAUSTION [IMMUTABLE]
  After findings, emit LENS COVERAGE TABLE:
    | # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |

  CRITICAL: Applicability tiers are PRE-COMMITTED in the ROLE MANIFEST APPLICABILITY MATRIX
  before any reviewer section runs. Reviewers may NOT assign or change applicability in §15.
  Reference the APPLICABILITY MATRIX row ID (e.g., "AM-01: HIGH").

  Status: ADDRESSED / OPEN.
  HIGH/MEDIUM applicability + OPEN -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.
  LOW applicability + OPEN -> no register entry; cite the APPLICABILITY MATRIX row in Finding
  Reference column.

§16 -- PRIMARY DRIVER DERIVATION [IMMUTABLE]
  Precedence: GClose=FAIL(1) > G_domain=FAIL(2) > G_lifecycle=FAIL(3) > GOpen=FAIL(4) >
  GClose=COND(5) > G_domain=COND(6) > G_lifecycle=COND(7) > GOpen=COND(8) > all PASS=N/A(9).
  Emit: **Applying §16 rule**: [n + reason]  **Primary Driver**: [result]

§17 -- NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  BRACKET OPENING: emit NULL HYPOTHESIS DIMENSION TABLE before challenge claims.
  Columns: Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict
  NH Verdict: positive diff -> FAVORS-BUILD; zero -> NEUTRAL; negative -> OPPOSES-BUILD.
  MUST-CLEAR dimensions marked (*).
  g_null rule: HOLDS if any MUST-CLEAR=OPPOSES-BUILD; CONDITIONAL if no majority FAVORS-BUILD;
               DEFEATED if FAVORS-BUILD majority with no MUST-CLEAR OPPOSES-BUILD.
  §9 Stage 1 g_null(initial) = §17 formula output.

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

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc.)*

### APPLICABILITY MATRIX

*(Complete this matrix now, before BRACKET OPENING executes. This matrix is locked at this point.
Reviewer sections reference it by row ID; they may not modify applicability values.)*

For each assigned reviewer role, list every `lens.verify` entry and assign an artifact-specific
applicability tier:
- **HIGH**: lens dimension directly relevant to this artifact type. Finding expected.
  OPEN in §15 -> ADVISORY-OPEN-LENS-REQUIRED in ACTION ITEM REGISTER.
- **MEDIUM**: lens dimension tangentially relevant. Finding expected.
  OPEN in §15 -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.
- **LOW**: lens dimension not applicable to this artifact type. OPEN is acceptable.
  State basis for LOW rating in Basis column.

| Row ID | Role | lens.verify Entry | Artifact Applicability | Basis for Rating |
|--------|------|------------------|----------------------|------------------|
| AM-01 | [DOMAIN ROLE] | [Full text lens.verify entry 1] | [HIGH / MEDIUM / LOW] | [One sentence: why this tier for this artifact] |
| AM-02 | [DOMAIN ROLE] | [Full text lens.verify entry 2] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-03 | [DOMAIN ROLE] | [Full text lens.verify entry 3 if present] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-04 | [LIFECYCLE ROLE] | [Full text lens.verify entry 1] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-05 | [LIFECYCLE ROLE] | [Full text lens.verify entry 2] | [HIGH / MEDIUM / LOW] | [One sentence] |

*(Add rows for every lens.verify entry from every assigned role. APPLICABILITY MATRIX is now
locked. No downstream section may alter these values.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]

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
count(FAVORS-BUILD) = [N] | count(OPPOSES-BUILD) = [M]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null(initial)** *(per §17 formula)*: [HOLDS / CONDITIONAL / DEFEATED]

**Challenge claims** *(assign CH-IDs per §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)** *(§9 Stage 1)*: [copy §17 result]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [verdict] | [class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Domain re-score**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| [DIM-1] | [revised] | [revised] | [revised] | [reason] |
| [DIM-2] | [revised] | [revised] | [revised] | |

**Additional Findings** *(per §14 and §11)*:

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

**Lens Coverage Table** *(per §15 -- cite APPLICABILITY MATRIX row IDs; do not reassign tiers)*:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [Full text lens.verify entry 1] | AM-01: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n, or cite AM-01 if LOW+OPEN] |
| Q-2 | [Full text lens.verify entry 2] | AM-02: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n, or cite AM-02 if LOW+OPEN] |
| Q-3 | [Full text if present] | AM-03: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n, or cite AM-03 if LOW+OPEN] |

*(Cite the APPLICABILITY MATRIX row. Status may not contradict pre-committed tier.
HIGH/MEDIUM+OPEN -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [verdict] | [class] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger.)*

```
G_domain_agg = worst([G_domain list]) = [PASS / CONDITIONAL / FAIL]
g_null(post-domain): apply §9 Stage 2
```
**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]
**g_null(post-domain)**: [FAIL / CONDITIONAL / PASS]

---

## §3.8 CH-ID SATURATION CHECK

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | [copy] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED] |

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy] | G_domain Aggregate: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph referencing GOpen, G_domain Aggregate, g_null(post-domain).]

**Null hypothesis status**: [yes / partial / no. One sentence.]

**Additional Findings** *(per §14 and §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation**: worst([_]) = **Section Severity**: [HIGH / MEDIUM / LOW]

**Lens Coverage Table** *(per §15 -- cite APPLICABILITY MATRIX row IDs)*:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [lens.verify entry 1] | AM-04: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or cite AM-04] |
| Q-2 | [lens.verify entry 2] | AM-05: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or cite AM-05] |

**Recommendation**: [One concrete action.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [verdict] | [class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Applying §9 Stage 3 formula**:
```
g_null(final) = formula(G_lifecycle=[_], g_null(post-domain)=[_]) = [FAIL / CONDITIONAL / PASS]
```
**g_null(final)**: [FAIL / CONDITIONAL / PASS]

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(aggregate domain re-scores; re-derive per §17)*:

| Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
|-----------|--------------------------|----------------------------|--------------|------------|
| [DIM-A*]  | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [agg] | [agg] | [diff] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

**Applying §17 rule to revised table**: MUST-CLEAR OPPOSES-BUILD=[_] | FAVORS=[_] | OPPOSES=[_]
Result: [HOLDS / CONDITIONAL / DEFEATED]

**Revised alternatives table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Domain Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| [DIM-1] | [agg] | [agg] | [agg] | [reason] |

**Full CH-ID Saturation Check**:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver |
|-------|--------------|-----------------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or WAIVER] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or WAIVER] |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [All defeated, or list.]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO] | **g_null Override**: [N/A or justification]
**GClose Rationale**: [2-3 sentences. Reference g_null trajectory.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [verdict] | [class] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger. Applies §10 and §11.)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [ref] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [ref] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [ref] | [COVERED / GAP] |

**Coverage gate signal** *(§10 -- informational)*: [COVERED / PARTIAL]
**§11 ADVISORY-ORPHAN check**: [List or "None detected."]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER] | [copy] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [copy] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [copy] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [copy] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [If none: "None detected."]
**Convergence**: [Independently named concerns. Highest-confidence signal.]
**Scope coverage**: [Uncovered surfaces. If all: "None."]

**§13 PROGRESSION LEDGER**:
```
g_null(initial)     = [copy from BRACKET OPENING]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING]
Trajectory:         [label]
```

---

## DISPOSITION

**Gate vector**: GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]

**Apply §3 formula**: GClose=FAIL->BLOCKED | Gi=FAIL->BLOCKED | No FAIL+CONDITIONAL->CONDITIONAL | All PASS->READY

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Applying §16 rule**: [rule n + reason]
**Primary Driver**: [result]
**Conditions / Blocker**: [if applicable]
**RESOLUTION REGISTRY**: [table if CONDITIONAL; "N/A -- disposition is [value]" otherwise]

---

## ACTION ITEM REGISTER

| Source | CH-ID / Finding | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|--------|----------------|-----------------|------------------|------------|---------------------|
| [gate ledger] | -- | [verbatim from local ledger rows] | [class] | [role] | [criterion] |
| [CH-ID] | CH-00n | [from PARTIAL/HOLDS] | [class] | [role] | [criterion] |
| [lens gap] | AM-0n | [ADVISORY-OPEN-LENS for HIGH/MEDIUM OPEN entries] | ADVISORY | [role] | Address [lens entry] for this artifact. |
| [scope gap] | -- | [ADVISORY-GAP] | ADVISORY | [role] | [criterion] |

---

**Artifact to review:**

{{artifact}}
