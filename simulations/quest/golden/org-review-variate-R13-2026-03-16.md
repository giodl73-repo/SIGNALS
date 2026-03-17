# org-review Variations -- Round 13 (v11 rubric, 2026-03-16)
Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v11-2026-03-16.md

Prior round summary:
- R1--R11: V-05 climbed to 210/225 via bracket architecture, local ledger, CH-ID tracing,
  domain-agg formula, scope coverage gate, g_null progression ledger, finding-surface linkage,
  conditional resolution registry, per-finding severity aggregation (C-30), lens exhaustion (C-31),
  primary driver derivation (C-32).
- R12: V-02 R12 achieved ~215/225 (C-33 PASS + C-34 PASS + C-35 PASS simultaneously but
  without C-30+C-31+C-32 base). V-01 R12 scored 71 (C-09 FAIL). V-03--V-05 R12 TBD.
- Gap: Perfect score (225) requires V-05 R11's C-30+C-31+C-32 base COMBINED with V-02 R12's
  C-33+C-34+C-35 additions.

Round 13 strategy:
- Baseline: V-05 R11 (§1-§16, C-30+C-31+C-32 PASS) as non-negotiable base. All R13 variants
  inherit §1-§16 and score >=210 from base inheritance.
- R13 is a frontier-extension round targeting simultaneous C-33+C-34+C-35 on top of C-30+C-31+C-32.
- V-01: single axis -- §17 NULL HYPOTHESIS DIMENSION TABLE CONTRACT. Adds a dedicated per-dimension
  current-state vs proposed-state table to BRACKET OPENING. g_null derivable from NH Verdict column
  alone. Targets C-35.
- V-02: single axis -- §17 LENS APPLICABILITY CONTRACT. Extends §15 LENS COVERAGE TABLE with
  artifact-specific applicability ratings (HIGH/MEDIUM/LOW). Coverage expectation rules pre-committed.
  Targets C-33.
- V-03: single axis -- §17 LENS APPLICABILITY CONTRACT + §18 DOMAIN COVERAGE GAP-CHECK CONTRACT.
  Extends §15 with applicability ratings AND adds post-lens-table domain-inward gap-check.
  Targets C-33+C-34 together (C-34 logically requires applicability framework).
- V-04: combination -- V-01 + V-02 axes (§17 NH DIMENSION TABLE + §18 LENS APPLICABILITY).
  Targets C-35+C-33.
- V-05: full integration -- V-01 + V-02 + V-03 axes (§17 + §18 + §19).
  Targets C-35+C-33+C-34 simultaneously. Candidate for 225/225.

---

## V-01 -- Single Axis: Null Hypothesis Dimension Table (C-35)

**Variation axis**: §17 NULL HYPOTHESIS DIMENSION TABLE CONTRACT. The BRACKET OPENING challenger
evaluates the null hypothesis using a structured per-dimension comparison table (current-state score
vs proposed-state score, per-dimension differential, per-dimension NH Verdict). g_null is derivable
from the NH Verdict column alone without reading challenger prose.

**Hypothesis**: Currently the challenger evaluates the null hypothesis through a three-option
alternatives comparison table (Status Quo / Build / Best Non-Build Alt) with no per-dimension
differentials or NH Verdict column, so g_null cannot be verified from table values alone -- the
NULL HYPOTHESIS DERIVATION RULE must be read alongside the table to interpret the verdict. §17
adds a dedicated NULL HYPOTHESIS DIMENSION TABLE to the BRACKET OPENING (separate from the C-16
alternatives table) with columns: Dimension | Current-State Score | Proposed-State Score |
Differential | NH Verdict. The NH Verdict column (FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD) makes
g_null mechanically derivable: g_null = DEFEATED if no MUST-CLEAR row shows OPPOSES-BUILD and
FAVORS-BUILD count > OPPOSES-BUILD count; HOLDS if any MUST-CLEAR row shows OPPOSES-BUILD; else
CONDITIONAL. A scorer verifying g_null reads only the NH Verdict column; no prose needed.

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
[Fill this section before proceeding. This is the pre-reviewer gate.]

IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive. These rows are cited in §5.5 SCOPE COVERAGE RECONCILIATION
  and §11 FINDING-SURFACE LINKAGE.)

OUT-OF-SCOPE -- surfaces this review will not evaluate:
  1. [SURFACE -- REASON_EXCLUDED]
  (Write "None" if nothing is excluded.)

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
  Silent scope expansion violates this contract.

§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment. No commitment proceeds with open HIGH findings.
  MEDIUM = Conditions commitment. Proceeds only after named resolution.
  LOW    = Advisory. Commitment may proceed.
  These definitions apply universally. They may not be restated at any gate.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose = FAIL  [override: null hypothesis holds]
                OR  exists Gi = FAIL
  CONDITIONAL  <-- no Gi = FAIL  AND  exists Gi = CONDITIONAL
  READY        <-- all Gi = PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst verdict among all G_domain rows.
  Precedence: FAIL > CONDITIONAL > PASS.
  Single domain reviewer: G_domain_agg = G_domain (direct pass-through).
  Multiple domain reviewers: G_domain_agg = worst(G_domain_1, ..., G_domain_n).
  BRACKET CLOSING applies this formula mechanically.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A missing cite is an audit-trail gap.

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, ...).
  Every downstream section carries a mandatory CH-ID response table.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class derivation: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section, after verdict is stated.
  Assembly: ACTION ITEM REGISTER copies all local ledger rows verbatim. No re-derivation
  of Gate Verdict or Class is permitted during assembly.
  EXCLUDED (no ledger row emitted): §3.5, §3.8, §5.5.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1. ROLE MANIFEST
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
  SATURATED: CH-ID has received a DOMAIN response before LIFECYCLE runs.
  FULLY SATURATED: CH-ID has received DOMAIN + LIFECYCLE responses before BRACKET CLOSING.
  PASS from BRACKET CLOSING is prohibited without full saturation or a stated waiver.
  Waiver format: "CH-XXX WAIVER: [reason this CH-ID cannot receive a response from [section]]"

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = GOpen  [emitted at BRACKET OPENING]
  Stage 2: g_null(post-domain) = formula(G_domain_agg, g_null(initial))  [emitted at §3.5]
    G_domain_agg=FAIL -> FAIL
    G_domain_agg=CONDITIONAL -> max(g_null(initial), CONDITIONAL)
    G_domain_agg=PASS -> g_null(initial)
  Stage 3: g_null(final) = formula(G_lifecycle, g_null(post-domain))  [emitted at BRACKET CLOSING]
    G_lifecycle=FAIL -> FAIL
    G_lifecycle=CONDITIONAL -> max(g_null(post-domain), CONDITIONAL)
    G_lifecycle=PASS -> g_null(post-domain)
  GClose must equal g_null(final). Deviation requires: "g_null OVERRIDE: [justification]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  After BRACKET CLOSING, §5.5 SCOPE COVERAGE RECONCILIATION maps each §1 IN-SCOPE surface
  to reviewer findings. Classification: COVERED (>= 1 finding) or GAP (no finding).
  GAP surfaces -> ADVISORY-GAP in ACTION ITEM REGISTER.
  Gate signal COVERED/PARTIAL is informational only. §5.5 emits no ledger row.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding in DOMAIN and LIFECYCLE sections carries a "[§1:S-n]" citation naming the
  in-scope surface it addresses. A finding without a valid §1:S-n citation = ADVISORY-ORPHAN.
  ADVISORY-ORPHAN items are appended to ACTION ITEM REGISTER.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION = CONDITIONAL -> emit RESOLUTION REGISTRY table after Overall Disposition:
    | Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status=OPEN |
  One row per CONDITIONAL gate. Resolution Criterion must be a falsifiable test.
  DISPOSITION != CONDITIONAL -> "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS must include a §13 PROGRESSION LEDGER sub-section:
    g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory label
  Trajectory labels: MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
                     DOMAIN-RECOVERED / LIFECYCLE-RECOVERED. Informational only.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Within each DOMAIN and LIFECYCLE section, findings are presented as a table:
    | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all individual finding severities). Precedence: HIGH>MEDIUM>LOW.
  No findings present: Section Severity = LOW.
  Do not assign Section Severity editorially. Apply the worst-case formula.
  The Section Severity is the value entered in the Local Gate Ledger Row's Class derivation.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN and LIFECYCLE section must address ALL entries from the role's lens.verify list.
  After the findings table, emit a LENS COVERAGE TABLE:
    | # | lens.verify Entry | Status | Finding Reference |
    Status values: ADDRESSED (a finding references this lens dimension) /
                   OPEN (no finding referenced this lens dimension).
  OPEN entries are automatically promoted to ADVISORY-OPEN-LENS in the ACTION ITEM REGISTER.
  Lens exhaustion is a completeness audit, not a gate condition.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  The Primary Driver of the disposition is derived by the following precedence rule.
  Apply mechanically at DISPOSITION time. Do not assign editorially.

  PRIMARY DRIVER DERIVATION RULE:
    1. if GClose = FAIL:                Primary Driver = BRACKET CLOSING  [override invoked]
    2. elif G_domain_agg = FAIL:        Primary Driver = DOMAIN
    3. elif G_lifecycle = FAIL:         Primary Driver = LIFECYCLE
    4. elif GOpen = FAIL:               Primary Driver = BRACKET OPENING
    5. elif GClose = CONDITIONAL:       Primary Driver = BRACKET CLOSING  [partial defeat]
    6. elif G_domain_agg = CONDITIONAL: Primary Driver = DOMAIN
    7. elif G_lifecycle = CONDITIONAL:  Primary Driver = LIFECYCLE
    8. elif GOpen = CONDITIONAL:        Primary Driver = BRACKET OPENING
    9. else (all PASS):                 Primary Driver = N/A

  Emit at DISPOSITION:
    **Applying §16 rule**: [state rule number fired and why]
    **Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]       ← NEW IN V-01
  The BRACKET OPENING challenger evaluates the null hypothesis using a dedicated per-dimension
  comparison table (NULL HYPOTHESIS DIMENSION TABLE). This table is SEPARATE from the C-16
  alternatives comparison table and appears after it.

  Table format:
    | Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
    NH Verdict values: FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD
    Differential = Proposed-State Score minus Current-State Score.
    NH Verdict: positive Differential -> FAVORS-BUILD; zero -> NEUTRAL; negative -> OPPOSES-BUILD.

  MUST-CLEAR dimensions: mark with asterisk (*) in the Dimension column.
  g_null derivation rule (pre-committed; applied at BRACKET OPENING):
    HOLDS      <-- any MUST-CLEAR row has NH Verdict = OPPOSES-BUILD
    CONDITIONAL <-- no MUST-CLEAR row OPPOSES-BUILD AND count(OPPOSES-BUILD) >= count(FAVORS-BUILD)
    DEFEATED   <-- no MUST-CLEAR row OPPOSES-BUILD AND count(FAVORS-BUILD) > count(OPPOSES-BUILD)
  g_null = DEFEATED -> GOpen = PASS; CONDITIONAL -> GOpen = CONDITIONAL; HOLDS -> GOpen = FAIL.
  A scorer verifying g_null reads only the NH Verdict column. Prose arguments may add context
  but are not required to determine g_null.
======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. CHALLENGER positions remain fixed. State total count.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table** *(>= 3 dimensions; re-scored by domain reviewers per §16 C-16)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17 -- g_null derivable from NH Verdict column alone)*:

| Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
|-----------|--------------------------|----------------------------|--------------|------------|
| [DIM-A*]  | [N]                       | [M]                         | [M-N]        | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [N]                       | [M]                         | [M-N]        | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [N]                       | [M]                         | [M-N]        | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

*(Dimensions marked * are MUST-CLEAR. Apply §17 g_null derivation rule to NH Verdict column.)*

**Applying §17 g_null derivation rule**:
```
MUST-CLEAR rows with OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD) = [N] | count(OPPOSES-BUILD) = [M]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null (from table)**: [HOLDS / CONDITIONAL / DEFEATED]

**NULL HYPOTHESIS DERIVATION RULE** *(per §9; confirms table result at BRACKET CLOSING)*:
  g_null confirmed by §17 table derivation. BRACKET CLOSING re-applies to revised table.

**Challenge claims** *(assign CH-IDs per §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction. One sentence.] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL -- consistent with §17 g_null table result]
**GOpen Reason**: [One sentence.]
**g_null(initial)** *(per §9 Stage 1 -- equals GOpen)*: [PASS / CONDITIONAL / FAIL]

*GOpen, g_null(initial), and all CH-IDs carry forward to every downstream section.*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]

**CH-ID Response Table** *(mandatory per §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

*(PARTIAL requires a named resolution path. OPEN = claim not addressable from this role's frame.)*

**Domain re-score** *(same dimensions as BRACKET OPENING alternatives table; re-score from this role's frame)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| [DIM-1] | [revised] | [revised] | [revised] | [reason] |
| [DIM-2] | [revised] | [revised] | [revised] | |
| [DIM-3] | [revised] | [revised] | [revised] | |

**Additional Findings** *(per §14: per-finding severity table; per §11: each finding cites §1 surface)*:

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
**Section Severity**: [HIGH / MEDIUM / LOW] -- mechanical result per §14; do not assign editorially.

**Lens Coverage Table** *(per §15 -- ALL lens.verify entries from role definition)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|-------------------|
| Q-1 | [Full text of lens.verify entry 1] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text of lens.verify entry 2] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-3 | [Full text of lens.verify entry 3 if present] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(Add rows for all lens.verify entries. OPEN entries -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence. If CONDITIONAL: name condition. If FAIL: name gap.]

*(For `--depth deep`: repeat as DOMAIN-2, DOMAIN-3. Each emits its own local ledger row, domain re-score, and lens coverage table. G_domain Aggregate = worst of all G_domain rows per §3a.)*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6 -- this section produces no verdict of its own.)*

**Applying §3a formula**:
```
G_domain rows collected:
  DOMAIN -- [ROLE_NAME]: [verdict]
  (DOMAIN-2 -- [ROLE_NAME]: [verdict] if --depth deep)
G_domain_agg = worst([list]) = [PASS / CONDITIONAL / FAIL]
```
**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

**Applying §9 Stage 2 formula**:
```
g_null(initial) = [copy from BRACKET OPENING] | G_domain_agg = [copy]
  FAIL->FAIL | CONDITIONAL->max(initial,CONDITIONAL) | PASS->g_null(initial)
g_null(post-domain) = [FAIL / CONDITIONAL / PASS]
```
**g_null(post-domain)**: [FAIL / CONDITIONAL / PASS]

*Both carry forward to §3.8, LIFECYCLE, and BRACKET CLOSING.*

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger per §6. Runs after §3.5, before LIFECYCLE.)*

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | [copy from DOMAIN] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED -- or N/A] |

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

**Additional Findings** *(per §14: per-finding severity table; per §11: each finding cites §1 surface)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1 -- commitment, program, or decision concerns.] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

*(Findings without a valid §1:S-n citation are ADVISORY-ORPHAN per §11.)*

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] -- mechanical result per §14; do not assign editorially.

**Lens Coverage Table** *(per §15 -- ALL lens.verify entries from role definition)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|-------------------|
| Q-1 | [Full text of lens.verify entry 1] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text of lens.verify entry 2] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(OPEN entries -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.)*

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
*Full record received: scope declaration, all CH-ID tables, all gate verdicts.*

**Applying §9 Stage 3 formula**:
```
g_null(post-domain) = [copy from §3.5]
G_lifecycle         = [copy from LIFECYCLE local ledger]
  FAIL->FAIL | CONDITIONAL->max(post-domain,CONDITIONAL) | PASS->g_null(post-domain)
g_null(final) = [FAIL / CONDITIONAL / PASS]
```
**g_null(final)**: [FAIL / CONDITIONAL / PASS]
*GClose must equal g_null(final) per §9. Deviation requires override justification below.*

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(per §17 -- aggregate domain re-scores; re-derive g_null)*:

| Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
|-----------|--------------------------|----------------------------|--------------|------------|
| [DIM-A*]  | [agg]                     | [agg]                       | [agg diff]   | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [agg]                     | [agg]                       | [agg diff]   | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [agg]                     | [agg]                       | [agg diff]   | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

**Applying §17 g_null derivation rule to revised table**:
```
MUST-CLEAR rows with OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD) = [N] | count(OPPOSES-BUILD) = [M]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```

**Revised alternatives table** *(aggregate domain re-scores; §16 C-16 scaffold)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Domain Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| [DIM-1] | [agg] | [agg] | [agg] | [reason] |
| [DIM-2] | [agg] | [agg] | [agg] | |
| [DIM-3] | [agg] | [agg] | [agg] | |

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

**Remaining gaps**: [All defeated, or list gaps.]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A -- formula applied | or: override justification one sentence]

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts per contract §3.

**GClose Rationale**: [2-3 sentences. Reference g_null(final) from §17 revised table derivation,
CH-ID saturation, and null hypothesis trajectory (initial -> post-domain -> final).]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6. Runs after BRACKET CLOSING, before GATE VECTOR TABLE.)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [DOMAIN F-n / etc.] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [reference] | [COVERED / GAP] |

**Coverage gate signal** *(§10 -- informational)*: [COVERED / PARTIAL]

**§11 ADVISORY-ORPHAN check** *(findings lacking §1 citation)*:
- [Finding reference or "None"]

**Forced advisory items for ACTION ITEM REGISTER**:
- GAP surfaces (§10): [list or "None"]
- ADVISORY-ORPHAN findings (§11): [list or "None"]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen -- bracket opening | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain -- domain aggregate | [DOMAIN_ROLE(S)] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle -- lifecycle | [LIFECYCLE_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose -- bracket closing | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Two reviewers with incompatible CH-ID responses or findings. If none: "None detected."]

**Convergence**: [CH-ID or concern named by 2+ reviewers. Name it and explain confidence.]

**§13 Progression Ledger** *(per §13 -- informational; no ledger row emitted)*:
```
g_null(initial)     = [copy from BRACKET OPENING]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING]
Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED /
                     LIFECYCLE-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

**Scope coverage** *(§10 gate signal)*: [COVERED / PARTIAL]

---

## DISPOSITION

**Gate vector** *(fill from GATE VECTOR TABLE)*:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply §3 formula** *(do not alter; do not reason editorially)*:
```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose=FAIL? -> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi=FAIL? -> BLOCKED
No FAIL, any CONDITIONAL? -> CONDITIONAL
All PASS? -> READY
```

**Null hypothesis progression** *(§9 -- from §13 ledger)*:
- g_null(initial)=[copy] | g_null(post-domain)=[copy] | g_null(final)=[copy]
- Trajectory: [from §13 PROGRESSION LEDGER]

**Scope coverage** *(§10 -- informational)*: [COVERED / PARTIAL]

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**RESOLUTION REGISTRY** *(per §12 -- emit if CONDITIONAL; otherwise write N/A line)*:

| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [verbatim condition] | [ROLE_NAME] | [falsifiable criterion] | OPEN |

*RESOLUTION REGISTRY: N/A -- disposition is [READY/BLOCKED]* <- delete this line if CONDITIONAL

**Applying §16 PRIMARY DRIVER DERIVATION RULE**:
```
GClose=[_], G_domain_agg=[_], G_lifecycle=[_], GOpen=[_]
Rule fired: [state rule number 1-9 from §16 and why it fires before others]
```
**Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**Conditions** *(if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]

**Blocker** *(if BLOCKED)*: [Specific finding from the FAIL gate.]

---

## ACTION ITEM REGISTER

*Copy all Local Gate Ledger rows from BRACKET OPENING, DOMAIN(s), LIFECYCLE, and BRACKET CLOSING
verbatim. Do not re-derive Gate Verdict or Class. Append: CH-ID PARTIAL/HOLDS rows, §8 waiver rows
(ADVISORY), §10 ADVISORY-GAP rows from §5.5, §11 ADVISORY-ORPHAN rows from §5.5, §15
ADVISORY-OPEN-LENS rows.*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [copy from local ledger] | [copy] | [copy] | [copy] | [What must be done] | [ROLE_NAME] | [Criterion] |
| CH-001 | -- | -- | [BLOCKED/CONDITIONAL/ADVISORY] | [Item from CH-ID status] | [ROLE_NAME] | [Criterion] |
| §8 WAIVER | -- | -- | ADVISORY | [Waiver text if any] | [ROLE_NAME] | N/A |
| §10 SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [Surface not addressed] | [ROLE_NAME] | [Criterion] |
| §11 FINDING-SURFACE LINKAGE | -- | -- | ADVISORY-ORPHAN | [Finding with no §1 citation] | [ROLE_NAME] | [Criterion] |
| §15 LENS EXHAUSTION | -- | -- | ADVISORY-OPEN-LENS | [Unanswered lens.verify entry] | [ROLE_NAME] | [Criterion] |
| -- | -- | -- | ADVISORY-OBS | [Advisory observation not from CH-ID or gate] | [ROLE_NAME] | [Criterion] |

*FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY*
*ADVISORY-GAP: §10 | ADVISORY-ORPHAN: §11 | ADVISORY-OPEN-LENS: §15*

---

**Artifact to review:**

{{artifact}}
```

---
## V-02 -- Single Axis: Lens Applicability Rating (C-33)

**Variation axis**: §17 LENS APPLICABILITY CONTRACT. Each row in the LENS COVERAGE TABLE (§15)
carries an artifact-specific applicability rating (HIGH / MEDIUM / LOW) pre-committed as the
rated basis for the ADDRESSED/OPEN determination. Coverage obligation rules are pre-committed
per tier. C-31 can classify without C-33; C-33 adds the evidence underlying the classification.

**Hypothesis**: Currently §15 LENS COVERAGE TABLE classifies entries as ADDRESSED/OPEN with no
evidence of why coverage is expected for this artifact specifically. §17 adds an Applicability
column. Applicability is rated per artifact (not from role definitions). Pre-committed rules
map applicability to obligation: HIGH OPEN -> mandatory ADVISORY-OPEN-LENS; MEDIUM OPEN ->
ADVISORY-OPEN-LENS unless waived; LOW OPEN -> informational only. ADDRESSED/OPEN determination
becomes a derived function of the Applicability rating rather than an editorial judgment.

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
IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Cited in §5.5 and §11.)
OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]
Scope Amendment Protocol: SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks commitment. MEDIUM=Conditions commitment. LOW=Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts). BRACKET CLOSING applies mechanically.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim receives a CH-ID. Every downstream section carries a CH-ID response table.
  PASS prohibited if any CH-ID shows OPEN status.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section. Assembly: verbatim copy. No re-derivation.
  EXCLUDED (no ledger row): §3.5, §3.8, §5.5.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.ROLE MANIFEST | 2.BRACKET OPENING | 3.DOMAIN(s) | 3.5.DOMAIN-AGG CHECKPOINT |
  3.8.CH-ID SATURATION CHECK | 4.LIFECYCLE | 5.BRACKET CLOSING |
  5.5.SCOPE COVERAGE RECONCILIATION | 6.GATE VECTOR TABLE | 7.CROSS-ROLE SIGNALS |
  8.DISPOSITION | 9.ACTION ITEM REGISTER. Reordering violates this contract.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: DOMAIN response before LIFECYCLE.
  FULLY SATURATED: DOMAIN+LIFECYCLE before BRACKET CLOSING.
  PASS prohibited without full saturation or stated waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = GOpen.
  Stage 2: FAIL->FAIL; CONDITIONAL->max(initial,CONDITIONAL); PASS->initial.
  Stage 3: FAIL->FAIL; CONDITIONAL->max(post-domain,CONDITIONAL); PASS->post-domain.
  GClose must equal g_null(final) or declare "g_null OVERRIDE: [reason]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps §1 surfaces to findings. GAP->ADVISORY-GAP. Gate signal informational.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding carries "[§1:S-n]" citation. No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit RESOLUTION REGISTRY after Overall Disposition.
  | Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status=OPEN |

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS §13 PROGRESSION LEDGER:
  g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory label. Informational only.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Findings as table: | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all finding severities). No findings = LOW. Do not assign editorially.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE section: address ALL role lens.verify entries.
  LENS COVERAGE TABLE format (extended per §17):
    | # | lens.verify Entry | Applicability | Status | Finding Reference |
  Status: ADDRESSED / OPEN.
  OPEN coverage obligation determined by §17 Applicability tier rules.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  PRIMARY DRIVER DERIVATION RULE (apply mechanically at DISPOSITION):
    1. GClose=FAIL -> BRACKET CLOSING      5. GClose=CONDITIONAL -> BRACKET CLOSING
    2. G_domain_agg=FAIL -> DOMAIN         6. G_domain_agg=CONDITIONAL -> DOMAIN
    3. G_lifecycle=FAIL -> LIFECYCLE       7. G_lifecycle=CONDITIONAL -> LIFECYCLE
    4. GOpen=FAIL -> BRACKET OPENING       8. GOpen=CONDITIONAL -> BRACKET OPENING
    9. all PASS -> N/A
  Emit: **Applying §16 rule**: [rule + why] | **Primary Driver**: [value]

§17 -- LENS APPLICABILITY CONTRACT [IMMUTABLE]                    <- NEW IN V-02
  The LENS COVERAGE TABLE (§15) must include an Applicability column for each lens.verify entry.
  The Applicability rating is artifact-specific -- rate per artifact under review, not from role
  definitions. The same role may carry different ratings for different artifact types.

  Applicability values: HIGH / MEDIUM / LOW

  Pre-committed coverage obligation rules:
    HIGH   = Lens dimension is directly and specifically applicable to this artifact type.
             OPEN at HIGH -> mandatory ADVISORY-OPEN-LENS registration in ACTION ITEM REGISTER.
    MEDIUM = Lens dimension applies with adaptation to this artifact type.
             OPEN at MEDIUM -> ADVISORY-OPEN-LENS registration unless waiver stated inline:
             "Q-n MEDIUM-WAIVER: [reason this dimension need not be addressed for this artifact]"
    LOW    = Lens dimension is generic and only indirectly applicable to this artifact type.
             OPEN at LOW -> informational note only. No ADVISORY-OPEN-LENS registration.

  Rate Applicability before reviewing findings. The Applicability rating is the pre-committed
  basis for the ADDRESSED/OPEN determination. A HIGH-applicability lens must be ADDRESSED;
  a LOW-applicability lens OPEN requires no remediation for this artifact.
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

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3. CHALLENGER positions remain fixed.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [One sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table** *(>= 3 dimensions)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DERIVATION RULE** *(per §9)*: [Formula mapping table to g_null verdict.]

**Challenge claims**:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger lens.verify.]
**Simplify**: [One from challenger lens.simplify.]
**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)** *(per §9 Stage 1)*: [PASS / CONDITIONAL / FAIL]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Domain re-score** *(same dimensions as BRACKET OPENING; re-score from this role's frame)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| [DIM-1] | [revised] | [revised] | [revised] | [reason] |
| [DIM-2] | [revised] | [revised] | [revised] | |
| [DIM-3] | [revised] | [revised] | [revised] | |

**Additional Findings** *(per §14 + §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1 -- from this role's lens.verify and expertise.depth.] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-3 | [§1:S-n -- optional] | [FINDING_3] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] -- mechanical per §14.

**Lens Coverage Table** *(per §15 + §17 -- rate Applicability per artifact before reviewing)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|---------------|--------|-------------------|
| Q-1 | [Full text of lens.verify entry 1] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text of lens.verify entry 2] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-3 | [Full text of lens.verify entry 3 if present] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(Per §17: HIGH OPEN -> mandatory ADVISORY-OPEN-LENS.
MEDIUM OPEN -> ADVISORY-OPEN-LENS unless "Q-n MEDIUM-WAIVER: [reason]" stated above.
LOW OPEN -> informational only; omit from register.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's lens.simplify.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*(For `--depth deep`: repeat DOMAIN-2, DOMAIN-3. Each emits own ledger row and lens coverage table.)*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6.)*

```
G_domain_agg = worst([DOMAIN verdicts]) = [PASS / CONDITIONAL / FAIL]
g_null(post-domain) via §9 Stage 2 = [FAIL / CONDITIONAL / PASS]
```
**G_domain Aggregate**: [verdict] | **g_null(post-domain)**: [verdict]

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger per §6.)*

| CH-ID | DOMAIN Status | Pre-LIFECYCLE Saturation |
|-------|--------------|--------------------------|
| CH-001 | [copy] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED -- or N/A] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None"]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy] | G_domain Aggregate: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph referencing GOpen, G_domain Aggregate, g_null(post-domain).]
**Null hypothesis status**: [yes / partial / no -- one sentence.]

**Additional Findings** *(per §14 + §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1 -- commitment, program, or decision concerns.] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] -- mechanical per §14.

**Lens Coverage Table** *(per §15 + §17)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|---------------|--------|-------------------|
| Q-1 | [Full text of lens.verify entry 1] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text of lens.verify entry 2] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(Per §17 obligation rules: HIGH OPEN mandatory; MEDIUM unless waived; LOW informational.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's lens.simplify.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Applying §9 Stage 3**:
```
g_null(post-domain)=[copy] + G_lifecycle=[copy] -> g_null(final): [FAIL/CONDITIONAL/PASS]
```

**Revised alternatives table** *(aggregate domain re-scores)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------|
| [DIM-1] | [agg] | [agg] | [agg] | |
| [DIM-2] | [agg] | [agg] | [agg] | |
| [DIM-3] | [agg] | [agg] | [agg] | |

**Applying NULL HYPOTHESIS DERIVATION RULE to revised table**: [Result. One sentence.]

**Full CH-ID Saturation Check** *(per §8)*:

| CH-ID | DOMAIN | LIFECYCLE | Full Saturation | Waiver |
|-------|--------|-----------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [All defeated, or list gaps.]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A or justification]
**GClose Rationale**: [2-3 sentences referencing g_null trajectory and saturation.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6.)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [reference] | [COVERED / GAP] |

**Coverage gate signal** *(§10)*: [COVERED / PARTIAL]
**§11 ADVISORY-ORPHAN check**: [findings without §1 citation, or "None"]
**Forced advisory items**: [GAP and ADVISORY-ORPHAN items, or "None"]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER_ROLE] | [verdict] | DISPOSITION_CONTRACT v1 |
| G_domain (agg) | [DOMAIN_ROLE(S)] | [verdict] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE_ROLE] | [verdict] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER_ROLE] | [verdict] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Name or "None detected."]
**Convergence**: [Name and explain confidence.]

**§13 Progression Ledger**:
```
g_null(initial)=[copy] | g_null(post-domain)=[copy] | g_null(final)=[copy]
Trajectory: [label]
```

**Scope coverage** *(§10)*: [COVERED / PARTIAL]

---

## DISPOSITION

**Gate vector**: GOpen=[copy] | G_domain_agg=[copy] | G_lifecycle=[copy] | GClose=[copy]

**Apply §3 formula**:
```
GClose=FAIL?->BLOCKED | Any FAIL?->BLOCKED | Any CONDITIONAL?->CONDITIONAL | All PASS?->READY
```

**Null hypothesis progression**: g_null(initial)=[copy] -> [copy] -> [copy] | Trajectory: [from §13]
**Scope coverage** *(§10)*: [COVERED / PARTIAL]
**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**RESOLUTION REGISTRY** *(per §12)*:
| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [condition] | [ROLE] | [criterion] | OPEN |
*RESOLUTION REGISTRY: N/A -- disposition is [READY/BLOCKED]* <- delete if CONDITIONAL

**Applying §16 PRIMARY DRIVER DERIVATION RULE**:
```
GClose=[_], G_domain_agg=[_], G_lifecycle=[_], GOpen=[_]
Rule fired: [rule number 1-9 and why]
```
**Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**Conditions** *(if CONDITIONAL)*: 1. [Condition.]
**Blocker** *(if BLOCKED)*: [Finding from FAIL gate.]

---

## ACTION ITEM REGISTER

*Copy all Local Gate Ledger rows verbatim. No re-derivation. Append: CH-ID PARTIAL/HOLDS rows,
§8 waiver rows, §10 ADVISORY-GAP rows, §11 ADVISORY-ORPHAN rows, §15/§17 ADVISORY-OPEN-LENS
rows (HIGH mandatory; MEDIUM unless waived; LOW omitted).*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [local ledger] | [copy] | [copy] | [copy] | [action] | [ROLE] | [criterion] |
| §10 SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [surface] | [ROLE] | [criterion] |
| §11 FINDING-SURFACE LINKAGE | -- | -- | ADVISORY-ORPHAN | [finding] | [ROLE] | [criterion] |
| §15/§17 LENS EXHAUSTION | -- | -- | ADVISORY-OPEN-LENS | [Q-n: applicability tier: entry] | [ROLE] | [criterion] |

*FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY*
*ADVISORY-OPEN-LENS: HIGH mandatory; MEDIUM unless waived; LOW omitted*

---

**Artifact to review:**

{{artifact}}
```

---
## V-03 -- Single Axis: Domain Coverage Gap-Check (C-33 + C-34)

**Variation axis**: §17 LENS APPLICABILITY CONTRACT + §18 DOMAIN COVERAGE GAP-CHECK CONTRACT.
C-34 requires a HIGH-applicability tier, which requires C-33 applicability ratings to exist.
V-03 treats both as a single "domain coverage" axis: extend §15 lens table with applicability
ratings (C-33), then add a domain-inward gap-check after the lens table (C-34). The gap-check
asks: for each artifact domain from §1 scope, does at least one reviewer have HIGH applicability?
If not, that domain is ADVISORY-GAP in the ACTION ITEM REGISTER.

**Hypothesis**: Currently §15 tracks per-role lens exhaustion (role-outward: did the reviewer
use every lens they have?) but nothing tracks per-domain expert coverage (domain-inward: does
each artifact domain have a qualified reviewer?). A domain may have all roles marking relevant
lenses ADDRESSED while no role has HIGH applicability to that domain. §17 adds applicability
ratings to the lens table. §18 adds a DOMAIN COVERAGE GAP-CHECK step: after all lens tables
are populated, list each artifact domain from §1 scope, find the highest applicability tier
any reviewer holds for it, and classify UNCOVERED (no HIGH-applicability reviewer) as
ADVISORY-GAP in the ACTION ITEM REGISTER. This is orthogonal to §15 (C-31) and §5.5 (C-29).

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
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§18;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]  [DOMAIN: domain-label-1]
  2. [SURFACE_2]  [DOMAIN: domain-label-2]
  3. [SURFACE_3]  [DOMAIN: domain-label-3]
  (Add rows. Tag each surface with its artifact domain in brackets. Cited in §5.5, §11, §18.)
OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]
Scope Amendment Protocol: SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks commitment. MEDIUM=Conditions commitment. LOW=Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts). BRACKET CLOSING applies mechanically.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim receives a CH-ID. Every downstream section carries a CH-ID response table.
  PASS prohibited if any CH-ID shows OPEN status.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section. Assembly: verbatim copy. No re-derivation.
  EXCLUDED (no ledger row): §3.5, §3.8, §5.5, §5.8.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.ROLE MANIFEST | 2.BRACKET OPENING | 3.DOMAIN(s) | 3.5.DOMAIN-AGG CHECKPOINT |
  3.8.CH-ID SATURATION CHECK | 4.LIFECYCLE | 5.BRACKET CLOSING |
  5.5.SCOPE COVERAGE RECONCILIATION | 5.8.DOMAIN COVERAGE GAP-CHECK |
  6.GATE VECTOR TABLE | 7.CROSS-ROLE SIGNALS | 8.DISPOSITION | 9.ACTION ITEM REGISTER.
  Reordering violates this contract.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: DOMAIN response before LIFECYCLE.
  FULLY SATURATED: DOMAIN+LIFECYCLE before BRACKET CLOSING.
  PASS prohibited without full saturation or stated waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = GOpen.
  Stage 2: FAIL->FAIL; CONDITIONAL->max(initial,CONDITIONAL); PASS->initial.
  Stage 3: FAIL->FAIL; CONDITIONAL->max(post-domain,CONDITIONAL); PASS->post-domain.
  GClose must equal g_null(final) or declare "g_null OVERRIDE: [reason]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps §1 surfaces to findings. GAP->ADVISORY-GAP. Gate signal informational.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding carries "[§1:S-n]" citation. No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit RESOLUTION REGISTRY after Overall Disposition.
  | Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status=OPEN |

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS §13 PROGRESSION LEDGER:
  g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory label. Informational only.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Findings as table: | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all finding severities). No findings = LOW. Do not assign editorially.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE section: address ALL role lens.verify entries.
  LENS COVERAGE TABLE format (extended per §17):
    | # | lens.verify Entry | Applicability | Status | Finding Reference |
  Status: ADDRESSED / OPEN. OPEN obligation rules governed by §17.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  PRIMARY DRIVER DERIVATION RULE (apply mechanically at DISPOSITION):
    1. GClose=FAIL -> BRACKET CLOSING      5. GClose=CONDITIONAL -> BRACKET CLOSING
    2. G_domain_agg=FAIL -> DOMAIN         6. G_domain_agg=CONDITIONAL -> DOMAIN
    3. G_lifecycle=FAIL -> LIFECYCLE       7. G_lifecycle=CONDITIONAL -> LIFECYCLE
    4. GOpen=FAIL -> BRACKET OPENING       8. GOpen=CONDITIONAL -> BRACKET OPENING
    9. all PASS -> N/A

§17 -- LENS APPLICABILITY CONTRACT [IMMUTABLE]                    <- NEW IN V-03
  LENS COVERAGE TABLE must include an Applicability column. Rate per artifact, not from role
  definitions. The rating is the pre-committed basis for coverage obligation.
  HIGH = directly applicable -> OPEN = mandatory ADVISORY-OPEN-LENS.
  MEDIUM = applies with adaptation -> OPEN = ADVISORY-OPEN-LENS unless waived inline.
  LOW = indirectly applicable -> OPEN = informational only; no registration.

§18 -- DOMAIN COVERAGE GAP-CHECK CONTRACT [IMMUTABLE]             <- NEW IN V-03
  After §5.5 SCOPE COVERAGE RECONCILIATION, §5.8 DOMAIN COVERAGE GAP-CHECK runs.
  §5.8 is excluded from the gate ledger (§6). It produces no gate verdict.

  GAP-CHECK PROCEDURE (apply mechanically):
    Step 1: List all distinct artifact domains from the DOMAIN tags in §1 IN-SCOPE surfaces.
    Step 2: For each domain, identify the highest Applicability tier any reviewer holds for
            any lens.verify entry associated with that domain (from all §15/§17 lens tables).
    Step 3: Classify each domain:
      EXPERT-COVERED  = at least one reviewer has HIGH applicability to this domain.
      PARTIAL-COVERED = no HIGH-applicability reviewer; at least one MEDIUM-applicability reviewer.
      UNCOVERED       = no reviewer with HIGH or MEDIUM applicability to this domain.
    Step 4: Promote UNCOVERED domains to ADVISORY-GAP in ACTION ITEM REGISTER.
            Record: domain name, highest applicability tier present, and reason for gap
            (absent role / no lens entries map to this domain / all lenses LOW).
    Step 5: PARTIAL-COVERED domains are noted as advisory observations (ADVISORY-OBS).

  The gap-check is pre-committed. It does not run editorially at review time.
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

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3. CHALLENGER positions remain fixed.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [One sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table** *(>= 3 dimensions)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DERIVATION RULE** *(per §9)*: [Formula mapping table to g_null verdict.]

**Challenge claims**:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger lens.verify.]
**Simplify**: [One from challenger lens.simplify.]
**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)** *(per §9 Stage 1)*: [PASS / CONDITIONAL / FAIL]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Domain re-score**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| [DIM-1] | [revised] | [revised] | [revised] | [reason] |
| [DIM-2] | [revised] | [revised] | [revised] | |
| [DIM-3] | [revised] | [revised] | [revised] | |

**Additional Findings** *(per §14 + §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-3 | [§1:S-n -- optional] | [FINDING_3] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] -- mechanical per §14.

**Lens Coverage Table** *(per §15 + §17 -- tag domain for each lens entry)*:

| # | lens.verify Entry | Domain | Applicability | Status | Finding Reference |
|---|------------------|--------|---------------|--------|-------------------|
| Q-1 | [Full text of lens.verify entry 1] | [domain-label] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text of lens.verify entry 2] | [domain-label] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-3 | [Full text of lens.verify entry 3] | [domain-label] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(Per §17: HIGH OPEN -> mandatory ADVISORY-OPEN-LENS. MEDIUM OPEN -> unless waived. LOW OPEN -> informational.
Domain column feeds §18 gap-check.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's lens.simplify.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6.)*

```
G_domain_agg = worst([DOMAIN verdicts]) = [PASS / CONDITIONAL / FAIL]
g_null(post-domain) via §9 Stage 2 = [FAIL / CONDITIONAL / PASS]
```
**G_domain Aggregate**: [verdict] | **g_null(post-domain)**: [verdict]

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger per §6.)*

| CH-ID | DOMAIN Status | Pre-LIFECYCLE Saturation |
|-------|--------------|--------------------------|
| CH-001 | [copy] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED -- or N/A] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None"]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy] | G_domain Aggregate: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph referencing GOpen, G_domain Aggregate, g_null(post-domain).]
**Null hypothesis status**: [yes / partial / no -- one sentence.]

**Additional Findings** *(per §14 + §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] -- mechanical per §14.

**Lens Coverage Table** *(per §15 + §17 -- include Domain column)*:

| # | lens.verify Entry | Domain | Applicability | Status | Finding Reference |
|---|------------------|--------|---------------|--------|-------------------|
| Q-1 | [Full text] | [domain-label] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text] | [domain-label] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(Per §17 obligation rules.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's lens.simplify.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Applying §9 Stage 3**:
```
g_null(post-domain)=[copy] + G_lifecycle=[copy] -> g_null(final): [FAIL/CONDITIONAL/PASS]
```

**Revised alternatives table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------|
| [DIM-1] | [agg] | [agg] | [agg] | |
| [DIM-2] | [agg] | [agg] | [agg] | |
| [DIM-3] | [agg] | [agg] | [agg] | |

**Applying NULL HYPOTHESIS DERIVATION RULE to revised table**: [Result. One sentence.]

**Full CH-ID Saturation Check** *(per §8)*:

| CH-ID | DOMAIN | LIFECYCLE | Full Saturation | Waiver |
|-------|--------|-----------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [All defeated, or list gaps.]
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

*(EXCLUDED from gate ledger per §6.)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1 -- domain-label-1] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_2 -- domain-label-2] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_3 -- domain-label-3] | [ROLE or "none"] | [reference] | [COVERED / GAP] |

**Coverage gate signal** *(§10)*: [COVERED / PARTIAL]
**§11 ADVISORY-ORPHAN check**: [findings without §1 citation, or "None"]
**Forced advisory items**: [GAP and ADVISORY-ORPHAN items, or "None"]

---

## §5.8 DOMAIN COVERAGE GAP-CHECK

*(EXCLUDED from gate ledger per §6. Runs after §5.5, before GATE VECTOR TABLE.
Applies §18 DOMAIN COVERAGE GAP-CHECK CONTRACT mechanically.)*

**Step 1 -- Artifact domains from §1**:
- [domain-label-1]: surfaces [list §1 surfaces tagged with this domain]
- [domain-label-2]: surfaces [list]
- [domain-label-3]: surfaces [list]
*(Add rows for all distinct domain labels from §1.)*

**Step 2 -- Highest applicability per domain across all reviewers**:

| Artifact Domain | Reviewer Role(s) | Highest Applicability | Relevant Lens Entry |
|----------------|-----------------|----------------------|---------------------|
| [domain-label-1] | [ROLE_NAME] | [HIGH / MEDIUM / LOW / NONE] | [Q-n or "none"] |
| [domain-label-2] | [ROLE_NAME] | [HIGH / MEDIUM / LOW / NONE] | [Q-n or "none"] |
| [domain-label-3] | [ROLE_NAME] | [HIGH / MEDIUM / LOW / NONE] | [Q-n or "none"] |

**Step 3 -- Domain classification**:

| Artifact Domain | Classification | Reason |
|----------------|----------------|--------|
| [domain-label-1] | [EXPERT-COVERED / PARTIAL-COVERED / UNCOVERED] | [highest tier present + why] |
| [domain-label-2] | [EXPERT-COVERED / PARTIAL-COVERED / UNCOVERED] | |
| [domain-label-3] | [EXPERT-COVERED / PARTIAL-COVERED / UNCOVERED] | |

**Step 4 -- ADVISORY-GAP items** *(UNCOVERED domains only -- per §18)*:
- [domain-label-X]: UNCOVERED -- [reason: absent role / no lens entries map to domain / all lenses LOW].
  -> ADVISORY-GAP in ACTION ITEM REGISTER.
*(Write "None" if all domains EXPERT-COVERED or PARTIAL-COVERED.)*

**Step 5 -- ADVISORY-OBS items** *(PARTIAL-COVERED domains)*:
- [domain-label-Y]: PARTIAL-COVERED -- [highest tier is MEDIUM; no HIGH-applicability reviewer].
  -> ADVISORY-OBS in ACTION ITEM REGISTER.
*(Write "None" if no PARTIAL-COVERED domains.)*

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER_ROLE] | [verdict] | DISPOSITION_CONTRACT v1 |
| G_domain (agg) | [DOMAIN_ROLE(S)] | [verdict] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE_ROLE] | [verdict] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER_ROLE] | [verdict] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Name or "None detected."]
**Convergence**: [Name and explain confidence.]

**§13 Progression Ledger**:
```
g_null(initial)=[copy] | g_null(post-domain)=[copy] | g_null(final)=[copy]
Trajectory: [label]
```

**Scope coverage** *(§10)*: [COVERED / PARTIAL]
**Domain coverage** *(§18)*: [EXPERT-COVERED for all domains / [N] UNCOVERED / [M] PARTIAL-COVERED]

---

## DISPOSITION

**Gate vector**: GOpen=[copy] | G_domain_agg=[copy] | G_lifecycle=[copy] | GClose=[copy]

**Apply §3 formula**:
```
GClose=FAIL?->BLOCKED | Any FAIL?->BLOCKED | Any CONDITIONAL?->CONDITIONAL | All PASS?->READY
```

**Null hypothesis progression**: g_null(initial)=[copy] -> [copy] -> [copy] | Trajectory: [from §13]
**Scope coverage** *(§10)*: [COVERED / PARTIAL]
**Domain coverage** *(§18)*: [summary]
**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**RESOLUTION REGISTRY** *(per §12)*:
| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [condition] | [ROLE] | [criterion] | OPEN |
*RESOLUTION REGISTRY: N/A -- disposition is [READY/BLOCKED]* <- delete if CONDITIONAL

**Applying §16 PRIMARY DRIVER DERIVATION RULE**:
```
GClose=[_], G_domain_agg=[_], G_lifecycle=[_], GOpen=[_]
Rule fired: [rule number 1-9 and why]
```
**Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**Conditions** *(if CONDITIONAL)*: 1. [Condition.]
**Blocker** *(if BLOCKED)*: [Finding from FAIL gate.]

---

## ACTION ITEM REGISTER

*Copy all Local Gate Ledger rows verbatim. No re-derivation. Append: CH-ID PARTIAL/HOLDS rows,
§8 waiver rows, §10 ADVISORY-GAP rows from §5.5, §11 ADVISORY-ORPHAN rows, §15/§17
ADVISORY-OPEN-LENS rows, §18 ADVISORY-GAP rows from §5.8 (UNCOVERED domains), §18 ADVISORY-OBS
rows (PARTIAL-COVERED domains).*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [local ledger] | [copy] | [copy] | [copy] | [action] | [ROLE] | [criterion] |
| §10 SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [surface] | [ROLE] | [criterion] |
| §11 FINDING-SURFACE LINKAGE | -- | -- | ADVISORY-ORPHAN | [finding] | [ROLE] | [criterion] |
| §15/§17 LENS EXHAUSTION | -- | -- | ADVISORY-OPEN-LENS | [Q-n: tier: entry] | [ROLE] | [criterion] |
| §18 DOMAIN COVERAGE GAP-CHECK | -- | -- | ADVISORY-GAP | [domain: uncovered -- reason] | [ROLE] | Add reviewer with HIGH applicability to [domain] |
| §18 DOMAIN COVERAGE GAP-CHECK | -- | -- | ADVISORY-OBS | [domain: partial-covered -- highest tier present] | [ROLE] | [criterion] |

*FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY*
*ADVISORY-GAP: §10 scope, §18 domain | ADVISORY-ORPHAN: §11 | ADVISORY-OPEN-LENS: §15/§17*

---

**Artifact to review:**

{{artifact}}
```

---
## V-04 -- Combination: V-01 + V-02 (C-35 + C-33)

**Variation axes**: §17 NULL HYPOTHESIS DIMENSION TABLE CONTRACT + §18 LENS APPLICABILITY
CONTRACT. V-01 and V-02 operate on independent fields: §17 governs the BRACKET OPENING null
hypothesis evaluation format (challenger's per-dimension table, g_null derivable from NH Verdict
column). §18 governs the LENS COVERAGE TABLE applicability rating (per-lens artifact-specific
tier, pre-committed obligation rules). No shared fields. Combining them activates C-35 + C-33
simultaneously on the V-05 R11 base, targeting 225 - (5 for C-34 only) = 220/225.

**Hypothesis**: V-01 adds §17 (C-35: g_null table-derivable). V-02 adds §17 LENS APPLICABILITY
(C-33: applicability ratings in lens table). V-04 combines both. The combination exposes whether
any applicability tier decision at the lens level correlates with how a dimension was scored in
the null hypothesis table -- a cross-axis signal available to neither contract alone.

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
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§18;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Cited in §5.5 and §11.)
OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]
Scope Amendment Protocol: SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks commitment. MEDIUM=Conditions commitment. LOW=Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts). BRACKET CLOSING applies mechanically.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim receives a CH-ID. Every downstream section carries a CH-ID response table.
  PASS prohibited if any CH-ID shows OPEN status.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section. Assembly: verbatim copy. No re-derivation.
  EXCLUDED (no ledger row): §3.5, §3.8, §5.5.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.ROLE MANIFEST | 2.BRACKET OPENING | 3.DOMAIN(s) | 3.5.DOMAIN-AGG CHECKPOINT |
  3.8.CH-ID SATURATION CHECK | 4.LIFECYCLE | 5.BRACKET CLOSING |
  5.5.SCOPE COVERAGE RECONCILIATION | 6.GATE VECTOR TABLE | 7.CROSS-ROLE SIGNALS |
  8.DISPOSITION | 9.ACTION ITEM REGISTER. Reordering violates this contract.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: DOMAIN response before LIFECYCLE.
  FULLY SATURATED: DOMAIN+LIFECYCLE before BRACKET CLOSING.
  PASS prohibited without full saturation or stated waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = GOpen.
  Stage 2: FAIL->FAIL; CONDITIONAL->max(initial,CONDITIONAL); PASS->initial.
  Stage 3: FAIL->FAIL; CONDITIONAL->max(post-domain,CONDITIONAL); PASS->post-domain.
  GClose must equal g_null(final) or declare "g_null OVERRIDE: [reason]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps §1 surfaces to findings. GAP->ADVISORY-GAP. Gate signal informational.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding carries "[§1:S-n]" citation. No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit RESOLUTION REGISTRY after Overall Disposition.
  | Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status=OPEN |

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS §13 PROGRESSION LEDGER:
  g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory label. Informational only.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Findings as table: | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all finding severities). No findings = LOW. Do not assign editorially.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE section: address ALL role lens.verify entries.
  LENS COVERAGE TABLE format (extended per §18):
    | # | lens.verify Entry | Applicability | Status | Finding Reference |
  Status: ADDRESSED / OPEN. OPEN obligation governed by §18 rules.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  PRIMARY DRIVER DERIVATION RULE (apply mechanically at DISPOSITION):
    1. GClose=FAIL -> BRACKET CLOSING      5. GClose=CONDITIONAL -> BRACKET CLOSING
    2. G_domain_agg=FAIL -> DOMAIN         6. G_domain_agg=CONDITIONAL -> DOMAIN
    3. G_lifecycle=FAIL -> LIFECYCLE       7. G_lifecycle=CONDITIONAL -> LIFECYCLE
    4. GOpen=FAIL -> BRACKET OPENING       8. GOpen=CONDITIONAL -> BRACKET OPENING
    9. all PASS -> N/A

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]      <- NEW (from V-01)
  BRACKET OPENING includes a NULL HYPOTHESIS DIMENSION TABLE separate from the alternatives table.
  Format: | Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
  NH Verdict: FAVORS-BUILD (positive Differential) / NEUTRAL (zero) / OPPOSES-BUILD (negative).
  MUST-CLEAR dimensions marked with asterisk (*).
  g_null derivation rule (pre-committed):
    HOLDS      <-- any MUST-CLEAR row has NH Verdict = OPPOSES-BUILD
    CONDITIONAL <-- no MUST-CLEAR OPPOSES-BUILD AND count(OPPOSES-BUILD) >= count(FAVORS-BUILD)
    DEFEATED   <-- no MUST-CLEAR OPPOSES-BUILD AND count(FAVORS-BUILD) > count(OPPOSES-BUILD)
  GOpen = PASS if DEFEATED; CONDITIONAL if CONDITIONAL; FAIL if HOLDS.
  g_null derivable from NH Verdict column alone. Prose may add context but is not required.
  BRACKET CLOSING re-populates the table with aggregated domain scores and re-applies the rule.

§18 -- LENS APPLICABILITY CONTRACT [IMMUTABLE]                   <- NEW (from V-02)
  LENS COVERAGE TABLE must include an Applicability column. Rate per artifact, not role definitions.
  HIGH = directly applicable -> OPEN = mandatory ADVISORY-OPEN-LENS.
  MEDIUM = applies with adaptation -> OPEN = ADVISORY-OPEN-LENS unless "Q-n MEDIUM-WAIVER: [reason]".
  LOW = indirectly applicable -> OPEN = informational only; no registration.
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

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3. CHALLENGER positions remain fixed.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [One sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table** *(>= 3 dimensions; re-scored by domain reviewers)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17 -- g_null derivable from NH Verdict column alone)*:

| Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
|-----------|--------------------------|----------------------------|--------------|------------|
| [DIM-A*]  | [N]                       | [M]                         | [M-N]        | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [N]                       | [M]                         | [M-N]        | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [N]                       | [M]                         | [M-N]        | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

*(Dimensions marked * are MUST-CLEAR. Apply §17 g_null derivation rule.)*

**Applying §17 g_null derivation rule**:
```
MUST-CLEAR rows with OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD) = [N] | count(OPPOSES-BUILD) = [M]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null (from table)**: [HOLDS / CONDITIONAL / DEFEATED]

**Challenge claims**:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger lens.verify.]
**Simplify**: [One from challenger lens.simplify.]
**GOpen Verdict**: [PASS / CONDITIONAL / FAIL -- consistent with §17 g_null table result]
**GOpen Reason**: [One sentence.]
**g_null(initial)** *(per §9 Stage 1)*: [PASS / CONDITIONAL / FAIL]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Domain re-score** *(same dimensions as BRACKET OPENING alternatives table)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| [DIM-1] | [revised] | [revised] | [revised] | [reason] |
| [DIM-2] | [revised] | [revised] | [revised] | |
| [DIM-3] | [revised] | [revised] | [revised] | |

**Additional Findings** *(per §14 + §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-3 | [§1:S-n -- optional] | [FINDING_3] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] -- mechanical per §14.

**Lens Coverage Table** *(per §15 + §18 -- rate Applicability per artifact before reviewing)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|---------------|--------|-------------------|
| Q-1 | [Full text of lens.verify entry 1] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text of lens.verify entry 2] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-3 | [Full text of lens.verify entry 3] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(Per §18: HIGH OPEN -> mandatory. MEDIUM OPEN -> unless waived. LOW OPEN -> informational.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's lens.simplify.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6.)*

```
G_domain_agg = worst([DOMAIN verdicts]) = [PASS / CONDITIONAL / FAIL]
g_null(post-domain) via §9 Stage 2 = [FAIL / CONDITIONAL / PASS]
```
**G_domain Aggregate**: [verdict] | **g_null(post-domain)**: [verdict]

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger per §6.)*

| CH-ID | DOMAIN Status | Pre-LIFECYCLE Saturation |
|-------|--------------|--------------------------|
| CH-001 | [copy] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED -- or N/A] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None"]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy] | G_domain Aggregate: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph referencing GOpen, G_domain Aggregate, g_null(post-domain).]
**Null hypothesis status**: [yes / partial / no -- one sentence.]

**Additional Findings** *(per §14 + §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] -- mechanical per §14.

**Lens Coverage Table** *(per §15 + §18)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|---------------|--------|-------------------|
| Q-1 | [Full text] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(Per §18 obligation rules.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's lens.simplify.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Applying §9 Stage 3**:
```
g_null(post-domain)=[copy] + G_lifecycle=[copy] -> g_null(final): [FAIL/CONDITIONAL/PASS]
```

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(per §17 -- aggregate domain scores)*:

| Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
|-----------|--------------------------|----------------------------|--------------|------------|
| [DIM-A*]  | [agg]                     | [agg]                       | [agg diff]   | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [agg]                     | [agg]                       | [agg diff]   | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [agg]                     | [agg]                       | [agg diff]   | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

**Applying §17 rule to revised table**:
```
MUST-CLEAR rows with OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD)=[N] | count(OPPOSES-BUILD)=[M]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```

**Revised alternatives table** *(aggregate)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------|
| [DIM-1] | [agg] | [agg] | [agg] | |
| [DIM-2] | [agg] | [agg] | [agg] | |
| [DIM-3] | [agg] | [agg] | [agg] | |

**Full CH-ID Saturation Check** *(per §8)*:

| CH-ID | DOMAIN | LIFECYCLE | Full Saturation | Waiver |
|-------|--------|-----------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [All defeated, or list gaps.]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A or justification]
**GClose Rationale**: [2-3 sentences referencing §17 revised table result, g_null trajectory, saturation.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6.)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [reference] | [COVERED / GAP] |

**Coverage gate signal** *(§10)*: [COVERED / PARTIAL]
**§11 ADVISORY-ORPHAN check**: [findings without §1 citation, or "None"]
**Forced advisory items**: [GAP and ADVISORY-ORPHAN items, or "None"]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER_ROLE] | [verdict] | DISPOSITION_CONTRACT v1 |
| G_domain (agg) | [DOMAIN_ROLE(S)] | [verdict] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE_ROLE] | [verdict] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER_ROLE] | [verdict] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Name or "None detected."]
**Convergence**: [Name and explain confidence.]

**§13 Progression Ledger**:
```
g_null(initial)=[copy] | g_null(post-domain)=[copy] | g_null(final)=[copy]
Trajectory: [label]
```

**Scope coverage** *(§10)*: [COVERED / PARTIAL]

---

## DISPOSITION

**Gate vector**: GOpen=[copy] | G_domain_agg=[copy] | G_lifecycle=[copy] | GClose=[copy]

**Apply §3 formula**:
```
GClose=FAIL?->BLOCKED | Any FAIL?->BLOCKED | Any CONDITIONAL?->CONDITIONAL | All PASS?->READY
```

**Null hypothesis progression**: g_null(initial)=[copy] -> [copy] -> [copy] | Trajectory: [from §13]
**Scope coverage** *(§10)*: [COVERED / PARTIAL]
**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**RESOLUTION REGISTRY** *(per §12)*:
| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [condition] | [ROLE] | [criterion] | OPEN |
*RESOLUTION REGISTRY: N/A -- disposition is [READY/BLOCKED]* <- delete if CONDITIONAL

**Applying §16 PRIMARY DRIVER DERIVATION RULE**:
```
GClose=[_], G_domain_agg=[_], G_lifecycle=[_], GOpen=[_]
Rule fired: [rule number 1-9 and why]
```
**Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**Conditions** *(if CONDITIONAL)*: 1. [Condition.]
**Blocker** *(if BLOCKED)*: [Finding from FAIL gate.]

---

## ACTION ITEM REGISTER

*Copy all Local Gate Ledger rows verbatim. No re-derivation. Append: CH-ID, §8, §10, §11,
§15/§18 ADVISORY-OPEN-LENS rows (HIGH mandatory; MEDIUM unless waived; LOW omitted).*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [local ledger] | [copy] | [copy] | [copy] | [action] | [ROLE] | [criterion] |
| §10 SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [surface] | [ROLE] | [criterion] |
| §11 FINDING-SURFACE LINKAGE | -- | -- | ADVISORY-ORPHAN | [finding] | [ROLE] | [criterion] |
| §15/§18 LENS EXHAUSTION | -- | -- | ADVISORY-OPEN-LENS | [Q-n: tier: entry] | [ROLE] | [criterion] |

*FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY*

---

**Artifact to review:**

{{artifact}}
```

---
## V-05 -- Full Integration: V-01 + V-02 + V-03 (C-35 + C-33 + C-34)

**Variation axes**: §17 NULL HYPOTHESIS DIMENSION TABLE + §18 LENS APPLICABILITY + §19 DOMAIN
COVERAGE GAP-CHECK. All three new R13 axes combined on the V-05 R11 base (§1-§16).
Candidate for 225/225 if C-35+C-33+C-34 all PASS simultaneously.

**Hypothesis**: The three new criteria are structurally independent. §17 operates at BRACKET
OPENING (challenger null hypothesis format -- g_null table-derivable). §18 operates at reviewer
lens tables (applicability rating column -- per-lens rated basis). §19 operates post-lens-table
(domain-inward gap-check -- UNCOVERED domains promoted to ADVISORY-GAP). No shared fields.
§18 is a prerequisite for §19 (applicability ratings must exist to determine HIGH tier). V-05
integrates all three: §17 adds C-35, §18 adds C-33, §19 adds C-34. Combined with V-05 R11
base (C-30+C-31+C-32 PASS from §14+§15+§16), this is the first variant that can achieve
C-30+C-31+C-32+C-33+C-34+C-35 simultaneously, targeting the perfect 225/225 score.

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
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§19;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]  [DOMAIN: domain-label-1]
  2. [SURFACE_2]  [DOMAIN: domain-label-2]
  3. [SURFACE_3]  [DOMAIN: domain-label-3]
  (Add rows. Be exhaustive. Tag each surface with its artifact domain in brackets.
  These rows are cited in §5.5 SCOPE COVERAGE RECONCILIATION, §11 FINDING-SURFACE LINKAGE,
  and §19 DOMAIN COVERAGE GAP-CHECK.)
OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]
Scope Amendment Protocol: SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment. No commitment proceeds with open HIGH findings.
  MEDIUM = Conditions commitment. Proceeds only after named resolution.
  LOW    = Advisory. Commitment may proceed.
  These definitions apply universally. They may not be restated at any gate.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose = FAIL  [override: null hypothesis holds]
                OR  exists Gi = FAIL
  CONDITIONAL  <-- no Gi = FAIL  AND  exists Gi = CONDITIONAL
  READY        <-- all Gi = PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst verdict among all G_domain rows. Precedence: FAIL > CONDITIONAL > PASS.
  BRACKET CLOSING applies this formula mechanically.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim receives a CH-ID. Every downstream section carries a CH-ID response table.
  PASS prohibited if any CH-ID shows OPEN status.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section. Assembly: verbatim copy. No re-derivation.
  EXCLUDED (no ledger row): §3.5, §3.8, §5.5, §5.8.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.ROLE MANIFEST | 2.BRACKET OPENING | 3.DOMAIN(s) | 3.5.DOMAIN-AGG CHECKPOINT |
  3.8.CH-ID SATURATION CHECK | 4.LIFECYCLE | 5.BRACKET CLOSING |
  5.5.SCOPE COVERAGE RECONCILIATION | 5.8.DOMAIN COVERAGE GAP-CHECK |
  6.GATE VECTOR TABLE | 7.CROSS-ROLE SIGNALS | 8.DISPOSITION | 9.ACTION ITEM REGISTER.
  Reordering any section violates this contract.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID has DOMAIN response before LIFECYCLE.
  FULLY SATURATED: CH-ID has DOMAIN + LIFECYCLE response before BRACKET CLOSING.
  PASS from BRACKET CLOSING prohibited without full saturation or stated waiver.
  Waiver format: "CH-XXX WAIVER: [reason]"

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = GOpen.
  Stage 2: g_null(post-domain): FAIL->FAIL; CONDITIONAL->max(initial,CONDITIONAL); PASS->initial.
  Stage 3: g_null(final): FAIL->FAIL; CONDITIONAL->max(post-domain,CONDITIONAL); PASS->post-domain.
  GClose must equal g_null(final). Deviation requires: "g_null OVERRIDE: [justification]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps each §1 IN-SCOPE surface to reviewer findings. COVERED / GAP classification.
  GAP -> ADVISORY-GAP in ACTION ITEM REGISTER. Gate signal COVERED/PARTIAL is informational.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE finding carries "[§1:S-n]" citation. No citation = ADVISORY-ORPHAN.
  ADVISORY-ORPHAN items appended to ACTION ITEM REGISTER.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit RESOLUTION REGISTRY after Overall Disposition:
    | Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status=OPEN |
  DISPOSITION!=CONDITIONAL -> "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS must include §13 PROGRESSION LEDGER:
    g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory label
  Labels: MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
          DOMAIN-RECOVERED / LIFECYCLE-RECOVERED. Informational only. No ledger row emitted.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Findings in DOMAIN/LIFECYCLE as table: | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all finding severities). Precedence: HIGH>MEDIUM>LOW.
  No findings: Section Severity = LOW. Do not assign Section Severity editorially.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE section: address ALL entries from the role's lens.verify list.
  LENS COVERAGE TABLE format (extended per §18):
    | # | lens.verify Entry | Applicability | Status | Finding Reference |
  Status: ADDRESSED / OPEN. OPEN obligation rules governed by §18.
  §18 OPEN-LENS registration: HIGH mandatory; MEDIUM unless waived; LOW omitted.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  PRIMARY DRIVER DERIVATION RULE -- apply mechanically at DISPOSITION. Do not assign editorially.
    1. GClose=FAIL -> BRACKET CLOSING      5. GClose=CONDITIONAL -> BRACKET CLOSING
    2. G_domain_agg=FAIL -> DOMAIN         6. G_domain_agg=CONDITIONAL -> DOMAIN
    3. G_lifecycle=FAIL -> LIFECYCLE       7. G_lifecycle=CONDITIONAL -> LIFECYCLE
    4. GOpen=FAIL -> BRACKET OPENING       8. GOpen=CONDITIONAL -> BRACKET OPENING
    9. all PASS -> N/A
  Emit: **Applying §16 rule**: [rule number + why] | **Primary Driver**: [value]

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]      <- NEW (C-35)
  BRACKET OPENING includes a NULL HYPOTHESIS DIMENSION TABLE separate from the alternatives table.
  Format: | Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
  NH Verdict: FAVORS-BUILD (pos Differential) / NEUTRAL (zero) / OPPOSES-BUILD (neg).
  MUST-CLEAR dimensions marked with asterisk (*) in Dimension column.
  g_null derivation rule (pre-committed; apply at BRACKET OPENING and BRACKET CLOSING):
    HOLDS      <-- any MUST-CLEAR row NH Verdict = OPPOSES-BUILD
    CONDITIONAL <-- no MUST-CLEAR OPPOSES-BUILD AND count(OPPOSES-BUILD) >= count(FAVORS-BUILD)
    DEFEATED   <-- no MUST-CLEAR OPPOSES-BUILD AND count(FAVORS-BUILD) > count(OPPOSES-BUILD)
  GOpen = PASS if DEFEATED; CONDITIONAL if CONDITIONAL; FAIL if HOLDS.
  g_null is derivable from the NH Verdict column alone. Prose arguments may add context
  but are not required to verify the g_null value.
  BRACKET CLOSING re-populates the NH dimension table with aggregated domain scores and
  re-applies the §17 derivation rule to produce the revised g_null verdict.

§18 -- LENS APPLICABILITY CONTRACT [IMMUTABLE]                   <- NEW (C-33)
  The LENS COVERAGE TABLE (§15) must include an Applicability column for each lens.verify entry.
  Rate Applicability per artifact under review, not from role definitions.
  The same role may carry different Applicability ratings for different artifact types.

  Applicability values and pre-committed coverage obligation:
    HIGH   = Lens dimension is directly and specifically applicable to this artifact type.
             OPEN at HIGH -> mandatory ADVISORY-OPEN-LENS registration.
    MEDIUM = Lens dimension applies with adaptation to this artifact type.
             OPEN at MEDIUM -> ADVISORY-OPEN-LENS registration unless waived inline:
             "Q-n MEDIUM-WAIVER: [reason this dimension need not be addressed for this artifact]"
    LOW    = Lens dimension is generic and only indirectly applicable to this artifact type.
             OPEN at LOW -> informational note only. No ADVISORY-OPEN-LENS registration.

  Applicability is rated before reviewing findings. The Applicability rating is the
  pre-committed basis for the ADDRESSED/OPEN determination: a HIGH-applicability lens
  must be ADDRESSED; a LOW-applicability lens OPEN requires no remediation for this artifact.

§19 -- DOMAIN COVERAGE GAP-CHECK CONTRACT [IMMUTABLE]            <- NEW (C-34)
  After §5.5 SCOPE COVERAGE RECONCILIATION, §5.8 DOMAIN COVERAGE GAP-CHECK runs.
  §5.8 is excluded from the gate ledger (§6 EXCLUDED list). It produces no gate verdict.

  GAP-CHECK PROCEDURE (apply mechanically using §18 Applicability values and §1 domain tags):
    Step 1: List all distinct artifact domains from the DOMAIN tags in §1 IN-SCOPE surfaces.
    Step 2: For each domain, scan all §15/§18 LENS COVERAGE TABLE rows across all reviewer
            sections. Find the highest Applicability tier any reviewer holds for any lens entry
            associated with that domain.
    Step 3: Classify each domain:
      EXPERT-COVERED  = at least one reviewer has HIGH applicability for a lens entry in this domain.
      PARTIAL-COVERED = no HIGH; at least one MEDIUM-applicability reviewer for this domain.
      UNCOVERED       = no reviewer with HIGH or MEDIUM applicability for any lens entry in this domain.
    Step 4: UNCOVERED domains -> ADVISORY-GAP in ACTION ITEM REGISTER.
            Record: domain name, highest applicability tier found, and gap reason
            (absent role / no lens entries map to domain / all lenses LOW for this domain).
    Step 5: PARTIAL-COVERED domains -> ADVISORY-OBS in ACTION ITEM REGISTER.

  This check is pre-committed. It does not run editorially at review time.
  Distinction from C-31/§15: §15 is role-outward (did each reviewer exhaust their lenses?).
  §19 is domain-inward (does each artifact domain have a HIGH-applicability reviewer?).
  Distinction from C-29/§10: §10 checks whether findings exist for declared surfaces.
  §19 checks whether HIGH-applicability reviewers exist for each artifact domain.
======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. CHALLENGER positions remain fixed.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table** *(>= 3 dimensions; re-scored by domain reviewers)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17 -- g_null derivable from NH Verdict column alone)*:

| Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
|-----------|--------------------------|----------------------------|--------------|------------|
| [DIM-A*]  | [N]                       | [M]                         | [M-N]        | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [N]                       | [M]                         | [M-N]        | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [N]                       | [M]                         | [M-N]        | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

*(Dimensions marked * are MUST-CLEAR. Apply §17 g_null derivation rule.)*

**Applying §17 g_null derivation rule**:
```
MUST-CLEAR rows with OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD) = [N] | count(OPPOSES-BUILD) = [M]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null (from §17 table)**: [HOLDS / CONDITIONAL / DEFEATED]

**Challenge claims** *(assign CH-IDs per §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction.] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger lens.verify.]
**Simplify**: [One from challenger lens.simplify.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL -- consistent with §17 g_null table result]
**GOpen Reason**: [One sentence.]
**g_null(initial)** *(per §9 Stage 1 -- equals GOpen)*: [PASS / CONDITIONAL / FAIL]

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

*(PARTIAL requires a named resolution path. OPEN = claim not addressable from this role's frame.)*

**Domain re-score** *(same dimensions as BRACKET OPENING alternatives table)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| [DIM-1] | [revised] | [revised] | [revised] | [reason] |
| [DIM-2] | [revised] | [revised] | [revised] | |
| [DIM-3] | [revised] | [revised] | [revised] | |

**Additional Findings** *(per §14: per-finding severity table; per §11: each finding cites §1 surface)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1 -- from this role's lens.verify and expertise.depth.] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-3 | [§1:S-n -- optional] | [FINDING_3] | [HIGH / MEDIUM / LOW] |

*(Findings without a valid §1:S-n citation are ADVISORY-ORPHAN per §11.)*

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] -- mechanical result per §14; do not assign editorially.

**Lens Coverage Table** *(per §15 + §18 -- ALL lens.verify entries; rate Applicability per artifact;
tag Domain for §19 gap-check)*:

| # | lens.verify Entry | Domain | Applicability | Status | Finding Reference |
|---|------------------|--------|---------------|--------|-------------------|
| Q-1 | [Full text of lens.verify entry 1] | [domain-label] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text of lens.verify entry 2] | [domain-label] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-3 | [Full text of lens.verify entry 3 if present] | [domain-label] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(Per §18: HIGH OPEN -> mandatory ADVISORY-OPEN-LENS.
MEDIUM OPEN -> ADVISORY-OPEN-LENS unless "Q-n MEDIUM-WAIVER: [reason]" stated here.
LOW OPEN -> informational only; no registration.
Domain column feeds §19 gap-check procedure.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's lens.simplify.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence. If CONDITIONAL: name condition. If FAIL: name gap.]

*(For `--depth deep`: repeat as DOMAIN-2, DOMAIN-3. Each emits own ledger row, domain re-score,
and lens coverage table. G_domain Aggregate = worst of all G_domain rows per §3a.)*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6 -- this section produces no verdict.)*

**Applying §3a formula**:
```
G_domain rows: DOMAIN--[ROLE_NAME]=[verdict] (add rows for depth deep)
G_domain_agg = worst([list]) = [PASS / CONDITIONAL / FAIL]
```
**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

**Applying §9 Stage 2 formula**:
```
g_null(initial)=[copy] | G_domain_agg=[copy]
  FAIL->FAIL | CONDITIONAL->max(initial,CONDITIONAL) | PASS->g_null(initial)
g_null(post-domain) = [FAIL / CONDITIONAL / PASS]
```
**g_null(post-domain)**: [FAIL / CONDITIONAL / PASS]

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger per §6.)*

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | [copy from DOMAIN] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED -- or N/A] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None"]
*LIFECYCLE may proceed. Full saturation check executes at BRACKET CLOSING.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy] | G_domain Aggregate: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table** *(mandatory per §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph referencing GOpen, G_domain Aggregate, and
g_null(post-domain) explicitly.]

**Null hypothesis status**: [yes / partial / no -- reference g_null(post-domain). One sentence.]

**Additional Findings** *(per §14 + §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1 -- commitment, program, or decision concerns.] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

*(Findings without a valid §1:S-n citation are ADVISORY-ORPHAN per §11.)*

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] -- mechanical result per §14; do not assign editorially.

**Lens Coverage Table** *(per §15 + §18 -- include Domain column for §19)*:

| # | lens.verify Entry | Domain | Applicability | Status | Finding Reference |
|---|------------------|--------|---------------|--------|-------------------|
| Q-1 | [Full text of lens.verify entry 1] | [domain-label] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text of lens.verify entry 2] | [domain-label] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(Per §18 obligation rules. Domain column feeds §19.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's lens.simplify.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: scope declaration, all CH-ID tables, all gate verdicts.*

**Applying §9 Stage 3 formula**:
```
g_null(post-domain)=[copy] | G_lifecycle=[copy]
  FAIL->FAIL | CONDITIONAL->max(post-domain,CONDITIONAL) | PASS->g_null(post-domain)
g_null(final) = [FAIL / CONDITIONAL / PASS]
```
**g_null(final)**: [FAIL / CONDITIONAL / PASS]

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(per §17 -- aggregate domain scores; re-derive g_null)*:

| Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
|-----------|--------------------------|----------------------------|--------------|------------|
| [DIM-A*]  | [agg]                     | [agg]                       | [agg diff]   | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [agg]                     | [agg]                       | [agg diff]   | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [agg]                     | [agg]                       | [agg diff]   | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

**Applying §17 rule to revised table**:
```
MUST-CLEAR rows with OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD)=[N] | count(OPPOSES-BUILD)=[M]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```

**Revised alternatives table** *(aggregate domain re-scores)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------|
| [DIM-1] | [agg] | [agg] | [agg] | [reason] |
| [DIM-2] | [agg] | [agg] | [agg] | |
| [DIM-3] | [agg] | [agg] | [agg] | |

**Full CH-ID Saturation Check** *(per §8)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver |
|-------|--------------|-----------------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [All defeated, or list gaps.]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A -- formula applied | or: override justification]

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts per contract §3.

**GClose Rationale**: [2-3 sentences. Reference g_null(final) from §17 revised table derivation,
CH-ID saturation, and null hypothesis trajectory (initial -> post-domain -> final).]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6. Runs after BRACKET CLOSING.)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1 -- domain-label-1] | [ROLE or "none"] | [F-n / etc.] | [COVERED / GAP] |
| [§1 SURFACE_2 -- domain-label-2] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_3 -- domain-label-3] | [ROLE or "none"] | [reference] | [COVERED / GAP] |

**Coverage gate signal** *(§10 -- informational)*: [COVERED / PARTIAL]
**§11 ADVISORY-ORPHAN check**: [findings without §1 citation, or "None"]
**Forced advisory items**: [GAP surfaces and ADVISORY-ORPHAN findings, or "None"]

---

## §5.8 DOMAIN COVERAGE GAP-CHECK

*(EXCLUDED from gate ledger per §6. Runs after §5.5, before GATE VECTOR TABLE.
Applies §19 DOMAIN COVERAGE GAP-CHECK CONTRACT mechanically.)*

**Step 1 -- Artifact domains from §1**:
- [domain-label-1]: surfaces [list §1 surfaces tagged with this domain]
- [domain-label-2]: surfaces [list]
- [domain-label-3]: surfaces [list]

**Step 2 -- Highest applicability per domain (from all §15/§18 lens coverage tables)**:

| Artifact Domain | Reviewer Role(s) | Highest Applicability | Lens Entry Reference |
|----------------|-----------------|----------------------|---------------------|
| [domain-label-1] | [ROLE_NAME] | [HIGH / MEDIUM / LOW / NONE] | [Q-n from DOMAIN or LIFECYCLE table] |
| [domain-label-2] | [ROLE_NAME] | [HIGH / MEDIUM / LOW / NONE] | [Q-n or "none"] |
| [domain-label-3] | [ROLE_NAME] | [HIGH / MEDIUM / LOW / NONE] | [Q-n or "none"] |

**Step 3 -- Domain classification** *(per §19 procedure)*:

| Artifact Domain | Classification | Reason |
|----------------|----------------|--------|
| [domain-label-1] | [EXPERT-COVERED / PARTIAL-COVERED / UNCOVERED] | [highest tier + why] |
| [domain-label-2] | [EXPERT-COVERED / PARTIAL-COVERED / UNCOVERED] | |
| [domain-label-3] | [EXPERT-COVERED / PARTIAL-COVERED / UNCOVERED] | |

**Step 4 -- ADVISORY-GAP items** *(UNCOVERED domains per §19 Step 4)*:
- [domain-X]: UNCOVERED -- [reason]. -> ADVISORY-GAP in ACTION ITEM REGISTER.
*(Write "None" if all domains EXPERT-COVERED or PARTIAL-COVERED.)*

**Step 5 -- ADVISORY-OBS items** *(PARTIAL-COVERED domains per §19 Step 5)*:
- [domain-Y]: PARTIAL-COVERED -- highest tier: MEDIUM. -> ADVISORY-OBS in ACTION ITEM REGISTER.
*(Write "None" if no PARTIAL-COVERED domains.)*

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen -- bracket opening | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain -- domain aggregate | [DOMAIN_ROLE(S)] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle -- lifecycle | [LIFECYCLE_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose -- bracket closing | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Two reviewers with incompatible CH-ID responses or findings. If none: "None detected."]

**Convergence**: [CH-ID or concern named by 2+ reviewers. Name it and explain confidence.]

**§13 Progression Ledger** *(per §13 -- informational; no ledger row emitted)*:
```
g_null(initial)     = [copy from BRACKET OPENING]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING]
Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED /
                     LIFECYCLE-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

**Scope coverage** *(§10 gate signal)*: [COVERED / PARTIAL]
**Domain coverage** *(§19)*: [EXPERT-COVERED for all / [N] UNCOVERED / [M] PARTIAL-COVERED]

---

## DISPOSITION

**Gate vector**:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply §3 formula** *(do not alter; do not reason editorially)*:
```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose=FAIL? -> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi=FAIL? -> BLOCKED
No FAIL, any CONDITIONAL? -> CONDITIONAL
All PASS? -> READY
```

**Null hypothesis progression** *(§9 -- from §13 ledger)*:
- g_null(initial)=[copy] | g_null(post-domain)=[copy] | g_null(final)=[copy]
- Trajectory: [from §13 PROGRESSION LEDGER]

**Scope coverage** *(§10 -- informational)*: [COVERED / PARTIAL]
**Domain coverage** *(§19)*: [summary: all EXPERT-COVERED / N UNCOVERED (ADVISORY-GAP) / M PARTIAL-COVERED (ADVISORY-OBS)]

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**RESOLUTION REGISTRY** *(per §12 -- emit if CONDITIONAL; otherwise write N/A line)*:

| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [verbatim condition] | [ROLE_NAME] | [falsifiable criterion] | OPEN |

*RESOLUTION REGISTRY: N/A -- disposition is [READY/BLOCKED]* <- delete this line if CONDITIONAL

**Applying §16 PRIMARY DRIVER DERIVATION RULE**:
```
GClose=[_], G_domain_agg=[_], G_lifecycle=[_], GOpen=[_]
Rule fired: [state rule number 1-9 from §16 and why it fires before others]
```
**Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**Conditions** *(if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]
2. [Additional conditions if present.]

**Blocker** *(if BLOCKED)*: [Specific finding from the FAIL gate. If GClose=FAIL, lead with:
"Challenger final verdict HOLDS -- [GClose Rationale summary]."]

---

## ACTION ITEM REGISTER

*Copy all Local Gate Ledger rows from BRACKET OPENING, DOMAIN(s), LIFECYCLE, and BRACKET CLOSING
verbatim. Do not re-derive Gate Verdict or Class. Append in order:*
*CH-ID PARTIAL/HOLDS rows | §8 waiver rows (ADVISORY) | §10 ADVISORY-GAP from §5.5 |*
*§11 ADVISORY-ORPHAN from §5.5 | §15/§18 ADVISORY-OPEN-LENS rows |*
*§19 ADVISORY-GAP from §5.8 (UNCOVERED domains) | §19 ADVISORY-OBS from §5.8 (PARTIAL-COVERED).*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [copy from local ledger] | [copy] | [copy] | [copy] | [What must be done] | [ROLE_NAME] | [Criterion] |
| CH-001 | -- | -- | [BLOCKED/CONDITIONAL/ADVISORY] | [Item] | [ROLE_NAME] | [Criterion] |
| §8 WAIVER | -- | -- | ADVISORY | [Waiver text if any] | [ROLE_NAME] | N/A |
| §10 SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [Surface not addressed] | [ROLE_NAME] | [Criterion] |
| §11 FINDING-SURFACE LINKAGE | -- | -- | ADVISORY-ORPHAN | [Finding with no §1 citation] | [ROLE_NAME] | [Criterion] |
| §15/§18 LENS EXHAUSTION | -- | -- | ADVISORY-OPEN-LENS | [Q-n: HIGH/MEDIUM: entry text] | [ROLE_NAME] | [Criterion] |
| §19 DOMAIN COVERAGE GAP-CHECK | -- | -- | ADVISORY-GAP | [domain: UNCOVERED -- reason] | [ROLE_NAME] | Add reviewer with HIGH applicability to [domain] |
| §19 DOMAIN COVERAGE GAP-CHECK | -- | -- | ADVISORY-OBS | [domain: PARTIAL-COVERED -- highest tier] | [ROLE_NAME] | [Criterion] |
| -- | -- | -- | ADVISORY-OBS | [Advisory observation not sourced from CH-ID or gate] | [ROLE_NAME] | [Criterion] |

*FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY*
*ADVISORY-GAP: §10 scope, §19 domain | ADVISORY-ORPHAN: §11 | ADVISORY-OPEN-LENS: §15/§18*
*ADVISORY-OPEN-LENS: HIGH mandatory; MEDIUM unless waived; LOW omitted*

---

**Artifact to review:**

{{artifact}}
```

---

## Round 13 Variation Summary

| Variation | New Axes | New Contracts | C-35 | C-33 | C-34 | Predicted Score |
|-----------|----------|---------------|------|------|------|-----------------|
| V-01 | NH Dimension Table | §17 | PASS | FAIL | vac | 215/225 |
| V-02 | Lens Applicability | §17 | FAIL | PASS | FAIL | 215/225 |
| V-03 | Domain Coverage Gap-Check | §17+§18 | FAIL | PASS | PASS | 220/225 |
| V-04 | V-01 + V-02 | §17+§18 | PASS | PASS | FAIL | 220/225 |
| V-05 | V-01 + V-02 + V-03 | §17+§18+§19 | PASS | PASS | PASS | **225/225** |

Notes:
- All variants inherit V-05 R11 base (C-30+C-31+C-32 PASS = 210/225 baseline).
- V-01: adds C-35 only (+5). C-33 FAIL (no applicability ratings) -> C-34 vacuous.
- V-02: adds C-33 only (+5). C-35 FAIL (no NH dimension table). C-34: C-31 active but
  C-33 applicability ratings exist yet no domain gap-check -> FAIL.
- V-03: adds C-33+C-34 together (+10). C-35 FAIL (no NH dimension table).
- V-04: adds C-35+C-33 (+10). C-34: applicability ratings exist, no gap-check -> FAIL.
- V-05: adds all three (+15). If all three PASS, achieves 225/225 perfect score.
- C-34 vacuous condition: C-31 inactive OR no multi-domain artifact. V-03/V-05 activate
  C-31 (§15 active) and have multi-domain §1 tagging -> C-34 active, not vacuous.
