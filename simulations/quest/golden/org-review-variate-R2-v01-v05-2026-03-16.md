# org-review Variations — Round 2 — 2026-03-16

Rubric: org-review-rubric-v2-2026-03-16.md
Targets: C-11 (verdict-preview tables), C-12 (count constraint)

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Count constraint | "exactly N rows" in §5 + BRACKET OPENING count field converts silent CH-ID drop to numeric violation |
| V-02 | Verdict-preview tables | Pre-printed Verdict columns at section headers make convergence a table-scan, not inference |
| V-03 | Inertia prominence | NULL HYPOTHESIS REGISTER before reviewer sections produces named-competitor null hypotheses |
| V-04 | C-11 + C-12 combined | V-01 and V-02 are independent and additive; both structural targets in one prompt |
| V-05 | Full integration | V-04 + inertia register + LIFECYCLE-before-DOMAIN resequencing |

Single-axis variations: V-01, V-02, V-03
Combination variations: V-04 (V-01+V-02), V-05 (V-01+V-02+V-03+role-sequence)

---

## V-01 — Count Constraint (C-12 target)

**Axis**: Count constraint injection
**Hypothesis**: Injecting "exactly N rows" language into §5 and at every CH-ID table header converts a silent CH-ID drop into a detectable numeric violation. The model cannot omit a row without producing a count mismatch that a scorer can detect mechanically.

**Changes from baseline**: §5 adds count constraint + count declaration field in BRACKET OPENING + "exactly N rows" on every CH-ID table header in DOMAIN, LIFECYCLE, BRACKET CLOSING.

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A — reason]`.

---

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
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, CH-002, ...).
  CH-ID COUNT: N = the number of CH-IDs declared in BRACKET OPENING. Record N
    in the "CH-ID Count declared" field immediately after the Challenge Claims table.
  Every downstream CH-ID table must contain exactly N rows — one row per declared CH-ID.
    A table with fewer than N rows is a §5 count violation regardless of other completeness.
    A table with more than N rows invents claims not in evidence — also a §5 violation.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

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

**CH-ID Count declared**: N = [fill — count the rows above. This number binds all downstream
  tables per contract §5. Every downstream CH-ID table must contain exactly N rows.]

**Verify Question**: [One from challenger's `lens.verify`.]

**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

*GOpen and all N CH-IDs above carry forward. Downstream tables: exactly N rows each.*

---

## DOMAIN — [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL — copy from BRACKET OPENING]

**CH-ID Response Table** *(exactly N rows — N from BRACKET OPENING "CH-ID Count declared" —
a row count other than N is a §5 contract violation)*:

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

**CH-ID Response Table** *(exactly N rows — N from BRACKET OPENING "CH-ID Count declared" —
a row count other than N is a §5 contract violation)*:

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

**CH-ID Final Assessment** *(exactly N rows — N from BRACKET OPENING "CH-ID Count declared" —
a row count other than N is a §5 contract violation)*:

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
1. [Condition from first CONDITIONAL gate — what must be resolved to upgrade to PASS.]
2. [Additional conditions if present.]

**Blocker** *(complete only if BLOCKED)*: [Specific finding from the FAIL gate. If GClose = FAIL,
lead with: "Challenger final verdict HOLDS — [GClose Rationale summary]."]

---

## ACTION ITEM REGISTER

*One row per PARTIAL or HOLDS CH-ID from BRACKET CLOSING. Items not sourced from a CH-ID are
marked ADVISORY-OBS. This register is the CH-ID-indexed synthesis artifact per contract §5.*

| CH-ID | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|-------|-----------------|------------------|------------|---------------------|
| CH-001 | [What must be done] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [One sentence: what must be true to close this item] |
| CH-002 | [Item 2] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [Resolution criterion] |
| — | [Advisory observation not sourced from a CH-ID, if any] | ADVISORY-OBS | [ROLE_NAME] | [Criterion] |

*Disposition class per contract §2:*
- **BLOCKED**: Must be resolved before any commitment.
- **CONDITIONAL**: Must be resolved before proceeding to next lifecycle phase.
- **ADVISORY**: May be deferred. Commitment may proceed.

*Every row traces: BRACKET OPENING CH-ID → reviewer CH-ID tables → BRACKET CLOSING final status.*

---

**Artifact to review:**

{{artifact}}
```

---

## V-02 — Verdict-Preview Tables (C-11 target)

**Axis**: Structural convergence via verdict-preview tables
**Hypothesis**: Pre-printing CH-ID rows with an empty Verdict column at each section header makes cross-role convergence detection a table-scan operation. The model fills verdict cells; the scorer detects convergence by comparing columns without re-reading prose.

**Changes from baseline**: Add a "Verdict Preview" stub table at the top of DOMAIN, LIFECYCLE, and BRACKET CLOSING sections. Add a CH-ID Cross-Gate Tally table in BRACKET CLOSING. Upgrade CROSS-ROLE SIGNALS Convergence field to consume the tally table.

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A — reason]`.

---

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

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

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

**CH-ID Verdict Preview** *(fill the Status column now — one word per row — before writing
the full response table below. This table is the convergence anchor for CROSS-ROLE SIGNALS.)*:

| CH-ID | Status |
|-------|--------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [ADDRESSED / PARTIAL / OPEN — omit if not active] |

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

**CH-ID Verdict Preview** *(fill the Status column now — before writing the full response table)*:

| CH-ID | Status |
|-------|--------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [ADDRESSED / PARTIAL / OPEN — omit if not active] |

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

**CH-ID Cross-Gate Tally** *(copy from DOMAIN and LIFECYCLE Verdict Preview tables above —
scan for convergence: same non-ADDRESSED status across both gates = high-confidence signal)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Converged? |
|-------|--------------|-----------------|-----------|
| CH-001 | [copy from DOMAIN preview] | [copy from LIFECYCLE preview] | [yes — if both PARTIAL or both OPEN / no] |
| CH-002 | [copy] | [copy] | [yes / no] |
| CH-003 | [copy if active] | [copy if active] | [yes / no] |

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

**Convergence** *(scan CH-ID Cross-Gate Tally in BRACKET CLOSING — rows where Converged = yes
are the highest-confidence signals; name each by CH-ID and explain why dual-gate confirmation
raises confidence. If no Converged = yes rows: "None detected — no CH-ID flagged by both gates.")*:

**Conflicts**: [Two reviewers with incompatible CH-ID responses or incompatible findings —
name roles and tension. If none: "None detected."]

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
1. [Condition from first CONDITIONAL gate.]
2. [Additional conditions if present.]

**Blocker** *(complete only if BLOCKED)*: [Specific finding from the FAIL gate. If GClose = FAIL,
lead with: "Challenger final verdict HOLDS — [GClose Rationale summary]."]

---

## ACTION ITEM REGISTER

*One row per PARTIAL or HOLDS CH-ID from BRACKET CLOSING. Items not sourced from a CH-ID are
marked ADVISORY-OBS. This register is the CH-ID-indexed synthesis artifact per contract §5.*

| CH-ID | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|-------|-----------------|------------------|------------|---------------------|
| CH-001 | [What must be done] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [One sentence: what must be true to close this item] |
| CH-002 | [Item 2] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [Resolution criterion] |
| — | [Advisory observation not sourced from a CH-ID, if any] | ADVISORY-OBS | [ROLE_NAME] | [Criterion] |

*Every row traces: BRACKET OPENING CH-ID → reviewer CH-ID tables → BRACKET CLOSING final status.*

---

**Artifact to review:**

{{artifact}}
```

---

## V-03 — Inertia Prominence (C-09 target)

**Axis**: Inertia framing
**Hypothesis**: A NULL HYPOTHESIS REGISTER block inserted before BRACKET OPENING — requiring a named tool, process, or workaround — forces the model to produce a specific inertia competitor before the challenger begins. This feeds C-09 (specific null hypothesis) without execution-time inference.

**Changes from baseline**: Add NULL HYPOTHESIS REGISTER section between §1 COMPLETE and BRACKET OPENING. BRACKET OPENING null hypothesis field references the Register. LIFECYCLE null hypothesis status field is upgraded to cite specific Register evidence. DISPOSITION adds a null hypothesis defeat line.

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A — reason]`.

---

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

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close — fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. CHALLENGER positions remain fixed.
State total count.)*

---

## NULL HYPOTHESIS REGISTER

*Complete before BRACKET OPENING. This is the challenger's evidence frame — not editorial.
Name the concrete alternative the team uses today. Generic phrases ("do nothing", "status quo")
are not acceptable; name the specific tool, process, or workaround.*

| Field | Value |
|-------|-------|
| What teams use today | [Specific tool, process, or workaround the team relies on instead of building this] |
| Why it works well enough | [One sentence — the genuine case for continuing with the status quo] |
| Where it breaks down | [One sentence — the gap or friction that motivates this artifact] |
| Switching cost | [HIGH / MEDIUM / LOW] |
| Null hypothesis strength | [HIGH / MEDIUM / LOW — how viable is the current approach overall?] |

*This register is the source of truth for null hypothesis fields throughout the review.*

---

## BRACKET OPENING — CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis** *(from NULL HYPOTHESIS REGISTER — name the specific tool or process)*:
[The team continues to use [TOOL/PROCESS from Register] because [WHY IT WORKS from Register].
One sentence. Do not substitute generic language.]

**Null hypothesis strength**: [Copy from NULL HYPOTHESIS REGISTER — HIGH / MEDIUM / LOW]

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

**Null hypothesis status** *(reference NULL HYPOTHESIS REGISTER — name the specific tool/process)*:
Given GOpen and G_domain Aggregate, the null hypothesis — [restate from Register: specific
tool/process] — is: [DEFEATED / PARTIALLY DEFEATED / STILL VIABLE]. Justification: [one sentence
citing specific CH-ID statuses that support this assessment.]

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

**GClose Rationale**: [2-3 sentences explaining the verdict. Reference the specific tool/process
from NULL HYPOTHESIS REGISTER when stating whether the null hypothesis holds or is defeated.]

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

**Null hypothesis defeat** *(from LIFECYCLE null hypothesis status and GClose verdict)*:
[DEFEATED / PARTIALLY DEFEATED / HOLDS — copy from LIFECYCLE null hypothesis status. If GClose
= FAIL, write: "HOLDS — challenger final verdict: [specific tool/process from Register] remains
the team's viable alternative."]

**Primary driver**: [The gate verdict most responsible for this disposition — one sentence.]

**Conditions** *(complete only if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]
2. [Additional conditions if present.]

**Blocker** *(complete only if BLOCKED)*: [Specific finding from the FAIL gate.]

---

## ACTION ITEM REGISTER

*One row per PARTIAL or HOLDS CH-ID from BRACKET CLOSING. Items not sourced from a CH-ID are
marked ADVISORY-OBS. This register is the CH-ID-indexed synthesis artifact per contract §5.*

| CH-ID | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|-------|-----------------|------------------|------------|---------------------|
| CH-001 | [What must be done] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [One sentence: what must be true to close this item] |
| CH-002 | [Item 2] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [Resolution criterion] |
| — | [Advisory observation not sourced from a CH-ID, if any] | ADVISORY-OBS | [ROLE_NAME] | [Criterion] |

*Every row traces: BRACKET OPENING CH-ID → reviewer CH-ID tables → BRACKET CLOSING final status.*

---

**Artifact to review:**

{{artifact}}
```

---

## V-04 — Count Constraint + Verdict-Preview Tables (C-11 + C-12 combined)

**Axis**: Both Round 1 excellence signals applied simultaneously
**Hypothesis**: V-01 (count constraint) and V-02 (verdict-preview tables) are structurally independent and additive. Combining both should yield max composite on C-03, C-08, C-11, and C-12 simultaneously.

**Changes from baseline**: All V-01 changes (§5 count constraint, CH-ID Count declared field, "exactly N rows" on all CH-ID tables) PLUS all V-02 changes (Verdict Preview stubs at DOMAIN and LIFECYCLE, CH-ID Cross-Gate Tally at BRACKET CLOSING, convergence-scan instruction in CROSS-ROLE SIGNALS).

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A — reason]`.

---

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
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, CH-002, ...).
  CH-ID COUNT: N = the number of CH-IDs declared in BRACKET OPENING. Record N
    in the "CH-ID Count declared" field immediately after the Challenge Claims table.
  Every downstream CH-ID table must contain exactly N rows — one row per declared CH-ID.
    A table with fewer than N rows is a §5 count violation regardless of other completeness.
    A table with more than N rows invents claims not in evidence — also a §5 violation.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

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

**CH-ID Count declared**: N = [fill — count the rows above. Every downstream CH-ID table
  must contain exactly N rows per contract §5.]

**Verify Question**: [One from challenger's `lens.verify`.]

**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

*GOpen and all N CH-IDs above carry forward. Downstream tables: exactly N rows each.*

---

## DOMAIN — [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL — copy from BRACKET OPENING]

**CH-ID Verdict Preview** *(fill the Status column now — one word per row — before writing
the full response table. This table is the convergence anchor for CROSS-ROLE SIGNALS.)*:

| CH-ID | Status |
|-------|--------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [ADDRESSED / PARTIAL / OPEN — omit if not active] |

**CH-ID Response Table** *(exactly N rows — N from BRACKET OPENING "CH-ID Count declared" —
a row count other than N is a §5 contract violation — PASS verdict prohibited if any row = OPEN)*:

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

**CH-ID Verdict Preview** *(fill the Status column now — before writing the full response table)*:

| CH-ID | Status |
|-------|--------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [ADDRESSED / PARTIAL / OPEN — omit if not active] |

**CH-ID Response Table** *(exactly N rows — N from BRACKET OPENING "CH-ID Count declared" —
a row count other than N is a §5 contract violation)*:

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

**CH-ID Cross-Gate Tally** *(copy from DOMAIN and LIFECYCLE Verdict Preview tables above —
scan for convergence: same non-ADDRESSED status in both columns = high-confidence signal)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Converged? |
|-------|--------------|-----------------|-----------|
| CH-001 | [copy from DOMAIN preview] | [copy from LIFECYCLE preview] | [yes / no] |
| CH-002 | [copy] | [copy] | [yes / no] |
| CH-003 | [copy if active] | [copy if active] | [yes / no] |

**CH-ID Final Assessment** *(exactly N rows — N from BRACKET OPENING "CH-ID Count declared" —
a row count other than N is a §5 contract violation)*:

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

**Convergence** *(scan CH-ID Cross-Gate Tally in BRACKET CLOSING — rows where Converged = yes
are the highest-confidence signals; name each by CH-ID. If no converged rows: "None detected.")*:

**Conflicts**: [Two reviewers with incompatible CH-ID responses or incompatible findings —
name roles and tension. If none: "None detected."]

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
1. [Condition from first CONDITIONAL gate.]
2. [Additional conditions if present.]

**Blocker** *(complete only if BLOCKED)*: [Specific finding from the FAIL gate. If GClose = FAIL,
lead with: "Challenger final verdict HOLDS — [GClose Rationale summary]."]

---

## ACTION ITEM REGISTER

*One row per PARTIAL or HOLDS CH-ID from BRACKET CLOSING. Items not sourced from a CH-ID are
marked ADVISORY-OBS. This register is the CH-ID-indexed synthesis artifact per contract §5.*

| CH-ID | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|-------|-----------------|------------------|------------|---------------------|
| CH-001 | [What must be done] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [One sentence: what must be true to close this item] |
| CH-002 | [Item 2] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [Resolution criterion] |
| — | [Advisory observation not sourced from a CH-ID, if any] | ADVISORY-OBS | [ROLE_NAME] | [Criterion] |

*Every row traces: BRACKET OPENING CH-ID → reviewer CH-ID tables → BRACKET CLOSING final status.*

---

**Artifact to review:**

{{artifact}}
```

---

## V-05 — Full Integration (C-11 + C-12 + Inertia + Role Sequence)

**Axis**: All structural improvements + LIFECYCLE-before-DOMAIN resequencing
**Hypothesis**: Running LIFECYCLE (commitment readiness) before DOMAIN (technical depth) surfaces "can we commit at all?" blockers before the technical reviewer expends effort. Combined with count constraint and verdict-preview tables, this maximizes composite score across all tiers.

**Changes from baseline**:
- V-01: §5 count constraint + CH-ID Count declared field + "exactly N rows" on all CH-ID tables
- V-02: Verdict Preview stubs at LIFECYCLE and DOMAIN; CH-ID Cross-Gate Tally at BRACKET CLOSING; convergence-scan in CROSS-ROLE SIGNALS
- V-03: NULL HYPOTHESIS REGISTER before BRACKET OPENING; named-competitor null hypothesis fields
- Role sequence: LIFECYCLE runs before DOMAIN; LIFECYCLE receives GOpen; DOMAIN receives GOpen + G_lifecycle; GATE VECTOR TABLE reflects execution order (GOpen, G_lifecycle, G_domain, GClose); §3 algebra unchanged (operates on the gate set, not execution order)

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A — reason]`.

---

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
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, CH-002, ...).
  CH-ID COUNT: N = the number of CH-IDs declared in BRACKET OPENING. Record N
    in the "CH-ID Count declared" field immediately after the Challenge Claims table.
  Every downstream CH-ID table must contain exactly N rows — one row per declared CH-ID.
    A table with fewer than N rows is a §5 count violation regardless of other completeness.
    A table with more than N rows invents claims not in evidence — also a §5 violation.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close — fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |

*Execution order: BRACKET OPENING → LIFECYCLE → DOMAIN → BRACKET CLOSING.*
*LIFECYCLE runs first to surface commitment-readiness blockers before technical depth.*
*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. CHALLENGER positions remain fixed.
State total count.)*

---

## NULL HYPOTHESIS REGISTER

*Complete before BRACKET OPENING. Name the concrete alternative the team uses today.
Generic phrases ("do nothing", "status quo") are not acceptable.*

| Field | Value |
|-------|-------|
| What teams use today | [Specific tool, process, or workaround the team relies on instead of building this] |
| Why it works well enough | [One sentence — the genuine case for continuing with the status quo] |
| Where it breaks down | [One sentence — the gap that motivates this artifact] |
| Switching cost | [HIGH / MEDIUM / LOW] |
| Null hypothesis strength | [HIGH / MEDIUM / LOW] |

*This register is the source of truth for all null hypothesis fields in this review.*

---

## BRACKET OPENING — CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis** *(from NULL HYPOTHESIS REGISTER — name the specific tool or process)*:
[The team continues to use [TOOL/PROCESS from Register] because [WHY IT WORKS from Register].
One sentence. Do not substitute generic language.]

**Null hypothesis strength**: [Copy from NULL HYPOTHESIS REGISTER — HIGH / MEDIUM / LOW]

**Challenge claims** *(assign CH-IDs; carry to every downstream section per contract §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1 — switching cost, workaround viability, or adoption friction. One sentence.] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 — optional] | [HIGH / MEDIUM / LOW] |

**CH-ID Count declared**: N = [fill — count the rows above. Every downstream CH-ID table
  must contain exactly N rows per contract §5.]

**Verify Question**: [One from challenger's `lens.verify`.]

**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

*GOpen and all N CH-IDs above carry forward. Execution continues: LIFECYCLE → DOMAIN → BRACKET CLOSING.*

---

## LIFECYCLE — [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL — copy from BRACKET OPENING]
*(DOMAIN has not yet run. LIFECYCLE assesses commitment readiness from GOpen alone.)*

**CH-ID Verdict Preview** *(fill the Status column now — before writing the full response table)*:

| CH-ID | Status |
|-------|--------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [ADDRESSED / PARTIAL / OPEN — omit if not active] |

**CH-ID Response Table** *(exactly N rows — N from BRACKET OPENING "CH-ID Count declared" —
a row count other than N is a §5 contract violation)*:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [Is evidence sufficient to proceed to technical review?
One paragraph referencing GOpen explicitly. Note: G_domain is not yet available — assess
commitment readiness from challenger framing alone.]

**Null hypothesis status** *(reference NULL HYPOTHESIS REGISTER)*:
Given GOpen, the null hypothesis — [restate: specific tool/process from Register] — is:
[STILL VIABLE / CHALLENGED / OPEN]. Justification: [one sentence. Note: full defeat requires
DOMAIN review; this is a preliminary commitment-readiness assessment.]

**Additional Findings**:
1. [FINDING_1 — from this role's `lens.verify`. Commitment, program, or decision concerns.]
2. [FINDING_2]

**Severity**: [HIGH / MEDIUM / LOW]
*Per contract §2.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence. If FAIL: execution should pause — DOMAIN review may
be deferred until this gate is resolved.]

---

## DOMAIN — [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL — copy from BRACKET OPENING]
Received G_lifecycle: [PASS / CONDITIONAL / FAIL — copy from LIFECYCLE]

**CH-ID Verdict Preview** *(fill the Status column now — before writing the full response table.
This table is the convergence anchor vs LIFECYCLE Verdict Preview above.)*:

| CH-ID | Status |
|-------|--------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [ADDRESSED / PARTIAL / OPEN — omit if not active] |

**CH-ID Response Table** *(exactly N rows — N from BRACKET OPENING "CH-ID Count declared" —
a row count other than N is a §5 contract violation — PASS verdict prohibited if any row = OPEN)*:

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
*Per contract §2. Do not copy GOpen or G_lifecycle severity.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence. If CONDITIONAL: name condition. If FAIL: name gap.]

*(For `--depth deep`: repeat labeled DOMAIN-2, DOMAIN-3. G_domain Aggregate = worst verdict
among all DOMAIN rows. State aggregate explicitly below.)*

**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL — worst among all DOMAIN rows]

---

## BRACKET CLOSING — CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: scope declaration, all CH-ID tables, all gate verdicts.*

**CH-ID Cross-Gate Tally** *(copy from LIFECYCLE and DOMAIN Verdict Preview tables above —
scan for convergence: same non-ADDRESSED status in both columns = high-confidence signal)*:

| CH-ID | LIFECYCLE Status | DOMAIN Status | Converged? |
|-------|-----------------|--------------|-----------|
| CH-001 | [copy from LIFECYCLE preview] | [copy from DOMAIN preview] | [yes / no] |
| CH-002 | [copy] | [copy] | [yes / no] |
| CH-003 | [copy if active] | [copy if active] | [yes / no] |

**CH-ID Final Assessment** *(exactly N rows — N from BRACKET OPENING "CH-ID Count declared" —
a row count other than N is a §5 contract violation)*:

| CH-ID | G_lifecycle Status | G_domain Status | Final Status | Notes |
|-------|-------------------|----------------|--------------|-------|
| CH-001 | [copy from LIFECYCLE] | [copy from DOMAIN] | [DEFEATED / PARTIAL / HOLDS] | [ONE_SENTENCE_NOTE] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [What was not fully addressed. If none: "None — all CH-IDs DEFEATED."]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
- PASS (= DEFEATED): All CH-IDs DEFEATED — accumulated record defeats the null hypothesis.
- CONDITIONAL (= PARTIAL): Some CH-IDs PARTIAL — material gaps remain; name them.
- FAIL (= HOLDS): At least one CH-ID HOLDS — null hypothesis survives.

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts. A HOLDS verdict
from the challenger is not overturned by G_lifecycle or G_domain PASses. This override is
pre-stated in the contract §3 and is not subject to editorial revision at the Disposition step.

**GClose Rationale**: [2-3 sentences. Reference the specific tool/process from NULL HYPOTHESIS
REGISTER when stating whether it has been defeated.]

---

## GATE VECTOR TABLE

*(Execution order: GOpen → G_lifecycle → G_domain → GClose. §3 algebra operates on the set —
order does not affect the disposition formula.)*

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen — bracket opening | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle — lifecycle | [LIFECYCLE_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain — domain aggregate | [DOMAIN_ROLE(S)] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose — bracket closing | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Convergence** *(scan CH-ID Cross-Gate Tally in BRACKET CLOSING — rows where Converged = yes
are the highest-confidence signals; name each by CH-ID. If no converged rows: "None detected.")*:

**Conflicts**: [Two reviewers with incompatible CH-ID responses or incompatible findings —
name roles and tension. If none: "None detected."]

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

**Null hypothesis defeat** *(from GClose verdict and NULL HYPOTHESIS REGISTER)*:
[DEFEATED / PARTIALLY DEFEATED / HOLDS — one sentence. If GClose = FAIL: "HOLDS — [specific
tool/process from Register] remains the team's viable alternative: [GClose Rationale summary]."]

**Primary driver**: [The gate verdict most responsible for this disposition — one sentence.
Do not reason from findings — the formula completed the derivation.]

**Conditions** *(complete only if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate. Gate order for resolution: GOpen → G_lifecycle → G_domain → GClose.]
2. [Additional conditions if present.]

**Blocker** *(complete only if BLOCKED)*: [Specific finding from the FAIL gate.]

---

## ACTION ITEM REGISTER

*One row per PARTIAL or HOLDS CH-ID from BRACKET CLOSING. Items not sourced from a CH-ID are
marked ADVISORY-OBS. This register is the CH-ID-indexed synthesis artifact per contract §5.*

| CH-ID | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|-------|-----------------|------------------|------------|---------------------|
| CH-001 | [What must be done] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [One sentence: what must be true to close this item] |
| CH-002 | [Item 2] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [Resolution criterion] |
| — | [Advisory observation not sourced from a CH-ID, if any] | ADVISORY-OBS | [ROLE_NAME] | [Criterion] |

*Every row traces: BRACKET OPENING CH-ID → reviewer CH-ID tables → BRACKET CLOSING final status.*

---

**Artifact to review:**

{{artifact}}
```

---

## Variation Summary

| Variation | C-11 | C-12 | C-09 | Role seq | Primary engineering target |
|-----------|------|------|------|----------|---------------------------|
| V-01 | — | YES | — | standard | §5 count constraint alone |
| V-02 | YES | — | — | standard | Verdict-preview tables alone |
| V-03 | — | — | YES | standard | Inertia register alone |
| V-04 | YES | YES | — | standard | Both Round 1 excellence signals |
| V-05 | YES | YES | YES | LIFECYCLE first | Full integration |

**Predicted score ranking** (against rubric v2):
1. V-05 — all four aspirational criteria in scope; role-sequence tests whether LIFECYCLE-first affects C-10
2. V-04 — C-11 + C-12 reliably; C-09 execution-dependent
3. V-02 — C-11 structural; C-12 missing means C-03 still execution-dependent
4. V-01 — C-12 structural; C-11 missing means C-08 still execution-dependent
5. V-03 — C-09 improved; no structural change for C-11/C-12

**Expected excellence patterns to watch**:
- E-3 hypothesis: V-05 LIFECYCLE-first may improve C-10 (role-grounded findings) because LIFECYCLE reviewers see the artifact before DOMAIN, potentially producing more commitment-framed findings
- E-4 hypothesis: V-04 vs V-05 delta isolates the role-sequence effect from the structural improvements
