---
skill: quest-variate
skill_target: org-review
date: 2026-03-17
round: 11
rubric: org-review-rubric-v11-2026-03-16.md
---

# org-review -- Variate R11

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis and three-axis combinations (V-04, V-05).

**R11 design target**: R10 V-05 combined §0 (dimension table) + §17 (lens applicability
protocol) + §18 (domain coverage gap-check) with an explicit dependency chain and
predicted 225/225. R11 scores R10 against v11 rubric and identifies the mechanisms
by which C-33, C-34, and C-35 still fail at model execution time despite the
protocol text being present.

**Gap analysis from R10 V-05:**

| Criterion | R10 V-05 predicted | Identified failure mode |
|-----------|-------------------|------------------------|
| C-33 Lens Applicability Rating Pre-committed | PASS predicted | §17 says "NOT inherited from role definition" but provides no enforcement. Model writes `HIGH -- this is a technical architecture role reviewing a technical artifact` (role-level generalization). The protocol has no mechanism to reject a rating that cites archetype rather than a specific artifact surface. |
| C-34 ADVISORY-GAP Domain Coverage Pre-committed | PASS predicted (via C-33) | §18 operates on "artifact domains declared in §1 IN-SCOPE" but §1 lists SURFACES, not domains. Model must infer domains from surfaces at §5.8 execution time. Inference is inconsistent -- broad surface labels may silently subsume multiple distinct domains, and the gap-check treats them as one. |
| C-35 Null Hypothesis Challenger Dimension Table | PASS predicted | §0 dimension table is required before challenge claims, but NH TESTIMONY prose in BRACKET OPENING is written after the table with no gate enforcing that only table values carry assessments. Model may introduce qualitative assessments in NH prose that do not trace to any table row, making g_null not derivable from the table alone. |

**R11 variation axes:**

- V-01: Inertia framing (single axis) -- §0 PRE-LOCK GATE. Dimension table must be
  declared complete and emitted with `DIMENSION TABLE LOCKED` sentinel before NH TESTIMONY
  begins. NH TESTIMONY section is labeled "Derived from locked table only"; any assessment
  not traceable to a table row is structurally invalid. C-35 PASS only.

- V-02: Output format (single axis) -- §17a SURFACE CITATION REQUIREMENT. Each Applicability
  row in §5.7 gains a `Basis (§1 citation)` column that names the specific §1 IN-SCOPE
  surface(s) justifying the rating. Generic archetype-level basis is explicitly rejected.
  §17 extended with CITATION VALIDITY RULE. C-33 PASS; C-34 flows from C-33.

- V-03: Lifecycle emphasis (single axis) -- §1a ARTIFACT DOMAIN INVENTORY. Immediately after
  §1 IN-SCOPE enumeration, the model emits an ARTIFACT DOMAIN INVENTORY: a numbered list of
  atomic domain concerns derived from the surfaces. §18 gap-check operates on this locked
  inventory rather than inferring domains from surface labels at execution time.
  C-34 PASS only.

- V-04: Inertia framing + Output format (two-axis) -- V-01 + V-02. §0 pre-lock gate (C-35)
  and §17a surface citation (C-33 -> C-34).

- V-05: Full integration (three-axis) -- V-01 + V-02 + V-03. §0 pre-lock gate (C-35),
  §17a surface citation (C-33), and §1a domain inventory (C-34 with locked source).

**Predicted R11 scores under v11:**
- V-01: C-35 PASS, C-33 FAIL (no surface citation), C-34 vacuous. 215/225
- V-02: C-33 PASS (surface citation), C-34 PASS (gap-check has §17 source data), C-35 FAIL. 220/225
- V-03: C-34 PASS (domain inventory locked), C-33 FAIL, C-35 FAIL. 215/225
- V-04: C-33+C-35 PASS, C-34 PASS via C-33 source. 225/225
- V-05: C-33+C-34+C-35 PASS with strongest enforcement chain. 225/225

---

## V-01

**Axis**: Inertia framing (single axis) -- §0 PRE-LOCK GATE. Dimension table must
emit `DIMENSION TABLE LOCKED` sentinel before NH TESTIMONY begins. NH TESTIMONY is
structurally subordinate to the locked table; no assessments admitted in prose that
are absent from a table row. C-35 PASS; C-33/C-34 unchanged from R10 V-01 baseline.

**Hypothesis**: R10 §0 requires the dimension table before challenge claims, but
allows NH TESTIMONY prose to introduce new qualitative assessments that are not in
the table. Adding a mandatory LOCK sentinel + subordination label means the model
must complete all dimension rows, declare the table complete, and then write NH TESTIMONY
as a derivation of the locked state. Any assessment appearing only in prose is
structurally inadmissible, making g_null derivable from table values alone (C-35).
C-33 and C-34 remain at R10 baseline (§17 without surface citation, §18 present).
Predicted: 215/225.

---

depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. Do not add sections
between pre-printed headers. If a field cannot be filled, write `[N/A -- reason]`.

---

```
==============================================================================
IMMUTABLE PROTOCOL BLOCK -- read all sections before executing any reviewer
==============================================================================

DISPOSITION_CONTRACT v1

§1 -- SCOPE ENUMERATION
[Fill before proceeding. Pre-reviewer gate.]
  IN-SCOPE surfaces: [enumerate exhaustively -- these rows are cited in §5.5]
  OUT-OF-SCOPE: [surface -- reason, or "None"]
  Scope Amendment Protocol: SCOPE AMENDMENT: [surface] added -- [reason]
§1 COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment. No commitment proceeds with open HIGH findings.
  MEDIUM = Conditions commitment. Proceeds only after named resolution.
  LOW    = Advisory. Commitment may proceed.
  These definitions apply universally and may not be restated at any gate.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose = FAIL  [override: null hypothesis holds]
                OR any Gi = FAIL
  CONDITIONAL  <-- no Gi = FAIL  AND  any Gi = CONDITIONAL
  READY        <-- all Gi = PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  If multiple DOMAIN sections: G_domain_agg = worst-case(all G_domain verdicts)
  Worst-case order: FAIL > CONDITIONAL > PASS
  Apply mechanically; do not aggregate editorially.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A missing cite is an audit-trail gap.

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, ...).
  Every downstream section carries a mandatory CH-ID response table.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

==============================================================================

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  (a) Row syntax: | Section | Gate | Verdict | Class |
  (b) Emit at end of each verdict-emitting section, after verdict is stated.
  (c) Assembly rule: copy all local rows to ACTION ITEM REGISTER verbatim.
      Do NOT re-derive Gate Verdict or Class. The register is a copy, not
      a synthesis.
  Excluded sections (emit NO local ledger row):
    §3.5 Domain-Aggregate Checkpoint -- produces no verdict
    §3.8 CH-ID Saturation Check -- produces no verdict
    §5.5 Scope Coverage Reconciliation -- informational only
    §5.7 Lens Coverage Table -- informational only
    §5.8 Domain Coverage Gap-Check -- produces no verdict

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical execution sequence:
  §0 Challenger Pre-Gate -> Role Manifest -> Bracket Opening -> Domain(s) ->
  §3.5 Domain-Aggregate Checkpoint -> §3.8 CH-ID Saturation Check ->
  §5.7 Lens Coverage Table -> §5.8 Domain Coverage Gap-Check ->
  Lifecycle -> Bracket Closing ->
  §5.5 Scope Coverage Reconciliation -> Gate Vector Table ->
  Cross-Role Signals -> Disposition -> Action Item Register
  Reordering is a contract violation.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED      = every CH-ID has >=1 response from a DOMAIN section
                   (verified at §3.8 before LIFECYCLE executes)
  FULLY SATURATED = every CH-ID has domain + lifecycle response
                   (verified at BRACKET CLOSING before GClose is stated)
  §3.8 SATURATION CHECK gate: LIFECYCLE does not begin until SATURATED.
  BRACKET CLOSING: PASS verdict prohibited if any CH-ID is UNSATURATED
  without a stated waiver citing the specific CH-ID and justification.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial)     = GOpen
  Stage 2: g_null(post-domain) = worst-case(G_domain_agg, g_null(initial))
  Stage 3: g_null(final)       = worst-case(G_lifecycle, g_null(post-domain))
  GClose must equal g_null(final). Deviation requires explicit override with
  named justification. All three g_null values emitted as labeled fields at
  their respective checkpoints and summarized in Cross-Role Signals.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 SCOPE COVERAGE RECONCILIATION executes after BRACKET CLOSING.
  Maps each §1 IN-SCOPE surface to reviewer findings.
  COVERED = surface appears in >=1 finding.
  GAP     = no finding references this surface -> forced LOW advisory ->
            appended to ACTION ITEM REGISTER as ADVISORY-GAP.
  §5.5 emits COVERED/PARTIAL signal (informational only, no ledger row,
  excluded from §3 gate formula).

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Every finding row in every reviewer section carries an individual
  Severity field (HIGH / MEDIUM / LOW).
  Section Severity = worst(Severity of F-1, F-2, ...) over all findings
  in that section. Derived mechanically; no editorial section-level
  severity assignment permitted.
  Local gate ledger row carries the derived Section Severity.

§15 -- LENS EXHAUSTION PROTOCOL [IMMUTABLE]
  §5.7 LENS COVERAGE TABLE executes after all DOMAIN sections and before
  LIFECYCLE. For each active reviewer role: ALL lens.verify entries from
  that role's definition must appear in the table.
  Status per entry: ADDRESSED (>=1 finding references this dimension)
                 or OPEN (no finding referenced this dimension).
  OPEN entries -> automatically promoted to ADVISORY-OPEN-LENS items in
  ACTION ITEM REGISTER.
  §5.7 emits no gate verdict and no local ledger row (excluded from §6).

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  After all gate verdicts are known, apply the following precedence rules
  in order to select exactly one gate as PRIMARY DRIVER of DISPOSITION:
  Rule 1: If GClose = FAIL -> PRIMARY DRIVER = GClose
  Rule 2: If any other Gi = FAIL -> PRIMARY DRIVER = first FAIL gate in
          canonical order (GOpen, G_domain_agg, G_lifecycle)
  Rule 3: If GClose = CONDITIONAL -> PRIMARY DRIVER = GClose
  Rule 4: If G_lifecycle = CONDITIONAL -> PRIMARY DRIVER = G_lifecycle
  Rule 5: If G_domain_agg = CONDITIONAL -> PRIMARY DRIVER = G_domain_agg
  Rule 6: If GOpen = CONDITIONAL -> PRIMARY DRIVER = GOpen
  Rule 7: If all Gi = PASS -> PRIMARY DRIVER = GClose (final confirming gate)
  PRIMARY DRIVER emitted as labeled field at DISPOSITION. Derivable from
  gate verdict values alone without reading reviewer narrative.

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  Each row in the LENS COVERAGE TABLE (§5.7) carries an Applicability rating
  specific to the artifact under review:
    HIGH   = lens dimension is directly relevant to the artifact's primary concerns
    MEDIUM = partial or indirect relevance to the artifact
    LOW    = minimal relevance to the artifact type
  Applicability rating is artifact-specific -- NOT inherited from role definition;
  the same role reviewing a different artifact may carry a different rating.
  Rating is assigned at table-population time based on the artifact under review.
  Coverage expectation by tier:
    HIGH-applicability: ADDRESSED required; OPEN -> ADVISORY-OPEN-LENS
    MEDIUM-applicability: ADDRESSED preferred; OPEN -> ADVISORY-LOW (lower urgency)
    LOW-applicability: OPEN acceptable; no ADVISORY-OPEN-LENS triggered
  §17 must be complete before §18 executes (§18 references §17 Applicability
  tiers as its source data).

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  After §5.7 LENS COVERAGE TABLE is populated (including Applicability ratings
  from §17), execute §5.8 DOMAIN COVERAGE GAP-CHECK:
  For each artifact domain declared in §1 IN-SCOPE:
    Identify the maximum Applicability tier among all reviewers whose
    lens dimensions cover that domain.
    COVERED      = at least one reviewer has HIGH applicability to this domain
    ADVISORY-GAP = highest tier is MEDIUM or LOW only, or no reviewer covers domain
  Each ADVISORY-GAP domain must be appended to ACTION ITEM REGISTER with:
    - Domain name (from §1)
    - Highest applicability tier found (or "none")
    - Reason no HIGH-applicability reviewer covers it
    - Disposition class: ADVISORY-GAP
  §5.8 emits no gate verdict and no local ledger row (excluded from §6).
  §18 requires §17 Applicability ratings; §17 must be complete before §18 executes.

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  The challenger's null hypothesis evaluation in BRACKET OPENING uses a structured
  dimension comparison table. The protocol has two phases:

  PHASE 1 -- TABLE POPULATION:
    Complete all dimension rows before writing any NH TESTIMONY prose.
    Table columns: Dimension | Current-State Score | Proposed-State Score |
                   Differential | Per-Dim Verdict
    Minimum 2 dimensions required.
    Per-Dim Verdict: BUILD-WINS / STATUS-QUO-WINS / TIED
    Current-State Score and Proposed-State Score: numeric (0-10) or labeled
    (HIGH/MEDIUM/LOW/NONE).

  PHASE 2 -- TABLE LOCK:
    After all dimension rows are complete, emit: DIMENSION TABLE LOCKED
    This sentinel is required before NH TESTIMONY may begin.
    NH TESTIMONY is structurally subordinate to the locked table.
    Any assessment appearing only in NH TESTIMONY prose that is absent from
    a table row is structurally inadmissible for g_null derivation.

  g_null(initial) derivation rule (applied to table values only):
    BUILD-WINS majority -> g_null(initial) candidate = PASS
    STATUS-QUO-WINS majority -> g_null(initial) candidate = FAIL
    Mixed or TIED majority -> g_null(initial) candidate = CONDITIONAL
  GOpen must be consistent with the §0 table derivation. A GOpen that
  contradicts the table majority requires a named justification citing the
  specific dimension(s) that override the majority.
  Distinct from C-16 alternatives table: C-16 operates at the bracket-wide
  scenario-comparison level (Status Quo / Build / Hybrid) and is re-scored
  by domain reviewers. §0 operates at the null hypothesis evaluation level
  only and is populated by the challenger before domain sections run.

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot.

Review Parameters:
- Artifact: {{artifact_id}}
- Depth: {{depth}}
- Reviewer set: {{reviewer_set}}

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3. CHALLENGER positions remain fixed.
State total count.)*

---

## §0 -- CHALLENGER PRE-GATE: NULL HYPOTHESIS DIMENSION TABLE

Contract: DISPOSITION_CONTRACT v1

*(Per §0 PHASE 1: populate all dimension rows before writing NH TESTIMONY.)*

**Null Hypothesis Dimension Comparison Table**:

| Dimension | Current-State Score | Proposed-State Score | Differential | Per-Dim Verdict |
|-----------|--------------------|--------------------|--------------|-----------------|
| [DIM_1 -- e.g., switching cost for team] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_2 -- e.g., value delivered without building] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_3 -- optional] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |

**§0 Table Majority**: [BUILD-WINS / STATUS-QUO-WINS / TIED -- count Per-Dim Verdicts]
**g_null(initial) candidate from §0**: [PASS / CONDITIONAL / FAIL -- derived from majority rule]

**DIMENSION TABLE LOCKED**
*(Per §0 PHASE 2: all dimension rows complete. NH TESTIMONY follows. Any assessment
below not traceable to a row above is structurally inadmissible for g_null derivation.)*

**NH TESTIMONY** *(Derived from locked table only)*:
[One paragraph summarizing what the dimension table shows about null hypothesis strength.
Do not introduce new assessments. Reference table row verdicts by dimension name.]

*(If GOpen contradicts the §0 table candidate, state the override justification below.
Otherwise GOpen must equal the §0-derived candidate.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table** *(per C-16 -- bracket-wide shared scaffold; re-scored
by domain reviewers; aggregated at BRACKET CLOSING)*:

| Dimension | Status Quo | Build | Hybrid |
|-----------|-----------|-------|--------|
| [DIM_A] | [score] | [score] | [score] |
| [DIM_B] | [score] | [score] | [score] |
| [DIM_C] | [score] | [score] | [score] |
| **Total** | [sum] | [sum] | [sum] |

**NULL HYPOTHESIS DERIVATION RULE**: Build beats Status Quo (B > A) AND
Build beats Hybrid (B > C) -> g_null = PASS. One condition fails -> CONDITIONAL.
Both fail -> FAIL. Apply mechanically using table totals above.

**Challenge claims** *(assign CH-IDs; carry to every downstream section per §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL -- must equal §0 candidate or state override]
**GOpen Reason**: [One sentence. If overriding §0 candidate: name the overriding dimension(s).]
**g_null(initial)**: [copy GOpen verdict -- Stage 1 of §9 progression]

*Local Gate Ledger Row*: | BRACKET OPENING | GOpen | [verdict] | [class per §6] |

*GOpen and all CH-IDs carry forward to every downstream section.*

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]

**CH-ID Response Table** *(mandatory per §5 -- PASS verdict prohibited if any row OPEN)*:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

*(PARTIAL requires named resolution path. OPEN = unanswerable from this role's frame.)*

**Alternatives Re-score** *(per C-16 -- re-score same dimensions from this role's frame)*:

| Dimension | Status Quo | Build | Hybrid |
|-----------|-----------|-------|--------|
| [DIM_A] | [re-score] | [re-score] | [re-score] |
| [DIM_B] | [re-score] | [re-score] | [re-score] |
| [DIM_C] | [re-score] | [re-score] | [re-score] |
| **Total** | [sum] | [sum] | [sum] |

**Additional Findings**:

| F-ID | Finding | Severity |
|------|---------|---------|
| F-01 | [FINDING from this role's `lens.verify` and `expertise.depth`. Names an in-scope surface.] | [HIGH / MEDIUM / LOW] |
| F-02 | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-03 | [FINDING_3 -- optional] | [HIGH / MEDIUM / LOW] |
| F-04 | [FINDING_4 -- optional] | [HIGH / MEDIUM / LOW] |

**Section Severity** *(per §14 formula: worst(F-01, F-02, ...))*: [HIGH / MEDIUM / LOW]
**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*(For `--depth deep`: repeat labeled DOMAIN-2, DOMAIN-3. State G_domain Aggregate
explicitly below per §3a.)*

**G_domain Aggregate** *(per §3a)*: [PASS / CONDITIONAL / FAIL -- worst among all DOMAIN rows]

*Local Gate Ledger Row*: | DOMAIN | G_domain | [verdict] | [class per §6] |

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

*(Informational only -- no verdict, no local ledger row per §6 exclusion list.)*

**G_domain Aggregate confirmed**: [copy from DOMAIN section]
**g_null(post-domain)** *(per §9 Stage 2: worst-case(G_domain_agg, g_null(initial)))*:
[PASS / CONDITIONAL / FAIL]

---

## §3.8 -- CH-ID SATURATION CHECK

*(Informational only -- no verdict, no local ledger row per §6 exclusion list.)*
*(LIFECYCLE does not begin until SATURATED confirmed per §8.)*

| CH-ID | DOMAIN Response Status | SATURATED? |
|-------|----------------------|-----------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN from DOMAIN] | [YES / NO] |
| CH-002 | [copy] | [YES / NO] |
| CH-003 | [copy if active] | [YES / NO] |

**Saturation status**: [SATURATED / UNSATURATED]
*(If UNSATURATED: state waiver with specific CH-ID and justification, or resolve
before proceeding to LIFECYCLE.)*

---

## §5.7 -- LENS COVERAGE TABLE

*(Produced after all DOMAIN sections complete, before LIFECYCLE. Per §15: ALL
lens.verify entries from each active role must appear. Per §17: each row carries
an Applicability rating specific to this artifact.)*

*(Informational only -- no gate verdict, no local ledger row per §6 exclusion list.)*

| Role | Lens Dimension | Applicability | Status | ADVISORY-OPEN-LENS? |
|------|---------------|--------------|--------|---------------------|
| [ROLE] | [lens.verify entry 1] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN / NO] |
| [ROLE] | [lens.verify entry 2] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN / NO] |
| [LIFECYCLE_ROLE] | [lens.verify entry] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN / NO] |

*(All ADVISORY-OPEN-LENS entries -- rows where Applicability=HIGH and Status=OPEN --
appear in ACTION ITEM REGISTER as ADVISORY-OPEN-LENS items per §15.)*

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

*(Executes after §5.7 per §18. Maps §1 IN-SCOPE domains to reviewer HIGH-applicability
coverage. Informational only -- no gate verdict, no local ledger row per §6.)*

| Artifact Domain (from §1) | Max Applicability Tier Among Reviewers | Gap Status | Disposition |
|--------------------------|---------------------------------------|------------|-------------|
| [DOMAIN_1] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [-- / ADVISORY-GAP -> ACTION REGISTER] |
| [DOMAIN_2] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [-- / ADVISORY-GAP -> ACTION REGISTER] |

*(ADVISORY-GAP rows are appended to ACTION ITEM REGISTER per §18.)*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]
Received G_domain Aggregate: [copy from §3.5]
Saturation confirmed: [SATURATED -- per §3.8]

**CH-ID Response Table** *(mandatory per §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [Is evidence sufficient for commitment given both
received verdicts? One paragraph referencing GOpen and G_domain Aggregate explicitly.]

**Null hypothesis status**: [Given GOpen and G_domain_agg, has the null hypothesis been
defeated? yes / partial / no -- one sentence of justification.]

**Additional Findings**:

| F-ID | Finding | Severity |
|------|---------|---------|
| F-01 | [FINDING from this role's `lens.verify`. Commitment, program, or decision concerns.] | [HIGH / MEDIUM / LOW] |
| F-02 | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Section Severity** *(per §14: worst(F-01, F-02, ...))*: [HIGH / MEDIUM / LOW]
**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

*Local Gate Ledger Row*: | LIFECYCLE | G_lifecycle | [verdict] | [class per §6] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: scope declaration, all CH-ID tables, all gate verdicts.*

Received G_domain Aggregate: [copy]
Received G_lifecycle: [copy]

**Alternatives Aggregated Table** *(per C-16 -- aggregate domain re-scores)*:

| Dimension | Status Quo (agg) | Build (agg) | Hybrid (agg) |
|-----------|-----------------|-------------|--------------|
| [DIM_A] | [aggregated] | [aggregated] | [aggregated] |
| [DIM_B] | [aggregated] | [aggregated] | [aggregated] |
| [DIM_C] | [aggregated] | [aggregated] | [aggregated] |
| **Total** | [sum] | [sum] | [sum] |

**NULL HYPOTHESIS DERIVATION RULE applied**: [Apply same rule stated in BRACKET OPENING
to aggregated totals -> derived g_null verdict]

**CH-ID Full Saturation Check** *(per §8 FULLY SATURATED requirement)*:

| CH-ID | G_domain Status | G_lifecycle Status | FULLY SATURATED? |
|-------|----------------|-------------------|-----------------|
| CH-001 | [copy from DOMAIN] | [copy from LIFECYCLE] | [YES / NO] |
| CH-002 | [copy] | [copy] | [YES / NO] |
| CH-003 | [copy if active] | [copy] | [YES / NO] |

*(PASS verdict prohibited if any CH-ID is not FULLY SATURATED without waiver.)*

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [NOTE] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [NOTE] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [NOTE] |

**Remaining gaps**: [What was not fully addressed. If none: "None -- all CH-IDs DEFEATED."]

**Override invoked**: [YES / NO]
*(If YES: state justification and which gate verdict is being overridden.)*

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
- PASS (DEFEATED): All CH-IDs DEFEATED -- null hypothesis defeated.
- CONDITIONAL (PARTIAL): Some CH-IDs PARTIAL -- material gaps remain.
- FAIL (HOLDS): At least one CH-ID HOLDS -- null hypothesis survives.
**GClose override authority**: GClose = FAIL overrides all prior gate verdicts per §3.

**GClose Rationale**: [2-3 sentences.]
**g_null(final)** *(per §9 Stage 3: worst-case(G_lifecycle, g_null(post-domain)))*:
[PASS / CONDITIONAL / FAIL -- GClose must equal this or state override]

*Local Gate Ledger Row*: | BRACKET CLOSING | GClose | [verdict] | [class per §6] |

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

*(Executes after BRACKET CLOSING per §10. Informational only -- no ledger row.)*

| §1 IN-SCOPE Surface | Coverage Status | Finding Reference |
|---------------------|----------------|-------------------|
| [SURFACE_1] | [COVERED / GAP] | [finding F-ID or "none"] |
| [SURFACE_2] | [COVERED / GAP] | [finding F-ID or "none"] |
| [SURFACE_3] | [COVERED / GAP] | [finding F-ID or "none"] |

GAP surfaces -> appended to ACTION ITEM REGISTER as ADVISORY-GAP items per §10.
**§5.5 Signal**: [COVERED (all surfaces) / PARTIAL (gaps present)]

---

## GATE VECTOR TABLE

*(Assembled verbatim from local ledger rows per §6(c).)*

| Gate | Section | Verdict | Contract Cite |
|------|---------|---------|---------------|
| GOpen | BRACKET OPENING | [copy] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | DOMAIN (aggregate per §3a) | [copy] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | LIFECYCLE | [copy] | DISPOSITION_CONTRACT v1 |
| GClose | BRACKET CLOSING | [copy] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**g_null Progression Ledger** *(per §9)*:
```
g_null(initial)     = [copy from BRACKET OPENING]   [Stage 1: = GOpen]
g_null(post-domain) = [copy from §3.5]              [Stage 2: worst-case(G_domain_agg, Stage 1)]
g_null(final)       = [copy from BRACKET CLOSING]   [Stage 3: worst-case(G_lifecycle, Stage 2)]
Trajectory: [e.g., PASS -> PASS -> PASS]
```

**Conflicts**: [Two reviewers with incompatible responses or findings -- name roles and
tension. If none: "None detected."]

**Convergence**: [Any concern named independently by two or more reviewers -- name it
and state why it is the highest-confidence signal.]

**Scope coverage**: [Any in-scope surface from §1 not covered by any reviewer. If all
covered: "None -- full in-scope surface reviewed." (detail in §5.5)]

---

## DISPOSITION

**Gate vector** *(from GATE VECTOR TABLE)*:
- GOpen         = [copy]
- G_domain_agg  = [copy]
- G_lifecycle   = [copy]
- GClose        = [copy]

**Apply §3 formula** *(do not alter; evaluate gate vector mechanically)*:
```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL?              --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL?        --> BLOCKED
No FAIL, any CONDITIONAL?   --> CONDITIONAL
All PASS?                   --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Primary Driver** *(per §16 precedence formula)*: [Gate name -- derived mechanically]

**Conditions** *(if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]
2. [Additional conditions if present.]

**Blocker** *(if BLOCKED)*: [Specific finding. If GClose = FAIL, lead with:
"Challenger final verdict HOLDS -- [GClose Rationale summary]."]

---

## ACTION ITEM REGISTER

*(CH-ID-sourced rows assembled verbatim from local gate ledger rows per §6(c).
ADVISORY-OPEN-LENS rows from §5.7 per §15. ADVISORY-GAP rows from §5.5 per §10 and
from §5.8 per §18. Do not re-derive.)*

| CH-ID / Source | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|---------------|-----------------|------------------|------------|---------------------|
| CH-001 | [derived from PARTIAL or HOLDS status] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE] | [Falsifiable criterion] |
| CH-002 | [Item 2] | [class] | [ROLE] | [Criterion] |
| ADVISORY-OPEN-LENS | [lens dimension not covered in review] | ADVISORY-OPEN-LENS | [ROLE] | [When ADDRESSED] |
| ADVISORY-GAP | [§1 surface with no reviewer finding] | ADVISORY-GAP | [ROLE] | [When COVERED] |
| ADVISORY-GAP | [domain with no HIGH-applicability reviewer per §5.8] | ADVISORY-GAP | [ROLE] | [When covered by HIGH reviewer] |
| ADVISORY-OBS | [advisory observation not sourced from CH-ID] | ADVISORY-OBS | [ROLE] | [Criterion] |

*Disposition class per §2: BLOCKED = must resolve before any commitment.
CONDITIONAL = must resolve before next lifecycle phase. ADVISORY = may defer.*

---

**Artifact to review:**

{{artifact}}

---

## V-02

**Axis**: Output format (single axis) -- §17a SURFACE CITATION REQUIREMENT. §17
extended with a CITATION VALIDITY RULE: each Applicability row in §5.7 must include
a `Basis (§1 citation)` column naming the specific §1 IN-SCOPE surface(s) justifying
the rating. Generic role-archetype basis is explicitly invalid. C-33 PASS; C-34 flows
from C-33 source data. C-35 unchanged (§0 dimension table present but no LOCK gate).

**Hypothesis**: R10 §17 says ratings must be "NOT inherited from role definition" but
provides no mechanism to enforce artifact-specificity at the row level. Adding a
mandatory `Basis (§1 citation)` column forces the model to name a §1 surface for each
row. A rating that cites "technical architecture role" rather than "§1.2: authentication
boundary decision" is structurally invalid per the CITATION VALIDITY RULE. C-33 PASS
because the applicability rating is now the rated basis for ADDRESSED/OPEN, derived from
named artifact surfaces. C-34 follows because §18 can now identify domains with no
HIGH-applicability row. C-35 remains FAIL (§0 has no LOCK gate). Predicted: 220/225.

---

depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. Do not add sections
between pre-printed headers. If a field cannot be filled, write `[N/A -- reason]`.

---

```
==============================================================================
IMMUTABLE PROTOCOL BLOCK -- read all sections before executing any reviewer
==============================================================================

[§1 through §5 DISPOSITION_CONTRACT v1 -- identical to V-01]
[§3a DOMAIN-AGGREGATE FORMULA -- identical to V-01]
[§6 LOCAL GATE LEDGER PROTOCOL -- identical to V-01]
[§7 SECTION ORDER CONTRACT -- identical to V-01]
[§8 CH-ID SATURATION REQUIREMENT -- identical to V-01]
[§9 NULL HYPOTHESIS PROGRESSION CONTRACT -- identical to V-01]
[§10 SCOPE COVERAGE GATE PROTOCOL -- identical to V-01]
[§14 PER-FINDING SEVERITY CHAIN -- identical to V-01]
[§15 LENS EXHAUSTION PROTOCOL -- identical to V-01]
[§16 PRIMARY DRIVER DERIVATION CONTRACT -- identical to V-01]

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  Each row in the LENS COVERAGE TABLE (§5.7) carries an Applicability rating
  specific to the artifact under review:
    HIGH   = lens dimension is directly relevant to the artifact's primary concerns
    MEDIUM = partial or indirect relevance to the artifact
    LOW    = minimal relevance to the artifact type
  Applicability rating is artifact-specific -- NOT inherited from role definition;
  the same role reviewing a different artifact may carry a different rating.
  Rating is assigned at table-population time based on the artifact under review.

  §17a -- CITATION VALIDITY RULE [IMMUTABLE]
    Each Applicability row must include a `Basis (§1 citation)` column.
    The Basis must name at least one specific §1 IN-SCOPE surface (by surface
    number and label) that justifies the applicability rating.
    VALID basis format: "§1.N: [surface label] -- [one sentence why]"
    INVALID basis format: any statement that cites only the role archetype
    (e.g., "this is a technical role" or "artifact is technical") without
    naming a §1 surface. An INVALID basis is treated as MISSING and the row
    is classified as ADVISORY-OPEN-LENS regardless of stated Status.

  Coverage expectation by tier:
    HIGH-applicability: ADDRESSED required; OPEN -> ADVISORY-OPEN-LENS
    MEDIUM-applicability: ADDRESSED preferred; OPEN -> ADVISORY-LOW
    LOW-applicability: OPEN acceptable; no ADVISORY-OPEN-LENS triggered
  §17 must be complete before §18 executes.

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  [Identical to V-01 §18 -- operates on §17 Applicability tiers after §17 complete]

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  [Identical to V-01 §0 PHASE 1 only -- dimension table required before challenge
  claims. NOTE: §0 PHASE 2 (DIMENSION TABLE LOCKED sentinel and subordination label)
  is NOT present in V-02. NH TESTIMONY may be written without the LOCK gate.]

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

[Identical structure to V-01.]

---

## §0 -- CHALLENGER PRE-GATE: NULL HYPOTHESIS DIMENSION TABLE

Contract: DISPOSITION_CONTRACT v1

*(Per §0: populate all dimension rows before writing NH TESTIMONY.)*

**Null Hypothesis Dimension Comparison Table**:

| Dimension | Current-State Score | Proposed-State Score | Differential | Per-Dim Verdict |
|-----------|--------------------|--------------------|--------------|-----------------|
| [DIM_1] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_2] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_3 -- optional] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |

**§0 Table Majority**: [BUILD-WINS / STATUS-QUO-WINS / TIED]
**g_null(initial) candidate from §0**: [PASS / CONDITIONAL / FAIL]

*(DIMENSION TABLE LOCKED sentinel not present in V-02. NH TESTIMONY prose begins here.)*

---

## BRACKET OPENING -- CHALLENGER

[Identical to V-01 -- null hypothesis, alternatives table, CH-IDs, GOpen, ledger row.]

---

## DOMAIN -- [ROLE_NAME]

[Identical to V-01 DOMAIN template.]

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

[Identical to V-01.]

---

## §3.8 -- CH-ID SATURATION CHECK

[Identical to V-01.]

---

## §5.7 -- LENS COVERAGE TABLE

*(Per §15 and §17 with §17a CITATION VALIDITY RULE: each row carries Applicability
AND a Basis (§1 citation) column. A basis that does not name a §1 surface is INVALID
and the row is treated as ADVISORY-OPEN-LENS.)*

*(Informational only -- no gate verdict, no local ledger row per §6 exclusion list.)*

| Role | Lens Dimension | Applicability | Basis (§1 citation) | Status | ADVISORY-OPEN-LENS? |
|------|---------------|--------------|---------------------|--------|---------------------|
| [ROLE] | [lens.verify entry 1] | [HIGH / MEDIUM / LOW] | [§1.N: surface label -- one sentence] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN or INVALID basis / NO] |
| [ROLE] | [lens.verify entry 2] | [HIGH / MEDIUM / LOW] | [§1.N: surface label -- one sentence] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN or INVALID basis / NO] |
| [LIFECYCLE_ROLE] | [lens.verify entry] | [HIGH / MEDIUM / LOW] | [§1.N: surface label -- one sentence] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN or INVALID basis / NO] |

*(ADVISORY-OPEN-LENS triggered by: Applicability=HIGH AND Status=OPEN, OR Basis=INVALID.)*

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

[Identical to V-01 §5.8 -- operates on §5.7 Applicability tiers from §17.]

---

## LIFECYCLE -- [ROLE_NAME]

[Identical to V-01 LIFECYCLE template.]

---

## BRACKET CLOSING -- CHALLENGER

[Identical to V-01 BRACKET CLOSING template.]

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

[Identical to V-01.]

---

## GATE VECTOR TABLE

[Identical to V-01.]

---

## CROSS-ROLE SIGNALS

[Identical to V-01.]

---

## DISPOSITION

[Identical to V-01.]

---

## ACTION ITEM REGISTER

*(CH-ID-sourced rows + ADVISORY-OPEN-LENS from §5.7 (including INVALID-BASIS rows) +
ADVISORY-GAP from §5.5 and §5.8. Identical structure to V-01.)*

[Identical to V-01.]

---

**Artifact to review:**

{{artifact}}

---

## V-03

**Axis**: Lifecycle emphasis (single axis) -- §1a ARTIFACT DOMAIN INVENTORY. Immediately
after §1 IN-SCOPE surfaces are enumerated, emit an ARTIFACT DOMAIN INVENTORY: a numbered
list of atomic domain concerns distilled from the surfaces, locked before any reviewer
section executes. §18 gap-check operates on this locked inventory rather than inferring
domains from surface labels at §5.8 execution time. C-34 PASS; C-33/C-35 unchanged.

**Hypothesis**: R10 §18 says "for each artifact domain declared in §1 IN-SCOPE" -- but
§1 lists surfaces, not domains. The model must infer domains from surfaces at §5.8 time,
which is late-binding and inconsistent: a surface like "rate-limit enforcement logic" may
be classified as one domain (performance) or two (rate-limiting + error propagation)
depending on model state. §1a pre-locks the domain inventory at scope time, before any
reviewer section runs. §18 then references an explicit inventory rather than inferring
domains on the fly. C-34 PASS because domains are pre-committed. C-33 FAIL (no surface
citation in §17). C-35 FAIL (no LOCK gate in §0). Predicted: 215/225.

---

depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. Do not add sections
between pre-printed headers. If a field cannot be filled, write `[N/A -- reason]`.

---

```
==============================================================================
IMMUTABLE PROTOCOL BLOCK -- read all sections before executing any reviewer
==============================================================================

[§1 through §5 DISPOSITION_CONTRACT v1 -- with §1a addition, see below]
[§3a through §16 -- identical to V-01]
[§17 LENS APPLICABILITY PROTOCOL -- identical to V-01 (no §17a citation rule)]
[§18 DOMAIN COVERAGE GAP-CHECK -- modified to reference §1a inventory, see below]
[§0 CHALLENGER NULL HYPOTHESIS DIMENSION TABLE -- §0 PHASE 1 only, identical to V-02
 (no DIMENSION TABLE LOCKED sentinel / PHASE 2)]

§1a -- ARTIFACT DOMAIN INVENTORY PROTOCOL [IMMUTABLE]
  Immediately after §1 IN-SCOPE enumeration is complete and before ROLE MANIFEST,
  emit an ARTIFACT DOMAIN INVENTORY:
  (a) Derive a minimal set of atomic domain concerns from the §1 IN-SCOPE surfaces.
      Each domain is a distinct type of concern (e.g., security, performance,
      data integrity, user experience). A domain is atomic if it cannot be split
      into two concerns that would require different reviewer expertise.
  (b) Number each domain: DOMAIN-1, DOMAIN-2, ...
  (c) For each domain, name at least one §1 surface that belongs to it.
  (d) Emit: ARTIFACT DOMAIN INVENTORY LOCKED
      This sentinel locks the inventory. §18 operates on these labeled domains only.
      Domain labels may not be created or altered after the LOCKED sentinel.
  §1a executes once, before any reviewer section. The locked inventory is the source
  of truth for §18 -- §18 does not re-infer domains from surfaces at execution time.

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  After §5.7 LENS COVERAGE TABLE is populated (including Applicability ratings from §17),
  execute §5.8 DOMAIN COVERAGE GAP-CHECK using the §1a ARTIFACT DOMAIN INVENTORY:
  For each DOMAIN-N in the locked §1a inventory:
    Identify the maximum Applicability tier among all reviewers whose lens dimensions
    cover that domain.
    COVERED      = at least one reviewer has HIGH applicability to DOMAIN-N
    ADVISORY-GAP = highest tier is MEDIUM or LOW, or no reviewer covers DOMAIN-N
  Each ADVISORY-GAP domain must be appended to ACTION ITEM REGISTER with:
    - Domain label (DOMAIN-N name from §1a inventory)
    - Highest applicability tier found (or "none")
    - Reason no HIGH-applicability reviewer covers it
    - Disposition class: ADVISORY-GAP
  §5.8 emits no gate verdict and no local ledger row (excluded from §6).
  §18 references §1a inventory as locked source; §17 as applicability source.

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

[Identical structure to V-01.]

---

## §1a -- ARTIFACT DOMAIN INVENTORY

*(Executed after §1 IN-SCOPE enumeration, before ROLE MANIFEST. Per §1a protocol:
derive atomic domains from §1 surfaces, lock before any reviewer runs.)*

| Domain ID | Domain Name | Atomic Concern | §1 Surface(s) |
|-----------|-------------|---------------|---------------|
| DOMAIN-1 | [e.g., Security boundaries] | [one sentence distinguishing from other domains] | [§1.N, §1.M] |
| DOMAIN-2 | [e.g., Performance envelope] | [one sentence] | [§1.P] |
| DOMAIN-3 | [optional] | [one sentence] | [§1.Q] |

**ARTIFACT DOMAIN INVENTORY LOCKED**
*(Domain labels above are fixed. §18 operates on DOMAIN-1, DOMAIN-2, ... only.)*

---

## §0 -- CHALLENGER PRE-GATE: NULL HYPOTHESIS DIMENSION TABLE

[Identical to V-02 §0 -- dimension table without DIMENSION TABLE LOCKED sentinel.]

---

## BRACKET OPENING -- CHALLENGER

[Identical to V-01.]

---

## DOMAIN -- [ROLE_NAME]

[Identical to V-01 DOMAIN template.]

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

[Identical to V-01.]

---

## §3.8 -- CH-ID SATURATION CHECK

[Identical to V-01.]

---

## §5.7 -- LENS COVERAGE TABLE

*(Per §15 and §17. Identical column structure to V-01 -- Applicability present,
no §17a Basis citation column. Applicability rating per row, artifact-specific.)*

| Role | Lens Dimension | Applicability | Status | ADVISORY-OPEN-LENS? |
|------|---------------|--------------|--------|---------------------|
| [ROLE] | [lens.verify entry 1] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN / NO] |
| [ROLE] | [lens.verify entry 2] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN / NO] |
| [LIFECYCLE_ROLE] | [lens.verify entry] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN / NO] |

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

*(Per §18 modified: operates on §1a ARTIFACT DOMAIN INVENTORY (locked), not §1 surfaces.)*

*(Informational only -- no gate verdict, no local ledger row per §6.)*

| Domain (§1a ID + Name) | Max Applicability Among Reviewers | Gap Status | Disposition |
|------------------------|----------------------------------|------------|-------------|
| DOMAIN-1: [name] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [-- / ADVISORY-GAP -> ACTION REGISTER] |
| DOMAIN-2: [name] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [-- / ADVISORY-GAP -> ACTION REGISTER] |
| DOMAIN-3: [name if active] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [-- / ADVISORY-GAP -> ACTION REGISTER] |

*(ADVISORY-GAP rows appended to ACTION ITEM REGISTER per §18.)*

---

## LIFECYCLE -- [ROLE_NAME]

[Identical to V-01 LIFECYCLE template.]

---

## BRACKET CLOSING -- CHALLENGER

[Identical to V-01.]

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

[Identical to V-01.]

---

## GATE VECTOR TABLE

[Identical to V-01.]

---

## CROSS-ROLE SIGNALS

[Identical to V-01.]

---

## DISPOSITION

[Identical to V-01.]

---

## ACTION ITEM REGISTER

[Identical to V-01 -- ADVISORY-GAP rows from §5.8 reference §1a domain IDs.]

---

**Artifact to review:**

{{artifact}}

---

## V-04

**Axis**: Inertia framing + Output format (two-axis combination) -- V-01 §0 PHASE 2
(DIMENSION TABLE LOCKED sentinel) + V-02 §17a SURFACE CITATION REQUIREMENT. No §1a
domain inventory. C-35 PASS (lock gate), C-33 PASS (surface citation), C-34 PASS
(follows from C-33 source data). All three criteria targeted.

**Hypothesis**: V-01 fixes C-35 by locking the dimension table before NH TESTIMONY.
V-02 fixes C-33 by requiring §1 surface citation in each Applicability row, which
makes §17 Applicability ratings artifact-specific evidence (not generic). C-34 follows
because §18 now has HIGH-applicability rows with valid artifact-specific basis.
The combination of dimension pre-lock and surface citation addresses the two independent
failure modes without requiring §1a domain inventory. Predicted: 225/225.

---

depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. Do not add sections
between pre-printed headers. If a field cannot be filled, write `[N/A -- reason]`.

---

```
==============================================================================
IMMUTABLE PROTOCOL BLOCK -- read all sections before executing any reviewer
==============================================================================

[§1 through §5 DISPOSITION_CONTRACT v1 -- identical to V-01]
[§3a through §16 -- identical to V-01]

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  [Base §17 identical to V-01]

  §17a -- CITATION VALIDITY RULE [IMMUTABLE]
    [Identical to V-02 §17a -- Basis (§1 citation) column required per row;
    archetype-only basis is INVALID and triggers ADVISORY-OPEN-LENS regardless
    of stated Status.]

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  [Identical to V-01 §18 -- operates on §1 IN-SCOPE domains,
  references §17 Applicability tiers (now backed by §17a valid citations).]

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  [PHASE 1 identical to V-01]

  PHASE 2 -- TABLE LOCK [IMMUTABLE]:
    [Identical to V-01 §0 PHASE 2 -- DIMENSION TABLE LOCKED sentinel required
    before NH TESTIMONY; NH TESTIMONY is subordinate to locked table; any
    assessment absent from a table row is structurally inadmissible for g_null.]

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

[Identical structure to V-01.]

---

## §0 -- CHALLENGER PRE-GATE: NULL HYPOTHESIS DIMENSION TABLE

Contract: DISPOSITION_CONTRACT v1

*(Per §0 PHASE 1: populate all dimension rows before writing NH TESTIMONY.)*

**Null Hypothesis Dimension Comparison Table**:

| Dimension | Current-State Score | Proposed-State Score | Differential | Per-Dim Verdict |
|-----------|--------------------|--------------------|--------------|-----------------|
| [DIM_1] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_2] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_3 -- optional] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |

**§0 Table Majority**: [BUILD-WINS / STATUS-QUO-WINS / TIED]
**g_null(initial) candidate from §0**: [PASS / CONDITIONAL / FAIL]

**DIMENSION TABLE LOCKED**
*(Per §0 PHASE 2. NH TESTIMONY follows. Assessments not traceable to a table row are
structurally inadmissible for g_null derivation.)*

**NH TESTIMONY** *(Derived from locked table only)*:
[One paragraph summarizing dimension table verdict. Reference table rows by dimension
name. Do not introduce assessments absent from the table.]

---

## BRACKET OPENING -- CHALLENGER

[Identical to V-01.]

---

## DOMAIN -- [ROLE_NAME]

[Identical to V-01 DOMAIN template.]

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

[Identical to V-01.]

---

## §3.8 -- CH-ID SATURATION CHECK

[Identical to V-01.]

---

## §5.7 -- LENS COVERAGE TABLE

*(Per §15, §17, and §17a CITATION VALIDITY RULE. Five columns: Role, Lens Dimension,
Applicability, Basis (§1 citation), Status, ADVISORY-OPEN-LENS? Basis must name §1
surface. Generic archetype basis is INVALID -> row treated as ADVISORY-OPEN-LENS.)*

| Role | Lens Dimension | Applicability | Basis (§1 citation) | Status | ADVISORY-OPEN-LENS? |
|------|---------------|--------------|---------------------|--------|---------------------|
| [ROLE] | [lens.verify entry 1] | [HIGH / MEDIUM / LOW] | [§1.N: surface -- one sentence] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN or INVALID / NO] |
| [ROLE] | [lens.verify entry 2] | [HIGH / MEDIUM / LOW] | [§1.N: surface -- one sentence] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN or INVALID / NO] |
| [LIFECYCLE_ROLE] | [lens.verify entry] | [HIGH / MEDIUM / LOW] | [§1.N: surface -- one sentence] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN or INVALID / NO] |

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

[Identical to V-01 §5.8 -- operates on §1 IN-SCOPE, references §5.7 Applicability
tiers which now have valid §17a citations as their basis.]

---

## LIFECYCLE -- [ROLE_NAME]

[Identical to V-01 LIFECYCLE template.]

---

## BRACKET CLOSING -- CHALLENGER

[Identical to V-01.]

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

[Identical to V-01.]

---

## GATE VECTOR TABLE

[Identical to V-01.]

---

## CROSS-ROLE SIGNALS

[Identical to V-01.]

---

## DISPOSITION

[Identical to V-01.]

---

## ACTION ITEM REGISTER

[Identical to V-01 structure. ADVISORY-OPEN-LENS includes INVALID-BASIS rows per §17a.]

---

**Artifact to review:**

{{artifact}}

---

## V-05

**Axis**: Full integration (three-axis) -- V-01 §0 PHASE 2 (DIMENSION TABLE LOCKED) +
V-02 §17a (SURFACE CITATION REQUIREMENT) + V-03 §1a (ARTIFACT DOMAIN INVENTORY).
All three C-33/C-34/C-35 failure modes addressed with the strongest enforcement chain.

**Hypothesis**: Each single-axis variation addresses one failure mode independently.
V-05 combines all three with an explicit dependency chain:
- §1a DOMAIN INVENTORY LOCKED at scope time (before any reviewer) -> §18 has a
  pre-committed source (C-34 source pre-committed, not inferred at §5.8 time)
- §17a SURFACE CITATION REQUIREMENT in §5.7 -> each Applicability row traces to a
  §1 surface, making ratings artifact-specific evidence (C-33 evidence traceable)
- §0 PHASE 2 DIMENSION TABLE LOCKED sentinel -> NH TESTIMONY is derived from
  locked table; g_null derivable from table values alone (C-35 derivable)
The three mechanisms are independent axes with no structural conflict. V-05 predicts
225/225 -- the strongest candidate.

---

depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. Do not add sections
between pre-printed headers. If a field cannot be filled, write `[N/A -- reason]`.

---

```
==============================================================================
IMMUTABLE PROTOCOL BLOCK -- read all sections before executing any reviewer
==============================================================================

DISPOSITION_CONTRACT v1

§1 -- SCOPE ENUMERATION
[Fill before proceeding. Pre-reviewer gate.]
  IN-SCOPE surfaces: [enumerate exhaustively -- rows cited in §5.5 and §1a]
  OUT-OF-SCOPE: [surface -- reason, or "None"]
  Scope Amendment Protocol: SCOPE AMENDMENT: [surface] added -- [reason]
§1 COMPLETE
  -> §1a ARTIFACT DOMAIN INVENTORY follows immediately (before ROLE MANIFEST).

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment. No commitment proceeds with open HIGH findings.
  MEDIUM = Conditions commitment. Proceeds only after named resolution.
  LOW    = Advisory. Commitment may proceed.
  These definitions apply universally and may not be restated at any gate.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose = FAIL  [override: null hypothesis holds]
                OR any Gi = FAIL
  CONDITIONAL  <-- no Gi = FAIL  AND  any Gi = CONDITIONAL
  READY        <-- all Gi = PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  If multiple DOMAIN sections: G_domain_agg = worst-case(all G_domain verdicts)
  Worst-case order: FAIL > CONDITIONAL > PASS
  Apply mechanically; do not aggregate editorially.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A missing cite is an audit-trail gap.

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, ...).
  Every downstream section carries a mandatory CH-ID response table.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

==============================================================================

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  (a) Row syntax: | Section | Gate | Verdict | Class |
  (b) Emit at end of each verdict-emitting section, after verdict is stated.
  (c) Assembly rule: copy all local rows to ACTION ITEM REGISTER verbatim.
  Excluded sections (no local ledger row):
    §3.5 / §3.8 / §5.5 / §5.7 / §5.8 / §1a

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical execution sequence:
  §1 -> §1a Artifact Domain Inventory ->
  §0 Challenger Pre-Gate ->
  Role Manifest -> Bracket Opening -> Domain(s) ->
  §3.5 Domain-Aggregate Checkpoint -> §3.8 CH-ID Saturation Check ->
  §5.7 Lens Coverage Table -> §5.8 Domain Coverage Gap-Check ->
  Lifecycle -> Bracket Closing ->
  §5.5 Scope Coverage Reconciliation -> Gate Vector Table ->
  Cross-Role Signals -> Disposition -> Action Item Register
  Reordering is a contract violation.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  [Identical to V-01]

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  [Identical to V-01]

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  [Identical to V-01]

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  [Identical to V-01]

§15 -- LENS EXHAUSTION PROTOCOL [IMMUTABLE]
  [Identical to V-01]

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  [Identical to V-01]

§1a -- ARTIFACT DOMAIN INVENTORY PROTOCOL [IMMUTABLE]
  Immediately after §1 COMPLETE, before §0 and before ROLE MANIFEST:
  (a) Derive a minimal set of atomic domain concerns from the §1 IN-SCOPE surfaces.
      Each domain is a distinct type of concern. A domain is atomic if it cannot be
      split into two concerns requiring different reviewer expertise.
  (b) Number each domain: DOMAIN-1, DOMAIN-2, ...
  (c) For each domain, name at least one §1 surface that belongs to it.
  (d) Emit: ARTIFACT DOMAIN INVENTORY LOCKED
      This sentinel locks the domain list. §18 operates on these labels only.
      Domain labels may not be created or altered after the LOCKED sentinel.

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  Each row in §5.7 carries an Applicability rating:
    HIGH / MEDIUM / LOW -- artifact-specific, NOT inherited from role definition.
  Coverage expectation by tier:
    HIGH: ADDRESSED required; OPEN -> ADVISORY-OPEN-LENS
    MEDIUM: ADDRESSED preferred; OPEN -> ADVISORY-LOW
    LOW: OPEN acceptable; no ADVISORY-OPEN-LENS

  §17a -- CITATION VALIDITY RULE [IMMUTABLE]
    Each §5.7 row carries a `Basis (§1 citation)` column.
    VALID: names at least one §1 IN-SCOPE surface by number and label with
    one sentence of justification (e.g., "§1.2: authentication boundary --
    this lens directly evaluates boundary correctness").
    INVALID: cites only role archetype without naming a §1 surface.
    INVALID basis -> row treated as ADVISORY-OPEN-LENS regardless of Status.
  §17 must be complete before §18 executes.

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  After §5.7 is complete (including §17 Applicability and §17a valid citations),
  execute §5.8 DOMAIN COVERAGE GAP-CHECK using the §1a ARTIFACT DOMAIN INVENTORY
  as the locked source of domain labels:
  For each DOMAIN-N in the §1a inventory:
    Identify the maximum Applicability tier among all reviewers whose lens
    dimensions cover DOMAIN-N (as mapped by the §1a surface-to-domain assignment).
    COVERED      = at least one reviewer has HIGH applicability to DOMAIN-N
                   (with valid §17a citation)
    ADVISORY-GAP = highest tier is MEDIUM or LOW, or no reviewer covers DOMAIN-N,
                   OR all HIGH-tier rows for DOMAIN-N have INVALID §17a basis
  Each ADVISORY-GAP domain appended to ACTION ITEM REGISTER:
    - Domain label (DOMAIN-N from §1a)
    - Highest valid applicability tier found
    - Reason no valid HIGH-applicability reviewer covers it
    - Disposition class: ADVISORY-GAP
  §5.8 emits no gate verdict and no local ledger row.
  Dependency chain: §1a (locked domains) -> §17 (applicability) ->
  §17a (valid citations) -> §18 (gap-check) -> §5.8 (action items)

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  PHASE 1 -- TABLE POPULATION:
    Complete all dimension rows before NH TESTIMONY.
    Columns: Dimension | Current-State Score | Proposed-State Score |
             Differential | Per-Dim Verdict
    Min 2 dimensions. Per-Dim: BUILD-WINS / STATUS-QUO-WINS / TIED.
  PHASE 2 -- TABLE LOCK:
    After all dimension rows complete, emit: DIMENSION TABLE LOCKED
    NH TESTIMONY is structurally subordinate to the locked table.
    Any assessment in NH TESTIMONY not traceable to a table row is
    structurally inadmissible for g_null derivation.
  g_null(initial) derivation:
    BUILD-WINS majority  -> PASS
    STATUS-QUO-WINS majority -> FAIL
    Mixed or TIED -> CONDITIONAL
  GOpen must equal §0 candidate or state named override.
  Dependency chain: §0 table (locked) -> NH TESTIMONY (derived) ->
  GOpen -> §9 Stage 1 -> g_null progression.

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot.

Review Parameters:
- Artifact: {{artifact_id}}
- Depth: {{depth}}
- Reviewer set: {{reviewer_set}}

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3. CHALLENGER positions remain fixed.)*

---

## §1a -- ARTIFACT DOMAIN INVENTORY

*(Executed after §1 COMPLETE, before §0, before ROLE MANIFEST. Per §1a protocol.)*

| Domain ID | Domain Name | Atomic Concern | §1 Surface(s) |
|-----------|-------------|---------------|---------------|
| DOMAIN-1 | [domain name] | [one sentence distinguishing from other domains] | [§1.N, §1.M] |
| DOMAIN-2 | [domain name] | [one sentence] | [§1.P] |
| DOMAIN-3 | [optional] | [one sentence] | [§1.Q] |

**ARTIFACT DOMAIN INVENTORY LOCKED**
*(Domain labels above are the fixed source for §18. No new domains admitted after this point.)*

---

## §0 -- CHALLENGER PRE-GATE: NULL HYPOTHESIS DIMENSION TABLE

Contract: DISPOSITION_CONTRACT v1

*(Per §0 PHASE 1: populate all dimension rows before NH TESTIMONY.)*

**Null Hypothesis Dimension Comparison Table**:

| Dimension | Current-State Score | Proposed-State Score | Differential | Per-Dim Verdict |
|-----------|--------------------|--------------------|--------------|-----------------|
| [DIM_1] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_2] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_3 -- optional] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |

**§0 Table Majority**: [BUILD-WINS / STATUS-QUO-WINS / TIED -- count Per-Dim Verdicts]
**g_null(initial) candidate from §0**: [PASS / CONDITIONAL / FAIL -- derived from majority]

**DIMENSION TABLE LOCKED**
*(Per §0 PHASE 2. NH TESTIMONY follows. Assessments not in a table row are inadmissible
for g_null derivation.)*

**NH TESTIMONY** *(Derived from locked table only)*:
[One paragraph. Reference dimension rows by name. No new assessments introduced.]

*(If GOpen contradicts §0 candidate, state override justification with specific
dimension(s) named. Otherwise GOpen = §0 candidate.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table** *(per C-16)*:

| Dimension | Status Quo | Build | Hybrid |
|-----------|-----------|-------|--------|
| [DIM_A] | [score] | [score] | [score] |
| [DIM_B] | [score] | [score] | [score] |
| [DIM_C] | [score] | [score] | [score] |
| **Total** | [sum] | [sum] | [sum] |

**NULL HYPOTHESIS DERIVATION RULE**: Build beats Status Quo (B > A) AND Build beats
Hybrid (B > C) -> g_null = PASS. One fails -> CONDITIONAL. Both fail -> FAIL.

**Challenge claims** *(assign CH-IDs; carry to every downstream section per §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL -- must equal §0 candidate or state override]
**GOpen Reason**: [One sentence.]
**g_null(initial)**: [copy GOpen verdict -- Stage 1 of §9 progression]

*Local Gate Ledger Row*: | BRACKET OPENING | GOpen | [verdict] | [class per §6] |

*GOpen and all CH-IDs carry forward to every downstream section.*

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

**Alternatives Re-score** *(per C-16)*:

| Dimension | Status Quo | Build | Hybrid |
|-----------|-----------|-------|--------|
| [DIM_A] | [re-score] | [re-score] | [re-score] |
| [DIM_B] | [re-score] | [re-score] | [re-score] |
| [DIM_C] | [re-score] | [re-score] | [re-score] |
| **Total** | [sum] | [sum] | [sum] |

**Additional Findings**:

| F-ID | Finding | Severity |
|------|---------|---------|
| F-01 | [FINDING from this role's `lens.verify` and `expertise.depth`. Names an in-scope surface.] | [HIGH / MEDIUM / LOW] |
| F-02 | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-03 | [optional] | [HIGH / MEDIUM / LOW] |
| F-04 | [optional] | [HIGH / MEDIUM / LOW] |

**Section Severity** *(per §14: worst(F-01, F-02, ...))*: [HIGH / MEDIUM / LOW]
**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]
**G_domain Aggregate** *(per §3a)*: [PASS / CONDITIONAL / FAIL]

*Local Gate Ledger Row*: | DOMAIN | G_domain | [verdict] | [class per §6] |

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

*(Informational only -- no local ledger row.)*

**G_domain Aggregate confirmed**: [copy]
**g_null(post-domain)** *(per §9 Stage 2)*: [PASS / CONDITIONAL / FAIL]

---

## §3.8 -- CH-ID SATURATION CHECK

*(Informational only -- no local ledger row. LIFECYCLE does not begin until SATURATED.)*

| CH-ID | DOMAIN Response Status | SATURATED? |
|-------|----------------------|-----------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] | [YES / NO] |
| CH-002 | [copy] | [YES / NO] |
| CH-003 | [copy if active] | [YES / NO] |

**Saturation status**: [SATURATED / UNSATURATED]

---

## §5.7 -- LENS COVERAGE TABLE

*(Per §15, §17, and §17a. Six columns: Role, Lens Dimension, Applicability,
Basis (§1 citation), Status, ADVISORY-OPEN-LENS?
Basis must name a §1 surface. INVALID basis -> row = ADVISORY-OPEN-LENS.)*

*(Informational only -- no local ledger row.)*

| Role | Lens Dimension | Applicability | Basis (§1 citation) | Status | ADVISORY-OPEN-LENS? |
|------|---------------|--------------|---------------------|--------|---------------------|
| [ROLE] | [lens.verify 1] | [HIGH / MEDIUM / LOW] | [§1.N: surface -- why] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN or INVALID / NO] |
| [ROLE] | [lens.verify 2] | [HIGH / MEDIUM / LOW] | [§1.N: surface -- why] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN or INVALID / NO] |
| [LIFECYCLE_ROLE] | [lens.verify] | [HIGH / MEDIUM / LOW] | [§1.N: surface -- why] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN or INVALID / NO] |

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

*(Per §18 full. Operates on §1a ARTIFACT DOMAIN INVENTORY (locked) as source of domain
labels. HIGH-applicability assessment valid only if §17a basis cites a §1 surface.)*

*(Informational only -- no local ledger row.)*

| Domain (§1a ID + Name) | Max Valid Applicability | Gap Status | Disposition |
|------------------------|------------------------|------------|-------------|
| DOMAIN-1: [name] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [-- / ADVISORY-GAP -> ACTION REGISTER] |
| DOMAIN-2: [name] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [-- / ADVISORY-GAP -> ACTION REGISTER] |
| DOMAIN-3: [name if active] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [-- / ADVISORY-GAP -> ACTION REGISTER] |

*"Valid" applicability = HIGH with a valid §17a citation (names §1 surface). INVALID-basis
HIGH rows do not count as COVERED.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]
Received G_domain Aggregate: [copy from §3.5]
Saturation confirmed: [SATURATED -- per §3.8]

**CH-ID Response Table** *(mandatory per §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [Is evidence sufficient for commitment? One paragraph
referencing GOpen and G_domain Aggregate explicitly.]

**Null hypothesis status**: [Has null hypothesis been defeated given GOpen and G_domain_agg?
yes / partial / no -- one sentence.]

**Additional Findings**:

| F-ID | Finding | Severity |
|------|---------|---------|
| F-01 | [FINDING from this role's `lens.verify`. Commitment, program, or decision concerns.] | [HIGH / MEDIUM / LOW] |
| F-02 | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Section Severity** *(per §14)*: [HIGH / MEDIUM / LOW]
**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

*Local Gate Ledger Row*: | LIFECYCLE | G_lifecycle | [verdict] | [class per §6] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: scope declaration, all CH-ID tables, all gate verdicts.*

Received G_domain Aggregate: [copy]
Received G_lifecycle: [copy]

**Alternatives Aggregated Table** *(per C-16)*:

| Dimension | Status Quo (agg) | Build (agg) | Hybrid (agg) |
|-----------|-----------------|-------------|--------------|
| [DIM_A] | [aggregated] | [aggregated] | [aggregated] |
| [DIM_B] | [aggregated] | [aggregated] | [aggregated] |
| [DIM_C] | [aggregated] | [aggregated] | [aggregated] |
| **Total** | [sum] | [sum] | [sum] |

**NULL HYPOTHESIS DERIVATION RULE applied**: [same rule from BRACKET OPENING applied
to aggregated totals -> derived g_null verdict]

**CH-ID Full Saturation Check** *(per §8)*:

| CH-ID | G_domain Status | G_lifecycle Status | FULLY SATURATED? |
|-------|----------------|-------------------|-----------------|
| CH-001 | [copy from DOMAIN] | [copy from LIFECYCLE] | [YES / NO] |
| CH-002 | [copy] | [copy] | [YES / NO] |
| CH-003 | [copy if active] | [copy] | [YES / NO] |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [NOTE] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [NOTE] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [NOTE] |

**Remaining gaps**: [If none: "None -- all CH-IDs DEFEATED."]
**Override invoked**: [YES / NO]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose override authority**: GClose = FAIL overrides all prior gate verdicts per §3.
**GClose Rationale**: [2-3 sentences.]
**g_null(final)** *(per §9 Stage 3)*: [PASS / CONDITIONAL / FAIL]

*Local Gate Ledger Row*: | BRACKET CLOSING | GClose | [verdict] | [class per §6] |

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

*(Executes after BRACKET CLOSING per §10. Informational only.)*

| §1 IN-SCOPE Surface | Coverage Status | Finding Reference |
|---------------------|----------------|-------------------|
| [SURFACE_1] | [COVERED / GAP] | [F-ID or "none"] |
| [SURFACE_2] | [COVERED / GAP] | [F-ID or "none"] |
| [SURFACE_3] | [COVERED / GAP] | [F-ID or "none"] |

**§5.5 Signal**: [COVERED / PARTIAL]

---

## GATE VECTOR TABLE

*(Assembled verbatim from local ledger rows per §6(c).)*

| Gate | Section | Verdict | Contract Cite |
|------|---------|---------|---------------|
| GOpen | BRACKET OPENING | [copy] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | DOMAIN (aggregate per §3a) | [copy] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | LIFECYCLE | [copy] | DISPOSITION_CONTRACT v1 |
| GClose | BRACKET CLOSING | [copy] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**g_null Progression Ledger** *(per §9)*:
```
g_null(initial)     = [copy from BRACKET OPENING]   [Stage 1: = GOpen]
g_null(post-domain) = [copy from §3.5]              [Stage 2: worst-case(G_domain_agg, Stage 1)]
g_null(final)       = [copy from BRACKET CLOSING]   [Stage 3: worst-case(G_lifecycle, Stage 2)]
Trajectory: [e.g., PASS -> PASS -> PASS]
```

**Conflicts**: [Incompatible CH-ID responses or findings across roles -- name tension.
If none: "None detected."]

**Convergence**: [Concern named independently by two or more reviewers -- name it and
state why it is the highest-confidence signal.]

**Scope coverage**: [Any §1 surface not covered. If all covered: "None -- full
in-scope surface reviewed." (see §5.5 for detail)]

---

## DISPOSITION

**Gate vector** *(from GATE VECTOR TABLE)*:
- GOpen         = [copy]
- G_domain_agg  = [copy]
- G_lifecycle   = [copy]
- GClose        = [copy]

**Apply §3 formula** *(evaluate mechanically)*:
```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL?              --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL?        --> BLOCKED
No FAIL, any CONDITIONAL?   --> CONDITIONAL
All PASS?                   --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Primary Driver** *(per §16 precedence formula -- derived mechanically)*: [Gate name]

**Conditions** *(if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]
2. [Additional if present.]

**Blocker** *(if BLOCKED)*: [Specific finding. If GClose = FAIL:
"Challenger final verdict HOLDS -- [GClose Rationale summary]."]

---

## ACTION ITEM REGISTER

*(Assembled verbatim from local gate ledger rows per §6(c). Do not re-derive.
Sources: CH-ID rows (from PARTIAL/HOLDS) + ADVISORY-OPEN-LENS from §5.7 per §15
(including INVALID-BASIS rows per §17a) + ADVISORY-GAP from §5.5 per §10 +
ADVISORY-GAP from §5.8 per §18 (operating on §1a domain inventory).)*

| CH-ID / Source | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|---------------|-----------------|------------------|------------|---------------------|
| CH-001 | [from PARTIAL or HOLDS] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE] | [Falsifiable criterion] |
| CH-002 | [Item 2] | [class] | [ROLE] | [Criterion] |
| ADVISORY-OPEN-LENS | [lens dimension OPEN with HIGH applicability] | ADVISORY-OPEN-LENS | [ROLE] | [When ADDRESSED] |
| ADVISORY-OPEN-LENS | [lens dimension with INVALID §17a basis] | ADVISORY-OPEN-LENS | [ROLE] | [When valid §1 surface cited] |
| ADVISORY-GAP | [§1 surface with no reviewer finding -- from §5.5] | ADVISORY-GAP | [ROLE] | [When COVERED] |
| ADVISORY-GAP | [§1a domain with no HIGH-applicability reviewer -- from §5.8] | ADVISORY-GAP | [ROLE] | [When covered by HIGH reviewer with valid citation] |
| ADVISORY-OBS | [advisory observation not sourced from CH-ID] | ADVISORY-OBS | [ROLE] | [Criterion] |

*Dependency chain summary: §1a (locked domains) feeds §18; §17a (citations) validates
§17 (applicability) feeds §18; §0 PHASE 2 (locked table) feeds §9 (g_null progression).
All three chains traceable without cross-referencing reviewer narrative.*

---

**Artifact to review:**

{{artifact}}
