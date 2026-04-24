You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A — reason]`.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK — complete §1 scope fields; do not alter §2-§5;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 — SCOPE ENUMERATION
[Fill this section before proceeding. This is the pre-reviewer gate.]

IN-SCOPE — surfaces this review will evaluate:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive.)

OUT-OF-SCOPE — surfaces this review will not evaluate:
  1. [SURFACE — REASON_EXCLUDED]
  (Write "None" if nothing is excluded.)

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE — [reason]
  Silent scope expansion violates this contract.

§1 COMPLETE — role selection and reviewer gates proceed below.

§2 — SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment. No commitment proceeds with open HIGH findings.
  MEDIUM = Conditions commitment. Proceeds only after named resolution.
  LOW    = Advisory. Commitment may proceed.
  These definitions apply universally. They may not be restated at any gate.

§3 — DISPOSITION ALGEBRA [IMMUTABLE — evaluated at DISPOSITION section]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose = FAIL  [override: null hypothesis holds]
                OR  exists Gi = FAIL
  CONDITIONAL  <-- no Gi = FAIL  AND  exists Gi = CONDITIONAL
  READY        <-- all Gi = PASS

§4 — CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A missing cite is an audit-trail gap.

§5 — CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, ...).
  Every downstream section carries a mandatory CH-ID response table.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.
======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close — fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. CHALLENGER positions remain fixed.
State total count.)*

---

## BRACKET OPENING — CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this — one sentence.]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW — how strong is the case for doing nothing?]

**Challenge claims** *(assign CH-IDs; carry to every downstream section per contract §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1 — switching cost, workaround viability, or adoption friction. One sentence.] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 — optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]

**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

*GOpen and all CH-IDs above carry forward to every downstream section.*

---

## DOMAIN — [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL — copy from BRACKET OPENING]

**CH-ID Response Table** *(mandatory per contract §5 — PASS verdict prohibited if any row = OPEN)*:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | [copy full claim from BRACKET OPENING] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

*(PARTIAL requires a named resolution path. OPEN = claim not addressable from this role's frame.)*

**Additional Findings**:
1. [FINDING_1 — from this role's `lens.verify` and `expertise.depth`. Names an in-scope surface.]
2. [FINDING_2]
3. [FINDING_3 — optional]
4. [FINDING_4 — optional]

**Severity**: [HIGH / MEDIUM / LOW]
*Per contract §2. Do not copy GOpen severity.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence. If CONDITIONAL: name condition. If FAIL: name gap.]

*(For `--depth deep`: repeat labeled DOMAIN-2, DOMAIN-3. G_domain Aggregate = worst verdict
among all DOMAIN rows. State aggregate explicitly below.)*

**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL — worst among all DOMAIN rows]

---

## LIFECYCLE — [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL — copy from BRACKET OPENING]
Received G_domain Aggregate: [PASS / CONDITIONAL / FAIL — copy from DOMAIN aggregate]

**CH-ID Response Table** *(mandatory per contract §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [Is evidence sufficient for commitment given both received
verdicts? One paragraph referencing GOpen and G_domain Aggregate explicitly.]

**Null hypothesis status**: [Given GOpen and G_domain, has the null hypothesis been defeated?
yes / partial / no — one sentence of justification.]

**Additional Findings**:
1. [FINDING_1 — from this role's `lens.verify`. Commitment, program, or decision concerns.]
2. [FINDING_2]

**Severity**: [HIGH / MEDIUM / LOW]
*Per contract §2.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

---

## BRACKET CLOSING — CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: scope declaration, all CH-ID tables, all gate verdicts.*

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy from DOMAIN] | [copy from LIFECYCLE] | [DEFEATED / PARTIAL / HOLDS] | [ONE_SENTENCE_NOTE] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [What was not fully addressed. If none: "None — all CH-IDs DEFEATED."]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
- PASS (= DEFEATED): All CH-IDs DEFEATED — accumulated record defeats the null hypothesis.
- CONDITIONAL (= PARTIAL): Some CH-IDs PARTIAL — material gaps remain; name them.
- FAIL (= HOLDS): At least one CH-ID HOLDS — null hypothesis survives.

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts. A HOLDS verdict
from the challenger is not overturned by G_domain or G_lifecycle PASses. This override is
pre-stated in the contract §3 and is not subject to editorial revision at the Disposition step.

**GClose Rationale**: [2-3 sentences explaining the verdict.]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen — bracket opening | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain — domain aggregate | [DOMAIN_ROLE(S)] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle — lifecycle | [LIFECYCLE_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose — bracket closing | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Two reviewers with incompatible CH-ID responses or incompatible findings —
name roles and tension. If none: "None detected."]

**Convergence**: [Any CH-ID or concern named independently by two or more reviewers — name it
and state why it is the highest-confidence signal in this review.]

**Scope coverage**: [Any in-scope surface from contract §1 not covered by any reviewer — list
it. If all covered: "None — full in-scope surface reviewed."]

---

## DISPOSITION

**Gate vector** *(fill from GATE VECTOR TABLE above)*:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula** *(do not alter the formula; do not reason editorially — evaluate
the gate vector against the pre-stated formula)*:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED — result of evaluating the formula above]

**Primary driver**: [The gate verdict most responsible for this disposition — one sentence.
Do not reason from findings — the formula completed the derivation.]

**Conditions** *(complete only if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate — what must be resolved to upgrade to PASS. Gate order:
   GOpen before G_domain before G_lifecycle before GClose.]
2. [Additional conditions if present.]

**Blocker** *(complete only if BLOCKED)*: [Specific finding from the FAIL gate. If GClose = FAIL,
lead with: "Challenger final verdict HOLDS — [GClose Rationale summary]."]

---

## ACTION ITEM REGISTER

*One row per PARTIAL or HOLDS CH-ID from BRACKET CLOSING. Items not sourced from a CH-ID are
marked ADVISORY-OBS. This register is the CH-ID-indexed synthesis artifact per contract §5.*

| CH-ID | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|-------|-----------------|------------------|------------|---------------------|
| CH-001 | [What must be done — derived from the PARTIAL or HOLDS status of this claim] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [Specific statement of what must be true before this item can be closed — one sentence] |
| CH-002 | [Item 2] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [Resolution criterion] |
| — | [Advisory observation not sourced from a CH-ID, if any] | ADVISORY-OBS | [ROLE_NAME] | [Criterion] |

*Disposition class per contract §2:*
- **BLOCKED**: Must be resolved before any commitment. An open BLOCKED item = BLOCKED disposition.
- **CONDITIONAL**: Must be resolved before proceeding to next lifecycle phase.
- **ADVISORY**: May be deferred. Commitment may proceed.

*Every row in this register traces to a CH-ID from BRACKET OPENING → reviewer CH-ID tables →
BRACKET CLOSING final status. The full chain is navigable in either direction without
cross-referencing reviewer sections separately.*

---

**Artifact to review:**

{{artifact}}