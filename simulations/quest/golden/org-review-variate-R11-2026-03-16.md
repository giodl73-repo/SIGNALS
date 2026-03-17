# org-review Variations -- Round 11 (v9 rubric, 2026-03-16)
Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v9-2026-03-16.md

Prior round summary:
- R1--R8: V-05 climbed from 75 to 180/180 via bracket architecture, local ledger, §3a, §7 contracts.
- R9: V-05=195/195 (Perfect, sole). C-27 (CH-ID saturation), C-28 (null progression), C-29 (scope coverage gate) extracted. §8+§9+§10 in preamble.
- R10: All five variants score 195/195 under v9 (rubric ceiling). Three excellence patterns identified as C-30/C-31/C-32 candidates:
  - §11 FINDING-SURFACE LINKAGE (bidirectional scope trace: bottom-up finding→surface closes loop with §5.5 top-down surface→finding)
  - §12 CONDITIONAL RESOLUTION REGISTRY (CONDITIONAL disposition escalated to ownership contract with named owner + falsifiable close criterion)
  - §13 g_null PROGRESSION LEDGER (three-stage null hypothesis trajectory assembled at one machine-readable location in CROSS-ROLE SIGNALS)

Round 11 strategy:
- Baseline: V-05 R9 + R10 additions (§11+§12+§13) as non-negotiable base. All R11 variants score 195/195 under v9 from base inheritance.
- R11 is a frontier-extension round: explore three new axes that could surface C-33+ patterns.
- V-01: single axis -- §14 FINDING SEVERITY AGGREGATION CONTRACT. Per-finding severity table in DOMAIN/LIFECYCLE; section severity = worst(individual finding severities); pre-committed formula eliminates editorial severity assignment.
- V-02: single axis -- §14 LENS EXHAUSTION REQUIREMENT. All lens.verify entries from each role's definition must be addressed; LENS COVERAGE TABLE emitted per reviewer; unanswered entries → ADVISORY-OPEN-LENS items.
- V-03: single axis -- §14 PRIMARY DRIVER DERIVATION CONTRACT. "Primary driver" field in DISPOSITION derived by pre-committed precedence formula over gate vector; no editorial selection at synthesis time.
- V-04: combination -- V-01 + V-02 axes (§14 FINDING SEVERITY + §15 LENS EXHAUSTION).
- V-05: full integration -- V-01 + V-02 + V-03 axes (§14 + §15 + §16).

---

## V-01 -- Single Axis: Finding Severity Aggregation

**Variation axis**: §14 FINDING SEVERITY AGGREGATION CONTRACT. Each finding in DOMAIN and LIFECYCLE sections carries an individual severity tag. Section severity is derived mechanically from those tags via worst-case formula. Eliminates editorial severity assignment at the section level.

**Hypothesis**: Currently each reviewer section emits ONE severity label covering all findings collectively, assigned editorially. This allows a HIGH-severity finding to be masked by a reviewer who assigns LOW to the section. §14 pre-commits a per-finding severity table and a mechanical aggregation formula: Section Severity = worst(all finding severities). The formula runs in-section at verdict time, before the section verdict is issued. A HIGH individual finding cannot produce a LOW section severity without a stated formula-deviation justification. This creates a new auditability chain: individual finding → individual severity → aggregation formula → section severity → gate verdict.

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
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§14;
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
    SATURATED:        CH-ID has a response in >= 1 DOMAIN section.
  Before BRACKET CLOSING executes, each CH-ID must satisfy:
    FULLY SATURATED:  CH-ID has a response in >= 1 DOMAIN section AND in the LIFECYCLE section.
  A PASS verdict from BRACKET CLOSING is prohibited when any CH-ID is not FULLY SATURATED
  without a stated saturation waiver.
  Saturation waiver format: "CH-XXX WAIVER: [LIFECYCLE not applicable -- one sentence reason]"
  Waivers are emitted in §3.8 and carried to ACTION ITEM REGISTER as ADVISORY.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  The null hypothesis verdict evolves through three stages. Apply the formula mechanically.

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
  the reviewer(s) that addressed it. Coverage rules:
    COVERED: surface named in >= 1 finding from >= 1 reviewer section.
    GAP:     surface not named in any reviewer finding.
  Gap handling (apply mechanically):
    GAP surfaces receive forced LOW advisory status.
    GAP surfaces are added to ACTION ITEM REGISTER as ADVISORY-GAP items.
    Attribution: "SCOPE COVERAGE GATE / [surface name] / not addressed by any reviewer"
  Gate signal (informational -- does not feed §3 formula):
    COVERED: all §1 IN-SCOPE surfaces addressed.
    PARTIAL: >= 1 §1 IN-SCOPE surface not addressed.
  A PARTIAL coverage signal does not block commitment. It appears in CROSS-ROLE SIGNALS.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding produced by a DOMAIN or LIFECYCLE reviewer section must carry a §1 IN-SCOPE
  surface citation in the format: "[§1:S-n] finding text"
  where S-n is the ordinal number of the surface in §1 IN-SCOPE (S-1, S-2, S-3, ...).
  A finding without a valid §1 surface citation is classified ADVISORY-ORPHAN.
  ADVISORY-ORPHAN items appear in the ACTION ITEM REGISTER with class ADVISORY-ORPHAN.
  §5.5 (top-down: scope surface -> findings) and §11 (bottom-up: finding -> scope surface)
  form a bidirectional trace. Satisfying §5.5 does not satisfy §11, and vice versa.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  When DISPOSITION = CONDITIONAL, the DISPOSITION section emits a RESOLUTION REGISTRY table
  immediately following the Overall Disposition field:
    | Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
    | [gate] | [verbatim condition] | [ROLE_NAME] | [falsifiable close criterion] | OPEN |
  One row per CONDITIONAL gate. Resolution Owner = role responsible for closing the condition.
  Resolution Criterion = a falsifiable test observable from outside the review process.
  Status = OPEN at review time.
  A CONDITIONAL disposition without a RESOLUTION REGISTRY violates this contract.
  If DISPOSITION = READY or BLOCKED, write: "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  In CROSS-ROLE SIGNALS, a §13 PROGRESSION LEDGER sub-section assembles the three g_null values:
    g_null(initial)     = [copy from BRACKET OPENING]
    g_null(post-domain) = [copy from §3.5]
    g_null(final)       = [copy from BRACKET CLOSING]
    Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED /
                         LIFECYCLE-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
  Trajectory label derivation (apply mechanically):
    MONOTONIC-PASS:      all three = PASS
    MONOTONIC-FAIL:      all three = FAIL
    DOMAIN-DEGRADED:     g_null(post-domain) worse than g_null(initial)
    LIFECYCLE-DEGRADED:  g_null(final) worse than g_null(post-domain)
    DOMAIN-RECOVERED:    g_null(post-domain) better than g_null(initial)
    LIFECYCLE-RECOVERED: g_null(final) better than g_null(post-domain)
  This ledger is informational only. No gate ledger row emitted (excluded from §6).

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Within each DOMAIN and LIFECYCLE reviewer section, each finding entry carries an individual
  severity tag. Additional Findings are presented as a table:
    | # | §1 Surface | Finding | Severity |
    |---|-----------|---------|---------|
  Section Severity is derived mechanically from this table:
    Section Severity = worst(all finding severities in this section).
    Precedence: HIGH > MEDIUM > LOW.
    If no findings: Section Severity = LOW (no findings = no concern = advisory).
  Do not assign Section Severity editorially. Apply the formula above and state the result.
  The "Section Severity" field that follows the findings table is the mechanical formula result.
  Gate verdicts (G_domain, G_lifecycle) are derived from evidence quality; Section Severity is
  a separate signal. A HIGH Section Severity finding in a PASS gate is not contradictory -- it
  means the finding is serious but does not rise to a blocking gate condition.
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

**Null hypothesis strength**: [HIGH / MEDIUM / LOW -- how strong is the case for doing nothing?]

**Alternatives comparison table** *(>= 3 dimensions; challenger populates initial scores on a defined scale)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | [brief reason] |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DERIVATION RULE** *(pre-committed per §9; applied mechanically at BRACKET CLOSING)*:
  g_null verdict = FAIL if Build(B) >= Status Quo(A) AND B >= Best-Alt(C) on >= 2 of 3 dimensions
                   (null hypothesis defeated -- build wins).
  g_null verdict = CONDITIONAL if B >= A XOR B >= C (partial defeat -- material gap remains).
  g_null verdict = PASS if B < A OR B < C on majority of dimensions (null hypothesis holds).
  [Adjust formula dimensions to match table above. State the rule before any reviewer runs.]

**Challenge claims** *(assign CH-IDs; carry to every downstream section per contract §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction. One sentence.] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]

**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

**g_null(initial)** *(per contract §9 Stage 1 -- equals GOpen)*: [PASS / CONDITIONAL / FAIL]

*GOpen, g_null(initial), and all CH-IDs above carry forward to every downstream section.*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]

**CH-ID Response Table** *(mandatory per contract §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | [copy full claim from BRACKET OPENING] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

*(PARTIAL requires a named resolution path. OPEN = claim not addressable from this role's frame.)*

**Domain re-score** *(same dimensions as BRACKET OPENING table; re-score from this role's technical frame)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| [DIM-1] | [revised score] | [revised score] | [revised score] | [one sentence] |
| [DIM-2] | [revised score] | [revised score] | [revised score] | |
| [DIM-3] | [revised score] | [revised score] | [revised score] | |

**Additional Findings** *(per §14: each finding carries individual severity; per §11: each finding cites §1 surface)*:

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
**Section Severity**: [HIGH / MEDIUM / LOW] ← mechanical result; do not assign editorially.

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence. If CONDITIONAL: name condition. If FAIL: name gap.]

*(For `--depth deep`: repeat labeled DOMAIN-2, DOMAIN-3. Each emits own local ledger row and domain re-score.)*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per contract §6 -- this section produces no verdict.)*

**Applying §3a formula**:
```
G_domain rows collected:
  DOMAIN -- [ROLE_NAME]: [PASS / CONDITIONAL / FAIL]
  (DOMAIN-2 -- [ROLE_NAME]: [PASS / CONDITIONAL / FAIL] if --depth deep)

G_domain_agg = worst([list]) = [PASS / CONDITIONAL / FAIL]
```

**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

**Applying §9 Stage 2 formula**:
```
g_null(initial)  = [copy from BRACKET OPENING]
G_domain_agg     = [copy from above]

Apply §9 Stage 2:
  if G_domain_agg = FAIL:        g_null(post-domain) = FAIL
  if G_domain_agg = CONDITIONAL: g_null(post-domain) = max(g_null(initial), CONDITIONAL)
  if G_domain_agg = PASS:        g_null(post-domain) = g_null(initial)

g_null(post-domain) = [FAIL / CONDITIONAL / PASS]
```

**g_null(post-domain)**: [FAIL / CONDITIONAL / PASS]

*Both G_domain_agg and g_null(post-domain) carry forward to §3.8, LIFECYCLE, and BRACKET CLOSING.*

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger per contract §6. Runs after §3.5, before LIFECYCLE, per §7.)*

**Applying §8 pre-LIFECYCLE saturation requirement**:

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN -- copy from DOMAIN] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED -- or N/A] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None"]
*LIFECYCLE may proceed. Full saturation check (domain + lifecycle) executes at BRACKET CLOSING.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]
Received G_domain Aggregate: [PASS / CONDITIONAL / FAIL -- copy from §3.5]
Received g_null(post-domain): [FAIL / CONDITIONAL / PASS -- copy from §3.5]

**CH-ID Response Table** *(mandatory per contract §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph referencing GOpen and G_domain Aggregate and g_null(post-domain) explicitly.]

**Null hypothesis status**: [yes / partial / no -- reference g_null(post-domain). One sentence.]

**Additional Findings** *(per §14: each finding carries individual severity; per §11: each finding cites §1 surface)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1 -- commitment, program, or decision concerns.] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

*(Findings without a valid §1:S-n citation are ADVISORY-ORPHAN per §11.)*

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] ← mechanical result; do not assign editorially.

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

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

Apply §9 Stage 3:
  if G_lifecycle = FAIL:        g_null(final) = FAIL
  if G_lifecycle = CONDITIONAL: g_null(final) = max(g_null(post-domain), CONDITIONAL)
  if G_lifecycle = PASS:        g_null(final) = g_null(post-domain)

g_null(final) = [FAIL / CONDITIONAL / PASS]
```

**g_null(final)**: [FAIL / CONDITIONAL / PASS]
*GClose verdict must equal g_null(final) per §9. Deviation requires override justification below.*

**Revised alternatives table** *(aggregate domain re-scores; apply NULL HYPOTHESIS DERIVATION RULE)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Domain Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| [DIM-1] | [agg score] | [agg score] | [agg score] | [one sentence] |
| [DIM-2] | [agg score] | [agg score] | [agg score] | |
| [DIM-3] | [agg score] | [agg score] | [agg score] | |

**Applying NULL HYPOTHESIS DERIVATION RULE to revised table**: [State result of formula. One sentence.]

**Full CH-ID Saturation Check** *(per contract §8 -- PASS prohibited without full saturation)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver (if needed) |
|-------|--------------|-----------------|-----------------|---------------------|
| CH-001 | [copy from DOMAIN] | [copy from LIFECYCLE] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy from DOMAIN] | [copy from LIFECYCLE] | [DEFEATED / PARTIAL / HOLDS] | [NOTE] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [What was not fully addressed. If none: "None -- all CH-IDs DEFEATED."]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
*Must equal g_null(final) per §9. Deviation requires override justification.*
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

*(EXCLUDED from gate ledger per contract §6. Runs after BRACKET CLOSING, before GATE VECTOR TABLE, per §7. Applies §10 SCOPE COVERAGE GATE PROTOCOL and cross-checks §11 FINDING-SURFACE LINKAGE.)*

**Mapping §1 IN-SCOPE surfaces to reviewer findings** *(cite by section + finding number)*:

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [DOMAIN F-1 / etc.] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [reference] | [COVERED / GAP] |

**Coverage gate signal** *(per §10 -- informational; does not feed §3 formula)*:
[COVERED -- all surfaces addressed | PARTIAL -- [N] surface(s) not addressed]

**§11 ADVISORY-ORPHAN check** *(findings lacking §1 surface citation)*:
- [Finding reference: "FINDING-SURFACE LINKAGE / [section] / F-n / no valid §1:S-n citation"]
- [or: "None -- all findings carry valid §1 surface citations"]

**Forced advisory items for ACTION ITEM REGISTER**:
- GAP surfaces (per §10): [list or "None"]
- ADVISORY-ORPHAN findings (per §11): [list or "None"]

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

**Conflicts**: [Two reviewers with incompatible CH-ID responses or findings -- name roles and tension. If none: "None detected."]

**Convergence**: [CH-ID or concern named by two or more reviewers -- name it and explain confidence.]

**§13 Progression Ledger** *(per contract §13 -- informational; no ledger row emitted)*:
```
g_null(initial)     = [copy from BRACKET OPENING]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING]
Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED /
                     LIFECYCLE-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

**Scope coverage** *(§10 gate signal)*: [Restate coverage gate signal. If PARTIAL: list surfaces. If COVERED: "None -- full in-scope surface reviewed."]

---

## DISPOSITION

**Gate vector** *(fill from GATE VECTOR TABLE)*:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula** *(do not alter; do not reason editorially)*:
```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Null hypothesis progression** *(§9 -- from §13 ledger)*:
- g_null(initial) = [copy] | g_null(post-domain) = [copy] | g_null(final) = [copy]
- Trajectory: [from §13 PROGRESSION LEDGER]

**Scope coverage** *(§10 -- informational)*: [COVERED / PARTIAL]

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**RESOLUTION REGISTRY** *(per §12 -- emit if CONDITIONAL; otherwise write N/A line)*:

| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [verbatim condition] | [ROLE_NAME] | [falsifiable criterion] | OPEN |

*RESOLUTION REGISTRY: N/A -- disposition is [READY/BLOCKED]* ← delete this line if CONDITIONAL

**Primary driver**: [The gate verdict most responsible for this disposition -- one sentence. Editorial statement.]

**Conditions** *(if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]
2. [Additional conditions if present.]

**Blocker** *(if BLOCKED)*: [Specific finding from the FAIL gate.]

---

## ACTION ITEM REGISTER

*Copy all Local Gate Ledger rows from BRACKET OPENING, DOMAIN(s), LIFECYCLE, and BRACKET CLOSING verbatim. Do not re-derive Gate Verdict or Class. Append: CH-ID PARTIAL/HOLDS rows, §8 waiver rows (ADVISORY), §10 ADVISORY-GAP rows from §5.5, §11 ADVISORY-ORPHAN rows from §5.5.*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [copy from local ledger] | [copy] | [copy] | [copy] | [What must be done] | [ROLE_NAME] | [Criterion] |
| CH-001 | -- | -- | [BLOCKED/CONDITIONAL/ADVISORY] | [Item from CH-ID status] | [ROLE_NAME] | [Criterion] |
| §8 WAIVER | -- | -- | ADVISORY | [Waiver text if any] | [ROLE_NAME] | N/A |
| §10 SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [Surface not addressed] | [ROLE_NAME] | [Criterion] |
| §11 FINDING-SURFACE LINKAGE | -- | -- | ADVISORY-ORPHAN | [Finding with no §1 citation] | [ROLE_NAME] | [Criterion] |
| -- | -- | -- | ADVISORY-OBS | [Advisory observation] | [ROLE_NAME] | [Criterion] |

*Disposition class per §6: FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY*
*ADVISORY-GAP: unaddressed §1 surface per §10. ADVISORY-ORPHAN: finding with no §1 citation per §11.*

---

**Artifact to review:**

{{artifact}}
```

---

## V-02 -- Single Axis: Lens Exhaustion

**Variation axis**: §14 LENS EXHAUSTION REQUIREMENT. Each reviewer must address ALL `lens.verify` entries from their role definition, not just one. A LENS COVERAGE TABLE is emitted at the end of each DOMAIN and LIFECYCLE reviewer section listing every verify question and its status. Unanswered questions become ADVISORY-OPEN-LENS items in the ACTION ITEM REGISTER.

**Hypothesis**: Currently each reviewer cites "One from this role's `lens.verify`" -- a sampling, not an exhaustion. A reviewer can satisfy the current prompt by asking one question while ignoring three others. §14 pre-commits exhaustion: every lens.verify entry must appear in the coverage table with an addressed/open status. A table row showing OPEN means the reviewer's documented expertise was not fully applied to the artifact. This creates a new completeness dimension at the role-capability level: distinct from CH-ID tracing (which covers the challenger's claims) and from §5.5/§11 (which cover scope surface coverage), §14 covers whether each reviewer's own expertise lens was fully activated.

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
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§14;
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
    SATURATED:        CH-ID has a response in >= 1 DOMAIN section.
  Before BRACKET CLOSING executes, each CH-ID must satisfy:
    FULLY SATURATED:  CH-ID has a response in >= 1 DOMAIN section AND in the LIFECYCLE section.
  A PASS verdict from BRACKET CLOSING is prohibited when any CH-ID is not FULLY SATURATED
  without a stated saturation waiver.
  Saturation waiver format: "CH-XXX WAIVER: [LIFECYCLE not applicable -- one sentence reason]"
  Waivers are emitted in §3.8 and carried to ACTION ITEM REGISTER as ADVISORY.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1 -- g_null(initial) [emitted at BRACKET OPENING]:
    g_null(initial) = GOpen verdict directly.
  Stage 2 -- g_null(post-domain) [emitted at §3.5]:
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

§14 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN and LIFECYCLE reviewer section must address ALL entries from the role's
  lens.verify definition. A LENS COVERAGE TABLE is emitted after Additional Findings:
    | # | lens.verify Entry | Status | Finding Reference |
    |---|------------------|--------|--------------------|
  Status values: ADDRESSED (finding covers this question) / OPEN (not addressed in this review).
  "One from this role's lens.verify" prompt fields are replaced by this full coverage table.
  OPEN entries are ADVISORY-OPEN-LENS items; append to ACTION ITEM REGISTER as ADVISORY-OPEN-LENS.
  The LENS EXHAUSTION REQUIREMENT does not change gate verdict derivation. A section with all
  OPEN lens entries may still emit a PASS gate verdict if the CH-ID and gate evidence supports it.
  Lens exhaustion is a completeness audit, not a gate condition.
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

**Alternatives comparison table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DERIVATION RULE** *(pre-committed per §9)*:
  [State formula mapping table dimensions to g_null verdict before any reviewer runs.]

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
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]

**CH-ID Response Table** *(mandatory per §5)*:

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

**Additional Findings** *(per §11: each finding cites §1 surface)*:
1. [§1:S-n] [FINDING_1 -- from this role's `lens.verify` and `expertise.depth`.]
2. [§1:S-n] [FINDING_2]
3. [§1:S-n -- optional] [FINDING_3]

*(Findings without a valid §1:S-n citation are ADVISORY-ORPHAN per §11.)*

**Severity**: [HIGH / MEDIUM / LOW] *(per §2)*

**Lens Coverage Table** *(per §14 LENS EXHAUSTION REQUIREMENT -- list ALL lens.verify entries)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|-------------------|
| Q-1 | [Full text of lens.verify entry 1 from role definition] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [Full text of lens.verify entry 2] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-3 | [Full text of lens.verify entry 3 if present] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(Add rows for all lens.verify entries. OPEN entries -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.)*

**Recommendation**: [One concrete action.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*(For `--depth deep`: repeat DOMAIN-2, DOMAIN-3. Each emits own local ledger row and lens coverage table.)*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6 -- no verdict.)*

**Applying §3a formula**:
```
G_domain rows: DOMAIN -- [ROLE_NAME]: [verdict]
G_domain_agg = worst([list]) = [PASS / CONDITIONAL / FAIL]
```
**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

**Applying §9 Stage 2 formula**:
```
g_null(initial) = [copy] | G_domain_agg = [copy]
-> g_null(post-domain) = [FAIL / CONDITIONAL / PASS]
```
**g_null(post-domain)**: [FAIL / CONDITIONAL / PASS]

*Both carry forward to §3.8, LIFECYCLE, and BRACKET CLOSING.*

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger per §6.)*

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

**CH-ID Response Table** *(mandatory per §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph referencing GOpen, G_domain Aggregate, and g_null(post-domain).]

**Null hypothesis status**: [yes / partial / no -- reference g_null(post-domain).]

**Additional Findings** *(per §11: each finding cites §1 surface)*:
1. [§1:S-n] [FINDING_1 -- commitment, program, or decision concerns.]
2. [§1:S-n] [FINDING_2]

*(Findings without a valid §1:S-n citation are ADVISORY-ORPHAN per §11.)*

**Severity**: [HIGH / MEDIUM / LOW]

**Lens Coverage Table** *(per §14 LENS EXHAUSTION REQUIREMENT)*:

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

**Applying §9 Stage 3 formula**:
```
g_null(post-domain) = [copy] | G_lifecycle = [copy]
-> g_null(final) = [FAIL / CONDITIONAL / PASS]
```
**g_null(final)**: [FAIL / CONDITIONAL / PASS]

**Revised alternatives table** *(aggregate domain re-scores; apply NULL HYPOTHESIS DERIVATION RULE)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Domain Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| [DIM-1] | [agg] | [agg] | [agg] | |
| [DIM-2] | [agg] | [agg] | [agg] | |
| [DIM-3] | [agg] | [agg] | [agg] | |

**Applying NULL HYPOTHESIS DERIVATION RULE to revised table**: [Result. One sentence.]

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

**Remaining gaps**: [What was not fully addressed. If none: "None -- all CH-IDs DEFEATED."]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A -- formula applied | or: override justification]

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts per §3.

**GClose Rationale**: [2-3 sentences. Reference g_null(final), CH-ID saturation, null hypothesis trajectory.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6. Per §10 and §11.)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [reference] | [COVERED / GAP] |

**Coverage gate signal** *(§10 -- informational)*: [COVERED / PARTIAL]

**§11 ADVISORY-ORPHAN check**: [findings without §1 citation, or "None"]

**Forced advisory items for ACTION ITEM REGISTER**: [GAP and ADVISORY-ORPHAN items, or "None"]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain (agg) | [DOMAIN_ROLE(S)] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Incompatible CH-ID responses or findings. If none: "None detected."]

**Convergence**: [CH-ID or concern named by 2+ reviewers. Name it and explain confidence.]

**§13 Progression Ledger** *(per §13 -- informational)*:
```
g_null(initial) = [copy] | g_null(post-domain) = [copy] | g_null(final) = [copy]
Trajectory: [label]
```

**Scope coverage** *(§10)*: [COVERED / PARTIAL -- list surfaces if PARTIAL]

---

## DISPOSITION

**Gate vector**: GOpen=[copy] | G_domain_agg=[copy] | G_lifecycle=[copy] | GClose=[copy]

**Apply §3 formula**:
```
GClose=FAIL? -> BLOCKED | Any Gi=FAIL? -> BLOCKED | Any CONDITIONAL? -> CONDITIONAL | All PASS? -> READY
```

**Null hypothesis progression**: g_null(initial)=[copy] -> g_null(post-domain)=[copy] -> g_null(final)=[copy] | Trajectory: [from §13]

**Scope coverage** *(§10)*: [COVERED / PARTIAL]

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**RESOLUTION REGISTRY** *(per §12)*:

| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [verbatim condition] | [ROLE_NAME] | [falsifiable criterion] | OPEN |

*RESOLUTION REGISTRY: N/A -- disposition is [READY/BLOCKED]* ← delete if CONDITIONAL

**Primary driver**: [The gate verdict most responsible -- one sentence.]

**Conditions** *(if CONDITIONAL)*:
1. [Condition.]

**Blocker** *(if BLOCKED)*: [Finding from FAIL gate.]

---

## ACTION ITEM REGISTER

*Copy all Local Gate Ledger rows verbatim. Append CH-ID rows, §8 waivers, §10 ADVISORY-GAP, §11 ADVISORY-ORPHAN, and §14 ADVISORY-OPEN-LENS rows.*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [local ledger copy] | [copy] | [copy] | [copy] | [action] | [ROLE] | [criterion] |
| CH-001 | -- | -- | [class] | [CH-ID item] | [ROLE] | [criterion] |
| §8 WAIVER | -- | -- | ADVISORY | [waiver text] | [ROLE] | N/A |
| §10 SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [surface] | [ROLE] | [criterion] |
| §11 FINDING-SURFACE LINKAGE | -- | -- | ADVISORY-ORPHAN | [finding] | [ROLE] | [criterion] |
| §14 LENS EXHAUSTION | -- | -- | ADVISORY-OPEN-LENS | [unanswered lens.verify entry] | [ROLE] | [criterion] |
| -- | -- | -- | ADVISORY-OBS | [observation] | [ROLE] | [criterion] |

*FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY | ADVISORY-GAP: §10 | ADVISORY-ORPHAN: §11 | ADVISORY-OPEN-LENS: §14*

---

**Artifact to review:**

{{artifact}}
```

---

## V-03 -- Single Axis: Primary Driver Derivation

**Variation axis**: §14 PRIMARY DRIVER DERIVATION CONTRACT. The "Primary driver" field in DISPOSITION is derived by a pre-committed precedence formula over the gate vector. Eliminates editorial selection of the primary driver at synthesis time.

**Hypothesis**: The DISPOSITION section currently emits a "Primary driver" field that is an editorial prose statement -- the AI chooses which gate verdict is "most responsible" without a stated rule. This creates a hidden editorial step after all mechanical formulas have run. §14 pre-commits a PRIMARY DRIVER DERIVATION RULE: a strict precedence order over the gate vector that identifies the primary driver mechanically. The rule mirrors the precedence already implicit in §3 DISPOSITION ALGEBRA but makes the driver selection auditable without reading reviewer narrative. This is a distinct layer from §3 (which derives the disposition label) -- §14 derives the single-gate attribution for the disposition.

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
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§14;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive. These rows are cited in §5.5 and §11 FINDING-SURFACE LINKAGE.)
OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]
Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks commitment. MEDIUM=Conditions commitment. LOW=Advisory.
  These definitions apply universally. They may not be restated at any gate.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts). Precedence: FAIL>CONDITIONAL>PASS.
  BRACKET CLOSING applies this formula mechanically.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim receives a CH-ID. Every downstream section carries a CH-ID response table.
  PASS prohibited if any CH-ID shows OPEN status.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section.
  Assembly: ACTION ITEM REGISTER copies rows verbatim. No re-derivation.
  EXCLUDED (no ledger row): §3.5, §3.8, §5.5.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.ROLE MANIFEST | 2.BRACKET OPENING | 3.DOMAIN(s) | 3.5.DOMAIN-AGG CHECKPOINT |
  3.8.CH-ID SATURATION CHECK | 4.LIFECYCLE | 5.BRACKET CLOSING |
  5.5.SCOPE COVERAGE RECONCILIATION | 6.GATE VECTOR TABLE | 7.CROSS-ROLE SIGNALS |
  8.DISPOSITION | 9.ACTION ITEM REGISTER
  Reordering violates this contract.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID has DOMAIN response before LIFECYCLE.
  FULLY SATURATED: CH-ID has DOMAIN + LIFECYCLE response before BRACKET CLOSING.
  PASS from BRACKET CLOSING prohibited without full saturation (or stated waiver).
  Waiver format: "CH-XXX WAIVER: [reason]"

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = GOpen [emitted at BRACKET OPENING]
  Stage 2: g_null(post-domain) = formula(G_domain_agg, g_null(initial)) [emitted at §3.5]
    FAIL->FAIL; CONDITIONAL->max(initial,CONDITIONAL); PASS->g_null(initial)
  Stage 3: g_null(final) = formula(G_lifecycle, g_null(post-domain)) [emitted at BRACKET CLOSING]
    FAIL->FAIL; CONDITIONAL->max(post-domain,CONDITIONAL); PASS->g_null(post-domain)
  GClose must equal g_null(final) or declare override: "g_null OVERRIDE: [reason]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps each §1 surface to findings. COVERED/GAP classification.
  GAP->ADVISORY-GAP in ACTION ITEM REGISTER. Gate signal: COVERED/PARTIAL (informational).

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE finding carries "[§1:S-n]" citation. No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit RESOLUTION REGISTRY table after Overall Disposition.
  | Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status=OPEN |
  DISPOSITION!=CONDITIONAL -> "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS must include §13 PROGRESSION LEDGER:
  g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory label
  Labels: MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
          DOMAIN-RECOVERED / LIFECYCLE-RECOVERED. Informational only.

§14 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  The Primary Driver of the disposition is derived by the following precedence rule.
  Apply mechanically at DISPOSITION time. Do not assign editorially.

  PRIMARY DRIVER DERIVATION RULE:
    1. if GClose = FAIL:         Primary Driver = BRACKET CLOSING  [override authority invoked]
    2. elif G_domain_agg = FAIL: Primary Driver = DOMAIN           [domain evidence fails]
    3. elif G_lifecycle = FAIL:  Primary Driver = LIFECYCLE        [readiness gate fails]
    4. elif GOpen = FAIL:        Primary Driver = BRACKET OPENING  [initial challenge fails]
    5. elif GClose = CONDITIONAL:       Primary Driver = BRACKET CLOSING  [partial defeat only]
    6. elif G_domain_agg = CONDITIONAL: Primary Driver = DOMAIN
    7. elif G_lifecycle = CONDITIONAL:  Primary Driver = LIFECYCLE
    8. elif GOpen = CONDITIONAL:        Primary Driver = BRACKET OPENING
    9. else (all PASS):                 Primary Driver = N/A        [no single driver; all clear]

  Emit the result as:
    **Applying §14 rule**: [state which rule number fired and why]
    **Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

  The "Primary driver" prose field is replaced by this mechanical formula block.
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

**Alternatives comparison table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DERIVATION RULE** *(pre-committed per §9)*:
  [Formula mapping table dimensions to g_null verdict.]

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

**Additional Findings** *(per §11: each finding cites §1 surface)*:
1. [§1:S-n] [FINDING_1 -- from this role's `lens.verify` and `expertise.depth`.]
2. [§1:S-n] [FINDING_2]
3. [§1:S-n -- optional] [FINDING_3]

**Severity**: [HIGH / MEDIUM / LOW]
**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
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
G_domain_agg = worst([DOMAIN verdicts]) = [PASS / CONDITIONAL / FAIL]
g_null(post-domain): apply §9 Stage 2 -> [FAIL / CONDITIONAL / PASS]
```
**G_domain Aggregate**: [verdict]
**g_null(post-domain)**: [verdict]

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
**Null hypothesis status**: [yes / partial / no -- reference g_null(post-domain).]

**Additional Findings** *(per §11)*:
1. [§1:S-n] [FINDING_1]
2. [§1:S-n] [FINDING_2]

**Severity**: [HIGH / MEDIUM / LOW]
**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
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

**Applying §9 Stage 3**: g_null(post-domain)=[copy] + G_lifecycle=[copy] -> **g_null(final)**: [FAIL/CONDITIONAL/PASS]

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
**GClose override authority**: GClose=FAIL overrides all prior gate verdicts per §3.
**GClose Rationale**: [2-3 sentences referencing g_null(final), saturation, trajectory.]

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
g_null(initial) = [copy] | g_null(post-domain) = [copy] | g_null(final) = [copy]
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
| [gate] | [condition] | [ROLE] | [falsifiable criterion] | OPEN |

*RESOLUTION REGISTRY: N/A -- disposition is [READY/BLOCKED]* ← delete if CONDITIONAL

**Applying §14 PRIMARY DRIVER DERIVATION RULE**:
```
GClose=[_], G_domain_agg=[_], G_lifecycle=[_], GOpen=[_]
Rule fired: [state rule number 1-9 from §14 and why]
```
**Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**Conditions** *(if CONDITIONAL)*:
1. [Condition.]

**Blocker** *(if BLOCKED)*: [Finding from FAIL gate.]

---

## ACTION ITEM REGISTER

*Copy all Local Gate Ledger rows verbatim. Append CH-ID, §8 waiver, §10 ADVISORY-GAP, §11 ADVISORY-ORPHAN rows.*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [local ledger] | [copy] | [copy] | [copy] | [action] | [ROLE] | [criterion] |
| CH-001 | -- | -- | [class] | [item] | [ROLE] | [criterion] |
| §8 WAIVER | -- | -- | ADVISORY | [waiver] | [ROLE] | N/A |
| §10 SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [surface] | [ROLE] | [criterion] |
| §11 FINDING-SURFACE LINKAGE | -- | -- | ADVISORY-ORPHAN | [finding] | [ROLE] | [criterion] |
| -- | -- | -- | ADVISORY-OBS | [observation] | [ROLE] | [criterion] |

*FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY | ADVISORY-GAP: §10 | ADVISORY-ORPHAN: §11*

---

**Artifact to review:**

{{artifact}}
```

---

## V-04 -- Combination: V-01 + V-02 (Finding Severity + Lens Exhaustion)

**Variation axes**: §14 FINDING SEVERITY AGGREGATION CONTRACT + §15 LENS EXHAUSTION REQUIREMENT.

**Hypothesis**: V-01 and V-02 are structurally independent and activate on different fields within the same reviewer sections. §14 governs the severity derivation chain (individual finding severity → worst-case aggregation → section severity signal). §15 governs role expertise coverage (all lens.verify entries must appear in coverage table; OPEN entries become ADVISORY-OPEN-LENS). No shared fields: §14 adds a severity column to the findings table; §15 adds a separate coverage table after findings. If both hold simultaneously, the combination surfaces whether any lens entry is addressed only via a LOW-severity finding while section severity is HIGH -- a cross-axis signal invisible to either contract alone.

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
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§15;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive. These rows are cited in §5.5 and §11 FINDING-SURFACE LINKAGE.)
OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]
Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks commitment. MEDIUM=Conditions commitment. LOW=Advisory.
  These definitions apply universally. They may not be restated at any gate.

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
  FULLY SATURATED: DOMAIN + LIFECYCLE before BRACKET CLOSING.
  PASS from BRACKET CLOSING prohibited without full saturation or waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = GOpen.
  Stage 2: g_null(post-domain): FAIL->FAIL; CONDITIONAL->max(initial,CONDITIONAL); PASS->initial.
  Stage 3: g_null(final): FAIL->FAIL; CONDITIONAL->max(post-domain,CONDITIONAL); PASS->post-domain.
  GClose must equal g_null(final) or declare "g_null OVERRIDE: [reason]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps §1 surfaces to findings. GAP->ADVISORY-GAP. Gate signal COVERED/PARTIAL is informational.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE finding carries "[§1:S-n]" citation. No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit RESOLUTION REGISTRY after Overall Disposition.
  | Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status=OPEN |

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS §13 PROGRESSION LEDGER:
  g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory label. Informational only.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Findings in DOMAIN/LIFECYCLE presented as table: | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all finding severities). HIGH>MEDIUM>LOW. No findings = LOW.
  Do not assign Section Severity editorially.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE section must address ALL lens.verify entries from the role definition.
  LENS COVERAGE TABLE emitted after findings: | # | lens.verify Entry | Status | Finding Reference |
  Status: ADDRESSED / OPEN. OPEN entries -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.
  Lens exhaustion is a completeness audit, not a gate condition.
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

**Alternatives comparison table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DERIVATION RULE** *(per §9)*: [Formula mapping dimensions to g_null verdict.]

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

**Additional Findings** *(per §14: per-finding severity; per §11: §1 surface citation)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1 -- from this role's `lens.verify` and `expertise.depth`.] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-3 | [§1:S-n -- optional] | [FINDING_3] | [HIGH / MEDIUM / LOW] |

*(No §1:S-n citation = ADVISORY-ORPHAN per §11.)*

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW] ← mechanical per §14.

**Lens Coverage Table** *(per §15 -- ALL lens.verify entries)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|-------------------|
| Q-1 | [lens.verify entry 1 text] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [lens.verify entry 2 text] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-3 | [lens.verify entry 3 if present] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(OPEN -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.)*

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*(For `--depth deep`: repeat DOMAIN-2, DOMAIN-3. Each emits own ledger row, re-score, and lens table.)*

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
**Null hypothesis status**: [yes / partial / no -- reference g_null(post-domain).]

**Additional Findings** *(per §14 and §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

*(No §1:S-n citation = ADVISORY-ORPHAN per §11.)*

**Finding Severity Aggregation (per §14)**: worst(F-1=[_], F-2=[_]) = **Section Severity**: [HIGH/MEDIUM/LOW] ← mechanical per §14.

**Lens Coverage Table** *(per §15)*:

| # | lens.verify Entry | Status | Finding Reference |
|---|------------------|--------|-------------------|
| Q-1 | [lens.verify entry 1] | [ADDRESSED / OPEN] | [F-n or N/A] |
| Q-2 | [lens.verify entry 2] | [ADDRESSED / OPEN] | [F-n or N/A] |

*(OPEN -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.)*

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

**Applying §9 Stage 3**: g_null(post-domain)=[copy] + G_lifecycle=[copy] -> **g_null(final)**: [verdict]

**Revised alternatives table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------|
| [DIM-1] | [agg] | [agg] | [agg] | |
| [DIM-2] | [agg] | [agg] | [agg] | |
| [DIM-3] | [agg] | [agg] | [agg] | |

**Applying NULL HYPOTHESIS DERIVATION RULE**: [Result. One sentence.]

**Full CH-ID Saturation Check** *(per §8)*:

| CH-ID | DOMAIN | LIFECYCLE | Full Saturation | Waiver |
|-------|--------|-----------|-----------------|--------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |

**CH-ID Final Assessment**:

| CH-ID | G_domain | G_lifecycle | Final Status | Notes |
|-------|----------|------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [All defeated, or list.]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A or justification]
**GClose override authority**: GClose=FAIL overrides all prior gate verdicts per §3.
**GClose Rationale**: [2-3 sentences referencing g_null(final), saturation, trajectory.]

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
**§11 ADVISORY-ORPHAN check**: [orphan findings or "None"]
**Forced advisory items**: [GAP and ADVISORY-ORPHAN, or "None"]

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
g_null(initial) = [copy] | g_null(post-domain) = [copy] | g_null(final) = [copy]
Trajectory: [label]
```

**Scope coverage** *(§10)*: [COVERED / PARTIAL]

---

## DISPOSITION

**Gate vector**: GOpen=[copy] | G_domain_agg=[copy] | G_lifecycle=[copy] | GClose=[copy]

**Apply §3 formula**: GClose=FAIL?->BLOCKED | Any FAIL?->BLOCKED | Any CONDITIONAL?->CONDITIONAL | All PASS?->READY

**Null hypothesis progression**: [copy initial] -> [copy post-domain] -> [copy final] | Trajectory: [from §13]

**Scope coverage** *(§10)*: [COVERED / PARTIAL]

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**RESOLUTION REGISTRY** *(per §12)*:

| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [condition] | [ROLE] | [falsifiable criterion] | OPEN |

*RESOLUTION REGISTRY: N/A -- disposition is [READY/BLOCKED]* ← delete if CONDITIONAL

**Primary driver**: [The gate verdict most responsible -- one sentence. Editorial statement.]

**Conditions** *(if CONDITIONAL)*:
1. [Condition.]

**Blocker** *(if BLOCKED)*: [Finding from FAIL gate.]

---

## ACTION ITEM REGISTER

*Copy Local Gate Ledger rows verbatim. Append CH-ID, §8 waiver, §10 ADVISORY-GAP, §11 ADVISORY-ORPHAN, §15 ADVISORY-OPEN-LENS rows.*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [local ledger] | [copy] | [copy] | [copy] | [action] | [ROLE] | [criterion] |
| CH-001 | -- | -- | [class] | [item] | [ROLE] | [criterion] |
| §8 WAIVER | -- | -- | ADVISORY | [waiver] | [ROLE] | N/A |
| §10 SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [surface] | [ROLE] | [criterion] |
| §11 FINDING-SURFACE LINKAGE | -- | -- | ADVISORY-ORPHAN | [finding] | [ROLE] | [criterion] |
| §15 LENS EXHAUSTION | -- | -- | ADVISORY-OPEN-LENS | [unanswered entry] | [ROLE] | [criterion] |
| -- | -- | -- | ADVISORY-OBS | [observation] | [ROLE] | [criterion] |

*FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY | ADVISORY-GAP:§10 | ADVISORY-ORPHAN:§11 | ADVISORY-OPEN-LENS:§15*

---

**Artifact to review:**

{{artifact}}
```

---

## V-05 -- Full Integration: V-01 + V-02 + V-03

**Variation axes**: §14 FINDING SEVERITY AGGREGATION CONTRACT + §15 LENS EXHAUSTION REQUIREMENT + §16 PRIMARY DRIVER DERIVATION CONTRACT.

**Hypothesis**: All three R11 axes are structurally independent and activate at different execution points with no shared fields. §14 activates inside each reviewer section at findings time (per-finding severity -> worst-case aggregation formula -> section severity). §15 activates inside each reviewer section at expertise coverage time (all lens.verify entries -> coverage table -> ADVISORY-OPEN-LENS for gaps). §16 activates at DISPOSITION time (gate vector -> precedence formula -> primary driver field). Together they form a complete pre-commitment audit trail for three currently-editorial steps: severity derivation chain, role expertise completeness, and disposition attribution. If all three hold simultaneously, three new C-33/C-34/C-35 patterns emerge -- each traceable to a distinct structural layer with no overlap. The combination also creates cross-axis observability: §14 and §15 together reveal whether lens entries are addressed only via LOW-severity findings; §15 and §16 together reveal whether the primary driver role is the same role with the most OPEN lens entries.

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
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§16;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive. These rows are cited in §5.5 SCOPE COVERAGE RECONCILIATION
  and §11 FINDING-SURFACE LINKAGE.)
OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]
Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks commitment. MEDIUM=Conditions commitment. LOW=Advisory.
  These definitions apply universally. They may not be restated at any gate.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts). Precedence: FAIL>CONDITIONAL>PASS.
  BRACKET CLOSING applies this formula mechanically. No editorial re-assessment at closure.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim receives a CH-ID. Every downstream section carries a CH-ID response table.
  PASS prohibited if any CH-ID shows OPEN status.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section, after verdict is stated.
  Assembly: ACTION ITEM REGISTER copies rows verbatim. Do not re-derive Gate Verdict or Class.
  EXCLUDED (no ledger row): §3.5, §3.8, §5.5.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.ROLE MANIFEST | 2.BRACKET OPENING | 3.DOMAIN(s) | 3.5.DOMAIN-AGG CHECKPOINT |
  3.8.CH-ID SATURATION CHECK | 4.LIFECYCLE | 5.BRACKET CLOSING |
  5.5.SCOPE COVERAGE RECONCILIATION | 6.GATE VECTOR TABLE | 7.CROSS-ROLE SIGNALS |
  8.DISPOSITION | 9.ACTION ITEM REGISTER
  Reordering violates this contract. LIFECYCLE precedes BRACKET CLOSING.
  CH-ID SATURATION CHECK precedes LIFECYCLE.
  SCOPE COVERAGE RECONCILIATION precedes GATE VECTOR TABLE.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID has DOMAIN response before LIFECYCLE.
  FULLY SATURATED: CH-ID has DOMAIN + LIFECYCLE response before BRACKET CLOSING.
  PASS from BRACKET CLOSING prohibited without full saturation or stated waiver.
  Waiver format: "CH-XXX WAIVER: [LIFECYCLE not applicable -- one sentence reason]"

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = GOpen. [BRACKET OPENING]
  Stage 2: g_null(post-domain) [§3.5]:
    FAIL->FAIL; CONDITIONAL->max(initial,CONDITIONAL); PASS->g_null(initial). Scale FAIL<CONDITIONAL<PASS.
  Stage 3: g_null(final) [BRACKET CLOSING]:
    FAIL->FAIL; CONDITIONAL->max(post-domain,CONDITIONAL); PASS->g_null(post-domain).
  GClose must equal g_null(final) or declare "g_null OVERRIDE: [reason]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps each §1 IN-SCOPE surface to reviewer findings. COVERED/GAP classification.
  GAP->ADVISORY-GAP in ACTION ITEM REGISTER. Gate signal COVERED/PARTIAL is informational.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE finding carries "[§1:S-n]" citation. No citation = ADVISORY-ORPHAN.
  §5.5 (top-down) and §11 (bottom-up) are independent requirements.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit RESOLUTION REGISTRY table after Overall Disposition:
    | Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status=OPEN |
  One row per CONDITIONAL gate. Resolution Criterion = falsifiable test.
  DISPOSITION!=CONDITIONAL -> "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS must include §13 PROGRESSION LEDGER sub-section:
    g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory label
  Labels: MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
          DOMAIN-RECOVERED / LIFECYCLE-RECOVERED. Informational only. No ledger row emitted.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Within each DOMAIN and LIFECYCLE section, each finding carries an individual severity tag.
  Findings presented as table: | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all finding severities). Precedence: HIGH>MEDIUM>LOW.
  No findings: Section Severity = LOW. Do not assign Section Severity editorially -- apply formula.
  Gate verdicts (G_domain, G_lifecycle) are derived from evidence quality and are independent of
  Section Severity. A HIGH Section Severity in a PASS gate is not contradictory.

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

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. CHALLENGER positions remain fixed. State total count.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table** *(>= 3 dimensions)*:

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

**Domain re-score** *(same dimensions as BRACKET OPENING; re-score from this role's frame)*:

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
**Section Severity**: [HIGH / MEDIUM / LOW] ← mechanical result per §14; do not assign editorially.

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

*(For `--depth deep`: repeat DOMAIN-2, DOMAIN-3. Each emits own local ledger row, domain re-score, and lens coverage table.)*

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
**Section Severity**: [HIGH / MEDIUM / LOW] ← mechanical result per §14; do not assign editorially.

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

*(EXCLUDED from gate ledger per §6. Runs after BRACKET CLOSING, before GATE VECTOR TABLE. Applies §10 SCOPE COVERAGE GATE PROTOCOL and cross-checks §11 FINDING-SURFACE LINKAGE.)*

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
g_null(initial)     = [copy from BRACKET OPENING]
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

*RESOLUTION REGISTRY: N/A -- disposition is [READY/BLOCKED]* ← delete this line if CONDITIONAL

**Applying §16 PRIMARY DRIVER DERIVATION RULE**:
```
GClose=[_], G_domain_agg=[_], G_lifecycle=[_], GOpen=[_]
Rule fired: [state rule number 1-9 from §16 and why it fires before others in the precedence order]
```
**Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**Conditions** *(if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]
2. [Additional conditions if present.]

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
| -- | -- | -- | ADVISORY-OBS | [Advisory observation not from CH-ID or gate] | [ROLE_NAME] | [Criterion] |

*FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY*
*ADVISORY-GAP: §10 | ADVISORY-ORPHAN: §11 | ADVISORY-OPEN-LENS: §15*

---

**Artifact to review:**

{{artifact}}
```

---

## Round 11 Variation Summary

| Variation | New Axis | New Contracts | Structural Addition | R9+R10 Base |
|-----------|----------|---------------|---------------------|-------------|
| V-01 | Per-Finding Severity Aggregation | §14 FINDING SEVERITY AGGREGATION | Per-finding severity table + worst-case formula in DOMAIN/LIFECYCLE | yes |
| V-02 | Lens Exhaustion | §14 LENS EXHAUSTION REQUIREMENT | LENS COVERAGE TABLE per reviewer; ADVISORY-OPEN-LENS in register | yes |
| V-03 | Primary Driver Derivation | §14 PRIMARY DRIVER DERIVATION | §14 formula block replaces editorial Primary Driver in DISPOSITION | yes |
| V-04 | V-01 + V-02 | §14 FINDING SEVERITY + §15 LENS EXHAUSTION | Both reviewer-section additions; no DISPOSITION change | yes |
| V-05 | V-01 + V-02 + V-03 | §14 + §15 + §16 | All three structural additions | yes |

**Predicted C-33/C-34/C-35 extraction candidates**:
- **C-33** (from V-01/V-04/V-05 if held): "Per-Finding Severity with Mechanical Aggregation Pre-committed as §14" -- individual findings carry severity tags; section severity is worst-case aggregate of those tags; eliminates editorial severity assignment; creates new auditability chain: finding -> individual severity -> formula -> section severity signal. Distinct from C-02 (section-level severity semantics) and C-12 (class derivation from gate verdicts).
- **C-34** (from V-02/V-04/V-05 if held): "Role Lens Exhaustion Pre-committed as §15 Requirement" -- all lens.verify entries must appear in LENS COVERAGE TABLE with ADDRESSED/OPEN status; OPEN entries are ADVISORY-OPEN-LENS; completeness at the role-capability level, distinct from CH-ID saturation (C-27: claim coverage), §5.5 (C-29: scope surface coverage), and §11 (C-30: finding-to-surface bidirectional trace).
- **C-35** (from V-03/V-05 if held): "Primary Driver Derivation Rule Pre-committed as §16 Contract" -- gate vector precedence formula selects the primary driver mechanically at DISPOSITION time; eliminates the last remaining editorial step after all gate verdicts are known; distinct from §3 (which derives the disposition label) because §16 derives single-gate attribution rather than the categorical READY/CONDITIONAL/BLOCKED outcome.

**Key test**: Can V-05 hold all three simultaneously? §14 (reviewer-level severity derivation), §15 (reviewer-level lens completeness), and §16 (synthesis-level driver attribution) activate at different execution points with no shared fields. If no conflict, C-33/C-34/C-35 extraction follows under v10, mirroring the C-27/C-28/C-29 pattern from R9.
