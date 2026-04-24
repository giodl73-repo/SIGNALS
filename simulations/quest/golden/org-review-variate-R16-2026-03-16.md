# org-review Variations -- Round 4 (v11 rubric, 2026-03-16)
Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v11-2026-03-16.md

Prior round summary:
- R1--R11: V-05 climbed to 210/225 via bracket architecture, local ledger, CH-ID tracing,
  per-finding severity aggregation (§14/C-30), lens exhaustion protocol (§15/C-31),
  primary driver derivation (§16/C-32). V-05 R11 is the baseline: 210/225.
- R12: V-02 R12 scored ~215/225 -- C-33+C-34+C-35 PASS simultaneously but WITHOUT the
  C-30+C-31+C-32 base (§14/§15/§16 absent). V-01 R12 failed C-09 (scored 71).
- Gap to 225: Combine V-05 R11's §1-§16 base with C-33+C-34+C-35 additions.

Round 4 strategy (three new aspirational criteria, new structural mechanisms):
- Baseline: V-05 R11 (§1-§16, C-30+C-31+C-32 PASS) as non-negotiable base.
  All R4 variants inherit §1-§16 and score >= 210 from base inheritance.
- R4 explores DIFFERENT structural placements for C-33/C-34/C-35 vs R12/R13:
  - V-01: single axis -- §17 ROLE MANIFEST APPLICABILITY PROTOCOL (C-33 target).
    Applicability rating committed in the ROLE MANIFEST table before any review executes,
    not per-row in the LENS COVERAGE TABLE during review. Each manifest row carries an
    Applicability column; ratings are artifact-specific (HIGH/MEDIUM/LOW).
  - V-02: single axis -- §17 PRE-REVIEW DOMAIN COVERAGE GAP-CHECK (C-34 target).
    A dedicated section between ROLE MANIFEST and BRACKET OPENING enumerates artifact
    domains, checks each for HIGH-applicability coverage, and emits ADVISORY-GAP items
    for uncovered domains before the first reviewer executes.
  - V-03: single axis -- §17 NH DIMENSION TABLE CONTRACT (C-35 target).
    Challenger's null hypothesis uses a structured per-dimension table with NH Verdict
    column (FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD). g_null(initial) derivable from
    NH Verdict column alone; no prose required.
  - V-04: combination -- V-01 + V-02 axes (§17 manifest applicability + §18 domain gap-check).
    C-33+C-34 target.
  - V-05: full integration -- V-01 + V-02 + V-03 axes (§17 + §18 + §19).
    C-33+C-34+C-35 simultaneously. 225/225 candidate.

---

## V-01

**Axis**: Role sequence -- §17 ROLE MANIFEST APPLICABILITY PROTOCOL (C-33 via manifest-time pre-commitment)
**Hypothesis**: C-33 requires that each LENS COVERAGE TABLE row carry an artifact-specific
applicability rating (HIGH/MEDIUM/LOW) as the evidential basis for the ADDRESSED/OPEN
determination. V-05 R11 emits LENS COVERAGE TABLEs with Status=ADDRESSED/OPEN but no
applicability rating -- the reviewer decides OPEN/ADDRESSED without a pre-committed basis.
V-01 relocates the applicability commitment to the ROLE MANIFEST: each manifest row carries an
Applicability column (HIGH/MEDIUM/LOW) rated before any reviewer executes. When the reviewer
emits its LENS COVERAGE TABLE, each row inherits the manifest applicability rating and carries
it explicitly. A scorer verifying C-33 reads the manifest -- the ratings are set before the
first reviewer, not invented at review time. The mechanism is distinct from R12/R13 which added
a separate §17 LENS COVERAGE APPLICABILITY PROTOCOL inside the contract block; V-01 here
pre-commits applicability at the role manifest level instead.

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

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. Do not add sections
between pre-printed headers. If a field cannot be filled, write `[N/A -- reason]`.

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
  BRACKET CLOSING applies this formula mechanically. No editorial re-assessment at closure.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A missing cite is an audit-trail gap.

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, ...).
  Every downstream section carries a mandatory CH-ID response table.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  (a) Row syntax: | Section | Gate | Verdict | Class |
      Class derives from verdict: FAIL -> BLOCKED; CONDITIONAL -> CONDITIONAL; PASS -> ADVISORY.
  (b) Emission timing: end of each verdict-emitting section, after verdict is stated.
  (c) Assembly: ACTION ITEM REGISTER copies local rows verbatim. Do not re-derive Gate Verdict
      or Class. The register is a copy, not a synthesis.
  EXCLUDED SECTIONS (emit NO ledger row):
    §3.5 Domain-Aggregate Checkpoint: produces no verdict; aggregation only. No row emitted.
    §3.8 CH-ID Saturation Check: produces no verdict; coverage verification only. No row emitted.
    §5.5 Scope Coverage Reconciliation: produces no gate verdict; coverage signal only. No row emitted.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical execution sequence:
    1. ROLE MANIFEST
    2. BRACKET OPENING
    3. DOMAIN(s)
    3.5. DOMAIN-AGGREGATE CHECKPOINT     [excluded from gate ledger per §6]
    3.8. CH-ID SATURATION CHECK          [excluded from gate ledger per §6]
    4. LIFECYCLE
    5. BRACKET CLOSING
    5.5. SCOPE COVERAGE RECONCILIATION   [excluded from gate ledger per §6]
    6. GATE VECTOR TABLE
    7. CROSS-ROLE SIGNALS
    8. DISPOSITION
    9. ACTION ITEM REGISTER
  Reordering any section violates this contract.
  LIFECYCLE must precede BRACKET CLOSING.
  CH-ID SATURATION CHECK must precede LIFECYCLE.
  SCOPE COVERAGE RECONCILIATION must precede GATE VECTOR TABLE.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  Before LIFECYCLE executes, each CH-ID must satisfy:
    SATURATED:       CH-ID has a response in >= 1 DOMAIN section.
  Before BRACKET CLOSING executes, each CH-ID must satisfy:
    FULLY SATURATED: CH-ID has a response in >= 1 DOMAIN section AND in the LIFECYCLE section.
  A PASS verdict from BRACKET CLOSING is prohibited when any CH-ID is not FULLY SATURATED
  without a stated saturation waiver.
  Saturation waiver format: "CH-XXX WAIVER: [LIFECYCLE not applicable -- one sentence reason]"
  Waivers are emitted in §3.8 and carried to ACTION ITEM REGISTER as ADVISORY.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1 -- g_null(initial) [emitted at BRACKET OPENING]:
    g_null(initial) = GOpen verdict directly.
  Stage 2 -- g_null(post-domain) [emitted at §3.5 DOMAIN-AGGREGATE CHECKPOINT]:
    if G_domain_agg = FAIL:        g_null(post-domain) = FAIL
    if G_domain_agg = CONDITIONAL: g_null(post-domain) = max(g_null(initial), CONDITIONAL)
    if G_domain_agg = PASS:        g_null(post-domain) = g_null(initial)
    Scale: FAIL < CONDITIONAL < PASS.
  Stage 3 -- g_null(final) [emitted at BRACKET CLOSING]:
    if G_lifecycle = FAIL:        g_null(final) = FAIL
    if G_lifecycle = CONDITIONAL: g_null(final) = max(g_null(post-domain), CONDITIONAL)
    if G_lifecycle = PASS:        g_null(final) = g_null(post-domain)
  GClose verdict must equal g_null(final) unless an override is invoked with explicit justification.
  Override format: "g_null OVERRIDE: [reason -- one sentence]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  After BRACKET CLOSING, §5.5 SCOPE COVERAGE RECONCILIATION maps each §1 IN-SCOPE surface to
  the reviewer(s) that addressed it.
    COVERED: surface named in >= 1 finding. GAP: surface not named in any finding.
  GAP surfaces -> forced LOW advisory, ADVISORY-GAP items in ACTION ITEM REGISTER.
  Gate signal (informational -- does not feed §3): COVERED / PARTIAL.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding produced by a DOMAIN or LIFECYCLE section must carry a §1 surface citation:
  "[§1:S-n] finding text". Findings without a valid §1 citation are ADVISORY-ORPHAN.
  ADVISORY-ORPHAN items appear in the ACTION ITEM REGISTER.
  §5.5 (top-down) and §11 (bottom-up) are independent requirements.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  When DISPOSITION = CONDITIONAL, emit a RESOLUTION REGISTRY table after Overall Disposition:
    | Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
  One row per CONDITIONAL gate. Status = OPEN at review time.
  If DISPOSITION != CONDITIONAL, write: "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  In CROSS-ROLE SIGNALS, a §13 PROGRESSION LEDGER assembles:
    g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory label
  Trajectory labels: MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED /
  LIFECYCLE-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED.
  Informational only. No ledger row emitted.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Within each DOMAIN and LIFECYCLE reviewer section, each finding entry carries an individual
  severity tag. Additional Findings are presented as a table:
    | # | §1 Surface | Finding | Severity |
    |---|-----------|---------|---------|
  Section Severity is derived mechanically from this table:
    Section Severity = worst(all finding severities in this section).
    Precedence: HIGH > MEDIUM > LOW.
    If no findings: Section Severity = LOW.
  Do not assign Section Severity editorially. Apply the formula and state the result.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN and LIFECYCLE reviewer section must address ALL entries from the role's
  lens.verify definition. A LENS COVERAGE TABLE is emitted after Additional Findings:
    | # | lens.verify Entry | Applicability | Status | Finding Reference |
    |---|------------------|--------------|--------|--------------------|
  The Applicability column is populated from the ROLE MANIFEST §17 pre-committed rating
  for this role. Status values: ADDRESSED / OPEN.
  OPEN entries on HIGH-applicability lens items are ADVISORY-OPEN-LENS items in ACTION ITEM REGISTER.
  OPEN entries on MEDIUM/LOW applicability items are informational.
  The lens exhaustion requirement does not change gate verdict derivation.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  In DISPOSITION, the Primary Driver field identifies which gate produced the binding verdict.
  Derivation formula (apply mechanically):
    If GClose = FAIL: Primary Driver = GClose (challenger override active)
    Else if any G_domain_i = FAIL: Primary Driver = DOMAIN (domain blocked)
    Else if G_lifecycle = FAIL: Primary Driver = LIFECYCLE
    Else if any gate = CONDITIONAL: Primary Driver = lowest-index CONDITIONAL gate
    Else: Primary Driver = N/A (all PASS)
  Do not assign Primary Driver editorially.

§17 -- ROLE MANIFEST APPLICABILITY PROTOCOL [IMMUTABLE]
  The ROLE MANIFEST table includes an Applicability column for each role row.
  Applicability is an artifact-specific rating (HIGH / MEDIUM / LOW) committed before
  any reviewer executes. It reflects how relevant this role's lens is to THIS artifact's
  domains and subject matter.

  Rating semantics:
    HIGH   = This role's lens.verify entries are directly applicable to this artifact.
             OPEN entries in the LENS COVERAGE TABLE are ADVISORY-OPEN-LENS.
    MEDIUM = This role's lens.verify entries are partially applicable.
             OPEN entries are informational but not action-required.
    LOW    = This role's lens.verify entries have limited applicability to this artifact.
             OPEN entries are not escalated.

  Rating is committed in the ROLE MANIFEST at execution start. Ratings may not change
  after ROLE MANIFEST is emitted (no retroactive re-rating during or after review).

  The LENS COVERAGE TABLE in each reviewer section inherits the role's pre-committed
  applicability rating from the ROLE MANIFEST. Each row in the table must carry the
  applicability value from the manifest, not a per-row re-assessment.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale | Applicability |
|------|-----------|------|---------------------|---------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] | [HIGH / MEDIUM / LOW -- rated for this artifact] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] | [HIGH / MEDIUM / LOW] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] | [HIGH / MEDIUM / LOW] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. Each row carries its Applicability rating.
  CHALLENGER Applicability is always HIGH -- inertia is universally applicable.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | [brief reason] |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DERIVATION RULE** *(pre-committed per §9; applied mechanically at BRACKET CLOSING)*:
  [State formula mapping table dimensions to g_null verdict before any reviewer runs.]

**Challenge claims** *(assign CH-IDs per §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
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

**CH-ID Response Table** *(mandatory per contract §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Domain Response | Status |
|-------|----------------------|----------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph referencing GOpen explicitly.]

**Null hypothesis status**: [yes / partial / no -- one sentence.]

**Additional Findings** *(per §14: each finding carries individual severity; per §11: each cites §1 surface)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

*(Findings without a valid §1:S-n citation are ADVISORY-ORPHAN per §11.)*

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**LENS COVERAGE TABLE** *(per §15 -- all lens.verify entries; Applicability from ROLE MANIFEST §17)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|--------------------|
| 1 | [lens.verify entry 1 from role definition] | [HIGH/MEDIUM/LOW -- from ROLE MANIFEST] | [ADDRESSED / OPEN] | [F-n or "no finding"] |
| 2 | [lens.verify entry 2] | [from ROLE MANIFEST] | [ADDRESSED / OPEN] | [F-n or "no finding"] |

*(OPEN entries on HIGH-applicability rows are ADVISORY-OPEN-LENS in ACTION ITEM REGISTER per §15.)*

**Recommendation**: [One concrete action.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(Per §6: EXCLUDED from gate ledger -- no row emitted here.)*

**Applying §3a formula**:
```
G_domain_agg = worst([list G_domain verdicts]) = [PASS / CONDITIONAL / FAIL]
```

**g_null(post-domain)** *(per §9 Stage 2)*:
```
G_domain_agg = [_]
g_null(initial) = [_]
Apply Stage 2 formula --> g_null(post-domain) = [PASS / CONDITIONAL / FAIL]
```

---

## §3.8 CH-ID SATURATION CHECK

*(Per §6: EXCLUDED from gate ledger -- no row emitted here. Pre-LIFECYCLE gate per §8.)*

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED -- or N/A] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None"]
*LIFECYCLE may proceed. Full saturation check (domain + lifecycle) executes at BRACKET CLOSING.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]
Received G_domain Aggregate: [copy from §3.5]
Received g_null(post-domain): [copy from §3.5]

**CH-ID Response Table** *(mandatory per contract §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph referencing GOpen and G_domain Aggregate and g_null(post-domain).]

**Null hypothesis status**: [yes / partial / no -- one sentence.]

**Additional Findings** *(per §14 and §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

*(Findings without a valid §1:S-n citation are ADVISORY-ORPHAN per §11.)*

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**LENS COVERAGE TABLE** *(per §15 -- all lens.verify entries; Applicability from ROLE MANIFEST §17)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|--------------------|
| 1 | [lens.verify entry 1 from role definition] | [from ROLE MANIFEST] | [ADDRESSED / OPEN] | [F-n or "no finding"] |
| 2 | [lens.verify entry 2] | [from ROLE MANIFEST] | [ADDRESSED / OPEN] | [F-n or "no finding"] |

*(OPEN entries on HIGH-applicability rows are ADVISORY-OPEN-LENS per §15.)*

**Recommendation**: [One concrete action.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Applying §9 Stage 3 formula**:
```
g_null(post-domain) = [copy from §3.5]
G_lifecycle         = [copy from LIFECYCLE local ledger]
Apply §9 Stage 3 --> g_null(final) = [FAIL / CONDITIONAL / PASS]
```

**Revised alternatives table** *(aggregate domain re-scores)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Domain Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| [DIM-1] | [agg score] | [agg score] | [agg score] | [one sentence] |
| [DIM-2] | [agg score] | [agg score] | [agg score] | |

**Applying NULL HYPOTHESIS DERIVATION RULE to revised table**: [State result. One sentence.]

**Full CH-ID Saturation Check** *(per §8 -- PASS prohibited without full saturation)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation |
|-------|--------------|-----------------|-----------------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] |

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
*Must equal g_null(final) per §9. Deviation requires override justification.*

**GClose Rationale**: [2-3 sentences. Reference g_null(final), CH-ID saturation, null trajectory.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6.)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [DOMAIN F-1 / etc.] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [reference] | [COVERED / GAP] |

**Coverage gate signal** *(informational)*:
[COVERED / PARTIAL -- list GAP surfaces if any]

**§11 ADVISORY-ORPHAN check**:
[List orphan findings or "None"]

**Forced advisory items for ACTION ITEM REGISTER**:
- GAP surfaces: [list or "None"]
- ADVISORY-ORPHAN findings: [list or "None"]
- ADVISORY-OPEN-LENS items from HIGH-applicability OPEN lens entries: [list or "None"]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN_ROLE(S)] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Two reviewers with incompatible CH-ID responses or findings. If none: "None detected."]

**Convergence**: [CH-ID or concern named by two or more reviewers.]

**§13 Progression Ledger**:
```
g_null(initial)     = [copy from BRACKET OPENING]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING]
Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED /
                     LIFECYCLE-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

**Scope coverage** *(§10 gate signal)*: [Restate. If PARTIAL: list surfaces.]

---

## DISPOSITION

**Gate vector**:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula**:
```
GClose = FAIL? --> BLOCKED
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [BLOCKED / CONDITIONAL / READY]

**Primary Driver** *(per §16)*: [derived mechanically from §16 formula]

**RESOLUTION REGISTRY** *(per §12)*:
[Emit registry table if CONDITIONAL; else "RESOLUTION REGISTRY: N/A -- disposition is [value]"]

---

## ACTION ITEM REGISTER

*(Copies local gate ledger rows verbatim per §6. Do not re-derive verdicts or classes.)*

| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [copy] | [copy] |
| DOMAIN -- [ROLE] | G_domain | [copy] | [copy] |
| LIFECYCLE -- [ROLE] | G_lifecycle | [copy] | [copy] |
| BRACKET CLOSING | GClose | [copy] | [copy] |

**Advisory items** *(ADVISORY-GAP, ADVISORY-ORPHAN, ADVISORY-OPEN-LENS, waivers)*:
- [list or "None"]

---

---

## V-02

**Axis**: Role sequence -- §17 PRE-REVIEW DOMAIN COVERAGE GAP-CHECK (C-34 via pre-review domain-inward check)
**Hypothesis**: C-34 requires that after the lens table is built, a gap-check name every artifact
domain with no HIGH-applicability reviewer and classify each as ADVISORY-GAP. V-05 R11 has §10
SCOPE COVERAGE GATE PROTOCOL which flags uncovered §1 IN-SCOPE surfaces, but §10 is surface-
outward (surface -> reviewer), not domain-inward (domain -> reviewer applicability). V-02 adds
§17 PRE-REVIEW DOMAIN COVERAGE GAP-CHECK positioned between ROLE MANIFEST and BRACKET OPENING.
The check enumerates artifact domains (inferred from §1 IN-SCOPE surfaces) and, for each domain,
determines whether any selected role has HIGH applicability. Domains with no HIGH-applicability
role become ADVISORY-GAP items in the ACTION ITEM REGISTER BEFORE any reviewer executes. This
is structurally distinct from R12's approach which ran the gap-check as part of the lens table
protocol inside §18; V-02 here moves the domain gap-check to a pre-review position.

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

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. Do not add sections
between pre-printed headers. If a field cannot be filled, write `[N/A -- reason]`.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§17;
reviewer sections may not execute until §1 COMPLETE and §17 gap-check
COMPLETE markers are both reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]
  (Add rows. Each row carries a [DOMAIN: label] annotation identifying the
  artifact domain this surface belongs to. Domains are used by §17 gap-check.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]
  (Write "None" if nothing is excluded.)

§1 COMPLETE -- role selection and §17 domain gap-check proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment.
  MEDIUM = Conditions commitment.
  LOW    = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose = FAIL  OR  exists Gi = FAIL
  CONDITIONAL  <-- no Gi = FAIL  AND  exists Gi = CONDITIONAL
  READY        <-- all Gi = PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(G_domain_1, ..., G_domain_n). Precedence: FAIL > CONDITIONAL > PASS.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim receives a CH-ID. Every downstream section carries a CH-ID response table.
  PASS prohibited if any CH-ID row shows OPEN status.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL -> BLOCKED; CONDITIONAL -> CONDITIONAL; PASS -> ADVISORY.
  Excluded sections (no row emitted): §3.5, §3.8, §5.5, §17.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical sequence:
    1. ROLE MANIFEST
    1.5. DOMAIN COVERAGE GAP-CHECK [§17 -- pre-review; excluded from gate ledger per §6]
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
  §17 DOMAIN COVERAGE GAP-CHECK must complete before BRACKET OPENING.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID response in >= 1 DOMAIN section before LIFECYCLE.
  FULLY SATURATED: response in >= 1 DOMAIN AND in LIFECYCLE before BRACKET CLOSING.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = GOpen. Stage 2: formula over G_domain_agg.
  Stage 3: formula over G_lifecycle. GClose must equal g_null(final).

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps §1 IN-SCOPE surfaces to reviewer findings. GAP surfaces -> ADVISORY-GAP.
  Gate signal (informational): COVERED / PARTIAL.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding cites §1 surface: "[§1:S-n] finding text". No citation -> ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  CONDITIONAL disposition -> RESOLUTION REGISTRY table. One row per CONDITIONAL gate.

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  In CROSS-ROLE SIGNALS: g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Per-finding severity tags in each reviewer section.
  Section Severity = worst(all finding severities). Do not assign editorially.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each reviewer section emits a LENS COVERAGE TABLE:
    | # | lens.verify Entry | Status | Finding Reference |
  OPEN entries -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  In DISPOSITION: Primary Driver derived by pre-committed precedence formula.
  GClose=FAIL -> GClose; any G_domain=FAIL -> DOMAIN; G_lifecycle=FAIL -> LIFECYCLE;
  any CONDITIONAL -> lowest-index CONDITIONAL gate; else N/A.

§17 -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  Runs AFTER ROLE MANIFEST, BEFORE BRACKET OPENING.
  Emit as section: "DOMAIN COVERAGE GAP-CHECK" (excluded from gate ledger per §6).

  Step 1 -- Enumerate artifact domains from §1 IN-SCOPE [DOMAIN: label] annotations.
  Step 2 -- For each domain, determine whether any selected role has HIGH applicability
            (i.e., the role's expertise.relevance directly covers this domain).
            Applicability assessment uses role definitions from .roles/signal/.
  Step 3 -- Domain coverage table:
    | Artifact Domain | Covering Role(s) | Coverage Status |
    |-----------------|-----------------|-----------------|
    | [domain-label]  | [ROLE or "none"] | [HIGH-COVERED / GAP] |
  Step 4 -- For each domain with Coverage Status = GAP:
            Emit: ADVISORY-LENS-GAP: Domain "[label]" has no HIGH-applicability reviewer.
            Add to ACTION ITEM REGISTER at review end as ADVISORY-LENS-GAP.
  Step 5 -- §17 COMPLETE marker before BRACKET OPENING proceeds.

  If no domains are identified from §1 annotations: emit
    "DOMAIN COVERAGE GAP-CHECK: N/A -- no [DOMAIN: label] annotations in §1 IN-SCOPE"
  and proceed to BRACKET OPENING.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

---

## DOMAIN COVERAGE GAP-CHECK

*(Per §17 -- runs before BRACKET OPENING. Excluded from gate ledger per §6.)*

**Artifact domains from §1 [DOMAIN: label] annotations**:
[List all distinct domain labels found in §1 IN-SCOPE rows.]

**Domain coverage table**:

| Artifact Domain | Covering Role(s) | Coverage Status |
|-----------------|-----------------|-----------------|
| [domain-label] | [ROLE or "none"] | [HIGH-COVERED / GAP] |
| [domain-label] | [ROLE or "none"] | [HIGH-COVERED / GAP] |

**GAP domains** *(per §17 Step 4)*:
[List ADVISORY-LENS-GAP items or "None -- all domains have HIGH-applicability coverage"]

§17 COMPLETE -- BRACKET OPENING proceeds.

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [One sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DERIVATION RULE**: [Pre-committed formula.]

**Challenge claims**:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)**: [PASS / CONDITIONAL / FAIL]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [_] | [_] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim | Response | Status |
|-------|----------------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph.]
**Null hypothesis status**: [yes / partial / no]

**Additional Findings** *(per §14 and §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**: worst([F-1=[_], ...]) = [SECTION_SEVERITY]
**Section Severity**: [HIGH / MEDIUM / LOW]

**LENS COVERAGE TABLE** *(per §15)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|--------------------|
| 1 | [entry] | [ADDRESSED / OPEN] | [F-n or "no finding"] |

*(OPEN entries -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.)*

**Recommendation**: [One action.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE] | G_domain | [_] | [_] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

```
G_domain_agg = worst([G_domain values]) = [_]
g_null(post-domain) = [formula result]
```

---

## §3.8 CH-ID SATURATION CHECK

| CH-ID | DOMAIN Status | Pre-LIFECYCLE Saturation |
|-------|--------------|--------------------------|
| CH-001 | [_] | [SATURATED / UNSATURATED] |
| CH-002 | [_] | [SATURATED / UNSATURATED] |

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen / G_domain_agg / g_null(post-domain): [copy from prior sections]

**CH-ID Response Table**:

| CH-ID | Challenge Claim | Response | Status |
|-------|----------------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph.]
**Null hypothesis status**: [yes / partial / no]

**Additional Findings** *(per §14 and §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**: worst([...]) = [SECTION_SEVERITY]
**Section Severity**: [HIGH / MEDIUM / LOW]

**LENS COVERAGE TABLE** *(per §15)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|--------------------|
| 1 | [entry] | [ADDRESSED / OPEN] | [F-n or "no finding"] |

**Recommendation**: [One action.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE] | G_lifecycle | [_] | [_] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

```
g_null(post-domain) = [copy]
G_lifecycle         = [copy]
g_null(final)       = [formula result]
```

**Revised alternatives table**: [columns: Dimension / Status Quo / Build / Best-Alt / Rationale]

**Applying NULL HYPOTHESIS DERIVATION RULE**: [Result.]

**Full CH-ID Saturation Check**:

| CH-ID | DOMAIN | LIFECYCLE | Full Saturation |
|-------|--------|-----------|-----------------|
| CH-001 | [_] | [_] | [FULLY SATURATED / UNSATURATED] |

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose Rationale**: [2-3 sentences.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [_] | [_] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [SURFACE_1] | [ROLE] | [ref] | [COVERED / GAP] |

**Coverage gate signal**: [COVERED / PARTIAL]
**§11 ADVISORY-ORPHAN check**: [list or "None"]
**Forced advisory items**: GAP surfaces: [list]; ADVISORY-ORPHAN: [list]; ADVISORY-LENS-GAP (from §17): [carry through]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER] | [_] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [_] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [_] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [_] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [or "None detected"]
**Convergence**: [or "None detected"]

**§13 Progression Ledger**:
```
g_null(initial) / g_null(post-domain) / g_null(final) / Trajectory
```

**Scope coverage**: [COVERED / PARTIAL]

---

## DISPOSITION

**Gate vector**: GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]
**Apply §3 formula**: [result]
**Overall Disposition**: [BLOCKED / CONDITIONAL / READY]
**Primary Driver** *(§16)*: [derived]
**RESOLUTION REGISTRY**: [table or N/A]

---

## ACTION ITEM REGISTER

| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
[copy local ledger rows verbatim]

**Advisory items**:
[ADVISORY-GAP, ADVISORY-ORPHAN, ADVISORY-OPEN-LENS, ADVISORY-LENS-GAP from §17, waivers]

---

---

## V-03

**Axis**: Inertia framing -- §17 NH DIMENSION TABLE CONTRACT (C-35 via tiered dimension table)
**Hypothesis**: C-35 requires the challenger's null hypothesis evaluation to use a structured
current-state vs proposed-state dimension table where g_null is derivable from table values
alone. V-05 R11 has an alternatives comparison table (Status Quo / Build / Best-Alt) with a
pre-committed NULL HYPOTHESIS DERIVATION RULE, but the derivation rule must be read alongside
the table to verify g_null -- no single column produces the verdict mechanically. V-03 adds
§17 NH DIMENSION TABLE CONTRACT to the BRACKET OPENING. The table has explicit columns for
Current-State Score, Proposed-State Score, Delta, and NH Verdict (FAVORS-BUILD / NEUTRAL /
OPPOSES-BUILD). Dimensions are tiered: MUST-CLEAR (structural blockers) and ADVISORY.
g_null(initial) is the mechanical output of a tier-weighted formula over NH Verdict column;
no prose reading required. This is distinct from R12 V-01 which added a standalone §17
section; V-03 here integrates the NH Dimension Table directly into the BRACKET OPENING template
as a required sub-block alongside the existing alternatives comparison table.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
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
pre-printed heading, label, field, formula, or structural element. If a field cannot be
filled, write `[N/A -- reason]`.

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
OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(G_domain_1, ...). FAIL > CONDITIONAL > PASS.

§4-§6: [IMMUTABLE -- contract cite, CH-ID tracing, local gate ledger. Identical to V-05 R11.]

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1. ROLE MANIFEST  2. BRACKET OPENING  3. DOMAIN(s)  3.5. DOMAIN-AGGREGATE CHECKPOINT
  3.8. CH-ID SATURATION CHECK  4. LIFECYCLE  5. BRACKET CLOSING
  5.5. SCOPE COVERAGE RECONCILIATION  6. GATE VECTOR TABLE  7. CROSS-ROLE SIGNALS
  8. DISPOSITION  9. ACTION ITEM REGISTER

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED before LIFECYCLE; FULLY SATURATED before BRACKET CLOSING.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = GOpen.
  Stage 2: formula over G_domain_agg. Stage 3: formula over G_lifecycle.

§10-§13: [IMMUTABLE -- scope coverage gate, finding-surface linkage, conditional resolution
registry, g_null progression ledger. Identical to V-05 R11.]

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Per-finding severity tags. Section Severity = worst(). No editorial assignment.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  LENS COVERAGE TABLE per reviewer section. OPEN entries -> ADVISORY-OPEN-LENS.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  Precedence formula for Primary Driver in DISPOSITION.

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]
  BRACKET OPENING includes a NULL HYPOTHESIS DIMENSION TABLE as a required sub-block,
  positioned BEFORE the alternatives comparison table. This table makes g_null(initial)
  mechanically derivable from the NH Verdict column without reading any prose.

  Table structure:
    | # | Dimension | Tier | Current-State Score | Proposed-State Score | Delta | NH Verdict |
    |---|-----------|------|--------------------|--------------------|-------|------------|

  Column definitions:
    Dimension: a specific measurable aspect of the build/no-build decision.
    Tier:      MUST-CLEAR (a MUST-CLEAR OPPOSES-BUILD blocks g_null regardless of other rows)
               or ADVISORY (contributes to weighted formula but does not block alone).
    Current-State Score: 1-5 scale for the team's current approach without this artifact.
    Proposed-State Score: 1-5 scale for the team's approach with this artifact built.
    Delta: Proposed-State Score minus Current-State Score (positive = favors build).
    NH Verdict: FAVORS-BUILD (Delta >= 1) | NEUTRAL (Delta = 0) | OPPOSES-BUILD (Delta <= -1).

  Minimum: >= 2 MUST-CLEAR dimensions and >= 1 ADVISORY dimension.

  g_null(initial) DERIVATION FORMULA [pre-committed; applied to NH Verdict column only]:
    Step 1 -- MUST-CLEAR check:
      If any MUST-CLEAR row has NH Verdict = OPPOSES-BUILD:
        g_null(initial) = CONDITIONAL or FAIL (challenger assigns based on severity)
        Emit: "MUST-CLEAR BLOCKED: [dimension name] OPPOSES-BUILD -- g_null floor = CONDITIONAL"
    Step 2 -- Weighted tally (runs regardless of Step 1):
      FAVORS-BUILD = +1, NEUTRAL = 0, OPPOSES-BUILD = -1.
      MUST-CLEAR weight = 2, ADVISORY weight = 1.
      Weighted score = sum(verdict * weight).
    Step 3 -- Apply threshold:
      Weighted score > 0: g_null(initial) = FAIL (null hypothesis defeated)
      Weighted score = 0: g_null(initial) = CONDITIONAL
      Weighted score < 0: g_null(initial) = PASS (null hypothesis holds)
    If Step 1 produced CONDITIONAL floor, use max(Step 1 result, Step 3 result).

  The NH Dimension Table REPLACES the "Null hypothesis strength: HIGH/MEDIUM/LOW" narrative.
  The alternatives comparison table remains (dimensions there may differ from §17 dimensions).
  g_null(initial) stated after the §17 table must match the formula result.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17 -- required sub-block; g_null(initial) derived here)*:

| # | Dimension | Tier | Current-State Score | Proposed-State Score | Delta | NH Verdict |
|---|-----------|------|--------------------|--------------------|-------|------------|
| 1 | [DIM-A] | [MUST-CLEAR / ADVISORY] | [1-5] | [1-5] | [Proposed-Current] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| 2 | [DIM-B] | [MUST-CLEAR / ADVISORY] | [1-5] | [1-5] | [Delta] | [NH Verdict] |
| 3 | [DIM-C] | [ADVISORY] | [1-5] | [1-5] | [Delta] | [NH Verdict] |

**Applying §17 g_null(initial) derivation formula**:
```
Step 1 -- MUST-CLEAR check:
  MUST-CLEAR rows: [list rows with their NH Verdict]
  Any OPPOSES-BUILD? [YES -- floor set to CONDITIONAL | NO]

Step 2 -- Weighted tally:
  Row contributions: [list each row: verdict * weight = contribution]
  Weighted score = [sum]

Step 3 -- Threshold:
  Weighted score [> / = / <] 0 --> g_null(initial) = [FAIL / CONDITIONAL / PASS]

Step 1 floor: [applicable or N/A]
g_null(initial) = max(Step 1, Step 3) = [FAIL / CONDITIONAL / PASS]
```

**g_null(initial)** *(derivable from NH Verdict column above)*: [FAIL / CONDITIONAL / PASS]

**Null hypothesis statement**: [What the team does today instead. One sentence.]

**Alternatives comparison table** *(separate from §17 table; compares options holistically)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DERIVATION RULE** *(per §9; applies to alternatives table at BRACKET CLOSING)*:
[State formula.]

**Challenge claims**:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence. Must be consistent with g_null(initial).]

*g_null(initial) = GOpen per §9 Stage 1. GOpen must match formula result above.*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [_] | [_] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table**:
[same structure as V-01]

**Additional Findings** *(per §14 and §11)*:
[same structure as V-01]

**LENS COVERAGE TABLE** *(per §15)*:
[same structure as V-01]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**: [standard row]

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT
[standard formula application]

## §3.8 CH-ID SATURATION CHECK
[standard check]

## LIFECYCLE -- [ROLE_NAME]
[same structure as V-01 LIFECYCLE section]

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Applying §9 Stage 3 formula**: [standard g_null(final) derivation]

**Revised NH Dimension Table** *(per §17 -- aggregate domain re-scores)*:

| # | Dimension | Tier | Aggregated Current-State | Aggregated Proposed-State | Delta | NH Verdict |
|---|-----------|------|--------------------------|--------------------------|-------|------------|
| 1 | [DIM-A] | [MUST-CLEAR / ADVISORY] | [agg score] | [agg score] | [Delta] | [NH Verdict] |
| 2 | [DIM-B] | [MUST-CLEAR / ADVISORY] | [agg score] | [agg score] | [Delta] | [NH Verdict] |
| 3 | [DIM-C] | [ADVISORY] | [agg score] | [agg score] | [Delta] | [NH Verdict] |

**Applying §17 formula to revised table**: [Step 1-3 result. Must be consistent with g_null(final).]

**Revised alternatives table** *(for NULL HYPOTHESIS DERIVATION RULE at closure)*:
[standard table]

**Full CH-ID Saturation Check**: [standard]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose Rationale**: [2-3 sentences. Reference g_null(final) and §17 NH Verdict column trajectory.]

**Local Gate Ledger Row**: [standard]

---

## §5.5 SCOPE COVERAGE RECONCILIATION
[standard]

## GATE VECTOR TABLE
[standard 4-row table]

## CROSS-ROLE SIGNALS

**Conflicts**: [or "None"]
**Convergence**: [or "None"]

**§13 Progression Ledger**:
```
g_null(initial)     = [copy -- verified from §17 NH Verdict column]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING]
Trajectory:         [label]
```

**Scope coverage**: [COVERED / PARTIAL]

---

## DISPOSITION
[standard formula + Primary Driver per §16]

## ACTION ITEM REGISTER
[standard ledger copy + advisory items]

---

---

## V-04

**Axes**: Role sequence + Output format -- §17 ROLE MANIFEST APPLICABILITY + §18 PRE-REVIEW DOMAIN COVERAGE GAP-CHECK (C-33+C-34 combined)
**Hypothesis**: C-33 and C-34 are orthogonal (C-31 is role-outward; C-34 is domain-inward)
but are structurally linked: C-34's gap-check requires knowing which roles have HIGH applicability
to which domains. V-04 combines V-01's manifest-level applicability ratings (§17) with V-02's
pre-review domain gap-check (§18). The key integration: the §18 domain gap-check table uses the
§17 applicability ratings directly -- a domain is HIGH-COVERED if any selected role's manifest
Applicability = HIGH AND the role's expertise.relevance covers that domain. This makes §17 the
pre-committed evidence that feeds §18's gap determination. C-33 is satisfied by the manifest
ratings; C-34 is satisfied by the §18 gap-check table that classifies each domain using those
ratings. The two criteria become causally linked: §17 ratings are the evidential basis for §18
classifications.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
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
pre-printed heading, label, field, formula, or structural element. If a field cannot be
filled, write `[N/A -- reason]`.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§18;
reviewer sections may not execute until §1 COMPLETE and §18 domain
gap-check COMPLETE markers are both reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE (each row carries a [DOMAIN: label] annotation):
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]
OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

§1 COMPLETE -- role selection and §18 domain gap-check proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain). FAIL > CONDITIONAL > PASS.

§4-§6: [IMMUTABLE -- contract cite, CH-ID tracing, local gate ledger.]

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1. ROLE MANIFEST
  1.5. DOMAIN COVERAGE GAP-CHECK [§18 -- pre-review; excluded from gate ledger]
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
  §18 DOMAIN COVERAGE GAP-CHECK must complete before BRACKET OPENING.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each reviewer section emits a LENS COVERAGE TABLE:
    | # | lens.verify Entry | Applicability | Status | Finding Reference |
  The Applicability column carries the pre-committed rating from the ROLE MANIFEST §17
  for this role. OPEN entries on HIGH-applicability items -> ADVISORY-OPEN-LENS.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]

§17 -- ROLE MANIFEST APPLICABILITY PROTOCOL [IMMUTABLE]
  The ROLE MANIFEST table includes an Applicability column for each role.
  Applicability is artifact-specific (HIGH / MEDIUM / LOW), committed before any reviewer.
  Rating semantics:
    HIGH   = Role's lens.verify entries directly applicable to this artifact's domains.
    MEDIUM = Partially applicable.
    LOW    = Limited applicability to this artifact.
  Ratings are committed in ROLE MANIFEST. Immutable after ROLE MANIFEST is emitted.
  Each LENS COVERAGE TABLE row inherits its role's manifest Applicability rating.
  Do not re-rate applicability per lens-entry; use the manifest rating uniformly for the role.

§18 -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  Runs AFTER ROLE MANIFEST (using §17 applicability ratings), BEFORE BRACKET OPENING.
  Emitted as section: "DOMAIN COVERAGE GAP-CHECK" (excluded from gate ledger per §6).

  Step 1 -- Enumerate artifact domains from §1 [DOMAIN: label] annotations.
  Step 2 -- For each domain, check whether any selected role has:
            (a) Manifest Applicability = HIGH (from §17) AND
            (b) expertise.relevance covering that domain (from role definition).
            If (a) AND (b): domain is HIGH-COVERED.
            If neither: domain is GAP.
  Step 3 -- Domain coverage table:
    | Artifact Domain | Role(s) with HIGH Applicability | Coverage Status |
    |-----------------|--------------------------------|-----------------|
    | [domain-label]  | [ROLE or "none"]               | [HIGH-COVERED / GAP] |
  Step 4 -- GAP domains: emit ADVISORY-LENS-GAP item for each.
  Step 5 -- §18 COMPLETE marker.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale | Applicability |
|------|-----------|------|---------------------|---------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] | HIGH |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] | [HIGH / MEDIUM / LOW] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] | [HIGH / MEDIUM / LOW] |

*(§17 applicability ratings above are committed. Immutable after this table is emitted.)*

---

## DOMAIN COVERAGE GAP-CHECK

*(Per §18 -- runs before BRACKET OPENING; uses §17 manifest ratings as evidence basis.)*

**Artifact domains from §1 [DOMAIN: label] annotations**:
[List distinct domain labels.]

**Domain coverage table**:

| Artifact Domain | Role(s) with HIGH Applicability | Coverage Status |
|-----------------|--------------------------------|-----------------|
| [domain-label] | [ROLE or "none"] | [HIGH-COVERED / GAP] |

**GAP domain items** *(per §18 Step 4)*:
[ADVISORY-LENS-GAP items or "None"]

§18 COMPLETE -- BRACKET OPENING proceeds.

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [One sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table**:
[3+ dimension table with Status Quo / Build / Best-Alt columns]

**NULL HYPOTHESIS DERIVATION RULE**: [Pre-committed formula per §9.]

**Challenge claims**:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [_] |
| CH-002 | [CLAIM_2] | [_] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)**: [= GOpen]

**Local Gate Ledger Row**: [standard]

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table**: [standard]
**Decision-readiness assessment**: [One paragraph.]
**Null hypothesis status**: [yes / partial / no]

**Additional Findings** *(per §14 and §11)*:

| # | §1 Surface | Finding | Severity |
[rows]

**Finding Severity Aggregation (per §14)**: [formula result]
**Section Severity**: [HIGH / MEDIUM / LOW]

**LENS COVERAGE TABLE** *(per §15 -- Applicability from §17 ROLE MANIFEST)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|--------------------|
| 1 | [entry] | [HIGH/MEDIUM/LOW -- from §17 ROLE MANIFEST] | [ADDRESSED / OPEN] | [F-n or "no finding"] |

*(OPEN on HIGH-applicability -> ADVISORY-OPEN-LENS per §15.)*

**Recommendation**: [One action.]
**G_domain Verdict / Reason**: [verdict. One sentence.]
**Local Gate Ledger Row**: [standard]

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT
[standard formula]

## §3.8 CH-ID SATURATION CHECK
[standard]

## LIFECYCLE -- [ROLE_NAME]
[same structure as DOMAIN section with §15 LENS COVERAGE TABLE carrying §17 applicability]

## BRACKET CLOSING -- CHALLENGER
Contract: DISPOSITION_CONTRACT v1
[standard §9 Stage 3 + revised alternatives table + CH-ID full saturation check + GClose]

## §5.5 SCOPE COVERAGE RECONCILIATION
[standard; forced advisory items include ADVISORY-LENS-GAP from §18]

## GATE VECTOR TABLE
[standard]

## CROSS-ROLE SIGNALS
[standard + §13 Progression Ledger]

## DISPOSITION
[standard §3 formula + §16 Primary Driver + §12 Resolution Registry if CONDITIONAL]

## ACTION ITEM REGISTER
[standard ledger copy; advisory items include ADVISORY-LENS-GAP from §18]

---

---

## V-05

**Axes**: Output format + Inertia framing + Role sequence -- §17 ROLE MANIFEST APPLICABILITY + §18 DOMAIN COVERAGE GAP-CHECK + §19 NH DIMENSION TABLE (C-33+C-34+C-35 maximal)
**Hypothesis**: The three criteria C-33/C-34/C-35 can be activated simultaneously with mutually
reinforcing mechanisms: (1) §17 commits applicability ratings in the ROLE MANIFEST before any
reviewer, satisfying C-33's pre-commitment requirement; (2) §18 uses §17's ratings as the
evidential basis for a domain-inward gap-check before BRACKET OPENING, satisfying C-34 and making
§18 causally downstream of §17; (3) §19 adds a tiered NH Dimension Table to BRACKET OPENING with
a pre-committed formula that makes g_null(initial) mechanically derivable from the NH Verdict
column, satisfying C-35 without disrupting the §9 g_null progression chain. Together:
§17 -> §18 (applicability evidence feeds domain gap-check) and §17 -> §15 (applicability feeds
per-row lens coverage annotation) create a single applicability commitment that satisfies both
C-33 and C-34. §19 activates C-35 independently through the NH Verdict column formula. The three
criteria share no conflicting structural constraints. All 27 aspirational criteria (C-09 through
C-35) should be simultaneously satisfiable in a single review execution.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
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

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§19;
reviewer sections may not execute until §1 COMPLETE and §18 domain
gap-check COMPLETE markers are both reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE (each row carries a [DOMAIN: label] annotation):
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]
  (Add rows. Exhaustive. [DOMAIN: label] annotations feed §18 gap-check.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

§1 COMPLETE -- role selection, §18 domain gap-check, and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions commitment. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain). FAIL > CONDITIONAL > PASS.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Challenge claims get CH-IDs. Every downstream section carries a CH-ID response table.
  PASS prohibited if any CH-ID shows OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row: | Section | Gate | Verdict | Class |
  Excluded sections (no row): §3.5, §3.8, §5.5, §17 [domain gap-check], §18 [not used here].

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical sequence:
    1. ROLE MANIFEST
    1.5. DOMAIN COVERAGE GAP-CHECK [§18 -- pre-review; excluded from gate ledger]
    2. BRACKET OPENING (includes §19 NH DIMENSION TABLE)
    3. DOMAIN(s)
    3.5. DOMAIN-AGGREGATE CHECKPOINT
    3.8. CH-ID SATURATION CHECK
    4. LIFECYCLE
    5. BRACKET CLOSING (includes revised §19 NH DIMENSION TABLE)
    5.5. SCOPE COVERAGE RECONCILIATION
    6. GATE VECTOR TABLE
    7. CROSS-ROLE SIGNALS
    8. DISPOSITION
    9. ACTION ITEM REGISTER
  §18 DOMAIN COVERAGE GAP-CHECK must complete before BRACKET OPENING.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: response in >= 1 DOMAIN before LIFECYCLE.
  FULLY SATURATED: response in >= 1 DOMAIN AND LIFECYCLE before BRACKET CLOSING.
  PASS from BRACKET CLOSING prohibited without full saturation (or stated waiver).

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = GOpen.
  g_null(initial) must equal the §19 NH Dimension Table formula result -- not an independent
  assessment. If §19 formula produces CONDITIONAL, GOpen = CONDITIONAL.
  Stage 2: formula over G_domain_agg. Stage 3: formula over G_lifecycle.
  GClose must equal g_null(final).

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps §1 surfaces to findings. GAP surfaces -> ADVISORY-GAP.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding: "[§1:S-n] finding text". No citation -> ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  CONDITIONAL disposition -> RESOLUTION REGISTRY table.

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS: g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Per-finding severity in reviewer sections.
  Section Severity = worst(). Do not assign editorially.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  LENS COVERAGE TABLE per reviewer section:
    | # | lens.verify Entry | Applicability | Status | Finding Reference |
  Applicability column: carry from §17 ROLE MANIFEST for this role.
  OPEN on HIGH-applicability rows -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  Precedence formula in DISPOSITION:
    GClose=FAIL -> Primary Driver=GClose. Any G_domain=FAIL -> DOMAIN.
    G_lifecycle=FAIL -> LIFECYCLE. Any CONDITIONAL -> lowest-index CONDITIONAL gate.
    All PASS -> N/A.

§17 -- ROLE MANIFEST APPLICABILITY PROTOCOL [IMMUTABLE]
  ROLE MANIFEST includes Applicability column (HIGH / MEDIUM / LOW) per role.
  Rating is artifact-specific and committed before any reviewer executes.
    HIGH: role's lens.verify directly applicable to this artifact's domains.
    MEDIUM: partially applicable.
    LOW: limited applicability.
  Immutable after ROLE MANIFEST is emitted. Used by §15 (LENS COVERAGE TABLE) and
  §18 (DOMAIN COVERAGE GAP-CHECK) as the applicability evidence basis.

§18 -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  Runs AFTER ROLE MANIFEST, BEFORE BRACKET OPENING. Excluded from gate ledger.
  Uses §17 manifest applicability ratings as evidence.

  Step 1 -- Enumerate artifact domains from §1 [DOMAIN: label] annotations.
  Step 2 -- For each domain: a role provides HIGH coverage if
            its §17 Applicability = HIGH AND its expertise.relevance covers the domain.
  Step 3 -- Domain coverage table:
    | Artifact Domain | Role(s) with HIGH Coverage | Coverage Status |
    |-----------------|---------------------------|-----------------|
    | [domain-label]  | [ROLE or "none"]          | [HIGH-COVERED / GAP] |
  Step 4 -- GAP domains: emit ADVISORY-LENS-GAP item per GAP domain.
  Step 5 -- §18 COMPLETE.

§19 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]
  BRACKET OPENING includes a NULL HYPOTHESIS DIMENSION TABLE as a required sub-block,
  BEFORE the alternatives comparison table. BRACKET CLOSING includes a revised table.
  This table makes g_null(initial) mechanically derivable from NH Verdict column.

  Table structure:
    | # | Dimension | Tier | Current-State Score | Proposed-State Score | Delta | NH Verdict |

  Column definitions:
    Tier:          MUST-CLEAR (blocks g_null if OPPOSES-BUILD) or ADVISORY.
    Current/Proposed-State Score: 1-5 scale.
    Delta:         Proposed minus Current. Positive = favors build.
    NH Verdict:    FAVORS-BUILD (Delta >= 1) | NEUTRAL (Delta = 0) | OPPOSES-BUILD (Delta <= -1).

  Minimum: >= 2 MUST-CLEAR dimensions and >= 1 ADVISORY dimension.

  g_null DERIVATION FORMULA [pre-committed; applied to NH Verdict column only]:
    Step 1 -- MUST-CLEAR check:
      If any MUST-CLEAR row has OPPOSES-BUILD: g_null floor = CONDITIONAL.
    Step 2 -- Weighted tally:
      FAVORS-BUILD=+1, NEUTRAL=0, OPPOSES-BUILD=-1. MUST-CLEAR weight=2, ADVISORY weight=1.
      Weighted score = sum(verdict * weight).
    Step 3 -- Threshold: score > 0 -> FAIL; score = 0 -> CONDITIONAL; score < 0 -> PASS.
    g_null = max(Step 1 floor, Step 3 result).

  §9 Stage 1: g_null(initial) = GOpen. GOpen must equal §19 formula result.
  §19 table and formula are the pre-committed evidence basis for g_null(initial).

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale | Applicability |
|------|-----------|------|---------------------|---------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] | HIGH |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] | [HIGH / MEDIUM / LOW] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] | [HIGH / MEDIUM / LOW] |

*(§17 applicability ratings committed above. Immutable. Used by §15 and §18.)*

---

## DOMAIN COVERAGE GAP-CHECK

*(Per §18 -- uses §17 manifest ratings as evidence. Excluded from gate ledger per §6.)*

**Artifact domains from §1 [DOMAIN: label] annotations**:
[List distinct domains.]

**Domain coverage table**:

| Artifact Domain | Role(s) with HIGH Coverage | Coverage Status |
|-----------------|---------------------------|-----------------|
| [domain-label] | [ROLE with HIGH applicability AND expertise match, or "none"] | [HIGH-COVERED / GAP] |
| [domain-label] | [ROLE or "none"] | [HIGH-COVERED / GAP] |

**Applicability evidence basis** *(§17 ratings applied in Step 2)*:
- [ROLE_NAME]: Applicability=[from manifest], expertise.relevance covers [domain list]
- [ROLE_NAME]: Applicability=[from manifest], expertise.relevance covers [domain list]

**GAP domain items** *(per §18 Step 4)*:
[ADVISORY-LENS-GAP: Domain "[label]" -- no HIGH-applicability coverage in selected role set]
[or "None -- all artifact domains have HIGH-applicability coverage"]

§18 COMPLETE -- BRACKET OPENING proceeds.

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**NULL HYPOTHESIS DIMENSION TABLE** *(per §19 -- g_null(initial) derived from NH Verdict column)*:

| # | Dimension | Tier | Current-State Score | Proposed-State Score | Delta | NH Verdict |
|---|-----------|------|--------------------|--------------------|-------|------------|
| 1 | [DIM-A -- specific measurable aspect] | MUST-CLEAR | [1-5] | [1-5] | [B-A] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| 2 | [DIM-B] | MUST-CLEAR | [1-5] | [1-5] | [Delta] | [NH Verdict] |
| 3 | [DIM-C] | ADVISORY | [1-5] | [1-5] | [Delta] | [NH Verdict] |

**Applying §19 g_null(initial) derivation formula**:
```
Step 1 -- MUST-CLEAR check:
  Row 1 (DIM-A, MUST-CLEAR): NH Verdict = [_]. OPPOSES-BUILD? [YES/NO]
  Row 2 (DIM-B, MUST-CLEAR): NH Verdict = [_]. OPPOSES-BUILD? [YES/NO]
  MUST-CLEAR floor = [CONDITIONAL -- one or more OPPOSES-BUILD | not triggered]

Step 2 -- Weighted tally:
  Row 1: [NH Verdict] * 2 (MUST-CLEAR) = [contribution]
  Row 2: [NH Verdict] * 2 (MUST-CLEAR) = [contribution]
  Row 3: [NH Verdict] * 1 (ADVISORY) = [contribution]
  Weighted score = [sum]

Step 3 -- Threshold: [score] [> / = / <] 0 --> g_null = [FAIL / CONDITIONAL / PASS]

g_null(initial) = max(Step 1 floor, Step 3 result) = [FAIL / CONDITIONAL / PASS]
```

**g_null(initial)** *(derivable from NH Verdict column above without reading prose)*:
[FAIL / CONDITIONAL / PASS]

**Null hypothesis statement**: [What the team does today instead. One sentence.]

**Alternatives comparison table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DERIVATION RULE** *(per §9; applied to alternatives table at BRACKET CLOSING)*:
[State formula. Must be consistent with §19 g_null formula result above.]

**Challenge claims**:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1 -- specific inertia vector: switching cost, workaround viability, adoption risk] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
*Must equal §19 formula result for g_null(initial). If §19 result is CONDITIONAL, GOpen = CONDITIONAL.*
**GOpen Reason**: [One sentence. Reference the binding §19 formula result and the null hypothesis statement.]

**g_null(initial)** *(per §9 Stage 1 = GOpen; equal to §19 formula result)*: [PASS / CONDITIONAL / FAIL]

*GOpen, g_null(initial), and all CH-IDs carry forward to every downstream section.*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]

**CH-ID Response Table** *(mandatory per contract §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Domain Response | Status |
|-------|----------------------|----------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1 -- specific to this role's expertise frame] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph referencing GOpen explicitly.]

**Null hypothesis status**: [yes / partial / no -- one sentence.]

**Additional Findings** *(per §14: individual severity; per §11: §1 surface citation)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1 -- names specific artifact surface] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

*(Findings without §1:S-n citation are ADVISORY-ORPHAN per §11.)*

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**LENS COVERAGE TABLE** *(per §15 -- full lens.verify; Applicability from §17 ROLE MANIFEST)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|--------------------|
| 1 | [lens.verify entry 1 from this role's definition] | [HIGH/MEDIUM/LOW -- from §17 ROLE MANIFEST] | [ADDRESSED / OPEN] | [F-n or "no finding"] |
| 2 | [lens.verify entry 2] | [from §17] | [ADDRESSED / OPEN] | [F-n or "no finding"] |

*(OPEN on HIGH-applicability rows -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER per §15.)*

**Recommendation**: [One concrete action naming what to do and where in the artifact.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(Per §6: EXCLUDED from gate ledger.)*

**Applying §3a formula**:
```
G_domain_agg = worst([list G_domain verdicts]) = [PASS / CONDITIONAL / FAIL]
```

**g_null(post-domain)** *(per §9 Stage 2)*:
```
g_null(initial) = [copy]   G_domain_agg = [copy]
Apply Stage 2 formula --> g_null(post-domain) = [PASS / CONDITIONAL / FAIL]
```

---

## §3.8 CH-ID SATURATION CHECK

*(Per §6: EXCLUDED from gate ledger.)*

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED or N/A] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None"]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]
Received G_domain Aggregate: [copy from §3.5]
Received g_null(post-domain): [copy from §3.5]

**CH-ID Response Table** *(mandatory per §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph. Reference GOpen, G_domain Aggregate, and g_null(post-domain) explicitly.]

**Null hypothesis status**: [yes / partial / no -- one sentence referencing g_null(post-domain).]

**Additional Findings** *(per §14 and §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

*(Findings without §1:S-n citation are ADVISORY-ORPHAN per §11.)*

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**LENS COVERAGE TABLE** *(per §15 -- Applicability from §17 ROLE MANIFEST)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|--------------------|
| 1 | [lens.verify entry from this role] | [from §17] | [ADDRESSED / OPEN] | [F-n or "no finding"] |
| 2 | [entry] | [from §17] | [ADDRESSED / OPEN] | [F-n or "no finding"] |

*(OPEN on HIGH-applicability rows -> ADVISORY-OPEN-LENS per §15.)*

**Recommendation**: [One concrete action.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Applying §9 Stage 3 formula**:
```
g_null(post-domain) = [copy from §3.5]
G_lifecycle         = [copy from LIFECYCLE local ledger]
Apply Stage 3: if G_lifecycle=FAIL -> g_null(final)=FAIL
               if G_lifecycle=CONDITIONAL -> g_null(final)=max(g_null(post-domain), CONDITIONAL)
               if G_lifecycle=PASS -> g_null(final)=g_null(post-domain)
g_null(final) = [FAIL / CONDITIONAL / PASS]
```

**Revised NH Dimension Table** *(per §19 -- aggregate domain re-scores applied to §19 structure)*:

| # | Dimension | Tier | Aggregated Current-State | Aggregated Proposed-State | Delta | NH Verdict |
|---|-----------|------|--------------------------|--------------------------|-------|------------|
| 1 | [DIM-A from opening] | MUST-CLEAR | [agg score] | [agg score] | [Delta] | [NH Verdict] |
| 2 | [DIM-B] | MUST-CLEAR | [agg score] | [agg score] | [Delta] | [NH Verdict] |
| 3 | [DIM-C] | ADVISORY | [agg score] | [agg score] | [Delta] | [NH Verdict] |

**Applying §19 formula to revised table**:
```
Step 1 (MUST-CLEAR): [any OPPOSES-BUILD? result]
Step 2 (Weighted tally): [contributions and sum]
Step 3 (Threshold): [result]
g_null(closing formula) = [FAIL / CONDITIONAL / PASS]
```
*g_null(final) from §9 Stage 3 must be consistent with §19 closing table formula result.*

**Revised alternatives table** *(aggregate domain re-scores; for NULL HYPOTHESIS DERIVATION RULE)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Domain Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| [DIM-1] | [agg] | [agg] | [agg] | [one sentence] |
| [DIM-2] | [agg] | [agg] | [agg] | |

**Applying NULL HYPOTHESIS DERIVATION RULE to revised alternatives table**: [Result. One sentence.]

**Full CH-ID Saturation Check** *(per §8)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver (if needed) |
|-------|--------------|-----------------|-----------------|---------------------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
*Must equal g_null(final). Must be consistent with §19 closing table formula.*
**Override invoked**: [YES / NO]
**GClose Rationale**: [2-3 sentences. Reference g_null(final), §19 NH Verdict column trajectory (opening -> closing), CH-ID saturation, and null hypothesis trajectory (initial -> post-domain -> final).]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6.)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [DOMAIN F-1 / etc.] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [reference] | [COVERED / GAP] |

**Coverage gate signal** *(informational -- does not feed §3)*:
[COVERED / PARTIAL -- list GAP surfaces if PARTIAL]

**§11 ADVISORY-ORPHAN check**:
[List findings lacking §1:S-n citation, or "None"]

**Forced advisory items for ACTION ITEM REGISTER**:
- GAP surfaces (per §10): [list or "None"]
- ADVISORY-ORPHAN findings (per §11): [list or "None"]
- ADVISORY-OPEN-LENS items (per §15, HIGH-applicability OPEN rows): [list or "None"]
- ADVISORY-LENS-GAP items (per §18 domain gap-check): [carry forward from §18 output]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN_ROLE(S)] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Two reviewers with incompatible CH-ID responses or findings. If none: "None detected."]

**Convergence**: [CH-ID or concern raised by >= 2 reviewers. If none: "None detected."]

**§13 Progression Ledger**:
```
g_null(initial)     = [copy from BRACKET OPENING -- verified from §19 NH Verdict column]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING -- consistent with §19 closing table]
Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED /
                     LIFECYCLE-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

**Scope coverage** *(§10 signal)*: [Restate. If PARTIAL: list gap surfaces.]

---

## DISPOSITION

**Gate vector**:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula**:
```
GClose = FAIL? --> BLOCKED
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [BLOCKED / CONDITIONAL / READY]

**Primary Driver** *(per §16 -- derived mechanically)*:
[GClose / DOMAIN / LIFECYCLE / lowest-index CONDITIONAL gate / N/A]

**RESOLUTION REGISTRY** *(per §12)*:
[If CONDITIONAL: emit table with one row per CONDITIONAL gate.
 If not CONDITIONAL: "RESOLUTION REGISTRY: N/A -- disposition is [value]"]

---

## ACTION ITEM REGISTER

*(Copies local gate ledger rows verbatim per §6. Do not re-derive verdicts or classes.)*

| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [copy] | [copy] |
| DOMAIN -- [ROLE] | G_domain | [copy] | [copy] |
| LIFECYCLE -- [ROLE] | G_lifecycle | [copy] | [copy] |
| BRACKET CLOSING | GClose | [copy] | [copy] |

**Advisory items** *(ADVISORY-GAP, ADVISORY-ORPHAN, ADVISORY-OPEN-LENS, ADVISORY-LENS-GAP, waivers)*:
- [List all advisory items from §5.5 or "None"]
