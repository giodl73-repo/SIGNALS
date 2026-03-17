---
skill: quest-variate
skill_target: org-review
date: 2026-03-16
round: 16
rubric: org-review-rubric-v14-2026-03-16.md
variants: V-03 V-04 V-05
companion: org-review-variate-R16-v01-v02-2026-03-16.md
---

# org-review -- Variate R16 (V-03, V-04, V-05)

Companion file for V-01 and V-02. This file contains V-03 (single-axis) and V-04, V-05
(two-axis combinations).

- V-03: Lifecycle emphasis -- LIFECYCLE emits NH Dimension Score sub-table (candidate C-41)
- V-04: Output format + Lifecycle emphasis (V-02 global F-IDs + V-03 lifecycle NH emission)
- V-05: Inertia framing + Lifecycle emphasis (V-01 NH Charter + V-03 lifecycle NH emission)

---

## V-03

**Axis**: Lifecycle emphasis -- LIFECYCLE reviewer also emits an NH Dimension Scores
sub-table (parallel to C-40's requirement for DOMAIN sections). The §17 NH TABLE
AGGREGATION RULE is extended: Column B = avg(all DOMAIN B scores + LIFECYCLE B score);
Column C = avg(all DOMAIN C scores + LIFECYCLE C score). LIFECYCLE is now a full
participant in the NH evidence chain alongside domain reviewers.

**Hypothesis**: C-40 requires DOMAIN sections to emit NH score sub-tables so bracket
closing can aggregate mechanically. But LIFECYCLE's commitment-frame assessment of
Build vs. Best-Alt is currently excluded from the NH averaging chain -- bracket closing
must either infer lifecycle's NH perspective from prose or ignore it. Including lifecycle's
NH scores closes the last arm of the averaging chain. Candidate C-41: Universal Reviewer
NH Score Emission -- all verdict-emitting reviewer archetypes (DOMAIN and LIFECYCLE) emit
NH Dimension Score sub-tables; bracket closing averages all reviewer scores per dimension
without any prose extraction.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this acknowledgment block first:

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. If a field cannot be
filled, write `[N/A -- reason]`.

---

```
======================================================================
DISPOSITION_CONTRACT v1-LC (lifecycle-nh-emission variant)
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§17;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE (each surface carries [DOMAIN: label]; cited in §5.5 and §11):
  1. [SURFACE_1] [DOMAIN: label]
  2. [SURFACE_2] [DOMAIN: label]
  3. [SURFACE_3] [DOMAIN: label]
  (Add rows. Be exhaustive.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

§1 COMPLETE -- role selection, APPLICABILITY MATRIX, and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions commitment. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR exists Gi=FAIL
  CONDITIONAL <-- no FAIL, exists CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain rows). Single domain: direct pass-through.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section: "Contract: DISPOSITION_CONTRACT v1-LC"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  CH-IDs at BRACKET OPENING. Every downstream section carries CH-ID response table.
  PASS prohibited if any CH-ID = OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row: | Section | Gate | Verdict | Class | (FAIL->BLOCKED; COND->CONDITIONAL; PASS->ADVISORY)
  Emit at verdict-emitting sections. Assemble ACTION ITEM REGISTER by verbatim copy.
  Do NOT re-derive Gate Verdict or Class.
  EXCLUDED: §3.5, §3.8, §5.5.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1. ROLE MANIFEST + APPLICABILITY MATRIX
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
  Reordering violates this contract.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID has DOMAIN response before LIFECYCLE.
  FULLY SATURATED: DOMAIN + LIFECYCLE before BRACKET CLOSING.
  PASS prohibited without full saturation or waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = §17 formula [BRACKET OPENING]
  Stage 2: g_null(post-domain) [§3.5]: FAIL->FAIL | COND->max(initial,COND) | PASS->initial
  Stage 3: g_null(final) [BRACKET CLOSING]:
    FAIL->FAIL | COND->max(post-domain,COND) | PASS->post-domain
  GClose = g_null(final). Override: "g_null OVERRIDE: [justification]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps §1 surfaces to findings. COVERED or GAP. GAP -> ADVISORY-GAP. No ledger row.

§10a -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  Group §1 surfaces by [DOMAIN: label]. ADVISORY-GAP: no HIGH AM row -> ACTION ITEM REGISTER.
  Table: | Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding: "[§1:S-n]" citation. Missing = ADVISORY-ORPHAN -> ACTION ITEM REGISTER.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  CONDITIONAL disposition -> | Gate | Condition | Owner | Resolution Criterion | Status |

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS §13 sub-section:
    g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Findings: | # | §1 Surface | Finding | Severity |
  Section Severity = worst(individual severities). Apply mechanically.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  After findings, each DOMAIN and LIFECYCLE section emits LENS COVERAGE TABLE:
    | # | lens.verify Entry | Applicability (AM row + tier) | Status | Finding Ref |
  HIGH+OPEN -> ADVISORY-OPEN-LENS-REQUIRED; MEDIUM+OPEN -> ADVISORY-OPEN-LENS.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  1.GClose=FAIL->BRACKET CLOSING | 2.G_domain_agg=FAIL->DOMAIN | 3.G_lifecycle=FAIL->LIFECYCLE
  4.GOpen=FAIL->BRACKET OPENING | 5.GClose=COND->BRACKET CLOSING | 6.G_domain_agg=COND->DOMAIN
  7.G_lifecycle=COND->LIFECYCLE | 8.GOpen=COND->BRACKET OPENING | 9.all PASS->N/A

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]
  BRACKET OPENING table:
    | Dimension | A: SQ (0-10) | B: Build (0-10) | C: Best-Alt (0-10) | B-A | B-C | NH Verdict |
  NH Verdict: B>A AND B>C -> FAVORS-BUILD; B<A OR B<C -> OPPOSES-BUILD; else NEUTRAL.
  MUST-CLEAR (*). Min 3 dimensions.

  g_null rule:
    HOLDS (MUST-CLEAR OPPOSES-BUILD) | CONDITIONAL (no MUST-CLEAR OPP; count(OPP)>=count(FAV))
    | DEFEATED (count(FAV)>count(OPP))

  NH TABLE AGGREGATION RULE -- BRACKET CLOSING [IMMUTABLE, extended for v1-LC]:
    Column A: carry forward challenger opening value unchanged (control arm).
    Column B (Proposed-Build): avg(all DOMAIN B scores per dimension + LIFECYCLE B score).
    Column C (Best-Non-Build-Alt): avg(all DOMAIN C scores per dimension + LIFECYCLE C score).
  Read from DOMAIN and LIFECYCLE NH Dimension Score sub-tables. No prose extraction.

  NH SCORE EMISSION REQUIREMENT -- DOMAIN sections [pre-committed]:
    Each DOMAIN section MUST emit before its gate ledger row:
      | Dimension | B Score: Proposed-Build (0-10) | C Score: Best-Non-Build-Alt (0-10) |
    One row per §17 dimension.

  NH SCORE EMISSION REQUIREMENT -- LIFECYCLE section [pre-committed, v1-LC addition]:
    The LIFECYCLE section MUST ALSO emit before its gate ledger row:
      | Dimension | B Score: Proposed-Build (0-10) | C Score: Best-Non-Build-Alt (0-10) |
    One row per §17 dimension. LIFECYCLE's commitment-frame NH assessment included in
    column B and C averages at BRACKET CLOSING.

    Rationale: The lifecycle reviewer evaluates the artifact from a commitment and program
    frame. Their assessment of Build vs. Best-Alt across NH dimensions is independent
    evidence not captured by technical domain reviewers. Including it in the average makes
    the NH evaluation more representative.

======================================================================
END DISPOSITION_CONTRACT v1-LC
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

*(REQUIRED before BRACKET OPENING. Locked.)*

| Row ID | Role | lens.verify Entry | Artifact Domain | Applicability | Basis |
|--------|------|------------------|----------------|--------------|-------|
| AM-01 | [DOMAIN ROLE] | [entry 1] | [domain] | [HIGH/MED/LOW] | [reason] |
| AM-02 | [DOMAIN ROLE] | [entry 2] | [domain] | [HIGH/MED/LOW] | [reason] |
| AM-03 | [LIFECYCLE ROLE] | [entry 1] | [domain] | [HIGH/MED/LOW] | [reason] |
| AM-04 | [LIFECYCLE ROLE] | [entry 2] | [domain] | [HIGH/MED/LOW] | [reason] |

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1-LC

**Null hypothesis**: [What the team does today -- one sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table** *(>= 3 dimensions; distinct from §17)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|----------------|-----------|------------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17)*:

| Dimension | A: SQ (0-10) | B: Build (0-10) | C: Best-Alt (0-10) | B-A | B-C | NH Verdict |
|-----------|-------------|-----------------|-------------------|-----|-----|------------|
| [DIM-A*]  | [N] | [M] | [P] | [M-N] | [M-P] | [verdict] |
| [DIM-B*]  | [N] | [M] | [P] | [M-N] | [M-P] | [verdict] |
| [DIM-C]   | [N] | [M] | [P] | [M-N] | [M-P] | [verdict] |

**Applying §17 rule**:
```
MUST-CLEAR OPPOSES-BUILD: [list or "none"] | FAV=[N] OPP=[M]
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

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [verdict] | [class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-LC
Received GOpen: [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | Technical Response | Status |
|-------|----------------------|-------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Additional Findings** *(per §14 and §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-3 | [§1:S-n] | [FINDING_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**Lens Coverage Table** *(per §15)*:

| # | lens.verify Entry | Applicability (AM row) | Status | Finding Ref |
|---|------------------|----------------------|--------|-------------|
| Q-1 | [entry 1] | AM-01: [tier] | [ADDRESSED / OPEN] | [F-n or AM-01] |
| Q-2 | [entry 2] | AM-02: [tier] | [ADDRESSED / OPEN] | [F-n or AM-02] |

**NH Dimension Scores** *(per §17 DOMAIN NH SCORE EMISSION REQUIREMENT)*:

| Dimension | B Score: Proposed-Build (0-10) | C Score: Best-Non-Build-Alt (0-10) |
|-----------|-------------------------------|-------------------------------------|
| [DIM-A]   | [score] | [score] |
| [DIM-B]   | [score] | [score] |
| [DIM-C]   | [score] | [score] |

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's `lens.simplify`.]
**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [verdict] | [class] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT *(EXCLUDED from gate ledger)*

```
G_domain_agg = worst([DOMAIN verdict]) = [PASS / CONDITIONAL / FAIL]
g_null(post-domain): initial=[_] | G_domain_agg=[_] -> [HOLDS/CONDITIONAL/DEFEATED]
```

---

## §3.8 CH-ID SATURATION CHECK *(EXCLUDED from gate ledger)*

| CH-ID | DOMAIN Status | Pre-LIFECYCLE Saturation |
|-------|--------------|--------------------------|
| CH-001 | [copy] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED or N/A] |

*LIFECYCLE may proceed.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-LC
Received GOpen: [copy] | G_domain_agg: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | Commitment-Frame Response | Status |
|-------|----------------------|--------------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph. Reference GOpen, G_domain_agg,
g_null(post-domain) explicitly.]

**Null hypothesis status**: [yes / partial / no]

**Additional Findings** *(per §14 and §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**Lens Coverage Table** *(per §15)*:

| # | lens.verify Entry | Applicability (AM row) | Status | Finding Ref |
|---|------------------|----------------------|--------|-------------|
| Q-1 | [entry 1] | AM-03: [tier] | [ADDRESSED / OPEN] | [F-n or AM-03] |
| Q-2 | [entry 2] | AM-04: [tier] | [ADDRESSED / OPEN] | [F-n or AM-04] |

**NH Dimension Scores** *(per §17 LIFECYCLE NH SCORE EMISSION REQUIREMENT -- v1-LC addition)*:

*(Commitment-frame assessment of the proposed artifact vs. best non-build alternative
across the same dimensions as BRACKET OPENING. Consumed by BRACKET CLOSING §17 aggregation.)*

| Dimension | B Score: Proposed-Build (0-10) | C Score: Best-Non-Build-Alt (0-10) |
|-----------|-------------------------------|-------------------------------------|
| [DIM-A]   | [score -- lifecycle's commitment-frame view] | [score] |
| [DIM-B]   | [score] | [score] |
| [DIM-C]   | [score] | [score] |

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's `lens.simplify`.]
**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [verdict] | [class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1-LC
*Full record received: scope, APPLICABILITY MATRIX, all DOMAIN NH scores, LIFECYCLE NH scores.*

**Applying §9 Stage 3**:
```
g_null(post-domain)=[copy] | G_lifecycle=[copy]
  FAIL->FAIL | COND->max(post-domain,COND) | PASS->post-domain
g_null(final) = [HOLDS / CONDITIONAL / DEFEATED]
```

**Revised NH DIMENSION TABLE** *(§17 aggregation -- DOMAIN + LIFECYCLE NH score sub-tables)*:

```
Column B aggregation per dimension (avg DOMAIN B scores + LIFECYCLE B score):
  [DIM-A]: DOMAIN=[score], LIFECYCLE=[score] -> avg=[result]
  [DIM-B]: DOMAIN=[score], LIFECYCLE=[score] -> avg=[result]
  [DIM-C]: DOMAIN=[score], LIFECYCLE=[score] -> avg=[result]

Column C aggregation per dimension (avg DOMAIN C scores + LIFECYCLE C score):
  [DIM-A]: DOMAIN=[score], LIFECYCLE=[score] -> avg=[result]
  [DIM-B]: DOMAIN=[score], LIFECYCLE=[score] -> avg=[result]
  [DIM-C]: DOMAIN=[score], LIFECYCLE=[score] -> avg=[result]

Column A: carry forward from BRACKET OPENING (control arm).
```

| Dimension | A: SQ | B: Build (agg D+L) | C: Best-Alt (agg D+L) | B-A | B-C | NH Verdict |
|-----------|-------|--------------------|-----------------------|-----|-----|------------|
| [DIM-A*]  | [carry] | [agg] | [agg] | [diff] | [diff] | [verdict] |
| [DIM-B*]  | [carry] | [agg] | [agg] | [diff] | [diff] | [verdict] |
| [DIM-C]   | [carry] | [agg] | [agg] | [diff] | [diff] | [verdict] |

*(Column B and C aggregations include both DOMAIN and LIFECYCLE sub-table scores per §17.)*

**Applying §17 rule to revised table**:
```
MUST-CLEAR OPPOSES-BUILD: [list or "none"] | FAV=[N] OPP=[M]
-> [HOLDS / CONDITIONAL / DEFEATED]
```

**Full CH-ID Saturation**:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver |
|-------|--------------|-----------------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A] |

**CH-ID Final Assessment**:

| CH-ID | G_domain | G_lifecycle | Final Status | Notes |
|-------|----------|-------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [All defeated, or list.]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A or justification]
**GClose Rationale**: [2-3 sentences. Reference g_null(final), CH-ID saturation,
NH trajectory including lifecycle NH scores.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [verdict] | [class] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION *(EXCLUDED from gate ledger)*

### Surface Coverage *(per §10)*

| IN-SCOPE Surface | Domain | Reviewer(s) | Finding Ref | Coverage |
|-----------------|--------|-------------|-------------|---------|
| [SURFACE_1] | [domain] | [ROLE] | [F-n or "none"] | [COVERED / GAP] |
| [SURFACE_2] | [domain] | [ROLE] | [F-n or "none"] | [COVERED / GAP] |
| [SURFACE_3] | [domain] | [ROLE] | [F-n or "none"] | [COVERED / GAP] |

**Surface coverage signal**: [COVERED / PARTIAL]

### Domain Coverage Gap-Check *(per §10a)*

| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|---------|
| [DOMAIN-1] | [AM-0n / "none"] | [COVERED / ADVISORY-GAP] |

### §11 ADVISORY-ORPHAN Check

**Findings missing §1 citation**: [List or "None."]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER_ROLE] | [copy] | DISPOSITION_CONTRACT v1-LC |
| G_domain_agg | [DOMAIN_ROLE] | [copy] | DISPOSITION_CONTRACT v1-LC |
| G_lifecycle | [LIFECYCLE_ROLE] | [copy] | DISPOSITION_CONTRACT v1-LC |
| GClose | [CHALLENGER_ROLE] | [copy] | DISPOSITION_CONTRACT v1-LC |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Incompatible responses. If none: "None."]
**Convergence**: [Concern named by >= 2 reviewers.]
**Scope coverage**: [Uncovered surfaces. If all covered: "None."]

**§13 PROGRESSION LEDGER**:
```
g_null(initial)=[_] | g_null(post-domain)=[_] | g_null(final)=[_]
Trajectory=[label]
```

**NH trajectory with lifecycle**: [One sentence noting whether LIFECYCLE NH scores
raised or lowered the aggregated B and C values relative to DOMAIN-only averages.]

---

## DISPOSITION

**Gate vector**: GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]

```
GClose=FAIL? -> BLOCKED | Any Gi=FAIL? -> BLOCKED
No FAIL + any COND? -> CONDITIONAL | All PASS? -> READY
```
**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Applying §16 rule**: [n]  **Primary Driver**: [result]

**Conditions** *(CONDITIONAL)*: [conditions]
**Blocker** *(BLOCKED)*: [blocker]

**RESOLUTION REGISTRY** *(CONDITIONAL only)*:
| Gate | Condition | Owner | Resolution Criterion | Status |
|------|-----------|-------|---------------------|--------|
| [gate] | [summary] | [role] | [test] | OPEN |

---

## ACTION ITEM REGISTER

*Assembly per §6: verbatim gate ledger rows, then CH-ID items, lens gaps, scope gaps,
domain gaps, orphans. Do NOT re-derive.*

| Source | CH-ID / Finding | Item Description | Disposition Class | Owner | Resolution Criterion |
|--------|----------------|-----------------|------------------|-------|---------------------|
| [gate ledger] | -- | [verbatim row] | [class] | [ROLE] | [criterion] |
| [CH-ID item] | CH-00n | [What must be done] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE] | [criterion] |
| [lens HIGH] | AM-0n / Q-n | ADVISORY-OPEN-LENS-REQUIRED: [entry] | ADVISORY | [ROLE] | Produce finding. |
| [scope gap] | -- | ADVISORY-GAP: §1 [surface] | ADVISORY | [ROLE] | Assign reviewer. |
| [domain gap] | -- | ADVISORY-GAP (DOMAIN): [domain] | ADVISORY | [ROLE] | Add reviewer. |

---

**Artifact to review:**

{{artifact}}

---
---

## V-04

**Axes**: Output format + Lifecycle emphasis (V-02 global F-IDs + V-03 LIFECYCLE NH
score emission combined).

**Hypothesis**: The two R16 chains are independent:
- F-ID chain: findings -> global registry -> action register (V-02)
- NH score chain: DOMAIN + LIFECYCLE NH sub-tables -> bracket closing aggregation (V-03)
V-04 tests whether they compose without structural conflict. Both §17 aggregation (extended
to include lifecycle) and §18 global finding registry can coexist in the same prompt.
Combined candidate: F-IDs reference findings in all sections including those that also
emit NH sub-tables; NH sub-tables are a structured emission separate from the finding table.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this acknowledgment block first:

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. If a field cannot be
filled, write `[N/A -- reason]`. F-IDs are globally sequential across all sections.

---

```
======================================================================
DISPOSITION_CONTRACT v1-FL (fid + lifecycle-nh-emission variant)
[IMMUTABLE -- complete §1; do not alter §2-§18; reviewer sections blocked until §1 COMPLETE]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE (each surface [DOMAIN: label]; cited §5.5, §11):
  1. [SURFACE_1] [DOMAIN: label]
  2. [SURFACE_2] [DOMAIN: label]
  3. [SURFACE_3] [DOMAIN: label]
  (Add rows.)
OUT-OF-SCOPE: 1. [SURFACE -- REASON]
§1 COMPLETE

§2 SEVERITY: HIGH=blocks | MEDIUM=conditions | LOW=advisory

§3 DISPOSITION ALGEBRA [IMMUTABLE]:
  BLOCKED <-- GClose=FAIL OR Gi=FAIL | CONDITIONAL <-- no FAIL+COND | READY <-- all PASS

§3a DOMAIN-AGGREGATE: worst(G_domain rows). Single: direct pass-through.

§4 CONTRACT CITE: "Contract: DISPOSITION_CONTRACT v1-FL" in each reviewer section.

§5 CH-ID TRACING: CH-IDs at BRACKET OPENING; CH-ID response tables downstream.
   PASS prohibited if CH-ID=OPEN.

§6 LOCAL GATE LEDGER [IMMUTABLE]: | Section | Gate | Verdict | Class |
   Class: FAIL->BLOCKED; COND->CONDITIONAL; PASS->ADVISORY.
   Emit at verdict sections. Assemble ACTION ITEM REGISTER verbatim. No re-derivation.
   EXCLUDED: §3.5, §3.8, §5.5.

§7 SECTION ORDER [IMMUTABLE]:
  1.ROLE MANIFEST+APPLICABILITY MATRIX  2.BRACKET OPENING  3.DOMAIN(s)
  3.5.DOMAIN-AGGREGATE CHECKPOINT  3.8.CH-ID SATURATION CHECK  4.LIFECYCLE
  5.BRACKET CLOSING  5.5.SCOPE COVERAGE RECONCILIATION (includes §18)
  6.GATE VECTOR TABLE  7.CROSS-ROLE SIGNALS  8.DISPOSITION  9.ACTION ITEM REGISTER

§8 CH-ID SATURATION: SATURATED(DOMAIN before LIFECYCLE); FULLY SATURATED(D+L before CLOSING).
   PASS prohibited without full saturation or waiver.

§9 NULL HYPOTHESIS PROGRESSION [IMMUTABLE]:
  Stage 1: g_null(initial)=§17 formula [BRACKET OPENING]
  Stage 2: g_null(post-domain) [§3.5]: FAIL->FAIL|COND->max(init,COND)|PASS->init
  Stage 3: g_null(final) [BRACKET CLOSING]: FAIL->FAIL|COND->max(post,COND)|PASS->post
  GClose=g_null(final) or "g_null OVERRIDE:[justification]"

§10 SCOPE COVERAGE: §5.5 maps §1 surfaces to F-IDs. COVERED(>=1 F-ID)|GAP->ADVISORY-GAP.
§10a DOMAIN GAP-CHECK: ADVISORY-GAP domains->ACTION ITEM REGISTER.
§11 FINDING-SURFACE LINKAGE: "[§1:S-n]" on each finding. Missing->ADVISORY-ORPHAN.
§12 CONDITIONAL RESOLUTION REGISTRY: emit table if CONDITIONAL disposition.
§13 g_null PROGRESSION LEDGER: in CROSS-ROLE SIGNALS.
§14 FINDING SEVERITY AGGREGATION: | F-ID | §1 Surface | Finding | Severity |
    F-IDs globally sequential. Section Severity=worst(individual).
§15 LENS EXHAUSTION: LENS COVERAGE TABLE after findings; Finding F-ID column cites global F-ID.
§16 PRIMARY DRIVER: [9-rule precedence -- same as v1-LC §16]

§17 NH DIMENSION TABLE [IMMUTABLE]:
  BRACKET OPENING: | Dimension | A:SQ | B:Build | C:Best-Alt | B-A | B-C | NH Verdict |
  Rule: MUST-CLEAR OPPOSES-BUILD->HOLDS; count(OPP)>=count(FAV)->CONDITIONAL; else DEFEATED.

  NH TABLE AGGREGATION (BRACKET CLOSING, pre-committed):
    Col A: carry forward.
    Col B: avg(all DOMAIN B + LIFECYCLE B per dimension). Read from sub-tables.
    Col C: avg(all DOMAIN C + LIFECYCLE C per dimension). Read from sub-tables.

  DOMAIN NH SCORE EMISSION (pre-committed):
    Each DOMAIN section emits before gate ledger:
      | Dimension | B Score (0-10) | C Score (0-10) |

  LIFECYCLE NH SCORE EMISSION (pre-committed, v1-FL addition):
    LIFECYCLE section emits before gate ledger:
      | Dimension | B Score (0-10) | C Score (0-10) |
    Lifecycle's commitment-frame NH scores included in Col B and Col C averages.

§18 GLOBAL FINDING REGISTRY [IMMUTABLE]:
  Every finding: globally unique sequential F-ID (F-001, F-002, ...). No reuse.
  At §5.5 assemble: | F-ID | Section | §1 Surface | Severity | Register Status |
  Register Status: ACTIONED|WAIVED|ADVISORY. HIGH/MEDIUM with ADVISORY = contract violation.
  ACTION ITEM REGISTER cites F-IDs. Bidirectional traceability without reviewer narrative.

======================================================================
END DISPOSITION_CONTRACT v1-FL
======================================================================
```

---

## ROLE MANIFEST

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

### APPLICABILITY MATRIX *(locked before BRACKET OPENING)*

| Row ID | Role | lens.verify Entry | Artifact Domain | Applicability | Basis |
|--------|------|------------------|----------------|--------------|-------|
| AM-01 | [DOMAIN] | [entry 1] | [domain] | [tier] | [reason] |
| AM-02 | [DOMAIN] | [entry 2] | [domain] | [tier] | [reason] |
| AM-03 | [LIFECYCLE] | [entry 1] | [domain] | [tier] | [reason] |
| AM-04 | [LIFECYCLE] | [entry 2] | [domain] | [tier] | [reason] |

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1-FL

**Null hypothesis**: [One sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table** *(>= 3 dimensions)*:

| Dimension | Status Quo (A) | Build (B) | Best Alt (C) | Notes |
|-----------|----------------|-----------|--------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NH DIMENSION TABLE** *(per §17)*:

| Dimension | A: SQ | B: Build | C: Best-Alt | B-A | B-C | NH Verdict |
|-----------|-------|----------|-------------|-----|-----|------------|
| [DIM-A*] | [N] | [M] | [P] | [M-N] | [M-P] | [verdict] |
| [DIM-B*] | [N] | [M] | [P] | [M-N] | [M-P] | [verdict] |
| [DIM-C]  | [N] | [M] | [P] | [M-N] | [M-P] | [verdict] |

```
MUST-CLEAR OPP: [list/"none"] | FAV=[N] OPP=[M] -> [HOLDS/CONDITIONAL/DEFEATED]
```
**g_null(initial)**: [verdict]

**Challenge claims**:

| CH-ID | Claim | Severity |
|-------|-------|---------|
| CH-001 | [CLAIM_1] | [tier] |
| CH-002 | [CLAIM_2] | [tier] |
| CH-003 | [optional] | [tier] |

**GOpen Verdict**: [verdict] | **GOpen Reason**: [one sentence]

*F-ID counter: BRACKET OPENING emits no findings. DOMAIN starts at F-001.*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [verdict] | [class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-FL
Received GOpen: [copy]
*F-ID counter: starts at F-001.*

**CH-ID Response Table**:

| CH-ID | Claim (copy) | Technical Response | Status |
|-------|-------------|-------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |
| CH-003 | [copy if active] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |

**Additional Findings** *(per §14, §11, §18 -- global F-IDs)*:

| F-ID | §1 Surface | Finding | Severity |
|------|-----------|---------|---------|
| F-001 | [§1:S-n] | [FINDING_1] | [tier] |
| F-002 | [§1:S-n] | [FINDING_2] | [tier] |
| F-003 | [§1:S-n] | [FINDING_3 -- optional] | [tier] |

**Section Severity**: worst(F-001=[_], F-002=[_]) = [tier]

**Lens Coverage Table** *(cite F-IDs)*:

| # | lens.verify Entry | Applicability | Status | F-ID |
|---|------------------|--------------|--------|------|
| Q-1 | [entry 1] | AM-01: [tier] | [ADDRESSED/OPEN] | [F-00n/AM-01] |
| Q-2 | [entry 2] | AM-02: [tier] | [ADDRESSED/OPEN] | [F-00n/AM-02] |

**NH Dimension Scores** *(per §17 DOMAIN emission)*:

| Dimension | B Score (0-10) | C Score (0-10) |
|-----------|---------------|---------------|
| [DIM-A] | [score] | [score] |
| [DIM-B] | [score] | [score] |
| [DIM-C] | [score] | [score] |

**Recommendation**: [One action.]
**G_domain Verdict**: [verdict] | **G_domain Reason**: [one sentence]

*F-ID counter after DOMAIN: [F-00n]. LIFECYCLE starts at [F-00n+1].*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [verdict] | [class] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT *(EXCLUDED from gate ledger)*

```
G_domain_agg=[verdict] | g_null(post-domain): [init]->[G_domain_agg]->[result]
```

---

## §3.8 CH-ID SATURATION CHECK *(EXCLUDED from gate ledger)*

| CH-ID | DOMAIN | Pre-LIFECYCLE Saturation |
|-------|--------|--------------------------|
| CH-001 | [copy] | [SATURATED/UNSATURATED] |
| CH-002 | [copy] | [SATURATED/UNSATURATED] |

*LIFECYCLE may proceed.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-FL
Received GOpen: [copy] | G_domain_agg: [copy] | g_null(post-domain): [copy]

*F-ID counter continues from [F-00n].*

**CH-ID Response Table**:

| CH-ID | Claim (copy) | Commitment-Frame Response | Status |
|-------|-------------|--------------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |
| CH-003 | [copy if active] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |

**Decision-readiness assessment**: [Paragraph referencing GOpen, G_domain_agg, g_null(post-domain).]
**Null hypothesis status**: [yes / partial / no]

**Additional Findings** *(per §14, §11, §18 -- continue F-ID counter)*:

| F-ID | §1 Surface | Finding | Severity |
|------|-----------|---------|---------|
| F-00n | [§1:S-n] | [FINDING_1] | [tier] |
| F-00n+1 | [§1:S-n] | [FINDING_2] | [tier] |

**Section Severity**: worst(F-00n=[_], F-00n+1=[_]) = [tier]

**Lens Coverage Table** *(cite F-IDs)*:

| # | lens.verify Entry | Applicability | Status | F-ID |
|---|------------------|--------------|--------|------|
| Q-1 | [entry 1] | AM-03: [tier] | [ADDRESSED/OPEN] | [F-00n/AM-03] |
| Q-2 | [entry 2] | AM-04: [tier] | [ADDRESSED/OPEN] | [F-00n/AM-04] |

**NH Dimension Scores** *(per §17 LIFECYCLE NH SCORE EMISSION -- v1-FL)*:

| Dimension | B Score (0-10) | C Score (0-10) |
|-----------|---------------|---------------|
| [DIM-A] | [score] | [score] |
| [DIM-B] | [score] | [score] |
| [DIM-C] | [score] | [score] |

**Recommendation**: [One action.]
**G_lifecycle Verdict**: [verdict] | **G_lifecycle Reason**: [one sentence]

*F-ID counter after LIFECYCLE: [F-00n]. Counter closes.*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [verdict] | [class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1-FL
*Full record: all F-IDs, all NH sub-tables (DOMAIN + LIFECYCLE), all gates, all CH-IDs.*

**Applying §9 Stage 3**:
```
g_null(post-domain)=[_] | G_lifecycle=[_] -> g_null(final)=[HOLDS/CONDITIONAL/DEFEATED]
```

**Revised NH DIMENSION TABLE** *(§17 aggregation from DOMAIN + LIFECYCLE sub-tables)*:

```
Col B = avg(DOMAIN B + LIFECYCLE B):
  DIM-A: D=[_] L=[_] -> avg=[_] | DIM-B: D=[_] L=[_] -> avg=[_] | DIM-C: D=[_] L=[_] -> avg=[_]
Col C = avg(DOMAIN C + LIFECYCLE C):
  DIM-A: D=[_] L=[_] -> avg=[_] | DIM-B: D=[_] L=[_] -> avg=[_] | DIM-C: D=[_] L=[_] -> avg=[_]
Col A: carry forward.
```

| Dimension | A | B (agg D+L) | C (agg D+L) | B-A | B-C | NH Verdict |
|-----------|---|-------------|-------------|-----|-----|------------|
| [DIM-A*] | [carry] | [agg] | [agg] | [diff] | [diff] | [verdict] |
| [DIM-B*] | [carry] | [agg] | [agg] | [diff] | [diff] | [verdict] |
| [DIM-C]  | [carry] | [agg] | [agg] | [diff] | [diff] | [verdict] |

```
MUST-CLEAR OPP: [list/"none"] | FAV=[N] OPP=[M] -> [HOLDS/CONDITIONAL/DEFEATED]
```

**Full CH-ID Saturation**:

| CH-ID | DOMAIN | LIFECYCLE | Full Saturation | Waiver |
|-------|--------|-----------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED/UNSATURATED] | [N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED/UNSATURATED] | [N/A] |

**CH-ID Final Assessment**:

| CH-ID | G_domain | G_lifecycle | Final | Notes |
|-------|----------|-------------|-------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |

**GClose Verdict**: [verdict] | **Override invoked**: [YES/NO]
**g_null Override**: [N/A or justification]
**GClose Rationale**: [2-3 sentences.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [verdict] | [class] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION *(EXCLUDED from gate ledger)*

### Surface Coverage *(cite F-IDs)*

| IN-SCOPE Surface | Domain | Reviewer | F-ID(s) | Coverage |
|-----------------|--------|---------|---------|---------|
| [SURFACE_1] | [dom] | [ROLE] | [F-00n/"none"] | [COVERED/GAP] |
| [SURFACE_2] | [dom] | [ROLE] | [F-00n/"none"] | [COVERED/GAP] |

### Domain Coverage Gap-Check | Artifact Domain | HIGH AM Rows | Coverage |

### §11 ADVISORY-ORPHAN Check: [F-IDs missing §1 citation or "None."]

### §18 GLOBAL FINDING REGISTRY

| F-ID | Section | §1 Surface | Severity | Register Status |
|------|---------|-----------|---------|----------------|
| F-001 | DOMAIN | [§1:S-n] | [tier] | [ACTIONED/WAIVED/ADVISORY] |
| F-002 | DOMAIN | [§1:S-n] | [tier] | [ACTIONED/WAIVED/ADVISORY] |
| F-00n | LIFECYCLE | [§1:S-n] | [tier] | [ACTIONED/WAIVED/ADVISORY] |

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Cite |
|------|----------|---------|------|
| GOpen | [CHALLENGER] | [copy] | v1-FL |
| G_domain_agg | [DOMAIN] | [copy] | v1-FL |
| G_lifecycle | [LIFECYCLE] | [copy] | v1-FL |
| GClose | [CHALLENGER] | [copy] | v1-FL |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [or "None."] | **Convergence**: [cite F-IDs] | **Scope coverage**: [or "None."]

**§13 PROGRESSION LEDGER**: g_null(initial)=[_] | post-domain=[_] | final=[_] | Trajectory=[label]

---

## DISPOSITION

**Gate vector**: GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]

```
GClose=FAIL->BLOCKED | Gi=FAIL->BLOCKED | no FAIL+COND->CONDITIONAL | all PASS->READY
```
**Overall Disposition**: [verdict]
**Applying §16 rule**: [n]  **Primary Driver**: [result]
**Conditions/Blocker**: [if applicable]
**RESOLUTION REGISTRY**: [table if CONDITIONAL, else "N/A"]

---

## ACTION ITEM REGISTER

| Source | CH-ID / F-ID | Item | Disposition Class | Owner | Criterion |
|--------|-------------|------|------------------|-------|-----------|
| [gate ledger] | -- | [verbatim] | [class] | [ROLE] | [criterion] |
| [finding HIGH/MED] | F-00n | [action] | [BLOCKED/CONDITIONAL] | [ROLE] | [criterion] |
| [lens gap] | AM-0n/Q-n | ADVISORY-OPEN-LENS[-REQUIRED]: [entry] | ADVISORY | [ROLE] | Produce finding. |
| [scope gap] | -- | ADVISORY-GAP: [surface] | ADVISORY | [ROLE] | Assign reviewer. |
| [domain gap] | -- | ADVISORY-GAP (DOMAIN): [domain] | ADVISORY | [ROLE] | Add reviewer. |

---

**Artifact to review:**

{{artifact}}

---
---

## V-05

**Axes**: Inertia framing + Lifecycle emphasis (V-01 §0 NULL HYPOTHESIS CHARTER + V-03
LIFECYCLE NH score emission combined).

**Hypothesis**: The §0 Charter pre-commits the strongest case for doing nothing and names
the evidence threshold. LIFECYCLE's NH score emission (V-03) provides a commitment-frame
quantitative assessment of Build vs. Best-Alt. Together they close two independent gaps:
- Charter ensures the reviewer record explicitly maps to the pre-stated status-quo arguments
- LIFECYCLE NH scores ensure the NH aggregation chain includes commitment-frame evidence

The combined architecture tests whether the §0 Charter reference requirement (V-01) and
the LIFECYCLE NH sub-table (V-03) are compatible -- both operate before BRACKET CLOSING
and their outputs feed separate slots of the closing reassessment. Candidate C-41: either
Charter completeness or Universal NH emission or both, confirmed as composable.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this acknowledgment block first:

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. If a field cannot be
filled, write `[N/A -- reason]`.

---

```
======================================================================
§0 -- NULL HYPOTHESIS CHARTER [IMMUTABLE -- complete before DISPOSITION_CONTRACT]
======================================================================

Status-quo name: [What the team does today -- one phrase]

Strongest case for doing nothing:
  Arg-1: [Best argument -- switching cost, workaround viability, or adoption friction.]
  Arg-2: [Second argument.]
  Arg-3: [Third argument -- or "N/A".]

Evidence threshold (pre-committed):
  DEFEATED: all §0 arguments addressed or shown LOW-impact.
  Partial defeat: >= 2/3 addressed with no HIGH-severity unaddressed argument.

Charter reference requirement (pre-committed):
  Each reviewer section MUST include:
    §0 Charter: [§0:Arg-n, §0:Arg-n] -- [one sentence]
    OR: §0 Charter: [§0: None] -- no Charter argument addressed
  Missing reference = CHARTER-GAP.

CH-ID grounding: each CH-ID must state "CH-00n grounds §0:Arg-n"

§0 COMPLETE.
======================================================================
```

---

```
======================================================================
DISPOSITION_CONTRACT v1-NL (nh-charter + lifecycle-nh-emission variant)
[IMMUTABLE -- complete §1; do not alter §2-§17; blocked until §1 COMPLETE]
======================================================================

§1 SCOPE ENUMERATION
IN-SCOPE (each surface [DOMAIN: label]; cited §5.5, §11):
  1. [SURFACE_1] [DOMAIN: label]
  2. [SURFACE_2] [DOMAIN: label]
  3. [SURFACE_3] [DOMAIN: label]
OUT-OF-SCOPE: 1. [SURFACE -- REASON]
§1 COMPLETE

§2 SEVERITY: HIGH=blocks | MEDIUM=conditions | LOW=advisory

§3 DISPOSITION ALGEBRA [IMMUTABLE]:
  BLOCKED(GClose=FAIL OR Gi=FAIL) | CONDITIONAL(no FAIL+COND) | READY(all PASS)
§3a DOMAIN-AGGREGATE: worst(G_domain). Single: pass-through.

§4 CONTRACT CITE: "Contract: DISPOSITION_CONTRACT v1-NL"

§5 CH-ID TRACING: CH-IDs at BRACKET OPENING; response tables downstream.
   PASS prohibited if CH-ID=OPEN. Each CH-ID states "grounds §0:Arg-n"

§6 LOCAL GATE LEDGER [IMMUTABLE]: | Section | Gate | Verdict | Class |
   Class: FAIL->BLOCKED; COND->CONDITIONAL; PASS->ADVISORY.
   Emit at verdict sections. Assemble ACTION ITEM REGISTER verbatim. No re-derivation.
   EXCLUDED: §3.5, §3.8, §5.5.

§7 SECTION ORDER [IMMUTABLE]:
  0.§0 CHARTER(complete)  1.ROLE MANIFEST+APPLICABILITY MATRIX  2.BRACKET OPENING
  3.DOMAIN(s)  3.5.DOMAIN-AGGREGATE CHECKPOINT  3.8.CH-ID SATURATION CHECK  4.LIFECYCLE
  5.BRACKET CLOSING  5.5.SCOPE COVERAGE RECONCILIATION  6.GATE VECTOR TABLE
  7.CROSS-ROLE SIGNALS  8.DISPOSITION  9.ACTION ITEM REGISTER

§8 CH-ID SATURATION: SATURATED(DOMAIN before LIFECYCLE); FULLY SATURATED(D+L before CLOSING).
   PASS prohibited without full saturation or waiver.

§9 NULL HYPOTHESIS PROGRESSION [IMMUTABLE]:
  Stage 1: g_null(initial)=§17 formula [BRACKET OPENING]
  Stage 2: g_null(post-domain) [§3.5]: FAIL|max(init,COND)|init
  Stage 3: g_null(final) [BRACKET CLOSING]: FAIL|max(post,COND)|post
  GClose=g_null(final) or "g_null OVERRIDE:[justification]"

§10 SCOPE COVERAGE: §5.5; COVERED(>=1 finding)|GAP->ADVISORY-GAP.
§10a DOMAIN GAP-CHECK: ADVISORY-GAP domains->ACTION ITEM REGISTER.
§11 FINDING-SURFACE LINKAGE: "[§1:S-n]" on each finding. Missing->ADVISORY-ORPHAN.
§12 CONDITIONAL RESOLUTION REGISTRY: table if CONDITIONAL.
§13 g_null PROGRESSION LEDGER: in CROSS-ROLE SIGNALS.
§14 FINDING SEVERITY AGGREGATION: | # | §1 Surface | Finding | Severity |
    Section Severity=worst(individual). Apply mechanically.
§15 LENS EXHAUSTION: LENS COVERAGE TABLE after findings. HIGH+OPEN->ADVISORY-OPEN-LENS-REQUIRED.
§16 PRIMARY DRIVER: 9-rule precedence formula.

§17 NH DIMENSION TABLE [IMMUTABLE]:
  BRACKET OPENING: | Dimension | A:SQ | B:Build | C:Best-Alt | B-A | B-C | NH Verdict |
  Rule: MUST-CLEAR OPP->HOLDS; count(OPP)>=count(FAV)->CONDITIONAL; else DEFEATED.

  NH TABLE AGGREGATION (BRACKET CLOSING, pre-committed):
    Col A: carry forward.
    Col B: avg(all DOMAIN B + LIFECYCLE B per dimension). From sub-tables only.
    Col C: avg(all DOMAIN C + LIFECYCLE C per dimension). From sub-tables only.

  DOMAIN NH SCORE EMISSION (pre-committed):
    Each DOMAIN emits before gate ledger:
      | Dimension | B Score (0-10) | C Score (0-10) |

  LIFECYCLE NH SCORE EMISSION (pre-committed, v1-NL):
    LIFECYCLE emits before gate ledger:
      | Dimension | B Score (0-10) | C Score (0-10) |
    Included in Col B and C averages.

======================================================================
END DISPOSITION_CONTRACT v1-NL
======================================================================
```

---

## ROLE MANIFEST

| Slot | Archetype | Role | Rationale |
|------|-----------|------|-----------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

### APPLICABILITY MATRIX *(locked before BRACKET OPENING)*

| Row ID | Role | lens.verify Entry | Artifact Domain | Applicability | Basis |
|--------|------|------------------|----------------|--------------|-------|
| AM-01 | [DOMAIN] | [entry 1] | [domain] | [tier] | [reason] |
| AM-02 | [DOMAIN] | [entry 2] | [domain] | [tier] | [reason] |
| AM-03 | [LIFECYCLE] | [entry 1] | [domain] | [tier] | [reason] |
| AM-04 | [LIFECYCLE] | [entry 2] | [domain] | [tier] | [reason] |

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1-NL
§0 Charter: [§0:Arg-n, §0:Arg-n] -- [which arguments this section addresses]

**Null hypothesis**: [One sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table** *(>= 3 dimensions)*:

| Dimension | Status Quo (A) | Build (B) | Best Alt (C) | Notes |
|-----------|----------------|-----------|--------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NH DIMENSION TABLE** *(per §17)*:

| Dimension | A: SQ | B: Build | C: Best-Alt | B-A | B-C | NH Verdict |
|-----------|-------|----------|-------------|-----|-----|------------|
| [DIM-A*] | [N] | [M] | [P] | [M-N] | [M-P] | [verdict] |
| [DIM-B*] | [N] | [M] | [P] | [M-N] | [M-P] | [verdict] |
| [DIM-C]  | [N] | [M] | [P] | [M-N] | [M-P] | [verdict] |

```
MUST-CLEAR OPP: [list/"none"] | FAV=[N] OPP=[M] -> [HOLDS/CONDITIONAL/DEFEATED]
```
**g_null(initial)**: [verdict]

**Challenge claims** *(each grounds §0 argument)*:

| CH-ID | Claim | §0 Grounding | Severity |
|-------|-------|-------------|---------|
| CH-001 | [CLAIM_1] | §0:Arg-[n] | [tier] |
| CH-002 | [CLAIM_2] | §0:Arg-[n] | [tier] |
| CH-003 | [optional] | §0:Arg-[n] | [tier] |

**GOpen Verdict**: [verdict] | **GOpen Reason**: [one sentence]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [verdict] | [class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-NL
Received GOpen: [copy]
§0 Charter: [§0:Arg-n] -- [which arguments addressed, or "§0: None"]

**CH-ID Response Table**:

| CH-ID | Claim (copy) | §0 Grounding | Technical Response | Status |
|-------|-------------|-------------|-------------------|--------|
| CH-001 | [copy] | §0:Arg-[n] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | §0:Arg-[n] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |
| CH-003 | [copy if active] | §0:Arg-[n] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |

**Additional Findings** *(per §14 and §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [tier] |
| F-2 | [§1:S-n] | [FINDING_2] | [tier] |

**Section Severity**: worst(F-1=[_], F-2=[_]) = [tier]

**Lens Coverage Table** *(per §15)*:

| # | lens.verify Entry | Applicability | Status | Finding Ref |
|---|------------------|--------------|--------|-------------|
| Q-1 | [entry 1] | AM-01: [tier] | [ADDRESSED/OPEN] | [F-n/AM-01] |
| Q-2 | [entry 2] | AM-02: [tier] | [ADDRESSED/OPEN] | [F-n/AM-02] |

**NH Dimension Scores** *(per §17 DOMAIN emission)*:

| Dimension | B Score (0-10) | C Score (0-10) |
|-----------|---------------|---------------|
| [DIM-A] | [score] | [score] |
| [DIM-B] | [score] | [score] |
| [DIM-C] | [score] | [score] |

**Recommendation**: [One action.]
**G_domain Verdict**: [verdict] | **G_domain Reason**: [one sentence]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [verdict] | [class] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT *(EXCLUDED from gate ledger)*

```
G_domain_agg=[verdict] | g_null(post-domain)=[HOLDS/CONDITIONAL/DEFEATED]
```

---

## §3.8 CH-ID SATURATION CHECK *(EXCLUDED from gate ledger)*

| CH-ID | DOMAIN | Pre-LIFECYCLE Saturation |
|-------|--------|--------------------------|
| CH-001 | [copy] | [SATURATED/UNSATURATED] |
| CH-002 | [copy] | [SATURATED/UNSATURATED] |

*LIFECYCLE may proceed.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-NL
Received GOpen: [copy] | G_domain_agg: [copy] | g_null(post-domain): [copy]
§0 Charter: [§0:Arg-n] -- [which Charter arguments addressed, or "§0: None"]

**CH-ID Response Table**:

| CH-ID | Claim (copy) | §0 Grounding | Commitment-Frame Response | Status |
|-------|-------------|-------------|--------------------------|--------|
| CH-001 | [copy] | §0:Arg-[n] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | §0:Arg-[n] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |
| CH-003 | [copy if active] | §0:Arg-[n] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |

**Decision-readiness assessment**: [Paragraph. Reference GOpen, G_domain_agg,
g_null(post-domain), and §0 Charter arguments explicitly.]

**Null hypothesis status**: [yes / partial / no]

**Additional Findings** *(per §14 and §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [tier] |
| F-2 | [§1:S-n] | [FINDING_2] | [tier] |

**Section Severity**: worst(F-1=[_], F-2=[_]) = [tier]

**Lens Coverage Table** *(per §15)*:

| # | lens.verify Entry | Applicability | Status | Finding Ref |
|---|------------------|--------------|--------|-------------|
| Q-1 | [entry 1] | AM-03: [tier] | [ADDRESSED/OPEN] | [F-n/AM-03] |
| Q-2 | [entry 2] | AM-04: [tier] | [ADDRESSED/OPEN] | [F-n/AM-04] |

**NH Dimension Scores** *(per §17 LIFECYCLE NH SCORE EMISSION -- v1-NL)*:

| Dimension | B Score (0-10) | C Score (0-10) |
|-----------|---------------|---------------|
| [DIM-A] | [score] | [score] |
| [DIM-B] | [score] | [score] |
| [DIM-C] | [score] | [score] |

**Recommendation**: [One action.]
**G_lifecycle Verdict**: [verdict] | **G_lifecycle Reason**: [one sentence]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [verdict] | [class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1-NL
*Full record: §0 Charter, all NH sub-tables (DOMAIN + LIFECYCLE), all gates, CH-IDs.*
§0 Charter: [§0:Arg-n] -- closing reassessment

**§0 Charter Coverage Audit**:

| §0 Argument | DOMAIN Referenced | LIFECYCLE Referenced | Coverage |
|-------------|------------------|---------------------|---------|
| Arg-1: [summary] | [YES/NO] | [YES/NO] | [COVERED / CHARTER-GAP] |
| Arg-2: [summary] | [YES/NO] | [YES/NO] | [COVERED / CHARTER-GAP] |
| Arg-3: [summary/N/A] | [YES/NO/N/A] | [YES/NO/N/A] | [COVERED / CHARTER-GAP / N/A] |

**Charter-gap arguments**: [List for ACTION ITEM REGISTER or "None."]

**Applying §9 Stage 3**:
```
g_null(post-domain)=[_] | G_lifecycle=[_] -> g_null(final)=[HOLDS/CONDITIONAL/DEFEATED]
```

**Revised NH DIMENSION TABLE** *(§17 aggregation: DOMAIN + LIFECYCLE sub-tables)*:

```
Col B = avg(DOMAIN B + LIFECYCLE B):
  DIM-A: D=[_] L=[_] avg=[_] | DIM-B: D=[_] L=[_] avg=[_] | DIM-C: D=[_] L=[_] avg=[_]
Col C = avg(DOMAIN C + LIFECYCLE C):
  DIM-A: D=[_] L=[_] avg=[_] | DIM-B: D=[_] L=[_] avg=[_] | DIM-C: D=[_] L=[_] avg=[_]
Col A: carry forward.
```

| Dimension | A | B (agg D+L) | C (agg D+L) | B-A | B-C | NH Verdict |
|-----------|---|-------------|-------------|-----|-----|------------|
| [DIM-A*] | [carry] | [agg] | [agg] | [diff] | [diff] | [verdict] |
| [DIM-B*] | [carry] | [agg] | [agg] | [diff] | [diff] | [verdict] |
| [DIM-C]  | [carry] | [agg] | [agg] | [diff] | [diff] | [verdict] |

```
MUST-CLEAR OPP: [list/"none"] | FAV=[N] OPP=[M] -> [HOLDS/CONDITIONAL/DEFEATED]
```

**Full CH-ID Saturation**:

| CH-ID | DOMAIN | LIFECYCLE | Full Saturation | Waiver |
|-------|--------|-----------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED/UNSATURATED] | [N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED/UNSATURATED] | [N/A] |

**CH-ID Final Assessment**:

| CH-ID | G_domain | G_lifecycle | Final | Notes |
|-------|----------|-------------|-------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |

**Remaining gaps**: [All defeated, or list.]
**GClose Verdict**: [verdict] | **Override invoked**: [YES/NO]
**g_null Override**: [N/A or justification]
**GClose Rationale**: [2-3 sentences. Reference g_null(final), CH-ID saturation, §0 Charter
coverage audit, NH trajectory including lifecycle scores.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [verdict] | [class] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION *(EXCLUDED from gate ledger)*

### Surface Coverage

| IN-SCOPE Surface | Domain | Reviewer | Finding Ref | Coverage |
|-----------------|--------|---------|-------------|---------|
| [SURFACE_1] | [dom] | [ROLE] | [F-n/"none"] | [COVERED/GAP] |
| [SURFACE_2] | [dom] | [ROLE] | [F-n/"none"] | [COVERED/GAP] |

**Surface coverage signal**: [COVERED / PARTIAL]

### Domain Coverage Gap-Check | Artifact Domain | HIGH AM Rows | Coverage |

### §11 ADVISORY-ORPHAN Check: [List or "None."]

### §0 Charter-Gap Items: [ADVISORY-CHARTER-GAP list from Bracket Closing audit, or "None."]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Cite |
|------|----------|---------|------|
| GOpen | [CHALLENGER] | [copy] | v1-NL |
| G_domain_agg | [DOMAIN] | [copy] | v1-NL |
| G_lifecycle | [LIFECYCLE] | [copy] | v1-NL |
| GClose | [CHALLENGER] | [copy] | v1-NL |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [or "None."] | **Convergence**: [name it] | **Scope coverage**: [or "None."]

**§13 PROGRESSION LEDGER**: g_null(initial)=[_] | post-domain=[_] | final=[_] | Trajectory=[label]

**§0 Charter disposition**: [Which arguments DEFEATED vs. CHARTER-GAP. One sentence.]

**NH trajectory with lifecycle**: [Did LIFECYCLE NH scores raise or lower the B/C aggregates
relative to DOMAIN-only? One sentence.]

---

## DISPOSITION

**Gate vector**: GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]

```
GClose=FAIL->BLOCKED | Gi=FAIL->BLOCKED | no FAIL+COND->CONDITIONAL | all PASS->READY
```
**Overall Disposition**: [verdict]
**Applying §16 rule**: [n]  **Primary Driver**: [result]
**Conditions/Blocker**: [if applicable]
**RESOLUTION REGISTRY**: [table if CONDITIONAL, else "N/A"]

---

## ACTION ITEM REGISTER

*Assembly per §6: verbatim gate ledger rows. Then CH-ID items, lens gaps, scope gaps,
domain gaps, orphans, charter gaps. Do NOT re-derive.*

| Source | CH-ID / Finding | Item | Disposition Class | Owner | Criterion |
|--------|----------------|------|------------------|-------|-----------|
| [gate ledger] | -- | [verbatim] | [class] | [ROLE] | [criterion] |
| [CH-ID] | CH-00n | [action] | [BLOCKED/CONDITIONAL/ADVISORY] | [ROLE] | [criterion] |
| [lens HIGH] | AM-0n/Q-n | ADVISORY-OPEN-LENS-REQUIRED: [entry] | ADVISORY | [ROLE] | Produce finding. |
| [scope gap] | -- | ADVISORY-GAP: §1 [surface] | ADVISORY | [ROLE] | Assign reviewer. |
| [domain gap] | -- | ADVISORY-GAP (DOMAIN): [domain] | ADVISORY | [ROLE] | Add reviewer. |
| [orphan] | -- | ADVISORY-ORPHAN: finding missing §1 citation | ADVISORY | [ROLE] | Add §1:S-n. |
| [charter gap] | -- | ADVISORY-CHARTER-GAP: §0:Arg-[n] "[summary]" not addressed | ADVISORY | [ROLE] | Assign reviewer. |

---

**Artifact to review:**

{{artifact}}
