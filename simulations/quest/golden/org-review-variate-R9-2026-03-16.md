# org-review Variations -- Round 9 (v8 rubric, 2026-03-16)
Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v8-2026-03-16.md

Prior round summary:
- R1--R6: V-04/V-05 climbed from 95 to 160/165 via bracket architecture, local ledger, three contracts.
- R7: V-04=170 (C-24: domain-aggregate formula). V-05=170 (C-25: exclusion registry).
- R8: V-05=180/180 (Perfect, sole). C-24+C-25+C-26 simultaneously. §3a + exclusion registry + §7.
  V-04=175 (no §7). V-01/V-02/V-03=170 (each holds one of the three).

Round 9 strategy:
- Baseline: V-05 R8 (180/180). The rubric ceiling is 180 under v8. Round 9 is a frontier-extension
  round: explore axes that could surface new C-27+ patterns.
- All R9 variants carry V-05 R8 features (§3a + exclusion registry + §7) as non-negotiable base.
- V-01: single axis -- CH-ID Saturation Pre-gate (§8 new contract + CH-ID SATURATION CHECK section).
        Hypothesis: pre-committing that every CH-ID must receive responses from BOTH domain AND lifecycle
        before BRACKET CLOSING may proceed prevents silent coverage gaps traceable to no section.
- V-02: single axis -- Null Hypothesis Progression Contract (§8 new contract + g_null tracking fields).
        Hypothesis: pre-committing the 3-stage g_null evolution formula (initial -> post-domain -> final)
        prevents bracket closing from returning a final null verdict inconsistent with intermediate states.
- V-03: single axis -- Scope Coverage Reconciliation Gate (§8 new contract + new SCOPE COVERAGE
        RECONCILIATION section after BRACKET CLOSING). Hypothesis: a formal coverage gate before
        DISPOSITION ensures no §1 IN-SCOPE surface escapes without a reviewer finding trace.
- V-04: combination -- V-01 + V-02 axes (§8 CH-ID Saturation + §9 Null Progression).
- V-05: full integration -- V-01 + V-02 + V-03 axes (§8 CH-ID Saturation + §9 Null Progression +
        §10 Scope Coverage + SCOPE COVERAGE RECONCILIATION section).

---

## V-01 -- Single Axis: CH-ID Saturation Pre-gate

**Variation axis**: CH-ID Saturation Requirement (new §8 in DISPOSITION_CONTRACT + new CH-ID SATURATION
CHECK section before BRACKET CLOSING).

**Hypothesis**: The current architecture tracks CH-ID status within each section independently but has no
gate that verifies cross-section coverage before BRACKET CLOSING executes. A CH-ID that received a
DOMAIN response but no LIFECYCLE response can receive DEFEATED status at BRACKET CLOSING without the
lifecycle section having addressed it. §8 pre-commits: every CH-ID must be SATURATED (response from
>= 1 DOMAIN section AND >= 1 LIFECYCLE section) before BRACKET CLOSING executes. The saturation check
section makes this condition explicit and machine-auditable. Waiver protocol handles legitimate gaps.

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
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§8;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
[Fill this section before proceeding. This is the pre-reviewer gate.]

IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive.)

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
    CH-ID SATURATION CHECK: produces no verdict; coverage verification only. No row emitted.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical execution sequence:
    1. ROLE MANIFEST
    2. BRACKET OPENING
    3. DOMAIN(s)
    3.5. DOMAIN-AGGREGATE CHECKPOINT  [excluded from gate ledger per §6]
    3.8. CH-ID SATURATION CHECK       [excluded from gate ledger per §6]
    4. LIFECYCLE
    5. BRACKET CLOSING
  Reordering any section violates this contract. LIFECYCLE must precede BRACKET CLOSING.
  CH-ID SATURATION CHECK must precede LIFECYCLE.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  Before LIFECYCLE executes, each CH-ID must satisfy the saturation condition:
    SATURATED:   CH-ID has a response in >= 1 DOMAIN section.
  Before BRACKET CLOSING executes, each CH-ID must satisfy the full saturation condition:
    FULLY SATURATED: CH-ID has a response in >= 1 DOMAIN section AND in the LIFECYCLE section.
  A PASS verdict from BRACKET CLOSING is prohibited when any CH-ID is not FULLY SATURATED
  without a stated saturation waiver.
  Saturation waiver format: "CH-XXX WAIVER: [LIFECYCLE not applicable -- one sentence reason]"
  Waivers are emitted in CH-ID SATURATION CHECK and carried to ACTION ITEM REGISTER as ADVISORY.
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

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. CHALLENGER positions remain fixed.
State total count.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW -- how strong is the case for doing nothing?]

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

*GOpen and all CH-IDs above carry forward to every downstream section.*

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

**Additional Findings**:
1. [FINDING_1 -- from this role's `lens.verify` and `expertise.depth`. Names an in-scope surface.]
2. [FINDING_2]
3. [FINDING_3 -- optional]
4. [FINDING_4 -- optional]

**Severity**: [HIGH / MEDIUM / LOW]
*Per contract §2. Do not copy GOpen severity.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence. If CONDITIONAL: name condition. If FAIL: name gap.]

*(For `--depth deep`: repeat labeled DOMAIN-2, DOMAIN-3. Each emits own local ledger row.)*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per contract §6 -- this section produces no verdict.)*

**Applying §3a formula** *(do not alter; copy G_domain verdict(s) from above; apply worst-case rule)*:

```
G_domain rows collected:
  DOMAIN -- [ROLE_NAME]: [PASS / CONDITIONAL / FAIL]
  (DOMAIN-2 -- [ROLE_NAME]: [PASS / CONDITIONAL / FAIL] if --depth deep)

G_domain_agg = worst([list]) = [PASS / CONDITIONAL / FAIL]
```

**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

*This value carries forward to LIFECYCLE and BRACKET CLOSING as the authoritative domain signal.*

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger per contract §6 -- this section produces no verdict.
Runs after DOMAIN-AGGREGATE CHECKPOINT, before LIFECYCLE, per §7 sequence.)*

**Applying §8 formula** *(verify each CH-ID received a DOMAIN response before LIFECYCLE executes)*:

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN -- copy from DOMAIN CH-ID table] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED -- or N/A if not active] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None"]

*LIFECYCLE may proceed. Full saturation check (domain + lifecycle) will execute at BRACKET CLOSING.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]
Received G_domain Aggregate: [PASS / CONDITIONAL / FAIL -- copy from §3.5]

**CH-ID Response Table** *(mandatory per contract §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [Is evidence sufficient for commitment given both received
verdicts? One paragraph referencing GOpen and G_domain Aggregate explicitly.]

**Null hypothesis status**: [Given GOpen and G_domain, has the null hypothesis been defeated?
yes / partial / no -- one sentence of justification.]

**Additional Findings**:
1. [FINDING_1 -- from this role's `lens.verify`. Commitment, program, or decision concerns.]
2. [FINDING_2]

**Severity**: [HIGH / MEDIUM / LOW]
*Per contract §2.*

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

**Full CH-ID Saturation Check** *(per contract §8 -- PASS verdict prohibited if any CH-ID not FULLY SATURATED without waiver)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver (if needed) |
|-------|--------------|-----------------|-----------------|---------------------|
| CH-001 | [copy from DOMAIN] | [copy from LIFECYCLE] | [FULLY SATURATED / UNSATURATED] | [WAIVER text or N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER text or N/A] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER text or N/A] |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy from DOMAIN] | [copy from LIFECYCLE] | [DEFEATED / PARTIAL / HOLDS] | [ONE_SENTENCE_NOTE] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [What was not fully addressed. If none: "None -- all CH-IDs DEFEATED."]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
- PASS (= DEFEATED): All CH-IDs DEFEATED and FULLY SATURATED -- null hypothesis defeated.
- CONDITIONAL (= PARTIAL): Some CH-IDs PARTIAL or UNSATURATED-with-waiver -- material gaps remain.
- FAIL (= HOLDS): At least one CH-ID HOLDS -- null hypothesis survives.

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts. A HOLDS verdict
from the challenger is not overturned by G_domain or G_lifecycle PASSes. This override is
pre-stated in the contract §3 and is not subject to editorial revision at the Disposition step.

**GClose Rationale**: [2-3 sentences explaining the verdict.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

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

**Conflicts**: [Two reviewers with incompatible CH-ID responses or incompatible findings --
name roles and tension. If none: "None detected."]

**Convergence**: [Any CH-ID or concern named independently by two or more reviewers -- name it
and state why it is the highest-confidence signal in this review.]

**Scope coverage**: [Any in-scope surface from contract §1 not covered by any reviewer -- list
it. If all covered: "None -- full in-scope surface reviewed."]

---

## DISPOSITION

**Gate vector** *(fill from GATE VECTOR TABLE above)*:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula** *(do not alter the formula; do not reason editorially -- evaluate
the gate vector against the pre-stated formula)*:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED -- result of evaluating the formula above]

**Primary driver**: [The gate verdict most responsible for this disposition -- one sentence.
Do not reason from findings -- the formula completed the derivation.]

**Conditions** *(complete only if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate -- what must be resolved to upgrade to PASS.]
2. [Additional conditions if present.]

**Blocker** *(complete only if BLOCKED)*: [Specific finding from the FAIL gate.]

---

## ACTION ITEM REGISTER

*Copy all Local Gate Ledger rows from BRACKET OPENING, DOMAIN(s), LIFECYCLE, and BRACKET
CLOSING verbatim. Do not re-derive Gate Verdict or Class. The register is a copy, not a synthesis.
One additional row per PARTIAL or HOLDS CH-ID from BRACKET CLOSING. Items from §8 waivers
are marked ADVISORY. Items not sourced from a CH-ID or gate verdict are marked ADVISORY-OBS.*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [copy from local ledger] | [copy] | [copy] | [copy] | [What must be done] | [ROLE_NAME] | [Specific criterion] |
| CH-001 | -- | -- | [BLOCKED/CONDITIONAL/ADVISORY] | [Item from CH-ID status] | [ROLE_NAME] | [Criterion] |
| §8 WAIVER | -- | -- | ADVISORY | [Waiver text if any] | [ROLE_NAME] | [N/A or criterion] |
| -- | -- | -- | ADVISORY-OBS | [Advisory observation not from CH-ID] | [ROLE_NAME] | [Criterion] |

*Disposition class derives from gate verdict per contract §6:*
*FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY*

---

**Artifact to review:**

{{artifact}}
```

---

## V-02 -- Single Axis: Null Hypothesis Progression Contract

**Variation axis**: Null Hypothesis Progression Contract (new §8 in DISPOSITION_CONTRACT +
g_null progression tracking fields added to BRACKET OPENING, §3.5, and BRACKET CLOSING).

**Hypothesis**: The current architecture checks the null hypothesis in BRACKET OPENING (g_null initial)
and reassesses it in BRACKET CLOSING (g_null final), but the transition rule between initial and final
is editorial -- the challenger at bracket closing may return a verdict inconsistent with intermediate
domain and lifecycle evidence without violating any stated contract. §8 pre-commits the 3-stage
progression formula: g_null(initial) -> g_null(post-domain) -> g_null(final). The formula is
mechanical: domain aggregate determines whether the null hypothesis can be promoted or demoted from its
initial state; lifecycle determines the final promotion or demotion. A bracket closing verdict that
deviates from the formula requires an explicit stated justification. This makes the null hypothesis
trajectory auditable across sections.

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
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§8;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
[Fill this section before proceeding. This is the pre-reviewer gate.]

IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive.)

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

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical execution sequence:
    1. ROLE MANIFEST
    2. BRACKET OPENING
    3. DOMAIN(s)
    3.5. DOMAIN-AGGREGATE CHECKPOINT  [excluded from gate ledger per §6]
    4. LIFECYCLE
    5. BRACKET CLOSING
  Reordering any section violates this contract. LIFECYCLE must precede BRACKET CLOSING.

§8 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  The null hypothesis verdict evolves through three stages. Each stage is derived mechanically.
  Do not assign g_null values editorially -- apply the formula.

  Stage 1 -- g_null(initial) [emitted at BRACKET OPENING]:
    g_null(initial) = GOpen verdict directly.
    PASS = artifact appears to defeat null; CONDITIONAL = partial defeat; FAIL = null holds.

  Stage 2 -- g_null(post-domain) [emitted at §3.5 DOMAIN-AGGREGATE CHECKPOINT]:
    if G_domain_agg = FAIL:        g_null(post-domain) = FAIL   [domain cannot defeat null]
    if G_domain_agg = CONDITIONAL: g_null(post-domain) = max(g_null(initial), CONDITIONAL)
                                   [CONDITIONAL at minimum; can only worsen from PASS to CONDITIONAL]
    if G_domain_agg = PASS:        g_null(post-domain) = g_null(initial)  [domain confirms initial]
    Scale: FAIL < CONDITIONAL < PASS. "max" returns the more favorable verdict.

  Stage 3 -- g_null(final) [emitted at BRACKET CLOSING]:
    if G_lifecycle = FAIL:        g_null(final) = FAIL
    if G_lifecycle = CONDITIONAL: g_null(final) = max(g_null(post-domain), CONDITIONAL)
    if G_lifecycle = PASS:        g_null(final) = g_null(post-domain)  [lifecycle confirms]

  GClose verdict must equal g_null(final) unless an override is invoked with explicit justification.
  Override format: "g_null OVERRIDE: [reason the formula does not apply -- one sentence]"
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

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. CHALLENGER positions remain fixed.
State total count.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW -- how strong is the case for doing nothing?]

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

**g_null(initial)** *(per contract §8 Stage 1 -- equals GOpen)*: [PASS / CONDITIONAL / FAIL]

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

**Additional Findings**:
1. [FINDING_1 -- from this role's `lens.verify` and `expertise.depth`. Names an in-scope surface.]
2. [FINDING_2]
3. [FINDING_3 -- optional]
4. [FINDING_4 -- optional]

**Severity**: [HIGH / MEDIUM / LOW]
*Per contract §2. Do not copy GOpen severity.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence. If CONDITIONAL: name condition. If FAIL: name gap.]

*(For `--depth deep`: repeat labeled DOMAIN-2, DOMAIN-3. Each emits own local ledger row.)*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per contract §6 -- this section produces no verdict.)*

**Applying §3a formula** *(do not alter; copy G_domain verdict(s) from above; apply worst-case rule)*:

```
G_domain rows collected:
  DOMAIN -- [ROLE_NAME]: [PASS / CONDITIONAL / FAIL]
  (DOMAIN-2 -- [ROLE_NAME]: [PASS / CONDITIONAL / FAIL] if --depth deep)

G_domain_agg = worst([list]) = [PASS / CONDITIONAL / FAIL]
```

**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

**Applying §8 Stage 2 formula** *(derive g_null(post-domain) from g_null(initial) and G_domain_agg)*:

```
g_null(initial)  = [copy from BRACKET OPENING]
G_domain_agg     = [copy from above]

Apply §8 Stage 2:
  if G_domain_agg = FAIL:        g_null(post-domain) = FAIL
  if G_domain_agg = CONDITIONAL: g_null(post-domain) = max(g_null(initial), CONDITIONAL)
  if G_domain_agg = PASS:        g_null(post-domain) = g_null(initial)

g_null(post-domain) = [FAIL / CONDITIONAL / PASS]
```

**g_null(post-domain)**: [FAIL / CONDITIONAL / PASS]

*Both G_domain_agg and g_null(post-domain) carry forward to LIFECYCLE and BRACKET CLOSING.*

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

**Decision-readiness assessment**: [Is evidence sufficient for commitment given both received
verdicts? One paragraph referencing GOpen and G_domain Aggregate explicitly.]

**Null hypothesis status**: [Given GOpen and G_domain, has the null hypothesis been defeated?
yes / partial / no -- one sentence of justification. Reference g_null(post-domain).]

**Additional Findings**:
1. [FINDING_1 -- from this role's `lens.verify`. Commitment, program, or decision concerns.]
2. [FINDING_2]

**Severity**: [HIGH / MEDIUM / LOW]
*Per contract §2.*

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

**Applying §8 Stage 3 formula** *(derive g_null(final) from g_null(post-domain) and G_lifecycle)*:

```
g_null(post-domain) = [copy from §3.5]
G_lifecycle         = [copy from LIFECYCLE local ledger]

Apply §8 Stage 3:
  if G_lifecycle = FAIL:        g_null(final) = FAIL
  if G_lifecycle = CONDITIONAL: g_null(final) = max(g_null(post-domain), CONDITIONAL)
  if G_lifecycle = PASS:        g_null(final) = g_null(post-domain)

g_null(final) = [FAIL / CONDITIONAL / PASS]
```

**g_null(final)**: [FAIL / CONDITIONAL / PASS]

*GClose verdict must equal g_null(final). If it differs, state override justification below.*

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy from DOMAIN] | [copy from LIFECYCLE] | [DEFEATED / PARTIAL / HOLDS] | [ONE_SENTENCE_NOTE] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [What was not fully addressed. If none: "None -- all CH-IDs DEFEATED."]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
*Must equal g_null(final) unless override is invoked.*
**g_null Override**: [N/A -- formula applied directly | or: override justification one sentence]

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts. A HOLDS verdict
from the challenger is not overturned by G_domain or G_lifecycle PASSes. This override is
pre-stated in the contract §3 and is not subject to editorial revision at the Disposition step.

**GClose Rationale**: [2-3 sentences explaining the verdict. Reference g_null(final) explicitly.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

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

**Conflicts**: [Two reviewers with incompatible CH-ID responses or incompatible findings --
name roles and tension. If none: "None detected."]

**Convergence**: [Any CH-ID or concern named independently by two or more reviewers -- name it
and state why it is the highest-confidence signal in this review.]

**Null hypothesis progression summary**: [Three values in sequence: g_null(initial) ->
g_null(post-domain) -> g_null(final). State whether the trajectory was monotonic or reversed,
and which section caused any reversal.]

**Scope coverage**: [Any in-scope surface from contract §1 not covered by any reviewer -- list
it. If all covered: "None -- full in-scope surface reviewed."]

---

## DISPOSITION

**Gate vector** *(fill from GATE VECTOR TABLE above)*:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula** *(do not alter the formula; do not reason editorially)*:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Null hypothesis progression** *(per §8)*:
- g_null(initial) = [copy from BRACKET OPENING]
- g_null(post-domain) = [copy from §3.5]
- g_null(final) = [copy from BRACKET CLOSING]
- Trajectory: [monotonic / reversed at DOMAIN / reversed at LIFECYCLE]

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Primary driver**: [The gate verdict most responsible for this disposition -- one sentence.]

**Conditions** *(complete only if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]
2. [Additional conditions if present.]

**Blocker** *(complete only if BLOCKED)*: [Specific finding from the FAIL gate.]

---

## ACTION ITEM REGISTER

*Copy all Local Gate Ledger rows from BRACKET OPENING, DOMAIN(s), LIFECYCLE, and BRACKET
CLOSING verbatim. Do not re-derive Gate Verdict or Class. One additional row per PARTIAL or
HOLDS CH-ID from BRACKET CLOSING. Items not sourced from a CH-ID or gate verdict: ADVISORY-OBS.*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [copy from local ledger] | [copy] | [copy] | [copy] | [What must be done] | [ROLE_NAME] | [Specific criterion] |
| CH-001 | -- | -- | [BLOCKED/CONDITIONAL/ADVISORY] | [Item from CH-ID status] | [ROLE_NAME] | [Criterion] |
| -- | -- | -- | ADVISORY-OBS | [Advisory observation] | [ROLE_NAME] | [Criterion] |

*Disposition class derives from gate verdict per contract §6:*
*FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY*

---

**Artifact to review:**

{{artifact}}
```

---

## V-03 -- Single Axis: Scope Coverage Reconciliation Gate

**Variation axis**: Scope Coverage Gate (new §8 in DISPOSITION_CONTRACT + new SCOPE COVERAGE
RECONCILIATION section after BRACKET CLOSING, before GATE VECTOR TABLE).

**Hypothesis**: The §1 SCOPE ENUMERATION declares IN-SCOPE surfaces before any reviewer runs, but no
gate verifies that every declared surface received at least one finding before DISPOSITION executes.
A surface in §1 that no reviewer addressed is a silent coverage gap: the artifact was evaluated on
surfaces the reviewers chose to cover, not the surfaces declared in scope. §8 pre-commits a coverage
gate: after BRACKET CLOSING, a SCOPE COVERAGE RECONCILIATION section maps each §1 IN-SCOPE surface
to the reviewer(s) that addressed it. Unaddressed surfaces are forced to LOW advisory status and added
to the ACTION ITEM REGISTER as ADVISORY-GAP items. The gate emits a COVERED / PARTIAL signal but does
not itself block commitment -- coverage gaps are informational, not blocking.

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
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§8;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
[Fill this section before proceeding. This is the pre-reviewer gate.]

IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive. These rows are cited in SCOPE COVERAGE RECONCILIATION.)

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
    SCOPE COVERAGE RECONCILIATION: produces no gate verdict; coverage signal only. No row emitted.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical execution sequence:
    1. ROLE MANIFEST
    2. BRACKET OPENING
    3. DOMAIN(s)
    3.5. DOMAIN-AGGREGATE CHECKPOINT     [excluded from gate ledger per §6]
    4. LIFECYCLE
    5. BRACKET CLOSING
    5.5. SCOPE COVERAGE RECONCILIATION   [excluded from gate ledger per §6]
    6. GATE VECTOR TABLE
    7. CROSS-ROLE SIGNALS
    8. DISPOSITION
    9. ACTION ITEM REGISTER
  Reordering any section violates this contract. LIFECYCLE must precede BRACKET CLOSING.
  SCOPE COVERAGE RECONCILIATION must precede GATE VECTOR TABLE.

§8 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  After BRACKET CLOSING, SCOPE COVERAGE RECONCILIATION maps each §1 IN-SCOPE surface to the
  reviewer(s) that addressed it. Coverage rules:
    COVERED: surface named in >= 1 finding from >= 1 reviewer section.
    GAP:     surface not named in any reviewer finding.
  Gap handling (pre-committed -- apply mechanically):
    GAP surfaces receive forced LOW advisory status.
    GAP surfaces are added to ACTION ITEM REGISTER as ADVISORY-GAP items.
    Attribution: "SCOPE COVERAGE GATE / [surface name] / not addressed by any reviewer"
  Gate signal (informational only -- does not feed §3 formula):
    COVERED: all §1 IN-SCOPE surfaces addressed.
    PARTIAL: >= 1 §1 IN-SCOPE surface not addressed.
  A PARTIAL coverage signal does not block commitment. It appears in CROSS-ROLE SIGNALS.
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

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. CHALLENGER positions remain fixed.
State total count.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW -- how strong is the case for doing nothing?]

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

*GOpen and all CH-IDs above carry forward to every downstream section.*

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

**Additional Findings**:
1. [FINDING_1 -- from this role's `lens.verify` and `expertise.depth`. Names an in-scope surface.]
2. [FINDING_2]
3. [FINDING_3 -- optional]
4. [FINDING_4 -- optional]

**Severity**: [HIGH / MEDIUM / LOW]
*Per contract §2. Do not copy GOpen severity.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence. If CONDITIONAL: name condition. If FAIL: name gap.]

*(For `--depth deep`: repeat labeled DOMAIN-2, DOMAIN-3. Each emits own local ledger row.)*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per contract §6 -- this section produces no verdict.)*

**Applying §3a formula** *(do not alter; copy G_domain verdict(s) from above; apply worst-case rule)*:

```
G_domain rows collected:
  DOMAIN -- [ROLE_NAME]: [PASS / CONDITIONAL / FAIL]
  (DOMAIN-2 -- [ROLE_NAME]: [PASS / CONDITIONAL / FAIL] if --depth deep)

G_domain_agg = worst([list]) = [PASS / CONDITIONAL / FAIL]
```

**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

*This value carries forward to LIFECYCLE and BRACKET CLOSING as the authoritative domain signal.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]
Received G_domain Aggregate: [PASS / CONDITIONAL / FAIL -- copy from §3.5]

**CH-ID Response Table** *(mandatory per contract §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [Is evidence sufficient for commitment given both received
verdicts? One paragraph referencing GOpen and G_domain Aggregate explicitly.]

**Null hypothesis status**: [Given GOpen and G_domain, has the null hypothesis been defeated?
yes / partial / no -- one sentence of justification.]

**Additional Findings**:
1. [FINDING_1 -- from this role's `lens.verify`. Commitment, program, or decision concerns.]
2. [FINDING_2]

**Severity**: [HIGH / MEDIUM / LOW]
*Per contract §2.*

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

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy from DOMAIN] | [copy from LIFECYCLE] | [DEFEATED / PARTIAL / HOLDS] | [ONE_SENTENCE_NOTE] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [What was not fully addressed. If none: "None -- all CH-IDs DEFEATED."]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
- PASS (= DEFEATED): All CH-IDs DEFEATED -- accumulated record defeats the null hypothesis.
- CONDITIONAL (= PARTIAL): Some CH-IDs PARTIAL -- material gaps remain; name them.
- FAIL (= HOLDS): At least one CH-ID HOLDS -- null hypothesis survives.

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts. A HOLDS verdict
from the challenger is not overturned by G_domain or G_lifecycle PASSes. This override is
pre-stated in the contract §3 and is not subject to editorial revision at the Disposition step.

**GClose Rationale**: [2-3 sentences explaining the verdict.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per contract §6. Runs after BRACKET CLOSING, before GATE VECTOR
TABLE, per §7 sequence. Applies §8 SCOPE COVERAGE GATE PROTOCOL.)*

**Mapping §1 IN-SCOPE surfaces to reviewer findings** *(cite by section + finding number)*:

| IN-SCOPE Surface | Reviewer(s) | Finding Reference | Coverage |
|-----------------|-------------|-------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [DOMAIN Finding 1 / CH-001 / etc.] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [reference] | [COVERED / GAP] |

**Coverage gate signal** *(per §8 -- informational only; does not feed §3 formula)*:
[COVERED -- all surfaces addressed | PARTIAL -- [N] surface(s) not addressed]

**Forced advisory items** *(GAP surfaces per §8 -- copy to ACTION ITEM REGISTER as ADVISORY-GAP)*:
- [GAP surface 1: "SCOPE COVERAGE GATE / [surface name] / not addressed by any reviewer"]
- [or: "None -- all surfaces covered"]

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

**Conflicts**: [Two reviewers with incompatible CH-ID responses or incompatible findings --
name roles and tension. If none: "None detected."]

**Convergence**: [Any CH-ID or concern named independently by two or more reviewers -- name it
and state why it is the highest-confidence signal in this review.]

**Scope coverage**: [Restate coverage gate signal from SCOPE COVERAGE RECONCILIATION.
If PARTIAL: list unaddressed surfaces. If COVERED: "None -- full in-scope surface reviewed."]

---

## DISPOSITION

**Gate vector** *(fill from GATE VECTOR TABLE above)*:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula** *(do not alter the formula; do not reason editorially)*:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Primary driver**: [The gate verdict most responsible for this disposition -- one sentence.]

**Conditions** *(complete only if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]
2. [Additional conditions if present.]

**Blocker** *(complete only if BLOCKED)*: [Specific finding from the FAIL gate.]

---

## ACTION ITEM REGISTER

*Copy all Local Gate Ledger rows from BRACKET OPENING, DOMAIN(s), LIFECYCLE, and BRACKET
CLOSING verbatim. Do not re-derive Gate Verdict or Class. One additional row per PARTIAL or
HOLDS CH-ID from BRACKET CLOSING. ADVISORY-GAP rows from SCOPE COVERAGE RECONCILIATION
are appended after gate ledger rows.*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [copy from local ledger] | [copy] | [copy] | [copy] | [What must be done] | [ROLE_NAME] | [Specific criterion] |
| CH-001 | -- | -- | [BLOCKED/CONDITIONAL/ADVISORY] | [Item from CH-ID status] | [ROLE_NAME] | [Criterion] |
| SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [Surface not addressed] | [ROLE_NAME] | [Criterion] |
| -- | -- | -- | ADVISORY-OBS | [Advisory observation] | [ROLE_NAME] | [Criterion] |

*Disposition class derives from gate verdict per contract §6:*
*FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY*
*ADVISORY-GAP: unaddressed §1 surface per §8 -- advisory, does not block commitment.*

---

**Artifact to review:**

{{artifact}}
```

---

## V-04 -- Combination: V-01 + V-02 (CH-ID Saturation + Null Progression)

**Variation axes**: §8 CH-ID SATURATION REQUIREMENT + §9 NULL HYPOTHESIS PROGRESSION CONTRACT.
Both single-axis contracts combined; new sections CH-ID SATURATION CHECK and g_null tracking fields.

**Hypothesis**: V-01 and V-02 address independent failure modes (cross-section CH-ID coverage gap and
inconsistent null hypothesis progression). Combining them tests whether the two contracts are composable
without structural conflict. §8 (CH-ID Saturation) gates LIFECYCLE entry; §9 (Null Progression) gates
BRACKET CLOSING's GClose verdict. They operate at different points in the execution order and should
not interfere. If both hold simultaneously, a new C-27 or C-28 pattern may emerge from the full
cross-section traceability chain: CH-ID saturation -> g_null progression -> bracket closing verdict.

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
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§9;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
[Fill this section before proceeding. This is the pre-reviewer gate.]

IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive.)

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
    CH-ID SATURATION CHECK: produces no verdict; coverage verification only. No row emitted.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical execution sequence:
    1. ROLE MANIFEST
    2. BRACKET OPENING
    3. DOMAIN(s)
    3.5. DOMAIN-AGGREGATE CHECKPOINT  [excluded from gate ledger per §6]
    3.8. CH-ID SATURATION CHECK       [excluded from gate ledger per §6]
    4. LIFECYCLE
    5. BRACKET CLOSING
  Reordering any section violates this contract. LIFECYCLE must precede BRACKET CLOSING.
  CH-ID SATURATION CHECK must precede LIFECYCLE.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  Before LIFECYCLE executes, each CH-ID must satisfy the saturation condition:
    SATURATED:   CH-ID has a response in >= 1 DOMAIN section.
  Before BRACKET CLOSING executes, each CH-ID must satisfy the full saturation condition:
    FULLY SATURATED: CH-ID has a response in >= 1 DOMAIN section AND in the LIFECYCLE section.
  A PASS verdict from BRACKET CLOSING is prohibited when any CH-ID is not FULLY SATURATED
  without a stated saturation waiver.
  Saturation waiver format: "CH-XXX WAIVER: [LIFECYCLE not applicable -- one sentence reason]"
  Waivers are emitted in CH-ID SATURATION CHECK and carried to ACTION ITEM REGISTER as ADVISORY.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  The null hypothesis verdict evolves through three stages. Each stage is derived mechanically.
  Do not assign g_null values editorially -- apply the formula.

  Stage 1 -- g_null(initial) [emitted at BRACKET OPENING]:
    g_null(initial) = GOpen verdict directly.

  Stage 2 -- g_null(post-domain) [emitted at §3.5 DOMAIN-AGGREGATE CHECKPOINT]:
    if G_domain_agg = FAIL:        g_null(post-domain) = FAIL
    if G_domain_agg = CONDITIONAL: g_null(post-domain) = max(g_null(initial), CONDITIONAL)
    if G_domain_agg = PASS:        g_null(post-domain) = g_null(initial)
    Scale: FAIL < CONDITIONAL < PASS. "max" returns the more favorable verdict.

  Stage 3 -- g_null(final) [emitted at BRACKET CLOSING]:
    if G_lifecycle = FAIL:        g_null(final) = FAIL
    if G_lifecycle = CONDITIONAL: g_null(final) = max(g_null(post-domain), CONDITIONAL)
    if G_lifecycle = PASS:        g_null(final) = g_null(post-domain)

  GClose verdict must equal g_null(final) unless an override is invoked with explicit justification.
  Override format: "g_null OVERRIDE: [reason the formula does not apply -- one sentence]"
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

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. CHALLENGER positions remain fixed.
State total count.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW -- how strong is the case for doing nothing?]

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

**Additional Findings**:
1. [FINDING_1 -- from this role's `lens.verify` and `expertise.depth`. Names an in-scope surface.]
2. [FINDING_2]
3. [FINDING_3 -- optional]
4. [FINDING_4 -- optional]

**Severity**: [HIGH / MEDIUM / LOW]
*Per contract §2. Do not copy GOpen severity.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*(For `--depth deep`: repeat labeled DOMAIN-2, DOMAIN-3. Each emits own local ledger row.)*

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

G_domain_agg = [PASS / CONDITIONAL / FAIL]
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

*Both G_domain_agg and g_null(post-domain) carry forward.*

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger per contract §6. Runs after DOMAIN-AGGREGATE CHECKPOINT, before
LIFECYCLE, per §7 sequence. Applies §8 pre-LIFECYCLE saturation requirement.)*

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN -- copy from DOMAIN CH-ID table] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED -- or N/A] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None"]
*LIFECYCLE may proceed. Full saturation check (domain + lifecycle) will execute at BRACKET CLOSING.*

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

**Decision-readiness assessment**: [One paragraph referencing GOpen and G_domain Aggregate explicitly.]

**Null hypothesis status**: [yes / partial / no -- reference g_null(post-domain).]

**Additional Findings**:
1. [FINDING_1]
2. [FINDING_2]

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

**Full CH-ID Saturation Check** *(per contract §8)*:

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
**g_null Override**: [N/A -- formula applied | or: override justification]

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts per contract §3.

**GClose Rationale**: [2-3 sentences. Reference g_null(final) and CH-ID saturation status.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

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

**Conflicts**: [Incompatible CH-ID responses or findings -- name roles and tension. If none: "None."]

**Convergence**: [CH-ID or concern named by two or more reviewers -- name it and explain confidence.]

**Null hypothesis progression**: [g_null(initial) -> g_null(post-domain) -> g_null(final).
State whether trajectory was monotonic or reversed, and which section caused any reversal.]

**Scope coverage**: [Any §1 surface not addressed. If all covered: "None -- full coverage."]

---

## DISPOSITION

**Gate vector**:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula**:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Null hypothesis progression** *(per §9)*:
- g_null(initial) = [copy] | g_null(post-domain) = [copy] | g_null(final) = [copy]
- Trajectory: [monotonic / reversed at DOMAIN / reversed at LIFECYCLE]

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Primary driver**: [One sentence.]

**Conditions** *(if CONDITIONAL)*: [List conditions.]

**Blocker** *(if BLOCKED)*: [Specific finding.]

---

## ACTION ITEM REGISTER

*Copy all Local Gate Ledger rows verbatim. No re-derivation. CH-ID PARTIAL/HOLDS items appended.
§8 waiver items appended as ADVISORY.*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [copy from local ledger] | [copy] | [copy] | [copy] | [What must be done] | [ROLE_NAME] | [Criterion] |
| CH-001 | -- | -- | [class] | [Item from CH-ID status] | [ROLE_NAME] | [Criterion] |
| §8 WAIVER | -- | -- | ADVISORY | [Waiver text if any] | [ROLE_NAME] | [N/A or criterion] |
| -- | -- | -- | ADVISORY-OBS | [Advisory observation] | [ROLE_NAME] | [Criterion] |

---

**Artifact to review:**

{{artifact}}
```

---

## V-05 -- Full Integration: V-01 + V-02 + V-03

**Variation axes**: §8 CH-ID SATURATION REQUIREMENT + §9 NULL HYPOTHESIS PROGRESSION CONTRACT +
§10 SCOPE COVERAGE GATE + new CH-ID SATURATION CHECK section (pre-LIFECYCLE) + new SCOPE COVERAGE
RECONCILIATION section (post-BRACKET CLOSING).

**Hypothesis**: All three V-01/V-02/V-03 axes are structurally independent and activate at different
points in the execution order. §8 CH-ID Saturation activates at §3.8 (pre-LIFECYCLE) and BRACKET
CLOSING. §9 Null Progression activates at BRACKET OPENING, §3.5, and BRACKET CLOSING. §10 Scope
Coverage activates at §5.5 (post-BRACKET CLOSING). No two contracts govern the same section-level
decision, so they should compose without conflict. If all three hold simultaneously, the review
achieves: (1) cross-section CH-ID coverage chain; (2) null hypothesis trajectory under contract;
(3) declared-scope-to-finding traceability. These together form a complete pre-commitment audit
trail for every major decision in the review. A new C-27 pattern may emerge from the combination
that none of the three single-axis variations can exhibit alone.

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
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§10;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
[Fill this section before proceeding. This is the pre-reviewer gate.]

IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive. These rows are cited in SCOPE COVERAGE RECONCILIATION.)

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

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. CHALLENGER positions remain fixed.
State total count.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW -- how strong is the case for doing nothing?]

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

**Additional Findings**:
1. [FINDING_1 -- from this role's `lens.verify` and `expertise.depth`. Names an in-scope surface.]
2. [FINDING_2]
3. [FINDING_3 -- optional]
4. [FINDING_4 -- optional]

**Severity**: [HIGH / MEDIUM / LOW]
*Per contract §2.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*(For `--depth deep`: repeat labeled DOMAIN-2, DOMAIN-3. Each emits own local ledger row.)*

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

**Decision-readiness assessment**: [One paragraph referencing GOpen and G_domain Aggregate and
g_null(post-domain) explicitly.]

**Null hypothesis status**: [yes / partial / no -- reference g_null(post-domain).]

**Additional Findings**:
1. [FINDING_1 -- commitment, program, or decision concerns.]
2. [FINDING_2]

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
**g_null Override**: [N/A -- formula applied | or: override justification]

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts per contract §3.

**GClose Rationale**: [2-3 sentences. Reference g_null(final), CH-ID saturation, and null hypothesis
trajectory (initial -> post-domain -> final).]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per contract §6. Runs after BRACKET CLOSING, before GATE VECTOR
TABLE, per §7 sequence. Applies §10 SCOPE COVERAGE GATE PROTOCOL.)*

**Mapping §1 IN-SCOPE surfaces to reviewer findings** *(cite by section + finding number)*:

| IN-SCOPE Surface | Reviewer(s) | Finding Reference | Coverage |
|-----------------|-------------|-------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [DOMAIN Finding 1 / CH-001 / etc.] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [reference] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [reference] | [COVERED / GAP] |

**Coverage gate signal** *(per §10 -- informational; does not feed §3 formula)*:
[COVERED -- all surfaces addressed | PARTIAL -- [N] surface(s) not addressed]

**Forced advisory items** *(GAP surfaces per §10 -- appended to ACTION ITEM REGISTER as ADVISORY-GAP)*:
- [GAP surface 1: "SCOPE COVERAGE GATE / [surface name] / not addressed by any reviewer"]
- [or: "None -- all surfaces covered"]

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

**Conflicts**: [Incompatible CH-ID responses or findings -- name roles and tension. If none: "None."]

**Convergence**: [CH-ID or concern named by two or more reviewers -- name it and explain confidence.]

**Null hypothesis progression** *(§9 trajectory)*: [g_null(initial) -> g_null(post-domain) ->
g_null(final). State whether monotonic or reversed, and which section caused any reversal.]

**Scope coverage** *(§10 gate signal)*: [Restate coverage gate signal. If PARTIAL: list surfaces.
If COVERED: "None -- full in-scope surface reviewed."]

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

**Null hypothesis progression** *(§9 -- informational summary)*:
- g_null(initial) = [copy] | g_null(post-domain) = [copy] | g_null(final) = [copy]
- Trajectory: [monotonic / reversed at DOMAIN / reversed at LIFECYCLE]

**Scope coverage** *(§10 -- informational)*: [COVERED / PARTIAL]

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Primary driver**: [The gate verdict most responsible -- one sentence.]

**Conditions** *(if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]
2. [Additional conditions if present.]

**Blocker** *(if BLOCKED)*: [Specific finding from the FAIL gate.]

---

## ACTION ITEM REGISTER

*Copy all Local Gate Ledger rows from BRACKET OPENING, DOMAIN(s), LIFECYCLE, and BRACKET
CLOSING verbatim. Do not re-derive Gate Verdict or Class. Append: CH-ID PARTIAL/HOLDS rows,
§8 waiver rows (ADVISORY), §10 ADVISORY-GAP rows from SCOPE COVERAGE RECONCILIATION.*

| Section | Gate | Verdict | Class | Item Description | Owner Role | Resolution Criterion |
|---------|------|---------|-------|-----------------|------------|---------------------|
| [copy from local ledger] | [copy] | [copy] | [copy] | [What must be done] | [ROLE_NAME] | [Criterion] |
| CH-001 | -- | -- | [class] | [Item from CH-ID status] | [ROLE_NAME] | [Criterion] |
| §8 WAIVER | -- | -- | ADVISORY | [Waiver text if any] | [ROLE_NAME] | [N/A] |
| §10 SCOPE COVERAGE GATE | -- | -- | ADVISORY-GAP | [Surface not addressed] | [ROLE_NAME] | [Criterion] |
| -- | -- | -- | ADVISORY-OBS | [Advisory observation not from CH-ID or gate] | [ROLE_NAME] | [Criterion] |

*Disposition class per §6: FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY*
*ADVISORY-GAP: unaddressed §1 surface per §10 -- advisory, does not block commitment.*

---

**Artifact to review:**

{{artifact}}
```

---

## Round 9 Variation Summary

| Variation | New Axis | New Contracts | New Sections | V-05 R8 Base |
|-----------|----------|---------------|--------------|--------------|
| V-01 | CH-ID Saturation Pre-gate | §8 CH-ID SATURATION REQUIREMENT | §3.8 CH-ID SATURATION CHECK | yes |
| V-02 | Null Hypothesis Progression | §8 NULL HYPOTHESIS PROGRESSION CONTRACT | g_null fields in §3.5 + BRACKET CLOSING | yes |
| V-03 | Scope Coverage Reconciliation | §8 SCOPE COVERAGE GATE PROTOCOL | §5.5 SCOPE COVERAGE RECONCILIATION | yes |
| V-04 | V-01 + V-02 combined | §8 CH-ID SATURATION + §9 NULL PROGRESSION | §3.8 + g_null fields | yes |
| V-05 | V-01 + V-02 + V-03 | §8 CH-ID SATURATION + §9 NULL PROGRESSION + §10 SCOPE COVERAGE | §3.8 + g_null fields + §5.5 | yes |

**Predicted C-27 extraction candidates**:
- **C-27a** (from V-01/V-04/V-05 if held): "CH-ID Cross-Section Coverage Pre-committed as Saturation Requirement" -- all CH-IDs must receive responses from both domain AND lifecycle archetypes, verified at a dedicated pre-gate section before BRACKET CLOSING.
- **C-27b** (from V-02/V-04/V-05 if held): "Null Hypothesis Progression Formula Pre-committed" -- g_null evolves through 3 mechanically-derived stages; bracket closing verdict is formula-bound, not editorial.
- **C-27c** (from V-03/V-05 if held): "Scope-to-Finding Coverage Gate After Bracket Closing" -- each §1 IN-SCOPE surface traces to >= 1 reviewer finding; unaddressed surfaces forced to ADVISORY-GAP before DISPOSITION.

**Key test**: Can V-05 hold all three simultaneously without structural conflict? If yes, C-27 extraction follows.
