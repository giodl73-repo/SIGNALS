---
skill: quest-variate
skill_target: org-review
date: 2026-03-16
round: 16
rubric: org-review-rubric-v14-2026-03-16.md
variants: V-01 V-02
---

# org-review -- Variate R16 (V-01, V-02)

All R15 variants achieved 250/250 under v14. The NH chain is fully mechanical end-to-end.
R16 explores three candidate C-41 patterns across five variants. This file contains V-01
and V-02 (single-axis). V-03 through V-05 are in the companion file.

**Variation axes selected:**
- V-01: Inertia framing -- §0 NULL HYPOTHESIS CHARTER as pre-contract block
- V-02: Output format -- Global F-ID registry (§18) across all reviewer sections
- V-03: Lifecycle emphasis -- LIFECYCLE emits NH Dimension Score sub-table (companion file)
- V-04: Output format + Lifecycle emphasis (companion file)
- V-05: Inertia framing + Lifecycle emphasis (companion file)

All variants carry forward the complete R15 contract machinery (§1-§17) intact.

---

## V-01

**Axis**: Inertia framing -- NULL HYPOTHESIS CHARTER as §0, a pre-DISPOSITION_CONTRACT
immutable block.

**Hypothesis**: §0 commits the status-quo champion's best case and the evidence threshold
required to defeat it *before* any contract or reviewer section runs. Downstream sections
carry `[§0:Arg-n]` citations showing which Charter argument they address. Reviewer sections
that address no Charter argument must declare `[§0: None]`. The BRACKET CLOSING emits a
Charter Coverage Audit table showing which arguments were COVERED vs. CHARTER-GAP.
CHARTER-GAP arguments become ADVISORY-CHARTER-GAP items in the ACTION ITEM REGISTER.

Candidate C-41: NH Charter Reference Completeness -- the set of Charter arguments is
pre-committed; each reviewer section must declare its Charter coverage; gaps are auditable
from the Charter Coverage Audit table without reading reviewer narrative.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
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
pre-printed heading, label, field, formula, or structural element. Do not add sections
between pre-printed headers. If a field cannot be filled, write `[N/A -- reason]`.

---

```
======================================================================
§0 -- NULL HYPOTHESIS CHARTER [IMMUTABLE -- complete before DISPOSITION_CONTRACT]
======================================================================

Status-quo name: [What the team does today -- one phrase]

Strongest case for doing nothing (pre-committed before any reviewer runs):
  Arg-1: [Best argument for status quo -- switching cost, workaround viability,
          or adoption friction. One sentence.]
  Arg-2: [Second strongest argument. One sentence.]
  Arg-3: [Third argument -- optional. One sentence or write "N/A".]

Evidence threshold (pre-committed):
  The null hypothesis is DEFEATED only when the review record demonstrates ALL §0
  arguments are addressed or shown LOW-impact. Partial defeat: >= 2 of 3 addressed
  with no HIGH-severity unaddressed argument remaining.

Charter reference requirement (pre-committed):
  Each reviewer section (BRACKET OPENING, DOMAIN, LIFECYCLE, BRACKET CLOSING) MUST
  include a §0 charter reference line:
    §0 Charter: [§0:Arg-n, §0:Arg-n] -- [one sentence on which arguments addressed]
    OR: §0 Charter: [§0: None] -- this section addresses no Charter argument
  Missing charter reference = CHARTER-GAP entry for this section in BRACKET CLOSING audit.

CH-ID grounding requirement (pre-committed):
  Each challenge claim in BRACKET OPENING MUST ground to a §0 argument:
    CH-00n grounds §0:Arg-n
  A CH-ID with no Charter grounding is a structural gap.

§0 COMPLETE -- DISPOSITION_CONTRACT proceeds below.
======================================================================
```

---

```
======================================================================
DISPOSITION_CONTRACT v1-NH (null-hypothesis-charter variant)
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§17;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE (each surface carries [DOMAIN: label] for §10a; cited in §5.5 and §11):
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
  Single domain: G_domain_agg = G_domain.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1-NH"
  Missing cite = audit-trail gap.

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim receives a CH-ID (CH-001, ...).
  Every downstream section carries a mandatory CH-ID response table.
  PASS verdict prohibited if any CH-ID row = OPEN.
  Each CH-ID must state its §0 grounding: "CH-00n grounds §0:Arg-n"

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emit at end of each verdict-emitting section. Assemble ACTION ITEM REGISTER by verbatim
  copy. Do NOT re-derive Gate Verdict or Class at assembly.
  EXCLUDED (no row emitted): §3.5, §3.8, §5.5.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  0. §0 NULL HYPOTHESIS CHARTER (pre-execution -- already complete)
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
  Reordering any section violates this contract.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID has DOMAIN response before LIFECYCLE executes.
  FULLY SATURATED: CH-ID has DOMAIN + LIFECYCLE responses before BRACKET CLOSING.
  PASS from BRACKET CLOSING prohibited without full saturation or stated waiver.
  Waiver syntax: "CH-XXX WAIVER: [reason]" -> ACTION ITEM REGISTER as ADVISORY.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = §17 formula output [emitted at BRACKET OPENING]
  Stage 2: g_null(post-domain) [at §3.5]:
    G_domain_agg=FAIL        -> FAIL
    G_domain_agg=CONDITIONAL -> max(g_null(initial), CONDITIONAL)
    G_domain_agg=PASS        -> g_null(initial)
  Stage 3: g_null(final) [at BRACKET CLOSING]:
    G_lifecycle=FAIL        -> FAIL
    G_lifecycle=CONDITIONAL -> max(g_null(post-domain), CONDITIONAL)
    G_lifecycle=PASS        -> g_null(post-domain)
  GClose must equal g_null(final). Override: "g_null OVERRIDE: [justification]"
  Scale: HOLDS=FAIL < CONDITIONAL < DEFEATED=PASS.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps each §1 surface to reviewer findings post-BRACKET CLOSING.
  COVERED (>=1 finding) or GAP (no finding). GAP -> ADVISORY-GAP in ACTION ITEM REGISTER.
  §5.5 also runs §10a DOMAIN COVERAGE GAP-CHECK. No ledger row emitted.

§10a -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  Group §1 surfaces by [DOMAIN: label]. For each domain, find HIGH-applicability AM rows.
  ADVISORY-GAP: no HIGH row covers this domain -> ACTION ITEM REGISTER.
  Table: | Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding carries "[§1:S-n]" citation. Missing = ADVISORY-ORPHAN -> ACTION ITEM REGISTER.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  CONDITIONAL disposition -> emit: | Gate | Condition | Owner | Resolution Criterion | Status |
  Else: "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  In CROSS-ROLE SIGNALS, §13 sub-section:
    g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory
  Labels: MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
          DOMAIN-RECOVERED / LIFECYCLE-RECOVERED. Informational only.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Findings table: | # | §1 Surface | Finding | Severity |
  Section Severity = worst(individual finding severities). HIGH>MEDIUM>LOW.
  Apply mechanically.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  After findings, each DOMAIN and LIFECYCLE section emits LENS COVERAGE TABLE:
    | # | lens.verify Entry | Applicability (AM row + tier) | Status | Finding Ref |
  HIGH+OPEN -> ADVISORY-OPEN-LENS-REQUIRED; MEDIUM+OPEN -> ADVISORY-OPEN-LENS.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  1. GClose=FAIL         -> Primary Driver = BRACKET CLOSING
  2. G_domain_agg=FAIL   -> DOMAIN
  3. G_lifecycle=FAIL    -> LIFECYCLE
  4. GOpen=FAIL          -> BRACKET OPENING
  5. GClose=CONDITIONAL  -> BRACKET CLOSING
  6. G_domain_agg=CONDITIONAL -> DOMAIN
  7. G_lifecycle=CONDITIONAL  -> LIFECYCLE
  8. GOpen=CONDITIONAL        -> BRACKET OPENING
  9. all PASS            -> N/A
  Emit: **Applying §16 rule**: [n]  **Primary Driver**: [result]

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]
  BRACKET OPENING table:
    | Dimension | A: Status-Quo (0-10) | B: Proposed-Build (0-10) |
    |           | C: Best-Non-Build-Alt (0-10) | B-A | B-C | NH Verdict |
  NH Verdict per row: B>A AND B>C -> FAVORS-BUILD; B<A OR B<C -> OPPOSES-BUILD; else NEUTRAL.
  MUST-CLEAR rows marked (*). Minimum 3 dimensions.

  g_null derivation rule (pre-committed):
    HOLDS       <-- any MUST-CLEAR = OPPOSES-BUILD
    CONDITIONAL <-- no MUST-CLEAR OPPOSES-BUILD; count(OPPOSES-BUILD) >= count(FAVORS-BUILD)
    DEFEATED    <-- no MUST-CLEAR OPPOSES-BUILD; count(FAVORS-BUILD) > count(OPPOSES-BUILD)

  NH TABLE AGGREGATION RULE (BRACKET CLOSING, pre-committed):
    Column A: carry forward challenger opening value unchanged (control arm).
    Column B: avg(all DOMAIN B scores per dimension).
    Column C: avg(all DOMAIN C scores per dimension).
  Read from DOMAIN NH Dimension Score sub-tables. No prose extraction.

  DOMAIN NH SCORE EMISSION REQUIREMENT (pre-committed):
    Each DOMAIN section MUST emit before its gate ledger row:
      | Dimension | B Score: Proposed-Build (0-10) | C Score: Best-Non-Build-Alt (0-10) |
    One row per §17 dimension. BRACKET CLOSING reads sub-tables directly.

======================================================================
END DISPOSITION_CONTRACT v1-NH
======================================================================
```

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3. CHALLENGER positions remain fixed.)*

### APPLICABILITY MATRIX

*(REQUIRED before BRACKET OPENING. Locked here. Referenced by §15 and §10a.)*

| Row ID | Role | lens.verify Entry | Artifact Domain Covered | Artifact Applicability | Basis |
|--------|------|------------------|------------------------|----------------------|-------|
| AM-01 | [DOMAIN ROLE] | [Full text entry 1] | [domain] | [HIGH / MEDIUM / LOW] | [reason] |
| AM-02 | [DOMAIN ROLE] | [Full text entry 2] | [domain] | [HIGH / MEDIUM / LOW] | [reason] |
| AM-03 | [LIFECYCLE ROLE] | [Full text entry 1] | [domain] | [HIGH / MEDIUM / LOW] | [reason] |
| AM-04 | [LIFECYCLE ROLE] | [Full text entry 2] | [domain] | [HIGH / MEDIUM / LOW] | [reason] |

*(Add rows for all lens.verify entries from all assigned roles. Matrix locked.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1-NH
§0 Charter: [§0:Arg-n, §0:Arg-n] -- [one sentence on which arguments this section addresses]

**Null hypothesis**: [What the team does today -- one sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table** *(>= 3 dimensions; distinct from §17 NH table)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|----------------|-----------|------------------------|-------|
| [DIM-1]   | [score] | [score] | [score] | |
| [DIM-2]   | [score] | [score] | [score] | |
| [DIM-3]   | [score] | [score] | [score] | |

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17)*:

| Dimension | A: SQ (0-10) | B: Build (0-10) | C: Best-Alt (0-10) | B-A | B-C | NH Verdict |
|-----------|-------------|-----------------|-------------------|-----|-----|------------|
| [DIM-A*]  | [N] | [M] | [P] | [M-N] | [M-P] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [N] | [M] | [P] | [M-N] | [M-P] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [N] | [M] | [P] | [M-N] | [M-P] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

*(Rows marked * are MUST-CLEAR.)*

**Applying §17 g_null derivation rule**:
```
MUST-CLEAR rows with OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD) = [N] | count(OPPOSES-BUILD) = [M]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null(initial)** *(§9 Stage 1)*: [HOLDS / CONDITIONAL / DEFEATED]

**Challenge claims** *(per §5 -- each CH-ID grounds to a §0 argument)*:

| CH-ID | Challenge Claim | §0 Grounding | Severity |
|-------|----------------|--------------|---------|
| CH-001 | [CLAIM_1] | §0:Arg-[n] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | §0:Arg-[n] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | §0:Arg-[n] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]
**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-NH
Received GOpen: [copy from BRACKET OPENING]
§0 Charter: [§0:Arg-n, §0:Arg-n] -- [which Charter arguments this section addresses]
  OR: §0 Charter: [§0: None] -- this section addresses no Charter argument

**CH-ID Response Table** *(per §5)*:

| CH-ID | Challenge Claim (copy) | §0 Grounding | Technical Response | Status |
|-------|----------------------|--------------|-------------------|--------|
| CH-001 | [copy] | §0:Arg-[n] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | §0:Arg-[n] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | §0:Arg-[n] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Additional Findings** *(per §14 and §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-3 | [§1:S-n] | [FINDING_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**Lens Coverage Table** *(per §15)*:

| # | lens.verify Entry | Applicability (AM row + tier) | Status | Finding Ref |
|---|------------------|-------------------------------|--------|-------------|
| Q-1 | [entry 1] | AM-01: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or AM-01] |
| Q-2 | [entry 2] | AM-02: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or AM-02] |

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
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6.)*

**Applying §3a**:
```
G_domain rows: DOMAIN -- [ROLE_NAME]: [verdict]
G_domain_agg = [PASS / CONDITIONAL / FAIL]
```
**Applying §9 Stage 2**:
```
g_null(initial)=[copy] | G_domain_agg=[copy]
  FAIL->FAIL | CONDITIONAL->max(initial,COND) | PASS->initial
g_null(post-domain) = [HOLDS / CONDITIONAL / DEFEATED]
```

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger.)*

| CH-ID | DOMAIN Status | Pre-LIFECYCLE Saturation |
|-------|--------------|--------------------------|
| CH-001 | [copy] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED or N/A] |

**Pre-LIFECYCLE unsaturated**: [List or "None"] -- LIFECYCLE may proceed.

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-NH
Received GOpen: [copy] | G_domain_agg: [copy] | g_null(post-domain): [copy]
§0 Charter: [§0:Arg-n] -- [which Charter arguments this section addresses]
  OR: §0 Charter: [§0: None]

**CH-ID Response Table** *(per §5)*:

| CH-ID | Challenge Claim (copy) | §0 Grounding | Commitment-Frame Response | Status |
|-------|----------------------|--------------|--------------------------|--------|
| CH-001 | [copy] | §0:Arg-[n] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | §0:Arg-[n] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | §0:Arg-[n] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph. Reference GOpen, G_domain_agg,
g_null(post-domain), and §0 Charter arguments explicitly.]

**Null hypothesis status**: [yes / partial / no -- reference g_null(post-domain).]

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

| # | lens.verify Entry | Applicability (AM row + tier) | Status | Finding Ref |
|---|------------------|-------------------------------|--------|-------------|
| Q-1 | [entry 1] | AM-03: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or AM-03] |
| Q-2 | [entry 2] | AM-04: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or AM-04] |

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

Contract: DISPOSITION_CONTRACT v1-NH
*Full record received: §0 Charter, scope, APPLICABILITY MATRIX, all gates, CH-IDs.*
§0 Charter: [§0:Arg-n] -- closing reassessment of which arguments survived

**§0 Charter Coverage Audit**:

| §0 Argument | DOMAIN Referenced ([§0:Arg-n]) | LIFECYCLE Referenced | Coverage |
|-------------|-------------------------------|---------------------|---------|
| Arg-1: [summary] | [YES / NO] | [YES / NO] | [COVERED / CHARTER-GAP] |
| Arg-2: [summary] | [YES / NO] | [YES / NO] | [COVERED / CHARTER-GAP] |
| Arg-3: [summary or N/A] | [YES / NO / N/A] | [YES / NO / N/A] | [COVERED / CHARTER-GAP / N/A] |

**Charter-gap arguments for ACTION ITEM REGISTER**:
[List ADVISORY-CHARTER-GAP items, or "None -- all Charter arguments covered."]

**Applying §9 Stage 3**:
```
g_null(post-domain)=[copy] | G_lifecycle=[copy]
  FAIL->FAIL | CONDITIONAL->max(post-domain,COND) | PASS->post-domain
g_null(final) = [HOLDS / CONDITIONAL / DEFEATED]
```
*GClose must equal g_null(final) per §9.*

**Revised NH DIMENSION TABLE** *(§17 aggregation from DOMAIN NH score sub-tables)*:

```
Column B aggregation (avg DOMAIN B scores per dimension):
  [DIM-A]: DOMAIN=[score] -> avg=[result]
  [DIM-B]: DOMAIN=[score] -> avg=[result]
  [DIM-C]: DOMAIN=[score] -> avg=[result]
Column C aggregation (avg DOMAIN C scores per dimension):
  [DIM-A]: DOMAIN=[score] -> avg=[result]
  [DIM-B]: DOMAIN=[score] -> avg=[result]
  [DIM-C]: DOMAIN=[score] -> avg=[result]
Column A: carry forward from BRACKET OPENING.
```

| Dimension | A: SQ | B: Build (agg) | C: Best-Alt (agg) | B-A | B-C | NH Verdict |
|-----------|-------|----------------|-------------------|-----|-----|------------|
| [DIM-A*]  | [carry] | [agg] | [agg] | [diff] | [diff] | [verdict] |
| [DIM-B*]  | [carry] | [agg] | [agg] | [diff] | [diff] | [verdict] |
| [DIM-C]   | [carry] | [agg] | [agg] | [diff] | [diff] | [verdict] |

**Applying §17 rule to revised table**:
```
MUST-CLEAR OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD)=[N] | count(OPPOSES-BUILD)=[M] -> [HOLDS / CONDITIONAL / DEFEATED]
```

**Full CH-ID Saturation** *(per §8)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver |
|-------|--------------|-----------------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A] |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [All defeated, or list.]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A -- formula applied | or: justification]
**GClose Rationale**: [2-3 sentences. Reference g_null(final), CH-ID saturation,
§0 Charter coverage audit, trajectory.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6. Applies §10, §10a, §11.)*

### Surface Coverage *(per §10)*

| IN-SCOPE Surface | Domain | Reviewer(s) | Finding Ref | Coverage |
|-----------------|--------|-------------|-------------|---------|
| [SURFACE_1] | [domain] | [ROLE or "none"] | [F-n or "none"] | [COVERED / GAP] |
| [SURFACE_2] | [domain] | [ROLE or "none"] | [F-n or "none"] | [COVERED / GAP] |
| [SURFACE_3] | [domain] | [ROLE or "none"] | [F-n or "none"] | [COVERED / GAP] |

**Surface coverage gate signal**: [COVERED / PARTIAL -- [N] gap(s)]

### Domain Coverage Gap-Check *(per §10a)*

| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|---------|
| [DOMAIN-1] | [AM-0n: [ROLE] -- "[lens summary]" / "none"] | [COVERED / ADVISORY-GAP] |

### §11 ADVISORY-ORPHAN Check

**Findings without §1:S-n citation**: [List or "None detected."]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen -- bracket opening | [CHALLENGER_ROLE] | [copy] | DISPOSITION_CONTRACT v1-NH |
| G_domain_agg -- domain aggregate | [DOMAIN_ROLE(S)] | [copy] | DISPOSITION_CONTRACT v1-NH |
| G_lifecycle -- lifecycle | [LIFECYCLE_ROLE] | [copy] | DISPOSITION_CONTRACT v1-NH |
| GClose -- bracket closing | [CHALLENGER_ROLE] | [copy] | DISPOSITION_CONTRACT v1-NH |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Incompatible CH-ID responses or findings across roles. If none: "None."]
**Convergence**: [Concern named independently by >= 2 reviewers -- name it.]
**Scope coverage**: [§1 surfaces not covered. If all covered: "None."]

**§13 PROGRESSION LEDGER**:
```
g_null(initial)     = [copy from BRACKET OPENING §17]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING §9 Stage 3]
Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED /
                     LIFECYCLE-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```
**§0 Charter disposition**: [Which §0 arguments were DEFEATED; which are CHARTER-GAP.
One sentence.]

---

## DISPOSITION

**Gate vector**:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply §3 formula**:
```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose=FAIL? -> BLOCKED | Any Gi=FAIL? -> BLOCKED
No FAIL, any CONDITIONAL? -> CONDITIONAL | All PASS? -> READY
```
**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Applying §16 rule**: [rule n + reason]
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

*Assembly per §6: copy all local gate ledger rows verbatim. Do NOT re-derive. Then add
CH-ID items, ADVISORY-OPEN-LENS items, ADVISORY-GAP items (§10 + §10a), ADVISORY-ORPHAN
items (§11), ADVISORY-CHARTER-GAP items (§0 Charter Coverage Audit).*

| Source | CH-ID / Finding | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|--------|----------------|-----------------|------------------|------------|---------------------|
| [gate ledger] | -- | [verbatim: Section / Gate / Verdict / Class] | [class] | [ROLE] | [criterion] |
| [CH-ID item] | CH-00n | [What must be done] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE] | [criterion] |
| [lens HIGH] | AM-0n / Q-n | ADVISORY-OPEN-LENS-REQUIRED: [entry] | ADVISORY | [ROLE] | Produce finding. |
| [lens MED] | AM-0n / Q-n | ADVISORY-OPEN-LENS: [entry] | ADVISORY | [ROLE] | Address or justify. |
| [scope gap] | -- | ADVISORY-GAP: §1 surface [name] not covered | ADVISORY | [ROLE] | Assign reviewer. |
| [domain gap] | -- | ADVISORY-GAP (DOMAIN): [domain] no HIGH-applicability reviewer | ADVISORY | [ROLE] | Add reviewer. |
| [orphan] | -- | ADVISORY-ORPHAN: finding missing §1 citation | ADVISORY | [ROLE] | Add §1:S-n. |
| [charter gap] | -- | ADVISORY-CHARTER-GAP: §0:Arg-[n] "[arg summary]" not addressed by any reviewer | ADVISORY | [ROLE] | Assign reviewer to address this Charter argument. |

---

**Artifact to review:**

{{artifact}}

---
---

## V-02

**Axis**: Output format -- Global F-ID registry (§18). Every finding across all reviewer
sections receives a globally unique sequential F-ID (F-001, F-002, ...). §18 assembles a
GLOBAL FINDING REGISTRY at §5.5 that serves as the cross-reference index. ACTION ITEM
REGISTER references findings by F-ID. Lens Coverage Table cites F-IDs in the Finding
column.

**Hypothesis**: Global F-IDs create a parallel auditability chain for findings, analogous
to CH-IDs for challenges. An auditor verifying action completeness needs only the GLOBAL
FINDING REGISTRY and ACTION ITEM REGISTER -- no reviewer section narrative required.
Candidate C-41: Bidirectional Finding-to-Action Traceability -- every HIGH or MEDIUM
finding F-ID must appear in the ACTION ITEM REGISTER as ACTIONED or WAIVED; a finding
with neither status is a contract violation detectable from the registry alone.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
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
filled, write `[N/A -- reason]`. F-IDs are globally sequential across all sections;
maintain a running counter and never reuse an F-ID.

---

```
======================================================================
DISPOSITION_CONTRACT v1-FID (global finding registry variant)
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§18;
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

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]

§1 COMPLETE -- role selection, APPLICABILITY MATRIX, and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment.
  MEDIUM = Conditions commitment.
  LOW    = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR exists Gi=FAIL
  CONDITIONAL <-- no FAIL, exists CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain rows). Single domain: direct pass-through.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section: "Contract: DISPOSITION_CONTRACT v1-FID"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  CH-IDs assigned at BRACKET OPENING. Every downstream section carries CH-ID response table.
  PASS prohibited if any CH-ID = OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row: | Section | Gate | Verdict | Class | (Class: FAIL->BLOCKED; COND->CONDITIONAL; PASS->ADVISORY)
  Emit at end of each verdict-emitting section. Assemble ACTION ITEM REGISTER by verbatim
  copy. Do NOT re-derive Gate Verdict or Class.
  EXCLUDED: §3.5, §3.8, §5.5.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1. ROLE MANIFEST + APPLICABILITY MATRIX
  2. BRACKET OPENING
  3. DOMAIN(s)
  3.5. DOMAIN-AGGREGATE CHECKPOINT
  3.8. CH-ID SATURATION CHECK
  4. LIFECYCLE
  5. BRACKET CLOSING
  5.5. SCOPE COVERAGE RECONCILIATION (includes §18 GLOBAL FINDING REGISTRY)
  6. GATE VECTOR TABLE
  7. CROSS-ROLE SIGNALS
  8. DISPOSITION
  9. ACTION ITEM REGISTER
  Reordering violates this contract.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID has DOMAIN response before LIFECYCLE.
  FULLY SATURATED: DOMAIN + LIFECYCLE responses before BRACKET CLOSING.
  PASS prohibited without full saturation or waiver. Waiver: "CH-XXX WAIVER: [reason]"

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = §17 formula [BRACKET OPENING]
  Stage 2: g_null(post-domain) [§3.5]:
    FAIL->FAIL | CONDITIONAL->max(initial,COND) | PASS->initial
  Stage 3: g_null(final) [BRACKET CLOSING]:
    FAIL->FAIL | CONDITIONAL->max(post-domain,COND) | PASS->post-domain
  GClose = g_null(final). Override: "g_null OVERRIDE: [justification]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps §1 surfaces to reviewer F-IDs. COVERED (>=1 F-ID) or GAP.
  GAP -> ADVISORY-GAP in ACTION ITEM REGISTER. No ledger row from §5.5.
  §5.5 also runs §10a and §18.

§10a -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  Group §1 surfaces by [DOMAIN: label]. Find HIGH-applicability AM rows per domain.
  ADVISORY-GAP: no HIGH row -> ACTION ITEM REGISTER.
  Table: | Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding carries "[§1:S-n]" citation. Missing = ADVISORY-ORPHAN -> ACTION ITEM REGISTER.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  CONDITIONAL disposition -> | Gate | Condition | Owner | Resolution Criterion | Status |
  Else: "RESOLUTION REGISTRY: N/A"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS §13 sub-section:
    g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Findings table: | F-ID | §1 Surface | Finding | Severity |
  F-IDs are globally sequential across all sections.
  Section Severity = worst(individual severities). Apply mechanically.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  After findings, each DOMAIN and LIFECYCLE section emits LENS COVERAGE TABLE:
    | # | lens.verify Entry | Applicability (AM row + tier) | Status | Finding F-ID |
  Finding F-ID column: cite the global F-ID that addresses this lens entry, or AM row.
  HIGH+OPEN -> ADVISORY-OPEN-LENS-REQUIRED; MEDIUM+OPEN -> ADVISORY-OPEN-LENS.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  1. GClose=FAIL -> BRACKET CLOSING | 2. G_domain_agg=FAIL -> DOMAIN
  3. G_lifecycle=FAIL -> LIFECYCLE | 4. GOpen=FAIL -> BRACKET OPENING
  5. GClose=COND -> BRACKET CLOSING | 6. G_domain_agg=COND -> DOMAIN
  7. G_lifecycle=COND -> LIFECYCLE | 8. GOpen=COND -> BRACKET OPENING | 9. all PASS -> N/A

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]
  BRACKET OPENING table:
    | Dimension | A: SQ (0-10) | B: Build (0-10) | C: Best-Alt (0-10) | B-A | B-C | NH Verdict |
  NH Verdict: B>A AND B>C -> FAVORS-BUILD; B<A OR B<C -> OPPOSES-BUILD; else NEUTRAL.
  MUST-CLEAR (*). Min 3 dimensions.

  g_null rule: HOLDS (MUST-CLEAR OPPOSES-BUILD) | CONDITIONAL (no MUST-CLEAR OPPOSES-BUILD;
    count(OPP)>=count(FAV)) | DEFEATED (count(FAV)>count(OPP))

  NH TABLE AGGREGATION (BRACKET CLOSING):
    Col A: carry forward. Col B: avg(DOMAIN B). Col C: avg(DOMAIN C). No prose extraction.

  DOMAIN NH SCORE EMISSION (pre-committed):
    Each DOMAIN section MUST emit before gate ledger:
      | Dimension | B Score (0-10) | C Score (0-10) |

§18 -- GLOBAL FINDING REGISTRY PROTOCOL [IMMUTABLE]
  Every finding emitted by any reviewer section receives a globally unique sequential F-ID
  (F-001, F-002, ...). Counter increments across sections in execution order. No reuse.

  At §5.5, assemble GLOBAL FINDING REGISTRY:
    | F-ID | Section | §1 Surface | Severity | Register Status |
  Register Status:
    ACTIONED  = F-ID appears in ACTION ITEM REGISTER (HIGH or MEDIUM finding with item)
    WAIVED    = explicitly waived with stated reason ("F-00n WAIVED: [reason]")
    ADVISORY  = LOW severity; no action required
  HIGH or MEDIUM finding with Register Status = ADVISORY is a contract violation.

  ACTION ITEM REGISTER "CH-ID / Finding" column cites F-ID for finding-sourced items.
  Bidirectionality: given F-ID, locate finding in registry; given action item, locate
  F-ID in registry. No reviewer narrative required for either direction.

======================================================================
END DISPOSITION_CONTRACT v1-FID
======================================================================
```

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot.

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

Contract: DISPOSITION_CONTRACT v1-FID

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
MUST-CLEAR OPPOSES-BUILD: [list or "none"] | count(FAV)=[N] | count(OPP)=[M]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null(initial)** *(§9 Stage 1)*: [HOLDS / CONDITIONAL / DEFEATED]

**Challenge claims**:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

*F-ID counter: BRACKET OPENING emits no findings. Counter starts at F-001 for DOMAIN.*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [verdict] | [class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1-FID
Received GOpen: [copy]

*F-ID counter starts at F-001 (or continues from prior DOMAIN if deep mode).*

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | Technical Response | Status |
|-------|----------------------|-------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Additional Findings** *(per §14, §11, §18 -- assign global F-IDs)*:

| F-ID | §1 Surface | Finding | Severity |
|------|-----------|---------|---------|
| F-001 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-002 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-003 | [§1:S-n] | [FINDING_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation**:
```
worst(F-001=[_], F-002=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**Lens Coverage Table** *(cite F-IDs in Finding F-ID column)*:

| # | lens.verify Entry | Applicability (AM row) | Status | Finding F-ID |
|---|------------------|----------------------|--------|--------------|
| Q-1 | [entry 1] | AM-01: [tier] | [ADDRESSED / OPEN] | [F-00n or AM-01] |
| Q-2 | [entry 2] | AM-02: [tier] | [ADDRESSED / OPEN] | [F-00n or AM-02] |

**NH Dimension Scores** *(per §17 DOMAIN NH SCORE EMISSION REQUIREMENT)*:

| Dimension | B Score: Proposed-Build (0-10) | C Score: Best-Non-Build-Alt (0-10) |
|-----------|-------------------------------|-------------------------------------|
| [DIM-A]   | [score] | [score] |
| [DIM-B]   | [score] | [score] |
| [DIM-C]   | [score] | [score] |

**Recommendation**: [One concrete action.]
**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*F-ID counter after this section: [F-00n]. LIFECYCLE begins at [F-00n+1].*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [verdict] | [class] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT *(EXCLUDED from gate ledger)*

```
G_domain_agg = worst([DOMAIN verdict]) = [PASS / CONDITIONAL / FAIL]
g_null(post-domain): g_null(initial)=[_] | G_domain_agg=[_] -> [HOLDS/CONDITIONAL/DEFEATED]
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

Contract: DISPOSITION_CONTRACT v1-FID
Received GOpen: [copy] | G_domain_agg: [copy from §3.5] | g_null(post-domain): [copy]

*F-ID counter continues from [F-00n].*

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | Commitment-Frame Response | Status |
|-------|----------------------|--------------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph. Reference GOpen, G_domain_agg,
g_null(post-domain) explicitly.]

**Null hypothesis status**: [yes / partial / no]

**Additional Findings** *(per §14, §11, §18 -- continue global F-ID counter)*:

| F-ID | §1 Surface | Finding | Severity |
|------|-----------|---------|---------|
| F-00n | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-00n+1 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation**:
```
worst(F-00n=[_], F-00n+1=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**Lens Coverage Table** *(cite F-IDs)*:

| # | lens.verify Entry | Applicability (AM row) | Status | Finding F-ID |
|---|------------------|----------------------|--------|--------------|
| Q-1 | [entry 1] | AM-03: [tier] | [ADDRESSED / OPEN] | [F-00n or AM-03] |
| Q-2 | [entry 2] | AM-04: [tier] | [ADDRESSED / OPEN] | [F-00n or AM-04] |

**Recommendation**: [One concrete action.]
**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

*F-ID counter after this section: [F-00n]. Counter closes. Bracket Closing references existing IDs.*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [verdict] | [class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1-FID
*Full record received: all F-IDs, all gates, all CH-IDs.*

**Applying §9 Stage 3**:
```
g_null(post-domain)=[copy] | G_lifecycle=[copy]
  FAIL->FAIL | COND->max(post-domain,COND) | PASS->post-domain
g_null(final) = [HOLDS / CONDITIONAL / DEFEATED]
```

**Revised NH DIMENSION TABLE** *(§17 aggregation from DOMAIN NH score sub-tables)*:

```
Col B = avg(DOMAIN B): [DIM-A]=[_] [DIM-B]=[_] [DIM-C]=[_]
Col C = avg(DOMAIN C): [DIM-A]=[_] [DIM-B]=[_] [DIM-C]=[_]
Col A: carry forward from BRACKET OPENING.
```

| Dimension | A: SQ | B: Build (agg) | C: Best-Alt (agg) | B-A | B-C | NH Verdict |
|-----------|-------|----------------|-------------------|-----|-----|------------|
| [DIM-A*]  | [carry] | [agg] | [agg] | [diff] | [diff] | [verdict] |
| [DIM-B*]  | [carry] | [agg] | [agg] | [diff] | [diff] | [verdict] |
| [DIM-C]   | [carry] | [agg] | [agg] | [diff] | [diff] | [verdict] |

```
MUST-CLEAR OPPOSES-BUILD: [list or "none"] | FAV=[N] OPP=[M] -> [HOLDS/CONDITIONAL/DEFEATED]
```

**Full CH-ID Saturation**:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver |
|-------|--------------|-----------------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A] |

**CH-ID Final Assessment**:

| CH-ID | G_domain | G_lifecycle | Final Status | Notes |
|-------|----------|-------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [All defeated, or list.]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A or justification]
**GClose Rationale**: [2-3 sentences.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [verdict] | [class] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION *(EXCLUDED from gate ledger)*

### Surface Coverage *(per §10 -- cite F-IDs)*

| IN-SCOPE Surface | Domain | Reviewer(s) | Finding F-ID(s) | Coverage |
|-----------------|--------|-------------|-----------------|---------|
| [SURFACE_1] | [domain] | [ROLE] | [F-00n or "none"] | [COVERED / GAP] |
| [SURFACE_2] | [domain] | [ROLE] | [F-00n or "none"] | [COVERED / GAP] |
| [SURFACE_3] | [domain] | [ROLE] | [F-00n or "none"] | [COVERED / GAP] |

**Surface coverage signal**: [COVERED / PARTIAL]

### Domain Coverage Gap-Check *(per §10a)*

| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|---------|
| [DOMAIN-1] | [AM-0n / "none"] | [COVERED / ADVISORY-GAP] |

### §11 ADVISORY-ORPHAN Check

**Findings missing §1:S-n**: [List F-IDs or "None."]

### §18 GLOBAL FINDING REGISTRY

*(All F-IDs assigned during execution. HIGH or MEDIUM with Status=ADVISORY = contract violation.)*

| F-ID | Section | §1 Surface | Severity | Register Status |
|------|---------|-----------|---------|----------------|
| F-001 | DOMAIN -- [ROLE] | [§1:S-n] | [HIGH/MED/LOW] | [ACTIONED / WAIVED / ADVISORY] |
| F-002 | DOMAIN -- [ROLE] | [§1:S-n] | [HIGH/MED/LOW] | [ACTIONED / WAIVED / ADVISORY] |
| F-00n | LIFECYCLE -- [ROLE] | [§1:S-n] | [HIGH/MED/LOW] | [ACTIONED / WAIVED / ADVISORY] |

*(If any F-ID has HIGH or MEDIUM severity with Status=ADVISORY, add to ACTION ITEM REGISTER
as FID-VIOLATION: "F-00n: severity [H/M] finding not actioned or waived".)*

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER_ROLE] | [copy] | DISPOSITION_CONTRACT v1-FID |
| G_domain_agg | [DOMAIN_ROLE] | [copy] | DISPOSITION_CONTRACT v1-FID |
| G_lifecycle | [LIFECYCLE_ROLE] | [copy] | DISPOSITION_CONTRACT v1-FID |
| GClose | [CHALLENGER_ROLE] | [copy] | DISPOSITION_CONTRACT v1-FID |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Incompatible responses. If none: "None."]
**Convergence**: [Concern named by >= 2 reviewers -- cite F-IDs.]
**Scope coverage**: [Uncovered surfaces. If all covered: "None."]

**§13 PROGRESSION LEDGER**:
```
g_null(initial)=[_] | g_null(post-domain)=[_] | g_null(final)=[_] | Trajectory=[label]
```

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

*Assembly per §6: verbatim gate ledger rows, then F-ID indexed items. Do NOT re-derive.*

| Source | CH-ID / F-ID | Item Description | Disposition Class | Owner | Resolution Criterion |
|--------|-------------|-----------------|------------------|-------|---------------------|
| [gate ledger] | -- | [verbatim row] | [class] | [ROLE] | [criterion] |
| [HIGH/MED finding] | F-00n | [What must be done] | [BLOCKED / CONDITIONAL] | [ROLE] | [criterion] |
| [lens HIGH] | AM-0n / Q-n | ADVISORY-OPEN-LENS-REQUIRED: [entry] | ADVISORY | [ROLE] | Produce finding. |
| [lens MED] | AM-0n / Q-n | ADVISORY-OPEN-LENS: [entry] | ADVISORY | [ROLE] | Address or justify. |
| [scope gap] | -- | ADVISORY-GAP: §1 [surface] | ADVISORY | [ROLE] | Assign reviewer. |
| [domain gap] | -- | ADVISORY-GAP (DOMAIN): [domain] | ADVISORY | [ROLE] | Add reviewer. |
| [orphan] | F-00n | ADVISORY-ORPHAN: missing §1 citation | ADVISORY | [ROLE] | Add citation. |
| [fid violation] | F-00n | FID-VIOLATION: severity [H/M] not actioned or waived | [class] | [ROLE] | Action or waive. |

---

**Artifact to review:**

{{artifact}}
