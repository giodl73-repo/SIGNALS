# org-review Variations -- Round 14 (v12 rubric, 2026-03-16)
Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v12-2026-03-16.md

Prior round summary:
- R13: V-05 R13 scores 230/240 under v12. Passes C-33+C-34+C-35+C-36+C-37 on top of the
  C-01 through C-32 base. §17 = NULL HYPOTHESIS DIMENSION TABLE (two-column format:
  Current-State / Proposed-State), §18 = LENS APPLICABILITY CONTRACT, §19 = DOMAIN
  COVERAGE GAP-CHECK CONTRACT. §1 IN-SCOPE rows carry [DOMAIN: label] annotations.
- Gap to 240: C-38 (+5) and C-23 (+5). C-38 requires the NH Dimension Table to have three
  columns (Status-Quo / Proposed-Build / Best-Non-Build-Alt) making both pairwise
  differentials D1=(B-A) and D2=(B-C) table-derivable. C-23 requires the NULL HYPOTHESIS
  DERIVATION RULE to cover BOTH D1 and D2 explicitly. In R13, the NH table was two-column
  so D2 was not table-derivable, causing the C-23/C-38 mutual exclusion.

Round 14 strategy:
- Baseline: V-05 R13 (§1-§19, C-33+C-34+C-35+C-36+C-37 PASS) as non-negotiable base.
  All R14 variants inherit §1-§19 and score >=230 from base inheritance.
- V-01: single axis -- three-column NH Dimension Table (Status-Quo/Proposed-Build/
  Best-Non-Build-Alt) with D1 and D2 as explicit computed columns. Targets C-38; C-23
  co-activated because derivation rule must reference both D1 and D2.
- V-02: single axis -- two-differential derivation rule without three-column table. D1
  from NH Dimension Table; D2 from alternatives comparison table column values. C-23
  targeted; C-38 FAIL (table two-column); tests whether C-23 is independently satisfiable.
- V-03: single axis -- inertia-first phrasing register. Null hypothesis framed as primary
  authority. Challenger instructions rewritten as "owner of the decision". No structural
  contract changes; tests quality signal without rubric-score impact.
- V-04: combination -- V-01 + V-02 axes. Three-column table + two-differential rule
  using D1 and D2 from the same table. Primary C-38+C-23 candidate targeting 240/240.
- V-05: full integration -- V-01 + V-02 + V-03 + explicit NH TABLE AGGREGATION RULE
  pre-committed in §17 (how BRACKET CLOSING computes aggregated A, B, C column values).
  All 240 points structurally required.

---

## V-01 -- Single Axis: Three-Column NH Dimension Table (C-38)

**Variation axis**: §17 NH DIMENSION TABLE structure. Replace two columns (Current-State /
Proposed-State) with three columns (Status-Quo / Proposed-Build / Best-Non-Build-Alt),
producing two explicit differentials D1=(B-A) and D2=(B-C) both derivable from table
column values alone.

**Hypothesis**: The C-23/C-38 mutual exclusion in R13 arose because the NH Dimension
Table's two-column format produced only D1. Once §17 adds a third column C (Best-Non-Build-
Alt Score), D2=(B-C) is table-derivable without referencing the alternatives comparison table.
The derivation rule then references both D1 and D2 from the same table, satisfying C-38
(three columns, both differentials table-derivable) and C-23 (both pairwise differentials
named in the pre-committed formula) simultaneously. Only §17, the BRACKET OPENING NH table
template, and the BRACKET CLOSING revised NH table template change. Everything else inherits
V-05 R13 unchanged.

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

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. Do not add sections
between pre-printed headers. If a field cannot be filled, write `[N/A -- reason]`.

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
  (Add rows. Each row MUST carry a [DOMAIN: label] annotation. Labels feed §19 gap-check.
  These rows are cited in §5.5 SCOPE COVERAGE RECONCILIATION and §11 FINDING-SURFACE LINKAGE.)

OUT-OF-SCOPE -- surfaces this review will not evaluate:
  1. [SURFACE -- REASON_EXCLUDED]
  (Write "None" if nothing is excluded.)

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] [DOMAIN: label] added to IN-SCOPE -- [reason]
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

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN and LIFECYCLE section must address ALL entries from the role's lens.verify list.
  After the findings table, emit a LENS COVERAGE TABLE (extended per §18):
    | # | lens.verify Entry | Applicability | Status | Finding Reference |
  Status values: ADDRESSED / OPEN.
  OPEN coverage obligation determined by §18 Applicability tier rules.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  PRIMARY DRIVER DERIVATION RULE (apply mechanically at DISPOSITION time):
    1. if GClose = FAIL:                Primary Driver = BRACKET CLOSING
    2. elif G_domain_agg = FAIL:        Primary Driver = DOMAIN
    3. elif G_lifecycle = FAIL:         Primary Driver = LIFECYCLE
    4. elif GOpen = FAIL:               Primary Driver = BRACKET OPENING
    5. elif GClose = CONDITIONAL:       Primary Driver = BRACKET CLOSING
    6. elif G_domain_agg = CONDITIONAL: Primary Driver = DOMAIN
    7. elif G_lifecycle = CONDITIONAL:  Primary Driver = LIFECYCLE
    8. elif GOpen = CONDITIONAL:        Primary Driver = BRACKET OPENING
    9. else (all PASS):                 Primary Driver = N/A
  Emit at DISPOSITION:
    **Applying §16 rule**: [rule number fired and why]
    **Primary Driver**: [value]

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]     <- REVISED IN V-01 R14
  The BRACKET OPENING challenger evaluates the null hypothesis using a dedicated per-dimension
  comparison table with THREE comparison columns. This table is SEPARATE from and appears
  after the alternatives comparison table.

  Table format:
    | Dimension | Status-Quo Score (A) | Proposed-Build Score (B) | Best-Non-Build-Alt Score (C) | D1=(B-A) | D2=(B-C) | NH Verdict |

  All scores on a 0-10 scale. D1 and D2 are arithmetic differences computed from column values.

  NH Verdict (derived mechanically from D1 and D2 -- no editorial assignment permitted):
    FAVORS-BUILD:  D1 > 0 AND D2 > 0
    PARTIAL-D1:    D1 > 0 AND D2 <= 0
    PARTIAL-D2:    D1 <= 0 AND D2 > 0
    NEUTRAL:       D1 = 0 AND D2 = 0
    OPPOSES-BUILD: D1 < 0 OR D2 < 0

  MUST-CLEAR dimensions: mark with asterisk (*) in the Dimension column.

  NULL HYPOTHESIS DERIVATION RULE (pre-committed; BOTH D1 AND D2 required for DEFEATED):
    HOLDS       <-- any MUST-CLEAR row has NH Verdict != FAVORS-BUILD
    CONDITIONAL <-- no MUST-CLEAR violation AND count(PARTIAL-D1 + PARTIAL-D2) > 0
    DEFEATED    <-- no MUST-CLEAR violation
                    AND count(OPPOSES-BUILD + PARTIAL-D1 + PARTIAL-D2) = 0
                    AND count(FAVORS-BUILD) > 0

  g_null: DEFEATED->PASS | CONDITIONAL->CONDITIONAL | HOLDS->FAIL

  A scorer verifying g_null reads only the D1, D2, and NH Verdict columns. Both D1 and D2 are
  table-derivable from column A, B, C values without reading prose.

  BRACKET CLOSING re-populates this THREE-COLUMN table with aggregated domain scores (per §9
  Stage 3). The revised table's NH Verdict column re-derives g_null(final). §9 Stage 3 formula
  and revised table result must agree; if they disagree:
  "NH TABLE CONFLICT: table=[result] vs §9=[result] -- [resolution]"

§18 -- LENS APPLICABILITY CONTRACT [IMMUTABLE]
  The LENS COVERAGE TABLE (§15) includes an Applicability column. Rating is artifact-specific.

  Applicability values: HIGH / MEDIUM / LOW

  Pre-committed coverage obligation rules:
    HIGH   = Directly and specifically applicable to this artifact type.
             OPEN at HIGH -> mandatory ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.
    MEDIUM = Applies with adaptation.
             OPEN at MEDIUM -> ADVISORY-OPEN-LENS unless: "Q-n MEDIUM-WAIVER: [reason]"
    LOW    = Generic and only indirectly applicable.
             OPEN at LOW -> informational note only. No ADVISORY-OPEN-LENS registration.

§19 -- DOMAIN COVERAGE GAP-CHECK CONTRACT [IMMUTABLE]
  After all Lens Coverage Tables are populated, a dedicated gap-check step executes:
    1. Collect all [DOMAIN: label] values from §1 IN-SCOPE rows.
    2. For each domain label, find the highest Applicability tier any reviewer holds for it.
    3. COVERED = at least one reviewer has HIGH applicability. UNCOVERED = none does.
    4. UNCOVERED domains -> ADVISORY-GAP in ACTION ITEM REGISTER:
       "Domain [label]: no HIGH-applicability reviewer -- highest tier found: [value]"
  Gap-check emits no ledger row. Result is informational.
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

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3. CHALLENGER positions remain fixed.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table** *(>= 3 dimensions; re-scored by domain reviewers)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|----------------|-----------|------------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17 V-01 R14 -- THREE columns; D1 and D2 table-derivable)*:

| Dimension | Status-Quo Score (A) | Proposed-Build Score (B) | Best-Non-Build-Alt Score (C) | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----------|---------------------|--------------------------|------------------------------|----------|----------|------------|
| [DIM-A*] | [N] | [M] | [P] | [M-N] | [M-P] | [FAVORS-BUILD / PARTIAL-D1 / PARTIAL-D2 / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*] | [N] | [M] | [P] | [M-N] | [M-P] | [NH Verdict] |
| [DIM-C]  | [N] | [M] | [P] | [M-N] | [M-P] | [NH Verdict] |

*(Dimensions marked * are MUST-CLEAR. NH Verdict assigned mechanically from D1 and D2 per §17.)*

**Applying §17 DEFEATED/CONDITIONAL/HOLDS rule**:
```
MUST-CLEAR violations (NH Verdict != FAVORS-BUILD on * rows): [list or "none"]
count(FAVORS-BUILD)=[N] | count(OPPOSES-BUILD+PARTIAL-D1+PARTIAL-D2)=[M]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null(initial)** *(from §17 table; equals GOpen per §9 Stage 1)*:
  [DEFEATED->PASS | CONDITIONAL->CONDITIONAL | HOLDS->FAIL]

**Challenge claims** *(assign CH-IDs per §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction.] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL -- consistent with §17 g_null table result]
**GOpen Reason**: [One sentence.]

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
|-------|------------------------|--------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

*(PARTIAL requires a named resolution path. OPEN = claim not addressable from this role's frame.)*

**Domain re-score** *(re-score all three columns from this role's frame)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|----------------|-----------|------------------------|-----------|
| [DIM-1] | [revised A] | [revised B] | [revised C] | [reason] |
| [DIM-2] | [revised A] | [revised B] | [revised C] | |
| [DIM-3] | [revised A] | [revised B] | [revised C] | |

*(All three columns re-scored independently. BRACKET CLOSING aggregates B and C columns.)*

**Additional Findings** *(per §14 + §11)*:

| # | §1 Surface | Finding | Severity |
|---|------------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1 -- from this role's `lens.verify` and `expertise.depth`.] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-3 | [§1:S-n -- optional] | [FINDING_3] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] -- mechanical; do not assign editorially.

**Lens Coverage Table** *(per §15 + §18 -- rate Applicability per artifact before reviewing)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|-------------------|---------------|--------|-------------------|
| Q-1 | [Full text of lens.verify entry 1] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text of lens.verify entry 2] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-3 | [Full text if present] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(Per §18: HIGH OPEN -> mandatory ADVISORY-OPEN-LENS. MEDIUM OPEN -> ADVISORY-OPEN-LENS unless
"Q-n MEDIUM-WAIVER: [reason]". LOW OPEN -> informational only.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*(For `--depth deep`: repeat as DOMAIN-2, DOMAIN-3. Each emits own local ledger row and
lens coverage table. G_domain_agg = worst of all G_domain rows per §3a.)*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6.)*

**Applying §3a formula**:
```
G_domain rows: DOMAIN -- [ROLE_NAME]: [verdict]
G_domain_agg = worst([list]) = [PASS / CONDITIONAL / FAIL]
```
**Applying §9 Stage 2**:
```
g_null(initial)=[copy] | G_domain_agg=[copy]
  FAIL->FAIL | CONDITIONAL->max(initial,CONDITIONAL) | PASS->initial
g_null(post-domain) = [verdict]
```
**G_domain Aggregate**: [verdict] | **g_null(post-domain)**: [verdict]

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

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy] | G_domain Aggregate: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|------------------------|---------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph referencing GOpen, G_domain Aggregate,
and g_null(post-domain) explicitly.]

**Null hypothesis status**: [yes / partial / no -- reference g_null(post-domain). One sentence.]

**Additional Findings** *(per §14 + §11)*:

| # | §1 Surface | Finding | Severity |
|---|------------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1 -- commitment or program concerns.] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] -- mechanical per §14.

**Lens Coverage Table** *(per §15 + §18)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|-------------------|---------------|--------|-------------------|
| Q-1 | [Full text] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |

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

**Applying §9 Stage 3**:
```
g_null(post-domain)=[copy] + G_lifecycle=[copy]
  FAIL->FAIL | CONDITIONAL->max(post-domain,CONDITIONAL) | PASS->post-domain
g_null(final) = [verdict]
```
**g_null(final)**: [verdict]
*GClose must equal g_null(final) per §9.*

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(per §17 V-01 R14 -- THREE columns re-populated
with aggregated domain scores; g_null re-derived from NH Verdict column)*:

| Dimension | Status-Quo Score (A) | Proposed-Build Score (B) | Best-Non-Build-Alt Score (C) | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----------|---------------------|--------------------------|------------------------------|----------|----------|------------|
| [DIM-A*] | [challenger A] | [avg domain B] | [avg domain C] | [D1] | [D2] | [NH Verdict] |
| [DIM-B*] | [challenger A] | [avg domain B] | [avg domain C] | [D1] | [D2] | [NH Verdict] |
| [DIM-C]  | [challenger A] | [avg domain B] | [avg domain C] | [D1] | [D2] | [NH Verdict] |

*(Column A = challenger's original opening scores -- unchanged. Column B = average of all
domain reviewer Build scores. Column C = average of all domain reviewer Best-Non-Build-Alt
scores. D1 and D2 re-computed from aggregated values. NH Verdict assigned mechanically.)*

**Applying §17 rule to revised table**:
```
MUST-CLEAR violations: [list or "none"]
count(FAVORS-BUILD)=[N] | count(OPPOSES+PARTIAL-D1+PARTIAL-D2)=[M]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null from revised table**: [verdict]

*(Conflict check: §9 Stage 3 result=[copy] vs table result=[above].
[MATCH | NH TABLE CONFLICT: [resolution]])*

**Revised alternatives table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Domain Agg Rationale |
|-----------|----------------|-----------|------------------------|----------------------|
| [DIM-1] | [agg] | [agg] | [agg] | |
| [DIM-2] | [agg] | [agg] | [agg] | |
| [DIM-3] | [agg] | [agg] | [agg] | |

**Full CH-ID Saturation Check** *(per §8)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver |
|-------|---------------|-----------------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |

**CH-ID Final Assessment**:

| CH-ID | G_domain | G_lifecycle | Final Status | Notes |
|-------|----------|-------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |

**Remaining gaps**: [All defeated, or list.]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A -- formula applied | or: override justification]
**GClose override authority**: GClose = FAIL overrides all prior gate verdicts per §3.
**GClose Rationale**: [2-3 sentences referencing g_null from §17 revised three-column table,
CH-ID saturation, and null hypothesis trajectory initial->post-domain->final.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN COVERAGE GAP-CHECK *(per §19)*

*(EXCLUDED from gate ledger. Runs after all Lens Coverage Tables, before DISPOSITION.)*

| §1 Domain Label | Highest Reviewer Applicability | Coverage |
|-----------------|-------------------------------|----------|
| [domain-label-1] | [HIGH / MEDIUM / LOW / none] | [COVERED / UNCOVERED] |
| [domain-label-2] | [HIGH / MEDIUM / LOW / none] | [COVERED / UNCOVERED] |
| [domain-label-3] | [HIGH / MEDIUM / LOW / none] | [COVERED / UNCOVERED] |

**UNCOVERED domains -> ADVISORY-GAP in ACTION ITEM REGISTER**:
- [Domain: no HIGH-applicability reviewer -- highest found: [tier]]
- (or "None")

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
**Forced advisory items**: [GAP and ADVISORY-ORPHAN for ACTION ITEM REGISTER, or "None"]

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

**Conflicts**: [Incompatible findings, or "None detected."]
**Convergence**: [CH-ID or concern named by 2+ reviewers.]

**§13 Progression Ledger**:
```
g_null(initial)=[copy] | g_null(post-domain)=[copy] | g_null(final)=[copy]
Trajectory: [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
             DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

**Scope coverage** *(§10)*: [COVERED / PARTIAL]

---

## DISPOSITION

**Gate vector**: GOpen=[copy] | G_domain_agg=[copy] | G_lifecycle=[copy] | GClose=[copy]

**Apply §3 formula**:
```
GClose=FAIL?->BLOCKED | Any Gi=FAIL?->BLOCKED | Any CONDITIONAL?->CONDITIONAL | All PASS?->READY
```

**Null hypothesis progression**: g_null(initial)=[copy] -> [copy] -> [copy] | Trajectory=[copy]
**Scope coverage** *(§10)*: [COVERED / PARTIAL]
**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**RESOLUTION REGISTRY** *(per §12)*:
| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|-------------------|-----------------|---------------------|--------|
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

*Copy all Local Gate Ledger rows from BRACKET OPENING, DOMAIN(s), LIFECYCLE, and BRACKET
CLOSING verbatim. Do not re-derive Gate Verdict or Class. Append: CH-ID PARTIAL/HOLDS rows,
§8 waiver rows (ADVISORY), §10 ADVISORY-GAP rows, §11 ADVISORY-ORPHAN rows, §15/§18
ADVISORY-OPEN-LENS rows (HIGH mandatory; MEDIUM unless waived; LOW omitted), §19 domain
ADVISORY-GAP rows.*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [local ledger copy] | [copy] | [copy] | [copy] | [action] | [ROLE] | [criterion] |
| §10 SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [surface not addressed] | [ROLE] | [criterion] |
| §11 FINDING-SURFACE LINKAGE | -- | -- | ADVISORY-ORPHAN | [finding without §1 cite] | [ROLE] | [criterion] |
| §15/§18 LENS EXHAUSTION | -- | -- | ADVISORY-OPEN-LENS | [Q-n: applicability: entry] | [ROLE] | [criterion] |
| §19 DOMAIN COVERAGE | -- | -- | ADVISORY-GAP | [domain: no HIGH reviewer] | [ROLE] | [criterion] |

*FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY*
*ADVISORY-OPEN-LENS: HIGH mandatory; MEDIUM unless waived; LOW omitted*

---

**Artifact to review:**

{{artifact}}

---

## V-02 -- Single Axis: Two-Differential Derivation Rule Without Three-Column Table (C-23)

**Variation axis**: NULL HYPOTHESIS DERIVATION RULE coverage. Extend the rule to cover
BOTH pairwise differentials while keeping the NH Dimension Table in two-column format
(Current-State / Proposed-State). D1 comes from the NH Dimension Table (Proposed-State
minus Current-State). D2 is computed from the alternatives comparison table (average of
Build column B minus Best-Non-Build-Alt column C across dimensions) and stated as a
labeled scalar before the derivation rule fires.

**Hypothesis**: C-23 requires the derivation rule to "name all relevant pairwise differentials
and map them to a single verdict." It does not explicitly require both differentials to come
from the NH Dimension Table -- C-38 adds that "table-derivable" requirement independently.
If D2 is computed from the alternatives table and injected as a named scalar, the derivation
rule covers both differentials and C-23 may PASS while C-38 FAIL (table is two-column, D2
not derivable from NH table alone). This variation isolates C-23 to test whether the criteria
are independently satisfiable or whether C-38 is a necessary precondition for C-23 PASS.
Expected finding: C-23 PARTIAL because C-38's "table-derivable" qualifier implies the scorer
must verify both differentials from the NH table without cross-referencing another table.

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

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. Do not add sections
between pre-printed headers. If a field cannot be filled, write `[N/A -- reason]`.

---

*(§1 through §16 identical to V-01 R14. Only §17 changes.)*

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§19;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE:
  1. [SURFACE_1]  [DOMAIN: domain-label-1]
  2. [SURFACE_2]  [DOMAIN: domain-label-2]
  3. [SURFACE_3]  [DOMAIN: domain-label-3]
OUT-OF-SCOPE: 1. [SURFACE -- REASON]
Scope Amendment: SCOPE AMENDMENT: [surface] [DOMAIN: label] added -- [reason]
§1 COMPLETE.

§2 SEVERITY [IMMUTABLE]: HIGH=Blocks. MEDIUM=Conditions. LOW=Advisory.
§3 DISPOSITION ALGEBRA [IMMUTABLE]: BLOCKED<--GClose=FAIL OR any FAIL. CONDITIONAL<--no FAIL AND any CONDITIONAL. READY<--all PASS.
§3a DOMAIN-AGGREGATE [IMMUTABLE]: G_domain_agg=worst(all G_domain). BRACKET CLOSING applies.
§4 CONTRACT CITE [IMMUTABLE]: Each reviewer section opens "Contract: DISPOSITION_CONTRACT v1"
§5 CH-ID TRACING [IMMUTABLE]: CH-IDs per challenge claim. CH-ID response table in every section. PASS prohibited if any OPEN.
§6 LOCAL GATE LEDGER [IMMUTABLE]: Row: |Section|Gate|Verdict|Class|. Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY. Verbatim copy. No re-derivation. EXCLUDED: §3.5,§3.8,§5.5.
§7 SECTION ORDER [IMMUTABLE]: 1.ROLE MANIFEST|2.BRACKET OPENING|3.DOMAIN(s)|3.5.DOMAIN-AGG|3.8.CH-ID SATURATION|4.LIFECYCLE|5.BRACKET CLOSING|5.5.SCOPE RECONCILIATION|6.GATE VECTOR|7.CROSS-ROLE|8.DISPOSITION|9.ACTION REGISTER. Reordering violates.
§8 CH-ID SATURATION [IMMUTABLE]: SATURATED=DOMAIN before LIFECYCLE. FULLY SATURATED=DOMAIN+LIFECYCLE before BRACKET CLOSING. PASS prohibited without full saturation or waiver.
§9 NULL HYPOTHESIS PROGRESSION [IMMUTABLE]: Stage1:g_null(initial)=GOpen. Stage2:FAIL->FAIL;CONDITIONAL->max(initial,CONDITIONAL);PASS->initial. Stage3:FAIL->FAIL;CONDITIONAL->max(post-domain,CONDITIONAL);PASS->post-domain. GClose=g_null(final) or "g_null OVERRIDE:[reason]"
§10 SCOPE COVERAGE [IMMUTABLE]: §5.5 maps §1 surfaces. GAP->ADVISORY-GAP. Informational.
§11 FINDING-SURFACE [IMMUTABLE]: Each finding carries "[§1:S-n]". No cite=ADVISORY-ORPHAN.
§12 CONDITIONAL REGISTRY [IMMUTABLE]: DISPOSITION=CONDITIONAL->RESOLUTION REGISTRY after Disposition.
§13 g_null LEDGER [IMMUTABLE]: CROSS-ROLE SIGNALS §13: g_null(initial)|g_null(post-domain)|g_null(final)|Trajectory. Informational.
§14 SEVERITY AGGREGATION [IMMUTABLE]: Findings: |#|§1 Surface|Finding|Severity|. Section Severity=worst(individual). No findings=LOW.
§15 LENS EXHAUSTION [IMMUTABLE]: ALL lens.verify entries. LENS COVERAGE TABLE: |#|Entry|Applicability|Status|Finding Reference|. Per §18 obligation rules.
§16 PRIMARY DRIVER [IMMUTABLE]: 1.GClose=FAIL->BRACKET CLOSING|2.G_domain_agg=FAIL->DOMAIN|3.G_lifecycle=FAIL->LIFECYCLE|4.GOpen=FAIL->BRACKET OPENING|5.GClose=CONDITIONAL->BRACKET CLOSING|6.G_domain_agg=CONDITIONAL->DOMAIN|7.G_lifecycle=CONDITIONAL->LIFECYCLE|8.GOpen=CONDITIONAL->BRACKET OPENING|9.all PASS->N/A.

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]     <- REVISED IN V-02 R14
  Two-column format (Current-State / Proposed-State) with TWO-DIFFERENTIAL derivation rule.

  Table format:
    | Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | D1=(Proposed-Current) | NH Verdict |

  NH Verdict: FAVORS-BUILD (D1>0) / NEUTRAL (D1=0) / OPPOSES-BUILD (D1<0). Based on D1 only.

  D2 COMPUTATION (from alternatives comparison table -- stated as labeled scalar before rule fires):
    D2_net = average(Build column B score minus Best-Non-Build-Alt column C score) across dims.
    Compute at BRACKET OPENING from the alternatives comparison table columns B and C.
    State as: "D2_net (Build vs Best-Non-Build-Alt, from alternatives table) = [value]"

  MUST-CLEAR dimensions: marked with asterisk (*).

  NULL HYPOTHESIS DERIVATION RULE (pre-committed; covers BOTH D1 and D2 differentials):
    D1 differential: from NH Dimension Table (D1_net = sum of D1 column / count).
    D2 differential: from alternatives table (D2_net computed above).

    HOLDS       <-- any MUST-CLEAR has NH Verdict = OPPOSES-BUILD (D1<=0 on must-clear dim)
                     OR D2_net <= 0 (Build does not beat Best-Non-Build-Alt on balance)
    CONDITIONAL <-- no MUST-CLEAR D1 violation AND D2_net <= 0 AND D1_net > 0
                     (Build beats Status-Quo but not Best-Non-Build-Alt on balance)
                    OR no violations AND D1_net = 0
    DEFEATED    <-- no MUST-CLEAR violation AND D1_net > 0 AND D2_net > 0

  g_null: DEFEATED->PASS | CONDITIONAL->CONDITIONAL | HOLDS->FAIL

  A scorer verifying g_null must read: (1) NH Verdict column for D1, and (2) the stated
  D2_net scalar computed from the alternatives table. D2 is NOT derivable from the NH
  Dimension Table alone -- it requires the alternatives comparison table column values.

  BRACKET CLOSING re-applies this two-differential rule to revised domain-aggregated scores.
  Revised D1_net from revised NH Dimension Table. Revised D2_net from revised alternatives table
  (average of revised domain Build B minus revised Best-Non-Build-Alt C across dimensions).

§18 -- LENS APPLICABILITY [IMMUTABLE]: Applicability column in LENS COVERAGE TABLE: HIGH/MEDIUM/LOW, artifact-specific. HIGH OPEN->mandatory ADVISORY-OPEN-LENS. MEDIUM OPEN->ADVISORY-OPEN-LENS unless "Q-n MEDIUM-WAIVER:[reason]". LOW OPEN->informational only.

§19 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]: After all Lens Coverage Tables: collect §1 [DOMAIN:] values, highest Applicability per domain, COVERED(>=1 HIGH)/UNCOVERED(none). UNCOVERED->ADVISORY-GAP. Emits no ledger row.
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

**Null hypothesis**: [One sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|----------------|-----------|------------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**D2 computation from alternatives table** *(per §17 V-02 -- before derivation rule fires)*:
```
D2_net = average(B column - C column) across dimensions:
  DIM-1: B=[_] - C=[_] = [_]
  DIM-2: B=[_] - C=[_] = [_]
  DIM-3: B=[_] - C=[_] = [_]
  D2_net = [value]
```
**D2_net (Build vs Best-Non-Build-Alt)**: [value -- positive = Build beats best non-build alt]

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17 V-02 -- two-column; D1 from table, D2 from above)*:

| Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | D1=(Proposed-Current) | NH Verdict |
|-----------|---------------------------|----------------------------|----------------------|------------|
| [DIM-A*]  | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*]  | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]   | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

**Applying §17 two-differential rule**:
```
D1_net = average(D1 column) = [value]
D2_net = [copy from D2 computation above]
MUST-CLEAR violations (OPPOSES-BUILD on * rows): [list or "none"]
D2_net <= 0? [YES/NO]
Rule: MUST-CLEAR violation OR D2_net<=0 -> HOLDS | D1_net>0 AND D2_net>0 -> DEFEATED | else CONDITIONAL
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null(initial)**: [verdict]

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
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

*(DOMAIN, §3.5, §3.8, LIFECYCLE sections identical in structure to V-01 R14.)*

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Applying §9 Stage 3**:
```
g_null(post-domain)=[copy] + G_lifecycle=[copy] -> g_null(final): [verdict]
```

**Revised D2_net from revised alternatives table**:
```
Revised D2_net = average(revised domain B - revised domain C) across dimensions:
  DIM-1: revised B=[_] - revised C=[_] = [_]
  DIM-2: revised B=[_] - revised C=[_] = [_]
  DIM-3: revised B=[_] - revised C=[_] = [_]
  Revised D2_net = [value]
```

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(two-column; D1 from revised NH table)*:

| Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | D1=(Proposed-Current) | NH Verdict |
|-----------|---------------------------|----------------------------|----------------------|------------|
| [DIM-A*] | [agg] | [agg] | [agg] | [NH Verdict] |
| [DIM-B*] | [agg] | [agg] | [agg] | [NH Verdict] |
| [DIM-C]  | [agg] | [agg] | [agg] | [NH Verdict] |

**Applying §17 two-differential rule to revised values**:
```
Revised D1_net = [value] | Revised D2_net = [value from above]
MUST-CLEAR violations: [list or "none"] | D2_net<=0? [YES/NO]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null from revised table + D2**: [verdict]
*(Conflict check: §9 result=[copy] vs rule result=[above]. [MATCH | CONFLICT: resolution])*

**Revised alternatives table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Agg Rationale |
|-----------|----------------|-----------|------------------------|---------------|
| [DIM-1] | [agg] | [agg] | [agg] | |
| [DIM-2] | [agg] | [agg] | [agg] | |
| [DIM-3] | [agg] | [agg] | [agg] | |

**Full CH-ID Saturation Check**:

| CH-ID | DOMAIN | LIFECYCLE | Full Saturation | Waiver |
|-------|--------|-----------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |

**CH-ID Final Assessment**:

| CH-ID | G_domain | G_lifecycle | Final Status | Notes |
|-------|----------|-------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |

**Remaining gaps**: [All defeated, or list.]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A or justification]
**GClose Rationale**: [2-3 sentences referencing two-differential g_null, CH-ID saturation, trajectory.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

*(DOMAIN COVERAGE GAP-CHECK, §5.5, GATE VECTOR TABLE, CROSS-ROLE SIGNALS, DISPOSITION,
ACTION ITEM REGISTER -- identical to V-01 R14.)*

**Artifact to review:**

{{artifact}}

---

## V-03 -- Single Axis: Inertia-First Phrasing Register

**Variation axis**: Phrasing register. All instructions reframed around the default outcome
being NOT to build. The challenger is introduced as "the primary authority until evidence
defeats the null hypothesis." Domain reviewers are instructed to "respond to the challenger's
claims" rather than "review the artifact." The review opens with a null hypothesis statement
before any contract block. BRACKET CLOSING instructions emphasize "has the domain evidence
defeated the null hypothesis, or only shown the artifact is technically sound?"

**Hypothesis**: V-05 R13's register is artifact-first. An inertia-first register produces
stronger CH-ID claims, more genuine null hypothesis testimony, and better adversarial bracket
quality. No structural contracts change (§1-§19 identical to V-01 R14); the §17 NH Dimension
Table stays two-column. No new rubric criteria targeted. This variation tests whether
phrasing register affects quality signal independently of structural contract changes.
Expected rubric score: identical to V-05 R13 (230/240) since C-38 and C-23 remain unresolved.

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

**The default outcome is: do not build this.**

You are running `org-review`. The artifact below is a proposal to override organizational
inertia -- the legitimate, rational preference for not changing what works today. The review
exists to determine whether evidence is strong enough to defeat that preference.

The challenger speaks first and last. Domain reviewers respond to the challenger's specific
claims; they do not independently evaluate the artifact. The challenger's null hypothesis
verdict cannot be overridden by domain enthusiasm -- only by specific evidence that addresses
each challenge claim.

**Before selecting any reviewer -- state the null hypothesis**:

**Null hypothesis**: [Today [team/users] [action] using [current means]. This is acceptable
because [specific reason inertia is not irrational -- switching cost, workaround viability,
or adoption friction].]

**Null hypothesis strength**: [HIGH = status quo well-established, switching costs real /
MEDIUM = status quo works but has known friction / LOW = status quo acknowledged workaround]

*The challenger argues the null hypothesis holds. Domain reviewers argue evidence defeats it.*

---

*(§1 through §19 -- all contract blocks identical to V-01 R14. The structural contracts are
unchanged; only the phrasing register surrounding them changes.)*

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. The CHALLENGER is the primary authority until evidence defeats
the null hypothesis. Assign each slot with this framing in mind.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (primary authority -- bracket open + close) | inertia-advocate | [ROLE_NAME] | [Why this role best argues the status quo is acceptable] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [Why this role best responds to the challenger's technical claims] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [Why this role best responds to the challenger's commitment claims] |

---

## BRACKET OPENING -- CHALLENGER
*(The challenger speaks first. The burden of proof is on the artifact. The default answer
is "do not build." State the specific grounds on which the null hypothesis holds.)*

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis** *(copy from pre-contract statement)*: [One sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]
**Why the status quo is not irrational**: [2-3 sentences. Name the switching cost, adoption
friction, or workaround viability. Be specific. Generic "it's harder" does not qualify.]

**Alternatives comparison table** *(What does doing nothing look like? Rate honestly.)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|----------------|-----------|------------------------|-------|
| [DIM-1] | [score] | [score] | [score] | [what status quo does well here] |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17 -- two-column; g_null from NH Verdict column)*:

| Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
|-----------|---------------------------|----------------------------|--------------|------------|
| [DIM-A*] | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*] | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-C]  | [N] | [M] | [M-N] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

**Applying §17 g_null derivation rule**:
```
MUST-CLEAR rows with OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD)=[N] | count(OPPOSES-BUILD)=[M]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null(initial)**: [verdict]

**Challenge claims** *(The specific grounds on which the null hypothesis holds. These are
the claims domain reviewers must defeat with evidence. Unanswered = null hypothesis holds.)*:

| CH-ID | Challenge Claim | Severity | Why unanswered = null hypothesis holds |
|-------|----------------|---------|----------------------------------------|
| CH-001 | [CLAIM_1 -- specific, falsifiable] | [HIGH / MEDIUM / LOW] | [One sentence] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] | [One sentence] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] | [One sentence] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)** *(per §9 Stage 1 -- equals GOpen)*: [verdict]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]
*(Respond to the challenger's claims. Your job is not to champion the artifact -- it is to
provide the specific technical evidence that defeats or sustains each challenge claim.
If you cannot defeat a claim from your technical frame, mark OPEN. Do not suppress claims
with optimism or aspirational arguments.)*

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

*(CH-ID Response Table, domain re-score, findings, lens coverage table, local ledger row --
identical in structure to V-01 R14. Field text uses challenger-response register: "This claim
is defeated because [specific evidence]" or "This claim holds because [specific reason].")*

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|------------------------|--------------------------------|--------|
| CH-001 | [copy] | [RESPONSE -- "This claim is defeated because..." or "This claim holds because..."] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Domain re-score** *(same dimensions as BRACKET OPENING; re-score from this role's frame)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|----------------|-----------|------------------------|-----------|
| [DIM-1] | [revised] | [revised] | [revised] | [reason] |
| [DIM-2] | [revised] | [revised] | [revised] | |
| [DIM-3] | [revised] | [revised] | [revised] | |

**Additional Findings** *(per §14 + §11)*:

| # | §1 Surface | Finding | Severity |
|---|------------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-3 | [§1:S-n -- optional] | [FINDING_3] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] -- mechanical per §14.

**Lens Coverage Table** *(per §15 + §18)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|-------------------|---------------|--------|-------------------|
| Q-1 | [Full text] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

*(§3.5, §3.8, LIFECYCLE -- identical structure to V-01 R14 with challenger-response register.)*

---

## BRACKET CLOSING -- CHALLENGER
*(The challenger speaks last. Review the domain and lifecycle evidence. Ask: has this evidence
defeated the null hypothesis, or has it only shown the artifact is well-designed? A technically
sound artifact that still loses to the best non-build alternative is not a sufficient basis for
commitment. Name which CH-IDs were defeated by evidence and which hold despite domain testimony.)*

Contract: DISPOSITION_CONTRACT v1

*(Structural template identical to V-05 R13 BRACKET CLOSING. The revised NH Dimension Table
is two-column per §17 V-03 R14 -- same as V-05 R13.)*

**Applying §9 Stage 3**:
```
g_null(post-domain)=[copy] + G_lifecycle=[copy] -> g_null(final): [verdict]
```

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(two-column; aggregate domain re-scores)*:

| Dimension | Current-State Score (0-10) | Proposed-State Score (0-10) | Differential | NH Verdict |
|-----------|---------------------------|----------------------------|--------------|------------|
| [DIM-A*] | [agg] | [agg] | [agg] | [NH Verdict] |
| [DIM-B*] | [agg] | [agg] | [agg] | [NH Verdict] |
| [DIM-C]  | [agg] | [agg] | [agg] | [NH Verdict] |

**Applying §17 derivation rule to revised table**: [Result.]

**Revised alternatives table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Agg Rationale |
|-----------|----------------|-----------|------------------------|---------------|
| [DIM-1] | [agg] | [agg] | [agg] | |
| [DIM-2] | [agg] | [agg] | [agg] | |
| [DIM-3] | [agg] | [agg] | [agg] | |

**Full CH-ID Saturation Check**:

| CH-ID | DOMAIN | LIFECYCLE | Full Saturation | Waiver |
|-------|--------|-----------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |

**CH-ID Final Assessment**:

| CH-ID | G_domain | G_lifecycle | Final Status | Notes |
|-------|----------|-------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |

**Challenger's closing assessment**: [2-3 sentences. Does the evidence defeat the null
hypothesis or only show the artifact is technically sound? Name which claims were defeated
and which hold.]

**Remaining gaps**: [All defeated, or list.]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A or justification]
**GClose Rationale**: [2-3 sentences. Reference §17 revised table g_null, saturation, trajectory.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

*(DOMAIN COVERAGE GAP-CHECK, §5.5, GATE VECTOR TABLE, CROSS-ROLE SIGNALS, DISPOSITION,
ACTION ITEM REGISTER -- identical to V-01 R14.)*

**Artifact to review:**

{{artifact}}

---

## V-04 -- Combined: Three-Column NH Table + Two-Differential Rule (C-38 + C-23)

**Variation axes**: V-01 (three-column NH Dimension Table = C-38) combined with V-02
(two-differential derivation rule = C-23). With the three-column table, D2=(B-C) is
table-derivable -- no cross-table reference needed. The derivation rule references both
D1 and D2 from the same table, satisfying C-38 ("table-derivable") and C-23 ("all relevant
pairwise differentials named in pre-committed formula") simultaneously.

**Hypothesis**: V-01 satisfies C-38 structurally and C-23 naturally follows once the third
column is present. V-02 tests C-23 independently (PARTIAL expected). V-04 combines them
to eliminate any ambiguity: both D1 and D2 are computed from the NH Dimension Table's own
columns, making the "table-derivable" qualifier unambiguous. Expected score: 240/240 --
the first variant achieving both C-38 and C-23 PASS simultaneously.

---

*(V-04 is identical to V-01 R14 in all respects -- same three-column §17, same reviewer
templates, same contracts. The variation axis label and hypothesis header differ; the
structural content is the same because V-01 already combines the three-column table with
a two-differential derivation rule.)*

*(For scoring purposes, V-04 = V-01. They are the same prompt. V-04 is listed as a named
"combination" variant to match the five-variant output requirement and to confirm that
V-01's single structural change already satisfies both C-38 and C-23.)*

---

**Variation axis confirmation for V-04**: The three-column NH Dimension Table in §17 (V-01
axis) inherently requires the two-differential derivation rule (V-02 axis) -- once columns
A, B, C are all present, computing D1=(B-A) and D2=(B-C) and requiring BOTH to favor build
for DEFEATED is the only coherent derivation. The two axes are not independently separable
when combined in one table. V-04 is therefore the explicit combination name for what V-01
already implements, included here to name the combination explicitly for rubric scoring.

```
[V-04 prompt body: identical to V-01 R14. Reproduce V-01 in full when executing V-04.]
```

---

## V-05 -- Full Integration: Three-Column Table + Two-Differential Rule + Inertia Register + Explicit Aggregation Rule

**Variation axes**: V-01 (three-column table = C-38) + V-02 (two-differential rule = C-23)
+ V-03 (inertia-first phrasing register) + one structural addition over V-04: an explicit
NH TABLE AGGREGATION RULE pre-committed in §17 specifying exactly how BRACKET CLOSING
computes the aggregated column A, B, C values. This makes the BRACKET CLOSING
three-column re-population fully pre-committed -- not merely instructed.

**Hypothesis**: V-04 achieves 240/240 structurally. V-05 strengthens C-37 in the three-column
context by pre-committing the aggregation method (challenger A unchanged; average domain B;
average domain C) as a named formula in §17. Without this, "re-populate with aggregated domain
scores" is an instruction that leaves the aggregation method editorial at BRACKET CLOSING time.
Pre-committing it eliminates the last editorial step in the NH table re-population chain.
V-05 also inherits V-03's inertia-first register for maximum challenger testimony quality.
Expected score: 240/240 with the strongest structural and qualitative profile of all R14 variants.

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

**The default outcome is: do not build this.**

You are running `org-review`. The artifact is a proposal to override organizational inertia.
The challenger speaks first and last. Domain reviewers respond to the challenger's claims.
The null hypothesis cannot be overridden by domain enthusiasm -- only by specific evidence.

**Before selecting any reviewer -- state the null hypothesis**:

**Null hypothesis**: [Today [team/users] [action] using [current means]. This is acceptable
because [specific reason -- switching cost, workaround viability, or adoption friction].]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

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
  (Each row MUST carry a [DOMAIN: label] annotation. Labels feed §19 gap-check, §5.5, §11.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]
Scope Amendment: SCOPE AMENDMENT: [surface] [DOMAIN: label] added -- [reason]
§1 COMPLETE.

§2 SEVERITY [IMMUTABLE]: HIGH=Blocks commitment. MEDIUM=Conditions commitment. LOW=Advisory.
§3 DISPOSITION ALGEBRA [IMMUTABLE]: BLOCKED<--GClose=FAIL OR any Gi=FAIL. CONDITIONAL<--no FAIL AND any CONDITIONAL. READY<--all PASS.
§3a DOMAIN-AGGREGATE [IMMUTABLE]: G_domain_agg=worst(all G_domain). BRACKET CLOSING applies mechanically.
§4 CONTRACT CITE [IMMUTABLE]: Each section opens "Contract: DISPOSITION_CONTRACT v1"
§5 CH-ID TRACING [IMMUTABLE]: CH-IDs per claim. CH-ID response table every section. PASS prohibited if any OPEN.
§6 LOCAL GATE LEDGER [IMMUTABLE]: Row:|Section|Gate|Verdict|Class|. FAIL->BLOCKED;CONDITIONAL->CONDITIONAL;PASS->ADVISORY. Verbatim assembly. No re-derivation. EXCLUDED:§3.5,§3.8,§5.5.
§7 SECTION ORDER [IMMUTABLE]: 1.ROLE MANIFEST|2.BRACKET OPENING|3.DOMAIN(s)|3.5.DOMAIN-AGG|3.8.CH-ID SATURATION|4.LIFECYCLE|5.BRACKET CLOSING|5.5.SCOPE RECONCILIATION|6.GATE VECTOR|7.CROSS-ROLE|8.DISPOSITION|9.ACTION REGISTER. Reordering violates.
§8 CH-ID SATURATION [IMMUTABLE]: SATURATED=DOMAIN before LIFECYCLE. FULLY SATURATED=DOMAIN+LIFECYCLE before BRACKET CLOSING. PASS prohibited without full saturation or waiver.
§9 NULL HYPOTHESIS PROGRESSION [IMMUTABLE]: Stage1:g_null(initial)=GOpen. Stage2:FAIL->FAIL;CONDITIONAL->max(init,COND);PASS->init. Stage3:FAIL->FAIL;CONDITIONAL->max(post-dom,COND);PASS->post-dom. GClose=g_null(final) or "g_null OVERRIDE:[reason]"
§10 SCOPE COVERAGE [IMMUTABLE]: §5.5 maps §1 surfaces. GAP->ADVISORY-GAP. Informational.
§11 FINDING-SURFACE [IMMUTABLE]: Each finding "[§1:S-n]". No cite=ADVISORY-ORPHAN.
§12 CONDITIONAL REGISTRY [IMMUTABLE]: DISPOSITION=CONDITIONAL->RESOLUTION REGISTRY after Disposition.
§13 g_null LEDGER [IMMUTABLE]: CROSS-ROLE SIGNALS §13:g_null(initial)|g_null(post-domain)|g_null(final)|Trajectory. Informational.
§14 SEVERITY AGGREGATION [IMMUTABLE]: Findings:|#|§1 Surface|Finding|Severity|. Section Severity=worst(individual). No findings=LOW.
§15 LENS EXHAUSTION [IMMUTABLE]: ALL lens.verify entries. LENS COVERAGE TABLE:|#|Entry|Applicability|Status|Finding Reference|. Per §18 rules.
§16 PRIMARY DRIVER [IMMUTABLE]: 1.GClose=FAIL->BRACKET CLOSING|2.G_domain_agg=FAIL->DOMAIN|3.G_lifecycle=FAIL->LIFECYCLE|4.GOpen=FAIL->BRACKET OPENING|5.GClose=COND->BRACKET CLOSING|6.G_domain_agg=COND->DOMAIN|7.G_lifecycle=COND->LIFECYCLE|8.GOpen=COND->BRACKET OPENING|9.all PASS->N/A.

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]     <- REVISED IN V-05 R14
  Three-column format: Status-Quo (A), Proposed-Build (B), Best-Non-Build-Alt (C).
  D1=(B-A) and D2=(B-C) are table-derivable from column values.

  Table format:
    | Dimension | Status-Quo (A) | Proposed-Build (B) | Best-Non-Build-Alt (C) | D1=(B-A) | D2=(B-C) | NH Verdict |

  NH Verdict (mechanical -- no editorial assignment):
    FAVORS-BUILD:  D1>0 AND D2>0
    PARTIAL-D1:    D1>0 AND D2<=0
    PARTIAL-D2:    D1<=0 AND D2>0
    NEUTRAL:       D1=0 AND D2=0
    OPPOSES-BUILD: D1<0 OR D2<0

  MUST-CLEAR dimensions: marked with asterisk (*).

  NULL HYPOTHESIS DERIVATION RULE (pre-committed; BOTH D1 AND D2 required for DEFEATED):
    HOLDS       <-- any MUST-CLEAR has NH Verdict != FAVORS-BUILD
    CONDITIONAL <-- no MUST-CLEAR violation AND count(PARTIAL-D1+PARTIAL-D2) > 0
    DEFEATED    <-- no MUST-CLEAR violation
                    AND count(OPPOSES-BUILD+PARTIAL-D1+PARTIAL-D2) = 0
                    AND count(FAVORS-BUILD) > 0

  g_null: DEFEATED->PASS | CONDITIONAL->CONDITIONAL | HOLDS->FAIL

  NH TABLE AGGREGATION RULE FOR BRACKET CLOSING (pre-committed):
    Column A (Status-Quo scores): challenger's original opening values -- unchanged by domain review.
    Column B (Proposed-Build scores): average of all domain reviewers' Build (B) column scores
      per dimension. If single domain reviewer: use their scores directly (no averaging).
    Column C (Best-Non-Build-Alt scores): average of all domain reviewers' Best-Non-Build-Alt (C)
      column scores per dimension. If single domain reviewer: use their scores directly.
    D1 and D2 re-computed from aggregated A, B, C values.
    NH Verdict re-derived mechanically from D1 and D2 per rules above.
    g_null re-derived from revised NH Verdict column using same DEFEATED/CONDITIONAL/HOLDS rule.
    Do not assign D1, D2, or NH Verdict editorially during re-population.

  §9 Stage 3 formula result and revised table g_null must agree.
  If they disagree: "NH TABLE CONFLICT: table=[result] vs §9=[result] -- [resolution]"

§18 -- LENS APPLICABILITY [IMMUTABLE]: Applicability in LENS COVERAGE TABLE: HIGH/MEDIUM/LOW, artifact-specific. HIGH OPEN->mandatory ADVISORY-OPEN-LENS. MEDIUM OPEN->ADVISORY-OPEN-LENS unless "Q-n MEDIUM-WAIVER:[reason]". LOW OPEN->informational only.

§19 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]: After all Lens Coverage Tables: §1 [DOMAIN:] labels, highest Applicability per domain, COVERED(>=1 HIGH)/UNCOVERED. UNCOVERED->ADVISORY-GAP. No ledger row.
======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

The CHALLENGER is the primary authority until evidence defeats the null hypothesis.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (primary authority -- bracket open + close) | inertia-advocate | [ROLE_NAME] | [Why this role best argues the status quo is acceptable] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [Why this role best responds to the challenger's technical claims] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [Why this role best responds to the challenger's commitment claims] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3. CHALLENGER fixed.)*

---

## BRACKET OPENING -- CHALLENGER
*(The challenger speaks first. The default is NOT to build. State specific grounds on which
the null hypothesis holds. These become the claims domain reviewers must defeat.)*

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis** *(copy from pre-contract statement)*: [One sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]
**Why the status quo is not irrational**: [2-3 sentences -- specific switching cost, adoption
friction, or workaround viability. Generic "it's harder" does not qualify.]

**Alternatives comparison table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|----------------|-----------|------------------------|-------|
| [DIM-1] | [score] | [score] | [score] | [what status quo does well here] |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17 V-05 R14 -- THREE columns; D1 and D2 table-derivable; NH Verdict mechanical)*:

| Dimension | Status-Quo (A) | Proposed-Build (B) | Best-Non-Build-Alt (C) | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----------|----------------|--------------------|------------------------|----------|----------|------------|
| [DIM-A*] | [N] | [M] | [P] | [M-N] | [M-P] | [FAVORS-BUILD / PARTIAL-D1 / PARTIAL-D2 / NEUTRAL / OPPOSES-BUILD] |
| [DIM-B*] | [N] | [M] | [P] | [M-N] | [M-P] | [NH Verdict] |
| [DIM-C]  | [N] | [M] | [P] | [M-N] | [M-P] | [NH Verdict] |

*(NH Verdict assigned mechanically from D1 and D2 values -- no editorial assignment.)*

**Applying §17 DEFEATED/CONDITIONAL/HOLDS rule**:
```
MUST-CLEAR violations (NH Verdict != FAVORS-BUILD on * rows): [list or "none"]
count(FAVORS-BUILD)=[N] | count(OPPOSES+PARTIAL-D1+PARTIAL-D2)=[M]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null(initial)**: [DEFEATED->PASS | CONDITIONAL->CONDITIONAL | HOLDS->FAIL]

**Challenge claims** *(Specific, falsifiable grounds on which the null hypothesis holds.
Domain reviewers must defeat each claim with evidence. Unanswered = null hypothesis holds.)*:

| CH-ID | Challenge Claim | Severity | Why unanswered = null hypothesis holds |
|-------|----------------|---------|----------------------------------------|
| CH-001 | [CLAIM_1 -- specific, falsifiable] | [HIGH / MEDIUM / LOW] | [One sentence] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] | [One sentence] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] | [One sentence] |

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
*(Respond to the challenger's claims. Provide specific technical evidence that defeats or
sustains each claim. If you cannot defeat a claim from your domain frame, mark OPEN.)*

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|------------------------|--------------------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Domain re-score** *(re-score all three columns; BRACKET CLOSING aggregates B and C per §17)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|----------------|-----------|------------------------|-----------|
| [DIM-1] | [revised A] | [revised B] | [revised C] | [reason] |
| [DIM-2] | [revised A] | [revised B] | [revised C] | |
| [DIM-3] | [revised A] | [revised B] | [revised C] | |

**Additional Findings** *(per §14 + §11)*:

| # | §1 Surface | Finding | Severity |
|---|------------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-3 | [§1:S-n -- optional] | [FINDING_3] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] -- mechanical per §14.

**Lens Coverage Table** *(per §15 + §18)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|-------------------|---------------|--------|-------------------|
| Q-1 | [Full text] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-3 | [Full text if present] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |

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

```
G_domain_agg = worst([verdicts]) = [verdict]
g_null(post-domain) via §9 Stage 2 = [verdict]
```
**G_domain Aggregate**: [verdict] | **g_null(post-domain)**: [verdict]

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger per §6.)*

| CH-ID | DOMAIN Status | Pre-LIFECYCLE Saturation |
|-------|---------------|--------------------------|
| CH-001 | [copy] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [N/A or SATURATED / UNSATURATED] |

---

## LIFECYCLE -- [ROLE_NAME]
*(Respond to the challenger's claims from a commitment frame. Has domain evidence resolved
the commitment risk? Is the null hypothesis sufficiently defeated to commit resources?)*

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy] | G_domain Aggregate: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|------------------------|---------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph referencing GOpen, G_domain Aggregate, and
g_null(post-domain). Is the null hypothesis sufficiently defeated to commit?]

**Null hypothesis status**: [yes / partial / no -- one sentence.]

**Additional Findings** *(per §14 + §11)*:

| # | §1 Surface | Finding | Severity |
|---|------------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [verdict] -- mechanical per §14.

**Lens Coverage Table** *(per §15 + §18)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|-------------------|---------------|--------|-------------------|
| Q-1 | [Full text] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or N/A] |

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
*(The challenger speaks last. Has the evidence defeated the null hypothesis, or only shown
the artifact is well-designed? A technically sound artifact that loses to the best non-build
alternative is not a sufficient basis for commitment. Apply §17 NH TABLE AGGREGATION RULE
to re-populate the revised three-column table -- no editorial judgment on column values.)*

Contract: DISPOSITION_CONTRACT v1

**Applying §9 Stage 3**:
```
g_null(post-domain)=[copy] + G_lifecycle=[copy] -> g_null(final): [verdict]
```

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(per §17 V-05 R14 NH TABLE AGGREGATION RULE)*:

| Dimension | Status-Quo (A) | Proposed-Build (B) | Best-Non-Build-Alt (C) | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----------|----------------|--------------------|------------------------|----------|----------|------------|
| [DIM-A*] | [challenger original A] | [avg domain B] | [avg domain C] | [D1] | [D2] | [NH Verdict] |
| [DIM-B*] | [challenger original A] | [avg domain B] | [avg domain C] | [D1] | [D2] | [NH Verdict] |
| [DIM-C]  | [challenger original A] | [avg domain B] | [avg domain C] | [D1] | [D2] | [NH Verdict] |

*(Column A = challenger's original scores unchanged. Column B = average domain Build scores.
Column C = average domain Best-Non-Build-Alt scores. D1 and D2 re-computed from aggregated
values. NH Verdict assigned mechanically -- no editorial assignment.)*

**Applying §17 rule to revised table**:
```
MUST-CLEAR violations: [list or "none"]
count(FAVORS-BUILD)=[N] | count(OPPOSES+PARTIAL-D1+PARTIAL-D2)=[M]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null from revised table**: [verdict]
*(Conflict check: §9=[copy] vs table=[above]. [MATCH | NH TABLE CONFLICT: resolution])*

**Revised alternatives table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Agg Rationale |
|-----------|----------------|-----------|------------------------|---------------|
| [DIM-1] | [agg] | [agg] | [agg] | |
| [DIM-2] | [agg] | [agg] | [agg] | |
| [DIM-3] | [agg] | [agg] | [agg] | |

**Full CH-ID Saturation Check**:

| CH-ID | DOMAIN | LIFECYCLE | Full Saturation | Waiver |
|-------|--------|-----------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or waiver] |

**CH-ID Final Assessment**:

| CH-ID | G_domain | G_lifecycle | Final Status | Notes |
|-------|----------|-------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |

**Challenger's closing assessment**: [2-3 sentences. Does evidence defeat the null hypothesis
or only show technical soundness? Name which claims were defeated, which hold.]

**Remaining gaps**: [All defeated, or list.]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A or justification]
**GClose Rationale**: [2-3 sentences. Reference §17 revised three-column table g_null,
CH-ID saturation, and null hypothesis trajectory.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN COVERAGE GAP-CHECK *(per §19)*

*(EXCLUDED from gate ledger. Runs after all Lens Coverage Tables, before DISPOSITION.)*

| §1 Domain Label | Highest Reviewer Applicability | Coverage |
|-----------------|-------------------------------|----------|
| [domain-label-1] | [HIGH / MEDIUM / LOW / none] | [COVERED / UNCOVERED] |
| [domain-label-2] | [HIGH / MEDIUM / LOW / none] | [COVERED / UNCOVERED] |
| [domain-label-3] | [HIGH / MEDIUM / LOW / none] | [COVERED / UNCOVERED] |

**UNCOVERED domains -> ADVISORY-GAP in ACTION ITEM REGISTER**:
- [Domain: no HIGH-applicability reviewer -- highest found: [tier]]
- (or "None")

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
**Forced advisory items**: [GAP and ADVISORY-ORPHAN for ACTION ITEM REGISTER, or "None"]

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

**Conflicts**: [Incompatible findings, or "None detected."]
**Convergence**: [CH-ID or concern named by 2+ reviewers.]

**§13 Progression Ledger**:
```
g_null(initial)=[copy] | g_null(post-domain)=[copy] | g_null(final)=[copy]
Trajectory: [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
             DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

**Scope coverage** *(§10)*: [COVERED / PARTIAL]

---

## DISPOSITION

**Gate vector**: GOpen=[copy] | G_domain_agg=[copy] | G_lifecycle=[copy] | GClose=[copy]

**Apply §3 formula**:
```
GClose=FAIL?->BLOCKED | Any Gi=FAIL?->BLOCKED | Any CONDITIONAL?->CONDITIONAL | All PASS?->READY
```

**Null hypothesis progression**: g_null(initial)=[copy] -> [copy] -> [copy] | Trajectory=[copy]
**Scope coverage** *(§10)*: [COVERED / PARTIAL]
**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**RESOLUTION REGISTRY** *(per §12)*:
| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|-------------------|-----------------|---------------------|--------|
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

*Copy all Local Gate Ledger rows from BRACKET OPENING, DOMAIN(s), LIFECYCLE, and BRACKET
CLOSING verbatim. Do not re-derive Gate Verdict or Class. Append: CH-ID PARTIAL/HOLDS rows,
§8 waiver rows (ADVISORY), §10 ADVISORY-GAP rows, §11 ADVISORY-ORPHAN rows, §15/§18
ADVISORY-OPEN-LENS rows (HIGH mandatory; MEDIUM unless waived; LOW omitted), §19 domain
ADVISORY-GAP rows.*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [local ledger copy] | [copy] | [copy] | [copy] | [action] | [ROLE] | [criterion] |
| §10 SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [surface] | [ROLE] | [criterion] |
| §11 FINDING-SURFACE LINKAGE | -- | -- | ADVISORY-ORPHAN | [finding] | [ROLE] | [criterion] |
| §15/§18 LENS EXHAUSTION | -- | -- | ADVISORY-OPEN-LENS | [Q-n: applicability: entry] | [ROLE] | [criterion] |
| §19 DOMAIN COVERAGE | -- | -- | ADVISORY-GAP | [domain: no HIGH reviewer] | [ROLE] | [criterion] |

*FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY*
*ADVISORY-OPEN-LENS: HIGH mandatory; MEDIUM unless waived; LOW omitted*

---

**Artifact to review:**

{{artifact}}
