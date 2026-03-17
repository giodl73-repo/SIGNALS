---
skill: quest-variate
skill_target: org-review
date: 2026-03-17
round: 19
rubric: org-review-rubric-v11-2026-03-16.md
---

# org-review -- Variate Round 19 (v11 rubric Round 7)

Generated: 2026-03-17
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v11-2026-03-16.md

## Prior round summary

- R1--R11: V-05 climbed to 210/225. All §1--§16 PASS. C-33/C-34/C-35 absent.
- R12 (v11 R1): V-02 scored ~215/225 -- C-33+C-34+C-35 PASS, §14/§15/§16 absent.
- R13--R15 (v11 R2--R4): Targeted individual placement of C-33/C-34/C-35.
- R16 (v11 R4): V-05 combined §17 manifest applicability + §18 domain gap-check +
  §19 NH dimension table. Failure modes: generic CERT justifications,
  conflated domain labels, underspecified VERDICT threshold.
- R17 (v11 R5): V-01 added §17a APPLICABILITY CERTIFICATION BLOCK (per-role
  justification); V-02 replaced prose gap-check with DOMAIN-ROLE COVERAGE MATRIX
  (rows = §1 domains, locked at matrix time); V-03 added CHALLENGER PRE-ASSESSMENT
  with NH DIMENSION TABLE and VERDICT column; V-05 combined all three.
- R18 (v11 R6): V-01 added CERT VALIDITY CHECK TABLE (3 binary columns, DOWNGRADE
  logic); V-02 added ARTIFACT DOMAIN INVENTORY LOCK STEP with SPLIT CHECK;
  V-03 added VERDICT THRESHOLD TABLE to §9 (D=F-O; D>=2 PASS, D=1/0 CONDITIONAL,
  D<=-1 FAIL). V-05 is the 225/225 candidate combining all three.

## Round 19 (v11 R7) strategy

Baseline: V-05 R18 (§1--§16 + §17a CERT BLOCK + §17b CERT VALIDITY CHECK TABLE +
§17c ARTIFACT DOMAIN INVENTORY + §17d DOMAIN-ROLE COVERAGE MATRIX + §9 VERDICT
THRESHOLD TABLE + DIMENSION TABLE in BRACKET OPENING).

Identified failure modes in V-05 R18:

- **C-33 residual**: §17b revision loop has no termination bound. After one revision
  cycle the CERT VALIDITY CHECK TABLE re-runs, but if the model writes a revised entry
  that nominally fills all fields while still citing artifact-type rather than a specific
  surface, the gate may cycle indefinitely or terminate early with a technically-valid-
  but-still-generic entry. No mechanism enforces "the named surface must exist in the
  artifact" -- the Basis Artifact-Specific column checks category (type vs. instance),
  not existence.

- **C-34 residual**: ARTIFACT DOMAIN INVENTORY SPLIT CHECK fires on qualitative
  judgment ("does this label cover more than one distinct concern?"). The AI may answer
  NO when the answer is YES because the concern decomposition is not mechanical. No
  enumerated trigger list exists; the SPLIT CHECK is prose-driven. A COVERED row may
  silently hide a gap inside a broad label even after SPLIT CHECK runs.

- **C-35 residual**: DIMENSION TABLE in BRACKET OPENING requires all F/O/Q cells, but
  NH TESTIMONY prose may be written before all dimension rows are assigned. The model
  may assign Category retrospectively after writing the prose argument, making the
  F/O/Q count derivable from prose rather than pre-locked. DIMENSION TABLE LOCKED
  statement is instructed but not gate-enforced before prose begins.

Round 19 targets one failure mode per single-axis variation, then combines:

- **V-01** (Lifecycle emphasis): REVISION TERMINATION BOUND on §17b. Max 1 revision
  cycle per role. If DOWNGRADE persists post-revision, role is EXCLUDED-LOW and does
  not execute a reviewer section. An ADVISORY coverage deficit is registered. Prevents
  infinite revision loops and makes C-33 resolution finitely auditable.

- **V-02** (Output format): MECHANICAL SPLIT TRIGGER LIST in §17c. Four named triggers
  that REQUIRE a split when any fires. Each label is audited against all four triggers.
  Outcome is a declared notation (SPLIT-REQUIRED or SPLIT-NOT-TRIGGERED with trigger
  audit) rather than a prose judgment. Makes C-34 gap-check derivable from trigger
  audit records.

- **V-03** (Inertia framing): DIMENSION PRE-LOCK PROTOCOL in §9 and BRACKET OPENING.
  DIMENSION TABLE must be fully completed with all Category cells (F/O/Q) and emitted
  with DIMENSION TABLE LOCKED statement before any NH TESTIMONY prose begins. NH
  TESTIMONY is structurally subordinate ("derived from locked table"). No dimension
  assessment admitted in prose that is not in the table. Makes C-35 verifiable from
  table alone.

- **V-04** (Lifecycle + Output format): V-01 + V-02.
- **V-05** (all three): V-01 + V-02 + V-03. 225/225 refined candidate.

**R19 single-axis predictions:**
- V-01 -> C-33 PASS tightened (revision bound makes EXCLUDED-LOW finitely detectable).
  Score same as V-05 R18 if revision bound never triggers; score may DROP if the
  base model relied on multiple revision cycles. Net: 225/225 if EXCLUDED-LOW is
  not invoked, or 220/225 if one DOMAIN role is EXCLUDED-LOW (C-08 depth PARTIAL).
- V-02 -> C-34 PASS tightened (SPLIT TRIGGER LIST eliminates editorial SPLIT CHECK).
  Predicted: 225/225.
- V-03 -> C-35 PASS tightened (DIMENSION PRE-LOCK enforces table-before-prose order).
  Predicted: 225/225.

**R19 two/three-axis predictions:**
- V-04 -> 225/225.
- V-05 -> 225/225 most conservative; all three failure modes simultaneously addressed.

---

## V-01

**Axis**: Lifecycle emphasis -- REVISION TERMINATION BOUND on §17b CERT VALIDITY CHECK
**Hypothesis**: V-05 R18's §17b CERT VALIDITY CHECK allows unlimited revision cycles.
A model that writes a nominally-revised but still generic entry (e.g., "Basis: this
role applies to compliance artifacts in general") can cycle without convergence, or
terminate after one cycle with an entry that passes the binary columns but whose
Basis sentence is not artifact-specific in a verifiable sense. Adding a hard revision
bound (max 1 cycle) forces one of two finite outcomes: (a) ALL-YES on first or revised
entry, or (b) EXCLUDED-LOW after one failed revision, with a coverage-deficit advisory
item. Predicted score: 225/225 when no EXCLUDED-LOW is invoked; 220/225 if a DOMAIN
role is EXCLUDED-LOW and depth falls below the C-08 floor.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this block first. Fill injected values.

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
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2--§17d;
reviewer sections may not execute until §1 COMPLETE, CERT VALIDITY
GATE = VALID, INVENTORY LOCK COMPLETE, and COVERAGE MATRIX COMPLETE
are all reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]
  (Add rows. Use specific domain labels -- one distinct concern per label.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]

§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions commitment. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose = FAIL OR exists Gi = FAIL
  CONDITIONAL <-- no FAIL AND exists CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts). FAIL > CONDITIONAL > PASS.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim receives CH-ID. Every downstream section carries CH-ID response
  table. PASS prohibited if any CH-ID row = OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section.
  Assembly: ACTION ITEM REGISTER copies verbatim. No re-derivation.
  EXCLUDED: §3.5, §3.8, §5.5, APPLICABILITY CERTIFICATION BLOCK,
            CERT VALIDITY CHECK TABLE, ARTIFACT DOMAIN INVENTORY,
            DOMAIN-ROLE COVERAGE MATRIX.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.   ROLE MANIFEST
  1.4. APPLICABILITY CERTIFICATION BLOCK  [per §17a; no ledger row]
  1.5. CERT VALIDITY CHECK TABLE          [per §17b; exit gate; no ledger row]
  1.6. ARTIFACT DOMAIN INVENTORY          [per §17c; no ledger row]
  1.7. DOMAIN-ROLE COVERAGE MATRIX        [per §17d; no ledger row]
  2.   BRACKET OPENING
  3.   DOMAIN(s)
  3.5. DOMAIN-AGGREGATE CHECKPOINT
  3.8. CH-ID SATURATION CHECK
  4.   LIFECYCLE
  5.   BRACKET CLOSING
  5.5. SCOPE COVERAGE RECONCILIATION
  6.   GATE VECTOR TABLE
  7.   CROSS-ROLE SIGNALS
  8.   DISPOSITION
  9.   ACTION ITEM REGISTER
  Reordering violates this contract.
  CERT VALIDITY GATE = VALID must be reached before step 1.6.
  INVENTORY LOCK COMPLETE must precede COVERAGE MATRIX (1.7).
  COVERAGE MATRIX must precede BRACKET OPENING (2).
  LIFECYCLE must precede BRACKET CLOSING.
  EXCLUDED-LOW roles (from §17b revision bound) are removed before step 1.6.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID in >= 1 DOMAIN section (before LIFECYCLE).
  FULLY SATURATED: CH-ID in DOMAIN + LIFECYCLE (before BRACKET CLOSING).
  PASS prohibited without full saturation or stated waiver.
  Waiver: "CH-XXX WAIVER: [reason]"

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  VERDICT THRESHOLD TABLE [IMMUTABLE]:
    D >= 2  --> g_null(initial) = PASS
    D = 1   --> g_null(initial) = CONDITIONAL
    D = 0   --> g_null(initial) = CONDITIONAL
    D <= -1 --> g_null(initial) = FAIL
  Stage 1: D = count(Category=F) - count(Category=O or Q) from DIMENSION TABLE.
           g_null(initial) = threshold_table[D]. D must be stated as a labeled field.
  Stage 2: g_null(post-domain):
    FAIL if G_domain_agg=FAIL;
    max(g_null(initial),CONDITIONAL) if G_domain_agg=CONDITIONAL;
    g_null(initial) if G_domain_agg=PASS.
  Stage 3: g_null(final):
    FAIL if G_lifecycle=FAIL;
    max(g_null(post-domain),CONDITIONAL) if G_lifecycle=CONDITIONAL;
    g_null(post-domain) if G_lifecycle=PASS.
  GClose must equal g_null(final) or declare override with named justification.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps each §1 IN-SCOPE surface to reviewer findings. GAP -> ADVISORY-GAP in register.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding cites "[§1:S-n]". No citation = ADVISORY-ORPHAN in register.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION = CONDITIONAL -> emit RESOLUTION REGISTRY table.

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  In CROSS-ROLE SIGNALS: g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Each finding row carries individual Severity. Section Severity = worst(all in section).

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE section emits LENS COVERAGE TABLE. Applicability from §17d
  matrix cell (this role x primary artifact domain). OPEN + HIGH-applicability ->
  ADVISORY-OPEN-LENS in register.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  GClose=FAIL -> GClose. G_domain=FAIL -> DOMAIN. G_lifecycle=FAIL -> LIFECYCLE.
  Any CONDITIONAL -> lowest-index gate. All PASS -> N/A.

§17 -- ROLE MANIFEST APPLICABILITY PROTOCOL [IMMUTABLE]
  ROLE MANIFEST includes Applicability column (HIGH/MEDIUM/LOW per role).
  HIGH = lens.verify directly addresses this artifact's primary domains.
  MEDIUM = partially addresses. LOW = limited applicability.
  §15 LENS COVERAGE TABLE inherits applicability from §17d matrix cell.

§17a -- APPLICABILITY CERTIFICATION REQUIREMENT [IMMUTABLE]
  After ROLE MANIFEST, before CERT VALIDITY CHECK TABLE, emit APPLICABILITY
  CERTIFICATION BLOCK. One entry per selected role. Format:
    Role [name]: Applicability = [HIGH/MEDIUM/LOW]
    Artifact domain: [specific §1 domain label this rating is based on]
    Lens.verify match: [specific lens.verify entry from this role's definition]
    Basis: [one sentence -- why this lens entry makes this role relevant to THIS
    artifact, not to the artifact type in general]
  Invalid: "relevant because [type] artifact" -- GENERIC.
  Invalid: no specific lens.verify entry cited -- INCOMPLETE.

§17b -- CERT VALIDITY CHECK REQUIREMENT [IMMUTABLE]
  After APPLICABILITY CERTIFICATION BLOCK, emit CERT VALIDITY CHECK TABLE.
  One row per role. Table:
    | Role | Domain Named (Y/N) | Lens Entry Quoted (Y/N) | Basis Artifact-Specific (Y/N) | Valid |
  Column rules (mechanical):
    Domain Named:             Y if Artifact domain names a specific §1 domain label.
    Lens Entry Quoted:        Y if Lens.verify match cites a specific entry from the
                              role definition (not a generic capability statement).
    Basis Artifact-Specific:  Y if Basis names a specific surface, section, field, or
                              behavior of THIS artifact (not of its type).
    Valid:                    ALL-YES if all three Y. DOWNGRADE if any N.
  REVISION BOUND [IMMUTABLE]:
    Max 1 revision cycle per role.
    If entry = DOWNGRADE: revise APPLICABILITY CERTIFICATION BLOCK and ROLE MANIFEST
    Applicability to LOW. Re-emit table once. If still DOWNGRADE after revision:
      Emit: "REVISION LIMIT REACHED: [role] -- EXCLUDED-LOW."
      Role is removed from active reviewer set.
      Add advisory: "ADVISORY: [role] EXCLUDED-LOW -- coverage deficit in [domain]."
    Revision count is tracked per-role (not globally).
  Emit CERT VALIDITY GATE:
    "CERT VALIDITY GATE: VALID [n roles active, m EXCLUDED-LOW] -- all active
    rows ALL-YES. Proceed to step 1.6."
    OR: "CERT VALIDITY GATE: INVALID -- [roles still DOWNGRADE]. Revise once."
  BRACKET OPENING is blocked until gate = VALID.

§17c -- ARTIFACT DOMAIN INVENTORY PROTOCOL [IMMUTABLE]
  After CERT VALIDITY GATE = VALID, before DOMAIN-ROLE COVERAGE MATRIX, emit
  ARTIFACT DOMAIN INVENTORY.
  Step 1 SCAN: extract all unique [DOMAIN: label] values from §1 IN-SCOPE rows.
  Step 2 DEDUPLICATE: one entry per unique label.
  Step 3 SPLIT CHECK: for each entry, ask: "Does this label cover more than one
    distinct concern that could independently have no HIGH-applicability reviewer?"
    If yes: split and update §1 annotations.
    State: "SPLIT: [original] -> [A], [B] -- reason"
    State: "KEPT: [label] -- single distinct concern"
  Step 4 LOCK: emit numbered list. State INVENTORY LOCK COUNT: N.
  Emit "INVENTORY LOCK COMPLETE -- matrix row count = N" before COVERAGE MATRIX.
  Note: active reviewer set excludes any EXCLUDED-LOW roles from §17b.

§17d -- DOMAIN-ROLE COVERAGE MATRIX CONTRACT [IMMUTABLE]
  After INVENTORY LOCK COMPLETE, produce DOMAIN-ROLE COVERAGE MATRIX.
  Rows: each locked domain from ARTIFACT DOMAIN INVENTORY.
  Columns: each ACTIVE role from ROLE MANIFEST (EXCLUDED-LOW roles absent).
  Cells: HIGH/MEDIUM/LOW/-- (role x domain applicability).
  Matrix row count must equal INVENTORY LOCK COUNT. Mismatch = contract violation;
  halt: "MATRIX CONTRACT VIOLATION: expected N rows, built M. Revise §1 annotations."
  Domain gap (mechanical): no HIGH cell in row -> DOMAIN-GAP ->
    Emit: "ADVISORY-GAP: [domain] -- no HIGH-applicability reviewer."
  §15 Applicability: use matrix cell for (this role, primary artifact domain).

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale | Applicability |
|------|-----------|------|---------------------|---------------|
| CHALLENGER (bracket open + close) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] | HIGH |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] | [H/M/L] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] | [H/M/L] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3 rows.)*

---

## APPLICABILITY CERTIFICATION BLOCK

*(Per §17a -- after ROLE MANIFEST, before CERT VALIDITY CHECK TABLE. No ledger row.)*

Role [challenger role name]: Applicability = HIGH
Artifact domain: [specific §1 domain label]
Lens.verify match: [specific lens.verify entry from this role's definition]
Basis: [one sentence -- why this lens entry applies to THIS artifact specifically]

Role [domain role name]: Applicability = [H/M/L]
Artifact domain: [specific §1 domain label with highest applicability]
Lens.verify match: [specific lens.verify entry]
Basis: [one sentence -- names a specific surface or behavior of THIS artifact]

Role [lifecycle role name]: Applicability = [H/M/L]
Artifact domain: [specific §1 domain label]
Lens.verify match: [specific lens.verify entry]
Basis: [one sentence -- names a specific surface of THIS artifact, not its type]

---

## CERT VALIDITY CHECK TABLE

*(Per §17b -- immediately after APPLICABILITY CERTIFICATION BLOCK. REVISION BOUND active. No ledger row.)*

| Role | Domain Named (Y/N) | Lens Entry Quoted (Y/N) | Basis Artifact-Specific (Y/N) | Valid |
|------|--------------------|------------------------|-------------------------------|-------|
| [challenger] | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |
| [domain]     | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |
| [lifecycle]  | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |

*(For any DOWNGRADE: revise APPLICABILITY CERTIFICATION BLOCK and lower Applicability to LOW.
Re-emit table ONCE. If still DOWNGRADE: emit "REVISION LIMIT REACHED: [role] -- EXCLUDED-LOW."
Remove EXCLUDED-LOW roles from active set. Register advisory coverage deficit.)*

**CERT VALIDITY GATE**: [VALID [n active, m EXCLUDED-LOW] -- proceed to step 1.6.]

---

## ARTIFACT DOMAIN INVENTORY

*(Per §17c -- after CERT VALIDITY GATE = VALID. Uses active reviewer set. No ledger row.)*

**Step 1-2 SCAN + DEDUPLICATE** -- unique [DOMAIN: label] values from §1:
- [label-1], [label-2], [label-3]

**Step 3 SPLIT CHECK**:
- [label-1]: [KEPT -- single distinct concern / SPLIT: [original] -> [A], [B] -- reason]
- [label-2]: [KEPT / SPLIT...]

**Locked domain inventory**:
1. [domain-A]
2. [domain-B]
3. [domain-C]

**INVENTORY LOCK COUNT**: [N]
**INVENTORY LOCK COMPLETE -- matrix row count = N**

---

## DOMAIN-ROLE COVERAGE MATRIX

*(Per §17d -- rows = locked inventory, count must = N. Active roles only. No ledger row.)*

| Artifact Domain | [CHALLENGER_ROLE] | [DOMAIN_ROLE] | [LIFECYCLE_ROLE] | Gap Status |
|-----------------|-------------------|---------------|------------------|-----------|
| [domain-A]      | [H/M/L/--]        | [H/M/L/--]    | [H/M/L/--]       | [DOMAIN-COVERED / DOMAIN-GAP] |
| [domain-B]      | [H/M/L/--]        | [H/M/L/--]    | [H/M/L/--]       | [DOMAIN-COVERED / DOMAIN-GAP] |
| [domain-C]      | [H/M/L/--]        | [H/M/L/--]    | [H/M/L/--]       | [DOMAIN-COVERED / DOMAIN-GAP] |

*(MATRIX CONTRACT CHECK: [N] rows = INVENTORY LOCK COUNT? [YES / VIOLATION])*

**ADVISORY-GAP items pre-registered**:
- [domain if DOMAIN-GAP]: "ADVISORY-GAP: [domain] -- no HIGH-applicability reviewer."
- [or "None -- all COVERED"]

**COVERAGE MATRIX COMPLETE.**

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**CHALLENGER PRE-ASSESSMENT -- DIMENSION TABLE**:

| # | Dimension | Status Quo | Proposed State | Category (F/O/Q) |
|---|-----------|------------|----------------|-----------------|
| 1 | [DIM-1]   | [_]        | [_]            | [F/O/Q]         |
| 2 | [DIM-2]   | [_]        | [_]            | [F/O/Q]         |
| 3 | [DIM-3]   | [_]        | [_]            | [F/O/Q]         |

*(F = FAVORS-BUILD, O = OPEN-TO-DEBATE, Q = STATUS-QUO-WINS)*

**VERDICT COUNT SUMMARY**: F=[_], O+Q=[_], D=F-(O+Q)=[_]
Apply VERDICT THRESHOLD TABLE (§9): D=[_] -> **g_null(initial) = [PASS/CONDITIONAL/FAIL]**

**NULL HYPOTHESIS DERIVATION RULE** *(pre-committed per §9)*:
g_null(initial) = threshold_table[D]. Both B-A and B-C differentials evaluated above.

**Null hypothesis**: [What the team does today -- one sentence.]
**Null hypothesis strength**: [H/M/L]

**Challenge claims**:
| CH-ID  | Claim | Severity |
|--------|-------|----------|
| CH-001 | [_]   | [H/M/L]  |
| CH-002 | [_]   | [H/M/L]  |

**GOpen Verdict**: [PASS/CONDITIONAL/FAIL] *(= g_null(initial))*
**GOpen Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section         | Gate  | Verdict | Class |
|-----------------|-------|---------|-------|
| BRACKET OPENING | GOpen | [_]     | [_]   |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table**:
| CH-ID  | Claim (copy) | Response | Status |
|--------|-------------|----------|--------|
| CH-001 | [copy]      | [_]      | [A/P/O] |
| CH-002 | [copy]      | [_]      | [A/P/O] |

**Additional Findings** *(per §14, §11)*:
| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING] | [H/M/L] |
| F-2 | [§1:S-n] | [FINDING] | [H/M/L] |

**Finding Severity Aggregation**: `worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]`
**Section Severity**: [H/M/L]

**LENS COVERAGE TABLE** *(Applicability from §17d matrix cell for this role)*:
| # | lens.verify Entry | Applicability | Status | Finding Ref |
|---|------------------|--------------|--------|------------|
| 1 | [entry 1]        | [matrix cell] | [A/O] | [F-n]      |
| 2 | [entry 2]        | [matrix cell] | [A/O] | [F-n]      |

**G_domain Verdict**: [PASS/CONDITIONAL/FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section               | Gate     | Verdict | Class |
|-----------------------|----------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [_]     | [_]   |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT *(EXCLUDED from ledger)*

```
G_domain_agg = worst([G_domain verdicts]) = [_]
g_null(post-domain) via §9 Stage 2: [_]
```

---

## §3.8 CH-ID SATURATION CHECK *(EXCLUDED from ledger)*

| CH-ID  | DOMAIN Status | Saturation  |
|--------|--------------|-------------|
| CH-001 | [A/P/O]      | [SAT/UNSAT] |
| CH-002 | [A/P/O]      | [SAT/UNSAT] |

**Unsaturated**: [list or "None"]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy] | G_domain_agg: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table**:
| CH-ID  | Claim (copy) | Response | Status  |
|--------|-------------|----------|---------|
| CH-001 | [copy]      | [_]      | [A/P/O] |
| CH-002 | [copy]      | [_]      | [A/P/O] |

**Additional Findings** *(per §14, §11)*:
| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING] | [H/M/L] |
| F-2 | [§1:S-n] | [FINDING] | [H/M/L] |

**Finding Severity Aggregation**: `worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]`
**Section Severity**: [H/M/L]

**LENS COVERAGE TABLE** *(Applicability from §17d matrix cell for this role)*:
| # | lens.verify Entry | Applicability | Status | Finding Ref |
|---|------------------|--------------|--------|------------|
| 1 | [entry 1]        | [matrix cell] | [A/O] | [F-n]      |
| 2 | [entry 2]        | [matrix cell] | [A/O] | [F-n]      |

**G_lifecycle Verdict**: [PASS/CONDITIONAL/FAIL]
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section                  | Gate        | Verdict | Class |
|--------------------------|-------------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [_]     | [_]   |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: CERT VALIDITY GATE=VALID, all CH-ID tables, all gate verdicts.*

```
g_null(post-domain)=[copy] | G_lifecycle=[copy]
Apply §9 Stage 3 --> g_null(final)=[_]
```

**Full CH-ID Saturation**:
| CH-ID  | DOMAIN  | LIFECYCLE | Full Saturation |
|--------|---------|-----------|----------------|
| CH-001 | [copy]  | [copy]    | [FS/UNSAT]     |
| CH-002 | [copy]  | [copy]    | [FS/UNSAT]     |

**GClose Verdict**: [PASS/CONDITIONAL/FAIL] *(= g_null(final). Override: "g_null OVERRIDE: [reason]")*
**GClose Rationale**: [2-3 sentences referencing domain evidence and lifecycle verdict.]

**Local Gate Ledger Row**:
| Section         | Gate   | Verdict | Class |
|-----------------|--------|---------|-------|
| BRACKET CLOSING | GClose | [_]     | [_]   |

---

## §5.5 SCOPE COVERAGE RECONCILIATION *(EXCLUDED from ledger)*

| Surface  | Reviewer(s) | Finding(s) | Coverage         |
|----------|-------------|-----------|-----------------|
| [§1:S-1] | [ROLE]      | [F-n]     | [COVERED / GAP] |
| [§1:S-2] | [ROLE]      | [F-n]     | [COVERED / GAP] |

**Coverage gate signal**: [COVERED / PARTIAL] | **Advisory items**: [ADVISORY-GAP items or "None"]

---

## GATE VECTOR TABLE

| Gate         | Reviewer       | Verdict | Contract Cite           |
|--------------|----------------|---------|------------------------|
| GOpen        | [CHALLENGER]   | [_]     | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN(S)]    | [_]     | DISPOSITION_CONTRACT v1 |
| G_lifecycle  | [LIFECYCLE]    | [_]     | DISPOSITION_CONTRACT v1 |
| GClose       | [CHALLENGER]   | [_]     | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [named tension between roles, or "None"]
**Convergence**: [named agreement across >= 2 roles]

**§13 Progression Ledger**:
```
g_null(initial)=[_] | g_null(post-domain)=[_] | g_null(final)=[_] | Trajectory: [STABLE/IMPROVING/DEGRADING]
```

---

## DISPOSITION

**Gate vector**: GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]
**Apply §3**: GClose=FAIL?->BLOCKED | Any FAIL?->BLOCKED | Any COND?->CONDITIONAL | All PASS?->READY
**Overall Disposition**: [BLOCKED / CONDITIONAL / READY]
**Primary Driver** *(per §16)*: [derived from gate vector using §16 rule set]
**RESOLUTION REGISTRY** *(per §12)*: [table if CONDITIONAL; else "N/A"]

---

## ACTION ITEM REGISTER

*(Copy local ledger rows verbatim per §6. No re-derivation.)*

| Section                  | Gate        | Verdict | Class  |
|--------------------------|-------------|---------|--------|
| BRACKET OPENING          | GOpen       | [copy]  | [copy] |
| DOMAIN -- [ROLE]         | G_domain    | [copy]  | [copy] |
| LIFECYCLE -- [ROLE]      | G_lifecycle | [copy]  | [copy] |
| BRACKET CLOSING          | GClose      | [copy]  | [copy] |

**Advisory items**: [ADVISORY-GAP, ADVISORY-ORPHAN, ADVISORY-OPEN-LENS,
                    EXCLUDED-LOW coverage deficit, or "None"]

---

**Artifact to review:**

{{artifact}}

---
---

## V-02

**Axis**: Output format -- MECHANICAL SPLIT TRIGGER LIST in §17c ARTIFACT DOMAIN INVENTORY
**Hypothesis**: V-05 R18's §17c SPLIT CHECK asks "does this label cover more than one
distinct concern?" -- a qualitative judgment the model may answer NO when the answer is
YES because the concern boundary is not mechanically defined. Four named triggers that
each REQUIRE a split when they fire replace editorial judgment with auditable notation.
Each label emits either "SPLIT-REQUIRED: [original] -> [A], [B] -- Trigger [n]: [rule]"
or "SPLIT-NOT-TRIGGERED: [label] -- T1 N, T2 N, T3 N, T4 N" for all four checks. A
scorer can verify the split decision from the notation without reading domain knowledge.
Predicted score: 225/225.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this block first. Fill injected values.

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
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2--§17d;
reviewer sections may not execute until §1 COMPLETE, CERT VALIDITY
GATE = VALID, INVENTORY LOCK COMPLETE, and COVERAGE MATRIX COMPLETE
are all reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]
  (Add rows. Use specific domain labels -- one distinct concern per label.
  Labels that fire a SPLIT TRIGGER in §17c will be split there.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]

§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions commitment. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose = FAIL OR exists Gi = FAIL
  CONDITIONAL <-- no FAIL AND exists CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts). FAIL > CONDITIONAL > PASS.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim receives CH-ID. Every downstream section carries CH-ID response
  table. PASS prohibited if any CH-ID row = OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section.
  Assembly: ACTION ITEM REGISTER copies verbatim. No re-derivation.
  EXCLUDED: §3.5, §3.8, §5.5, APPLICABILITY CERTIFICATION BLOCK,
            CERT VALIDITY CHECK TABLE, ARTIFACT DOMAIN INVENTORY,
            DOMAIN-ROLE COVERAGE MATRIX.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.   ROLE MANIFEST
  1.4. APPLICABILITY CERTIFICATION BLOCK  [per §17a; no ledger row]
  1.5. CERT VALIDITY CHECK TABLE          [per §17b; exit gate; no ledger row]
  1.6. ARTIFACT DOMAIN INVENTORY          [per §17c; SPLIT TRIGGER audit; no ledger row]
  1.7. DOMAIN-ROLE COVERAGE MATRIX        [per §17d; no ledger row]
  2.   BRACKET OPENING
  3.   DOMAIN(s)
  3.5. DOMAIN-AGGREGATE CHECKPOINT
  3.8. CH-ID SATURATION CHECK
  4.   LIFECYCLE
  5.   BRACKET CLOSING
  5.5. SCOPE COVERAGE RECONCILIATION
  6.   GATE VECTOR TABLE
  7.   CROSS-ROLE SIGNALS
  8.   DISPOSITION
  9.   ACTION ITEM REGISTER
  Reordering violates this contract.
  CERT VALIDITY GATE = VALID before step 1.6.
  INVENTORY LOCK COMPLETE before COVERAGE MATRIX.
  COVERAGE MATRIX before BRACKET OPENING.
  LIFECYCLE before BRACKET CLOSING.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID in >= 1 DOMAIN section (before LIFECYCLE).
  FULLY SATURATED: CH-ID in DOMAIN + LIFECYCLE (before BRACKET CLOSING).
  PASS prohibited without full saturation or stated waiver.
  Waiver: "CH-XXX WAIVER: [reason]"

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  VERDICT THRESHOLD TABLE [IMMUTABLE]:
    D >= 2  --> g_null(initial) = PASS
    D = 1   --> g_null(initial) = CONDITIONAL
    D = 0   --> g_null(initial) = CONDITIONAL
    D <= -1 --> g_null(initial) = FAIL
  Stage 1: D = count(Category=F) - count(Category=O or Q) from DIMENSION TABLE.
           g_null(initial) = threshold_table[D].
  Stage 2: g_null(post-domain):
    FAIL if G_domain_agg=FAIL;
    max(g_null(initial),CONDITIONAL) if G_domain_agg=CONDITIONAL;
    g_null(initial) if G_domain_agg=PASS.
  Stage 3: g_null(final):
    FAIL if G_lifecycle=FAIL;
    max(g_null(post-domain),CONDITIONAL) if G_lifecycle=CONDITIONAL;
    g_null(post-domain) if G_lifecycle=PASS.
  GClose must equal g_null(final) or declare override.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps each §1 IN-SCOPE surface to reviewer findings. GAP -> ADVISORY-GAP.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding cites "[§1:S-n]". No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION = CONDITIONAL -> emit RESOLUTION REGISTRY table.

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  In CROSS-ROLE SIGNALS: g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Each finding row carries individual Severity. Section Severity = worst(all in section).

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE section emits LENS COVERAGE TABLE. Applicability from §17d
  matrix cell. OPEN + HIGH-applicability -> ADVISORY-OPEN-LENS.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  GClose=FAIL -> GClose. G_domain=FAIL -> DOMAIN. G_lifecycle=FAIL -> LIFECYCLE.
  Any CONDITIONAL -> lowest-index gate. All PASS -> N/A.

§17 -- ROLE MANIFEST APPLICABILITY PROTOCOL [IMMUTABLE]
  ROLE MANIFEST includes Applicability column (HIGH/MEDIUM/LOW per role).

§17a -- APPLICABILITY CERTIFICATION REQUIREMENT [IMMUTABLE]
  After ROLE MANIFEST, emit APPLICABILITY CERTIFICATION BLOCK. One entry per role.
  Format: Role [name]: Applicability | Artifact domain | Lens.verify match | Basis
  Invalid: generic type-reference in Basis. Invalid: no specific lens.verify cited.

§17b -- CERT VALIDITY CHECK REQUIREMENT [IMMUTABLE]
  After APPLICABILITY CERTIFICATION BLOCK, emit CERT VALIDITY CHECK TABLE.
    | Role | Domain Named (Y/N) | Lens Entry Quoted (Y/N) | Basis Artifact-Specific (Y/N) | Valid |
  Valid = ALL-YES if all three Y. DOWNGRADE if any N.
  For any DOWNGRADE: revise APPLICABILITY CERTIFICATION BLOCK, lower Applicability to LOW,
  re-emit table. Repeat until all = ALL-YES.
  Emit CERT VALIDITY GATE:
    "CERT VALIDITY GATE: VALID -- all ALL-YES. Proceed to step 1.6."
  BRACKET OPENING blocked until gate = VALID.

§17c -- ARTIFACT DOMAIN INVENTORY PROTOCOL [IMMUTABLE]
  After CERT VALIDITY GATE = VALID, emit ARTIFACT DOMAIN INVENTORY.
  Step 1 SCAN: extract all unique [DOMAIN: label] values from §1.
  Step 2 DEDUPLICATE: one entry per unique label.
  Step 3 SPLIT TRIGGER AUDIT [IMMUTABLE]:
    For each label, audit all four triggers. If ANY fires: SPLIT REQUIRED.
    Trigger T1 (Conjunction): label contains "and", "or", "/", or "," separating concerns.
    Trigger T2 (Behavioral-Structural): label simultaneously describes system behavior
      (what it does) AND structural implementation (how it is built).
    Trigger T3 (Component-Quality): label combines a component name with a quality
      attribute (e.g., "auth security", "payment reliability", "config performance").
    Trigger T4 (Multi-ownership): two distinct team domains would independently own
      separate parts of this label.
    Required notation per label:
      SPLIT-REQUIRED: "[original]" -> "[A]", "[B]" -- Trigger T[n]: [rule text].
        Update §1 annotations. Use split labels in subsequent steps.
      SPLIT-NOT-TRIGGERED: "[label]" -- T1 N, T2 N, T3 N, T4 N.
    No label may be KEPT without an explicit T1 N/T2 N/T3 N/T4 N declaration.
  Step 4 LOCK: emit numbered list from post-split labels. State INVENTORY LOCK COUNT: N.
  Emit "INVENTORY LOCK COMPLETE -- matrix row count = N".

§17d -- DOMAIN-ROLE COVERAGE MATRIX CONTRACT [IMMUTABLE]
  After INVENTORY LOCK COMPLETE, produce DOMAIN-ROLE COVERAGE MATRIX.
  Rows: each locked domain from §17c. Columns: each selected role.
  Cells: HIGH/MEDIUM/LOW/--.
  Row count must equal INVENTORY LOCK COUNT. Mismatch -> contract violation; halt.
  Domain gap: no HIGH cell -> DOMAIN-GAP ->
    Emit: "ADVISORY-GAP: [domain] -- no HIGH-applicability reviewer."
  §15 Applicability: use matrix cell for (this role, primary artifact domain).

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

| Slot | Archetype | Role | Selection Rationale | Applicability |
|------|-----------|------|---------------------|---------------|
| CHALLENGER (bracket open + close) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] | HIGH |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] | [H/M/L] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] | [H/M/L] |

---

## APPLICABILITY CERTIFICATION BLOCK

*(Per §17a)*

Role [challenger]: Applicability = HIGH
Artifact domain: [§1 domain label]
Lens.verify match: [specific entry]
Basis: [one sentence -- THIS artifact, not its type]

Role [domain]: Applicability = [H/M/L]
Artifact domain: [§1 domain label]
Lens.verify match: [specific entry]
Basis: [one sentence -- specific surface of THIS artifact]

Role [lifecycle]: Applicability = [H/M/L]
Artifact domain: [§1 domain label]
Lens.verify match: [specific entry]
Basis: [one sentence -- specific surface of THIS artifact]

---

## CERT VALIDITY CHECK TABLE

*(Per §17b)*

| Role | Domain Named (Y/N) | Lens Entry Quoted (Y/N) | Basis Artifact-Specific (Y/N) | Valid |
|------|--------------------|------------------------|-------------------------------|-------|
| [challenger] | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |
| [domain]     | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |
| [lifecycle]  | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |

**CERT VALIDITY GATE**: [VALID -- all ALL-YES. Proceed to step 1.6.]

---

## ARTIFACT DOMAIN INVENTORY

*(Per §17c -- SPLIT TRIGGER AUDIT required for every label. No ledger row.)*

**Step 1-2 SCAN + DEDUPLICATE**:
- [label-1], [label-2], [label-3]

**Step 3 SPLIT TRIGGER AUDIT** *(all 4 triggers checked per label)*:
- [label-1]: [SPLIT-REQUIRED: "[original]" -> "[A]", "[B]" -- Trigger T[n]: [rule] / SPLIT-NOT-TRIGGERED: T1 N, T2 N, T3 N, T4 N]
- [label-2]: [...]
- [label-3]: [...]

**Locked domain inventory** *(post-split)*:
1. [domain-A]
2. [domain-B]
3. [domain-C]

**INVENTORY LOCK COUNT**: [N]
**INVENTORY LOCK COMPLETE -- matrix row count = N**

---

## DOMAIN-ROLE COVERAGE MATRIX

*(Per §17d)*

| Artifact Domain | [CHALLENGER_ROLE] | [DOMAIN_ROLE] | [LIFECYCLE_ROLE] | Gap Status |
|-----------------|-------------------|---------------|------------------|-----------|
| [domain-A]      | [H/M/L/--]        | [H/M/L/--]    | [H/M/L/--]       | [COVERED / DOMAIN-GAP] |
| [domain-B]      | [H/M/L/--]        | [H/M/L/--]    | [H/M/L/--]       | [COVERED / DOMAIN-GAP] |
| [domain-C]      | [H/M/L/--]        | [H/M/L/--]    | [H/M/L/--]       | [COVERED / DOMAIN-GAP] |

*(MATRIX CONTRACT CHECK: [N] rows = INVENTORY LOCK COUNT? [YES / VIOLATION])*

**ADVISORY-GAP items**: [list or "None -- all COVERED"]

**COVERAGE MATRIX COMPLETE.**

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**CHALLENGER PRE-ASSESSMENT -- DIMENSION TABLE**:

| # | Dimension | Status Quo | Proposed State | Category (F/O/Q) |
|---|-----------|------------|----------------|-----------------|
| 1 | [DIM-1]   | [_]        | [_]            | [F/O/Q]         |
| 2 | [DIM-2]   | [_]        | [_]            | [F/O/Q]         |
| 3 | [DIM-3]   | [_]        | [_]            | [F/O/Q]         |

**VERDICT COUNT SUMMARY**: F=[_], O+Q=[_], D=[_]
Apply VERDICT THRESHOLD TABLE (§9): D=[_] -> **g_null(initial) = [_]**

**NULL HYPOTHESIS DERIVATION RULE**: g_null(initial) = threshold_table[D].

**Null hypothesis**: [What team does today -- one sentence.]
**Null hypothesis strength**: [H/M/L]

**Challenge claims**:
| CH-ID  | Claim | Severity |
|--------|-------|----------|
| CH-001 | [_]   | [H/M/L]  |
| CH-002 | [_]   | [H/M/L]  |

**GOpen Verdict**: [_] *(= g_null(initial))* | **GOpen Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section         | Gate  | Verdict | Class |
|-----------------|-------|---------|-------|
| BRACKET OPENING | GOpen | [_]     | [_]   |

---

*(DOMAIN, §3.5, §3.8, LIFECYCLE, BRACKET CLOSING, §5.5, GATE VECTOR TABLE,
CROSS-ROLE SIGNALS, DISPOSITION, ACTION ITEM REGISTER sections identical to V-01
above. Replicate in full.)*

---

**Artifact to review:**

{{artifact}}

---
---

## V-03

**Axis**: Inertia framing -- DIMENSION PRE-LOCK PROTOCOL (table-before-prose enforcement)
**Hypothesis**: V-05 R18's BRACKET OPENING requires a DIMENSION TABLE with F/O/Q
Category cells, but the instruction sequence allows the model to write the table while
composing the null hypothesis prose argument -- meaning prose reasoning may influence
Category assignments retrospectively. The VERDICT COUNT SUMMARY counts cells after the
fact. V-03 adds a PRE-LOCK gate inside the BRACKET OPENING template: (1) DIMENSION
TABLE must be emitted with all Category cells filled before any prose begins; (2) a
DIMENSION TABLE LOCKED statement is emitted with F/O/Q counts; (3) the NH TESTIMONY
section is structurally marked "derived from DIMENSION TABLE above -- no new dimension
evidence admitted"; (4) any dimension assessment in prose that is not traceable to a
table row is flagged UNDECLARED-DIMENSION. This makes g_null(initial) derivable from
the table alone: scorer reads Category column, counts F vs O+Q, applies threshold table.
Predicted score: 225/225.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this block first. Fill injected values.

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
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2--§17d;
reviewer sections may not execute until §1 COMPLETE, CERT VALIDITY
GATE = VALID, INVENTORY LOCK COMPLETE, and COVERAGE MATRIX COMPLETE
are all reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]
  (Add rows.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]

§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions commitment. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose = FAIL OR exists Gi = FAIL
  CONDITIONAL <-- no FAIL AND exists CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts). FAIL > CONDITIONAL > PASS.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim receives CH-ID. Every downstream section carries CH-ID response
  table. PASS prohibited if any CH-ID row = OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section.
  Assembly: ACTION ITEM REGISTER copies verbatim. No re-derivation.
  EXCLUDED: §3.5, §3.8, §5.5, APPLICABILITY CERTIFICATION BLOCK,
            CERT VALIDITY CHECK TABLE, ARTIFACT DOMAIN INVENTORY,
            DOMAIN-ROLE COVERAGE MATRIX.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.   ROLE MANIFEST
  1.4. APPLICABILITY CERTIFICATION BLOCK  [per §17a; no ledger row]
  1.5. CERT VALIDITY CHECK TABLE          [per §17b; exit gate; no ledger row]
  1.6. ARTIFACT DOMAIN INVENTORY          [per §17c; no ledger row]
  1.7. DOMAIN-ROLE COVERAGE MATRIX        [per §17d; no ledger row]
  2.   BRACKET OPENING
       2.0. DIMENSION TABLE                [DIMENSION PRE-LOCK; no ledger row]
       2.1. DIMENSION TABLE LOCKED        [gate; before NH TESTIMONY]
       2.2. NH TESTIMONY                  [derived from locked table]
       2.3. Challenge claims + GOpen
  3.   DOMAIN(s)
  3.5. DOMAIN-AGGREGATE CHECKPOINT
  3.8. CH-ID SATURATION CHECK
  4.   LIFECYCLE
  5.   BRACKET CLOSING
  5.5. SCOPE COVERAGE RECONCILIATION
  6.   GATE VECTOR TABLE
  7.   CROSS-ROLE SIGNALS
  8.   DISPOSITION
  9.   ACTION ITEM REGISTER
  Reordering violates this contract.
  DIMENSION TABLE LOCKED must precede NH TESTIMONY.
  LIFECYCLE must precede BRACKET CLOSING.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID in >= 1 DOMAIN (before LIFECYCLE).
  FULLY SATURATED: CH-ID in DOMAIN + LIFECYCLE (before BRACKET CLOSING).
  PASS prohibited without full saturation or stated waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  VERDICT THRESHOLD TABLE [IMMUTABLE]:
    D >= 2  --> g_null(initial) = PASS
    D = 1   --> g_null(initial) = CONDITIONAL
    D = 0   --> g_null(initial) = CONDITIONAL
    D <= -1 --> g_null(initial) = FAIL
  DIMENSION PRE-LOCK PROTOCOL [IMMUTABLE]:
    DIMENSION TABLE must be fully populated (all Category cells = F, O, or Q) and
    DIMENSION TABLE LOCKED statement emitted BEFORE any NH TESTIMONY prose begins.
    Category cells accept exactly {F, O, Q}. No blank cells. No mixed values.
    DIMENSION TABLE LOCKED: emit "DIMENSION TABLE LOCKED: [n] rows. F=[a], O+Q=[b], D=[a-b]."
    NH TESTIMONY is labeled: "NH TESTIMONY (derived from DIMENSION TABLE above --
    no new dimension evidence admitted):"
    Any dimension claim in NH TESTIMONY not traceable to a DIMENSION TABLE row =>
    emit: "UNDECLARED-DIMENSION: [claim] -- not in DIMENSION TABLE. Advisory note only."
  Stage 1: D = count(F) - count(O or Q). g_null(initial) = threshold_table[D].
  Stage 2: g_null(post-domain):
    FAIL if G_domain_agg=FAIL;
    max(g_null(initial),CONDITIONAL) if G_domain_agg=CONDITIONAL;
    g_null(initial) if G_domain_agg=PASS.
  Stage 3: g_null(final):
    FAIL if G_lifecycle=FAIL;
    max(g_null(post-domain),CONDITIONAL) if G_lifecycle=CONDITIONAL;
    g_null(post-domain) if G_lifecycle=PASS.
  GClose must equal g_null(final) or declare override.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps each §1 surface to findings. GAP -> ADVISORY-GAP.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding cites "[§1:S-n]". No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION = CONDITIONAL -> emit RESOLUTION REGISTRY table.

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  In CROSS-ROLE SIGNALS: g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Each finding row carries individual Severity. Section Severity = worst(all in section).

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE section emits LENS COVERAGE TABLE. Applicability from §17d.
  OPEN + HIGH-applicability -> ADVISORY-OPEN-LENS.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  GClose=FAIL -> GClose. G_domain=FAIL -> DOMAIN. G_lifecycle=FAIL -> LIFECYCLE.
  Any CONDITIONAL -> lowest-index. All PASS -> N/A.

§17 -- ROLE MANIFEST APPLICABILITY PROTOCOL [IMMUTABLE]
  ROLE MANIFEST includes Applicability column (HIGH/MEDIUM/LOW per role).

§17a -- APPLICABILITY CERTIFICATION REQUIREMENT [IMMUTABLE]
  After ROLE MANIFEST, emit APPLICABILITY CERTIFICATION BLOCK. One entry per role.
  Format: Role [name]: Applicability | Artifact domain | Lens.verify match | Basis
  Invalid: generic type-reference. Invalid: no specific lens.verify cited.

§17b -- CERT VALIDITY CHECK REQUIREMENT [IMMUTABLE]
  After APPLICABILITY CERTIFICATION BLOCK, emit CERT VALIDITY CHECK TABLE.
    | Role | Domain Named (Y/N) | Lens Entry Quoted (Y/N) | Basis Artifact-Specific (Y/N) | Valid |
  Valid = ALL-YES if all three Y. DOWNGRADE if any N.
  For any DOWNGRADE: revise and re-emit until all = ALL-YES.
  Emit CERT VALIDITY GATE: "CERT VALIDITY GATE: VALID -- all ALL-YES."
  BRACKET OPENING blocked until gate = VALID.

§17c -- ARTIFACT DOMAIN INVENTORY PROTOCOL [IMMUTABLE]
  After CERT VALIDITY GATE = VALID, emit ARTIFACT DOMAIN INVENTORY.
  Step 1 SCAN: extract unique [DOMAIN: label] values from §1.
  Step 2 DEDUPLICATE.
  Step 3 SPLIT CHECK: for each label, ask whether it covers > 1 distinct concern.
    If yes: split. State: "SPLIT: [original] -> [A], [B]"
    State: "KEPT: [label] -- single concern"
  Step 4 LOCK: emit numbered list. State INVENTORY LOCK COUNT: N.
  Emit "INVENTORY LOCK COMPLETE."

§17d -- DOMAIN-ROLE COVERAGE MATRIX CONTRACT [IMMUTABLE]
  After INVENTORY LOCK COMPLETE, produce DOMAIN-ROLE COVERAGE MATRIX.
  Rows: locked domain inventory. Columns: selected roles. Cells: HIGH/MEDIUM/LOW/--.
  Row count must equal INVENTORY LOCK COUNT. Mismatch -> halt.
  Domain gap: no HIGH cell -> DOMAIN-GAP ->
    Emit: "ADVISORY-GAP: [domain] -- no HIGH-applicability reviewer."

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

| Slot | Archetype | Role | Selection Rationale | Applicability |
|------|-----------|------|---------------------|---------------|
| CHALLENGER (bracket open + close) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] | HIGH |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] | [H/M/L] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] | [H/M/L] |

---

## APPLICABILITY CERTIFICATION BLOCK

*(Per §17a)*

Role [challenger]: Applicability = HIGH
Artifact domain: [§1 label] | Lens.verify match: [entry] | Basis: [THIS artifact specifically]

Role [domain]: Applicability = [H/M/L]
Artifact domain: [§1 label] | Lens.verify match: [entry] | Basis: [specific surface]

Role [lifecycle]: Applicability = [H/M/L]
Artifact domain: [§1 label] | Lens.verify match: [entry] | Basis: [specific surface]

---

## CERT VALIDITY CHECK TABLE

*(Per §17b)*

| Role | Domain Named | Lens Quoted | Basis Artifact-Specific | Valid |
|------|-------------|------------|------------------------|-------|
| [challenger] | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |
| [domain]     | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |
| [lifecycle]  | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |

**CERT VALIDITY GATE**: [VALID -- all ALL-YES. Proceed.]

---

## ARTIFACT DOMAIN INVENTORY

*(Per §17c)*

**Scan + Deduplicate**: [label-1], [label-2], [label-3]

**Split Check**:
- [label-1]: [KEPT -- single concern / SPLIT -> [A], [B]]
- [label-2]: [...]

**Locked list**: 1. [A] / 2. [B] / 3. [C]
**INVENTORY LOCK COUNT**: [N] | **INVENTORY LOCK COMPLETE**

---

## DOMAIN-ROLE COVERAGE MATRIX

*(Per §17d)*

| Artifact Domain | [CHALLENGER] | [DOMAIN] | [LIFECYCLE] | Gap Status |
|-----------------|-------------|---------|------------|-----------|
| [domain-A]      | [H/M/L/--]  | [H/M/L/--] | [H/M/L/--] | [COVERED / DOMAIN-GAP] |
| [domain-B]      | [H/M/L/--]  | [H/M/L/--] | [H/M/L/--] | [COVERED / DOMAIN-GAP] |

**ADVISORY-GAP items**: [list or "None"] | **COVERAGE MATRIX COMPLETE.**

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

### 2.0 DIMENSION TABLE *(complete all rows before proceeding to 2.1)*

| # | Dimension | Status Quo | Proposed State | Category (F/O/Q) |
|---|-----------|------------|----------------|-----------------|
| 1 | [DIM-1]   | [_]        | [_]            | [F/O/Q]         |
| 2 | [DIM-2]   | [_]        | [_]            | [F/O/Q]         |
| 3 | [DIM-3]   | [_]        | [_]            | [F/O/Q]         |

*(F = FAVORS-BUILD, O = OPEN-TO-DEBATE, Q = STATUS-QUO-WINS. No blanks. No prose in Category cell.)*

### 2.1 DIMENSION TABLE LOCKED

**DIMENSION TABLE LOCKED**: [n] rows. F=[a], O+Q=[b], D=a-b=[_]
Apply VERDICT THRESHOLD TABLE (§9): D=[_] -> **g_null(initial) = [PASS/CONDITIONAL/FAIL]**

### 2.2 NH TESTIMONY *(derived from DIMENSION TABLE above -- no new dimension evidence admitted)*

[Prose interpreting the locked table. Each claim traces to a dimension row number.
Example: "Dimension 1 (FAVORS-BUILD) indicates [x]. Dimension 2 (OPEN-TO-DEBATE)
indicates [y]. Dimension 3 (FAVORS-BUILD) indicates [z]."]

*(Any dimension claim not traceable to a DIMENSION TABLE row: emit
"UNDECLARED-DIMENSION: [claim]" as advisory.)*

**Null hypothesis**: [What team does today -- one sentence.]
**Null hypothesis strength**: [H/M/L]
**NULL HYPOTHESIS DERIVATION RULE**: g_null(initial) = threshold_table[D] per §9.

### 2.3 Challenge claims + GOpen

**Challenge claims**:
| CH-ID  | Claim | Severity |
|--------|-------|----------|
| CH-001 | [_]   | [H/M/L]  |
| CH-002 | [_]   | [H/M/L]  |

**GOpen Verdict**: [PASS/CONDITIONAL/FAIL] *(= g_null(initial))*
**GOpen Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section         | Gate  | Verdict | Class |
|-----------------|-------|---------|-------|
| BRACKET OPENING | GOpen | [_]     | [_]   |

---

*(DOMAIN, §3.5, §3.8, LIFECYCLE, BRACKET CLOSING, §5.5, GATE VECTOR TABLE,
CROSS-ROLE SIGNALS, DISPOSITION, ACTION ITEM REGISTER sections identical to V-01
above. Replicate in full.)*

---

**Artifact to review:**

{{artifact}}

---
---

## V-04

**Axis**: Lifecycle emphasis + Output format -- REVISION TERMINATION BOUND + MECHANICAL SPLIT TRIGGER LIST
**Hypothesis**: V-01 and V-02 address independent failure modes (C-33 revision loop vs.
C-34 SPLIT CHECK coverage). Combining them does not create an interaction: §17b REVISION
BOUND terminates after max 1 revision cycle (modifying §17b), while §17c SPLIT TRIGGER
LIST adds mandatory per-label trigger notation (modifying §17c). The contracts operate in
separate phases (CERT VALIDITY CHECK at step 1.5, ARTIFACT DOMAIN INVENTORY at step 1.6).
V-04 passes both improvements forward without the §9 DIMENSION PRE-LOCK change. Predicted
score: 225/225.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- §1 COMPLETE, CERT VALIDITY GATE = VALID,
INVENTORY LOCK COMPLETE, COVERAGE MATRIX COMPLETE all required
before reviewer sections execute]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE:
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]
OUT-OF-SCOPE:
  1. [SURFACE -- REASON]
§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks. MEDIUM = Conditions. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND exists CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain). FAIL > CONDITIONAL > PASS.

§4 -- CONTRACT CITE [IMMUTABLE]
  Each reviewer: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING [IMMUTABLE]
  Each claim gets CH-ID. Downstream sections carry CH-ID response table.
  PASS prohibited if any CH-ID = OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emit at end of verdict-emitting sections.
  ACTION ITEM REGISTER copies verbatim. No re-derivation.
  EXCLUDED: §3.5, §3.8, §5.5, CERT BLOCK, CERT TABLE, INVENTORY, MATRIX.

§7 -- SECTION ORDER [IMMUTABLE]
  1. ROLE MANIFEST
  1.4. APPLICABILITY CERT BLOCK   [§17a]
  1.5. CERT VALIDITY CHECK TABLE  [§17b; exit gate]
  1.6. ARTIFACT DOMAIN INVENTORY  [§17c; SPLIT TRIGGER AUDIT]
  1.7. DOMAIN-ROLE COVERAGE MATRIX [§17d]
  2. BRACKET OPENING
  3. DOMAIN(s) | 3.5 AGGREGATE | 3.8 SATURATION CHECK
  4. LIFECYCLE
  5. BRACKET CLOSING
  5.5. SCOPE COVERAGE RECONCILIATION
  6. GATE VECTOR | 7. CROSS-ROLE | 8. DISPOSITION | 9. ACTION REGISTER
  CERT VALIDITY GATE = VALID before 1.6.
  INVENTORY LOCK COMPLETE before 1.7.
  COVERAGE MATRIX before 2. LIFECYCLE before 5.
  EXCLUDED-LOW roles removed before 1.6.

§8 -- CH-ID SATURATION [IMMUTABLE]
  SATURATED: CH-ID in >= 1 DOMAIN. FULLY SATURATED: DOMAIN + LIFECYCLE.
  PASS prohibited without full saturation or waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  VERDICT THRESHOLD TABLE [IMMUTABLE]:
    D >= 2 -> PASS | D = 1 -> CONDITIONAL | D = 0 -> CONDITIONAL | D <= -1 -> FAIL
  Stage 1: D = count(F) - count(O+Q). g_null(initial) = threshold_table[D].
  Stage 2: g_null(post-domain):
    FAIL if G_domain_agg=FAIL; max(g_null(initial),COND) if COND; g_null(initial) if PASS.
  Stage 3: g_null(final):
    FAIL if G_lifecycle=FAIL; max(g_null(post-domain),COND) if COND; g_null(post-domain) if PASS.
  GClose = g_null(final) or override.

§10-§16 [IMMUTABLE -- same as V-01 §10-§16]
  §10: §5.5 coverage reconciliation. §11: §1:S-n citation. §12: RESOLUTION REGISTRY.
  §13: g_null progression ledger. §14: per-finding severity aggregation.
  §15: LENS COVERAGE TABLE; OPEN+HIGH -> ADVISORY-OPEN-LENS.
  §16: PRIMARY DRIVER: GClose=FAIL->GClose; G_domain=FAIL->DOMAIN;
       G_lifecycle=FAIL->LIFECYCLE; CONDITIONAL->lowest-index; all PASS->N/A.

§17 -- ROLE MANIFEST APPLICABILITY PROTOCOL [IMMUTABLE]
  ROLE MANIFEST includes Applicability (HIGH/MEDIUM/LOW) per role.

§17a -- APPLICABILITY CERTIFICATION REQUIREMENT [IMMUTABLE]
  After ROLE MANIFEST: APPLICABILITY CERTIFICATION BLOCK.
  One entry per role: Applicability | Artifact domain | Lens.verify match | Basis
  Invalid: generic type-reference or missing lens.verify entry.

§17b -- CERT VALIDITY CHECK REQUIREMENT [IMMUTABLE]
  Table: | Role | Domain Named | Lens Quoted | Basis Artifact-Specific | Valid |
  Valid = ALL-YES. DOWNGRADE if any N.
  REVISION BOUND [IMMUTABLE]:
    Max 1 revision cycle per role.
    If DOWNGRADE after revision: emit "REVISION LIMIT REACHED: [role] -- EXCLUDED-LOW."
    Register: "ADVISORY: [role] EXCLUDED-LOW -- coverage deficit in [domain]."
  CERT VALIDITY GATE: "VALID [n active, m EXCLUDED-LOW]."

§17c -- ARTIFACT DOMAIN INVENTORY PROTOCOL [IMMUTABLE]
  Step 1 SCAN: unique [DOMAIN: label] from §1.
  Step 2 DEDUPLICATE.
  Step 3 SPLIT TRIGGER AUDIT [IMMUTABLE]:
    Four triggers (checked for every label; REQUIRED split if any fires):
    T1 Conjunction: label contains "and", "or", "/", "," separating concerns.
    T2 Behavioral-Structural: spans what-system-does AND how-system-built.
    T3 Component-Quality: combines component name + quality attribute.
    T4 Multi-ownership: two team domains would own separate parts independently.
    Required notation:
      SPLIT-REQUIRED: "[original]" -> "[A]", "[B]" -- Trigger T[n]: [rule text fired].
      SPLIT-NOT-TRIGGERED: "[label]" -- T1 N, T2 N, T3 N, T4 N.
    No label may proceed without trigger audit notation.
  Step 4 LOCK: numbered list. INVENTORY LOCK COUNT: N.
  Emit "INVENTORY LOCK COMPLETE."

§17d -- DOMAIN-ROLE COVERAGE MATRIX CONTRACT [IMMUTABLE]
  Rows: locked inventory. Columns: active roles. Cells: HIGH/MEDIUM/LOW/--.
  Row count = INVENTORY LOCK COUNT. Mismatch -> halt.
  DOMAIN-GAP (no HIGH): emit "ADVISORY-GAP: [domain] -- no HIGH-applicability reviewer."

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

| Slot | Archetype | Role | Selection Rationale | Applicability |
|------|-----------|------|---------------------|---------------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] | HIGH |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] | [H/M/L] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] | [H/M/L] |

---

## APPLICABILITY CERTIFICATION BLOCK

*(Per §17a)*

Role [challenger]: Applicability = HIGH | Domain: [§1 label] | Lens: [entry] | Basis: [THIS artifact]
Role [domain]: Applicability = [H/M/L] | Domain: [§1 label] | Lens: [entry] | Basis: [specific surface]
Role [lifecycle]: Applicability = [H/M/L] | Domain: [§1 label] | Lens: [entry] | Basis: [specific surface]

---

## CERT VALIDITY CHECK TABLE

*(Per §17b -- REVISION BOUND active)*

| Role | Domain Named | Lens Quoted | Basis Artifact-Specific | Valid |
|------|-------------|------------|------------------------|-------|
| [challenger] | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |
| [domain]     | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |
| [lifecycle]  | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |

*(DOWNGRADE: revise ONCE. If still DOWNGRADE: emit "REVISION LIMIT REACHED: [role] -- EXCLUDED-LOW.")*

**CERT VALIDITY GATE**: [VALID [n active, m EXCLUDED-LOW]]

---

## ARTIFACT DOMAIN INVENTORY

*(Per §17c -- SPLIT TRIGGER AUDIT required per label)*

**Scan + Deduplicate**: [label-1], [label-2], [label-3]

**Split Trigger Audit**:
- [label-1]: [SPLIT-REQUIRED: "[original]" -> "[A]", "[B]" -- T[n]: [rule] /
              SPLIT-NOT-TRIGGERED: T1 N, T2 N, T3 N, T4 N]
- [label-2]: [...]

**Locked list**: 1. [A] / 2. [B] / 3. [C]
**INVENTORY LOCK COUNT**: [N] | **INVENTORY LOCK COMPLETE**

---

## DOMAIN-ROLE COVERAGE MATRIX

*(Per §17d)*

| Artifact Domain | [CHALLENGER] | [DOMAIN] | [LIFECYCLE] | Gap Status |
|-----------------|-------------|---------|------------|-----------|
| [domain-A]      | [H/M/L/--]  | [H/M/L/--] | [H/M/L/--] | [COVERED / DOMAIN-GAP] |
| [domain-B]      | [H/M/L/--]  | [H/M/L/--] | [H/M/L/--] | [COVERED / DOMAIN-GAP] |

**ADVISORY-GAP items**: [list or "None"] | **COVERAGE MATRIX COMPLETE.**

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**DIMENSION TABLE**:
| # | Dimension | Status Quo | Proposed State | Category (F/O/Q) |
|---|-----------|------------|----------------|-----------------|
| 1 | [DIM-1]   | [_]        | [_]            | [F/O/Q]         |
| 2 | [DIM-2]   | [_]        | [_]            | [F/O/Q]         |
| 3 | [DIM-3]   | [_]        | [_]            | [F/O/Q]         |

**VERDICT COUNT SUMMARY**: F=[_], O+Q=[_], D=[_]
Apply threshold (§9): D=[_] -> **g_null(initial) = [_]**

**Null hypothesis**: [One sentence.] | **Null hypothesis strength**: [H/M/L]
**NULL HYPOTHESIS DERIVATION RULE**: g_null(initial) = threshold_table[D].

**Challenge claims**:
| CH-ID  | Claim | Severity |
|--------|-------|----------|
| CH-001 | [_]   | [H/M/L]  |
| CH-002 | [_]   | [H/M/L]  |

**GOpen Verdict**: [_] | **GOpen Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [_] | [_] |

---

*(DOMAIN, §3.5, §3.8, LIFECYCLE, BRACKET CLOSING, §5.5, GATE VECTOR TABLE,
CROSS-ROLE SIGNALS, DISPOSITION, ACTION ITEM REGISTER sections identical to V-01
above. Replicate in full.)*

---

**Artifact to review:**

{{artifact}}

---
---

## V-05

**Axis**: Lifecycle emphasis + Output format + Inertia framing -- all three R19 fixes
**Hypothesis**: V-01 (REVISION TERMINATION BOUND), V-02 (SPLIT TRIGGER AUDIT), and V-03
(DIMENSION PRE-LOCK PROTOCOL) each target an independent residual failure mode from
V-05 R18. The three modifications operate at different phases:
- §17b REVISION BOUND: step 1.5 (CERT VALIDITY CHECK)
- §17c SPLIT TRIGGER AUDIT: step 1.6 (ARTIFACT DOMAIN INVENTORY)
- §9 DIMENSION PRE-LOCK: step 2.0-2.1 (BRACKET OPENING)
No cross-phase dependencies. Combining all three closes each residual gap simultaneously.
Predicted score: 225/225. First variant with all three enforcement levels active together.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- §1 COMPLETE + CERT VALIDITY GATE = VALID +
INVENTORY LOCK COMPLETE + COVERAGE MATRIX COMPLETE all required
before reviewer sections execute]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE:
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]
OUT-OF-SCOPE:
  1. [SURFACE -- REASON]
§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks. MEDIUM = Conditions. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND exists CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain). FAIL > CONDITIONAL > PASS.

§4 -- CONTRACT CITE [IMMUTABLE]
  Each reviewer: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING [IMMUTABLE]
  Each claim gets CH-ID. Downstream sections carry response tables.
  PASS prohibited if any CH-ID = OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emit at end of verdict-emitting sections. ACTION ITEM REGISTER copies verbatim.
  EXCLUDED: §3.5, §3.8, §5.5, CERT BLOCK, CERT TABLE, INVENTORY, MATRIX.

§7 -- SECTION ORDER [IMMUTABLE]
  1.   ROLE MANIFEST
  1.4. APPLICABILITY CERT BLOCK   [§17a; no ledger row]
  1.5. CERT VALIDITY CHECK TABLE  [§17b; exit gate; REVISION BOUND active]
  1.6. ARTIFACT DOMAIN INVENTORY  [§17c; SPLIT TRIGGER AUDIT]
  1.7. DOMAIN-ROLE COVERAGE MATRIX [§17d]
  2.   BRACKET OPENING
       2.0. DIMENSION TABLE       [DIMENSION PRE-LOCK; all F/O/Q before 2.1]
       2.1. DIMENSION TABLE LOCKED [gate; before NH TESTIMONY]
       2.2. NH TESTIMONY          [derived from locked table]
       2.3. Challenge claims + GOpen
  3.   DOMAIN(s) | 3.5 AGGREGATE | 3.8 SATURATION CHECK
  4.   LIFECYCLE
  5.   BRACKET CLOSING
  5.5. SCOPE COVERAGE RECONCILIATION
  6.   GATE VECTOR | 7. CROSS-ROLE | 8. DISPOSITION | 9. ACTION REGISTER
  CERT VALIDITY GATE = VALID before 1.6.
  EXCLUDED-LOW roles removed before 1.6.
  INVENTORY LOCK COMPLETE before 1.7.
  COVERAGE MATRIX before 2.
  DIMENSION TABLE LOCKED before 2.2.
  LIFECYCLE before 5.
  Reordering violates this contract.

§8 -- CH-ID SATURATION [IMMUTABLE]
  SATURATED: CH-ID in >= 1 DOMAIN. FULLY SATURATED: DOMAIN + LIFECYCLE.
  PASS prohibited without full saturation or waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  VERDICT THRESHOLD TABLE [IMMUTABLE]:
    D >= 2 -> PASS | D = 1 -> CONDITIONAL | D = 0 -> CONDITIONAL | D <= -1 -> FAIL
  DIMENSION PRE-LOCK PROTOCOL [IMMUTABLE]:
    All DIMENSION TABLE Category cells (F/O/Q) must be filled and DIMENSION TABLE LOCKED
    statement emitted BEFORE NH TESTIMONY prose begins.
    Cell values: exactly {F, O, Q}. No blanks. No mixed values.
    DIMENSION TABLE LOCKED: "DIMENSION TABLE LOCKED: [n] rows. F=[a], O+Q=[b], D=[a-b]."
    NH TESTIMONY labeled: "NH TESTIMONY (derived from DIMENSION TABLE above -- no new
    dimension evidence admitted):"
    Dimension claim in NH TESTIMONY not traceable to DIMENSION TABLE row ->
    emit: "UNDECLARED-DIMENSION: [claim] -- advisory only."
  Stage 1: D = count(F) - count(O+Q). g_null(initial) = threshold_table[D].
  Stage 2: g_null(post-domain):
    FAIL if G_domain_agg=FAIL; max(g_null(initial),COND) if COND; g_null(initial) if PASS.
  Stage 3: g_null(final):
    FAIL if G_lifecycle=FAIL; max(g_null(post-domain),COND) if COND;
    g_null(post-domain) if PASS.
  GClose = g_null(final) or override with justification.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps §1 surfaces to findings. GAP -> ADVISORY-GAP.

§11 -- FINDING-SURFACE LINKAGE [IMMUTABLE]
  Each finding cites "[§1:S-n]". No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY [IMMUTABLE]
  DISPOSITION = CONDITIONAL -> RESOLUTION REGISTRY table.

§13 -- g_null PROGRESSION LEDGER [IMMUTABLE]
  In CROSS-ROLE SIGNALS: g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory.

§14 -- FINDING SEVERITY AGGREGATION [IMMUTABLE]
  Each finding row carries individual Severity. Section Severity = worst(all).

§15 -- LENS EXHAUSTION [IMMUTABLE]
  Each DOMAIN/LIFECYCLE: LENS COVERAGE TABLE with Applicability from §17d matrix cell.
  OPEN + HIGH-applicability -> ADVISORY-OPEN-LENS.

§16 -- PRIMARY DRIVER DERIVATION [IMMUTABLE]
  GClose=FAIL->GClose. G_domain=FAIL->DOMAIN. G_lifecycle=FAIL->LIFECYCLE.
  Any CONDITIONAL -> lowest-index. All PASS -> N/A.

§17 -- ROLE MANIFEST APPLICABILITY PROTOCOL [IMMUTABLE]
  ROLE MANIFEST includes Applicability (HIGH/MEDIUM/LOW) per role.

§17a -- APPLICABILITY CERTIFICATION REQUIREMENT [IMMUTABLE]
  After ROLE MANIFEST: APPLICABILITY CERTIFICATION BLOCK. One entry per role.
  Format: Role [name]: Applicability | Artifact domain | Lens.verify match | Basis
  Invalid: generic type-reference. Invalid: missing specific lens.verify entry.

§17b -- CERT VALIDITY CHECK REQUIREMENT [IMMUTABLE]
  Table: | Role | Domain Named (Y/N) | Lens Quoted (Y/N) | Basis Artifact-Specific (Y/N) | Valid |
  Valid = ALL-YES. DOWNGRADE if any N.
  REVISION BOUND [IMMUTABLE]:
    Max 1 revision cycle per role.
    If DOWNGRADE after one revision: emit "REVISION LIMIT REACHED: [role] -- EXCLUDED-LOW."
    Remove role from active reviewer set.
    Register: "ADVISORY: [role] EXCLUDED-LOW -- coverage deficit in [domain]."
  CERT VALIDITY GATE: "VALID [n active, m EXCLUDED-LOW] -- all active rows ALL-YES."
  BRACKET OPENING blocked until gate = VALID.

§17c -- ARTIFACT DOMAIN INVENTORY PROTOCOL [IMMUTABLE]
  After CERT VALIDITY GATE = VALID, emit ARTIFACT DOMAIN INVENTORY.
  Step 1 SCAN: unique [DOMAIN: label] from §1.
  Step 2 DEDUPLICATE.
  Step 3 SPLIT TRIGGER AUDIT [IMMUTABLE]:
    Four triggers (all four checked per label; ANY fire -> SPLIT REQUIRED):
    T1 Conjunction: label contains "and", "or", "/", "," separating concerns.
    T2 Behavioral-Structural: label simultaneously describes what-system-does AND
      how-system-built.
    T3 Component-Quality: combines component name + quality attribute.
    T4 Multi-ownership: two distinct team domains would own parts independently.
    Required notation:
      SPLIT-REQUIRED: "[original]" -> "[A]", "[B]" -- Trigger T[n]: [rule text fired].
        Update §1 annotations. Use split labels in remaining steps.
      SPLIT-NOT-TRIGGERED: "[label]" -- T1 N, T2 N, T3 N, T4 N.
    Every label must emit one of these two notations. No label proceeds without audit.
  Step 4 LOCK: numbered list from post-split labels. INVENTORY LOCK COUNT: N.
  Emit "INVENTORY LOCK COMPLETE -- matrix row count = N."

§17d -- DOMAIN-ROLE COVERAGE MATRIX CONTRACT [IMMUTABLE]
  After INVENTORY LOCK COMPLETE, produce DOMAIN-ROLE COVERAGE MATRIX.
  Rows: locked domain inventory. Columns: active roles (EXCLUDED-LOW absent).
  Cells: HIGH/MEDIUM/LOW/--.
  Row count must equal INVENTORY LOCK COUNT. Mismatch -> contract violation; halt:
  "MATRIX CONTRACT VIOLATION: expected N rows, built M. Revise §1 annotations."
  Domain gap: no HIGH cell in row -> DOMAIN-GAP ->
    Emit: "ADVISORY-GAP: [domain] -- no HIGH-applicability reviewer."
  §15 Applicability: use matrix cell (this role, primary artifact domain).

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

| Slot | Archetype | Role | Selection Rationale | Applicability |
|------|-----------|------|---------------------|---------------|
| CHALLENGER (bracket open + close) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] | HIGH |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] | [H/M/L] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] | [H/M/L] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3 rows.)*

---

## APPLICABILITY CERTIFICATION BLOCK

*(Per §17a)*

Role [challenger]: Applicability = HIGH
Artifact domain: [§1 domain label] | Lens.verify match: [specific entry] | Basis: [THIS artifact specifically]

Role [domain]: Applicability = [H/M/L]
Artifact domain: [§1 domain label] | Lens.verify match: [specific entry] | Basis: [specific surface of THIS artifact]

Role [lifecycle]: Applicability = [H/M/L]
Artifact domain: [§1 domain label] | Lens.verify match: [specific entry] | Basis: [specific surface of THIS artifact]

---

## CERT VALIDITY CHECK TABLE

*(Per §17b -- REVISION BOUND: max 1 revision per role. No ledger row.)*

| Role | Domain Named (Y/N) | Lens Entry Quoted (Y/N) | Basis Artifact-Specific (Y/N) | Valid |
|------|--------------------|------------------------|-------------------------------|-------|
| [challenger] | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |
| [domain]     | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |
| [lifecycle]  | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |

*(DOWNGRADE: revise APPLICABILITY CERTIFICATION BLOCK and lower Applicability to LOW.
Re-emit table ONCE. If still DOWNGRADE: "REVISION LIMIT REACHED: [role] -- EXCLUDED-LOW."
Register advisory coverage deficit. Remove from active set.)*

**CERT VALIDITY GATE**: [VALID [n active, m EXCLUDED-LOW] -- all active rows ALL-YES. Proceed to 1.6.]

---

## ARTIFACT DOMAIN INVENTORY

*(Per §17c -- SPLIT TRIGGER AUDIT: all 4 triggers checked per label. No ledger row.)*

**Step 1-2 SCAN + DEDUPLICATE**: [label-1], [label-2], [label-3]

**Step 3 SPLIT TRIGGER AUDIT**:
- [label-1]: [SPLIT-REQUIRED: "[original]" -> "[A]", "[B]" -- Trigger T[n]: [rule text] /
              SPLIT-NOT-TRIGGERED: T1 N, T2 N, T3 N, T4 N]
- [label-2]: [...]
- [label-3]: [...]

**Locked domain inventory** *(post-split)*:
1. [domain-A]
2. [domain-B]
3. [domain-C]

**INVENTORY LOCK COUNT**: [N]
**INVENTORY LOCK COMPLETE -- matrix row count = N**

---

## DOMAIN-ROLE COVERAGE MATRIX

*(Per §17d -- active roles only; EXCLUDED-LOW absent. Row count = N. No ledger row.)*

| Artifact Domain | [CHALLENGER_ROLE] | [DOMAIN_ROLE] | [LIFECYCLE_ROLE] | Gap Status |
|-----------------|-------------------|---------------|------------------|-----------|
| [domain-A]      | [H/M/L/--]        | [H/M/L/--]    | [H/M/L/--]       | [COVERED / DOMAIN-GAP] |
| [domain-B]      | [H/M/L/--]        | [H/M/L/--]    | [H/M/L/--]       | [COVERED / DOMAIN-GAP] |
| [domain-C]      | [H/M/L/--]        | [H/M/L/--]    | [H/M/L/--]       | [COVERED / DOMAIN-GAP] |

*(MATRIX CONTRACT CHECK: [N] rows = INVENTORY LOCK COUNT? [YES / VIOLATION])*

**ADVISORY-GAP items pre-registered**: [list or "None -- all COVERED"]

**COVERAGE MATRIX COMPLETE.**

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

### 2.0 DIMENSION TABLE *(all Category cells must be filled before emitting 2.1)*

| # | Dimension | Status Quo | Proposed State | Category (F/O/Q) |
|---|-----------|------------|----------------|-----------------|
| 1 | [DIM-1]   | [_]        | [_]            | [F/O/Q]         |
| 2 | [DIM-2]   | [_]        | [_]            | [F/O/Q]         |
| 3 | [DIM-3]   | [_]        | [_]            | [F/O/Q]         |

*(F = FAVORS-BUILD, O = OPEN-TO-DEBATE, Q = STATUS-QUO-WINS. No blanks. No prose in Category cell.)*

### 2.1 DIMENSION TABLE LOCKED

**DIMENSION TABLE LOCKED**: [n] rows. F=[a], O+Q=[b], D=a-b=[_]
Apply VERDICT THRESHOLD TABLE (§9): D=[_] -> **g_null(initial) = [PASS/CONDITIONAL/FAIL]**

### 2.2 NH TESTIMONY *(derived from DIMENSION TABLE above -- no new dimension evidence admitted)*

[Prose interpreting the locked table. Trace each claim to a dimension row number.
Example: "Dimension 1 (F -- FAVORS-BUILD): [interpretation]. Dimension 2 (O --
OPEN-TO-DEBATE): [interpretation]..."]

*(Any dimension claim not traceable to a DIMENSION TABLE row -> emit:
"UNDECLARED-DIMENSION: [claim] -- advisory only.")*

**Null hypothesis**: [What the team does today -- one sentence.]
**Null hypothesis strength**: [H/M/L]
**NULL HYPOTHESIS DERIVATION RULE**: g_null(initial) = threshold_table[D] per §9 Stage 1.

### 2.3 Challenge claims + GOpen

**Challenge claims**:
| CH-ID  | Claim | Severity |
|--------|-------|----------|
| CH-001 | [_]   | [H/M/L]  |
| CH-002 | [_]   | [H/M/L]  |

**GOpen Verdict**: [PASS/CONDITIONAL/FAIL] *(= g_null(initial) per §9)*
**GOpen Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section         | Gate  | Verdict | Class |
|-----------------|-------|---------|-------|
| BRACKET OPENING | GOpen | [_]     | [_]   |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table**:
| CH-ID  | Claim (copy) | Response | Status  |
|--------|-------------|----------|---------|
| CH-001 | [copy]      | [_]      | [A/P/O] |
| CH-002 | [copy]      | [_]      | [A/P/O] |

**Additional Findings** *(per §14, §11)*:
| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING] | [H/M/L] |
| F-2 | [§1:S-n] | [FINDING] | [H/M/L] |

**Finding Severity Aggregation**: `worst(F-1=[_], F-2=[_]) = [_]`
**Section Severity**: [H/M/L]

**LENS COVERAGE TABLE** *(Applicability from §17d matrix cell, this role x primary domain)*:
| # | lens.verify Entry | Applicability | Status | Finding Ref |
|---|------------------|--------------|--------|------------|
| 1 | [entry 1]        | [H/M/L]       | [A/O]  | [F-n]      |
| 2 | [entry 2]        | [H/M/L]       | [A/O]  | [F-n]      |

**G_domain Verdict**: [PASS/CONDITIONAL/FAIL] | **Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section               | Gate     | Verdict | Class |
|-----------------------|----------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [_]     | [_]   |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT *(EXCLUDED from ledger)*

```
G_domain_agg = worst([G_domain verdicts]) = [_]
g_null(post-domain) via §9 Stage 2: [_]
```

---

## §3.8 CH-ID SATURATION CHECK *(EXCLUDED from ledger)*

| CH-ID  | DOMAIN Status | Saturation  |
|--------|--------------|-------------|
| CH-001 | [A/P/O]      | [SAT/UNSAT] |
| CH-002 | [A/P/O]      | [SAT/UNSAT] |

**Unsaturated**: [list or "None"]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received: GOpen=[copy] | G_domain_agg=[copy] | g_null(post-domain)=[copy]

**CH-ID Response Table**:
| CH-ID  | Claim (copy) | Response | Status  |
|--------|-------------|----------|---------|
| CH-001 | [copy]      | [_]      | [A/P/O] |
| CH-002 | [copy]      | [_]      | [A/P/O] |

**Additional Findings** *(per §14, §11)*:
| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING] | [H/M/L] |
| F-2 | [§1:S-n] | [FINDING] | [H/M/L] |

**Finding Severity Aggregation**: `worst(F-1=[_], F-2=[_]) = [_]`
**Section Severity**: [H/M/L]

**LENS COVERAGE TABLE**:
| # | lens.verify Entry | Applicability | Status | Finding Ref |
|---|------------------|--------------|--------|------------|
| 1 | [entry 1]        | [H/M/L]       | [A/O]  | [F-n]      |
| 2 | [entry 2]        | [H/M/L]       | [A/O]  | [F-n]      |

**G_lifecycle Verdict**: [PASS/CONDITIONAL/FAIL] | **Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section                  | Gate        | Verdict | Class |
|--------------------------|-------------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [_]     | [_]   |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: CERT VALIDITY GATE=VALID, DIMENSION TABLE LOCKED, all CH-ID
tables, all gate verdicts.*

```
g_null(post-domain)=[copy] | G_lifecycle=[copy]
Apply §9 Stage 3 --> g_null(final)=[_]
```

**Full CH-ID Saturation**:
| CH-ID  | DOMAIN  | LIFECYCLE | Full Saturation |
|--------|---------|-----------|----------------|
| CH-001 | [copy]  | [copy]    | [FS/UNSAT]     |
| CH-002 | [copy]  | [copy]    | [FS/UNSAT]     |

**GClose Verdict**: [PASS/CONDITIONAL/FAIL] *(= g_null(final). Override: "g_null OVERRIDE: [justification]")*
**GClose Rationale**: [2-3 sentences referencing domain evidence, lifecycle verdict, and DIMENSION TABLE.]

**Local Gate Ledger Row**:
| Section         | Gate   | Verdict | Class |
|-----------------|--------|---------|-------|
| BRACKET CLOSING | GClose | [_]     | [_]   |

---

## §5.5 SCOPE COVERAGE RECONCILIATION *(EXCLUDED from ledger)*

| Surface  | Reviewer(s) | Finding(s) | Coverage         |
|----------|-------------|-----------|-----------------|
| [§1:S-1] | [ROLE]      | [F-n]     | [COVERED / GAP] |
| [§1:S-2] | [ROLE]      | [F-n]     | [COVERED / GAP] |

**Coverage gate signal**: [COVERED / PARTIAL] | **Advisory items**: [ADVISORY-GAP items or "None"]

---

## GATE VECTOR TABLE

| Gate         | Reviewer     | Verdict | Contract Cite           |
|--------------|-------------|---------|------------------------|
| GOpen        | [CHALLENGER] | [_]     | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN(S)]  | [_]     | DISPOSITION_CONTRACT v1 |
| G_lifecycle  | [LIFECYCLE]  | [_]     | DISPOSITION_CONTRACT v1 |
| GClose       | [CHALLENGER] | [_]     | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [named tension, or "None"]
**Convergence**: [named agreement across >= 2 roles]

**§13 Progression Ledger**:
```
g_null(initial)=[_] | g_null(post-domain)=[_] | g_null(final)=[_] | Trajectory: [STABLE/IMPROVING/DEGRADING]
```

---

## DISPOSITION

**Gate vector**: GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]
**Apply §3**: GClose=FAIL?->BLOCKED | Any FAIL?->BLOCKED | Any COND?->CONDITIONAL | All PASS?->READY
**Overall Disposition**: [BLOCKED / CONDITIONAL / READY]
**Primary Driver** *(per §16)*: [derived from gate vector]
**RESOLUTION REGISTRY** *(per §12)*: [table if CONDITIONAL; "N/A" otherwise]

---

## ACTION ITEM REGISTER

*(Copy local ledger rows verbatim per §6. No re-derivation.)*

| Section                  | Gate        | Verdict | Class  |
|--------------------------|-------------|---------|--------|
| BRACKET OPENING          | GOpen       | [copy]  | [copy] |
| DOMAIN -- [ROLE]         | G_domain    | [copy]  | [copy] |
| LIFECYCLE -- [ROLE]      | G_lifecycle | [copy]  | [copy] |
| BRACKET CLOSING          | GClose      | [copy]  | [copy] |

**Advisory items**: [ADVISORY-GAP, ADVISORY-ORPHAN, ADVISORY-OPEN-LENS,
                    UNDECLARED-DIMENSION, EXCLUDED-LOW coverage deficit, or "None"]

---

**Artifact to review:**

{{artifact}}

---

## Predicted R19 scores

| Variant | C-33 | C-34 | C-35 | Predicted |
|---------|------|------|------|-----------|
| V-01 | PASS (revision bound makes loop finite) | PASS (inherited from V-05 R18 §17c) | PASS (inherited) | 225/225 |
| V-02 | PASS (inherited from V-05 R18 §17b) | PASS (SPLIT TRIGGER LIST replaces editorial) | PASS (inherited) | 225/225 |
| V-03 | PASS (inherited) | PASS (inherited) | PASS (PRE-LOCK enforces table-before-prose) | 225/225 |
| V-04 | PASS | PASS | PASS | 225/225 |
| V-05 | PASS | PASS | PASS | 225/225 |

**Excellence Signals from R19:**

Pattern 11: REVISION TERMINATION BOUND -- a revision loop with no explicit cycle limit
can either cycle indefinitely or converge prematurely on a nominally-compliant entry.
Adding a hard bound (max 1 cycle) converts a potentially-unbounded process into a
finite decision: PASS on first entry, PASS on revision, or EXCLUDED-LOW. The bound
makes the cert check a three-outcome gate, not an iterative process.

Pattern 12: SPLIT TRIGGER AUDIT -- replacing qualitative judgment ("is this label
ambiguous?") with four enumerated mechanical triggers (Conjunction, Behavioral-
Structural, Component-Quality, Multi-ownership) forces the model to audit each label
against each rule and emit a notation (SPLIT-REQUIRED or SPLIT-NOT-TRIGGERED). The
notation is machine-readable: a scorer verifies the trigger decision without reading
domain knowledge.

Pattern 13: DIMENSION PRE-LOCK -- requiring the DIMENSION TABLE to be completed with
categorical (F/O/Q) cells before NH TESTIMONY begins enforces a separation of evidence-
collection from argument-construction. The DIMENSION TABLE LOCKED statement acts as a
structural barrier: all dimension ratings are committed, then prose is derived from the
committed values. Category assignment cannot be influenced by the prose being written
at the same time.

```json
{
  "round": 19,
  "rubric_version": "v11",
  "v11_round": 7,
  "date": "2026-03-17",
  "baseline": "V-05 R18",
  "top_score_predicted": 225,
  "max_score": 225,
  "variations": 5,
  "single_axis": ["V-01 (REVISION TERMINATION BOUND)", "V-02 (SPLIT TRIGGER AUDIT)", "V-03 (DIMENSION PRE-LOCK)"],
  "two_axis": "V-04 (V-01 + V-02)",
  "three_axis": "V-05 (V-01 + V-02 + V-03)",
  "c33_failure_addressed": "revision loop termination",
  "c34_failure_addressed": "mechanical trigger list replaces editorial split check",
  "c35_failure_addressed": "dimension table locked before NH prose"
}
```
