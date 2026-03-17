# org-review Variations -- Round 12 (v11 rubric, 2026-03-16)
Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v11-2026-03-16.md

Prior round summary:
- R1--R8: V-05 climbed from 75 to 180/180 via bracket architecture, local ledger, §3a, §7 contracts.
- R9: V-05=195/195 (Perfect). C-27 (CH-ID saturation), C-28 (null progression), C-29 (scope coverage gate) extracted. §8+§9+§10 in preamble.
- R10: All five variants score 195/195 (rubric ceiling). Three excellence patterns extracted as C-30/C-31/C-32: §11 FINDING-SURFACE LINKAGE, §12 CONDITIONAL RESOLUTION REGISTRY, §13 g_null PROGRESSION LEDGER.
- R11: V-05=210/225 (v11 rubric). Three new axes: §14 FINDING SEVERITY AGGREGATION, §15 LENS EXHAUSTION, §16 PRIMARY DRIVER DERIVATION. V-05 R11 is the baseline for R12.

v11 rubric adds C-33/C-34/C-35 targeting V-02 R12 (canonical source):
  C-33: Lens Applicability Rating Pre-committed -- each LENS COVERAGE TABLE row carries HIGH/MEDIUM/LOW applicability per artifact domain.
  C-34: ADVISORY-GAP Domain Coverage Pre-committed -- gap-check names artifact domains with no HIGH-applicability reviewer; each -> ADVISORY-GAP in action register.
  C-35: Null Hypothesis Challenger Dimension Comparison Table -- challenger's null hypothesis evaluation uses structured current-state vs proposed-state table; g_null derivable from table values alone.

Round 12 strategy:
- Baseline: V-05 R11 (§1-§16) as non-negotiable base. All R12 variants inherit 210/225.
- R12 is a frontier-extension round: explore C-33+C-34+C-35 activation.
- V-01: single axis -- §17 NULL HYPOTHESIS DIMENSION TABLE CONTRACT (C-35 target). Add structured null hypothesis dimension table to BRACKET OPENING; g_null(initial) derivable from table values without reading prose.
- V-02: single axis -- §17 LENS COVERAGE APPLICABILITY PROTOCOL + §18 NULL HYPOTHESIS DIMENSION TABLE CONTRACT (C-33+C-34+C-35 combined -- canonical source per rubric). Integrated design: both protocols added together as a unified evidence pre-commitment layer.
- V-03: single axis -- §17 LENS COVERAGE APPLICABILITY PROTOCOL only (C-33+C-34 target). Role manifest extended with applicability ratings; LENS COVERAGE TABLE section emitted before BRACKET OPENING; domain gap-check -> ADVISORY-LENS-GAP.
- V-04: combination -- V-01 + V-03 axes (§17 LENS COVERAGE APPLICABILITY + §18 NULL HYPOTHESIS DIMENSION TABLE). Additive combination: V-03 §17 in position, V-01 §17 renumbered to §18.
- V-05: full integration -- V-04 with explicit §17<->§18 cross-reference. §17 applicability gap domains feed directly into §18 dimension table; §18 cites §17 domain ratings; creates unified lens-to-null-hypothesis traceability chain.

---

## V-01 -- Single Axis: Null Hypothesis Dimension Table (C-35)

**Variation axis**: §17 NULL HYPOTHESIS DIMENSION TABLE CONTRACT. BRACKET OPENING challenger uses a structured current-state vs proposed-state dimension table for null hypothesis evaluation. g_null(initial) is derived mechanically from the table rather than from a narrative strength label.

**Hypothesis**: Currently BRACKET OPENING states "Null hypothesis strength: HIGH/MEDIUM/LOW" as a narrative judgment. §17 replaces this with a pre-committed dimension table: at least 3 dimensions, each comparing the current state (team does nothing) against the proposed state (artifact is built). g_null(initial) is the mechanical output of a formula applied to the table's Delta column. A reviewer cannot assign g_null(initial) FAIL if the table shows majority dimensions favoring the null -- the table and formula are the constraint. This creates a new auditability dimension: g_null strength is now derivable from table values alone, distinct from C-16 (alternatives comparison table, which compares Status Quo/Build/Best-Alt) and from §9 (which governs progression through stages). C-35 is the evidence basis that feeds §9 Stage 1; §9 Stage 1 required g_null(initial) but did not constrain how it was derived.

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

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed heading, label, field, formula, or structural element. Do not add sections between pre-printed headers. If a field cannot be filled, write `[N/A -- reason]`.

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

§3 -- DISPOSITION ALGEBRA [IMMUTABLE -- evaluated at DISPOSITION section]
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
    SATURATED: CH-ID has a response in >= 1 DOMAIN section.
  Before BRACKET CLOSING executes, each CH-ID must satisfy:
    FULLY SATURATED: CH-ID has a response in >= 1 DOMAIN section AND in the LIFECYCLE section.
  A PASS verdict from BRACKET CLOSING is prohibited when any CH-ID is not FULLY SATURATED
  without a stated saturation waiver.
  Waiver format: "CH-XXX WAIVER: [LIFECYCLE not applicable -- one sentence reason]"
  Waivers are emitted in §3.8 and carried to ACTION ITEM REGISTER as ADVISORY.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  The null hypothesis verdict evolves through three stages. Apply the formula mechanically.

  Stage 1 -- g_null(initial) [emitted at BRACKET OPENING]:
    g_null(initial) = result of applying §17 NULL HYPOTHESIS DIMENSION TABLE formula.
    [If §17 is inactive: g_null(initial) = GOpen verdict directly.]

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
  the reviewer(s) that addressed it. Coverage rules:
    COVERED: surface named in >= 1 finding from >= 1 reviewer section.
    GAP:     surface not named in any reviewer finding.
  Gap handling:
    GAP surfaces receive forced LOW advisory status.
    GAP surfaces are added to ACTION ITEM REGISTER as ADVISORY-GAP items.
    Attribution: "SCOPE COVERAGE GATE / [surface name] / not addressed by any reviewer"
  Gate signal (informational -- does not feed §3 formula):
    COVERED: all §1 IN-SCOPE surfaces addressed.
    PARTIAL: >= 1 §1 IN-SCOPE surface not addressed.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding produced by a DOMAIN or LIFECYCLE reviewer section must carry a §1 IN-SCOPE
  surface citation in the format: "[§1:S-n] finding text"
  A finding without a valid §1 surface citation is classified ADVISORY-ORPHAN.
  §5.5 (top-down: scope surface -> findings) and §11 (bottom-up: finding -> scope surface)
  form a bidirectional trace. Satisfying §5.5 does not satisfy §11, and vice versa.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  When DISPOSITION = CONDITIONAL, the DISPOSITION section emits a RESOLUTION REGISTRY table:
    | Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
  One row per CONDITIONAL gate. Resolution Owner = role responsible for closing the condition.
  Resolution Criterion = a falsifiable test observable from outside the review process.
  Status = OPEN at review time.
  If DISPOSITION = READY or BLOCKED, write: "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  In CROSS-ROLE SIGNALS, a §13 PROGRESSION LEDGER sub-section assembles the three g_null values:
    g_null(initial)     = [copy from BRACKET OPENING]
    g_null(post-domain) = [copy from §3.5]
    g_null(final)       = [copy from BRACKET CLOSING]
    Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED /
                         LIFECYCLE-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
  Trajectory derivation (apply mechanically):
    MONOTONIC-PASS:      all three = PASS
    MONOTONIC-FAIL:      all three = FAIL
    DOMAIN-DEGRADED:     g_null(post-domain) worse than g_null(initial)
    LIFECYCLE-DEGRADED:  g_null(final) worse than g_null(post-domain)
    DOMAIN-RECOVERED:    g_null(post-domain) better than g_null(initial)
    LIFECYCLE-RECOVERED: g_null(final) better than g_null(post-domain)
  This ledger is informational only. No gate ledger row emitted.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Within each DOMAIN and LIFECYCLE reviewer section, each finding entry carries an individual
  severity tag. Additional Findings are presented as a table:
    | # | §1 Surface | Finding | Severity |
  Section Severity is derived mechanically from this table:
    Section Severity = worst(all finding severities in this section).
    Precedence: HIGH > MEDIUM > LOW.
    If no findings: Section Severity = LOW.
  Do not assign Section Severity editorially. Apply the formula above and state the result.
  Gate verdicts (G_domain, G_lifecycle) are derived from evidence quality; Section Severity is
  a separate signal. A HIGH Section Severity finding in a PASS gate is not contradictory.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN and LIFECYCLE section must address ALL entries from the role's lens.verify.
  After findings, emit LENS COVERAGE TABLE:
    | # | lens.verify Entry | Status | Finding Reference |
    Status values: ADDRESSED / OPEN.
  OPEN entries -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.
  Lens exhaustion is a completeness audit, not a gate condition.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  Primary Driver of the disposition is derived by the following precedence rule.
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

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]
  BRACKET OPENING challenger evaluates the null hypothesis using a structured dimension comparison
  table before stating challenge claims. The table compares current state (team does nothing:
  null hypothesis holds) against proposed state (artifact is built: null hypothesis is defeated).

  Table format:
    | Dimension | Current State (null holds) | Proposed State (artifact built) | Delta | g_null Signal |
  Minimum 3 dimensions. Dimensions should name concrete capabilities, costs, or workflow states
  that distinguish the null scenario from the proposal scenario.

  g_null Signal values:
    WEAKENS NULL    = proposed state is meaningfully better on this dimension; null is harder to defend.
    NEUTRAL         = no material difference between current and proposed on this dimension.
    STRENGTHENS NULL = current state is acceptable or better on this dimension; null is defensible.

  g_null DERIVATION FORMULA (apply mechanically to table; emit result as g_null(initial)):
    Count WEAKENS NULL, NEUTRAL, STRENGTHENS NULL signals across all table rows.
    g_null(initial) = FAIL        if WEAKENS NULL is the majority signal (> 50% of rows).
    g_null(initial) = CONDITIONAL if no majority signal (no value > 50% of rows).
    g_null(initial) = PASS        if STRENGTHENS NULL or NEUTRAL is the majority signal (> 50% of rows).

  §17 table is distinct from the §3a alternatives comparison table (Status Quo vs Build vs Best-Alt).
  §17 compares the null scenario directly against the proposal; §3a compares three alternatives.
  Both tables are present. §17 table is emitted first in BRACKET OPENING.

  §9 Stage 1 g_null(initial) is the output of §17 formula, not the GOpen verdict.
  GOpen verdict is derived from the challenge claims and §17 output combined.

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

**Null hypothesis dimension table** *(per §17 -- g_null(initial) derivable from table values alone)*:

| Dimension | Current State (null holds) | Proposed State (artifact built) | Delta | g_null Signal |
|-----------|---------------------------|--------------------------------|-------|---------------|
| [DIM-1 -- name the key capability/workflow/cost dimension] | [current value or state] | [proposed value or state] | [FAVORS-BUILD / NEUTRAL / FAVORS-NULL] | [WEAKENS NULL / NEUTRAL / STRENGTHENS NULL] |
| [DIM-2] | [current] | [proposed] | [FAVORS-BUILD / NEUTRAL / FAVORS-NULL] | [WEAKENS NULL / NEUTRAL / STRENGTHENS NULL] |
| [DIM-3] | [current] | [proposed] | [FAVORS-BUILD / NEUTRAL / FAVORS-NULL] | [WEAKENS NULL / NEUTRAL / STRENGTHENS NULL] |

*(Add rows as needed. Each dimension is an independent signal. Do not aggregate editorially.)*

**Applying §17 formula**:
```
WEAKENS NULL count    = [n]
NEUTRAL count         = [n]
STRENGTHENS NULL count = [n]
Total rows = [n]
Majority signal = [WEAKENS NULL / NEUTRAL / STRENGTHENS NULL / none (no majority)]
g_null(initial) = [FAIL / CONDITIONAL / PASS]
```

**Alternatives comparison table** *(per §3a -- >= 3 dimensions; distinct from §17 table above)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DERIVATION RULE** *(pre-committed per §9; applied mechanically at BRACKET CLOSING)*:
  [Formula mapping table dimensions to g_null verdict. State before any reviewer runs.]

**Challenge claims** *(assign CH-IDs per §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction. One sentence.] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)** *(per §17 formula above -- not equal to GOpen unless formula produces same result)*: [PASS / CONDITIONAL / FAIL]

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
**Section Severity**: [HIGH / MEDIUM / LOW] <- mechanical result per §14; do not assign editorially.

**Lens Coverage Table** *(per §15 -- ALL lens.verify entries from role definition)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|-------------------|
| Q-1 | [Full text of lens.verify entry 1] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text of lens.verify entry 2] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-3 | [Full text if present] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(Add rows for all lens.verify entries. OPEN entries -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence. If CONDITIONAL: name condition. If FAIL: name gap.]

*(For `--depth deep`: repeat labeled DOMAIN-2, DOMAIN-3. Each emits own local ledger row, domain re-score, and lens coverage table.)*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6 -- this section produces no verdict.)*

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

**Decision-readiness assessment**: [One paragraph referencing GOpen, G_domain Aggregate, and g_null(post-domain) explicitly.]

**Null hypothesis status**: [yes / partial / no -- reference g_null(post-domain). One sentence.]

**Additional Findings** *(per §14: per-finding severity; per §11: each finding cites §1 surface)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1 -- commitment, program, or decision concerns.] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

*(Findings without a valid §1:S-n citation are ADVISORY-ORPHAN per §11.)*

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] <- mechanical result per §14; do not assign editorially.

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

**Revised alternatives table** *(aggregate domain re-scores; apply NULL HYPOTHESIS DERIVATION RULE)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Domain Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| [DIM-1] | [agg] | [agg] | [agg] | [reason] |
| [DIM-2] | [agg] | [agg] | [agg] | |
| [DIM-3] | [agg] | [agg] | [agg] | |

**Applying NULL HYPOTHESIS DERIVATION RULE to revised table**: [Result. One sentence.]

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

**GClose Rationale**: [2-3 sentences. Reference g_null(final), CH-ID saturation, and null hypothesis trajectory (initial -> post-domain -> final).]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6. Runs after BRACKET CLOSING, before GATE VECTOR TABLE. Applies §10 and cross-checks §11.)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [DOMAIN F-n / etc.] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [reference] | [COVERED / GAP] |

**Coverage gate signal** *(§10 -- informational)*: [COVERED -- all surfaces addressed | PARTIAL -- [N] surface(s) not addressed]

**§11 ADVISORY-ORPHAN check** *(findings lacking §1 citation)*:
- [Finding reference: "FINDING-SURFACE LINKAGE / [section] / F-n / no valid §1:S-n citation" or "None"]

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
g_null(initial)     = [copy from BRACKET OPENING §17 formula]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING]
Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED /
                     LIFECYCLE-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

**Scope coverage** *(§10 gate signal)*: [Restate. If PARTIAL: list surfaces. If COVERED: "None -- full in-scope surface reviewed."]

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

*Copy all Local Gate Ledger rows from BRACKET OPENING, DOMAIN(s), LIFECYCLE, and BRACKET CLOSING verbatim. Do not re-derive Gate Verdict or Class. Append: CH-ID PARTIAL/HOLDS rows, §8 waiver rows (ADVISORY), §10 ADVISORY-GAP rows from §5.5, §11 ADVISORY-ORPHAN rows from §5.5, §15 ADVISORY-OPEN-LENS rows.*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [copy from local ledger] | [copy] | [copy] | [copy] | [What must be done] | [ROLE_NAME] | [Criterion] |
| CH-001 | -- | -- | [BLOCKED/CONDITIONAL/ADVISORY] | [Item from CH-ID status] | [ROLE_NAME] | [Criterion] |
| §8 WAIVER | -- | -- | ADVISORY | [Waiver text if any] | [ROLE_NAME] | N/A |
| §10 SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [Surface not addressed] | [ROLE_NAME] | [Criterion] |
| §11 FINDING-SURFACE LINKAGE | -- | -- | ADVISORY-ORPHAN | [Finding with no §1 citation] | [ROLE_NAME] | [Criterion] |
| §15 LENS EXHAUSTION | -- | -- | ADVISORY-OPEN-LENS | [Unanswered lens.verify entry] | [ROLE_NAME] | [Criterion] |
| -- | -- | -- | ADVISORY-OBS | [Advisory observation] | [ROLE_NAME] | [Criterion] |

*FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY*
*ADVISORY-GAP:§10 | ADVISORY-ORPHAN:§11 | ADVISORY-OPEN-LENS:§15*

---

**Artifact to review:**

{{artifact}}
```

---

## V-02 -- Single Axis: Lens Coverage Applicability + Null Hypothesis Dimension Table (C-33+C-34+C-35) [Canonical Source]

**Variation axis**: §17 LENS COVERAGE APPLICABILITY PROTOCOL + §18 NULL HYPOTHESIS DIMENSION TABLE CONTRACT. Integrated design treating both as a unified evidence pre-commitment layer. §17 pre-commits applicability ratings for each reviewer x artifact domain pair before reviewer sections execute; domain gap-check identifies ADVISORY-LENS-GAP domains. §18 adds structured null hypothesis dimension table in BRACKET OPENING; g_null(initial) derivable from table values alone.

**Hypothesis**: C-33+C-34+C-35 can be activated simultaneously by adding §17+§18 to the V-05 R11 base. §17 activates at role-selection time (before BRACKET OPENING), providing artifact-domain-level coverage accountability. §18 activates inside BRACKET OPENING, providing null hypothesis evaluation accountability. They are structurally independent with no shared fields. Together they complete the pre-commitment audit chain for two previously-editorial steps: domain coverage selection (§17) and null hypothesis strength derivation (§18). Target: 225/225.

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

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed heading, label, field, formula, or structural element. Do not add sections between pre-printed headers. If a field cannot be filled, write `[N/A -- reason]`.

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
  (Add rows. Be exhaustive. Cited in §5.5, §11, and §17 LENS COVERAGE APPLICABILITY PROTOCOL.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]
Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks commitment. MEDIUM=Conditions commitment. LOW=Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts). FAIL>CONDITIONAL>PASS.
  BRACKET CLOSING applies mechanically. No editorial re-assessment.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim receives a CH-ID. Every downstream section carries CH-ID response table.
  PASS prohibited if any CH-ID shows OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section, after verdict stated.
  Assembly: ACTION ITEM REGISTER copies verbatim. Do not re-derive.
  EXCLUDED (no ledger row): §3.5, §3.8, §5.5, §1.5.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.   ROLE MANIFEST
  1.5. LENS COVERAGE TABLE            [excluded from gate ledger per §6]
  2.   BRACKET OPENING
  3.   DOMAIN(s)
  3.5. DOMAIN-AGGREGATE CHECKPOINT    [excluded per §6]
  3.8. CH-ID SATURATION CHECK         [excluded per §6]
  4.   LIFECYCLE
  5.   BRACKET CLOSING
  5.5. SCOPE COVERAGE RECONCILIATION  [excluded per §6]
  6.   GATE VECTOR TABLE
  7.   CROSS-ROLE SIGNALS
  8.   DISPOSITION
  9.   ACTION ITEM REGISTER
  LENS COVERAGE TABLE must follow ROLE MANIFEST and precede BRACKET OPENING.
  LIFECYCLE precedes BRACKET CLOSING.
  CH-ID SATURATION CHECK precedes LIFECYCLE.
  SCOPE COVERAGE RECONCILIATION precedes GATE VECTOR TABLE.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID has DOMAIN response before LIFECYCLE.
  FULLY SATURATED: CH-ID has DOMAIN+LIFECYCLE response before BRACKET CLOSING.
  PASS from BRACKET CLOSING prohibited without full saturation or stated waiver.
  Waiver: "CH-XXX WAIVER: [LIFECYCLE not applicable -- reason]" -> ADVISORY in register.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = result of §18 formula. [BRACKET OPENING]
  Stage 2: FAIL->FAIL | CONDITIONAL->max(initial,CONDITIONAL) | PASS->g_null(initial). [§3.5]
  Stage 3: FAIL->FAIL | CONDITIONAL->max(post-domain,CONDITIONAL) | PASS->g_null(post-domain). [BRACKET CLOSING]
  GClose must equal g_null(final). Deviation requires: "g_null OVERRIDE: [reason]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps IN-SCOPE surfaces to reviewer findings. COVERED/GAP.
  GAP -> ADVISORY-GAP in register. Gate signal COVERED/PARTIAL is informational.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE finding carries "[§1:S-n]" citation. No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit RESOLUTION REGISTRY:
    | Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status=OPEN |
  Otherwise: "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS contains §13 PROGRESSION LEDGER:
    g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory
  Trajectory: MONOTONIC-PASS/FAIL | DOMAIN-DEGRADED/RECOVERED | LIFECYCLE-DEGRADED/RECOVERED.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Findings as table: | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all finding severities). HIGH>MEDIUM>LOW. No findings -> LOW.
  Do not assign editorially. Gate verdicts independent of Section Severity.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE section addresses ALL lens.verify entries.
  After findings emit LENS COVERAGE TABLE (§15): | # | lens.verify Entry | Status | Finding Reference |
  OPEN entries -> ADVISORY-OPEN-LENS in register.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  PRIMARY DRIVER DERIVATION RULE (apply at DISPOSITION; do not assign editorially):
    1.GClose=FAIL->BRACKET CLOSING  2.G_domain_agg=FAIL->DOMAIN  3.G_lifecycle=FAIL->LIFECYCLE
    4.GOpen=FAIL->BRACKET OPENING   5.GClose=COND->BRACKET CLOSING  6.G_domain_agg=COND->DOMAIN
    7.G_lifecycle=COND->LIFECYCLE   8.GOpen=COND->BRACKET OPENING  9.all PASS->N/A
  Emit: "Applying §16 rule: [rule# + reason]" | "Primary Driver: [value]"

§17 -- LENS COVERAGE APPLICABILITY PROTOCOL [IMMUTABLE]
  After ROLE MANIFEST, at §1.5 LENS COVERAGE TABLE, pre-commit applicability ratings for each
  reviewer across each artifact domain (derived from §1 IN-SCOPE surfaces).
  Table format: | Artifact Domain | Reviewer | Lens Applicability | Rationale |
  One row per (artifact domain x reviewer) pair.
  Lens Applicability:
    HIGH   = this reviewer's primary lens directly addresses this domain.
    MEDIUM = partial coverage; incidental findings expected.
    LOW    = tangential; outside this reviewer's primary frame.
  Ratings pre-committed BEFORE reviewer sections execute.
  They are the rated basis for ADDRESSED/OPEN in CH-ID response tables.
  Domain gap-check (apply mechanically):
    For each artifact domain: if no reviewer carries HIGH applicability ->
      classify ADVISORY-LENS-GAP.
      Add to ACTION ITEM REGISTER: "LENS COVERAGE APPLICABILITY / [§1:S-n domain] /
      no HIGH-applicability reviewer assigned" | Class: ADVISORY-LENS-GAP.
  Write "No ADVISORY-LENS-GAP domains." if all domains have at least one HIGH reviewer.

§18 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]
  BRACKET OPENING uses a structured dimension comparison table for null hypothesis evaluation.
  Table format: | Dimension | Current State (null holds) | Proposed State (artifact built) | Delta | g_null Signal |
  Minimum 3 dimensions. Each dimension names a concrete capability, cost, or workflow state.
  g_null Signal values:
    WEAKENS NULL     = proposed is materially better; null harder to defend.
    NEUTRAL          = no material difference.
    STRENGTHENS NULL = current state acceptable or better; null is defensible.
  g_null DERIVATION FORMULA (apply mechanically; result = g_null(initial)):
    g_null(initial) = FAIL        if WEAKENS NULL > 50% of rows (null defeated).
    g_null(initial) = CONDITIONAL if no value exceeds 50% (mixed signals).
    g_null(initial) = PASS        if WEAKENS NULL <= 50% and NEUTRAL+STRENGTHENS > WEAKENS.
  §18 table is DISTINCT from the alternatives comparison table (Status Quo/Build/Best-Alt):
    §18 = null scenario vs proposal (two-way comparison).
    Alternatives table = three-strategy comparison.
  §18 table emitted first in BRACKET OPENING. §9 Stage 1 g_null(initial) = §18 formula result.
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

*After completing this manifest, proceed to §1.5 LENS COVERAGE TABLE before BRACKET OPENING.*

---
## §1.5 LENS COVERAGE TABLE *(per §17 -- emitted after ROLE MANIFEST, before BRACKET OPENING)*

*(List artifact domains from §1 IN-SCOPE surfaces. For each domain, rate each reviewer's applicability. Apply domain gap-check per §17.)*

| Artifact Domain | Reviewer | Lens Applicability (HIGH/MEDIUM/LOW) | Rationale |
|-----------------|----------|--------------------------------------|-----------|
| [§1:S-1 -- domain name] | [CHALLENGER_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-1 -- domain name] | [DOMAIN_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-1 -- domain name] | [LIFECYCLE_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-2 -- domain name] | [CHALLENGER_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-2 -- domain name] | [DOMAIN_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-2 -- domain name] | [LIFECYCLE_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-3 -- domain name] | [CHALLENGER_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-3 -- domain name] | [DOMAIN_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-3 -- domain name] | [LIFECYCLE_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |

*(Add rows for all §1 IN-SCOPE domains x all assigned reviewers.)*

**Domain gap-check** *(per §17 -- apply mechanically)*:

| Artifact Domain | Has HIGH-Applicability Reviewer? | Classification |
|-----------------|----------------------------------|----------------|
| [§1:S-1 domain] | [YES -- [ROLE_NAME]] / [NO] | [OK / ADVISORY-LENS-GAP] |
| [§1:S-2 domain] | [YES -- [ROLE_NAME]] / [NO] | [OK / ADVISORY-LENS-GAP] |
| [§1:S-3 domain] | [YES -- [ROLE_NAME]] / [NO] | [OK / ADVISORY-LENS-GAP] |

**ADVISORY-LENS-GAP domains**: [List each or "None -- all domains have HIGH-applicability reviewer."]
*Each ADVISORY-LENS-GAP domain -> ACTION ITEM REGISTER per §17.*

---
## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]

**Null hypothesis dimension table** *(per §18 -- g_null(initial) derivable from table values alone)*:

| Dimension | Current State (null holds) | Proposed State (artifact built) | Delta | g_null Signal |
|-----------|---------------------------|--------------------------------|-------|---------------|
| [DIM-1] | [current value or state] | [proposed value or state] | [FAVORS-BUILD / NEUTRAL / FAVORS-NULL] | [WEAKENS NULL / NEUTRAL / STRENGTHENS NULL] |
| [DIM-2] | [current] | [proposed] | [FAVORS-BUILD / NEUTRAL / FAVORS-NULL] | [WEAKENS NULL / NEUTRAL / STRENGTHENS NULL] |
| [DIM-3] | [current] | [proposed] | [FAVORS-BUILD / NEUTRAL / FAVORS-NULL] | [WEAKENS NULL / NEUTRAL / STRENGTHENS NULL] |

*(Add rows as needed. Each dimension is an independent signal.)*

**Applying §18 formula**:
```
WEAKENS NULL count     = [n]
NEUTRAL count          = [n]
STRENGTHENS NULL count = [n]
Majority signal = [WEAKENS NULL / NEUTRAL+STRENGTHENS / none (tied)]
g_null(initial) = [FAIL / CONDITIONAL / PASS]
```

**Alternatives comparison table** *(per §3a -- distinct from §18 table above)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DERIVATION RULE** *(pre-committed per §9; applied mechanically at BRACKET CLOSING)*:
  [Formula mapping table dimensions to g_null verdict. State before any reviewer runs.]

**Challenge claims** *(assign CH-IDs per §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction.] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)** *(per §18 formula above)*: [PASS / CONDITIONAL / FAIL]

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

**Domain re-score** *(same dimensions as BRACKET OPENING alternatives table)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| [DIM-1] | [revised] | [revised] | [revised] | [reason] |
| [DIM-2] | [revised] | [revised] | [revised] | |
| [DIM-3] | [revised] | [revised] | [revised] | |

**Additional Findings** *(per §14: per-finding severity; per §11: each finding cites §1 surface)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-3 | [§1:S-n -- optional] | [FINDING_3] | [HIGH / MEDIUM / LOW] |

*(Findings without §1:S-n citation are ADVISORY-ORPHAN per §11.)*

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] <- mechanical result; do not assign editorially.

**Lens Coverage Table** *(per §15 -- ALL lens.verify entries)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|-------------------|
| Q-1 | [entry 1] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [entry 2] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-3 | [entry 3 if present] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(OPEN entries -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*(For `--depth deep`: repeat DOMAIN-2, DOMAIN-3. Each emits local ledger row, domain re-score, lens coverage table.)*

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
**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

**Applying §9 Stage 2 formula**:
```
g_null(initial)=[copy] | G_domain_agg=[copy]
  FAIL->FAIL | CONDITIONAL->max(initial,CONDITIONAL) | PASS->g_null(initial)
g_null(post-domain) = [FAIL / CONDITIONAL / PASS]
```
**g_null(post-domain)**: [FAIL / CONDITIONAL / PASS]

*Both carry forward to §3.8, LIFECYCLE, and BRACKET CLOSING.*

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger per §6.)*

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | [copy] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED -- N/A] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None"]

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

**Decision-readiness assessment**: [One paragraph referencing GOpen, G_domain Aggregate, and g_null(post-domain) explicitly.]

**Null hypothesis status**: [yes / partial / no -- reference g_null(post-domain). One sentence.]

**Additional Findings** *(per §14 + §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] <- mechanical result.

**Lens Coverage Table** *(per §15)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|-------------------|
| Q-1 | [entry 1] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [entry 2] | [ADDRESSED / OPEN] | [F-n or N/A] |

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

**Applying §9 Stage 3 formula**:
```
g_null(post-domain)=[copy] | G_lifecycle=[copy]
  FAIL->FAIL | CONDITIONAL->max(post-domain,CONDITIONAL) | PASS->g_null(post-domain)
g_null(final) = [FAIL / CONDITIONAL / PASS]
```
**g_null(final)**: [FAIL / CONDITIONAL / PASS]

**Revised alternatives table** *(aggregate domain re-scores; apply NULL HYPOTHESIS DERIVATION RULE)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Domain Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| [DIM-1] | [agg] | [agg] | [agg] | [reason] |
| [DIM-2] | [agg] | [agg] | [agg] | |
| [DIM-3] | [agg] | [agg] | [agg] | |

**Applying NULL HYPOTHESIS DERIVATION RULE to revised table**: [Result. One sentence.]

**Full CH-ID Saturation Check** *(per §8)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver |
|-------|--------------|-----------------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or WAIVER] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or WAIVER] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or WAIVER] |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [All defeated, or list gaps.]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A -- formula applied | or: justification one sentence]

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts per §3.

**GClose Rationale**: [2-3 sentences. Reference g_null(final), CH-ID saturation, and trajectory.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6. Runs after BRACKET CLOSING, before GATE VECTOR TABLE.)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [F-n] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [reference] | [COVERED / GAP] |

**Coverage gate signal**: [COVERED / PARTIAL -- list surfaces if PARTIAL]
**§11 ADVISORY-ORPHAN check**: [list findings without §1:S-n or "None"]

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

**Conflicts**: [Incompatible CH-ID responses or findings. If none: "None detected."]

**Convergence**: [CH-ID or concern named by 2+ reviewers. Name it and explain confidence.]

**§13 Progression Ledger** *(informational; no ledger row)*:
```
g_null(initial)     = [copy from BRACKET OPENING]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING]
Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED /
                     LIFECYCLE-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

**Scope coverage** *(§10 gate signal)*: [COVERED / PARTIAL]
**§17 Lens coverage summary**: [Restate ADVISORY-LENS-GAP domains from §1.5, if any. If none: "No ADVISORY-LENS-GAP domains."]

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
- Trajectory: [from §13]

**Scope coverage** *(§10)*: [COVERED / PARTIAL]

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**RESOLUTION REGISTRY** *(per §12 -- emit if CONDITIONAL; otherwise write N/A line)*:

| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [verbatim condition] | [ROLE_NAME] | [falsifiable criterion] | OPEN |

*RESOLUTION REGISTRY: N/A -- disposition is [READY/BLOCKED]* <- delete if CONDITIONAL

**Applying §16 PRIMARY DRIVER DERIVATION RULE**:
```
GClose=[_], G_domain_agg=[_], G_lifecycle=[_], GOpen=[_]
Rule fired: [rule number + reason]
```
**Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**Conditions** *(if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]

**Blocker** *(if BLOCKED)*: [Specific finding from the FAIL gate.]

---
## ACTION ITEM REGISTER

*Copy all Local Gate Ledger rows from BRACKET OPENING, DOMAIN(s), LIFECYCLE, and BRACKET CLOSING verbatim. Do not re-derive Gate Verdict or Class. Append: CH-ID PARTIAL/HOLDS rows, §8 waiver rows, §10 ADVISORY-GAP rows from §5.5, §11 ADVISORY-ORPHAN rows from §5.5, §15 ADVISORY-OPEN-LENS rows, §17 ADVISORY-LENS-GAP rows from §1.5.*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [copy from local ledger] | [copy] | [copy] | [copy] | [What must be done] | [ROLE_NAME] | [Criterion] |
| CH-001 | -- | -- | [BLOCKED/CONDITIONAL/ADVISORY] | [Item from CH-ID] | [ROLE_NAME] | [Criterion] |
| §8 WAIVER | -- | -- | ADVISORY | [Waiver text] | [ROLE_NAME] | N/A |
| §10 SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [Surface not addressed] | [ROLE_NAME] | [Criterion] |
| §11 FINDING-SURFACE LINKAGE | -- | -- | ADVISORY-ORPHAN | [Finding with no §1 citation] | [ROLE_NAME] | [Criterion] |
| §15 LENS EXHAUSTION | -- | -- | ADVISORY-OPEN-LENS | [Unanswered lens.verify entry] | [ROLE_NAME] | [Criterion] |
| §17 LENS COVERAGE APPLICABILITY | -- | -- | ADVISORY-LENS-GAP | [Domain with no HIGH-applicability reviewer] | [ROLE_NAME] | [Assign HIGH-applicability reviewer or accept gap] |
| -- | -- | -- | ADVISORY-OBS | [Advisory observation] | [ROLE_NAME] | [Criterion] |

*FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY*
*ADVISORY-GAP:§10 | ADVISORY-ORPHAN:§11 | ADVISORY-OPEN-LENS:§15 | ADVISORY-LENS-GAP:§17*

---

**Artifact to review:**

{{artifact}}
```

---
## V-03 -- Single Axis: Lens Coverage Applicability Protocol (C-33+C-34)

**Variation axis**: §17 LENS COVERAGE APPLICABILITY PROTOCOL only. Adds applicability ratings (HIGH/MEDIUM/LOW) to the role-selection phase for each reviewer x artifact domain pair. After the LENS COVERAGE TABLE is built, a domain gap-check identifies artifact domains with no HIGH-applicability reviewer and classifies each as ADVISORY-LENS-GAP in the action register. No null hypothesis dimension table (§18 not active).

**Hypothesis**: C-33 and C-34 can be activated independently of C-35. §17 is structurally self-contained at the role-selection phase. The LENS COVERAGE TABLE lives between ROLE MANIFEST and BRACKET OPENING, does not affect any gate verdicts, and produces its own advisory output. If C-33+C-34 score independently, V-03 + V-01 in combination should equal V-02. This split also tests whether C-33+C-34 are separable from C-35 in scoring.

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

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed heading, label, field, formula, or structural element. Do not add sections between pre-printed headers. If a field cannot be filled, write `[N/A -- reason]`.

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
  (Add rows. Be exhaustive. Cited in §5.5, §11, and §17 LENS COVERAGE APPLICABILITY PROTOCOL.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]
Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks commitment. MEDIUM=Conditions commitment. LOW=Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts). FAIL>CONDITIONAL>PASS.
  BRACKET CLOSING applies mechanically. No editorial re-assessment.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim receives a CH-ID. Every downstream section carries CH-ID response table.
  PASS prohibited if any CH-ID shows OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section, after verdict stated.
  Assembly: ACTION ITEM REGISTER copies verbatim. Do not re-derive.
  EXCLUDED (no ledger row): §3.5, §3.8, §5.5, §1.5.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.   ROLE MANIFEST
  1.5. LENS COVERAGE TABLE            [excluded from gate ledger per §6]
  2.   BRACKET OPENING
  3.   DOMAIN(s)
  3.5. DOMAIN-AGGREGATE CHECKPOINT    [excluded per §6]
  3.8. CH-ID SATURATION CHECK         [excluded per §6]
  4.   LIFECYCLE
  5.   BRACKET CLOSING
  5.5. SCOPE COVERAGE RECONCILIATION  [excluded per §6]
  6.   GATE VECTOR TABLE
  7.   CROSS-ROLE SIGNALS
  8.   DISPOSITION
  9.   ACTION ITEM REGISTER
  LENS COVERAGE TABLE must follow ROLE MANIFEST and precede BRACKET OPENING.
  LIFECYCLE precedes BRACKET CLOSING.
  CH-ID SATURATION CHECK precedes LIFECYCLE.
  SCOPE COVERAGE RECONCILIATION precedes GATE VECTOR TABLE.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID has DOMAIN response before LIFECYCLE.
  FULLY SATURATED: CH-ID has DOMAIN+LIFECYCLE response before BRACKET CLOSING.
  PASS from BRACKET CLOSING prohibited without full saturation or stated waiver.
  Waiver: "CH-XXX WAIVER: [LIFECYCLE not applicable -- reason]" -> ADVISORY in register.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = GOpen verdict directly. [BRACKET OPENING; §18 inactive]
  Stage 2: FAIL->FAIL | CONDITIONAL->max(initial,CONDITIONAL) | PASS->g_null(initial). [§3.5]
  Stage 3: FAIL->FAIL | CONDITIONAL->max(post-domain,CONDITIONAL) | PASS->g_null(post-domain). [BRACKET CLOSING]
  GClose must equal g_null(final). Deviation requires: "g_null OVERRIDE: [reason]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps IN-SCOPE surfaces to reviewer findings. COVERED/GAP.
  GAP -> ADVISORY-GAP in register. Gate signal COVERED/PARTIAL is informational.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE finding carries "[§1:S-n]" citation. No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit RESOLUTION REGISTRY:
    | Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status=OPEN |
  Otherwise: "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS contains §13 PROGRESSION LEDGER:
    g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory
  Trajectory: MONOTONIC-PASS/FAIL | DOMAIN-DEGRADED/RECOVERED | LIFECYCLE-DEGRADED/RECOVERED.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Findings as table: | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all finding severities). HIGH>MEDIUM>LOW. No findings -> LOW.
  Do not assign editorially. Gate verdicts independent of Section Severity.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE section addresses ALL lens.verify entries.
  After findings emit LENS COVERAGE TABLE (§15): | # | lens.verify Entry | Status | Finding Reference |
  OPEN entries -> ADVISORY-OPEN-LENS in register.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  PRIMARY DRIVER DERIVATION RULE (apply at DISPOSITION; do not assign editorially):
    1.GClose=FAIL->BRACKET CLOSING  2.G_domain_agg=FAIL->DOMAIN  3.G_lifecycle=FAIL->LIFECYCLE
    4.GOpen=FAIL->BRACKET OPENING   5.GClose=COND->BRACKET CLOSING  6.G_domain_agg=COND->DOMAIN
    7.G_lifecycle=COND->LIFECYCLE   8.GOpen=COND->BRACKET OPENING  9.all PASS->N/A
  Emit: "Applying §16 rule: [rule# + reason]" | "Primary Driver: [value]"

§17 -- LENS COVERAGE APPLICABILITY PROTOCOL [IMMUTABLE]
  After ROLE MANIFEST, at §1.5 LENS COVERAGE TABLE, pre-commit applicability ratings for each
  reviewer across each artifact domain (derived from §1 IN-SCOPE surfaces).
  Table format: | Artifact Domain | Reviewer | Lens Applicability | Rationale |
  One row per (artifact domain x reviewer) pair.
  Lens Applicability:
    HIGH   = this reviewer's primary lens directly addresses this domain.
    MEDIUM = partial coverage; incidental findings expected.
    LOW    = tangential; outside this reviewer's primary frame.
  Ratings pre-committed BEFORE reviewer sections execute.
  They are the rated basis for ADDRESSED/OPEN in CH-ID response tables.
  Domain gap-check (apply mechanically):
    For each artifact domain: if no reviewer carries HIGH applicability ->
      classify ADVISORY-LENS-GAP.
      Add to ACTION ITEM REGISTER: "LENS COVERAGE APPLICABILITY / [§1:S-n domain] /
      no HIGH-applicability reviewer assigned" | Class: ADVISORY-LENS-GAP.
  Write "No ADVISORY-LENS-GAP domains." if all domains have at least one HIGH reviewer.

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

*After completing this manifest, proceed to §1.5 LENS COVERAGE TABLE before BRACKET OPENING.*

---
## §1.5 LENS COVERAGE TABLE *(per §17 -- emitted after ROLE MANIFEST, before BRACKET OPENING)*

*(List artifact domains from §1 IN-SCOPE surfaces. For each domain, rate each reviewer's applicability. Apply domain gap-check per §17.)*

| Artifact Domain | Reviewer | Lens Applicability (HIGH/MEDIUM/LOW) | Rationale |
|-----------------|----------|--------------------------------------|-----------|
| [§1:S-1 -- domain name] | [CHALLENGER_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-1 -- domain name] | [DOMAIN_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-1 -- domain name] | [LIFECYCLE_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-2 -- domain name] | [CHALLENGER_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-2 -- domain name] | [DOMAIN_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-2 -- domain name] | [LIFECYCLE_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-3 -- domain name] | [CHALLENGER_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-3 -- domain name] | [DOMAIN_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-3 -- domain name] | [LIFECYCLE_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |

*(Add rows for all §1 IN-SCOPE domains x all assigned reviewers.)*

**Domain gap-check** *(per §17 -- apply mechanically)*:

| Artifact Domain | Has HIGH-Applicability Reviewer? | Classification |
|-----------------|----------------------------------|----------------|
| [§1:S-1 domain] | [YES -- [ROLE_NAME]] / [NO] | [OK / ADVISORY-LENS-GAP] |
| [§1:S-2 domain] | [YES -- [ROLE_NAME]] / [NO] | [OK / ADVISORY-LENS-GAP] |
| [§1:S-3 domain] | [YES -- [ROLE_NAME]] / [NO] | [OK / ADVISORY-LENS-GAP] |

**ADVISORY-LENS-GAP domains**: [List each or "None -- all domains have HIGH-applicability reviewer."]
*Each ADVISORY-LENS-GAP domain -> ACTION ITEM REGISTER per §17.*

---
## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW -- how strong is the case for doing nothing?]

**Alternatives comparison table** *(per §3a)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DERIVATION RULE** *(pre-committed per §9; applied mechanically at BRACKET CLOSING)*:
  [Formula mapping table dimensions to g_null verdict. State before any reviewer runs.]

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

**Domain re-score** *(same dimensions as BRACKET OPENING alternatives table)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| [DIM-1] | [revised] | [revised] | [revised] | [reason] |
| [DIM-2] | [revised] | [revised] | [revised] | |
| [DIM-3] | [revised] | [revised] | [revised] | |

**Additional Findings** *(per §14: per-finding severity; per §11: each finding cites §1 surface)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-3 | [§1:S-n -- optional] | [FINDING_3] | [HIGH / MEDIUM / LOW] |

*(Findings without §1:S-n citation are ADVISORY-ORPHAN per §11.)*

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] <- mechanical result; do not assign editorially.

**Lens Coverage Table** *(per §15 -- ALL lens.verify entries)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|-------------------|
| Q-1 | [entry 1] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [entry 2] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-3 | [entry 3 if present] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(OPEN entries -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*(For `--depth deep`: repeat DOMAIN-2, DOMAIN-3. Each emits local ledger row, domain re-score, lens coverage table.)*

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
**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

**Applying §9 Stage 2 formula**:
```
g_null(initial)=[copy] | G_domain_agg=[copy]
  FAIL->FAIL | CONDITIONAL->max(initial,CONDITIONAL) | PASS->g_null(initial)
g_null(post-domain) = [FAIL / CONDITIONAL / PASS]
```
**g_null(post-domain)**: [FAIL / CONDITIONAL / PASS]

*Both carry forward to §3.8, LIFECYCLE, and BRACKET CLOSING.*

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger per §6.)*

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | [copy] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED -- N/A] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None"]

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

**Decision-readiness assessment**: [One paragraph referencing GOpen, G_domain Aggregate, and g_null(post-domain) explicitly.]

**Null hypothesis status**: [yes / partial / no -- reference g_null(post-domain). One sentence.]

**Additional Findings** *(per §14 + §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] <- mechanical result.

**Lens Coverage Table** *(per §15)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|-------------------|
| Q-1 | [entry 1] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [entry 2] | [ADDRESSED / OPEN] | [F-n or N/A] |

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

**Applying §9 Stage 3 formula**:
```
g_null(post-domain)=[copy] | G_lifecycle=[copy]
  FAIL->FAIL | CONDITIONAL->max(post-domain,CONDITIONAL) | PASS->g_null(post-domain)
g_null(final) = [FAIL / CONDITIONAL / PASS]
```
**g_null(final)**: [FAIL / CONDITIONAL / PASS]

**Revised alternatives table** *(aggregate domain re-scores; apply NULL HYPOTHESIS DERIVATION RULE)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Domain Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| [DIM-1] | [agg] | [agg] | [agg] | [reason] |
| [DIM-2] | [agg] | [agg] | [agg] | |
| [DIM-3] | [agg] | [agg] | [agg] | |

**Applying NULL HYPOTHESIS DERIVATION RULE to revised table**: [Result. One sentence.]

**Full CH-ID Saturation Check** *(per §8)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver |
|-------|--------------|-----------------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or WAIVER] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or WAIVER] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or WAIVER] |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [All defeated, or list gaps.]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A -- formula applied | or: justification one sentence]

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts per §3.

**GClose Rationale**: [2-3 sentences. Reference g_null(final), CH-ID saturation, and trajectory.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6. Runs after BRACKET CLOSING, before GATE VECTOR TABLE.)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [F-n] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [reference] | [COVERED / GAP] |

**Coverage gate signal**: [COVERED / PARTIAL -- list surfaces if PARTIAL]
**§11 ADVISORY-ORPHAN check**: [list findings without §1:S-n or "None"]

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

**Conflicts**: [Incompatible CH-ID responses or findings. If none: "None detected."]

**Convergence**: [CH-ID or concern named by 2+ reviewers. Name it and explain confidence.]

**§13 Progression Ledger** *(informational; no ledger row)*:
```
g_null(initial)     = [copy from BRACKET OPENING]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING]
Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED /
                     LIFECYCLE-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

**Scope coverage** *(§10 gate signal)*: [COVERED / PARTIAL]
**§17 Lens coverage summary**: [Restate ADVISORY-LENS-GAP domains from §1.5, if any. If none: "No ADVISORY-LENS-GAP domains."]

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
- Trajectory: [from §13]

**Scope coverage** *(§10)*: [COVERED / PARTIAL]

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**RESOLUTION REGISTRY** *(per §12 -- emit if CONDITIONAL; otherwise write N/A line)*:

| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [verbatim condition] | [ROLE_NAME] | [falsifiable criterion] | OPEN |

*RESOLUTION REGISTRY: N/A -- disposition is [READY/BLOCKED]* <- delete if CONDITIONAL

**Applying §16 PRIMARY DRIVER DERIVATION RULE**:
```
GClose=[_], G_domain_agg=[_], G_lifecycle=[_], GOpen=[_]
Rule fired: [rule number + reason]
```
**Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**Conditions** *(if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]

**Blocker** *(if BLOCKED)*: [Specific finding from the FAIL gate.]

---
## ACTION ITEM REGISTER

*Copy all Local Gate Ledger rows from BRACKET OPENING, DOMAIN(s), LIFECYCLE, and BRACKET CLOSING verbatim. Do not re-derive Gate Verdict or Class. Append: CH-ID PARTIAL/HOLDS rows, §8 waiver rows, §10 ADVISORY-GAP rows from §5.5, §11 ADVISORY-ORPHAN rows from §5.5, §15 ADVISORY-OPEN-LENS rows, §17 ADVISORY-LENS-GAP rows from §1.5.*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [copy from local ledger] | [copy] | [copy] | [copy] | [What must be done] | [ROLE_NAME] | [Criterion] |
| CH-001 | -- | -- | [BLOCKED/CONDITIONAL/ADVISORY] | [Item from CH-ID] | [ROLE_NAME] | [Criterion] |
| §8 WAIVER | -- | -- | ADVISORY | [Waiver text] | [ROLE_NAME] | N/A |
| §10 SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [Surface not addressed] | [ROLE_NAME] | [Criterion] |
| §11 FINDING-SURFACE LINKAGE | -- | -- | ADVISORY-ORPHAN | [Finding with no §1 citation] | [ROLE_NAME] | [Criterion] |
| §15 LENS EXHAUSTION | -- | -- | ADVISORY-OPEN-LENS | [Unanswered lens.verify entry] | [ROLE_NAME] | [Criterion] |
| §17 LENS COVERAGE APPLICABILITY | -- | -- | ADVISORY-LENS-GAP | [Domain with no HIGH-applicability reviewer] | [ROLE_NAME] | [Assign HIGH-applicability reviewer or accept gap] |
| -- | -- | -- | ADVISORY-OBS | [Advisory observation] | [ROLE_NAME] | [Criterion] |

*FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY*
*ADVISORY-GAP:§10 | ADVISORY-ORPHAN:§11 | ADVISORY-OPEN-LENS:§15 | ADVISORY-LENS-GAP:§17*

---

**Artifact to review:**

{{artifact}}
```

---
## V-04 -- Combination: V-01 + V-03 (C-33+C-34+C-35 Additive)

**Variation axes**: §17 LENS COVERAGE APPLICABILITY PROTOCOL (from V-03) + §18 NULL HYPOTHESIS DIMENSION TABLE CONTRACT (from V-01). Additive combination: V-03 lens coverage layer applied first (§17), then V-01 null hypothesis dimension table applied independently (§18). No cross-references between §17 and §18; each protocol operates in its own execution context.

**Hypothesis**: The additive combination of V-01 + V-03 achieves the same criteria coverage as V-02 (all three of C-33+C-34+C-35) but through independent protocol modules. If V-04 scores the same as V-02, then integrated design confers no structural advantage over additive composition. If V-04 scores lower, the integration in V-02 creates emergent auditability that the additive approach misses. The comparison isolates whether protocol coupling matters for scoring.

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

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed heading, label, field, formula, or structural element. Do not add sections between pre-printed headers. If a field cannot be filled, write `[N/A -- reason]`.

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
  (Add rows. Be exhaustive. Cited in §5.5, §11, and §17 LENS COVERAGE APPLICABILITY PROTOCOL.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]
Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks commitment. MEDIUM=Conditions commitment. LOW=Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts). FAIL>CONDITIONAL>PASS.
  BRACKET CLOSING applies mechanically. No editorial re-assessment.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim receives a CH-ID. Every downstream section carries CH-ID response table.
  PASS prohibited if any CH-ID shows OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section, after verdict stated.
  Assembly: ACTION ITEM REGISTER copies verbatim. Do not re-derive.
  EXCLUDED (no ledger row): §3.5, §3.8, §5.5, §1.5.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.   ROLE MANIFEST
  1.5. LENS COVERAGE TABLE            [excluded from gate ledger per §6]
  2.   BRACKET OPENING
  3.   DOMAIN(s)
  3.5. DOMAIN-AGGREGATE CHECKPOINT    [excluded per §6]
  3.8. CH-ID SATURATION CHECK         [excluded per §6]
  4.   LIFECYCLE
  5.   BRACKET CLOSING
  5.5. SCOPE COVERAGE RECONCILIATION  [excluded per §6]
  6.   GATE VECTOR TABLE
  7.   CROSS-ROLE SIGNALS
  8.   DISPOSITION
  9.   ACTION ITEM REGISTER
  LENS COVERAGE TABLE must follow ROLE MANIFEST and precede BRACKET OPENING.
  LIFECYCLE precedes BRACKET CLOSING.
  CH-ID SATURATION CHECK precedes LIFECYCLE.
  SCOPE COVERAGE RECONCILIATION precedes GATE VECTOR TABLE.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID has DOMAIN response before LIFECYCLE.
  FULLY SATURATED: CH-ID has DOMAIN+LIFECYCLE response before BRACKET CLOSING.
  PASS from BRACKET CLOSING prohibited without full saturation or stated waiver.
  Waiver: "CH-XXX WAIVER: [LIFECYCLE not applicable -- reason]" -> ADVISORY in register.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = result of §18 formula. [BRACKET OPENING]
  Stage 2: FAIL->FAIL | CONDITIONAL->max(initial,CONDITIONAL) | PASS->g_null(initial). [§3.5]
  Stage 3: FAIL->FAIL | CONDITIONAL->max(post-domain,CONDITIONAL) | PASS->g_null(post-domain). [BRACKET CLOSING]
  GClose must equal g_null(final). Deviation requires: "g_null OVERRIDE: [reason]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps IN-SCOPE surfaces to reviewer findings. COVERED/GAP.
  GAP -> ADVISORY-GAP in register. Gate signal COVERED/PARTIAL is informational.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE finding carries "[§1:S-n]" citation. No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit RESOLUTION REGISTRY:
    | Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status=OPEN |
  Otherwise: "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS contains §13 PROGRESSION LEDGER:
    g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory
  Trajectory: MONOTONIC-PASS/FAIL | DOMAIN-DEGRADED/RECOVERED | LIFECYCLE-DEGRADED/RECOVERED.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Findings as table: | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all finding severities). HIGH>MEDIUM>LOW. No findings -> LOW.
  Do not assign editorially. Gate verdicts independent of Section Severity.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE section addresses ALL lens.verify entries.
  After findings emit LENS COVERAGE TABLE (§15): | # | lens.verify Entry | Status | Finding Reference |
  OPEN entries -> ADVISORY-OPEN-LENS in register.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  PRIMARY DRIVER DERIVATION RULE (apply at DISPOSITION; do not assign editorially):
    1.GClose=FAIL->BRACKET CLOSING  2.G_domain_agg=FAIL->DOMAIN  3.G_lifecycle=FAIL->LIFECYCLE
    4.GOpen=FAIL->BRACKET OPENING   5.GClose=COND->BRACKET CLOSING  6.G_domain_agg=COND->DOMAIN
    7.G_lifecycle=COND->LIFECYCLE   8.GOpen=COND->BRACKET OPENING  9.all PASS->N/A
  Emit: "Applying §16 rule: [rule# + reason]" | "Primary Driver: [value]"

§17 -- LENS COVERAGE APPLICABILITY PROTOCOL [IMMUTABLE]
  After ROLE MANIFEST, at §1.5 LENS COVERAGE TABLE, pre-commit applicability ratings for each
  reviewer across each artifact domain (derived from §1 IN-SCOPE surfaces).
  Table format: | Artifact Domain | Reviewer | Lens Applicability | Rationale |
  One row per (artifact domain x reviewer) pair.
  Lens Applicability:
    HIGH   = this reviewer's primary lens directly addresses this domain.
    MEDIUM = partial coverage; incidental findings expected.
    LOW    = tangential; outside this reviewer's primary frame.
  Ratings pre-committed BEFORE reviewer sections execute.
  They are the rated basis for ADDRESSED/OPEN in CH-ID response tables.
  Domain gap-check (apply mechanically):
    For each artifact domain: if no reviewer carries HIGH applicability ->
      classify ADVISORY-LENS-GAP.
      Add to ACTION ITEM REGISTER: "LENS COVERAGE APPLICABILITY / [§1:S-n domain] /
      no HIGH-applicability reviewer assigned" | Class: ADVISORY-LENS-GAP.
  Write "No ADVISORY-LENS-GAP domains." if all domains have at least one HIGH reviewer.

§18 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]
  BRACKET OPENING uses a structured dimension comparison table for null hypothesis evaluation.
  Table format: | Dimension | Current State (null holds) | Proposed State (artifact built) | Delta | g_null Signal |
  Minimum 3 dimensions. Each dimension names a concrete capability, cost, or workflow state.
  g_null Signal values:
    WEAKENS NULL     = proposed is materially better; null harder to defend.
    NEUTRAL          = no material difference.
    STRENGTHENS NULL = current state acceptable or better; null is defensible.
  g_null DERIVATION FORMULA (apply mechanically; result = g_null(initial)):
    g_null(initial) = FAIL        if WEAKENS NULL > 50% of rows (null defeated).
    g_null(initial) = CONDITIONAL if no value exceeds 50% (mixed signals).
    g_null(initial) = PASS        if WEAKENS NULL <= 50% and NEUTRAL+STRENGTHENS > WEAKENS.
  §18 table is DISTINCT from the alternatives comparison table (Status Quo/Build/Best-Alt):
    §18 = null scenario vs proposal (two-way comparison).
    Alternatives table = three-strategy comparison.
  §18 table emitted first in BRACKET OPENING. §9 Stage 1 g_null(initial) = §18 formula result.
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

*After completing this manifest, proceed to §1.5 LENS COVERAGE TABLE before BRACKET OPENING.*

---
## §1.5 LENS COVERAGE TABLE *(per §17 -- emitted after ROLE MANIFEST, before BRACKET OPENING)*

*(List artifact domains from §1 IN-SCOPE surfaces. For each domain, rate each reviewer's applicability. Apply domain gap-check per §17.)*

| Artifact Domain | Reviewer | Lens Applicability (HIGH/MEDIUM/LOW) | Rationale |
|-----------------|----------|--------------------------------------|-----------|
| [§1:S-1 -- domain name] | [CHALLENGER_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-1 -- domain name] | [DOMAIN_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-1 -- domain name] | [LIFECYCLE_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-2 -- domain name] | [CHALLENGER_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-2 -- domain name] | [DOMAIN_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-2 -- domain name] | [LIFECYCLE_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-3 -- domain name] | [CHALLENGER_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-3 -- domain name] | [DOMAIN_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-3 -- domain name] | [LIFECYCLE_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |

*(Add rows for all §1 IN-SCOPE domains x all assigned reviewers.)*

**Domain gap-check** *(per §17 -- apply mechanically)*:

| Artifact Domain | Has HIGH-Applicability Reviewer? | Classification |
|-----------------|----------------------------------|----------------|
| [§1:S-1 domain] | [YES -- [ROLE_NAME]] / [NO] | [OK / ADVISORY-LENS-GAP] |
| [§1:S-2 domain] | [YES -- [ROLE_NAME]] / [NO] | [OK / ADVISORY-LENS-GAP] |
| [§1:S-3 domain] | [YES -- [ROLE_NAME]] / [NO] | [OK / ADVISORY-LENS-GAP] |

**ADVISORY-LENS-GAP domains**: [List each or "None -- all domains have HIGH-applicability reviewer."]
*Each ADVISORY-LENS-GAP domain -> ACTION ITEM REGISTER per §17.*

---
## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]

**Null hypothesis dimension table** *(per §18 -- g_null(initial) derivable from table values alone)*:

| Dimension | Current State (null holds) | Proposed State (artifact built) | Delta | g_null Signal |
|-----------|---------------------------|--------------------------------|-------|---------------|
| [DIM-1] | [current value or state] | [proposed value or state] | [FAVORS-BUILD / NEUTRAL / FAVORS-NULL] | [WEAKENS NULL / NEUTRAL / STRENGTHENS NULL] |
| [DIM-2] | [current] | [proposed] | [FAVORS-BUILD / NEUTRAL / FAVORS-NULL] | [WEAKENS NULL / NEUTRAL / STRENGTHENS NULL] |
| [DIM-3] | [current] | [proposed] | [FAVORS-BUILD / NEUTRAL / FAVORS-NULL] | [WEAKENS NULL / NEUTRAL / STRENGTHENS NULL] |

*(Add rows as needed. Each dimension is an independent signal.)*

**Applying §18 formula**:
```
WEAKENS NULL count     = [n]
NEUTRAL count          = [n]
STRENGTHENS NULL count = [n]
Majority signal = [WEAKENS NULL / NEUTRAL+STRENGTHENS / none (tied)]
g_null(initial) = [FAIL / CONDITIONAL / PASS]
```

**Alternatives comparison table** *(per §3a -- distinct from §18 table above)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DERIVATION RULE** *(pre-committed per §9; applied mechanically at BRACKET CLOSING)*:
  [Formula mapping table dimensions to g_null verdict. State before any reviewer runs.]

**Challenge claims** *(assign CH-IDs per §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction.] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)** *(per §18 formula above)*: [PASS / CONDITIONAL / FAIL]

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

**Domain re-score** *(same dimensions as BRACKET OPENING alternatives table)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| [DIM-1] | [revised] | [revised] | [revised] | [reason] |
| [DIM-2] | [revised] | [revised] | [revised] | |
| [DIM-3] | [revised] | [revised] | [revised] | |

**Additional Findings** *(per §14: per-finding severity; per §11: each finding cites §1 surface)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-3 | [§1:S-n -- optional] | [FINDING_3] | [HIGH / MEDIUM / LOW] |

*(Findings without §1:S-n citation are ADVISORY-ORPHAN per §11.)*

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] <- mechanical result; do not assign editorially.

**Lens Coverage Table** *(per §15 -- ALL lens.verify entries)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|-------------------|
| Q-1 | [entry 1] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [entry 2] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-3 | [entry 3 if present] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(OPEN entries -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*(For `--depth deep`: repeat DOMAIN-2, DOMAIN-3. Each emits local ledger row, domain re-score, lens coverage table.)*

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
**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

**Applying §9 Stage 2 formula**:
```
g_null(initial)=[copy] | G_domain_agg=[copy]
  FAIL->FAIL | CONDITIONAL->max(initial,CONDITIONAL) | PASS->g_null(initial)
g_null(post-domain) = [FAIL / CONDITIONAL / PASS]
```
**g_null(post-domain)**: [FAIL / CONDITIONAL / PASS]

*Both carry forward to §3.8, LIFECYCLE, and BRACKET CLOSING.*

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger per §6.)*

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | [copy] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED -- N/A] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None"]

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

**Decision-readiness assessment**: [One paragraph referencing GOpen, G_domain Aggregate, and g_null(post-domain) explicitly.]

**Null hypothesis status**: [yes / partial / no -- reference g_null(post-domain). One sentence.]

**Additional Findings** *(per §14 + §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] <- mechanical result.

**Lens Coverage Table** *(per §15)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|-------------------|
| Q-1 | [entry 1] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [entry 2] | [ADDRESSED / OPEN] | [F-n or N/A] |

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

**Applying §9 Stage 3 formula**:
```
g_null(post-domain)=[copy] | G_lifecycle=[copy]
  FAIL->FAIL | CONDITIONAL->max(post-domain,CONDITIONAL) | PASS->g_null(post-domain)
g_null(final) = [FAIL / CONDITIONAL / PASS]
```
**g_null(final)**: [FAIL / CONDITIONAL / PASS]

**Revised alternatives table** *(aggregate domain re-scores; apply NULL HYPOTHESIS DERIVATION RULE)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Domain Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| [DIM-1] | [agg] | [agg] | [agg] | [reason] |
| [DIM-2] | [agg] | [agg] | [agg] | |
| [DIM-3] | [agg] | [agg] | [agg] | |

**Applying NULL HYPOTHESIS DERIVATION RULE to revised table**: [Result. One sentence.]

**Full CH-ID Saturation Check** *(per §8)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver |
|-------|--------------|-----------------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or WAIVER] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or WAIVER] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or WAIVER] |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [All defeated, or list gaps.]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A -- formula applied | or: justification one sentence]

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts per §3.

**GClose Rationale**: [2-3 sentences. Reference g_null(final), CH-ID saturation, and trajectory.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6. Runs after BRACKET CLOSING, before GATE VECTOR TABLE.)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [F-n] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [reference] | [COVERED / GAP] |

**Coverage gate signal**: [COVERED / PARTIAL -- list surfaces if PARTIAL]
**§11 ADVISORY-ORPHAN check**: [list findings without §1:S-n or "None"]

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

**Conflicts**: [Incompatible CH-ID responses or findings. If none: "None detected."]

**Convergence**: [CH-ID or concern named by 2+ reviewers. Name it and explain confidence.]

**§13 Progression Ledger** *(informational; no ledger row)*:
```
g_null(initial)     = [copy from BRACKET OPENING]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING]
Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED /
                     LIFECYCLE-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

**Scope coverage** *(§10 gate signal)*: [COVERED / PARTIAL]
**§17 Lens coverage summary**: [Restate ADVISORY-LENS-GAP domains from §1.5, if any. If none: "No ADVISORY-LENS-GAP domains."]

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
- Trajectory: [from §13]

**Scope coverage** *(§10)*: [COVERED / PARTIAL]

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**RESOLUTION REGISTRY** *(per §12 -- emit if CONDITIONAL; otherwise write N/A line)*:

| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [verbatim condition] | [ROLE_NAME] | [falsifiable criterion] | OPEN |

*RESOLUTION REGISTRY: N/A -- disposition is [READY/BLOCKED]* <- delete if CONDITIONAL

**Applying §16 PRIMARY DRIVER DERIVATION RULE**:
```
GClose=[_], G_domain_agg=[_], G_lifecycle=[_], GOpen=[_]
Rule fired: [rule number + reason]
```
**Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**Conditions** *(if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]

**Blocker** *(if BLOCKED)*: [Specific finding from the FAIL gate.]

---
## ACTION ITEM REGISTER

*Copy all Local Gate Ledger rows from BRACKET OPENING, DOMAIN(s), LIFECYCLE, and BRACKET CLOSING verbatim. Do not re-derive Gate Verdict or Class. Append: CH-ID PARTIAL/HOLDS rows, §8 waiver rows, §10 ADVISORY-GAP rows from §5.5, §11 ADVISORY-ORPHAN rows from §5.5, §15 ADVISORY-OPEN-LENS rows, §17 ADVISORY-LENS-GAP rows from §1.5.*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [copy from local ledger] | [copy] | [copy] | [copy] | [What must be done] | [ROLE_NAME] | [Criterion] |
| CH-001 | -- | -- | [BLOCKED/CONDITIONAL/ADVISORY] | [Item from CH-ID] | [ROLE_NAME] | [Criterion] |
| §8 WAIVER | -- | -- | ADVISORY | [Waiver text] | [ROLE_NAME] | N/A |
| §10 SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [Surface not addressed] | [ROLE_NAME] | [Criterion] |
| §11 FINDING-SURFACE LINKAGE | -- | -- | ADVISORY-ORPHAN | [Finding with no §1 citation] | [ROLE_NAME] | [Criterion] |
| §15 LENS EXHAUSTION | -- | -- | ADVISORY-OPEN-LENS | [Unanswered lens.verify entry] | [ROLE_NAME] | [Criterion] |
| §17 LENS COVERAGE APPLICABILITY | -- | -- | ADVISORY-LENS-GAP | [Domain with no HIGH-applicability reviewer] | [ROLE_NAME] | [Assign HIGH-applicability reviewer or accept gap] |
| -- | -- | -- | ADVISORY-OBS | [Advisory observation] | [ROLE_NAME] | [Criterion] |

*FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY*
*ADVISORY-GAP:§10 | ADVISORY-ORPHAN:§11 | ADVISORY-OPEN-LENS:§15 | ADVISORY-LENS-GAP:§17*

---

**Artifact to review:**

{{artifact}}
```

---
## V-05 -- Full Integration: V-04 + §17<->§18 Cross-Reference Contract (C-33+C-34+C-35 Maximum Auditability)

**Variation axes**: §17 LENS COVERAGE APPLICABILITY PROTOCOL + §18 NULL HYPOTHESIS DIMENSION TABLE CONTRACT + explicit §17<->§18 cross-reference contract. §17 feeds §18: every ADVISORY-LENS-GAP domain identified in §17 MUST appear as a dimension in the §18 null hypothesis table. §18 cites §17: every §18 dimension carries a §17 domain reference; uncited dimensions are ADVISORY-DIMENSION-ORPHAN. A chain-verification field in BRACKET OPENING confirms the cross-reference is intact.

**Hypothesis**: The §17<->§18 cross-reference creates a stronger pre-commitment chain than independent protocols. A gap in lens coverage (§17) is directly connected to the null hypothesis evaluation (§18): if a domain has no HIGH-applicability reviewer, the null hypothesis must explicitly state whether doing nothing is acceptable on that uncovered dimension. This prevents the null hypothesis from being evaluated only on well-covered domains while silently ignoring coverage gaps. If the cross-reference requirement creates a new auditability pattern beyond C-33+C-34+C-35, it may become C-36 in a future rubric round.

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

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed heading, label, field, formula, or structural element. Do not add sections between pre-printed headers. If a field cannot be filled, write `[N/A -- reason]`.

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
  (Add rows. Be exhaustive. Cited in §5.5, §11, and §17 LENS COVERAGE APPLICABILITY PROTOCOL.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]
Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks commitment. MEDIUM=Conditions commitment. LOW=Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts). FAIL>CONDITIONAL>PASS.
  BRACKET CLOSING applies mechanically. No editorial re-assessment.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim receives a CH-ID. Every downstream section carries CH-ID response table.
  PASS prohibited if any CH-ID shows OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section, after verdict stated.
  Assembly: ACTION ITEM REGISTER copies verbatim. Do not re-derive.
  EXCLUDED (no ledger row): §3.5, §3.8, §5.5, §1.5.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.   ROLE MANIFEST
  1.5. LENS COVERAGE TABLE            [excluded from gate ledger per §6]
  2.   BRACKET OPENING
  3.   DOMAIN(s)
  3.5. DOMAIN-AGGREGATE CHECKPOINT    [excluded per §6]
  3.8. CH-ID SATURATION CHECK         [excluded per §6]
  4.   LIFECYCLE
  5.   BRACKET CLOSING
  5.5. SCOPE COVERAGE RECONCILIATION  [excluded per §6]
  6.   GATE VECTOR TABLE
  7.   CROSS-ROLE SIGNALS
  8.   DISPOSITION
  9.   ACTION ITEM REGISTER
  LENS COVERAGE TABLE must follow ROLE MANIFEST and precede BRACKET OPENING.
  LIFECYCLE precedes BRACKET CLOSING.
  CH-ID SATURATION CHECK precedes LIFECYCLE.
  SCOPE COVERAGE RECONCILIATION precedes GATE VECTOR TABLE.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID has DOMAIN response before LIFECYCLE.
  FULLY SATURATED: CH-ID has DOMAIN+LIFECYCLE response before BRACKET CLOSING.
  PASS from BRACKET CLOSING prohibited without full saturation or stated waiver.
  Waiver: "CH-XXX WAIVER: [LIFECYCLE not applicable -- reason]" -> ADVISORY in register.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = result of §18 formula. [BRACKET OPENING]
  Stage 2: FAIL->FAIL | CONDITIONAL->max(initial,CONDITIONAL) | PASS->g_null(initial). [§3.5]
  Stage 3: FAIL->FAIL | CONDITIONAL->max(post-domain,CONDITIONAL) | PASS->g_null(post-domain). [BRACKET CLOSING]
  GClose must equal g_null(final). Deviation requires: "g_null OVERRIDE: [reason]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps IN-SCOPE surfaces to reviewer findings. COVERED/GAP.
  GAP -> ADVISORY-GAP in register. Gate signal COVERED/PARTIAL is informational.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE finding carries "[§1:S-n]" citation. No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit RESOLUTION REGISTRY:
    | Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status=OPEN |
  Otherwise: "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS contains §13 PROGRESSION LEDGER:
    g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory
  Trajectory: MONOTONIC-PASS/FAIL | DOMAIN-DEGRADED/RECOVERED | LIFECYCLE-DEGRADED/RECOVERED.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Findings as table: | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all finding severities). HIGH>MEDIUM>LOW. No findings -> LOW.
  Do not assign editorially. Gate verdicts independent of Section Severity.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE section addresses ALL lens.verify entries.
  After findings emit LENS COVERAGE TABLE (§15): | # | lens.verify Entry | Status | Finding Reference |
  OPEN entries -> ADVISORY-OPEN-LENS in register.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  PRIMARY DRIVER DERIVATION RULE (apply at DISPOSITION; do not assign editorially):
    1.GClose=FAIL->BRACKET CLOSING  2.G_domain_agg=FAIL->DOMAIN  3.G_lifecycle=FAIL->LIFECYCLE
    4.GOpen=FAIL->BRACKET OPENING   5.GClose=COND->BRACKET CLOSING  6.G_domain_agg=COND->DOMAIN
    7.G_lifecycle=COND->LIFECYCLE   8.GOpen=COND->BRACKET OPENING  9.all PASS->N/A
  Emit: "Applying §16 rule: [rule# + reason]" | "Primary Driver: [value]"

§17 -- LENS COVERAGE APPLICABILITY PROTOCOL [IMMUTABLE] (extended: feeds §18)
  After ROLE MANIFEST, at §1.5 LENS COVERAGE TABLE, pre-commit applicability ratings for each
  reviewer across each artifact domain (derived from §1 IN-SCOPE surfaces).
  Table format: | Artifact Domain | Reviewer | Lens Applicability | Rationale |
  One row per (artifact domain x reviewer) pair.
  Lens Applicability:
    HIGH   = this reviewer's primary lens directly addresses this domain.
    MEDIUM = partial coverage; incidental findings expected.
    LOW    = tangential; outside this reviewer's primary frame.
  Ratings pre-committed BEFORE reviewer sections execute.
  They are the rated basis for ADDRESSED/OPEN in CH-ID response tables.
  Domain gap-check (apply mechanically):
    For each artifact domain: if no reviewer carries HIGH applicability ->
      classify ADVISORY-LENS-GAP.
      Add to ACTION ITEM REGISTER: "LENS COVERAGE APPLICABILITY / [§1:S-n domain] /
      no HIGH-applicability reviewer assigned" | Class: ADVISORY-LENS-GAP.
  Write "No ADVISORY-LENS-GAP domains." if all domains have at least one HIGH reviewer.

  §17->§18 CHAIN REQUIREMENT:
    Each ADVISORY-LENS-GAP domain identified in §17 MUST appear as a dimension in the §18
    NULL HYPOTHESIS DIMENSION TABLE. Rationale: a domain with no HIGH-applicability reviewer
    is a coverage gap; the null hypothesis must explicitly address whether doing nothing is
    acceptable on that uncovered dimension. This cross-reference is machine-verifiable:
    every §17 ADVISORY-LENS-GAP domain name must match a dimension name in the §18 table.

§18 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE] (extended: cites §17)
  BRACKET OPENING uses a structured dimension comparison table for null hypothesis evaluation.
  Table format: | Dimension | Current State (null holds) | Proposed State (artifact built) | Delta | g_null Signal |
  Minimum 3 dimensions. Each dimension names a concrete capability, cost, or workflow state.
  g_null Signal values:
    WEAKENS NULL     = proposed is materially better; null harder to defend.
    NEUTRAL          = no material difference.
    STRENGTHENS NULL = current state acceptable or better; null is defensible.
  g_null DERIVATION FORMULA (apply mechanically; result = g_null(initial)):
    g_null(initial) = FAIL        if WEAKENS NULL > 50% of rows (null defeated).
    g_null(initial) = CONDITIONAL if no value exceeds 50% (mixed signals).
    g_null(initial) = PASS        if WEAKENS NULL <= 50% and NEUTRAL+STRENGTHENS > WEAKENS.
  §18->§17 CITATION REQUIREMENT:
    Each dimension in the §18 table carries a §17 reference in the following format:
      | Dimension | §17 Domain | Current State | Proposed State | Delta | g_null Signal |
    §17 Domain = the §1 IN-SCOPE domain from §17 LENS COVERAGE TABLE that this dimension maps to.
    A dimension not traceable to a §17 domain is classified ADVISORY-DIMENSION-ORPHAN.
    ADVISORY-LENS-GAP dimensions (required by §17->§18 chain) are pre-labeled in the table.

  §18 table is DISTINCT from the alternatives comparison table (Status Quo/Build/Best-Alt):
    §18 = null scenario vs proposal (two-way comparison).
    Alternatives table = three-strategy comparison.
  §18 table emitted first in BRACKET OPENING. §9 Stage 1 g_null(initial) = §18 formula result.
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

*After completing this manifest, proceed to §1.5 LENS COVERAGE TABLE before BRACKET OPENING.*

---
## §1.5 LENS COVERAGE TABLE *(per §17 -- emitted after ROLE MANIFEST, before BRACKET OPENING)*

*(List artifact domains from §1 IN-SCOPE surfaces. For each domain, rate each reviewer's applicability. Apply domain gap-check per §17.)*

| Artifact Domain | Reviewer | Lens Applicability (HIGH/MEDIUM/LOW) | Rationale |
|-----------------|----------|--------------------------------------|-----------|
| [§1:S-1 -- domain name] | [CHALLENGER_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-1 -- domain name] | [DOMAIN_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-1 -- domain name] | [LIFECYCLE_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-2 -- domain name] | [CHALLENGER_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-2 -- domain name] | [DOMAIN_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-2 -- domain name] | [LIFECYCLE_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-3 -- domain name] | [CHALLENGER_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-3 -- domain name] | [DOMAIN_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |
| [§1:S-3 -- domain name] | [LIFECYCLE_ROLE] | [HIGH / MEDIUM / LOW] | [ONE_SENTENCE] |

*(Add rows for all §1 IN-SCOPE domains x all assigned reviewers.)*

**Domain gap-check** *(per §17 -- apply mechanically)*:

| Artifact Domain | Has HIGH-Applicability Reviewer? | Classification |
|-----------------|----------------------------------|----------------|
| [§1:S-1 domain] | [YES -- [ROLE_NAME]] / [NO] | [OK / ADVISORY-LENS-GAP] |
| [§1:S-2 domain] | [YES -- [ROLE_NAME]] / [NO] | [OK / ADVISORY-LENS-GAP] |
| [§1:S-3 domain] | [YES -- [ROLE_NAME]] / [NO] | [OK / ADVISORY-LENS-GAP] |

**ADVISORY-LENS-GAP domains**: [List each or "None -- all domains have HIGH-applicability reviewer."]
*Each ADVISORY-LENS-GAP domain -> ACTION ITEM REGISTER per §17.*

---
## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]

**Null hypothesis dimension table** *(per §18, citing §17 domains -- g_null(initial) derivable from table values alone)*:

| Dimension | §17 Domain | Current State (null holds) | Proposed State (artifact built) | Delta | g_null Signal |
|-----------|------------|---------------------------|--------------------------------|-------|---------------|
| [DIM-1 -- must include each §17 ADVISORY-LENS-GAP domain] | [§1:S-n] | [current value] | [proposed value] | [FAVORS-BUILD / NEUTRAL / FAVORS-NULL] | [WEAKENS NULL / NEUTRAL / STRENGTHENS NULL] |
| [DIM-2] | [§1:S-n] | [current] | [proposed] | | |
| [DIM-3] | [§1:S-n] | [current] | [proposed] | | |

*(§17 ADVISORY-LENS-GAP domains must appear as dimensions. Dimensions without a §17 domain = ADVISORY-DIMENSION-ORPHAN.)*

**Applying §18 formula**:
```
WEAKENS NULL count     = [n]
NEUTRAL count          = [n]
STRENGTHENS NULL count = [n]
Majority signal = [WEAKENS NULL / NEUTRAL+STRENGTHENS / none (tied)]
g_null(initial) = [FAIL / CONDITIONAL / PASS]
```

**§17->§18 chain verification**:
- ADVISORY-LENS-GAP domains from §1.5: [list or "None"]
- Each present in §18 dimension table: [YES -- [DIM-n] / NO -- CHAIN VIOLATION]

**Alternatives comparison table** *(per §3a -- distinct from §18 table above)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DERIVATION RULE** *(pre-committed per §9; applied mechanically at BRACKET CLOSING)*:
  [Formula mapping table dimensions to g_null verdict. State before any reviewer runs.]

**Challenge claims** *(assign CH-IDs per §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction.] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)** *(per §18 formula above)*: [PASS / CONDITIONAL / FAIL]

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

**Domain re-score** *(same dimensions as BRACKET OPENING alternatives table)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| [DIM-1] | [revised] | [revised] | [revised] | [reason] |
| [DIM-2] | [revised] | [revised] | [revised] | |
| [DIM-3] | [revised] | [revised] | [revised] | |

**Additional Findings** *(per §14: per-finding severity; per §11: each finding cites §1 surface)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-3 | [§1:S-n -- optional] | [FINDING_3] | [HIGH / MEDIUM / LOW] |

*(Findings without §1:S-n citation are ADVISORY-ORPHAN per §11.)*

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] <- mechanical result; do not assign editorially.

**Lens Coverage Table** *(per §15 -- ALL lens.verify entries)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|-------------------|
| Q-1 | [entry 1] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [entry 2] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-3 | [entry 3 if present] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(OPEN entries -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*(For `--depth deep`: repeat DOMAIN-2, DOMAIN-3. Each emits local ledger row, domain re-score, lens coverage table.)*

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
**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

**Applying §9 Stage 2 formula**:
```
g_null(initial)=[copy] | G_domain_agg=[copy]
  FAIL->FAIL | CONDITIONAL->max(initial,CONDITIONAL) | PASS->g_null(initial)
g_null(post-domain) = [FAIL / CONDITIONAL / PASS]
```
**g_null(post-domain)**: [FAIL / CONDITIONAL / PASS]

*Both carry forward to §3.8, LIFECYCLE, and BRACKET CLOSING.*

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger per §6.)*

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | [copy] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED -- N/A] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None"]

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

**Decision-readiness assessment**: [One paragraph referencing GOpen, G_domain Aggregate, and g_null(post-domain) explicitly.]

**Null hypothesis status**: [yes / partial / no -- reference g_null(post-domain). One sentence.]

**Additional Findings** *(per §14 + §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] <- mechanical result.

**Lens Coverage Table** *(per §15)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|-------------------|
| Q-1 | [entry 1] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [entry 2] | [ADDRESSED / OPEN] | [F-n or N/A] |

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

**Applying §9 Stage 3 formula**:
```
g_null(post-domain)=[copy] | G_lifecycle=[copy]
  FAIL->FAIL | CONDITIONAL->max(post-domain,CONDITIONAL) | PASS->g_null(post-domain)
g_null(final) = [FAIL / CONDITIONAL / PASS]
```
**g_null(final)**: [FAIL / CONDITIONAL / PASS]

**Revised alternatives table** *(aggregate domain re-scores; apply NULL HYPOTHESIS DERIVATION RULE)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Domain Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| [DIM-1] | [agg] | [agg] | [agg] | [reason] |
| [DIM-2] | [agg] | [agg] | [agg] | |
| [DIM-3] | [agg] | [agg] | [agg] | |

**Applying NULL HYPOTHESIS DERIVATION RULE to revised table**: [Result. One sentence.]

**Full CH-ID Saturation Check** *(per §8)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver |
|-------|--------------|-----------------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or WAIVER] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or WAIVER] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [N/A or WAIVER] |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [All defeated, or list gaps.]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A -- formula applied | or: justification one sentence]

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts per §3.

**GClose Rationale**: [2-3 sentences. Reference g_null(final), CH-ID saturation, and trajectory.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6. Runs after BRACKET CLOSING, before GATE VECTOR TABLE.)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [F-n] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [reference] | [COVERED / GAP] |

**Coverage gate signal**: [COVERED / PARTIAL -- list surfaces if PARTIAL]
**§11 ADVISORY-ORPHAN check**: [list findings without §1:S-n or "None"]

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

**Conflicts**: [Incompatible CH-ID responses or findings. If none: "None detected."]

**Convergence**: [CH-ID or concern named by 2+ reviewers. Name it and explain confidence.]

**§13 Progression Ledger** *(informational; no ledger row)*:
```
g_null(initial)     = [copy from BRACKET OPENING]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING]
Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED /
                     LIFECYCLE-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

**Scope coverage** *(§10 gate signal)*: [COVERED / PARTIAL]
**§17 Lens coverage summary**: [Restate ADVISORY-LENS-GAP domains from §1.5, if any.]

**§17->§18 chain status**: [Confirm each ADVISORY-LENS-GAP domain appears in §18 table. "Chain intact." or "Chain violation: [domain] not in §18 table."]

---
**§17 Lens coverage summary**: [Restate ADVISORY-LENS-GAP domains from §1.5, if any. If none: "No ADVISORY-LENS-GAP domains."]

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
- Trajectory: [from §13]

**Scope coverage** *(§10)*: [COVERED / PARTIAL]

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**RESOLUTION REGISTRY** *(per §12 -- emit if CONDITIONAL; otherwise write N/A line)*:

| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [verbatim condition] | [ROLE_NAME] | [falsifiable criterion] | OPEN |

*RESOLUTION REGISTRY: N/A -- disposition is [READY/BLOCKED]* <- delete if CONDITIONAL

**Applying §16 PRIMARY DRIVER DERIVATION RULE**:
```
GClose=[_], G_domain_agg=[_], G_lifecycle=[_], GOpen=[_]
Rule fired: [rule number + reason]
```
**Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**Conditions** *(if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]

**Blocker** *(if BLOCKED)*: [Specific finding from the FAIL gate.]

---
## ACTION ITEM REGISTER

*Copy all Local Gate Ledger rows verbatim. Append: CH-ID PARTIAL/HOLDS, §8 waivers, §10 ADVISORY-GAP, §11 ADVISORY-ORPHAN, §15 ADVISORY-OPEN-LENS, §17 ADVISORY-LENS-GAP, §18 ADVISORY-DIMENSION-ORPHAN.*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [copy from local ledger] | [copy] | [copy] | [copy] | [What must be done] | [ROLE_NAME] | [Criterion] |
| CH-001 | -- | -- | [BLOCKED/CONDITIONAL/ADVISORY] | [Item from CH-ID] | [ROLE_NAME] | [Criterion] |
| §8 WAIVER | -- | -- | ADVISORY | [Waiver text] | [ROLE_NAME] | N/A |
| §10 SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [Surface not addressed] | [ROLE_NAME] | [Criterion] |
| §11 FINDING-SURFACE LINKAGE | -- | -- | ADVISORY-ORPHAN | [Finding with no §1 citation] | [ROLE_NAME] | [Criterion] |
| §15 LENS EXHAUSTION | -- | -- | ADVISORY-OPEN-LENS | [Unanswered lens.verify entry] | [ROLE_NAME] | [Criterion] |
| §17 LENS COVERAGE APPLICABILITY | -- | -- | ADVISORY-LENS-GAP | [Domain with no HIGH-applicability reviewer] | [ROLE_NAME] | [Assign reviewer or accept gap] |
| §18 NULL HYPOTHESIS DIMENSION TABLE | -- | -- | ADVISORY-DIMENSION-ORPHAN | [Dimension not traceable to §17 domain] | [ROLE_NAME] | [Map to §17 domain or justify] |
| -- | -- | -- | ADVISORY-OBS | [Advisory observation] | [ROLE_NAME] | [Criterion] |

*FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY*
*ADVISORY-GAP:§10 | ADVISORY-ORPHAN:§11 | ADVISORY-OPEN-LENS:§15 | ADVISORY-LENS-GAP:§17 | ADVISORY-DIMENSION-ORPHAN:§18*

---

**Artifact to review:**

{{artifact}}
```

---
## Round 12 Variation Summary

| Variation | New Axes | New Contracts | Structural Additions | R11 Base |
|-----------|----------|---------------|---------------------|----------|
| V-01 | Null Hypothesis Dimension Table (C-35) | §17 NULL HYPOTHESIS DIMENSION TABLE | §17 in preamble; NULL HYPOTHESIS DIMENSION TABLE in BRACKET OPENING; g_null(initial) from formula | yes |
| V-02 | Lens Coverage Applicability + Null Hypothesis Table (C-33+C-34+C-35) | §17 LENS COVERAGE APPLICABILITY + §18 NULL HYPOTHESIS DIMENSION TABLE | §1.5 LENS COVERAGE TABLE section; §17 in preamble; §18 in preamble; both structural additions | yes |
| V-03 | Lens Coverage Applicability (C-33+C-34) | §17 LENS COVERAGE APPLICABILITY PROTOCOL | §1.5 LENS COVERAGE TABLE section; §17 in preamble; ADVISORY-LENS-GAP in register | yes |
| V-04 | V-01+V-03 additive (C-33+C-34+C-35) | §17 + §18 (independent) | Same structure as V-02; §17 and §18 not cross-referenced | yes |
| V-05 | V-04 + §17<->§18 cross-reference (C-33+C-34+C-35+chain) | §17 + §18 + chain contract | §17->§18 chain requirement; §18->§17 domain citation; chain-verification field; ADVISORY-DIMENSION-ORPHAN | yes |

**Predicted extraction candidates for rubric v12**:
- **C-36** (from V-05 if held): "§17<->§18 Chain Pre-committed" -- every ADVISORY-LENS-GAP domain from §17 appears as a dimension in §18; every §18 dimension cites a §17 domain; chain integrity is machine-verifiable from table values. Distinct from C-33 (per-row applicability rating), C-34 (gap-check), and C-35 (dimension table structure).

**Key test**: Can V-04 and V-05 both achieve 225/225? If V-05 outscores V-04, the chain contract is the signal. If they score equally, C-36 extraction is premature. V-02 vs V-04 comparison tests whether integrated vs additive design matters for C-33+C-34+C-35 simultaneously.
