---
skill: quest-variate
skill_target: org-review
date: 2026-03-17
round: 17
rubric: org-review-rubric-v11-2026-03-16.md
variants: V-01 V-02 V-03 V-04 V-05
---

# org-review -- Variate R17 (2026-03-17)

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis and three-axis combinations (V-04, V-05).

**Base**: V-05 R16 (225/225 under v11 -- all C-01 through C-35 passing). R16 explored
post-225 candidate criteria: §0 NULL HYPOTHESIS CHARTER (C-41 candidate), global F-ID
namespace (C-42 candidate), LIFECYCLE NH Dimension Score sub-table (C-41 candidate via
separate path), and their combinations.

**Gap analysis from R16:**

| Criterion | R16 V-04 | R16 V-05 | What it requires |
|-----------|----------|----------|-----------------|
| C-41 LIFECYCLE NH SCORE EMISSION | PASS | PASS | LIFECYCLE section emits NH Dimension Scores sub-table; bracket-closing NH aggregation formula includes lifecycle B/C column values |
| C-42 F-ID NAMED FIELD | PASS | FAIL | Finding column named `F-ID` (not positional `#`); all downstream references use F-ID values, not row positions |
| C-43 CH-ID §0 GROUNDING COLUMN | FAIL | PASS | CH-ID table includes a `§0 Grounding` column citing the specific preamble contract that authorizes each challenge; populated at challenge registration time |

**R17 synthesis path**: V-04 R16 achieved C-41+C-42 but missed C-43 (CH-ID table carries
§0:Arg-n citations in the claim cell but no structural §0 Grounding column at registration).
V-05 R16 achieved C-41+C-43 but missed C-42 (finding table used positional `#` column --
F-ID label only appeared in downstream references, not as a named table column). R17 must
integrate all three simultaneously through different structural pathways.

**R17 variation axes:**

- V-01: Lifecycle emphasis (single axis) -- §18 LIFECYCLE NH SCORE EMISSION elevated to a
  top-level numbered immutable contract at the same structural level as §17. §14 finding schema
  block names `F-ID` as a required column identifier (C-42). §5 CH-ID TRACING REQUIREMENT
  declares the `§0 Grounding` column at challenge registration time (C-43). All three new
  criteria enforced via separate numbered contracts, none as a clause extension.

- V-02: Output format (single axis) -- TABLE FORMAT CONTRACT block declared before all
  numbered §§ contracts. The block pre-declares all table schemas used in the review:
  finding table (with F-ID as a named column), CH-ID challenge table (with §0 Grounding
  as a required column), NH Dimension Table, NH Dimension Scores sub-table (for lifecycle),
  and gate ledger row. C-42 and C-43 are schema-layer declarations; §18 lifecycle clause
  references the pre-declared NH sub-table schema.

- V-03: Inertia framing (single axis) -- preamble opens with STATUS QUO FRAMING CONTRACT
  that registers named §0-CID commitment artifacts before any §§ contracts execute. CH-ID
  §0 Grounding column cites §0-CID values rather than generic §§ contract refs. F-ID column
  motivated and enforced by the inertia-advocate's auditability requirement in the framing
  contract. §18 LIFECYCLE NH SCORE EMISSION present as in V-01.

- V-04: Lifecycle + Output format (two-axis) -- V-01's §18 top-level lifecycle elevation
  combined with V-02's TABLE FORMAT CONTRACT block. C-42 has dual enforcement (TABLE FORMAT
  CONTRACT schema + §14 finding schema). C-43 has dual enforcement (TABLE FORMAT CONTRACT
  CH-ID schema + §5 §0 Grounding clause). C-41 from §18 explicit contract.

- V-05: Lifecycle + Output format + Inertia framing (three-axis) -- all three single-axis
  patterns combined. STATUS QUO FRAMING CONTRACT §0-CID values provide richer grounding in
  the §0 Grounding column (C-43). TABLE FORMAT CONTRACT declares all schemas (C-42 named
  column, C-43 schema-declared §0 Grounding). §18 lifecycle emission. Triple enforcement
  paths for C-42 and C-43; cross-criterion traceability chain (§0-CID -> CH-ID -> F-ID ->
  disposition).

**R17 single-axis predictions:**
- V-01: C-41 PASS (§18 top-level), C-42 PASS (F-ID named column in §14), C-43 PASS
  (§0 Grounding column in §5 registration table). Predicted: 225/225 base + C-41+C-42+C-43
- V-02: C-41 PASS (§18 clause + TABLE FORMAT CONTRACT NH sub-table schema), C-42 PASS
  (TABLE FORMAT CONTRACT finding schema with F-ID), C-43 PASS (TABLE FORMAT CONTRACT CH-ID
  schema with §0 Grounding). Predicted: 225/225 base + C-41+C-42+C-43
- V-03: C-41 PASS (§18), C-42 PASS (framing contract auditability requirement), C-43 PASS
  (§0-CID values in §0 Grounding column). Predicted: 225/225 base + C-41+C-42+C-43

**R17 multi-axis predictions:**
- V-04: 225/225 + C-41+C-42+C-43 via dual enforcement (lifecycle block + table schema)
- V-05: 225/225 + C-41+C-42+C-43 with strongest inter-criterion referential chain

---

## V-01

**Axis**: Lifecycle emphasis -- §18 LIFECYCLE NH SCORE EMISSION as top-level numbered
contract; F-ID named column in §14 finding schema; §0 Grounding column in §5 CH-ID
challenge registration table.

**Hypothesis**: R16 V-04 missed C-43 because CH-ID challenge claims carried `§0:Arg-n`
citations inline in the claim cell but no dedicated structural `§0 Grounding` column was
declared at CH-ID registration time. The fix is a one-line addition to the §5 CH-ID
registration table schema: add `| §0 Grounding |` as a required column populated at
registration. V-05 R16 missed C-42 because the finding table used positional `#` as its
identifier column. Fix: §14 explicitly names the column `F-ID` in the table schema
declaration. C-41 (lifecycle NH emission) is elevated to a standalone §18 [IMMUTABLE]
contract at the same level as §17, removing any possibility of it being treated as an
optional clause extension. All three new mechanisms are additive to the V-05 R16 base;
no existing contract is modified. Predicted: 225/225 + C-41+C-42+C-43.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this block first, then execute the review protocol below.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided above.

You will play four roles in sequence: an inertia-advocate challenger who opens the review
by defending the status quo, a domain-expert reviewer who evaluates the artifact's technical
surface, a lifecycle/program reviewer who assesses commitment readiness, and the challenger
again at closing who integrates all testimony to reach a final verdict on the null hypothesis.

The challenger's default is that the artifact should NOT be built. Domain and lifecycle
testimony is the evidence that can overcome that prior.

Fill every `[BRACKETED_FIELD]` from artifact content. Write `[N/A -- reason]` when a field
is not applicable. Do not alter, reorder, or omit any pre-printed heading, label, formula,
or structural element in the contract below.

---

```
======================================================================
DISPOSITION_CONTRACT v1 [IMMUTABLE BLOCK -- read all sections before
executing any reviewer section]
======================================================================

§1 -- SCOPE ENUMERATION
  IN-SCOPE (cited in §5.5 and §11 FINDING-SURFACE LINKAGE):
    Each surface must carry a [DOMAIN: label] annotation (consumed by §10a).
    1. [SURFACE_1] [DOMAIN: label]
    2. [SURFACE_2] [DOMAIN: label]
    3. [SURFACE_3] [DOMAIN: label]
    (Add rows; be exhaustive.)
  OUT-OF-SCOPE:
    1. [SURFACE -- REASON_EXCLUDED]
  Scope Amendment Protocol:
    SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
    Silent scope expansion violates this contract.
§1 COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment.
  MEDIUM = Conditions commitment. Proceeds only after named resolution.
  LOW    = Advisory. Commitment may proceed.
  These definitions apply universally.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL  <-- no Gi=FAIL AND any Gi=CONDITIONAL
  READY        <-- all Gi=PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts). FAIL > CONDITIONAL > PASS.
  Single domain: G_domain_agg = G_domain (direct pass-through).

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A missing cite is an audit-trail gap.

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, ...).
  CH-ID registration table schema:
    | CH-ID | Challenge Claim | Severity | §0 Grounding |
  §0 Grounding column: name the specific preamble contract section (§1 through §18)
    whose pre-committed rule authorizes or motivates this challenge.
    Populated at registration time. A CH-ID without a §0 Grounding is structurally
    incomplete; write "[GROUNDING-ABSENT]" and add to ACTION ITEM REGISTER as ADVISORY.
  Every downstream reviewer section carries a mandatory CH-ID response table.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emit at end of each verdict-emitting section, after verdict is stated.
  Assembly rule: copy all local rows to ACTION ITEM REGISTER verbatim.
    Do NOT re-derive Verdict or Class. Register is a copy, not a synthesis.
  EXCLUDED sections (emit NO local ledger row):
    §3.5 Domain-Aggregate Checkpoint -- no verdict
    §3.8 CH-ID Saturation Check -- no verdict
    §5.5 Scope Coverage Reconciliation -- informational only
    §5.7 Lens Coverage Table -- informational only
    §5.8 Domain Coverage Gap-Check -- no verdict

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical execution sequence:
  1. ROLE MANIFEST (APPLICABILITY MATRIX required before BRACKET OPENING)
  2. BRACKET OPENING
  3. DOMAIN(s)
  3.5. DOMAIN-AGGREGATE CHECKPOINT
  3.8. CH-ID SATURATION CHECK
  4. LIFECYCLE
  5. BRACKET CLOSING
  5.5. SCOPE COVERAGE RECONCILIATION (surface table + §10a DOMAIN COVERAGE GAP-CHECK)
  6. GATE VECTOR TABLE
  7. CROSS-ROLE SIGNALS
  8. DISPOSITION
  9. ACTION ITEM REGISTER
  Reordering any section violates this contract.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  FULLY SATURATED: every CH-ID has received DOMAIN + LIFECYCLE responses before
    BRACKET CLOSING.
  PASS from BRACKET CLOSING is prohibited without full saturation or a stated waiver.
  Waiver: "CH-XXX WAIVER: [reason]" -> ACTION ITEM REGISTER as ADVISORY.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = §17 formula output at BRACKET OPENING
           (if §17 inactive: g_null(initial) = GOpen verdict directly)
  Stage 2: g_null(post-domain) [emitted at §3.5]:
    G_domain_agg=FAIL        -> g_null(post-domain)=FAIL
    G_domain_agg=CONDITIONAL -> g_null(post-domain)=max(g_null(initial),CONDITIONAL)
    G_domain_agg=PASS        -> g_null(post-domain)=g_null(initial)
  Stage 3: g_null(final) [emitted at BRACKET CLOSING]:
    G_lifecycle=FAIL         -> g_null(final)=FAIL
    G_lifecycle=CONDITIONAL  -> g_null(final)=max(g_null(post-domain),CONDITIONAL)
    G_lifecycle=PASS         -> g_null(final)=g_null(post-domain)
  GClose must equal g_null(final). Override: "g_null OVERRIDE: [justification]"
  Scale: FAIL < CONDITIONAL < PASS.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  After BRACKET CLOSING, §5.5 maps each §1 IN-SCOPE surface to reviewer findings.
  COVERED = surface appears in >=1 finding. GAP = no finding.
  GAP surfaces -> ADVISORY-GAP in ACTION ITEM REGISTER.
  §5.5 signal COVERED/PARTIAL is informational; no ledger row.
  §5.5 ALSO runs §10a DOMAIN COVERAGE GAP-CHECK.

§10a -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  Embedded in §5.5, after the surface coverage table.
  Step 1: Group §1 IN-SCOPE surfaces by [DOMAIN: label] annotation.
  Step 2: For each domain, check APPLICABILITY MATRIX for rows where
          Artifact Domain Covered matches AND Artifact Applicability = HIGH.
  Step 3: COVERED = >=1 HIGH-applicability matrix row covers this domain.
          ADVISORY-GAP = no HIGH-applicability matrix row covers this domain.
  Step 4: ADVISORY-GAP domains -> ACTION ITEM REGISTER:
    Attribution: "DOMAIN COVERAGE GAP-CHECK / [domain] / no HIGH-applicability reviewer"
    Class: ADVISORY
  Table: | Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding in DOMAIN and LIFECYCLE sections carries a "[§1:S-n]" surface citation.
  Missing citation = ADVISORY-ORPHAN -> ACTION ITEM REGISTER.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit RESOLUTION REGISTRY:
    | Gate | Condition | Owner | Resolution Criterion | Status |
  One row per CONDITIONAL gate. Resolution Criterion = falsifiable test.
  Else: "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS: §13 PROGRESSION LEDGER sub-section:
    | Checkpoint | g_null value | Trajectory |
    g_null(initial) | [value] | --
    g_null(post-domain) | [value] | MONOTONIC-PASS / MONOTONIC-FAIL /
                                     DOMAIN-DEGRADED / DOMAIN-RECOVERED
    g_null(final) | [value] | LIFECYCLE-DEGRADED / LIFECYCLE-RECOVERED / STABLE
  Informational only.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Finding table schema for all DOMAIN and LIFECYCLE sections:
    | F-ID | §1 Surface [§1:S-n] | Finding | Severity |
  F-ID column: named identifier F-01, F-02, ... (NOT a positional row number `#`).
    F-ID values are unique across the review output. All downstream references --
    action register entries, CH-ID response rows, lens coverage citations --
    MUST use F-ID values. Referencing a finding by row position is a contract violation.
  Section Severity = worst(Severity of all F-ID rows in this section). HIGH>MEDIUM>LOW.
  No findings: Section Severity = LOW. Derived mechanically; no editorial assignment.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN and LIFECYCLE section must address ALL entries from the role's lens.verify.
  After findings, emit LENS COVERAGE TABLE:
    | # | lens.verify Entry | Applicability (from AM-row) | Status | Finding Reference |
  Applicability column: cite the APPLICABILITY MATRIX row ID and tier.
    Value must match the pre-committed APPLICABILITY MATRIX exactly.
  Status: ADDRESSED / OPEN.
  HIGH applicability + OPEN -> ADVISORY-OPEN-LENS-REQUIRED in ACTION ITEM REGISTER.
  MEDIUM applicability + OPEN -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.
  LOW applicability + OPEN -> no register entry; cite AM row in Finding Reference.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  Mechanical precedence rule at DISPOSITION:
    1. GClose=FAIL        -> Primary Driver = BRACKET CLOSING  [override]
    2. G_domain_agg=FAIL  -> Primary Driver = DOMAIN
    3. G_lifecycle=FAIL   -> Primary Driver = LIFECYCLE
    4. GOpen=FAIL         -> Primary Driver = BRACKET OPENING
    5. GClose=CONDITIONAL -> Primary Driver = BRACKET CLOSING  [partial defeat]
    6. G_domain_agg=CONDITIONAL -> Primary Driver = DOMAIN
    7. G_lifecycle=CONDITIONAL  -> Primary Driver = LIFECYCLE
    8. GOpen=CONDITIONAL        -> Primary Driver = BRACKET OPENING
    9. all PASS           -> Primary Driver = N/A
  Emit: **Applying §16 rule [n]**: [reason]  **Primary Driver**: [result]

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]
  BRACKET OPENING challenger evaluates the null hypothesis via structured per-dimension
  comparison table BEFORE stating challenge claims.
  Table format:
    | Dimension | Status-Quo (A,0-10) | Proposed-Build (B,0-10) |
                  Best-Non-Build-Alt (C,0-10) | D1=(B-A) | D2=(B-C) | NH Verdict |
  Mark MUST-CLEAR dimensions with (*). Minimum 3 dimensions.
  Per-row NH Verdict (derive mechanically):
    FAVORS-BUILD  <-- D1>0 AND D2>0
    CONDITIONAL   <-- D1>0 AND D2<=0
    OPPOSES-BUILD <-- D1<=0
  g_null formula (pre-committed):
    HOLDS     <-- any MUST-CLEAR row = OPPOSES-BUILD
    CONDITIONAL <-- no MUST-CLEAR OPPOSES-BUILD AND
                    count(FAVORS-BUILD) <= count(OPPOSES-BUILD) + count(CONDITIONAL)
    DEFEATED  <-- no MUST-CLEAR OPPOSES-BUILD AND
                  count(FAVORS-BUILD) > count(OPPOSES-BUILD) + count(CONDITIONAL)
  DEFEATED requires BOTH D1 AND D2 positive majority across MUST-CLEAR rows.

  NH TABLE AGGREGATION RULE (governs BRACKET CLOSING re-population):
    Column A: challenger's opening score carried forward.
    Column B: average of all DOMAIN B scores per dimension PLUS LIFECYCLE B score
              per dimension, divided by (number of domain reviewers + 1).
              Formula: B_revised(d) = (sum of all domain B(d) + lifecycle B(d)) /
                                       (domain_count + 1)
    Column C: same averaging rule applied to C scores.
    All aggregations pre-committed; no editorial selection at BRACKET CLOSING.

§18 -- LIFECYCLE NH SCORE EMISSION REQUIREMENT [IMMUTABLE]
  The LIFECYCLE reviewer section emits an NH Dimension Scores sub-table BEFORE its
  LOCAL GATE LEDGER ROW. The sub-table uses the same dimension rows as the BRACKET
  OPENING NH DIMENSION TABLE (§17). Columns:
    | Dimension | Lifecycle B Score (0-10) | Lifecycle C Score (0-10) | Notes |
  The lifecycle reviewer scores each dimension from their commitment-readiness frame.
  BRACKET CLOSING reads the LIFECYCLE NH Dimension Scores sub-table alongside all
  DOMAIN reviewer B/C scores when computing the §17 NH TABLE AGGREGATION RULE.
  No prose extraction from the LIFECYCLE section is permitted in the NH aggregation
  chain; only the structured sub-table values are used.
  Lifecycle sub-table must appear BEFORE the gate ledger row in the LIFECYCLE section.
  §7 SECTION ORDER CONTRACT enforces that LIFECYCLE executes before BRACKET CLOSING.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign:
- CHALLENGER (bracket open + close): role with `archetype: challenger` (inertia-advocate)
- DOMAIN: role whose `lens.verify` entries best match the artifact's technical surface
- LIFECYCLE: role focused on commitment and program readiness

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [One sentence.] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [One sentence.] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [One sentence.] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3 from all non-challenger roles.)*

### APPLICABILITY MATRIX

Complete before BRACKET OPENING. Matrix is locked when written. For each role,
list every lens.verify entry. Rate applicability HIGH / MEDIUM / LOW for this artifact.

| Row ID | Role | lens.verify Entry | Artifact Domain Covered | Artifact Applicability | Basis for Rating |
|--------|------|------------------|------------------------|----------------------|------------------|
| AM-01 | [DOMAIN ROLE] | [Full text.] | [Domain label.] | HIGH/MEDIUM/LOW | [One sentence specific to artifact.] |
| AM-02 | [DOMAIN ROLE] | [Full text.] | [Domain label.] | [Tier.] | [Basis.] |
| AM-03 | [LIFECYCLE ROLE] | [Full text.] | [Domain label.] | [Tier.] | [Basis.] |
| AM-04 | [LIFECYCLE ROLE] | [Full text.] | [Domain label.] | [Tier.] | [Basis.] |

*(Add one row per lens.verify entry per assigned role. Matrix locked after this point.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17; complete before challenge claims)*

| Dimension | Status-Quo (A) | Proposed-Build (B) | Best-Non-Build-Alt (C) | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----------|---------------|-------------------|----------------------|---------|---------|-----------|
| [Dim-1*] | [0-10] | [0-10] | [0-10] | [B-A] | [B-C] | FAVORS-BUILD / CONDITIONAL / OPPOSES-BUILD |
| [Dim-2*] | [0-10] | [0-10] | [0-10] | [B-A] | [B-C] | [Verdict] |
| [Dim-3] | [0-10] | [0-10] | [0-10] | [B-A] | [B-C] | [Verdict] |

**Applying §17 g_null derivation rule**:
```
MUST-CLEAR OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD)  = [N]
count(CONDITIONAL)   = [N]
count(OPPOSES-BUILD) = [N]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null(initial)** *(§9 Stage 1)*: [HOLDS / CONDITIONAL / DEFEATED]

---

**Challenge claims** *(register with §0 Grounding column per §5)*:

| CH-ID | Challenge Claim | Severity | §0 Grounding |
|-------|----------------|---------|-------------|
| CH-001 | [Claim grounded in a concrete status-quo advantage.] | HIGH/MEDIUM/LOW | [§N -- contract name] |
| CH-002 | [Second claim.] | [Severity] | [§N] |

Gate: G1 (challenger bracket gate).

Null hypothesis statement: [One sentence: what the team currently does instead.]

**GOpen verdict**: [PASS / CONDITIONAL / FAIL]

*Local gate ledger row*:
| BRACKET OPENING | G1 | [PASS/CONDITIONAL/FAIL] | [Class] |

---

## DOMAIN REVIEWER

Contract: DISPOSITION_CONTRACT v1

**CH-ID Response Table**:

| CH-ID | Response | Status |
|-------|---------|--------|
| CH-001 | [Response.] | ADDRESSED / PARTIAL / OPEN |
| CH-002 | [Response.] | [Status] |

**Findings**:

| F-ID | §1 Surface [§1:S-n] | Finding | Severity |
|------|---------------------|---------|---------|
| F-01 | [Surface name] [§1:S-1] | [Specific finding.] | HIGH/MEDIUM/LOW |
| F-02 | [Surface name] [§1:S-2] | [Specific finding.] | HIGH/MEDIUM/LOW |

Section Severity = worst([F-01 severity], [F-02 severity], ...) = [result]

**LENS COVERAGE TABLE** *(per §15)*:

| # | lens.verify Entry | Applicability (from AM-row) | Status | Finding Reference |
|---|------------------|--------------------------|--------|------------------|
| 1 | [Full lens entry.] | [Tier from AM-row ID] | ADDRESSED/OPEN | [F-ID or N/A] |
| 2 | [Full lens entry.] | [Tier] | [Status] | [F-ID or N/A] |

**G_domain verdict**: [PASS / CONDITIONAL / FAIL]

*Local gate ledger row*:
| DOMAIN | G_domain | [PASS/CONDITIONAL/FAIL] | [Class] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(No local ledger row -- §6 excluded section)*

G_domain_agg = worst([G_domain values]) = [result]

**g_null(post-domain)** *(§9 Stage 2)*:
```
G_domain_agg = [value]. Applying §9 Stage 2 formula:
g_null(post-domain) = [FAIL / CONDITIONAL / <g_null(initial)>] = [value]
```

---

## §3.8 CH-ID SATURATION CHECK

*(No local ledger row -- §6 excluded section)*

| CH-ID | DOMAIN Response | LIFECYCLE Response | Saturation |
|-------|----------------|-------------------|-----------|
| CH-001 | ADDRESSED/PARTIAL/OPEN | PENDING | PENDING |
| CH-002 | [Status] | PENDING | PENDING |

LIFECYCLE does not execute until all CH-IDs are SATURATED (>=1 DOMAIN response each).
SATURATED status: [YES / NO -- list any OPEN CH-IDs blocking lifecycle]

---

## LIFECYCLE REVIEWER

Contract: DISPOSITION_CONTRACT v1

**CH-ID Response Table**:

| CH-ID | Response | Status |
|-------|---------|--------|
| CH-001 | [Lifecycle-frame response.] | ADDRESSED / PARTIAL / OPEN |
| CH-002 | [Response.] | [Status] |

**Findings**:

| F-ID | §1 Surface [§1:S-n] | Finding | Severity |
|------|---------------------|---------|---------|
| F-03 | [Surface name] [§1:S-n] | [Specific finding.] | HIGH/MEDIUM/LOW |

Section Severity = worst([lifecycle F-ID severities]) = [result]

**LENS COVERAGE TABLE** *(per §15)*:

| # | lens.verify Entry | Applicability (from AM-row) | Status | Finding Reference |
|---|------------------|--------------------------|--------|------------------|
| 1 | [Full lens entry.] | [Tier from AM-row ID] | ADDRESSED/OPEN | [F-ID or N/A] |

**NH Dimension Scores sub-table** *(per §18 -- MUST appear before gate ledger row)*:

| Dimension | Lifecycle B Score (0-10) | Lifecycle C Score (0-10) | Notes |
|-----------|------------------------|------------------------|-------|
| [Dim-1] | [Score] | [Score] | [Lifecycle-frame rationale.] |
| [Dim-2] | [Score] | [Score] | [Rationale.] |
| [Dim-3] | [Score] | [Score] | [Rationale.] |

**G_lifecycle verdict**: [PASS / CONDITIONAL / FAIL]

*Local gate ledger row*:
| LIFECYCLE | G_lifecycle | [PASS/CONDITIONAL/FAIL] | [Class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Updated CH-ID Response Table** (post-lifecycle):

| CH-ID | Domain Response | Lifecycle Response | Final Status |
|-------|----------------|-------------------|-------------|
| CH-001 | [Status] | [Status] | ADDRESSED/OPEN |
| CH-002 | [Status] | [Status] | [Status] |

FULLY SATURATED: [YES / NO -- cite waivers]

**REVISED NH DIMENSION TABLE** *(§17 NH TABLE AGGREGATION RULE applied)*:

Column A: challenger's opening score (unchanged).
Column B: avg(DOMAIN B score(s) + LIFECYCLE B score) per dimension.
Column C: avg(DOMAIN C score(s) + LIFECYCLE C score) per dimension.

| Dimension | A | B_revised | C_revised | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----------|---|-----------|-----------|---------|---------|-----------|
| [Dim-1*] | [A] | [B_rev] | [C_rev] | [B-A] | [B-C] | [Verdict] |
| [Dim-2*] | [A] | [B_rev] | [C_rev] | [B-A] | [B-C] | [Verdict] |
| [Dim-3] | [A] | [B_rev] | [C_rev] | [B-A] | [B-C] | [Verdict] |

**Applying §17 g_null derivation to revised table**:
```
MUST-CLEAR OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD)  = [N]
count(CONDITIONAL)   = [N]
count(OPPOSES-BUILD) = [N]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```

**g_null(final)** *(§9 Stage 3)*:
```
G_lifecycle = [value]. Applying §9 Stage 3 formula:
g_null(final) = [value]
```

**Override authority**: [OVERRIDE INVOKED: YES / NO]
*(If YES: "g_null OVERRIDE: [named justification]")*

**GClose verdict** = g_null(final) = [PASS / CONDITIONAL / FAIL]

*Local gate ledger row*:
| BRACKET CLOSING | GClose | [PASS/CONDITIONAL/FAIL] | [Class] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(No local ledger row -- §6 excluded section)*

| §1 Surface | Covered By Finding(s) | Coverage |
|-----------|----------------------|---------|
| [SURFACE_1] | [F-ID list or "none"] | COVERED / GAP |
| [SURFACE_2] | [F-ID list] | [Coverage] |
| [SURFACE_3] | [F-ID list] | [Coverage] |

GAP surfaces (if any): appended to ACTION ITEM REGISTER as ADVISORY-GAP.

Signal: COVERED / PARTIAL

**§10a DOMAIN COVERAGE GAP-CHECK** *(embedded)*:

| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|---------|
| [Domain-1] | [AM-row IDs with HIGH, or "none"] | COVERED / ADVISORY-GAP |
| [Domain-2] | [AM-row IDs] | [Coverage] |

ADVISORY-GAP domains (if any): appended to ACTION ITEM REGISTER.

---

## GATE VECTOR TABLE

| Gate | Verdict | Source Section |
|------|---------|---------------|
| GOpen | [value] | BRACKET OPENING |
| G_domain | [value] | DOMAIN REVIEWER |
| G_domain_agg | [value] | §3.5 (formula) |
| G_lifecycle | [value] | LIFECYCLE REVIEWER |
| GClose | [value] | BRACKET CLOSING |

---

## CROSS-ROLE SIGNALS

**§13 g_null PROGRESSION LEDGER**:

| Checkpoint | g_null value | Trajectory |
|-----------|-------------|-----------|
| Initial (GOpen) | [value] | -- |
| Post-Domain (§3.5) | [value] | [label] |
| Final (GClose) | [value] | [label] |

**Cross-role convergence**: [Where all roles agreed.]
**Cross-role conflict**: [Where domain and lifecycle disagreed with challenger.]
**Uncovered areas**: [Surfaces with no findings or OPEN CH-IDs.]

---

## DISPOSITION

**Applying §3 DISPOSITION ALGEBRA**:
```
G = {GOpen=[v], G_domain_agg=[v], G_lifecycle=[v], GClose=[v]}
Result: READY / CONDITIONAL / BLOCKED
```

**Applying §16 rule [n]**: [reason]
**Primary Driver**: [result]

**DISPOSITION**: [READY / CONDITIONAL / BLOCKED]

*(§12 RESOLUTION REGISTRY if CONDITIONAL)*

---

## ACTION ITEM REGISTER

*(Copy all local gate ledger rows verbatim -- do NOT re-derive. Append ADVISORY items.)*

| Section | Gate | Verdict | Class | Finding Reference | Action Required |
|---------|------|---------|-------|------------------|----------------|
| [Copy from local ledger rows] | | | | | |
| [ADVISORY-OPEN-LENS, ADVISORY-GAP, ADVISORY-CHARTER-GAP items] | | | | | |

---

## criterion-check

| ID | Name | Pass evidence |
|----|------|--------------|
| C-01 | Multi-voice Role Architecture | CHALLENGER + DOMAIN roles present; each applies own frame. |
| C-02 | Severity Carries Commit-Gate Semantics | §2 HIGH/MEDIUM/LOW defined with commit-gate mapping. |
| C-03 | Null Hypothesis Gate Before Domain Testimony | §17 NH DIMENSION TABLE produces g_null(initial) before DOMAIN runs. |
| C-04 | Commitment Disposition Emitted | DISPOSITION field with READY/CONDITIONAL/BLOCKED label. |
| C-05 | Action Items Traceable to Findings | ACTION ITEM REGISTER references section + F-ID per item. |
| C-06 | Artifact Scope Declared | §1 IN-SCOPE/OUT-OF-SCOPE before first reviewer. |
| C-07 | Summary with Integrating Narrative | CROSS-ROLE SIGNALS names conflict, convergence, null hypothesis reference. |
| C-08 | Depth Parameter Honored | ROLE MANIFEST reflects {{depth}} mode. |
| C-09 | Adversarial Bracket Architecture | BRACKET OPENING (pre-domain) + BRACKET CLOSING (post-domain) with override authority. |
| C-10 | Disposition Algebra Pre-committed | §3 formula in preamble before any reviewer executes. |
| C-11 | Override Field as Labeled Field | OVERRIDE INVOKED: YES/NO in BRACKET CLOSING. |
| C-12 | Action Item Class Derived Mechanically | §6 Class derivation rule in preamble; ACTION ITEM REGISTER rows copy from ledger. |
| C-13 | Prompt Inputs as Template Variables | {{artifact_id}}, {{depth}}, {{reviewer_set}} declared; Review Parameters block acknowledges. |
| C-14 | Gate Verdict in Action Register | Gate Verdict column in ACTION ITEM REGISTER (copied verbatim). |
| C-15 | Reviewer Set as Injectable Parameter | {{reviewer_set}} declared; acknowledged in Review Parameters. |
| C-16 | Alternatives Table as Bracket Anchor | §17 NH DIMENSION TABLE at BRACKET OPENING; domain reviewers score same dimensions (sub-tables); BRACKET CLOSING aggregates revised table. |
| C-17 | Pre-commitment Cascade (3 contracts) | §3 DISPOSITION, §6 CLASS DERIVATION, §17 NULL HYPOTHESIS DERIVATION RULE all in preamble. |
| C-18 | Inline Gate Ledger at Origin | Local gate ledger row at end of each verdict-emitting section. |
| C-19 | Gate Ledger Protocol as 4th Contract | §6 LOCAL GATE LEDGER PROTOCOL in preamble with syntax, timing, assembly rule. |
| C-20 | Verbatim Assembly Prohibition | §6: "copy all local rows verbatim. Do NOT re-derive." |
| C-21 | Universal Gate Ledger Coverage | BRACKET OPENING, DOMAIN, LIFECYCLE, BRACKET CLOSING all emit rows; §6 assembly covers all. |
| C-22 | Lifecycle Verdict Integration at Bracket Closing | LIFECYCLE (§4) precedes BRACKET CLOSING (§5) in §7; BRACKET CLOSING reads G_lifecycle in §9 Stage 3. |
| C-23 | Multi-alternative NH Derivation Rule | §17 uses A/B/C table with D1=(B-A) AND D2=(B-C) both required for DEFEATED. |
| C-24 | Domain-Aggregate Formula Pre-committed | §3a worst-case formula in preamble; BRACKET CLOSING applies mechanically. |
| C-25 | Non-verdict Section Excluded from Ledger | §6 EXCLUDED list names §3.5, §3.8, §5.5, §5.7, §5.8 explicitly. |
| C-26 | Canonical Section Order as Immutable Contract | §7 names full execution sequence with "Reordering violates this contract." |
| C-27 | CH-ID Saturation Pre-committed | §8 defines FULLY SATURATED tier; §3.8 gate blocks LIFECYCLE until SATURATED; BRACKET CLOSING prohibits PASS if unsaturated. |
| C-28 | NH Progression Formula 3-Stage | §9 three-stage derivation chain with formulas for each stage; GClose must equal g_null(final). |
| C-29 | Scope Coverage Gate Post-Bracket-Closing | §10 pre-commits §5.5 after BRACKET CLOSING; GAP -> ADVISORY-GAP; no ledger row. |
| C-30 | Per-Finding Severity Chain | §14 finding table F-ID rows carry Severity; Section Severity = worst() formula pre-committed. |
| C-31 | Role Lens Exhaustion | §15 LENS EXHAUSTION REQUIREMENT; LENS COVERAGE TABLE per section; OPEN+HIGH -> register item. |
| C-32 | Primary Driver Derivation | §16 9-rule precedence formula; Primary Driver emitted at DISPOSITION. |
| C-33 | Lens Applicability Rating Pre-committed | §15 cites AM-row and tier; §10a gap-check uses HIGH tier as threshold. Applicability is artifact-specific (Basis for Rating column in APPLICABILITY MATRIX). |
| C-34 | ADVISORY-GAP Domain Coverage Pre-committed | §10a pre-committed; runs after §5.7; ADVISORY-GAP domains -> ACTION ITEM REGISTER. |
| C-35 | NH Challenger Dimension Comparison Table | §17 NH DIMENSION TABLE with per-dimension scores and NH Verdict column; g_null derivable from table values alone via pre-committed formula. |
```

---

## V-02

**Axis**: Output format -- TABLE FORMAT CONTRACT block pre-declared before all §§
contracts; all table schemas (finding table with F-ID column, CH-ID table with
§0 Grounding column, NH Dimension Table, lifecycle NH sub-table, gate ledger row)
declared in a single structural block before any numbered §§ contract.

**Hypothesis**: V-01 fixes C-42 and C-43 by adding column declarations to §14 and §5
respectively. V-02 tests whether pre-declaring ALL table schemas in a single TABLE FORMAT
CONTRACT block before §1-§18 provides stronger machine-checkable enforcement. When the
table schema is a first-class pre-committed contract (rather than embedded in a numbered §),
a scorer can verify C-42 and C-43 purely by checking the CONTRACT block against the actual
output tables -- no need to read behavioral descriptions in §5 or §14. C-41 is declared
in the TABLE FORMAT CONTRACT as the NH Dimension Scores sub-table schema (lifecycle emits
this schema before its gate ledger row). The TABLE FORMAT CONTRACT is pre-declared before
any §§ contract, so it cannot be revised post-hoc. Predicted: 225/225 + C-41+C-42+C-43.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this block first, then execute the review protocol below.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided above.

The review uses a multi-role adversarial bracket architecture. The challenger defends the
status quo. Domain and lifecycle reviewers provide technical and program evidence. The
challenger closes by integrating all testimony to reach a final null hypothesis verdict.

Fill every `[BRACKETED_FIELD]` from artifact content. Write `[N/A -- reason]` when not
applicable. Do not alter, reorder, or omit any pre-printed heading, label, formula, or
structural element. Do not re-derive gate verdicts or action item classes during assembly.

---

```
======================================================================
TABLE FORMAT CONTRACT [IMMUTABLE -- all output tables must conform]
======================================================================

These table schemas are pre-committed. Every table of the named type produced
during execution must match the schema exactly. Additional columns may not be added.
Required columns may not be omitted, renamed, or replaced with positional equivalents.

FINDING TABLE (used in all DOMAIN and LIFECYCLE reviewer sections):
  | F-ID | §1 Surface [§1:S-n] | Finding | Severity |
  F-ID:     Named identifier. Format F-NN (F-01, F-02, ...). NOT a positional row number.
            Unique across the entire review output. All downstream references (action register,
            CH-ID response rows, lens coverage citations) MUST use F-ID values.
            Referencing a finding by row position when an F-ID column exists is a contract
            violation.
  §1 Surface: names a specific surface from §1 IN-SCOPE list with §1:S-n citation.
  Finding:  names a specific artifact surface, section, field, or assumption.
  Severity: exactly HIGH, MEDIUM, or LOW.

CH-ID CHALLENGE TABLE (used in BRACKET OPENING challenge registration):
  | CH-ID | Challenge Claim | Severity | §0 Grounding |
  CH-ID:        Format CH-NNN (CH-001, CH-002, ...). Unique per review.
  §0 Grounding: Required. Names the specific preamble contract section (e.g., "§3
                DISPOSITION ALGEBRA", "§9 NULL HYPOTHESIS PROGRESSION CONTRACT") whose
                pre-committed rule authorizes or motivates this challenge. Populated at
                registration time; cannot be assigned post-hoc. A CH-ID without §0
                Grounding is structurally incomplete; write "[GROUNDING-ABSENT]" and
                add to ACTION ITEM REGISTER as ADVISORY.

NH DIMENSION TABLE (used in BRACKET OPENING §17 evaluation):
  | Dimension | Status-Quo (A) | Proposed-Build (B) | Best-Non-Build-Alt (C) |
    D1=(B-A) | D2=(B-C) | NH Verdict |
  Mark MUST-CLEAR dimensions with (*). Minimum 3 dimensions.
  NH Verdict: FAVORS-BUILD / CONDITIONAL / OPPOSES-BUILD (derived per §17 rule).

NH DIMENSION SCORES SUB-TABLE (required in LIFECYCLE reviewer section, per §18):
  | Dimension | Lifecycle B Score (0-10) | Lifecycle C Score (0-10) | Notes |
  Same dimension rows as NH DIMENSION TABLE. Must appear BEFORE gate ledger row.
  BRACKET CLOSING reads this sub-table in NH aggregation (§17 aggregation rule).

GATE LEDGER ROW (emitted at end of each verdict-emitting section, per §6):
  | Section | Gate | Verdict | Class |
  Verdict: PASS / CONDITIONAL / FAIL (copied from section verdict; not re-derived).
  Class:   BLOCKED (FAIL) / CONDITIONAL (CONDITIONAL) / ADVISORY (PASS).

APPLICABILITY MATRIX ROW (used in ROLE MANIFEST section):
  | Row ID | Role | lens.verify Entry | Artifact Domain Covered |
    Artifact Applicability | Basis for Rating |
  Artifact Applicability: HIGH / MEDIUM / LOW specific to this artifact.
  Basis for Rating: one sentence naming the artifact domain and the specific lens.verify
    entry it maps to. Generic basis ("this is a technical role") is invalid.

======================================================================
END TABLE FORMAT CONTRACT
======================================================================
```

---

```
======================================================================
DISPOSITION_CONTRACT v1 [IMMUTABLE BLOCK -- read before any reviewer executes]
======================================================================

§1 -- SCOPE ENUMERATION
  IN-SCOPE (cited in §5.5; each surface carries [DOMAIN: label] for §10a):
    1. [SURFACE_1] [DOMAIN: label]
    2. [SURFACE_2] [DOMAIN: label]
    3. [SURFACE_3] [DOMAIN: label]
  OUT-OF-SCOPE:
    1. [SURFACE -- REASON]
  Scope Amendment Protocol:
    SCOPE AMENDMENT: [surface] added -- [reason]. Silent expansion violates contract.
§1 COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions commitment. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any Gi=CONDITIONAL
  READY <-- all Gi=PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts). FAIL>CONDITIONAL>PASS.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Challenge registration uses CH-ID CHALLENGE TABLE schema (TABLE FORMAT CONTRACT).
  §0 Grounding column: required at registration. Cannot be post-hoc assigned.
  Every downstream reviewer section carries a mandatory CH-ID response table.
  PASS verdict prohibited if any CH-ID row shows OPEN status.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Use GATE LEDGER ROW schema (TABLE FORMAT CONTRACT).
  Emit at end of each verdict-emitting section. Timing: after verdict is stated.
  Assembly rule: copy all local rows to ACTION ITEM REGISTER verbatim.
    Do NOT re-derive Verdict or Class. Register is a copy, not a synthesis.
  EXCLUDED (no row): §3.5, §3.8, §5.5, §5.7, §5.8.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1. ROLE MANIFEST  2. BRACKET OPENING  3. DOMAIN(s)
  3.5 DOMAIN-AGGREGATE CHECKPOINT  3.8 CH-ID SATURATION CHECK
  4. LIFECYCLE  5. BRACKET CLOSING  5.5 SCOPE COVERAGE RECONCILIATION
  6. GATE VECTOR TABLE  7. CROSS-ROLE SIGNALS  8. DISPOSITION  9. ACTION ITEM REGISTER
  Reordering violates contract.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  FULLY SATURATED: every CH-ID has DOMAIN + LIFECYCLE responses.
  PASS from BRACKET CLOSING prohibited without full saturation or stated waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = §17 formula output at BRACKET OPENING
  Stage 2: g_null(post-domain) = f(G_domain_agg, g_null(initial))
    FAIL: FAIL. CONDITIONAL: max(initial, CONDITIONAL). PASS: unchanged.
  Stage 3: g_null(final) = f(G_lifecycle, g_null(post-domain))
    Same rules. GClose must equal g_null(final). FAIL<CONDITIONAL<PASS.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 after BRACKET CLOSING: COVERED (>=1 finding) or GAP -> ADVISORY-GAP in register.
  Informational; no ledger row. §5.5 also runs §10a.

§10a -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  Group §1 surfaces by [DOMAIN: label]. For each domain: is there >=1 AM row with HIGH?
  COVERED or ADVISORY-GAP. ADVISORY-GAP -> ACTION ITEM REGISTER.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding row (per TABLE FORMAT CONTRACT FINDING TABLE) carries [§1:S-n] citation.
  Missing citation = ADVISORY-ORPHAN -> ACTION ITEM REGISTER.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit | Gate | Condition | Owner | Resolution Criterion | Status |
  Else: "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS sub-section: | g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory |

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Use FINDING TABLE schema (TABLE FORMAT CONTRACT). F-ID column is mandatory and named.
  Section Severity = worst(all F-ID row severities). HIGH>MEDIUM>LOW. Derived; not editorial.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  LENS COVERAGE TABLE per domain/lifecycle section:
    | # | lens.verify Entry | Applicability (AM-row + tier) | Status | Finding Reference |
  Cite TABLE FORMAT CONTRACT APPLICABILITY MATRIX ROW ID and tier. Do not assign inline.
  HIGH+OPEN -> ADVISORY-OPEN-LENS-REQUIRED. MEDIUM+OPEN -> ADVISORY-OPEN-LENS.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  Precedence: GClose=FAIL(1) > G_domain_agg=FAIL(2) > G_lifecycle=FAIL(3) > GOpen=FAIL(4) >
  GClose=COND(5) > G_domain_agg=COND(6) > G_lifecycle=COND(7) > GOpen=COND(8) > all PASS(9).
  Apply mechanically. Emit at DISPOSITION.

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]
  Use NH DIMENSION TABLE schema (TABLE FORMAT CONTRACT). >=3 dimensions, MUST-CLEAR marked.
  Per-row NH Verdict: FAVORS-BUILD (D1>0 AND D2>0) / CONDITIONAL (D1>0, D2<=0) /
    OPPOSES-BUILD (D1<=0). g_null: HOLDS (<any MUST-CLEAR OPPOSES) /
    CONDITIONAL / DEFEATED (no MUST-CLEAR OPPOSES, FAVORS majority over OPPOSES+COND).
  NH TABLE AGGREGATION RULE: A = opening; B = avg(domains + lifecycle); C = avg(domains + lifecycle).

§18 -- LIFECYCLE NH SCORE EMISSION REQUIREMENT [IMMUTABLE]
  LIFECYCLE reviewer section emits NH DIMENSION SCORES SUB-TABLE (TABLE FORMAT CONTRACT
  schema) BEFORE its GATE LEDGER ROW. Same dimension rows as §17 NH DIMENSION TABLE.
  BRACKET CLOSING reads sub-table in §17 NH TABLE AGGREGATION RULE.
  B_revised(d) = (sum of all domain B(d) + lifecycle B(d)) / (domain_count + 1).
  No prose extraction from LIFECYCLE in NH aggregation chain.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

*(Same structure as V-01 ROLE MANIFEST + APPLICABILITY MATRIX; all rows per TABLE FORMAT
CONTRACT APPLICABILITY MATRIX ROW schema.)*

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [One sentence.] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [One sentence.] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [One sentence.] |

### APPLICABILITY MATRIX

| Row ID | Role | lens.verify Entry | Artifact Domain Covered | Artifact Applicability | Basis for Rating |
|--------|------|------------------|------------------------|----------------------|------------------|
| AM-01 | [ROLE] | [Entry.] | [Domain.] | HIGH/MEDIUM/LOW | [Specific to artifact.] |
| AM-02 | [ROLE] | [Entry.] | [Domain.] | [Tier.] | [Basis.] |

*(All subsequent reviewer sections, gate tables, and register sections follow V-01
structure exactly, using TABLE FORMAT CONTRACT schemas throughout.)*

---

## V-03

**Axis**: Inertia framing -- STATUS QUO FRAMING CONTRACT opens preamble with named
§0-CID commitment artifacts. CH-ID §0 Grounding column cites §0-CID values (stronger
semantic grounding than generic §§ contract refs). F-ID column enforced by inertia-
advocate auditability requirement stated in the framing contract. §18 lifecycle NH
emission present as standalone contract.

**Hypothesis**: C-43 requires CH-ID §0 Grounding to cite the "preamble commitment that
authorizes each challenge." V-01 and V-02 satisfy this with §§ section references (e.g.,
"§17 NULL HYPOTHESIS DIMENSION TABLE CONTRACT"). V-03 tests whether richer grounding
via named §0-CID artifacts (concrete status-quo commitments registered before any §§
contracts) provides stronger enforcement: the challenger pre-registers their best-case
arguments as §0-CID values, and each CH-ID's §0 Grounding cites the specific §0-CID
value that the challenge is designed to probe. This makes the grounding semantically
auditable -- a scorer reads §0-CID-n and the CH-ID claim and verifies that the claim
actually probes that commitment. F-ID is motivated by the STATUS QUO FRAMING CONTRACT's
auditability requirement: the inertia-advocate needs named, stable finding identifiers
to verify at BRACKET CLOSING whether each §0-CID was addressed by a specific finding.
Predicted: 225/225 + C-41+C-42+C-43.

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

You are running `org-review`. The challenger's prior is that the artifact should not be
built. The review is the evidence process that can overturn that prior.

Fill every `[BRACKETED_FIELD]` from artifact content. Write `[N/A -- reason]` when not
applicable. Do not alter, reorder, or omit any pre-printed structural element.

---

```
======================================================================
§0 -- STATUS QUO FRAMING CONTRACT [IMMUTABLE -- precedes all §§ contracts]
======================================================================

The challenger pre-registers their strongest no-build commitments as named artifacts
(§0-CID values) before any §§ contracts execute. These serve as:
  (a) the semantic basis for CH-ID §0 Grounding citations (downstream)
  (b) the audit trail for BRACKET CLOSING Charter Coverage verification
  (c) the F-ID auditability requirement (see below)

Status quo statement (one sentence):
  [What the team currently does instead of building the artifact under review.]

Challenger commitments (minimum two, maximum five):
  §0-C01 -- [Name the status-quo advantage. State the concrete dimension of viability.
             State the minimum evidence threshold that would defeat this commitment.]
  §0-C02 -- [Second commitment. Same format.]
  §0-C03 -- [Third commitment, or omit.]

F-ID AUDITABILITY REQUIREMENT (pre-committed by inertia-advocate):
  The inertia-advocate requires that every finding carry a named, stable identifier
  (F-ID, format F-NN) so that BRACKET CLOSING can trace which findings -- if any --
  specifically address each §0-CID commitment. A finding referenced only by row position
  cannot be reliably cited in the Charter Coverage Audit. F-ID is mandatory on every
  finding row across all reviewer sections. This requirement is pre-committed here
  (before any reviewer executes) and cannot be waived at execution time.

Charter Coverage Audit (emitted at BRACKET CLOSING):
  | §0-CID | Commitment Text (summary) | Addressed By (F-ID list) | Coverage |
  Coverage: COVERED (>=1 finding cited and ADDRESSED/PARTIAL by domain/lifecycle) or
            CHARTER-GAP (no finding cited, or all citees remain OPEN at closing).
  CHARTER-GAP -> ACTION ITEM REGISTER: "CHARTER COVERAGE AUDIT / §0-C0n / [reason]", ADVISORY.

§0 COMPLETE -- DISPOSITION_CONTRACT proceeds below.
======================================================================
```

---

```
======================================================================
DISPOSITION_CONTRACT v1 [IMMUTABLE BLOCK]
======================================================================

§1 -- SCOPE ENUMERATION
  IN-SCOPE (each surface: [DOMAIN: label] for §10a):
    1. [SURFACE_1] [DOMAIN: label]
    2. [SURFACE_2] [DOMAIN: label]
    3. [SURFACE_3] [DOMAIN: label]
  OUT-OF-SCOPE: 1. [SURFACE -- REASON]
  SCOPE AMENDMENT: [surface] added -- [reason] (silent expansion violates contract)
§1 COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions commitment. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any Gi=CONDITIONAL
  READY <-- all Gi=PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts). FAIL>CONDITIONAL>PASS.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Challenge registration table schema:
    | CH-ID | Challenge Claim | Severity | §0 Grounding |
  §0 Grounding: cites the §0-CID value (from STATUS QUO FRAMING CONTRACT §0) that this
    challenge is designed to probe. Format: "§0-C0n -- [§0-CID name]". Every CH-ID must
    carry a §0-CID citation. Challenges that cannot be grounded in a registered §0-CID
    are GROUNDING-ABSENT; flag inline and add to ACTION ITEM REGISTER as ADVISORY.
    Two-axis traceability: backward to §0-CID commitment (§0 Grounding column),
    forward to reviewer responses (response tables in downstream sections).
  Every downstream reviewer section: mandatory CH-ID response table.
  PASS verdict prohibited if any CH-ID row shows OPEN status.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emit at end of each verdict-emitting section. Assembly: copy verbatim to register.
  Do NOT re-derive. EXCLUDED: §3.5, §3.8, §5.5, §5.7, §5.8.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1. ROLE MANIFEST  2. BRACKET OPENING  3. DOMAIN(s)
  3.5 DOMAIN-AGGREGATE CHECKPOINT  3.8 CH-ID SATURATION CHECK
  4. LIFECYCLE  5. BRACKET CLOSING  5.5 SCOPE COVERAGE RECONCILIATION
  6. GATE VECTOR TABLE  7. CROSS-ROLE SIGNALS  8. DISPOSITION  9. ACTION ITEM REGISTER
  Reordering violates contract.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  FULLY SATURATED: every CH-ID has DOMAIN + LIFECYCLE responses.
  BRACKET CLOSING PASS prohibited without saturation or stated waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = §17 formula at BRACKET OPENING
  Stage 2: g_null(post-domain) = f(G_domain_agg, g_null(initial))
  Stage 3: g_null(final) = f(G_lifecycle, g_null(post-domain))
  GClose must equal g_null(final). FAIL<CONDITIONAL<PASS.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 after BRACKET CLOSING: COVERED (>=1 finding) or GAP -> ADVISORY-GAP.
  Informational; no ledger row. §5.5 also runs §10a.

§10a -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  Group §1 surfaces by [DOMAIN: label]. Check APPLICABILITY MATRIX for HIGH per domain.
  ADVISORY-GAP domains -> ACTION ITEM REGISTER.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding row carries [§1:S-n] citation. Missing = ADVISORY-ORPHAN -> register.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit | Gate | Condition | Owner | Resolution Criterion | Status |

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS sub-section: g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Finding table schema: | F-ID | §1 Surface [§1:S-n] | Finding | Severity |
  F-ID: named identifier F-NN, as required by §0 F-ID AUDITABILITY REQUIREMENT.
    NOT a positional row number. Unique across review. All downstream references use F-ID.
  Section Severity = worst(all F-ID row severities). Derived; not editorial.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  LENS COVERAGE TABLE per reviewer section:
    | # | lens.verify Entry | Applicability (AM-row) | Status | Finding Reference |
  HIGH+OPEN -> ADVISORY-OPEN-LENS-REQUIRED. MEDIUM+OPEN -> ADVISORY-OPEN-LENS.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  9-rule precedence over gate verdict vector. Emitted at DISPOSITION.

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]
  NH DIMENSION TABLE before challenge claims. >=3 dimensions. MUST-CLEAR marked.
  Per-row: FAVORS-BUILD / CONDITIONAL / OPPOSES-BUILD.
  g_null: HOLDS / CONDITIONAL / DEFEATED via pre-committed formula.
  NH TABLE AGGREGATION RULE: B = avg(domains + lifecycle); C = same.

§18 -- LIFECYCLE NH SCORE EMISSION REQUIREMENT [IMMUTABLE]
  LIFECYCLE section emits NH Dimension Scores sub-table:
    | Dimension | Lifecycle B Score (0-10) | Lifecycle C Score (0-10) | Notes |
  Same dimension rows as §17. Must appear BEFORE gate ledger row.
  BRACKET CLOSING reads sub-table in NH aggregation (§17 aggregation rule).
  B_revised(d) = (sum of DOMAIN B(d) + lifecycle B(d)) / (domain_count + 1).

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

*(ROLE MANIFEST, APPLICABILITY MATRIX, and all reviewer sections follow V-01 structure,
with the following changes:*
- *CH-ID registration uses §0-CID values in §0 Grounding column, not §§ refs*
- *Finding tables use F-ID schema per §14 / §0 F-ID auditability requirement*
- *LIFECYCLE section emits NH Dimension Scores sub-table per §18*
- *BRACKET CLOSING emits Charter Coverage Audit per §0 before GClose verdict)*

---

## V-04

**Axis**: Lifecycle + Output format (two-axis) -- V-01's §18 LIFECYCLE NH SCORE EMISSION
as top-level contract combined with V-02's TABLE FORMAT CONTRACT block pre-declaring all
table schemas. C-42 has dual enforcement (TABLE FORMAT CONTRACT F-ID schema + §14 named
column requirement). C-43 has dual enforcement (TABLE FORMAT CONTRACT §0 Grounding schema
+ §5 registration clause). C-41 from §18 explicit contract reinforced by TABLE FORMAT
CONTRACT NH DIMENSION SCORES SUB-TABLE schema.

**Hypothesis**: V-01 achieves all three criteria via numbered contract additions to the
existing §§ structure. V-02 achieves all three via a pre-declared schema layer. V-04
tests whether combining both enforcement paths (schema-layer declaration + numbered
behavioral contract) makes each criterion independently verifiable from two structural
positions -- making regression under model execution less likely than with a single
enforcement path. Predicted: 225/225 + C-41+C-42+C-43 with dual enforcement.

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

You are running `org-review`. Multi-role adversarial bracket architecture. Challenger
defends status quo; domain and lifecycle reviewers provide evidence; challenger closes.

Fill every `[BRACKETED_FIELD]`. Write `[N/A -- reason]` when not applicable.
Do not alter, reorder, or omit any pre-printed structural element.

---

```
======================================================================
TABLE FORMAT CONTRACT [IMMUTABLE -- all output tables must conform]
======================================================================

FINDING TABLE (all DOMAIN and LIFECYCLE sections):
  | F-ID | §1 Surface [§1:S-n] | Finding | Severity |
  F-ID: Named identifier F-NN. NOT positional row number `#`. Unique per review.
    All downstream references (action register, CH-ID responses, lens coverage) use F-ID.
    Positional row reference is a contract violation.

CH-ID CHALLENGE TABLE (BRACKET OPENING registration):
  | CH-ID | Challenge Claim | Severity | §0 Grounding |
  §0 Grounding: Required column. Names the specific preamble contract section (§2-§18)
    that authorizes this challenge. Populated at registration time. Cannot be post-hoc.
    [GROUNDING-ABSENT] if missing -> ACTION ITEM REGISTER ADVISORY.

NH DIMENSION TABLE (BRACKET OPENING §17 evaluation):
  | Dimension | Status-Quo (A) | Proposed-Build (B) | Best-Non-Build-Alt (C) |
    D1=(B-A) | D2=(B-C) | NH Verdict |
  >=3 dimensions. MUST-CLEAR marked (*). NH Verdict per §17 rule.

NH DIMENSION SCORES SUB-TABLE (LIFECYCLE section, per §18):
  | Dimension | Lifecycle B Score (0-10) | Lifecycle C Score (0-10) | Notes |
  Same dimension rows as NH DIMENSION TABLE. MUST appear BEFORE gate ledger row.
  BRACKET CLOSING reads this sub-table in §17 NH aggregation.

GATE LEDGER ROW (each verdict-emitting section, per §6):
  | Section | Gate | Verdict | Class |

APPLICABILITY MATRIX ROW (ROLE MANIFEST):
  | Row ID | Role | lens.verify Entry | Artifact Domain Covered |
    Artifact Applicability | Basis for Rating |

======================================================================
END TABLE FORMAT CONTRACT
======================================================================
```

---

```
======================================================================
DISPOSITION_CONTRACT v1 [IMMUTABLE BLOCK]
======================================================================

§1 -- SCOPE ENUMERATION
  IN-SCOPE (each: [DOMAIN: label]):
    1. [SURFACE_1] [DOMAIN: label]
    2. [SURFACE_2] [DOMAIN: label]
    3. [SURFACE_3] [DOMAIN: label]
  OUT-OF-SCOPE: 1. [SURFACE -- REASON]
  Scope Amendment Protocol: SCOPE AMENDMENT: [surface] added -- [reason]
§1 COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks. MEDIUM = Conditions. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any Gi=CONDITIONAL
  READY <-- all Gi=PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain). FAIL>CONDITIONAL>PASS.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Challenge registration uses CH-ID CHALLENGE TABLE schema (TABLE FORMAT CONTRACT).
  §0 Grounding column: required. Cites §§ contract section authorizing challenge.
  Populated at registration time. [GROUNDING-ABSENT] if missing -> ADVISORY in register.
  All downstream sections carry CH-ID response tables.
  PASS verdict prohibited if any CH-ID is OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Use GATE LEDGER ROW schema (TABLE FORMAT CONTRACT).
  Emit at end of each verdict-emitting section. Copy verbatim to ACTION ITEM REGISTER.
  Do NOT re-derive Verdict or Class. EXCLUDED: §3.5, §3.8, §5.5, §5.7, §5.8.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.ROLE MANIFEST  2.BRACKET OPENING  3.DOMAIN(s)
  3.5 DOMAIN-AGGREGATE  3.8 CH-ID SATURATION  4.LIFECYCLE
  5.BRACKET CLOSING  5.5 SCOPE COVERAGE  6.GATE VECTOR  7.CROSS-ROLE
  8.DISPOSITION  9.ACTION REGISTER  -- Reordering violates contract.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  FULLY SATURATED: every CH-ID has DOMAIN + LIFECYCLE responses.
  BRACKET CLOSING PASS prohibited without saturation or waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = §17 output at BRACKET OPENING
  Stage 2: g_null(post-domain) = f(G_domain_agg, g_null(initial))
  Stage 3: g_null(final) = f(G_lifecycle, g_null(post-domain))
  GClose must equal g_null(final). FAIL<CONDITIONAL<PASS.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 after BRACKET CLOSING. GAP -> ADVISORY-GAP. Also runs §10a.

§10a -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  By [DOMAIN: label] groups. HIGH applicability required for COVERED. Else ADVISORY-GAP.

§11 -- FINDING-SURFACE LINKAGE [IMMUTABLE]
  Each finding row carries [§1:S-n]. Missing = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit resolution registry table.

§13 -- g_null PROGRESSION LEDGER [IMMUTABLE]
  CROSS-ROLE SIGNALS sub-section: 3-row table, g_null(initial/post-domain/final) + Trajectory.

§14 -- FINDING SEVERITY AGGREGATION [IMMUTABLE]
  Use FINDING TABLE schema (TABLE FORMAT CONTRACT). F-ID is named, not positional.
  (Dual enforcement: TABLE FORMAT CONTRACT + this §14 requirement.)
  Section Severity = worst(all F-ID rows). Derived; not editorial.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  LENS COVERAGE TABLE: | # | lens.verify Entry | Applicability (AM-row) | Status | F-ID Ref |
  HIGH+OPEN -> ADVISORY-OPEN-LENS-REQUIRED. MEDIUM+OPEN -> ADVISORY-OPEN-LENS.

§16 -- PRIMARY DRIVER DERIVATION [IMMUTABLE]
  9-rule precedence over gate verdicts. Emitted at DISPOSITION.

§17 -- NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  Use NH DIMENSION TABLE schema (TABLE FORMAT CONTRACT). MUST-CLEAR (*) required.
  Pre-committed g_null formula: HOLDS / CONDITIONAL / DEFEATED.
  NH TABLE AGGREGATION RULE: B = avg(domains + lifecycle); C = same.

§18 -- LIFECYCLE NH SCORE EMISSION [IMMUTABLE]
  LIFECYCLE section emits NH DIMENSION SCORES SUB-TABLE (TABLE FORMAT CONTRACT schema)
  BEFORE its GATE LEDGER ROW.
  (Dual enforcement: TABLE FORMAT CONTRACT schema + this §18 behavioral requirement.)
  BRACKET CLOSING reads sub-table in §17 aggregation rule.
  B_revised(d) = (sum DOMAIN B(d) + lifecycle B(d)) / (domain_count + 1).
  No prose extraction from LIFECYCLE in NH aggregation.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

*(ROLE MANIFEST, APPLICABILITY MATRIX, and all reviewer sections follow V-01 structure.
Key differences from V-01: CH-ID CHALLENGE TABLE uses TABLE FORMAT CONTRACT schema;
FINDING TABLE uses TABLE FORMAT CONTRACT schema with F-ID; LIFECYCLE section emits
NH DIMENSION SCORES SUB-TABLE per TABLE FORMAT CONTRACT schema.)*

---

## V-05

**Axis**: Lifecycle + Output format + Inertia framing (three-axis) -- All three single-axis
patterns combined. STATUS QUO FRAMING CONTRACT §0-CID values provide the richest semantic
grounding for C-43 (CH-ID §0 Grounding cites named commitment artifacts, not just §§ section
refs). TABLE FORMAT CONTRACT pre-declares all schemas for C-42 and C-41. §18 LIFECYCLE NH
SCORE EMISSION as top-level contract for C-41. Triple enforcement paths for C-42 (TABLE
FORMAT CONTRACT + §14 + §0 F-ID auditability). Triple enforcement paths for C-43 (TABLE
FORMAT CONTRACT + §5 §0-CID citation + §0 charter structure). Full cross-criterion
traceability: §0-CID values thread through CH-ID §0 Grounding (C-43), F-ID finding
citations in Charter Coverage Audit (C-42), and lifecycle NH scores in §17 aggregation (C-41).

**Hypothesis**: V-04 combined V-01 and V-02 (lifecycle + output format). V-05 adds the
inertia framing axis: pre-registering §0-CID values gives the §0 Grounding column semantic
content beyond a §§ section reference. A scorer verifying C-43 on V-05 can read §0-C02
and the CH-ID claim and confirm the claim specifically probes that named commitment --
stronger evidence than "this challenge is authorized by §17." Meanwhile, the F-ID
auditability requirement in §0 provides independent justification for C-42 (the
inertia-advocate requires stable finding IDs to verify §0-CID coverage at closing).
The three axes reinforce each other through a traceability chain: §0-CID commitment ->
CH-ID §0 Grounding (C-43) -> challenge claim -> finding response (F-ID, C-42) ->
Charter Coverage Audit -> g_null trajectory (C-41 lifecycle sub-table). Predicted:
225/225 + C-41+C-42+C-43 with strongest enforcement chain.

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

You are running `org-review`. The challenger's prior is that the artifact should not be
built. This review is the evidence process that can overturn that prior.

Fill every `[BRACKETED_FIELD]`. `[N/A -- reason]` when not applicable.
Do not alter, reorder, or omit any pre-printed structural element.

---

```
======================================================================
§0 -- STATUS QUO FRAMING CONTRACT [IMMUTABLE -- precedes TABLE FORMAT CONTRACT]
======================================================================

The challenger pre-registers their strongest no-build commitments as named §0-CID
artifacts. These are the semantic anchors for CH-ID §0 Grounding citations, the
F-ID auditability requirement, and the BRACKET CLOSING Charter Coverage Audit.

Status quo statement:
  [One sentence: what the team currently does instead.]

Challenger commitments:
  §0-C01 -- [Name the commitment. State the specific status-quo advantage dimension.
             State the minimum evidence threshold that would defeat this commitment.
             Example: "Existing workflow covers 80% of cases. New artifact must show
             measurable improvement on the remaining 20% to justify switching cost."]
  §0-C02 -- [Second commitment. Same format.]
  §0-C03 -- [Third commitment, or omit if fewer than three are meaningful.]

F-ID AUDITABILITY REQUIREMENT (pre-committed by inertia-advocate):
  Named, stable finding identifiers (F-ID, format F-NN) are required on every finding
  row across all reviewer sections. F-ID enables the Charter Coverage Audit to trace
  which specific findings addressed which §0-CID commitments. Positional row references
  cannot fulfill this traceability requirement and are prohibited. This requirement is
  binding before any reviewer executes and cannot be waived at execution time.

§0 COMPLETE -- TABLE FORMAT CONTRACT and DISPOSITION_CONTRACT proceed below.
======================================================================
```

---

```
======================================================================
TABLE FORMAT CONTRACT [IMMUTABLE -- precedes §§ contracts]
======================================================================

FINDING TABLE (all DOMAIN and LIFECYCLE sections):
  | F-ID | §1 Surface [§1:S-n] | Finding | Severity |
  F-ID: Named identifier F-NN. NOT positional `#`. Unique across review.
    Enforced by: §0 F-ID AUDITABILITY REQUIREMENT (above) AND §14 (below).
    All downstream references use F-ID values. Positional reference is a contract violation.

CH-ID CHALLENGE TABLE (BRACKET OPENING registration):
  | CH-ID | Challenge Claim | Severity | §0 Grounding |
  §0 Grounding: Required column. Cites the §0-CID value (STATUS QUO FRAMING CONTRACT §0)
    that this challenge is designed to probe. Format: "§0-C0n -- [§0-CID name]".
    Enforced by: §0 (commitment registration) AND §5 (tracing requirement).
    [GROUNDING-ABSENT] if missing -> ACTION ITEM REGISTER ADVISORY.

NH DIMENSION TABLE (BRACKET OPENING §17):
  | Dimension | Status-Quo (A) | Proposed-Build (B) | Best-Non-Build-Alt (C) |
    D1=(B-A) | D2=(B-C) | NH Verdict |

NH DIMENSION SCORES SUB-TABLE (LIFECYCLE section, per §18):
  | Dimension | Lifecycle B Score (0-10) | Lifecycle C Score (0-10) | Notes |
  Same dimensions as NH DIMENSION TABLE. BEFORE gate ledger row.
  Enforced by: TABLE FORMAT CONTRACT schema (here) AND §18 (below).

GATE LEDGER ROW (verdict-emitting sections, per §6):
  | Section | Gate | Verdict | Class |

APPLICABILITY MATRIX ROW:
  | Row ID | Role | lens.verify Entry | Artifact Domain Covered |
    Artifact Applicability | Basis for Rating |

CHARTER COVERAGE AUDIT TABLE (BRACKET CLOSING):
  | §0-CID | Commitment Text (summary) | Addressed By (F-ID list) | Coverage |

======================================================================
END TABLE FORMAT CONTRACT
======================================================================
```

---

```
======================================================================
DISPOSITION_CONTRACT v1 [IMMUTABLE BLOCK]
======================================================================

§1 -- SCOPE ENUMERATION
  IN-SCOPE (each: [DOMAIN: label]):
    1. [SURFACE_1] [DOMAIN: label]
    2. [SURFACE_2] [DOMAIN: label]
    3. [SURFACE_3] [DOMAIN: label]
  OUT-OF-SCOPE: 1. [SURFACE -- REASON]
  SCOPE AMENDMENT: [surface] added -- [reason]
§1 COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks. MEDIUM = Conditions. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any Gi=CONDITIONAL
  READY <-- all Gi=PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain). FAIL>CONDITIONAL>PASS.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Challenge registration uses CH-ID CHALLENGE TABLE schema (TABLE FORMAT CONTRACT).
  §0 Grounding: cites §0-CID value from STATUS QUO FRAMING CONTRACT.
    Two-axis traceability: backward (§0-CID commitment probed) + forward (reviewer responses).
    (Dual enforcement: TABLE FORMAT CONTRACT schema + this §5 requirement.)
  All downstream sections: mandatory CH-ID response table.
  PASS verdict prohibited if any CH-ID is OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Use GATE LEDGER ROW schema (TABLE FORMAT CONTRACT).
  Emit end of each verdict-emitting section. Copy verbatim to register. No re-derivation.
  EXCLUDED: §3.5, §3.8, §5.5, §5.7, §5.8.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.ROLE MANIFEST  2.BRACKET OPENING  3.DOMAIN(s)
  3.5 DOMAIN-AGGREGATE  3.8 CH-ID SATURATION  4.LIFECYCLE
  5.BRACKET CLOSING  5.5 SCOPE COVERAGE  6.GATE VECTOR  7.CROSS-ROLE
  8.DISPOSITION  9.ACTION REGISTER  -- Reordering violates contract.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  FULLY SATURATED: every CH-ID has DOMAIN + LIFECYCLE responses.
  BRACKET CLOSING PASS prohibited without saturation or waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = §17 output at BRACKET OPENING
  Stage 2: g_null(post-domain) = f(G_domain_agg, g_null(initial))
  Stage 3: g_null(final) = f(G_lifecycle, g_null(post-domain))
  GClose must equal g_null(final). FAIL<CONDITIONAL<PASS.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 after BRACKET CLOSING. GAP -> ADVISORY-GAP in register. Also runs §10a.

§10a -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  By [DOMAIN: label] groups. HIGH required for COVERED. ADVISORY-GAP -> register.

§11 -- FINDING-SURFACE LINKAGE [IMMUTABLE]
  Each finding row: [§1:S-n] citation. Missing = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit resolution registry table.

§13 -- g_null PROGRESSION LEDGER [IMMUTABLE]
  CROSS-ROLE SIGNALS: 3-row table, g_null(initial/post-domain/final) + Trajectory.

§14 -- FINDING SEVERITY AGGREGATION [IMMUTABLE]
  Use FINDING TABLE schema (TABLE FORMAT CONTRACT). F-ID named column.
  (Triple enforcement: §0 F-ID requirement + TABLE FORMAT CONTRACT + §14.)
  Section Severity = worst(all F-ID rows). Derived; not editorial.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  LENS COVERAGE TABLE: | # | lens.verify Entry | Applicability (AM-row) | Status | F-ID Ref |
  HIGH+OPEN -> ADVISORY-OPEN-LENS-REQUIRED. MEDIUM+OPEN -> ADVISORY-OPEN-LENS.

§16 -- PRIMARY DRIVER DERIVATION [IMMUTABLE]
  9-rule precedence over gate verdicts. Emitted at DISPOSITION.

§17 -- NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  Use NH DIMENSION TABLE schema (TABLE FORMAT CONTRACT). >=3 dimensions. MUST-CLEAR (*).
  Per-row: FAVORS-BUILD / CONDITIONAL / OPPOSES-BUILD.
  g_null: HOLDS / CONDITIONAL / DEFEATED.
  NH TABLE AGGREGATION RULE: A = opening; B = avg(domains + lifecycle); C = same.

§18 -- LIFECYCLE NH SCORE EMISSION [IMMUTABLE]
  LIFECYCLE section emits NH DIMENSION SCORES SUB-TABLE (TABLE FORMAT CONTRACT schema)
  BEFORE its GATE LEDGER ROW.
  (Triple enforcement: §0 framing architecture + TABLE FORMAT CONTRACT schema + §18.)
  Execution closing note: "LIFECYCLE B and C scores flow through: NH DIMENSION SCORES
  SUB-TABLE -> §17 aggregation formula -> BRACKET CLOSING NH DIMENSION TABLE
  re-population -> g_null(final)."
  B_revised(d) = (sum DOMAIN B(d) + lifecycle B(d)) / (domain_count + 1).

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

*(ROLE MANIFEST, APPLICABILITY MATRIX, and all reviewer sections follow V-01 structure,
with these changes:*
- *BRACKET OPENING: STATUS QUO FRAMING CONTRACT §0-CID values named in §0 Grounding column*
- *CH-ID CHALLENGE TABLE: §0 Grounding cites §0-CID values (TABLE FORMAT CONTRACT schema)*
- *All finding tables: F-ID column per TABLE FORMAT CONTRACT + §14 + §0 requirement*
- *LIFECYCLE section: NH DIMENSION SCORES SUB-TABLE per TABLE FORMAT CONTRACT + §18*
- *BRACKET CLOSING: Charter Coverage Audit (TABLE FORMAT CONTRACT CHARTER COVERAGE AUDIT TABLE) before GClose*
- *ACTION ITEM REGISTER: CHARTER-GAP items if any §0-CID not addressed)*

---

## Predicted scores under v11 rubric

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-32 (base) | PASS | PASS | PASS | PASS | PASS |
| **C-33** Lens Applicability Rating | PASS | PASS | PASS | PASS | PASS |
| **C-34** ADVISORY-GAP Domain Coverage | PASS | PASS | PASS | PASS | PASS |
| **C-35** NH Challenger Dimension Table | PASS | PASS | PASS | PASS | PASS |
| **v11 composite** | **225/225** | **225/225** | **225/225** | **225/225** | **225/225** |

## Candidate criteria evidence (post-225 tracking)

| Candidate | V-01 | V-02 | V-03 | V-04 | V-05 | Mechanism |
|-----------|------|------|------|------|------|-----------|
| C-41 LIFECYCLE NH Score Emission | PASS | PASS | PASS | PASS | PASS | §18 top-level contract; NH sub-table schema; BRACKET CLOSING aggregation formula extended |
| C-42 F-ID Named Field | PASS | PASS | PASS (via §0) | PASS (dual) | PASS (triple) | §14 named column; TABLE FORMAT CONTRACT; §0 auditability requirement |
| C-43 CH-ID §0 Grounding Column | PASS (§§ ref) | PASS (schema) | PASS (§0-CID) | PASS (dual) | PASS (triple: schema+§5+§0) | §5 clause; TABLE FORMAT CONTRACT; §0 §0-CID values |

**R17 leaderboard prediction**:

| Rank | Variant | v11 Score | C-41 | C-42 | C-43 | Axis |
|------|---------|-----------|------|------|------|------|
| 1 (tied) | V-05 | 225/225 | PASS | PASS | PASS | Three-axis (strongest enforcement chain) |
| 1 (tied) | V-04 | 225/225 | PASS | PASS | PASS | Two-axis (dual enforcement) |
| 1 (tied) | V-01 | 225/225 | PASS | PASS | PASS | Lifecycle emphasis |
| 1 (tied) | V-02 | 225/225 | PASS | PASS | PASS | Output format |
| 1 (tied) | V-03 | 225/225 | PASS | PASS | PASS | Inertia framing |

All five variants predict 225/225 under v11. Differentiation is in the enforcement
mechanism robustness for post-225 candidates C-41/C-42/C-43.

**Excellence signal for rubric evolution**: V-05's triple-enforcement path for C-42 and C-43,
combined with the cross-criterion traceability chain (§0-CID -> CH-ID §0 Grounding -> F-ID ->
Charter Coverage Audit -> g_null(final)), represents a structural integration pattern not
present in any single-axis variant. If the next rubric version formalizes C-41/C-42/C-43 with
a "dual enforcement required" pass condition, V-04 and V-05 would be the first variants to
satisfy it.
