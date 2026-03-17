---
skill: quest-variate
skill_target: org-review
date: 2026-03-16
round: 18
rubric: org-review-rubric-v11-2026-03-16.md
---

# org-review -- Variate Round 18 (v11 rubric Round 6)

Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v11-2026-03-16.md

## Prior round summary

- R1--R11: V-05 climbed to 210/225. All §1--§16 contracts PASS. C-33/C-34/C-35 absent.
- R12: V-02 scored ~215/225 -- C-33+C-34+C-35 PASS but without §14/§15/§16.
- R13--R15: Targeted placement of C-33/C-34/C-35 individually.
- R16 (v11 R4): V-05 combined §17 manifest applicability + §18 domain gap-check + §19 NH
  dimension table as 225/225 candidate. Failure modes: generic CERT justifications,
  inconsistent domain labeling, underspecified VERDICT threshold.
- R17 (v11 R5): V-01 added §17a APPLICABILITY CERTIFICATION BLOCK (per-role justification);
  V-02 replaced prose gap-check with DOMAIN-ROLE COVERAGE MATRIX (rows=§1 domains, locked
  at matrix time); V-03 added CHALLENGER PRE-ASSESSMENT with NH DIMENSION TABLE and VERDICT
  column; V-05 combined all three.

## Round 18 (v11 R6) strategy

Baseline: V-05 R17 (§1--§17a + DOMAIN-ROLE COVERAGE MATRIX + CHALLENGER PRE-ASSESSMENT).

Identified failure modes in R17 V-05:

- **C-33**: APPLICABILITY CERTIFICATION BLOCK adds per-role justification but has no structural
  exit gate. Model may write a nominally complete entry (all fields present) whose Basis sentence
  describes artifact type rather than this artifact. No mechanism blocks BRACKET OPENING if
  justifications are generic.
- **C-34**: DOMAIN-ROLE COVERAGE MATRIX rows derive from §1 [DOMAIN: label] annotations that
  the model writes itself. Overly broad labels (e.g., one "architecture" label covering three
  distinct concerns) collapse into a single COVERED row, hiding real domain gaps.
- **C-35**: CHALLENGER PRE-ASSESSMENT has NH DIMENSION TABLE with VERDICT column, but §9 Stage 1
  formula says "majority FAVORS-BUILD" without defining majority. For close counts (3F:2O,
  2F:2O) the model reasons narratively rather than applying a mechanical threshold.

Round 18 targets one failure mode per single-axis variation, then combines:

- **V-01** (Lifecycle emphasis): CERT VALIDITY CHECK TABLE after APPLICABILITY CERTIFICATION
  BLOCK. Three binary columns (Domain Named Y/N, Lens Entry Quoted Y/N, Basis Artifact-Specific
  Y/N) plus computed Valid (ALL-YES / DOWNGRADE). CERT VALIDITY GATE blocks BRACKET OPENING
  until all entries = ALL-YES. Makes C-33 verifiable from Valid column alone.
- **V-02** (Output format): §17b ARTIFACT DOMAIN INVENTORY LOCK STEP before COVERAGE MATRIX.
  Model enumerates, deduplicates, and split-checks §1 domain labels into a locked numbered list.
  Matrix row count must equal INVENTORY LOCK COUNT. Mismatch halts. Makes C-34 anchored to a
  structurally verified domain set.
- **V-03** (Inertia framing): §9 Stage 1 extended with VERDICT THRESHOLD TABLE (D = F - O;
  explicit integer thresholds: D>=2 PASS, D=1 or D=0 CONDITIONAL, D<=-1 FAIL). PRE-ASSESSMENT
  emits VERDICT COUNT SUMMARY with D value. g_null(initial) derives from table[D], not prose.
  Makes C-35 verifiable from VERDICT COUNT SUMMARY + threshold lookup alone.
- **V-04** (Lifecycle + Output format): V-01 + V-02. C-33 + C-34 target.
- **V-05** (Lifecycle + Output format + Inertia framing): V-01 + V-02 + V-03. 225/225 candidate.

---

## V-01

**Axis**: Lifecycle emphasis -- CERT VALIDITY CHECK TABLE with exit gate
**Hypothesis**: R17 V-01 added the APPLICABILITY CERTIFICATION BLOCK requiring each role entry
to name (1) artifact domain, (2) lens.verify match, and (3) a basis sentence. The weakness:
the instruction says "generic justifications must be revised" but there is no structural exit
gate. The model may write a justification that nominally fills every field but whose Basis
sentence says "this role is relevant to this type of artifact." A scorer must read the prose
to judge. V-01 adds a CERT VALIDITY CHECK TABLE immediately after the APPLICABILITY
CERTIFICATION BLOCK: one row per role, three binary columns, and a computed Valid column
(ALL-YES if all three Y, else DOWNGRADE). A CERT VALIDITY GATE line follows:
"CERT VALIDITY GATE: VALID -- all ALL-YES. Reviewer sections may proceed."
If any row = DOWNGRADE, the gate reads INVALID and blocks BRACKET OPENING. Model must
revise the failing entry and re-emit the table. Makes C-33 mechanically verifiable: scorer
reads Valid column + gate line only.

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
pre-printed heading, label, field, formula, or structural element. If a field cannot be
filled, write `[N/A -- reason]`.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§17b;
reviewer sections may not execute until §1 COMPLETE, CERT VALIDITY
GATE = VALID, and §17b CERT CHECK COMPLETE markers are all reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]
  (Add rows. Domain labels used in §17 matrix and §5.5 reconciliation.)

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
  Each challenge claim receives CH-ID. Every downstream section carries CH-ID response table.
  PASS prohibited if any CH-ID row = OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section.
  Assembly: ACTION ITEM REGISTER copies verbatim. No re-derivation.
  EXCLUDED: §3.5, §3.8, §5.5, APPLICABILITY CERTIFICATION BLOCK,
            CERT VALIDITY CHECK TABLE.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.   ROLE MANIFEST
  1.5. APPLICABILITY CERTIFICATION BLOCK   [per §17a; no ledger row]
  1.6. CERT VALIDITY CHECK TABLE           [per §17b; exit gate; no ledger row]
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
  CERT VALIDITY GATE must = VALID before BRACKET OPENING.
  LIFECYCLE must precede BRACKET CLOSING.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID in >= 1 DOMAIN section (before LIFECYCLE).
  FULLY SATURATED: CH-ID in DOMAIN + LIFECYCLE (before BRACKET CLOSING).
  PASS prohibited without full saturation or stated waiver.
  Waiver: "CH-XXX WAIVER: [reason]"

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  g_null(initial) = GOpen.
  g_null(post-domain): FAIL if G_domain_agg=FAIL; max(g_null(initial),CONDITIONAL) if
  G_domain_agg=CONDITIONAL; g_null(initial) if G_domain_agg=PASS.
  g_null(final): FAIL if G_lifecycle=FAIL; max(g_null(post-domain),CONDITIONAL) if
  G_lifecycle=CONDITIONAL; g_null(post-domain) if G_lifecycle=PASS.
  GClose must equal g_null(final) or declare override.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps each §1 surface to findings. GAP -> ADVISORY-GAP in register.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding cites "[§1:S-n]". No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION = CONDITIONAL -> emit RESOLUTION REGISTRY table.

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  In CROSS-ROLE SIGNALS: g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Each finding row carries individual Severity. Section Severity = worst(all in section).

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE section emits LENS COVERAGE TABLE. Applicability from §17 ROLE
  MANIFEST rating. OPEN + HIGH-applicability -> ADVISORY-OPEN-LENS in register.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  GClose=FAIL -> GClose. G_domain=FAIL -> DOMAIN. G_lifecycle=FAIL -> LIFECYCLE.
  Any CONDITIONAL -> lowest-index gate. All PASS -> N/A.

§17 -- ROLE MANIFEST APPLICABILITY PROTOCOL [IMMUTABLE]
  ROLE MANIFEST includes Applicability column (HIGH/MEDIUM/LOW per role).
  HIGH = lens.verify directly addresses this artifact's primary domains.
  MEDIUM = partially addresses. LOW = limited applicability.
  §15 LENS COVERAGE TABLE inherits applicability from this manifest.

§17a -- APPLICABILITY CERTIFICATION REQUIREMENT [IMMUTABLE]
  After ROLE MANIFEST, before CERT VALIDITY CHECK TABLE, emit APPLICABILITY CERTIFICATION BLOCK.
  One entry per selected role. Format:
    Role [name]: Applicability = [HIGH/MEDIUM/LOW]
    Artifact domain: [specific §1 domain label this rating is based on]
    Lens.verify match: [specific lens.verify entry from this role's definition]
    Basis: [one sentence -- why this lens entry makes this role relevant to THIS artifact,
    not to the artifact type in general]
  Invalid: "relevant because [type] artifact" -- GENERIC.
  Invalid: no specific lens.verify entry cited -- INCOMPLETE.

§17b -- CERT VALIDITY CHECK REQUIREMENT [IMMUTABLE]
  After APPLICABILITY CERTIFICATION BLOCK, emit CERT VALIDITY CHECK TABLE. One row per role.
  Table: | Role | Domain Named (Y/N) | Lens Entry Quoted (Y/N) | Basis Artifact-Specific (Y/N) | Valid |
  Column rules (mechanical):
    Domain Named:             Y if Artifact domain names a specific §1 domain label. N otherwise.
    Lens Entry Quoted:        Y if Lens.verify match cites a specific entry from the role
                              definition (not a generic capability statement). N otherwise.
    Basis Artifact-Specific:  Y if Basis names a specific surface, section, field, or behavior
                              of THIS artifact (not of its artifact type). N otherwise.
    Valid:                    ALL-YES if all three Y. DOWNGRADE if any N.
  For any DOWNGRADE: revise APPLICABILITY CERTIFICATION BLOCK and ROLE MANIFEST Applicability
  to LOW for that role. Re-emit table. Repeat until all rows = ALL-YES.
  Emit CERT VALIDITY GATE:
    CERT VALIDITY GATE: VALID -- all ALL-YES. Proceed to BRACKET OPENING.
    OR: CERT VALIDITY GATE: INVALID -- [roles]. Revise before proceeding.
  BRACKET OPENING is blocked until gate = VALID.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale | Applicability |
|------|-----------|------|---------------------|---------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] | HIGH |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] | [HIGH/MEDIUM/LOW] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] | [HIGH/MEDIUM/LOW] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3 rows.)*

---

## APPLICABILITY CERTIFICATION BLOCK

*(Per §17a -- after ROLE MANIFEST, before CERT VALIDITY CHECK TABLE. No ledger row.)*

Role [challenger role name]: Applicability = HIGH
Artifact domain: [specific §1 domain label]
Lens.verify match: [specific lens.verify entry from this role's definition]
Basis: [one sentence -- why this lens entry applies to THIS artifact specifically]

Role [domain role name]: Applicability = [HIGH/MEDIUM/LOW]
Artifact domain: [specific §1 domain label with highest applicability]
Lens.verify match: [specific lens.verify entry]
Basis: [one sentence -- names a specific surface or behavior of THIS artifact]

Role [lifecycle role name]: Applicability = [HIGH/MEDIUM/LOW]
Artifact domain: [specific §1 domain label]
Lens.verify match: [specific lens.verify entry]
Basis: [one sentence -- names a specific surface of THIS artifact, not its type]

---

## CERT VALIDITY CHECK TABLE

*(Per §17b -- immediately after APPLICABILITY CERTIFICATION BLOCK. No ledger row.)*

| Role | Domain Named (Y/N) | Lens Entry Quoted (Y/N) | Basis Artifact-Specific (Y/N) | Valid |
|------|--------------------|------------------------|-------------------------------|-------|
| [challenger] | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |
| [domain]     | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |
| [lifecycle]  | [Y/N] | [Y/N] | [Y/N] | [ALL-YES / DOWNGRADE] |

*(For any DOWNGRADE: revise APPLICABILITY CERTIFICATION BLOCK and ROLE MANIFEST Applicability
to LOW, then re-emit this table. Repeat until all = ALL-YES.)*

**CERT VALIDITY GATE**: [VALID -- all ALL-YES. Reviewer sections may proceed.]

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]
**Null hypothesis strength**: [HIGH/MEDIUM/LOW]

**Alternatives comparison table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1]   | [score]       | [score]   | [score]              | |
| [DIM-2]   | [score]       | [score]   | [score]              | |
| [DIM-3]   | [score]       | [score]   | [score]              | |

**NULL HYPOTHESIS DERIVATION RULE** *(pre-committed per §9)*:
[Formula mapping B-A and B-C differentials to g_null verdict. Both differentials required.]

**Challenge claims**:

| CH-ID  | Challenge Claim | Severity |
|--------|----------------|----------|
| CH-001 | [CLAIM_1] | [H/M/L] |
| CH-002 | [CLAIM_2] | [H/M/L] |
| CH-003 | [optional] | [H/M/L] |

**GOpen Verdict**: [PASS/CONDITIONAL/FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)** *(= GOpen per §9)*: [PASS/CONDITIONAL/FAIL]

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
| CH-001 | [copy] | [_] | [A/P/O] |
| CH-002 | [copy] | [_] | [A/P/O] |

**Additional Findings** *(per §14, §11)*:
| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING] | [H/M/L] |
| F-2 | [§1:S-n] | [FINDING] | [H/M/L] |

**Finding Severity Aggregation**: `worst(F-1=[_],F-2=[_]) = [SECTION_SEVERITY]`
**Section Severity**: [H/M/L]

**LENS COVERAGE TABLE** *(Applicability from ROLE MANIFEST §17)*:
| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|-------------------|
| 1 | [entry 1] | [from ROLE MANIFEST] | [A/O] | [F-n] |
| 2 | [entry 2] | [from ROLE MANIFEST] | [A/O] | [F-n] |

**G_domain Verdict**: [PASS/CONDITIONAL/FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section               | Gate     | Verdict | Class |
|-----------------------|----------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [_]     | [_]   |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT *(EXCLUDED from ledger)*

```
G_domain_agg = worst([verdicts]) = [_]
g_null(post-domain) via §9 Stage 2: [_]
```

---

## §3.8 CH-ID SATURATION CHECK *(EXCLUDED from ledger)*

| CH-ID | DOMAIN Status | Saturation |
|-------|--------------|-----------|
| CH-001 | [status] | [SAT/UNSAT] |
| CH-002 | [status] | [SAT/UNSAT] |

**Unsaturated**: [list or "None"]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy] | G_domain_agg: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table**:
| CH-ID  | Claim (copy) | Response | Status |
|--------|-------------|----------|--------|
| CH-001 | [copy] | [_] | [A/P/O] |
| CH-002 | [copy] | [_] | [A/P/O] |

**Additional Findings** *(per §14, §11)*:
| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING] | [H/M/L] |
| F-2 | [§1:S-n] | [FINDING] | [H/M/L] |

**Finding Severity Aggregation**: `worst(F-1=[_],F-2=[_]) = [SECTION_SEVERITY]`
**Section Severity**: [H/M/L]

**LENS COVERAGE TABLE** *(Applicability from ROLE MANIFEST §17)*:
| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|-------------------|
| 1 | [entry 1] | [from ROLE MANIFEST] | [A/O] | [F-n] |
| 2 | [entry 2] | [from ROLE MANIFEST] | [A/O] | [F-n] |

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
| CH-ID | DOMAIN | LIFECYCLE | Full Saturation |
|-------|--------|-----------|----------------|
| CH-001 | [copy] | [copy] | [FS/UNSAT] |
| CH-002 | [copy] | [copy] | [FS/UNSAT] |

**GClose Verdict**: [PASS/CONDITIONAL/FAIL] *(= g_null(final). Override: "g_null OVERRIDE: [reason]")*
**GClose Rationale**: [2-3 sentences.]

**Local Gate Ledger Row**:
| Section         | Gate   | Verdict | Class |
|-----------------|--------|---------|-------|
| BRACKET CLOSING | GClose | [_]     | [_]   |

---

## §5.5 SCOPE COVERAGE RECONCILIATION *(EXCLUDED from ledger)*

| Surface | Reviewer(s) | Finding(s) | Coverage |
|---------|-------------|-----------|---------|
| [§1:S-1] | [ROLE] | [F-n] | [COVERED/GAP] |
| [§1:S-2] | [ROLE] | [F-n] | [COVERED/GAP] |

**Coverage gate signal**: [COVERED/PARTIAL] | **Advisory items**: [list or "None"]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|--------------|
| GOpen | [CHALLENGER] | [_] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN(S)] | [_] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [_] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [_] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [or "None"]
**Convergence**: [cross-role signal]

**§13 Progression Ledger**:
```
g_null(initial)=[_] | g_null(post-domain)=[_] | g_null(final)=[_] | Trajectory: [label]
```

---

## DISPOSITION

**Gate vector**: GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]
**Apply §3**: GClose=FAIL?->BLOCKED | Any FAIL?->BLOCKED | Any COND?->CONDITIONAL | All PASS?->READY
**Overall Disposition**: [BLOCKED/CONDITIONAL/READY]
**Primary Driver** *(per §16)*: [derived]
**RESOLUTION REGISTRY** *(per §12)*: [table if CONDITIONAL; else "N/A"]

---

## ACTION ITEM REGISTER

*(Copy local ledger rows verbatim. Do not re-derive.)*

| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [copy] | [copy] |
| DOMAIN -- [ROLE] | G_domain | [copy] | [copy] |
| LIFECYCLE -- [ROLE] | G_lifecycle | [copy] | [copy] |
| BRACKET CLOSING | GClose | [copy] | [copy] |

**Advisory items**: [ADVISORY-GAP, ADVISORY-ORPHAN, ADVISORY-OPEN-LENS, or "None"]

---

**Artifact to review:**

{{artifact}}

---
---

## V-02

**Axis**: Output format -- §17b ARTIFACT DOMAIN INVENTORY LOCK STEP (C-34 anchoring)
**Hypothesis**: R17 V-02 builds the DOMAIN-ROLE COVERAGE MATRIX with rows = §1 [DOMAIN: label]
annotations. The weakness: the model writes those annotations itself and may use overly broad
labels that conflate multiple distinct concerns into one COVERED row, hiding a real domain gap.
V-02 adds §17b ARTIFACT DOMAIN INVENTORY LOCK STEP between ROLE MANIFEST and COVERAGE MATRIX.
The model scans §1 labels, deduplicates, applies a SPLIT CHECK (does this label cover more than
one concern that could independently have no HIGH-applicability reviewer?), and locks a numbered
inventory list with INVENTORY LOCK COUNT: N. The matrix must have exactly N rows. A count
mismatch is a contract violation that halts execution. C-34 is now anchored to a structurally
verified, split-checked domain set: scorer verifies by counting inventory entries and matrix rows.

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
pre-printed heading, label, field, formula, or structural element. If a field cannot be
filled, write `[N/A -- reason]`.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§17b;
reviewer sections may not execute until §1 COMPLETE, INVENTORY LOCK
COMPLETE, and COVERAGE MATRIX COMPLETE markers are all reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]
  (Add rows. Use specific domain labels -- one distinct concern per label.
  Broad labels conflating multiple concerns will be split in §17b.)

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
  Each challenge claim receives CH-ID. Every downstream section carries CH-ID response table.
  PASS prohibited if any CH-ID row = OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section.
  Assembly: ACTION ITEM REGISTER copies verbatim. No re-derivation.
  EXCLUDED: §3.5, §3.8, §5.5, ARTIFACT DOMAIN INVENTORY, DOMAIN-ROLE COVERAGE MATRIX.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.   ROLE MANIFEST
  1.3. ARTIFACT DOMAIN INVENTORY     [per §17b; locked list; no ledger row]
  1.5. DOMAIN-ROLE COVERAGE MATRIX   [per §17; pre-reviewer; no ledger row]
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
  INVENTORY LOCK COMPLETE must precede COVERAGE MATRIX.
  COVERAGE MATRIX must precede BRACKET OPENING.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID in >= 1 DOMAIN (before LIFECYCLE).
  FULLY SATURATED: CH-ID in DOMAIN + LIFECYCLE (before BRACKET CLOSING).
  PASS prohibited without full saturation or stated waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  g_null(initial) = GOpen.
  g_null(post-domain): FAIL if G_domain_agg=FAIL; max(g_null(initial),CONDITIONAL) if
  G_domain_agg=CONDITIONAL; g_null(initial) if G_domain_agg=PASS.
  g_null(final): FAIL if G_lifecycle=FAIL; max(g_null(post-domain),CONDITIONAL) if
  G_lifecycle=CONDITIONAL; g_null(post-domain) if G_lifecycle=PASS.
  GClose must equal g_null(final) or declare override.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps each §1 surface to findings. GAP -> ADVISORY-GAP in register.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding cites "[§1:S-n]". No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION = CONDITIONAL -> emit RESOLUTION REGISTRY table.

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  In CROSS-ROLE SIGNALS: g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Each finding row carries individual Severity. Section Severity = worst(all in section).

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE section emits LENS COVERAGE TABLE. Applicability from §17 matrix cell
  (this role x primary domain). OPEN + HIGH-applicability -> ADVISORY-OPEN-LENS.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  GClose=FAIL->GClose. G_domain=FAIL->DOMAIN. G_lifecycle=FAIL->LIFECYCLE.
  Any CONDITIONAL -> lowest-index. All PASS -> N/A.

§17 -- DOMAIN-ROLE COVERAGE MATRIX CONTRACT [IMMUTABLE]
  After INVENTORY LOCK COMPLETE, produce a DOMAIN-ROLE COVERAGE MATRIX.
  Rows: each locked domain from ARTIFACT DOMAIN INVENTORY.
  Columns: each selected role from ROLE MANIFEST.
  Cells: HIGH/MEDIUM/LOW/-- (role x domain applicability).
  Matrix row count must equal INVENTORY LOCK COUNT. Mismatch = contract violation; halt and
  state: "MATRIX CONTRACT VIOLATION: expected N rows, built M rows. Revise §1 annotations."
  Domain gap (mechanical): no HIGH cell in row -> DOMAIN-GAP ->
    ADVISORY-GAP item: "ADVISORY-GAP: [domain] -- no HIGH-applicability reviewer. [reason]"
  §15 Applicability: use matrix cell for (this role, primary artifact domain).

§17b -- ARTIFACT DOMAIN INVENTORY PROTOCOL [IMMUTABLE]
  Before DOMAIN-ROLE COVERAGE MATRIX, emit ARTIFACT DOMAIN INVENTORY.
  Step 1 SCAN: extract all unique [DOMAIN: label] values from §1 IN-SCOPE rows.
  Step 2 DEDUPLICATE: one entry per unique label (same label on multiple surfaces = one entry).
  Step 3 SPLIT CHECK: for each entry, ask: "Does this label cover more than one distinct
    concern that could independently have no HIGH-applicability reviewer, hidden inside a
    COVERED row?" If yes: split and update §1 annotations.
    State: "SPLIT: [original] -> [A], [B] -- reason for split"
  Step 4 LOCK: emit numbered list. State INVENTORY LOCK COUNT: N.
  Emit "INVENTORY LOCK COMPLETE -- matrix row count = N" before COVERAGE MATRIX.

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

## ARTIFACT DOMAIN INVENTORY

*(Per §17b -- before COVERAGE MATRIX. No ledger row.)*

**Step 1-2 SCAN + DEDUPLICATE** -- unique [DOMAIN: label] values from §1:
- [label-1], [label-2], [label-3] (list all)

**Step 3 SPLIT CHECK**:
- [label-1]: [KEPT -- single distinct concern]
- [label-2]: [KEPT / SPLIT: [original] -> [A], [B] -- reason]
- (repeat per label)

**Locked domain inventory**:
1. [domain-A]
2. [domain-B]
3. [domain-C]

**INVENTORY LOCK COUNT**: [N]
**INVENTORY LOCK COMPLETE -- matrix row count = N**

---

## DOMAIN-ROLE COVERAGE MATRIX

*(Per §17 -- rows = locked inventory; count must = N. No ledger row.)*

| Artifact Domain | [CHALLENGER_ROLE] | [DOMAIN_ROLE] | [LIFECYCLE_ROLE] | Gap Status |
|-----------------|-------------------|---------------|------------------|-----------|
| [domain-A] | [H/M/L/--] | [H/M/L/--] | [H/M/L/--] | [DOMAIN-COVERED/DOMAIN-GAP] |
| [domain-B] | [H/M/L/--] | [H/M/L/--] | [H/M/L/--] | [DOMAIN-COVERED/DOMAIN-GAP] |
| [domain-C] | [H/M/L/--] | [H/M/L/--] | [H/M/L/--] | [DOMAIN-COVERED/DOMAIN-GAP] |

*(MATRIX CONTRACT CHECK: N rows = INVENTORY LOCK COUNT? [YES / VIOLATION])*

**ADVISORY-GAP items pre-registered**:
- [domain if DOMAIN-GAP]: "ADVISORY-GAP: [domain] -- no HIGH-applicability reviewer."
- (or "None -- all COVERED")

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today -- one sentence.]
**Null hypothesis strength**: [H/M/L]

**Alternatives comparison table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1]   | [score] | [score] | [score] | |
| [DIM-2]   | [score] | [score] | [score] | |
| [DIM-3]   | [score] | [score] | [score] | |

**NULL HYPOTHESIS DERIVATION RULE**: [Formula over B-A and B-C differentials.]

**Challenge claims**:
| CH-ID  | Claim | Severity |
|--------|-------|----------|
| CH-001 | [_] | [H/M/L] |
| CH-002 | [_] | [H/M/L] |

**GOpen Verdict**: [_] | **GOpen Reason**: [One sentence.]
**g_null(initial)** *(= GOpen)*: [_]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [_] | [_] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1 | Received GOpen: [copy]

**CH-ID Response Table**:
| CH-ID | Claim (copy) | Response | Status |
|-------|-------------|----------|--------|
| CH-001 | [copy] | [_] | [A/P/O] |
| CH-002 | [copy] | [_] | [A/P/O] |

**Additional Findings**:
| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [_] | [H/M/L] |
| F-2 | [§1:S-n] | [_] | [H/M/L] |

**Section Severity** *(worst per §14)*: [H/M/L]

**LENS COVERAGE TABLE** *(Applicability from §17 matrix cell)*:
| # | lens.verify Entry | Applicability | Status | Finding Ref |
|---|------------------|--------------|--------|------------|
| 1 | [entry 1] | [matrix cell] | [A/O] | [F-n] |
| 2 | [entry 2] | [matrix cell] | [A/O] | [F-n] |

**G_domain Verdict**: [_] | **Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [_] | [_] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT *(EXCLUDED)*

```
G_domain_agg = worst([verdicts]) = [_]
g_null(post-domain) via §9: [_]
```

---

## §3.8 CH-ID SATURATION CHECK *(EXCLUDED)*

| CH-ID | DOMAIN Status | Saturation |
|-------|--------------|-----------|
| CH-001 | [_] | [SAT/UNSAT] |
| CH-002 | [_] | [SAT/UNSAT] |

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1 | GOpen: [copy] | G_domain_agg: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table**:
| CH-ID | Claim (copy) | Response | Status |
|-------|-------------|----------|--------|
| CH-001 | [copy] | [_] | [A/P/O] |
| CH-002 | [copy] | [_] | [A/P/O] |

**Additional Findings**:
| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [_] | [H/M/L] |
| F-2 | [§1:S-n] | [_] | [H/M/L] |

**Section Severity** *(worst per §14)*: [H/M/L]

**LENS COVERAGE TABLE**:
| # | lens.verify Entry | Applicability | Status | Finding Ref |
|---|------------------|--------------|--------|------------|
| 1 | [entry 1] | [matrix cell] | [A/O] | [F-n] |
| 2 | [entry 2] | [matrix cell] | [A/O] | [F-n] |

**G_lifecycle Verdict**: [_] | **Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [_] | [_] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

```
g_null(post-domain)=[copy] | G_lifecycle=[copy]
Apply §9 Stage 3 --> g_null(final)=[_]
```

**Full CH-ID Saturation**:
| CH-ID | DOMAIN | LIFECYCLE | Full Saturation |
|-------|--------|-----------|----------------|
| CH-001 | [copy] | [copy] | [FS/UNSAT] |
| CH-002 | [copy] | [copy] | [FS/UNSAT] |

**GClose Verdict**: [_] *(= g_null(final). Override: "g_null OVERRIDE: [reason]")*
**GClose Rationale**: [2-3 sentences.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [_] | [_] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION *(EXCLUDED)*

| Surface | Reviewer(s) | Finding(s) | Coverage |
|---------|-------------|-----------|---------|
| [§1:S-1] | [ROLE] | [F-n] | [COVERED/GAP] |

**Coverage gate**: [COVERED/PARTIAL] | **Advisory items**: [list or "None"]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|--------------|
| GOpen | [CHALLENGER] | [_] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN(S)] | [_] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [_] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [_] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [or "None"] | **Convergence**: [signal]

**§13 Progression Ledger**:
```
g_null(initial)=[_] | g_null(post-domain)=[_] | g_null(final)=[_] | Trajectory: [label]
```

---

## DISPOSITION

**Gate vector**: GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]
**Apply §3**: GClose=FAIL?->BLOCKED | Any FAIL?->BLOCKED | Any COND?->CONDITIONAL | All PASS?->READY
**Overall Disposition**: [_] | **Primary Driver** *(per §16)*: [_]
**RESOLUTION REGISTRY**: [table if CONDITIONAL; else "N/A"]

---

## ACTION ITEM REGISTER

*(Copy verbatim. Do not re-derive.)*

| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [copy] | [copy] |
| DOMAIN -- [ROLE] | G_domain | [copy] | [copy] |
| LIFECYCLE -- [ROLE] | G_lifecycle | [copy] | [copy] |
| BRACKET CLOSING | GClose | [copy] | [copy] |

**Advisory items**: [ADVISORY-GAP from §17, ADVISORY-ORPHAN, ADVISORY-OPEN-LENS, or "None"]

---

**Artifact to review:**

{{artifact}}

---
---

## V-03

**Axis**: Inertia framing -- §9 VERDICT THRESHOLD TABLE for mechanical g_null(initial) (C-35)
**Hypothesis**: R17 V-03 introduced CHALLENGER PRE-ASSESSMENT with NH DIMENSION TABLE and VERDICT
column (FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD). §9 Stage 1 says g_null(initial) derives from
"majority FAVORS-BUILD" but does not define majority with integer thresholds. For close counts
(e.g., 3F:2O or 2F:2O) the model reasons narratively. V-03 replaces the prose rule with a
VERDICT THRESHOLD TABLE in §9: D = F - O (signed integer); D>=2: PASS; D=1 or D=0: CONDITIONAL;
D<=-1: FAIL. PRE-ASSESSMENT emits VERDICT COUNT SUMMARY with F, O, N, D values. g_null(initial)
= table[D]. C-35 is now verifiable by a scorer computing D from the count summary and looking up
the pre-committed table -- no prose reading required.

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
pre-printed heading, label, field, formula, or structural element. If a field cannot be
filled, write `[N/A -- reason]`.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§17c;
reviewer sections may not execute until §1 COMPLETE and
CHALLENGER PRE-ASSESSMENT COMPLETE markers are both reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]
  (Add rows. Domain labels feed §17 matrix and §5.5 reconciliation.)

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
  Each challenge claim receives CH-ID. Every downstream carries CH-ID response table.
  PASS prohibited if any CH-ID row = OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section.
  Assembly: ACTION ITEM REGISTER copies verbatim. No re-derivation.
  EXCLUDED: §3.5, §3.8, §5.5, CHALLENGER PRE-ASSESSMENT, DOMAIN-ROLE COVERAGE MATRIX.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  0.5. CHALLENGER PRE-ASSESSMENT     [per §17c; before ROLE MANIFEST; no ledger row]
  1.   ROLE MANIFEST
  1.5. DOMAIN-ROLE COVERAGE MATRIX   [per §17; pre-reviewer; no ledger row]
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
  CHALLENGER PRE-ASSESSMENT must precede ROLE MANIFEST.
  LIFECYCLE must precede BRACKET CLOSING.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID in >= 1 DOMAIN (before LIFECYCLE).
  FULLY SATURATED: CH-ID in DOMAIN + LIFECYCLE (before BRACKET CLOSING).
  PASS prohibited without full saturation or stated waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1 -- g_null(initial) [derived at CHALLENGER PRE-ASSESSMENT, inherited by BRACKET OPENING]:
    Step A: PRE-ASSESSMENT emits VERDICT COUNT SUMMARY:
      F = count of FAVORS-BUILD verdicts in NH DIMENSION TABLE
      O = count of OPPOSES-BUILD verdicts in NH DIMENSION TABLE
      N = count of NEUTRAL verdicts
      D = F - O  (signed integer)
    Step B: Apply VERDICT THRESHOLD TABLE [IMMUTABLE -- do not alter]:
      D >= 2:  g_null(initial) = PASS         [build clearly favored]
      D = 1:   g_null(initial) = CONDITIONAL  [build modestly favored]
      D = 0:   g_null(initial) = CONDITIONAL  [tie -- insufficient differentiation]
      D = -1:  g_null(initial) = FAIL         [status quo favored on balance]
      D <= -2: g_null(initial) = FAIL         [status quo clearly preferred]
    Step C: Emit "g_null(initial) = [PASS/CONDITIONAL/FAIL] via D=[value]"
    GOpen inherits g_null(initial) from PRE-ASSESSMENT. Do not re-derive.
  Stage 2 -- g_null(post-domain) [emitted at §3.5]:
    if G_domain_agg=FAIL: g_null(post-domain)=FAIL
    if G_domain_agg=CONDITIONAL: g_null(post-domain)=max(g_null(initial),CONDITIONAL)
    if G_domain_agg=PASS: g_null(post-domain)=g_null(initial)
  Stage 3 -- g_null(final) [emitted at BRACKET CLOSING]:
    if G_lifecycle=FAIL: g_null(final)=FAIL
    if G_lifecycle=CONDITIONAL: g_null(final)=max(g_null(post-domain),CONDITIONAL)
    if G_lifecycle=PASS: g_null(final)=g_null(post-domain)
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
  Each DOMAIN/LIFECYCLE section emits LENS COVERAGE TABLE. Applicability from §17 ROLE MANIFEST
  rating. OPEN + HIGH-applicability -> ADVISORY-OPEN-LENS.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  GClose=FAIL->GClose. G_domain=FAIL->DOMAIN. G_lifecycle=FAIL->LIFECYCLE.
  Any CONDITIONAL->lowest-index. All PASS->N/A.

§17 -- ROLE MANIFEST APPLICABILITY PROTOCOL [IMMUTABLE]
  ROLE MANIFEST includes Applicability column (HIGH/MEDIUM/LOW per role).
  HIGH = lens.verify directly addresses this artifact's primary domains.
  MEDIUM = partially. LOW = limited. §15 inherits from this manifest.

§17c -- CHALLENGER PRE-ASSESSMENT PROTOCOL [IMMUTABLE]
  Runs before ROLE MANIFEST. Not a reviewer section (no contract cite, no CH-IDs, no ledger row).
  Purpose: derive g_null(initial) mechanically via §9 Stage 1 VERDICT THRESHOLD TABLE.

  NH DIMENSION TABLE format:
    | Dimension | What Challenger Assesses | Status Quo (A) | Build (B) | Verdict |
  Verdict column: FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD only.
    FAVORS-BUILD:  Build meaningfully better than Status Quo on this dimension.
    NEUTRAL:       Build and Status Quo comparable on this dimension.
    OPPOSES-BUILD: Status Quo comparable or better than Build on this dimension.
  Minimum 3 dimensions. Each row = one null hypothesis axis.

  After table: emit VERDICT COUNT SUMMARY and apply §9 Stage 1 VERDICT THRESHOLD TABLE.
  State: "g_null(initial) = [PASS/CONDITIONAL/FAIL] via D=[value]"
  Emit "CHALLENGER PRE-ASSESSMENT COMPLETE" before ROLE MANIFEST.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## CHALLENGER PRE-ASSESSMENT

*(Per §17c -- before ROLE MANIFEST. No contract cite, no CH-IDs, no ledger row.)*

**NH DIMENSION TABLE** *(minimum 3 dimensions)*:

| Dimension | What Challenger Assesses | Status Quo (A) | Build (B) | Verdict |
|-----------|--------------------------|---------------|-----------|---------|
| [DIM-1]   | [one sentence]           | [assessment]  | [assessment] | [FAVORS-BUILD/NEUTRAL/OPPOSES-BUILD] |
| [DIM-2]   | [one sentence]           | [assessment]  | [assessment] | [FAVORS-BUILD/NEUTRAL/OPPOSES-BUILD] |
| [DIM-3]   | [one sentence]           | [assessment]  | [assessment] | [FAVORS-BUILD/NEUTRAL/OPPOSES-BUILD] |
| [DIM-4 -- optional] | [one sentence] | [assessment] | [assessment] | [FAVORS-BUILD/NEUTRAL/OPPOSES-BUILD] |

**VERDICT COUNT SUMMARY** *(per §9 Stage 1 Step A)*:
```
F (FAVORS-BUILD)  = [count]
O (OPPOSES-BUILD) = [count]
N (NEUTRAL)       = [count]
D = F - O         = [signed integer]
```

**Apply VERDICT THRESHOLD TABLE** *(§9 Stage 1 Step B -- thresholds immutable)*:
```
D >= 2  --> PASS         D = 1  --> CONDITIONAL
D = 0   --> CONDITIONAL  D = -1 --> FAIL
D <= -2 --> FAIL

D = [value] --> g_null(initial) = [PASS/CONDITIONAL/FAIL]
```

**g_null(initial)**: [PASS/CONDITIONAL/FAIL]  *(derived from D -- not prose; BRACKET OPENING inherits)*

**CHALLENGER PRE-ASSESSMENT COMPLETE**

---

## ROLE MANIFEST

| Slot | Archetype | Role | Selection Rationale | Applicability |
|------|-----------|------|---------------------|---------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] | HIGH |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] | [H/M/L] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] | [H/M/L] |

---

## DOMAIN-ROLE COVERAGE MATRIX

*(Per §17 -- rows = §1 domain labels. No ledger row.)*

| Artifact Domain | [CHALLENGER_ROLE] | [DOMAIN_ROLE] | [LIFECYCLE_ROLE] | Gap Status |
|-----------------|-------------------|---------------|------------------|-----------|
| [domain-1] | [H/M/L/--] | [H/M/L/--] | [H/M/L/--] | [DOMAIN-COVERED/DOMAIN-GAP] |
| [domain-2] | [H/M/L/--] | [H/M/L/--] | [H/M/L/--] | [DOMAIN-COVERED/DOMAIN-GAP] |

**ADVISORY-GAP items pre-registered**:
- [domain if DOMAIN-GAP]: "ADVISORY-GAP: [domain] -- no HIGH-applicability reviewer."
- (or "None")

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today -- one sentence.]
**Null hypothesis strength**: [H/M/L]
*(g_null(initial) inherited from PRE-ASSESSMENT -- do not re-derive.)*

**Challenge claims** *(grounded in NEUTRAL/OPPOSES-BUILD dimensions from PRE-ASSESSMENT)*:
| CH-ID  | Claim | Severity |
|--------|-------|----------|
| CH-001 | [CLAIM grounded in PRE-ASSESSMENT dimension] | [H/M/L] |
| CH-002 | [CLAIM] | [H/M/L] |

**GOpen Verdict**: [_] *(must equal g_null(initial) from PRE-ASSESSMENT)*
**GOpen Reason**: [One sentence referencing D value and dominant dimension.]
**g_null(initial)** *(inherited)*: [copy from PRE-ASSESSMENT]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [_] | [_] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1 | Received GOpen: [copy]

**CH-ID Response Table**:
| CH-ID | Claim (copy) | Response | Status |
|-------|-------------|----------|--------|
| CH-001 | [copy] | [_] | [A/P/O] |
| CH-002 | [copy] | [_] | [A/P/O] |

**Additional Findings**:
| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [_] | [H/M/L] |
| F-2 | [§1:S-n] | [_] | [H/M/L] |

**Section Severity** *(worst per §14)*: [H/M/L]

**LENS COVERAGE TABLE** *(Applicability from ROLE MANIFEST)*:
| # | lens.verify Entry | Applicability | Status | Finding Ref |
|---|------------------|--------------|--------|------------|
| 1 | [entry 1] | [from manifest] | [A/O] | [F-n] |
| 2 | [entry 2] | [from manifest] | [A/O] | [F-n] |

**G_domain Verdict**: [_] | **Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [_] | [_] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT *(EXCLUDED)*

```
G_domain_agg = worst([verdicts]) = [_]
g_null(post-domain) via §9: [_]
```

---

## §3.8 CH-ID SATURATION CHECK *(EXCLUDED)*

| CH-ID | DOMAIN Status | Saturation |
|-------|--------------|-----------|
| CH-001 | [_] | [SAT/UNSAT] |
| CH-002 | [_] | [SAT/UNSAT] |

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1 | GOpen: [copy] | G_domain_agg: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table**:
| CH-ID | Claim (copy) | Response | Status |
|-------|-------------|----------|--------|
| CH-001 | [copy] | [_] | [A/P/O] |
| CH-002 | [copy] | [_] | [A/P/O] |

**Additional Findings**:
| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [_] | [H/M/L] |
| F-2 | [§1:S-n] | [_] | [H/M/L] |

**Section Severity** *(worst per §14)*: [H/M/L]

**LENS COVERAGE TABLE** *(Applicability from ROLE MANIFEST)*:
| # | lens.verify Entry | Applicability | Status | Finding Ref |
|---|------------------|--------------|--------|------------|
| 1 | [entry 1] | [from manifest] | [A/O] | [F-n] |
| 2 | [entry 2] | [from manifest] | [A/O] | [F-n] |

**G_lifecycle Verdict**: [_] | **Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [_] | [_] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

```
g_null(post-domain)=[copy] | G_lifecycle=[copy]
Apply §9 Stage 3 --> g_null(final)=[_]
```

**Full CH-ID Saturation**:
| CH-ID | DOMAIN | LIFECYCLE | Full Saturation |
|-------|--------|-----------|----------------|
| CH-001 | [copy] | [copy] | [FS/UNSAT] |
| CH-002 | [copy] | [copy] | [FS/UNSAT] |

**GClose Verdict**: [_] *(= g_null(final). Override: "g_null OVERRIDE: [reason]")*
**GClose Rationale**: [2-3 sentences referencing g_null(initial) D=[value], trajectory.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [_] | [_] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION *(EXCLUDED)*

| Surface | Reviewer(s) | Finding(s) | Coverage |
|---------|-------------|-----------|---------|
| [§1:S-1] | [ROLE] | [F-n] | [COVERED/GAP] |

**Coverage gate**: [COVERED/PARTIAL] | **Advisory items**: [list or "None"]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|--------------|
| GOpen | [CHALLENGER] | [_] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN(S)] | [_] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [_] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [_] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [or "None"] | **Convergence**: [signal]

**§13 Progression Ledger**:
```
g_null(initial)=[_] [D=[value]] | g_null(post-domain)=[_] | g_null(final)=[_] | Trajectory: [label]
```

---

## DISPOSITION

**Gate vector**: GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]
**Apply §3**: GClose=FAIL?->BLOCKED | Any FAIL?->BLOCKED | Any COND?->CONDITIONAL | All PASS?->READY
**Overall Disposition**: [_] | **Primary Driver** *(per §16)*: [_]
**RESOLUTION REGISTRY**: [table if CONDITIONAL; else "N/A"]

---

## ACTION ITEM REGISTER

*(Copy verbatim. Do not re-derive.)*

| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [copy] | [copy] |
| DOMAIN -- [ROLE] | G_domain | [copy] | [copy] |
| LIFECYCLE -- [ROLE] | G_lifecycle | [copy] | [copy] |
| BRACKET CLOSING | GClose | [copy] | [copy] |

**Advisory items**: [ADVISORY-GAP from §17, ADVISORY-ORPHAN, ADVISORY-OPEN-LENS, or "None"]

---

**Artifact to review:**

{{artifact}}

---
---

## V-04

**Axes**: Lifecycle emphasis + Output format -- CERT VALIDITY GATE + DOMAIN INVENTORY LOCK (C-33 + C-34)
**Hypothesis**: V-01 closes the C-33 structural enforcement gap with a CERT VALIDITY CHECK TABLE
and blocking gate. V-02 closes the C-34 domain taxonomy gap with a §17b ARTIFACT DOMAIN
INVENTORY LOCK STEP. The two axes are independent: V-01 validates role-column applicability
ratings (per-role certification); V-02 validates domain-row taxonomy (pre-matrix inventory).
Combining them addresses both vertical (column) and horizontal (row) dimensions of the
DOMAIN-ROLE COVERAGE MATRIX simultaneously. V-04 isolates the C-33+C-34 two-axis combination
before the full triple-axis V-05.

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
pre-printed heading, label, field, formula, or structural element. If a field cannot be
filled, write `[N/A -- reason]`.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§17c;
reviewer sections may not execute until §1 COMPLETE, INVENTORY LOCK
COMPLETE, and CERT VALIDITY GATE = VALID are all reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE:
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]
  (Specific domain labels -- one distinct concern per label. Broad labels split in §17b.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON]

Scope Amendment: SCOPE AMENDMENT: [surface] -- [reason]
§1 COMPLETE.

§2 SEVERITY SEMANTICS [IMMUTABLE]: HIGH=Blocks. MEDIUM=Conditions. LOW=Advisory.

§3 DISPOSITION ALGEBRA [IMMUTABLE]:
  BLOCKED <-- GClose=FAIL OR exists Gi=FAIL
  CONDITIONAL <-- no FAIL AND exists CONDITIONAL
  READY <-- all PASS

§3a DOMAIN-AGGREGATE FORMULA [IMMUTABLE]: G_domain_agg = worst(all G_domain). FAIL>CONDITIONAL>PASS.

§4 CONTRACT CITE [IMMUTABLE]: Each reviewer section opens with "Contract: DISPOSITION_CONTRACT v1"

§5 CH-ID TRACING [IMMUTABLE]: Each claim gets CH-ID. All downstream sections carry CH-ID table.
  PASS prohibited if any CH-ID = OPEN.

§6 LOCAL GATE LEDGER [IMMUTABLE]:
  Row: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section. Assembly: verbatim copy, no re-derivation.
  EXCLUDED: §3.5, §3.8, §5.5, ARTIFACT DOMAIN INVENTORY, DOMAIN-ROLE COVERAGE MATRIX,
            APPLICABILITY CERTIFICATION BLOCK, CERT VALIDITY CHECK TABLE.

§7 SECTION ORDER [IMMUTABLE]:
  1.   ROLE MANIFEST
  1.3. ARTIFACT DOMAIN INVENTORY     [§17b; locked list; no ledger row]
  1.5. DOMAIN-ROLE COVERAGE MATRIX   [§17; pre-reviewer; no ledger row]
  1.7. APPLICABILITY CERTIFICATION BLOCK  [§17a; no ledger row]
  1.8. CERT VALIDITY CHECK TABLE     [§17c; exit gate; no ledger row]
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
  CERT VALIDITY GATE must = VALID before BRACKET OPENING.

§8 CH-ID SATURATION [IMMUTABLE]: SATURATED=DOMAIN response before LIFECYCLE.
  FULLY SATURATED=DOMAIN+LIFECYCLE before BRACKET CLOSING. PASS prohibited without FS or waiver.

§9 NULL HYPOTHESIS PROGRESSION [IMMUTABLE]:
  g_null(initial)=GOpen. g_null(post-domain): FAIL if G_domain_agg=FAIL; max(initial,CONDITIONAL)
  if CONDITIONAL; initial if PASS. g_null(final): FAIL if G_lifecycle=FAIL; max(post-domain,
  CONDITIONAL) if CONDITIONAL; post-domain if PASS. GClose=g_null(final) or override.

§10 SCOPE COVERAGE GATE [IMMUTABLE]: §5.5 maps §1 surfaces. GAP->ADVISORY-GAP.
§11 FINDING-SURFACE LINKAGE [IMMUTABLE]: Each finding cites "[§1:S-n]". No cite=ADVISORY-ORPHAN.
§12 CONDITIONAL REGISTRY [IMMUTABLE]: CONDITIONAL->emit RESOLUTION REGISTRY table.
§13 g_null LEDGER [IMMUTABLE]: In CROSS-ROLE SIGNALS: initial|post-domain|final|Trajectory.
§14 FINDING SEVERITY AGGREGATION [IMMUTABLE]: Per-row Severity. Section Severity=worst(all rows).
§15 LENS EXHAUSTION [IMMUTABLE]: DOMAIN/LIFECYCLE emit LENS COVERAGE TABLE. Applicability from
  §17 matrix cell (role x primary domain). OPEN+HIGH->ADVISORY-OPEN-LENS.
§16 PRIMARY DRIVER [IMMUTABLE]: GClose=FAIL->GClose. G_domain=FAIL->DOMAIN. G_lifecycle=FAIL->
  LIFECYCLE. Any CONDITIONAL->lowest-index. All PASS->N/A.

§17 DOMAIN-ROLE COVERAGE MATRIX [IMMUTABLE]:
  After INVENTORY LOCK, produce matrix. Rows=locked domains. Columns=ROLE MANIFEST roles.
  Cells: HIGH/MEDIUM/LOW/--. Row count must = INVENTORY LOCK COUNT. Mismatch halts.
  DOMAIN-GAP (no HIGH in row)->ADVISORY-GAP item in register.
  §15 applicability: matrix cell for (role, primary domain).

§17a APPLICABILITY CERTIFICATION [IMMUTABLE]:
  After COVERAGE MATRIX, before CERT VALIDITY CHECK TABLE. One entry per role.
  Format: Role [name]: Applicability=[H/M/L] / Artifact domain:[§1 label] /
  Lens.verify match:[specific entry] / Basis:[one sentence, THIS artifact specifically]
  Invalid: generic type-level justification or missing specific lens.verify entry.

§17b ARTIFACT DOMAIN INVENTORY [IMMUTABLE]:
  Step 1 SCAN: unique [DOMAIN: label] from §1.
  Step 2 DEDUPLICATE: one entry per unique label.
  Step 3 SPLIT CHECK: split labels covering multiple distinct concerns.
    State: "SPLIT: [original]->[A],[B]"
  Step 4 LOCK: numbered list. INVENTORY LOCK COUNT: N.
  Emit "INVENTORY LOCK COMPLETE -- matrix row count = N" before COVERAGE MATRIX.

§17c CERT VALIDITY CHECK [IMMUTABLE]:
  After APPLICABILITY CERTIFICATION BLOCK. One row per role.
  | Role | Domain Named (Y/N) | Lens Entry Quoted (Y/N) | Basis Artifact-Specific (Y/N) | Valid |
  Domain Named: Y if specific §1 label named. Lens Entry Quoted: Y if specific role-definition
  entry cited (not generic). Basis Artifact-Specific: Y if names specific surface of THIS artifact.
  Valid: ALL-YES if all Y. DOWNGRADE if any N -> revise cert and ROLE MANIFEST to LOW. Re-emit.
  CERT VALIDITY GATE: VALID (all ALL-YES) or INVALID (list roles). Gate must = VALID before §2.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

| Slot | Archetype | Role | Selection Rationale | Applicability |
|------|-----------|------|---------------------|---------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] | HIGH |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] | [H/M/L] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] | [H/M/L] |

---

## ARTIFACT DOMAIN INVENTORY *(Per §17b. No ledger row.)*

**Step 1-2**: Unique domains from §1: [list]
**Step 3 SPLIT CHECK**: [label]: [KEPT / SPLIT: [orig]->[A],[B] -- reason]

**Locked inventory**:
1. [domain-A]
2. [domain-B]
3. [domain-C]

**INVENTORY LOCK COUNT**: [N]
**INVENTORY LOCK COMPLETE -- matrix row count = N**

---

## DOMAIN-ROLE COVERAGE MATRIX *(Rows = locked inventory, count = N. No ledger row.)*

| Artifact Domain | [CHALLENGER] | [DOMAIN] | [LIFECYCLE] | Gap Status |
|-----------------|-------------|----------|-------------|-----------|
| [domain-A] | [H/M/L/--] | [H/M/L/--] | [H/M/L/--] | [COVERED/GAP] |
| [domain-B] | [H/M/L/--] | [H/M/L/--] | [H/M/L/--] | [COVERED/GAP] |
| [domain-C] | [H/M/L/--] | [H/M/L/--] | [H/M/L/--] | [COVERED/GAP] |

*(MATRIX CONTRACT CHECK: N rows = INVENTORY LOCK COUNT? [YES/VIOLATION])*
**ADVISORY-GAP pre-registered**: [domain if DOMAIN-GAP: "ADVISORY-GAP: [domain]..." or "None"]

---

## APPLICABILITY CERTIFICATION BLOCK *(Per §17a. No ledger row.)*

Role [challenger]: Applicability=HIGH / Artifact domain:[§1 label] / Lens.verify match:[specific entry] / Basis:[THIS artifact specifically]
Role [domain]: Applicability=[H/M/L] / Artifact domain:[§1 label] / Lens.verify match:[specific entry] / Basis:[THIS artifact specifically]
Role [lifecycle]: Applicability=[H/M/L] / Artifact domain:[§1 label] / Lens.verify match:[specific entry] / Basis:[THIS artifact specifically]

---

## CERT VALIDITY CHECK TABLE *(Per §17c. No ledger row.)*

| Role | Domain Named | Lens Entry Quoted | Basis Artifact-Specific | Valid |
|------|-------------|------------------|------------------------|-------|
| [challenger] | [Y/N] | [Y/N] | [Y/N] | [ALL-YES/DOWNGRADE] |
| [domain]     | [Y/N] | [Y/N] | [Y/N] | [ALL-YES/DOWNGRADE] |
| [lifecycle]  | [Y/N] | [Y/N] | [Y/N] | [ALL-YES/DOWNGRADE] |

*(Revise any DOWNGRADE; re-emit until all ALL-YES.)*
**CERT VALIDITY GATE**: [VALID -- all ALL-YES. Proceed to BRACKET OPENING.]

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
**Null hypothesis**: [One sentence.] | **Strength**: [H/M/L]

**Alternatives comparison table**:
| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [_] | [_] | [_] | |
| [DIM-2] | [_] | [_] | [_] | |
| [DIM-3] | [_] | [_] | [_] | |

**NULL HYPOTHESIS DERIVATION RULE**: [Formula over B-A and B-C.]

**Challenge claims**:
| CH-ID | Claim | Severity |
|-------|-------|----------|
| CH-001 | [_] | [H/M/L] |
| CH-002 | [_] | [H/M/L] |

**GOpen**: [_] | **Reason**: [One sentence.] | **g_null(initial)** *(=GOpen)*: [_]

**Local Gate Ledger Row**: | BRACKET OPENING | GOpen | [_] | [_] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1 | GOpen: [copy]

**CH-ID Response**: | CH-001 | [copy] | [_] | [A/P/O] | | CH-002 | [copy] | [_] | [A/P/O] |

**Additional Findings**: | F-1 | [§1:S-n] | [_] | [H/M/L] | | F-2 | [§1:S-n] | [_] | [H/M/L] |
**Section Severity** *(worst)*: [H/M/L]

**LENS COVERAGE TABLE**: | 1 | [entry 1] | [matrix cell] | [A/O] | [F-n] | | 2 | [entry 2] | [matrix cell] | [A/O] | [F-n] |

**G_domain**: [_] | **Reason**: [One sentence.]
**Local Gate Ledger Row**: | DOMAIN -- [ROLE_NAME] | G_domain | [_] | [_] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT *(EXCLUDED)*
```
G_domain_agg=worst([verdicts])=[_] | g_null(post-domain) via §9:[_]
```

## §3.8 CH-ID SATURATION CHECK *(EXCLUDED)*
| CH-001 | [status] | [SAT/UNSAT] | | CH-002 | [status] | [SAT/UNSAT] |

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1 | GOpen:[copy] | G_domain_agg:[copy] | g_null(post-domain):[copy]

**CH-ID Response**: | CH-001 | [copy] | [_] | [A/P/O] | | CH-002 | [copy] | [_] | [A/P/O] |
**Additional Findings**: | F-1 | [§1:S-n] | [_] | [H/M/L] | | F-2 | [§1:S-n] | [_] | [H/M/L] |
**Section Severity** *(worst)*: [H/M/L]
**LENS COVERAGE TABLE**: | 1 | [entry 1] | [matrix cell] | [A/O] | [F-n] | | 2 | [entry 2] | [matrix cell] | [A/O] | [F-n] |

**G_lifecycle**: [_] | **Reason**: [One sentence.]
**Local Gate Ledger Row**: | LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [_] | [_] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
```
g_null(post-domain)=[copy] | G_lifecycle=[copy] | §9 Stage 3 --> g_null(final)=[_]
```
**Full CH-ID Saturation**: | CH-001 | [copy] | [copy] | [FS/UNSAT] | | CH-002 | [copy] | [copy] | [FS/UNSAT] |
**GClose**: [_] *(=g_null(final). Override: "g_null OVERRIDE:[reason]")* | **Rationale**: [2-3 sentences.]
**Local Gate Ledger Row**: | BRACKET CLOSING | GClose | [_] | [_] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION *(EXCLUDED)*
| [§1:S-1] | [ROLE] | [F-n] | [COVERED/GAP] | | [§1:S-2] | [ROLE] | [F-n] | [COVERED/GAP] |
**Coverage gate**: [COVERED/PARTIAL] | **Advisory**: [list or "None"]

## GATE VECTOR TABLE
| GOpen | [CHALLENGER] | [_] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN(S)] | [_] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [_] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [_] | DISPOSITION_CONTRACT v1 |

## CROSS-ROLE SIGNALS
**Conflicts**: [or "None"] | **Convergence**: [signal]
**§13**: `g_null(initial)=[_] | g_null(post-domain)=[_] | g_null(final)=[_] | Trajectory:[label]`

## DISPOSITION
**Gate vector**: GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]
**§3**: GClose=FAIL?->BLOCKED | Any FAIL?->BLOCKED | Any COND?->CONDITIONAL | All PASS?->READY
**Disposition**: [_] | **Primary Driver** *(§16)*: [_] | **RESOLUTION REGISTRY**: [table or "N/A"]

## ACTION ITEM REGISTER *(verbatim copy)*
| BRACKET OPENING | GOpen | [copy] | [copy] |
| DOMAIN -- [ROLE] | G_domain | [copy] | [copy] |
| LIFECYCLE -- [ROLE] | G_lifecycle | [copy] | [copy] |
| BRACKET CLOSING | GClose | [copy] | [copy] |
**Advisory**: [ADVISORY-GAP, ADVISORY-ORPHAN, ADVISORY-OPEN-LENS, or "None"]

---

**Artifact to review:**

{{artifact}}

---
---

## V-05

**Axes**: Lifecycle emphasis + Output format + Inertia framing -- CERT VALIDITY GATE + DOMAIN INVENTORY LOCK + VERDICT THRESHOLD TABLE (C-33 + C-34 + C-35 simultaneously)
**Hypothesis**: V-01 closes C-33 (CERT VALIDITY CHECK TABLE with blocking gate). V-02 closes C-34
(ARTIFACT DOMAIN INVENTORY LOCK anchoring matrix rows to a split-checked domain set). V-03 closes
C-35 (VERDICT THRESHOLD TABLE with integer D-threshold making g_null(initial) derivable from
count values alone). V-05 integrates all three in canonical order:
  0.5 CHALLENGER PRE-ASSESSMENT (D-threshold -> g_null(initial))
  1   ROLE MANIFEST
  1.3 ARTIFACT DOMAIN INVENTORY (lock step)
  1.5 DOMAIN-ROLE COVERAGE MATRIX (N rows = lock count)
  1.7 APPLICABILITY CERTIFICATION BLOCK
  1.8 CERT VALIDITY CHECK TABLE (exit gate)
  2   BRACKET OPENING (inherits g_null(initial), CERT VALIDITY GATE=VALID confirmed)
Each pre-review section produces a machine-verifiable artifact. C-33: Valid column in CERT
VALIDITY CHECK TABLE. C-34: matrix row count vs INVENTORY LOCK COUNT. C-35: D value in VERDICT
COUNT SUMMARY vs threshold table. No prose reading required for any criterion. 225/225 candidate.

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
pre-printed heading, label, field, formula, or structural element. If a field cannot be
filled, write `[N/A -- reason]`.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§17d;
reviewer sections may not execute until ALL pre-review gates cleared:
§1 COMPLETE, CHALLENGER PRE-ASSESSMENT COMPLETE, INVENTORY LOCK
COMPLETE, COVERAGE MATRIX COMPLETE, CERT VALIDITY GATE = VALID]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]
  (Add rows. Specific domain labels -- one distinct concern per label.
  Broad labels conflating multiple concerns will be split in §17b.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

Scope Amendment: SCOPE AMENDMENT: [surface] -- [reason]
§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks commitment. MEDIUM=Conditions commitment. LOW=Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR exists Gi=FAIL
  CONDITIONAL <-- no FAIL AND exists CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg=worst(all G_domain verdicts). FAIL>CONDITIONAL>PASS.

§4 -- CONTRACT CITE [IMMUTABLE]: "Contract: DISPOSITION_CONTRACT v1" opens each reviewer section.

§5 -- CH-ID TRACING [IMMUTABLE]: Claims get CH-IDs. All downstream carry CH-ID tables.
  PASS prohibited if any CH-ID=OPEN.

§6 -- LOCAL GATE LEDGER [IMMUTABLE]
  Row: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section. Assembly: verbatim copy, no re-derivation.
  EXCLUDED (no ledger row):
    §3.5 DOMAIN-AGGREGATE CHECKPOINT
    §3.8 CH-ID SATURATION CHECK
    §5.5 SCOPE COVERAGE RECONCILIATION
    CHALLENGER PRE-ASSESSMENT
    ARTIFACT DOMAIN INVENTORY
    DOMAIN-ROLE COVERAGE MATRIX
    APPLICABILITY CERTIFICATION BLOCK
    CERT VALIDITY CHECK TABLE

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  0.5. CHALLENGER PRE-ASSESSMENT          [§17d; before ROLE MANIFEST; no ledger row]
  1.   ROLE MANIFEST
  1.3. ARTIFACT DOMAIN INVENTORY          [§17b; locked list; no ledger row]
  1.5. DOMAIN-ROLE COVERAGE MATRIX        [§17; pre-reviewer; no ledger row]
  1.7. APPLICABILITY CERTIFICATION BLOCK  [§17a; no ledger row]
  1.8. CERT VALIDITY CHECK TABLE          [§17c; exit gate; no ledger row]
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
  PRE-ASSESSMENT must precede ROLE MANIFEST.
  CERT VALIDITY GATE must = VALID before BRACKET OPENING.
  LIFECYCLE must precede BRACKET CLOSING.

§8 -- CH-ID SATURATION [IMMUTABLE]
  SATURATED: CH-ID in >= 1 DOMAIN section (before LIFECYCLE).
  FULLY SATURATED: CH-ID in DOMAIN + LIFECYCLE (before BRACKET CLOSING).
  PASS prohibited without FS or stated waiver. Waiver: "CH-XXX WAIVER: [reason]"

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1 -- g_null(initial) [derived at CHALLENGER PRE-ASSESSMENT]:
    Step A: VERDICT COUNT SUMMARY:
      F = count of FAVORS-BUILD verdicts in NH DIMENSION TABLE
      O = count of OPPOSES-BUILD verdicts
      N = count of NEUTRAL verdicts
      D = F - O  (signed integer)
    Step B: VERDICT THRESHOLD TABLE [do not alter]:
      D >= 2:  g_null(initial) = PASS         [build clearly favored]
      D = 1:   g_null(initial) = CONDITIONAL  [build modestly favored]
      D = 0:   g_null(initial) = CONDITIONAL  [tie]
      D = -1:  g_null(initial) = FAIL         [status quo favored]
      D <= -2: g_null(initial) = FAIL         [status quo clearly preferred]
    Step C: Emit "g_null(initial)=[PASS/CONDITIONAL/FAIL] via D=[value]"
    GOpen inherits g_null(initial) from PRE-ASSESSMENT. Do not re-derive.
  Stage 2 -- g_null(post-domain) [emitted at §3.5]:
    G_domain_agg=FAIL: g_null(post-domain)=FAIL
    G_domain_agg=CONDITIONAL: g_null(post-domain)=max(g_null(initial),CONDITIONAL)
    G_domain_agg=PASS: g_null(post-domain)=g_null(initial)
  Stage 3 -- g_null(final) [emitted at BRACKET CLOSING]:
    G_lifecycle=FAIL: g_null(final)=FAIL
    G_lifecycle=CONDITIONAL: g_null(final)=max(g_null(post-domain),CONDITIONAL)
    G_lifecycle=PASS: g_null(final)=g_null(post-domain)
  GClose must equal g_null(final) or declare override with justification.

§10 -- SCOPE COVERAGE GATE [IMMUTABLE]: §5.5 maps §1 surfaces. GAP->ADVISORY-GAP.
§11 -- FINDING-SURFACE LINKAGE [IMMUTABLE]: "[§1:S-n]" on each finding. No cite=ADVISORY-ORPHAN.
§12 -- CONDITIONAL REGISTRY [IMMUTABLE]: CONDITIONAL->RESOLUTION REGISTRY table.
§13 -- g_null LEDGER [IMMUTABLE]: CROSS-ROLE SIGNALS: initial|post-domain|final|Trajectory.
§14 -- FINDING SEVERITY AGGREGATION [IMMUTABLE]: Per-row Severity. Section=worst(all rows).
§15 -- LENS EXHAUSTION [IMMUTABLE]: DOMAIN/LIFECYCLE emit LENS COVERAGE TABLE after findings.
  Applicability=§17 matrix cell (role x primary domain). OPEN+HIGH->ADVISORY-OPEN-LENS.
§16 -- PRIMARY DRIVER [IMMUTABLE]: GClose=FAIL->GClose. G_domain=FAIL->DOMAIN.
  G_lifecycle=FAIL->LIFECYCLE. Any CONDITIONAL->lowest-index. All PASS->N/A.

§17 -- DOMAIN-ROLE COVERAGE MATRIX CONTRACT [IMMUTABLE]
  After INVENTORY LOCK COMPLETE, produce DOMAIN-ROLE COVERAGE MATRIX.
  Rows: locked domains from ARTIFACT DOMAIN INVENTORY.
  Columns: roles from ROLE MANIFEST. Cells: HIGH/MEDIUM/LOW/--.
  Row count must = INVENTORY LOCK COUNT. Mismatch halts: "MATRIX CONTRACT VIOLATION."
  DOMAIN-GAP (no HIGH in row)->ADVISORY-GAP: "ADVISORY-GAP:[domain]--no HIGH reviewer."
  §15 applicability: matrix cell for (role, primary artifact domain).

§17a -- APPLICABILITY CERTIFICATION [IMMUTABLE]
  After COVERAGE MATRIX, before CERT VALIDITY CHECK TABLE. One entry per role.
  Format: Role [name]: Applicability=[H/M/L]
          Artifact domain:[specific §1 label]
          Lens.verify match:[specific entry from role definition]
          Basis:[one sentence -- THIS artifact, specific surface/field/behavior, not type]
  Invalid: generic type-level justification. Invalid: no specific lens.verify entry.

§17b -- ARTIFACT DOMAIN INVENTORY [IMMUTABLE]
  Step 1 SCAN: unique [DOMAIN:label] from §1. Step 2 DEDUPLICATE.
  Step 3 SPLIT CHECK: split labels covering multiple concerns that could independently lack
    HIGH coverage. State: "SPLIT:[original]->[A],[B]--[reason]"
  Step 4 LOCK: numbered list. INVENTORY LOCK COUNT:N.
  "INVENTORY LOCK COMPLETE--matrix row count=N" before COVERAGE MATRIX.

§17c -- CERT VALIDITY CHECK [IMMUTABLE]
  After APPLICABILITY CERTIFICATION BLOCK. One row per role.
  | Role | Domain Named (Y/N) | Lens Entry Quoted (Y/N) | Basis Artifact-Specific (Y/N) | Valid |
  Domain Named: Y=specific §1 label. Lens Entry Quoted: Y=specific role-definition entry.
  Basis Artifact-Specific: Y=names specific surface/field/behavior of THIS artifact.
  Valid: ALL-YES if all Y. DOWNGRADE if any N.
  DOWNGRADE->revise cert and ROLE MANIFEST Applicability to LOW. Re-emit. Repeat until all ALL-YES.
  CERT VALIDITY GATE: VALID (all ALL-YES) blocks BRACKET OPENING until reached.

§17d -- CHALLENGER PRE-ASSESSMENT [IMMUTABLE]
  Runs before ROLE MANIFEST. Not a reviewer section. No contract cite, no CH-IDs, no ledger row.
  NH DIMENSION TABLE:
    | Dimension | What Challenger Assesses | Status Quo (A) | Build (B) | Verdict |
  Verdict: FAVORS-BUILD/NEUTRAL/OPPOSES-BUILD.
    FAVORS-BUILD=Build meaningfully better. NEUTRAL=Comparable. OPPOSES-BUILD=SQ comparable or better.
  Minimum 3 dimensions. Each row = one null hypothesis axis.
  After table: emit VERDICT COUNT SUMMARY and apply §9 Stage 1 VERDICT THRESHOLD TABLE.
  Emit "CHALLENGER PRE-ASSESSMENT COMPLETE" before ROLE MANIFEST.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## CHALLENGER PRE-ASSESSMENT

*(Per §17d -- before ROLE MANIFEST. No contract cite, no CH-IDs, no ledger row.)*

**NH DIMENSION TABLE** *(minimum 3 dimensions -- each row = one null hypothesis axis)*:

| Dimension | What Challenger Assesses | Status Quo (A) | Build (B) | Verdict |
|-----------|--------------------------|---------------|-----------|---------|
| [DIM-1]   | [one sentence]           | [assessment]  | [assessment] | [FAVORS-BUILD/NEUTRAL/OPPOSES-BUILD] |
| [DIM-2]   | [one sentence]           | [assessment]  | [assessment] | [FAVORS-BUILD/NEUTRAL/OPPOSES-BUILD] |
| [DIM-3]   | [one sentence]           | [assessment]  | [assessment] | [FAVORS-BUILD/NEUTRAL/OPPOSES-BUILD] |
| [DIM-4]   | [optional]               | [assessment]  | [assessment] | [FAVORS-BUILD/NEUTRAL/OPPOSES-BUILD] |

**VERDICT COUNT SUMMARY** *(§9 Stage 1 Step A)*:
```
F (FAVORS-BUILD)  = [count]
O (OPPOSES-BUILD) = [count]
N (NEUTRAL)       = [count]
D = F - O         = [signed integer]
```

**Apply VERDICT THRESHOLD TABLE** *(§9 Stage 1 Step B -- thresholds immutable)*:
```
D >= 2  --> PASS         D = 1  --> CONDITIONAL
D = 0   --> CONDITIONAL  D = -1 --> FAIL
D <= -2 --> FAIL

D = [value] --> g_null(initial) = [PASS/CONDITIONAL/FAIL]
```

**g_null(initial)**: [PASS/CONDITIONAL/FAIL] *(derived from D -- not prose; BRACKET OPENING inherits)*

**CHALLENGER PRE-ASSESSMENT COMPLETE**

---

## ROLE MANIFEST

| Slot | Archetype | Role | Selection Rationale | Applicability |
|------|-----------|------|---------------------|---------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] | HIGH |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] | [H/M/L] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] | [H/M/L] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3 rows.)*

---

## ARTIFACT DOMAIN INVENTORY *(Per §17b. No ledger row.)*

**Step 1-2 SCAN+DEDUPLICATE**: Unique [DOMAIN:label] values from §1: [list]

**Step 3 SPLIT CHECK**:
- [label-1]: [KEPT -- single concern / SPLIT:[orig]->[A],[B]--reason]
- [label-2]: [KEPT / SPLIT]

**Locked inventory**:
1. [domain-A]
2. [domain-B]
3. [domain-C]

**INVENTORY LOCK COUNT**: [N]
**INVENTORY LOCK COMPLETE -- matrix row count = N**

---

## DOMAIN-ROLE COVERAGE MATRIX *(Per §17 -- rows=locked inventory, count=N. No ledger row.)*

| Artifact Domain | [CHALLENGER] | [DOMAIN] | [LIFECYCLE] | Gap Status |
|-----------------|-------------|----------|-------------|-----------|
| [domain-A] | [H/M/L/--] | [H/M/L/--] | [H/M/L/--] | [DOMAIN-COVERED/DOMAIN-GAP] |
| [domain-B] | [H/M/L/--] | [H/M/L/--] | [H/M/L/--] | [DOMAIN-COVERED/DOMAIN-GAP] |
| [domain-C] | [H/M/L/--] | [H/M/L/--] | [H/M/L/--] | [DOMAIN-COVERED/DOMAIN-GAP] |

*(MATRIX CONTRACT CHECK: [N] rows = INVENTORY LOCK COUNT [N]? [YES/VIOLATION])*

**ADVISORY-GAP pre-registered**:
- [domain if DOMAIN-GAP]: "ADVISORY-GAP:[domain]--no HIGH-applicability reviewer."
- (or "None -- all COVERED")

---

## APPLICABILITY CERTIFICATION BLOCK *(Per §17a. No ledger row.)*

Role [challenger]: Applicability=HIGH
Artifact domain: [specific §1 domain label]
Lens.verify match: [specific entry from role definition]
Basis: [one sentence -- THIS artifact, specific surface/behavior, not type]

Role [domain]: Applicability=[H/M/L]
Artifact domain: [specific §1 domain label]
Lens.verify match: [specific entry from role definition]
Basis: [one sentence -- THIS artifact specifically]

Role [lifecycle]: Applicability=[H/M/L]
Artifact domain: [specific §1 domain label]
Lens.verify match: [specific entry from role definition]
Basis: [one sentence -- THIS artifact specifically]

---

## CERT VALIDITY CHECK TABLE *(Per §17c. No ledger row.)*

| Role | Domain Named (Y/N) | Lens Entry Quoted (Y/N) | Basis Artifact-Specific (Y/N) | Valid |
|------|--------------------|------------------------|-------------------------------|-------|
| [challenger] | [Y/N] | [Y/N] | [Y/N] | [ALL-YES/DOWNGRADE] |
| [domain]     | [Y/N] | [Y/N] | [Y/N] | [ALL-YES/DOWNGRADE] |
| [lifecycle]  | [Y/N] | [Y/N] | [Y/N] | [ALL-YES/DOWNGRADE] |

*(For any DOWNGRADE: revise cert and ROLE MANIFEST Applicability to LOW. Re-emit until all ALL-YES.)*

**CERT VALIDITY GATE**: [VALID -- all ALL-YES. Proceed to BRACKET OPENING.]

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*(g_null(initial) inherited from PRE-ASSESSMENT -- do not re-derive. GOpen = g_null(initial).)*

**Null hypothesis**: [What the team does today -- one sentence.]
**Null hypothesis strength**: [H/M/L]

**Challenge claims** *(CH-IDs per §5 -- grounded in NEUTRAL/OPPOSES-BUILD dimensions from PRE-ASSESSMENT)*:

| CH-ID  | Challenge Claim | Severity |
|--------|----------------|----------|
| CH-001 | [CLAIM grounded in a PRE-ASSESSMENT dimension where SQ was comparable or better] | [H/M/L] |
| CH-002 | [CLAIM_2] | [H/M/L] |
| CH-003 | [optional] | [H/M/L] |

**GOpen Verdict**: [PASS/CONDITIONAL/FAIL] *(must = g_null(initial) from PRE-ASSESSMENT)*
**GOpen Reason**: [One sentence referencing D=[value] and dominant dimension.]
**g_null(initial)** *(inherited from PRE-ASSESSMENT)*: [copy]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [_] | [_] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table** *(mandatory per §5)*:
| CH-ID  | Challenge Claim (copy) | Domain Response | Status |
|--------|----------------------|-----------------|--------|
| CH-001 | [copy] | [_] | [A/P/O] |
| CH-002 | [copy] | [_] | [A/P/O] |
| CH-003 | [copy if active] | [_] | [A/P/O] |

**Additional Findings** *(per §14, §11)*:
| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING] | [H/M/L] |
| F-2 | [§1:S-n] | [FINDING] | [H/M/L] |
| F-3 | [§1:S-n -- optional] | [FINDING] | [H/M/L] |

**Finding Severity Aggregation** *(per §14)*: `worst(F-1=[_],F-2=[_],...) = [SECTION_SEVERITY]`
**Section Severity**: [H/M/L]

**LENS COVERAGE TABLE** *(per §15 -- Applicability = §17 matrix cell for this role x primary domain)*:
| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|-------------------|
| 1 | [entry 1] | [matrix cell] | [A/O] | [F-n] |
| 2 | [entry 2] | [matrix cell] | [A/O] | [F-n] |
*(OPEN on HIGH-applicability rows -> ADVISORY-OPEN-LENS per §15.)*

**G_domain Verdict**: [PASS/CONDITIONAL/FAIL] | **Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [_] | [_] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT *(EXCLUDED from ledger)*

```
G_domain_agg = worst([list verdicts]) = [PASS/CONDITIONAL/FAIL]
g_null(post-domain) via §9 Stage 2:
  G_domain_agg=[_], g_null(initial)=[_] --> g_null(post-domain)=[PASS/CONDITIONAL/FAIL]
```

---

## §3.8 CH-ID SATURATION CHECK *(EXCLUDED from ledger)*

| CH-ID | DOMAIN Status | Pre-LIFECYCLE Saturation |
|-------|--------------|--------------------------|
| CH-001 | [A/P/O] | [SAT/UNSAT] |
| CH-002 | [A/P/O] | [SAT/UNSAT] |
| CH-003 | [if active] | [SAT/UNSAT] |

**Unsaturated**: [list or "None"]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy] | G_domain_agg: [copy from §3.5] | g_null(post-domain): [copy from §3.5]

**CH-ID Response Table**:
| CH-ID  | Claim (copy) | Lifecycle Response | Status |
|--------|-------------|-------------------|--------|
| CH-001 | [copy] | [_] | [A/P/O] |
| CH-002 | [copy] | [_] | [A/P/O] |
| CH-003 | [if active] | [_] | [A/P/O] |

**Additional Findings** *(per §14, §11)*:
| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING] | [H/M/L] |
| F-2 | [§1:S-n] | [FINDING] | [H/M/L] |

**Finding Severity Aggregation**: `worst(F-1=[_],F-2=[_]) = [SECTION_SEVERITY]`
**Section Severity**: [H/M/L]

**LENS COVERAGE TABLE** *(Applicability = §17 matrix cell)*:
| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|-------------------|
| 1 | [entry 1] | [matrix cell] | [A/O] | [F-n] |
| 2 | [entry 2] | [matrix cell] | [A/O] | [F-n] |

**G_lifecycle Verdict**: [PASS/CONDITIONAL/FAIL] | **Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [_] | [_] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: PRE-ASSESSMENT D=[value], CERT VALIDITY GATE=VALID, all verdicts.*

```
g_null(post-domain) = [copy from §3.5]
G_lifecycle         = [copy from LIFECYCLE local ledger]
Apply §9 Stage 3 --> g_null(final) = [PASS/CONDITIONAL/FAIL]
```

**Full CH-ID Saturation Check** *(per §8)*:
| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation |
|-------|--------------|-----------------|----------------|
| CH-001 | [copy] | [copy] | [FS/UNSAT] |
| CH-002 | [copy] | [copy] | [FS/UNSAT] |
| CH-003 | [if active] | [copy] | [FS/UNSAT] |
*(PASS prohibited if any UNSATURATED without waiver.)*

**GClose Verdict**: [PASS/CONDITIONAL/FAIL]
*(Must = g_null(final) per §9. Override: "g_null OVERRIDE: [explicit justification]")*
**GClose Rationale**: [2-3 sentences referencing g_null(initial) D=[value] from PRE-ASSESSMENT,
trajectory, and whether PRE-ASSESSMENT NEUTRAL/OPPOSES-BUILD dimensions were addressed.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [_] | [_] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION *(EXCLUDED from ledger)*

| IN-SCOPE Surface | Reviewer(s) | Finding(s) | Coverage |
|-----------------|-------------|-----------|---------|
| [§1:S-1] | [ROLE or "none"] | [F-n or "none"] | [COVERED/GAP] |
| [§1:S-2] | [ROLE or "none"] | [F-n or "none"] | [COVERED/GAP] |
| [§1:S-3] | [ROLE or "none"] | [F-n or "none"] | [COVERED/GAP] |

**Coverage gate signal** *(informational)*: [COVERED/PARTIAL]
**Advisory items for ACTION ITEM REGISTER**: [ADVISORY-GAP/ADVISORY-ORPHAN/ADVISORY-OPEN-LENS or "None"]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|--------------|
| GOpen | [CHALLENGER_ROLE] | [_] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN_ROLE(S)] | [_] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE_ROLE] | [_] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER_ROLE] | [_] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Incompatible responses between reviewers. If none: "None detected."]
**Convergence**: [CH-ID or concern named independently by two or more reviewers.]

**§13 Progression Ledger**:
```
g_null(initial)     = [copy from PRE-ASSESSMENT]    [D=[value] via threshold]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING]
Trajectory:         [MONOTONIC-PASS/MONOTONIC-FAIL/DOMAIN-DEGRADED/
                     LIFECYCLE-DEGRADED/DOMAIN-RECOVERED/LIFECYCLE-RECOVERED]
```

---

## DISPOSITION

**Gate vector**: GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]

**Apply §3**:
```
GClose=FAIL? --> BLOCKED
Any other Gi=FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [BLOCKED/CONDITIONAL/READY]
**Primary Driver** *(per §16 -- mechanically derived)*: [gate or N/A]
**RESOLUTION REGISTRY** *(per §12)*:
| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [what must resolve] | [role] | [specific criterion] | OPEN |
*(or "N/A -- [disposition]" if not CONDITIONAL)*

---

## ACTION ITEM REGISTER

*(Copies local gate ledger rows verbatim per §6. Do not re-derive Gate Verdict or Class.)*

| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [copy] | [copy] |
| DOMAIN -- [ROLE] | G_domain | [copy] | [copy] |
| LIFECYCLE -- [ROLE] | G_lifecycle | [copy] | [copy] |
| BRACKET CLOSING | GClose | [copy] | [copy] |

**Advisory items** *(ADVISORY-GAP from §17 matrix, ADVISORY-ORPHAN, ADVISORY-OPEN-LENS from §15, from §5.5)*:
- [item or "None"]

---

**Artifact to review:**

{{artifact}}
