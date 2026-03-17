## V-03 -- Single Axis: §5.5 Domain Gap-Check Extension (C-34)

**Variation axis**: The domain coverage gap-check (C-34) is embedded into §5.5 SCOPE COVERAGE
RECONCILIATION rather than as a standalone §3.9 section. §5.5 already enumerates §1 IN-SCOPE
surfaces and maps each to reviewer findings; the gap-check extends it with a domain-inward
question: "for each artifact domain, does any reviewer have HIGH applicability?"

**Hypothesis**: R13 encodes C-34 as §19 DOMAIN COVERAGE GAP-CHECK CONTRACT -- a new standalone
section after §3.8. Risk: a standalone section after §3.8 interrupts the gate flow and may be
omitted or treated as optional. V-03 hypothesis: embedding the domain gap-check inside §5.5
is structurally sounder because §5.5 is the natural reconciliation point -- it already exists
in every review, it already maps surfaces to reviewers, and adding a domain-inward pass there
requires minimal structural change. The C-34 gap-check becomes a second sub-table within §5.5:
after the surface-coverage table, emit a DOMAIN COVERAGE GAP table listing each artifact domain
(derived from §1 surfaces), the reviewer(s) with HIGH applicability for that domain, and a
gap classification (COVERED / ADVISORY-GAP). Domains with no HIGH-applicability reviewer become
ADVISORY-GAP entries in the ACTION ITEM REGISTER. This is orthogonal to C-31 (role-outward) and
C-10 (surface-coverage); C-34 is domain-inward.

Note: This variation does NOT add a lens applicability column to §15 (that is V-01/V-02). The
domain gap-check in §5.5 requires the reviewer to assess applicability at the artifact-domain
level during reconciliation, not per lens entry. This is a coarser granularity than C-33 but
satisfies C-34 independently.

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
IN-SCOPE (cited in §5.5 and §11):
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

Scope Amendment: "SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]"
§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks. MEDIUM=Conditions. LOW=Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED: GClose=FAIL OR any Gi=FAIL
  CONDITIONAL: no FAIL AND any CONDITIONAL
  READY: all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain). FAIL>CONDITIONAL>PASS.

§4 -- CONTRACT CITE [IMMUTABLE]
  "Contract: DISPOSITION_CONTRACT v1" opens every reviewer section.

§5 -- CH-ID TRACING [IMMUTABLE]
  Challenge claims -> CH-IDs. Every downstream section: CH-ID response table.
  PASS prohibited if any CH-ID = OPEN.

§6 -- LOCAL GATE LEDGER [IMMUTABLE]
  | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  EXCLUDED: §3.5, §3.8, §5.5.

§7 -- SECTION ORDER [IMMUTABLE]
  1.ROLE MANIFEST  2.BRACKET OPENING  3.DOMAIN(s)
  3.5.DOMAIN-AGGREGATE  3.8.CH-ID SATURATION  4.LIFECYCLE
  5.BRACKET CLOSING  5.5.SCOPE COVERAGE (includes DOMAIN COVERAGE GAP-CHECK)
  6.GATE VECTOR TABLE  7.CROSS-ROLE SIGNALS  8.DISPOSITION  9.ACTION ITEM REGISTER

§8 -- CH-ID SATURATION [IMMUTABLE]
  FULLY SATURATED: DOMAIN + LIFECYCLE responses. PASS prohibited without saturation or waiver.

§9 -- NULL HYPOTHESIS PROGRESSION [IMMUTABLE]
  Stage 1: g_null(initial) = §17 formula [BRACKET OPENING]
  Stage 2: g_null(post-domain) [§3.5]
  Stage 3: g_null(final) [BRACKET CLOSING]
  GClose must equal g_null(final). Override: "g_null OVERRIDE: [justification]"

§10 -- SCOPE COVERAGE GATE [IMMUTABLE]
  §5.5 maps §1 surfaces to findings. GAP -> ADVISORY-GAP in register. Informational.
  §5.5 ALSO runs the DOMAIN COVERAGE GAP-CHECK per §10a below.

§10a -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  Runs within §5.5, after the surface coverage table.
  Step 1: List each ARTIFACT DOMAIN (named in §1 IN-SCOPE surfaces; group surfaces into domains).
  Step 2: For each domain, list reviewer(s) with HIGH applicability coverage.
          (Applicability: a reviewer has HIGH applicability for a domain if their lens.verify
          entries directly target that domain's concerns.)
  Step 3: Classify:
    COVERED  = at least one reviewer has HIGH applicability for this domain.
    ADVISORY-GAP = no reviewer has HIGH applicability for this domain.
  Step 4: Each ADVISORY-GAP domain -> ADVISORY-GAP entry in ACTION ITEM REGISTER with
          Attribution: "DOMAIN COVERAGE GAP-CHECK / [domain name] / no HIGH-applicability reviewer"
  Table format:
    | Artifact Domain | Reviewer(s) with HIGH Applicability | Coverage |
  This check is informational -- it does not feed the §3 formula or add gate verdicts.

§11 -- FINDING-SURFACE LINKAGE [IMMUTABLE]
  Each finding: [§1:S-n] citation. Missing = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY [IMMUTABLE]
  CONDITIONAL: emit RESOLUTION REGISTRY table. Else: "N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER [IMMUTABLE]
  CROSS-ROLE SIGNALS: §13 PROGRESSION LEDGER with initial/post-domain/final + trajectory.

§14 -- FINDING SEVERITY AGGREGATION [IMMUTABLE]
  | # | §1 Surface | Finding | Severity | -- Section Severity = worst. Apply mechanically.

§15 -- LENS EXHAUSTION [IMMUTABLE]
  After findings: LENS COVERAGE TABLE:
    | # | lens.verify Entry | Status | Finding Reference |
  Status: ADDRESSED / OPEN.
  OPEN -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.

§16 -- PRIMARY DRIVER DERIVATION [IMMUTABLE]
  Precedence: GClose=FAIL(1) > G_domain=FAIL(2) > G_lifecycle=FAIL(3) > GOpen=FAIL(4) >
  GClose=COND(5) > G_domain=COND(6) > G_lifecycle=COND(7) > GOpen=COND(8) > all PASS=N/A(9).

§17 -- NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  BRACKET OPENING: emit NULL HYPOTHESIS DIMENSION TABLE before challenge claims.
  | Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
  NH Verdict: pos diff->FAVORS-BUILD; zero->NEUTRAL; neg->OPPOSES-BUILD.
  MUST-CLEAR (*). g_null rule: HOLDS(any MUST-CLEAR=OPPOSES)/CONDITIONAL(no majority)/DEFEATED(FAVORS majority).
  §9 Stage 1 g_null(initial) = §17 output.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today -- one sentence.]

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

**Applying §17 rule**: MUST-CLEAR OPPOSES=[_] | FAVORS=[_] | OPPOSES=[_] -> [HOLDS/CONDITIONAL/DEFEATED]
**g_null(initial)** *(§17 formula)*: [result]

**Challenge claims**:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

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
Received GOpen: [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | Technical Response | Status |
|-------|----------------------|--------------------|--------|
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

**Lens Coverage Table** *(per §15)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|-------------------|
| Q-1 | [Full text lens.verify entry 1] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text lens.verify entry 2] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-3 | [Full text if present] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(OPEN entries -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.)*

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
g_null(post-domain): §9 Stage 2 formula
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

| CH-ID | Challenge Claim (copy) | Commitment-Frame Response | Status |
|-------|----------------------|--------------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph referencing GOpen, G_domain Aggregate, g_null(post-domain).]

**Null hypothesis status**: [yes / partial / no. One sentence.]

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

**Lens Coverage Table** *(per §15)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|-------------------|
| Q-1 | [lens.verify entry 1] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [lens.verify entry 2] | [ADDRESSED / OPEN] | [F-n or N/A] |

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
g_null(final) = formula(G_lifecycle=[_], g_null(post-domain)=[_]) = [result]
```
**g_null(final)**: [FAIL / CONDITIONAL / PASS]

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(aggregate domain re-scores; §17 rule)*:

| Dimension | Current-State Score | Proposed-State Score | Differential | NH Verdict |
|-----------|--------------------|--------------------|--------------|------------|
| [DIM-A*]  | [agg] | [agg] | [diff] | [verdict] |
| [DIM-B*]  | [agg] | [agg] | [diff] | [verdict] |
| [DIM-C]   | [agg] | [agg] | [diff] | [verdict] |

**§17 rule result**: [HOLDS / CONDITIONAL / DEFEATED]

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

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO] | **g_null Override**: [N/A or justification]
**GClose Rationale**: [2-3 sentences.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [verdict] | [class] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger. Runs after BRACKET CLOSING. Applies §10, §10a, and §11.)*

### Surface Coverage *(per §10)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [ref] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [ref] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [ref] | [COVERED / GAP] |

**Surface coverage gate signal** *(informational)*: [COVERED / PARTIAL]

### Domain Coverage Gap-Check *(per §10a)*

*(Group §1 IN-SCOPE surfaces into artifact domains. For each domain, identify reviewer(s) with
HIGH applicability -- i.e., their lens.verify entries directly target that domain's concerns.)*

| Artifact Domain | Reviewer(s) with HIGH Applicability | Coverage |
|----------------|-------------------------------------|----------|
| [DOMAIN-1 -- derived from §1 surfaces] | [ROLE or "none"] | [COVERED / ADVISORY-GAP] |
| [DOMAIN-2] | [ROLE or "none"] | [COVERED / ADVISORY-GAP] |
| [DOMAIN-3 if applicable] | [ROLE or "none"] | [COVERED / ADVISORY-GAP] |

*(ADVISORY-GAP domains -> ACTION ITEM REGISTER:
"DOMAIN COVERAGE GAP-CHECK / [domain name] / no HIGH-applicability reviewer assigned")*

**§11 ADVISORY-ORPHAN check**: [List findings lacking §1 citation, or "None detected."]

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
**Convergence**: [Independently named concerns.]
**Scope coverage**: [Uncovered surfaces. If all: "None."]

**§13 PROGRESSION LEDGER**:
```
g_null(initial)     = [copy from BRACKET OPENING]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING]
Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
                     DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

---

## DISPOSITION

**Gate vector**: GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]

**Apply §3 formula**: GClose=FAIL->BLOCKED | Gi=FAIL->BLOCKED | No FAIL+COND->CONDITIONAL | All PASS->READY

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Applying §16 rule**: [rule n + reason]
**Primary Driver**: [result]
**Conditions / Blocker**: [if applicable]
**RESOLUTION REGISTRY**: [table if CONDITIONAL; "N/A -- disposition is [value]" otherwise]

---

## ACTION ITEM REGISTER

| Source | CH-ID / Finding | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|--------|----------------|-----------------|------------------|------------|---------------------|
| [gate ledger] | -- | [verbatim local ledger rows] | [class] | [role] | [criterion] |
| [CH-ID] | CH-00n | [from PARTIAL/HOLDS] | [class] | [role] | [criterion] |
| [lens gap] | Q-n | [ADVISORY-OPEN-LENS] | ADVISORY | [role] | Address lens entry. |
| [scope gap] | -- | [ADVISORY-GAP: §1 surface] | ADVISORY | [role] | [criterion] |
| [domain gap] | -- | [ADVISORY-GAP: domain with no HIGH-applicability reviewer] | ADVISORY | [role] | Assign HIGH-applicability reviewer to cover [domain]. |
| [orphan] | -- | [ADVISORY-ORPHAN] | ADVISORY | [role] | Re-assign to valid §1 surface. |

---

**Artifact to review:**

{{artifact}}
