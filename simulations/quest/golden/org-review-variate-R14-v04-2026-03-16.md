## V-04 -- Combined: Role Manifest Applicability + §5.5 Domain Gap-Check (C-33 + C-34)

**Variation axis**: V-02 axis (ROLE MANIFEST APPLICABILITY MATRIX, C-33 front-loaded) combined
with V-03 axis (DOMAIN COVERAGE GAP-CHECK in §5.5, C-34). Single structural encoding for both:
applicability is pre-committed in ROLE MANIFEST; domain gap-check runs in §5.5 drawing on
ROLE MANIFEST ratings.

**Hypothesis**: C-33 and C-34 are logically coupled: C-34 (domain-inward gap-check) requires
knowing which reviewers have HIGH applicability per domain -- the same information C-33 requires
per lens entry. V-04 hypothesis: encoding both at the ROLE MANIFEST level (front-loaded before
any reviewer runs) creates a single source of truth. The §5.5 domain gap-check can then reference
the APPLICABILITY MATRIX directly: for each artifact domain, look up which ROLE MANIFEST rows
have HIGH applicability -- if none, it's ADVISORY-GAP. This is tighter than V-03 (which requires
the reviewer to re-assess applicability at §5.5 time) because the §5.5 domain gap-check becomes
a mechanical lookup against a pre-committed table rather than a fresh assessment.

The combination also creates forward traceability: APPLICABILITY MATRIX -> §15 (per-lens
status) -> §5.5 DOMAIN GAP-CHECK (per-domain aggregation). A scorer can verify:
(a) C-33: APPLICABILITY MATRIX row exists with HIGH/MEDIUM/LOW per lens entry.
(b) C-34: §5.5 DOMAIN COVERAGE GAP table references APPLICABILITY MATRIX rows.

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
  Challenge claims -> CH-IDs. Every downstream: CH-ID response table.
  PASS prohibited if any CH-ID = OPEN.

§6 -- LOCAL GATE LEDGER [IMMUTABLE]
  | Section | Gate | Verdict | Class | -- EXCLUDED: §3.5, §3.8, §5.5.

§7 -- SECTION ORDER [IMMUTABLE]
  1.ROLE MANIFEST (APPLICABILITY MATRIX required)
  2.BRACKET OPENING  3.DOMAIN(s)  3.5.DOMAIN-AGGREGATE  3.8.CH-ID SATURATION
  4.LIFECYCLE  5.BRACKET CLOSING
  5.5.SCOPE COVERAGE (surface table + DOMAIN COVERAGE GAP-CHECK)
  6.GATE VECTOR TABLE  7.CROSS-ROLE SIGNALS  8.DISPOSITION  9.ACTION ITEM REGISTER

§8 -- CH-ID SATURATION [IMMUTABLE]
  FULLY SATURATED: DOMAIN + LIFECYCLE responses. PASS prohibited without saturation or waiver.

§9 -- NULL HYPOTHESIS PROGRESSION [IMMUTABLE]
  g_null(initial) = §17 formula [BRACKET OPENING]
  g_null(post-domain) [§3.5] | g_null(final) [BRACKET CLOSING]
  GClose must equal g_null(final). Override: "g_null OVERRIDE: [justification]"

§10 -- SCOPE COVERAGE GATE [IMMUTABLE]
  §5.5 maps §1 surfaces to findings. GAP -> ADVISORY-GAP.
  §5.5 ALSO runs the DOMAIN COVERAGE GAP-CHECK per §10a.

§10a -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  Runs within §5.5, after the surface coverage table.
  Step 1: List each ARTIFACT DOMAIN (grouped from §1 IN-SCOPE surfaces).
  Step 2: For each domain, look up ROLE MANIFEST APPLICABILITY MATRIX rows where
          Artifact Applicability = HIGH and the domain falls within that lens entry's scope.
  Step 3: Classify:
    COVERED    = at least one APPLICABILITY MATRIX row with HIGH rating covers this domain.
    ADVISORY-GAP = no APPLICABILITY MATRIX row with HIGH rating covers this domain.
  Step 4: ADVISORY-GAP domains -> ACTION ITEM REGISTER:
    "DOMAIN COVERAGE GAP-CHECK / [domain] / no HIGH-applicability reviewer in APPLICABILITY MATRIX"
  Table: | Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
  This check is informational -- does not feed §3 formula.

§11 -- FINDING-SURFACE LINKAGE [IMMUTABLE]
  Each finding: [§1:S-n]. Missing = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY [IMMUTABLE]
  CONDITIONAL: RESOLUTION REGISTRY table. Else: "N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER [IMMUTABLE]
  CROSS-ROLE SIGNALS: initial/post-domain/final + trajectory label.

§14 -- FINDING SEVERITY AGGREGATION [IMMUTABLE]
  | # | §1 Surface | Finding | Severity | -- Section Severity = worst. Mechanical.

§15 -- LENS EXHAUSTION [IMMUTABLE]
  After findings: LENS COVERAGE TABLE:
    | # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
  Applicability from APPLICABILITY MATRIX -- cite row ID. Do not reassign.
  HIGH/MEDIUM OPEN -> ADVISORY-OPEN-LENS in register. LOW OPEN -> cite AM row, no register entry.

§16 -- PRIMARY DRIVER DERIVATION [IMMUTABLE]
  Precedence rule 1-9 (GClose=FAIL->BRACKET CLOSING ... all PASS->N/A). Mechanical.

§17 -- NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  BRACKET OPENING: NULL HYPOTHESIS DIMENSION TABLE before challenge claims.
  | Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
  NH Verdict: pos->FAVORS-BUILD; zero->NEUTRAL; neg->OPPOSES-BUILD. MUST-CLEAR (*).
  g_null rule: HOLDS/CONDITIONAL/DEFEATED. §9 Stage 1 = §17 output.

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

### APPLICABILITY MATRIX

*(Complete before BRACKET OPENING executes. Locked at this point. Cited by §15 and §10a.)*

Assign artifact-specific applicability tier per (role, lens.verify entry):
- **HIGH**: directly relevant; finding expected; OPEN -> ADVISORY-OPEN-LENS-REQUIRED
- **MEDIUM**: tangentially relevant; finding expected; OPEN -> ADVISORY-OPEN-LENS
- **LOW**: not applicable; OPEN acceptable; cite this row in §15 Finding Reference

| Row ID | Role | lens.verify Entry | Artifact Domain Covered | Artifact Applicability | Basis for Rating |
|--------|------|------------------|------------------------|----------------------|------------------|
| AM-01 | [DOMAIN ROLE] | [Full text entry 1] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-02 | [DOMAIN ROLE] | [Full text entry 2] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-03 | [DOMAIN ROLE] | [Full text entry 3 if present] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-04 | [LIFECYCLE ROLE] | [Full text entry 1] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-05 | [LIFECYCLE ROLE] | [Full text entry 2] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |

*(The "Artifact Domain Covered" column drives §10a DOMAIN COVERAGE GAP-CHECK in §5.5.
Add rows for every lens.verify entry from every assigned role. APPLICABILITY MATRIX is now locked.)*

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
**g_null(initial)** *(§9 Stage 1)*: [result]

**Challenge claims**:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

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

**Finding Severity Aggregation (per §14)**: worst([_]) = **Section Severity**: [HIGH / MEDIUM / LOW]

**Lens Coverage Table** *(per §15 -- cite APPLICABILITY MATRIX rows; do not reassign tiers)*:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [Full text entry 1] | AM-01: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n, or "AM-01: LOW, not applicable"] |
| Q-2 | [Full text entry 2] | AM-02: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n, or cite AM-02] |
| Q-3 | [Full text if present] | AM-03: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n, or cite AM-03] |

*(HIGH/MEDIUM OPEN -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.)*

**Recommendation**: [One concrete action.]

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
g_null(post-domain): §9 Stage 2
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

**Finding Severity Aggregation (per §14)**: worst([_]) = **Section Severity**: [HIGH / MEDIUM / LOW]

**Lens Coverage Table** *(per §15 -- cite APPLICABILITY MATRIX rows)*:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [entry 1] | AM-04: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or cite AM-04] |
| Q-2 | [entry 2] | AM-05: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or cite AM-05] |

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

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(§17 -- aggregate re-scores)*:

| Dimension | Current-State Score | Proposed-State Score | Differential | NH Verdict |
|-----------|--------------------|--------------------|--------------|------------|
| [DIM-A*]  | [agg] | [agg] | [diff] | [verdict] |
| [DIM-B*]  | [agg] | [agg] | [diff] | [verdict] |
| [DIM-C]   | [agg] | [agg] | [diff] | [verdict] |

**§17 result**: [HOLDS / CONDITIONAL / DEFEATED]

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

*(EXCLUDED from gate ledger. Applies §10, §10a, §11.)*

### Surface Coverage *(per §10)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [ref] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [ref] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [ref] | [COVERED / GAP] |

**Surface coverage gate signal** *(informational)*: [COVERED / PARTIAL]

### Domain Coverage Gap-Check *(per §10a -- references APPLICABILITY MATRIX)*

*(For each artifact domain, look up APPLICABILITY MATRIX rows with HIGH rating covering that domain.)*

| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|----------|
| [DOMAIN-1] | [AM-0n: [ROLE] / "none"] | [COVERED / ADVISORY-GAP] |
| [DOMAIN-2] | [AM-0n: [ROLE] / "none"] | [COVERED / ADVISORY-GAP] |
| [DOMAIN-3 if applicable] | [AM-0n or "none"] | [COVERED / ADVISORY-GAP] |

*(ADVISORY-GAP -> ACTION ITEM REGISTER: "DOMAIN COVERAGE GAP-CHECK / [domain] / no APPLICABILITY
MATRIX row with HIGH rating covers this domain")*

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
**Scope coverage**: [Uncovered surfaces or "None."]

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

**Apply §3 formula**: GClose=FAIL->BLOCKED | Gi=FAIL->BLOCKED | No FAIL+COND->CONDITIONAL | All PASS->READY

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Applying §16 rule**: [rule n + reason]
**Primary Driver**: [result]
**Conditions / Blocker**: [if applicable]
**RESOLUTION REGISTRY**: [table if CONDITIONAL; "N/A -- [value]" otherwise]

---

## ACTION ITEM REGISTER

| Source | CH-ID / Finding | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|--------|----------------|-----------------|------------------|------------|---------------------|
| [gate ledger] | -- | [verbatim local ledger rows] | [class] | [role] | [criterion] |
| [CH-ID] | CH-00n | [PARTIAL/HOLDS item] | [class] | [role] | [criterion] |
| [lens gap] | AM-0n | [ADVISORY-OPEN-LENS: HIGH/MEDIUM lens entry not addressed] | ADVISORY | [role] | Address [lens entry]. |
| [domain gap] | -- | [ADVISORY-GAP: domain with no HIGH-applicability MATRIX row] | ADVISORY | [role] | Add HIGH-applicability reviewer for [domain]. |
| [scope gap] | -- | [ADVISORY-GAP: §1 surface not covered] | ADVISORY | [role] | [criterion] |
| [orphan] | -- | [ADVISORY-ORPHAN] | ADVISORY | [role] | Re-assign to valid §1 surface. |

---

**Artifact to review:**

{{artifact}}
