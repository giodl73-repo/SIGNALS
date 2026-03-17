---
skill: quest-variate
skill_target: org-review
date: 2026-03-17
round: 12
rubric: org-review-rubric-v11-2026-03-16.md
---

# org-review -- Variate R12

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis and three-axis combinations (V-04, V-05).

**R12 design target**: R11 V-05 predicted 225/225 but actual score is 210/225
(C-33/C-34/C-35 all absent). The R11 mechanisms were structurally present but
lacked execution-time enforcement. R12 identifies the residual failure mode per
criterion and applies a stronger binding mechanism:

| Criterion | R11 V-05 mechanism | R11 failure mode | R12 fix |
|-----------|-------------------|-----------------|---------|
| C-35 Null Hypothesis Dimension Table | §0 PRE-LOCK GATE with DIMENSION TABLE LOCKED sentinel | Model fills NH TESTIMONY before all dimension rows are complete, or introduces off-table assessments that carry no row citation. LOCKED sentinel is emitted but NH prose is not structurally subordinate -- no mechanism rejects uncited assessments. | §0 PHASE 2a DIMENSION COUNT BINDING: bind `dimension_count = N` after table lock. g_null derivation formula references `dimension_count` by name. NH TESTIMONY opening sentence must state `dimension_count`. Any assessment that does not trace to a named row is structurally inadmissible AND cannot alter `dimension_count`. Count binding makes the reference verifiable. |
| C-33 Lens Applicability Rating Pre-committed | §17a with Basis column requiring §1 citation | Model writes Basis column with generic archetype-level text ("this role covers architecture concerns"). CITATION VALIDITY RULE says "generic basis is invalid" but provides no enforcement mechanism that distinguishes valid from invalid at population time. | §17a TYPED ASSERTION BLOCK replaces Basis column with a 3-field typed structure: `{surface_anchor: "[verbatim §1 text]", rating_basis: "[sentence]", rating: "HIGH/MEDIUM/LOW"}`. surface_anchor must contain text that appears verbatim in §1. The structure is machine-checkable: if surface_anchor does not match §1 text, the row is invalid by inspection. Generic text cannot satisfy the verbatim-match requirement. |
| C-34 ADVISORY-GAP Domain Coverage | §1a ARTIFACT DOMAIN INVENTORY (locked list) + §18 gap-check | §18 operates on the §1a inventory but the ADVISORY-GAP determination is a prose narrative that may conflate multiple domains or silently skip domains with ambiguous coverage. No count assertion forces the model to account for every inventory row. | §18 DOMAIN COVERAGE CERTIFICATION with count assertion: "§5.8 certified [N] domains, [M] ADVISORY-GAP identified." N must equal |§1a inventory|. Certification forces enumeration of every row; a missing row produces a count mismatch. Formal notation K(d) = |R(d)| where R(d) = {roles with HIGH applicability to domain d} makes the K(d) = 0 → ADVISORY-GAP condition binary and auditable. |

**R12 axes:**

- V-01: Lifecycle emphasis (single axis) -- §0 PHASE 2a COUNT BINDING. After
  DIMENSION TABLE LOCKED, bind `dimension_count = N`. g_null derivation references
  `dimension_count` by name. NH TESTIMONY must open with the dimension count.
  C-35 PASS; C-33/C-34 unchanged from R11 baseline.

- V-02: Output format (single axis) -- §17a TYPED ASSERTION BLOCK. Replace Basis
  column with typed 3-field structure {surface_anchor, rating_basis, rating}.
  surface_anchor must contain verbatim text from §1 IN-SCOPE. CITATION VALIDITY RULE
  enforces at structure level, not prose level. C-33 PASS; C-34 flows from C-33 source.
  C-35 unchanged (§0 LOCK gate present, no count binding).

- V-03: Phrasing register (single axis) -- §18 FORMAL PREDICATE NOTATION. Let
  R(d) = {roles with HIGH applicability to domain d in §5.7}. K(d) = |R(d)|.
  K(d) = 0 → ADVISORY-GAP. §5.8 emits count assertion: N domains certified, M gaps.
  C-34 PASS; C-33/C-35 unchanged from R11 baseline.

- V-04: Lifecycle + Output format (two-axis) -- V-01 COUNT BINDING (C-35) +
  V-02 TYPED ASSERTION BLOCK (C-33 -> C-34).

- V-05: Full integration (three-axis) -- V-01 COUNT BINDING (C-35) + V-02 TYPED
  ASSERTION BLOCK (C-33) + V-03 FORMAL PREDICATE NOTATION (C-34 with tightest
  enforcement). Strongest combination: count verifies dimension table completeness;
  verbatim anchor verifies applicability rating provenance; formal predicate verifies
  domain gap exhaustiveness.

**Predicted R12 scores under v11:**
- V-01: C-35 PASS (dimension_count binding in g_null formula), C-33 FAIL, C-34 vacuous. 215/225
- V-02: C-33 PASS (typed assertion, verbatim anchor), C-34 PASS (§17a supplies source data), C-35 FAIL. 220/225
- V-03: C-34 PASS (formal predicate + count assertion), C-33 FAIL (no typed assertion), C-35 FAIL. 215/225
- V-04: C-35 PASS + C-33 PASS + C-34 PASS via C-33. 225/225
- V-05: C-35 + C-33 + C-34 PASS with independent enforcement per criterion. 225/225

---

## V-01

**Axis**: Lifecycle emphasis (single axis) -- §0 PHASE 2a COUNT BINDING.
**Hypothesis**: R11 §0 requires DIMENSION TABLE LOCKED before NH TESTIMONY, but
NH TESTIMONY can still introduce off-table assessments because no mechanism ties
prose claims to specific table rows. Adding `dimension_count = N` as a bound
variable and requiring the g_null derivation formula to reference `dimension_count`
by name (not a placeholder) forces the model to produce a filled count at table-lock
time. NH TESTIMONY must state `dimension_count` in its opening sentence, creating a
traceable link: locked rows -> dimension_count -> NH TESTIMONY first sentence ->
g_null derivation. Any assessment in NH prose absent from a named table row cannot
change `dimension_count` and is therefore structurally inadmissible for g_null
derivation. C-33/C-34 unchanged from R11 V-01 baseline. Predicted: 215/225.

---

depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit
any pre-printed heading, label, field, formula, or structural element. Do not add
sections between pre-printed headers. If a field cannot be filled, write
`[N/A -- reason]`.

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

§1a -- ARTIFACT DOMAIN INVENTORY
[Fill immediately after §1 COMPLETE. Derive atomic domain concerns from §1
IN-SCOPE surfaces. Each domain = one addressable concern for a single reviewer role.
Numbered list. This inventory is the source set for §5.8 gap-check.]
  1. [DOMAIN_1]
  2. [DOMAIN_2]
  3. [DOMAIN_3 -- add rows as needed]
§1a COMPLETE

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
  PRIMARY DRIVER emitted as labeled field at DISPOSITION.

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
  For each domain in §1a ARTIFACT DOMAIN INVENTORY:
    Identify the maximum Applicability tier among all reviewers whose
    lens dimensions cover that domain.
    COVERED      = at least one reviewer has HIGH applicability to this domain
    ADVISORY-GAP = highest tier is MEDIUM or LOW only, or no reviewer covers domain
  Each ADVISORY-GAP domain must be appended to ACTION ITEM REGISTER with:
    - Domain name (from §1a)
    - Highest applicability tier found (or "none")
    - Reason no HIGH-applicability reviewer covers it
    - Disposition class: ADVISORY-GAP
  §5.8 emits no gate verdict and no local ledger row (excluded from §6).
  §18 requires §17 Applicability ratings; §17 must be complete before §18 executes.

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  The challenger's null hypothesis evaluation in BRACKET OPENING uses a structured
  dimension comparison table. The protocol has THREE phases:

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
    This sentinel is required before any further output may continue.

  PHASE 2a -- DIMENSION COUNT BINDING:
    Immediately after DIMENSION TABLE LOCKED, emit:
      dimension_count = N  (where N = number of rows in the table above)
    This binding is named. It is referenced by name in the g_null derivation
    rule and in the NH TESTIMONY opening sentence.
    A placeholder [N] does not satisfy this requirement; the bound value must
    be a filled integer.

  PHASE 3 -- NH TESTIMONY:
    NH TESTIMONY is structurally subordinate to the locked table.
    NH TESTIMONY must open with: "Based on dimension_count=[bound value]
    dimension rows in the locked table, ..."
    Any assessment appearing only in NH TESTIMONY prose that is absent from
    a named table row above is structurally inadmissible for g_null derivation.
    Citing "dimension_count" by name in the opening sentence is required.

  g_null(initial) derivation rule (applied to table values only):
    Let B = count of BUILD-WINS verdicts in table
    Let S = count of STATUS-QUO-WINS verdicts in table
    Derivation: B > dimension_count/2 -> PASS
                S > dimension_count/2 -> FAIL
                else -> CONDITIONAL
    The formula references dimension_count by name. The bound value of
    dimension_count is the denominator. A g_null derivation that does not
    reference dimension_count by name does not satisfy this requirement.
    GOpen must be consistent with the §0 table derivation. A GOpen that
    contradicts the table derivation requires a named justification citing
    the specific dimension(s) that override the result.

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

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

*(Per §0 PHASE 1: populate all dimension rows before writing any NH TESTIMONY.)*

**Null Hypothesis Dimension Comparison Table**:

| Dimension | Current-State Score | Proposed-State Score | Differential | Per-Dim Verdict |
|-----------|--------------------|--------------------|--------------|-----------------|
| [DIM_1] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_2] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_3 -- optional] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |

**DIMENSION TABLE LOCKED**

*(Per §0 PHASE 2a: bind dimension count immediately.)*

**dimension_count = [N]**

*(Per §0 PHASE 3: NH TESTIMONY begins. Opening sentence must state dimension_count by name.)*

**NH TESTIMONY** *(Derived from locked table only)*:
[Opening sentence required: "Based on dimension_count=[N] dimension rows in the locked
table, ..." Summarize what the table shows. Do not introduce assessments absent from
a named table row.]

**§0 Table derivation**:
- B (BUILD-WINS count) = [N]
- S (STATUS-QUO-WINS count) = [N]
- dimension_count = [N]
- B > dimension_count/2? [YES/NO] --> g_null candidate PASS
- S > dimension_count/2? [YES/NO] --> g_null candidate FAIL
- else --> CONDITIONAL
- **g_null(initial) candidate from §0**: [PASS / CONDITIONAL / FAIL]

*(If GOpen contradicts the §0 derivation, state the override justification below,
citing the specific dimension(s). Otherwise GOpen must equal the §0-derived candidate.)*

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
| F-03 | [optional] | [HIGH / MEDIUM / LOW] |

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
*(If UNSATURATED: state waiver with specific CH-ID and justification.)*

---

## §5.7 -- LENS COVERAGE TABLE

*(Produced after all DOMAIN sections complete, before LIFECYCLE. Per §15: ALL
lens.verify entries from each active role must appear. Per §17: each row carries
an Applicability rating specific to this artifact.)*

*(Informational only -- no gate verdict, no local ledger row per §6 exclusion list.)*

| Role | Lens Dimension | Applicability | Status | ADVISORY-OPEN-LENS? |
|------|---------------|--------------|--------|---------------------|
| [ROLE] | [lens.verify entry] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN / NO] |
| [LIFECYCLE_ROLE] | [lens.verify entry] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN / NO] |

*(All ADVISORY-OPEN-LENS entries appear in ACTION ITEM REGISTER per §15.)*

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

*(Executes after §5.7 per §18. Maps §1a ARTIFACT DOMAIN INVENTORY to reviewer
HIGH-applicability coverage. Informational only -- no gate verdict, no local ledger row.)*

| Domain (from §1a) | Max Applicability Among Reviewers | Gap Status | Disposition |
|------------------|----------------------------------|------------|-------------|
| [DOMAIN_1] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [-- / ADVISORY-GAP -> ACTION REGISTER] |
| [DOMAIN_2] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [-- / ADVISORY-GAP -> ACTION REGISTER] |

*(ADVISORY-GAP rows appended to ACTION ITEM REGISTER per §18.)*

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

**Decision-readiness assessment**: [One paragraph referencing GOpen and G_domain Aggregate
explicitly. Is evidence sufficient for commitment?]

**Null hypothesis status**: [Given GOpen and G_domain_agg, has the null hypothesis been
defeated? yes / partial / no -- one sentence.]

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

**Alternatives Aggregated Table** *(per C-16)*:

| Dimension | Status Quo (agg) | Build (agg) | Hybrid (agg) |
|-----------|-----------------|-------------|--------------|
| [DIM_A] | [aggregated] | [aggregated] | [aggregated] |
| [DIM_B] | [aggregated] | [aggregated] | [aggregated] |
| [DIM_C] | [aggregated] | [aggregated] | [aggregated] |
| **Total** | [sum] | [sum] | [sum] |

**NULL HYPOTHESIS DERIVATION RULE applied**: [Apply rule from BRACKET OPENING to
aggregated totals -> derived g_null verdict]

**CH-ID Full Saturation Check** *(per §8 FULLY SATURATED requirement)*:

| CH-ID | G_domain Status | G_lifecycle Status | FULLY SATURATED? |
|-------|----------------|-------------------|-----------------|
| CH-001 | [copy] | [copy] | [YES / NO] |
| CH-002 | [copy] | [copy] | [YES / NO] |
| CH-003 | [copy if active] | [copy] | [YES / NO] |

*(PASS verdict prohibited if any CH-ID not FULLY SATURATED without waiver.)*

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [NOTE] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [NOTE] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [NOTE] |

**Remaining gaps**: [If none: "None -- all CH-IDs DEFEATED."]

**Override invoked**: [YES / NO]
*(If YES: state justification and gate being overridden.)*

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
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
| [SURFACE_1] | [COVERED / GAP] | [F-ID or "none"] |
| [SURFACE_2] | [COVERED / GAP] | [F-ID or "none"] |

GAP surfaces -> appended to ACTION ITEM REGISTER as ADVISORY-GAP items per §10.
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

**Conflicts**: [Incompatible responses from two reviewers. If none: "None detected."]
**Convergence**: [Concern named by two or more reviewers independently.]
**Scope coverage**: [Any §1 surface uncovered. If all covered: "None."]

---

## DISPOSITION

**Gate vector** *(from GATE VECTOR TABLE)*:
- GOpen         = [copy]
- G_domain_agg  = [copy]
- G_lifecycle   = [copy]
- GClose        = [copy]

**Apply §3 formula** *(do not alter; evaluate mechanically)*:
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

**Blocker** *(if BLOCKED)*: [If GClose = FAIL: "Challenger final verdict HOLDS -- [GClose Rationale summary]."]

---

## ACTION ITEM REGISTER

*(CH-ID-sourced rows assembled verbatim from local gate ledger rows per §6(c).
ADVISORY-OPEN-LENS rows from §5.7 per §15. ADVISORY-GAP rows from §5.5 per §10
and from §5.8 per §18. Do not re-derive.)*

| CH-ID / Source | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|---------------|-----------------|------------------|------------|---------------------|
| CH-001 | [from PARTIAL or HOLDS status] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE] | [Falsifiable criterion] |
| ADVISORY-OPEN-LENS | [lens dimension uncovered] | ADVISORY-OPEN-LENS | [ROLE] | [When ADDRESSED] |
| ADVISORY-GAP | [§1 surface with no finding] | ADVISORY-GAP | [ROLE] | [When COVERED] |
| ADVISORY-GAP | [domain with no HIGH-applicability reviewer per §5.8] | ADVISORY-GAP | [ROLE] | [When covered by HIGH reviewer] |

---

**Artifact to review:**

{{artifact}}

---

## V-02

**Axis**: Output format (single axis) -- §17a TYPED ASSERTION BLOCK.
**Hypothesis**: R11 §17a added a Basis column requiring a §1 IN-SCOPE citation, but
the CITATION VALIDITY RULE was enforced only as prose instruction ("generic archetype
text is invalid"). The model can satisfy the structural requirement of a non-empty
Basis cell while writing generic text because no mechanism distinguishes a valid
surface-anchor citation from an invalid one at the column level. Replacing the Basis
column with a typed 3-field assertion block forces the model to produce a structured
object where `surface_anchor` must contain verbatim text from §1. The verbatim-match
requirement is inspectable by comparing the `surface_anchor` value against the §1
IN-SCOPE list -- no prose judgment required. Generic archetype text cannot satisfy
a verbatim-match test against §1 enumerated surfaces. C-33 PASS; C-34 flows from
C-33 surface data in §5.8. C-35 unchanged (§0 with DIMENSION TABLE LOCKED, no
count binding). Predicted: 220/225.

---

depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit
any pre-printed heading, label, field, formula, or structural element. Do not add
sections between pre-printed headers. If a field cannot be filled, write
`[N/A -- reason]`.

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

§1a -- ARTIFACT DOMAIN INVENTORY
[Fill immediately after §1 COMPLETE.]
  1. [DOMAIN_1]
  2. [DOMAIN_2]
  3. [DOMAIN_3 -- add rows as needed]
§1a COMPLETE

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

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, ...).
  Every downstream section carries a mandatory CH-ID response table.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

==============================================================================

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  (a) Row syntax: | Section | Gate | Verdict | Class |
  (b) Emit at end of each verdict-emitting section, after verdict is stated.
  (c) Assembly rule: copy all local rows to ACTION ITEM REGISTER verbatim.
      Do NOT re-derive Gate Verdict or Class.
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
  FULLY SATURATED = every CH-ID has domain + lifecycle response
  §3.8 SATURATION CHECK gate: LIFECYCLE does not begin until SATURATED.
  BRACKET CLOSING: PASS verdict prohibited if any CH-ID UNSATURATED without waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial)     = GOpen
  Stage 2: g_null(post-domain) = worst-case(G_domain_agg, g_null(initial))
  Stage 3: g_null(final)       = worst-case(G_lifecycle, g_null(post-domain))
  GClose must equal g_null(final). Deviation requires explicit override.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 executes after BRACKET CLOSING. Maps §1 surfaces to findings.
  GAP surfaces -> ADVISORY-GAP in ACTION ITEM REGISTER.
  §5.5 emits COVERED/PARTIAL signal (informational only, no ledger row).

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Every finding row carries individual Severity.
  Section Severity = worst(all finding severities in section). Derived mechanically.

§15 -- LENS EXHAUSTION PROTOCOL [IMMUTABLE]
  §5.7 executes after all DOMAIN sections, before LIFECYCLE.
  ALL lens.verify entries per active role must appear with ADDRESSED or OPEN.
  OPEN entries -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  [Rules 1-7 as in V-01 -- identical text omitted for brevity; rules must be
  reproduced verbatim in actual deployment. See V-01 §16 above.]

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  Each row in the LENS COVERAGE TABLE (§5.7) carries a typed applicability
  assertion block with the following three fields:
    surface_anchor : verbatim text fragment from §1 IN-SCOPE that grounds
                     the rating. Must be enclosed in double quotes.
                     CITATION VALIDITY RULE: surface_anchor must contain
                     text that appears verbatim in §1 IN-SCOPE. Generic
                     role-archetype text (e.g., "this role covers architecture")
                     does not satisfy this requirement and renders the row invalid.
    rating_basis   : one sentence linking the surface_anchor to the lens dimension
                     (why this surface makes the lens HIGH/MEDIUM/LOW applicable).
    rating         : HIGH, MEDIUM, or LOW.

  A row missing surface_anchor, or whose surface_anchor does not match §1 text
  verbatim, is an invalid row. An invalid row must be rewritten before §18 executes.

  Coverage expectation by tier:
    HIGH   -> ADDRESSED required; OPEN -> ADVISORY-OPEN-LENS
    MEDIUM -> ADDRESSED preferred; OPEN -> ADVISORY-LOW
    LOW    -> OPEN acceptable; no ADVISORY-OPEN-LENS triggered

  §17 must be complete and all rows valid before §18 executes.

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  After §5.7 is populated with valid §17 assertion blocks, execute §5.8:
  For each domain in §1a ARTIFACT DOMAIN INVENTORY:
    Identify the maximum Applicability tier (from §17 `rating` fields) among
    all reviewers whose lens dimensions cover that domain.
    COVERED      = at least one reviewer has rating: HIGH for this domain
    ADVISORY-GAP = highest rating is MEDIUM or LOW, or no reviewer covers domain
  Each ADVISORY-GAP domain -> ACTION ITEM REGISTER with domain name, highest
  tier found, reason, disposition class ADVISORY-GAP.
  §5.8 emits no gate verdict, no local ledger row.

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  PHASE 1: Complete all dimension rows first.
  Table columns: Dimension | Current-State Score | Proposed-State Score |
                 Differential | Per-Dim Verdict
  Minimum 2 dimensions. Per-Dim Verdict: BUILD-WINS / STATUS-QUO-WINS / TIED.
  PHASE 2: Emit DIMENSION TABLE LOCKED sentinel.
  NH TESTIMONY follows. Any assessment absent from a table row is structurally
  inadmissible for g_null derivation.
  g_null(initial) derivation rule:
    BUILD-WINS majority -> PASS; STATUS-QUO-WINS majority -> FAIL; else CONDITIONAL
  GOpen must be consistent with derivation or state override with named justification.

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

Review Parameters:
- Artifact: {{artifact_id}}
- Depth: {{depth}}
- Reviewer set: {{reviewer_set}}

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

---

## §0 -- CHALLENGER PRE-GATE: NULL HYPOTHESIS DIMENSION TABLE

Contract: DISPOSITION_CONTRACT v1

**Null Hypothesis Dimension Comparison Table**:

| Dimension | Current-State Score | Proposed-State Score | Differential | Per-Dim Verdict |
|-----------|--------------------|--------------------|--------------|-----------------|
| [DIM_1] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_2] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_3 -- optional] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |

**DIMENSION TABLE LOCKED**

**§0 Table Majority**: [BUILD-WINS / STATUS-QUO-WINS / TIED]
**g_null(initial) candidate from §0**: [PASS / CONDITIONAL / FAIL]

**NH TESTIMONY** *(Derived from locked table only)*:
[Summarize what the table shows. Do not introduce off-table assessments.]

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [One sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table**:

| Dimension | Status Quo | Build | Hybrid |
|-----------|-----------|-------|--------|
| [DIM_A] | [score] | [score] | [score] |
| [DIM_B] | [score] | [score] | [score] |
| [DIM_C] | [score] | [score] | [score] |
| **Total** | [sum] | [sum] | [sum] |

**NULL HYPOTHESIS DERIVATION RULE**: Build > Status Quo AND Build > Hybrid -> PASS.
One fails -> CONDITIONAL. Both fail -> FAIL.

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)**: [copy GOpen]

*Local Gate Ledger Row*: | BRACKET OPENING | GOpen | [verdict] | [class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim | Response | Status |
|-------|----------------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Alternatives Re-score**:

| Dimension | Status Quo | Build | Hybrid |
|-----------|-----------|-------|--------|
| [DIM_A] | [re-score] | [re-score] | [re-score] |
| [DIM_B] | [re-score] | [re-score] | [re-score] |
| **Total** | [sum] | [sum] | [sum] |

**Additional Findings**:

| F-ID | Finding | Severity |
|------|---------|---------|
| F-01 | [FINDING] | [HIGH / MEDIUM / LOW] |
| F-02 | [FINDING] | [HIGH / MEDIUM / LOW] |

**Section Severity** *(worst(F-01, F-02, ...))*: [HIGH / MEDIUM / LOW]
**Recommendation**: [One concrete action.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

*Local Gate Ledger Row*: | DOMAIN | G_domain | [verdict] | [class] |

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

**G_domain Aggregate confirmed**: [copy]
**g_null(post-domain)**: [worst-case(G_domain_agg, g_null(initial))]

---

## §3.8 -- CH-ID SATURATION CHECK

| CH-ID | DOMAIN Response Status | SATURATED? |
|-------|----------------------|-----------|
| CH-001 | [status] | [YES / NO] |
| CH-002 | [status] | [YES / NO] |

**Saturation status**: [SATURATED / UNSATURATED]

---

## §5.7 -- LENS COVERAGE TABLE

*(Per §17: each row carries a typed assertion block. surface_anchor must be verbatim
from §1. Invalid rows must be rewritten before §18 executes.)*

| Role | Lens Dimension | Assertion Block | Status | ADVISORY-OPEN-LENS? |
|------|---------------|-----------------|--------|---------------------|
| [ROLE] | [lens.verify entry] | surface_anchor: "[verbatim §1 text]" / rating_basis: "[one sentence]" / rating: [HIGH/MEDIUM/LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN / NO] |
| [LIFECYCLE_ROLE] | [lens.verify entry] | surface_anchor: "[verbatim §1 text]" / rating_basis: "[one sentence]" / rating: [HIGH/MEDIUM/LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN / NO] |

*(ADVISORY-OPEN-LENS entries -> ACTION ITEM REGISTER per §15.)*

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

*(Maps §1a inventory. Source: §17 `rating` fields from §5.7.)*

| Domain (§1a) | Max rating Among Reviewers | Gap Status | Disposition |
|-------------|---------------------------|------------|-------------|
| [DOMAIN_1] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [-- / ADVISORY-GAP -> ACTION REGISTER] |
| [DOMAIN_2] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [-- / ADVISORY-GAP -> ACTION REGISTER] |

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]
Received G_domain Aggregate: [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim | Response | Status |
|-------|----------------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph.]
**Null hypothesis status**: [yes / partial / no -- one sentence.]

**Additional Findings**:

| F-ID | Finding | Severity |
|------|---------|---------|
| F-01 | [FINDING] | [HIGH / MEDIUM / LOW] |
| F-02 | [FINDING] | [HIGH / MEDIUM / LOW] |

**Section Severity**: [worst(F-01, F-02)]
**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]

*Local Gate Ledger Row*: | LIFECYCLE | G_lifecycle | [verdict] | [class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
Received G_domain Aggregate: [copy]
Received G_lifecycle: [copy]

**Alternatives Aggregated Table**:

| Dimension | Status Quo (agg) | Build (agg) | Hybrid (agg) |
|-----------|-----------------|-------------|--------------|
| [DIM_A] | [agg] | [agg] | [agg] |
| **Total** | [sum] | [sum] | [sum] |

**NULL HYPOTHESIS DERIVATION RULE applied**: [result]

**CH-ID Full Saturation Check**:

| CH-ID | G_domain | G_lifecycle | FULLY SATURATED? |
|-------|---------|------------|-----------------|
| CH-001 | [copy] | [copy] | [YES / NO] |
| CH-002 | [copy] | [copy] | [YES / NO] |

**CH-ID Final Assessment**:

| CH-ID | G_domain | G_lifecycle | Final Status | Notes |
|-------|---------|------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [NOTE] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [NOTE] |

**Override invoked**: [YES / NO]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose Rationale**: [2-3 sentences.]
**g_null(final)**: [worst-case(G_lifecycle, g_null(post-domain))]

*Local Gate Ledger Row*: | BRACKET CLOSING | GClose | [verdict] | [class] |

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

| §1 Surface | Coverage Status | Finding Reference |
|------------|----------------|-------------------|
| [SURFACE] | [COVERED / GAP] | [F-ID or "none"] |

**§5.5 Signal**: [COVERED / PARTIAL]

---

## GATE VECTOR TABLE

| Gate | Section | Verdict | Contract Cite |
|------|---------|---------|---------------|
| GOpen | BRACKET OPENING | [copy] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | DOMAIN | [copy] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | LIFECYCLE | [copy] | DISPOSITION_CONTRACT v1 |
| GClose | BRACKET CLOSING | [copy] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**g_null Progression Ledger**:
```
g_null(initial)     = [copy]
g_null(post-domain) = [copy]
g_null(final)       = [copy]
Trajectory: [e.g., PASS -> PASS -> PASS]
```

**Conflicts**: [If none: "None detected."]
**Convergence**: [If none: "None detected."]
**Scope coverage**: [If all covered: "None."]

---

## DISPOSITION

**Gate vector**: GOpen=[_] G_domain_agg=[_] G_lifecycle=[_] GClose=[_]

**Apply §3 formula**: [result]

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Primary Driver** *(per §16)*: [Gate -- derived mechanically]

---

## ACTION ITEM REGISTER

| CH-ID / Source | Item | Disposition Class | Owner | Resolution Criterion |
|---------------|------|------------------|-------|---------------------|
| CH-001 | [item] | [class] | [ROLE] | [criterion] |
| ADVISORY-OPEN-LENS | [lens dimension] | ADVISORY-OPEN-LENS | [ROLE] | [when ADDRESSED] |
| ADVISORY-GAP | [§1 surface gap] | ADVISORY-GAP | [ROLE] | [when COVERED] |
| ADVISORY-GAP | [§5.8 domain gap] | ADVISORY-GAP | [ROLE] | [when HIGH reviewer covers] |

---

**Artifact to review:**

{{artifact}}

---

## V-03

**Axis**: Phrasing register (single axis) -- §18 FORMAL PREDICATE NOTATION.
**Hypothesis**: R11 §18 gap-check described the certification in narrative form:
"identify the maximum Applicability tier... ADVISORY-GAP = highest tier is MEDIUM or
LOW." The narrative form allows the model to conflate domains or apply the rule
inconsistently because no count assertion forces enumeration of every §1a row. Adding
formal predicate notation -- `K(d) = |R(d)|` where `R(d)` is the set of roles with
HIGH applicability to domain d -- makes the condition binary and auditable: K(d) = 0
is unambiguous. Requiring §5.8 to emit a count assertion (`certified N domains,
M gaps`) forces the model to enumerate all N rows in §1a. A count mismatch is
detectable by comparing N against |§1a|. C-34 PASS; C-33/C-35 unchanged from
R11 V-03 baseline. Predicted: 215/225.

---

depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit
any pre-printed heading, label, field, formula, or structural element. Do not add
sections between pre-printed headers. If a field cannot be filled, write
`[N/A -- reason]`.

---

```
==============================================================================
IMMUTABLE PROTOCOL BLOCK -- read all sections before executing any reviewer
==============================================================================

DISPOSITION_CONTRACT v1

§1 -- SCOPE ENUMERATION
  IN-SCOPE surfaces: [enumerate exhaustively -- cited in §5.5]
  OUT-OF-SCOPE: [surface -- reason, or "None"]
§1 COMPLETE

§1a -- ARTIFACT DOMAIN INVENTORY
[Fill immediately after §1 COMPLETE. Derive atomic domain concerns from IN-SCOPE
surfaces. Number each domain. This is the enumerated source set S for §5.8.
|S| = number of rows in this inventory.]
  1. [DOMAIN_1]
  2. [DOMAIN_2]
  3. [DOMAIN_3]
|S| = [N]     ← emit the cardinality immediately after the list
§1a COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions commitment. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose = FAIL OR any Gi = FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst-case(all G_domain verdicts). FAIL > CONDITIONAL > PASS.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim receives CH-ID. Every downstream section carries
  mandatory CH-ID response table. PASS prohibited if any CH-ID OPEN.

==============================================================================

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Emit after verdict. Copy verbatim to ACTION ITEM REGISTER. No re-derivation.
  Excluded: §3.5, §3.8, §5.5, §5.7, §5.8.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  §0 Pre-Gate -> Role Manifest -> Bracket Opening -> Domain(s) ->
  §3.5 -> §3.8 -> §5.7 -> §5.8 -> Lifecycle -> Bracket Closing ->
  §5.5 -> Gate Vector -> Cross-Role Signals -> Disposition -> Action Register
  Reordering is a contract violation.

§8 -- CH-ID SATURATION [IMMUTABLE]
  SATURATED = all CH-IDs have >=1 DOMAIN response. §3.8 gate blocks LIFECYCLE.
  FULLY SATURATED = all CH-IDs have domain + lifecycle response. Required at GClose.

§9 -- NULL HYPOTHESIS PROGRESSION [IMMUTABLE]
  g_null(initial) = GOpen; g_null(post-domain) = worst-case(G_domain_agg, Stage 1);
  g_null(final) = worst-case(G_lifecycle, Stage 2). GClose = g_null(final) or override.

§10 -- SCOPE COVERAGE [IMMUTABLE]
  §5.5 after Bracket Closing. GAP surfaces -> ADVISORY-GAP in register.

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Each finding row carries Severity. Section Severity = worst(all findings).

§15 -- LENS EXHAUSTION [IMMUTABLE]
  §5.7 after all DOMAIN sections. All lens.verify entries -> ADDRESSED or OPEN.
  OPEN -> ADVISORY-OPEN-LENS in register.

§16 -- PRIMARY DRIVER DERIVATION [IMMUTABLE]
  [Rules 1-7: see V-01 §16 for full text. Must be reproduced verbatim in deployment.]

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  Each §5.7 row carries Applicability (HIGH/MEDIUM/LOW) specific to this artifact.
  NOT inherited from role definition. Assigned at table-population time.
  HIGH -> ADDRESSED required; OPEN -> ADVISORY-OPEN-LENS
  MEDIUM -> OPEN -> ADVISORY-LOW
  LOW -> OPEN acceptable

§18 -- DOMAIN COVERAGE CERTIFICATION [IMMUTABLE]
  Formal predicate notation. Execute after §5.7 is complete.

  Let S = §1a ARTIFACT DOMAIN INVENTORY (domain set, |S| pre-declared in §1a)
  Let R(d) = {role r | Applicability(r, d) = HIGH in §5.7}    for each d in S
  Let K(d) = |R(d)|

  For each d in S:
    K(d) >= 1  -->  d is COVERED
    K(d) = 0   -->  d is ADVISORY-GAP

  §5.8 must emit a COUNT ASSERTION immediately after the domain table:
    "§5.8 certified [N] domains, [M] ADVISORY-GAP identified."
    N must equal |S| (the cardinality declared in §1a). A count mismatch
    indicates a missing domain row and is a protocol error.

  Each ADVISORY-GAP domain d -> ACTION ITEM REGISTER:
    Domain: d, K(d) = 0, Reason: [no HIGH-applicability reviewer covers d],
    Disposition: ADVISORY-GAP
  §5.8 emits no gate verdict, no local ledger row.

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  PHASE 1: Complete all dimension rows first.
  PHASE 2: Emit DIMENSION TABLE LOCKED sentinel.
  NH TESTIMONY follows (derived from locked table only).
  g_null derivation: BUILD-WINS majority -> PASS; STATUS-QUO-WINS majority -> FAIL;
  else CONDITIONAL. GOpen consistent with derivation or state override.

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

Review Parameters: Artifact: {{artifact_id}} | Depth: {{depth}} | Reviewer set: {{reviewer_set}}

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

---

## §0 -- CHALLENGER PRE-GATE

Contract: DISPOSITION_CONTRACT v1

| Dimension | Current-State Score | Proposed-State Score | Differential | Per-Dim Verdict |
|-----------|--------------------|--------------------|--------------|-----------------|
| [DIM_1] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_2] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |

**DIMENSION TABLE LOCKED**

**§0 Table Majority**: [BUILD-WINS / STATUS-QUO-WINS / TIED]
**g_null(initial) candidate**: [PASS / CONDITIONAL / FAIL]

**NH TESTIMONY**: [Derived from locked table only. No off-table assessments.]

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [One sentence.]

| Dimension | Status Quo | Build | Hybrid |
|-----------|-----------|-------|--------|
| [DIM_A] | [score] | [score] | [score] |
| **Total** | [sum] | [sum] | [sum] |

**NULL HYPOTHESIS DERIVATION RULE**: Build > Status Quo AND Build > Hybrid -> PASS.

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**g_null(initial)**: [copy GOpen]

*Local Gate Ledger Row*: | BRACKET OPENING | GOpen | [verdict] | [class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1

**CH-ID Response Table**:

| CH-ID | Challenge Claim | Response | Status |
|-------|----------------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Alternatives Re-score**:

| Dimension | Status Quo | Build | Hybrid |
|-----------|-----------|-------|--------|
| [DIM_A] | [re-score] | [re-score] | [re-score] |
| **Total** | [sum] | [sum] | [sum] |

| F-ID | Finding | Severity |
|------|---------|---------|
| F-01 | [FINDING] | [HIGH / MEDIUM / LOW] |
| F-02 | [FINDING] | [HIGH / MEDIUM / LOW] |

**Section Severity**: [worst(findings)]
**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

*Local Gate Ledger Row*: | DOMAIN | G_domain | [verdict] | [class] |

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

**G_domain Aggregate confirmed**: [copy]
**g_null(post-domain)**: [worst-case(G_domain_agg, g_null(initial))]

---

## §3.8 -- CH-ID SATURATION CHECK

| CH-ID | DOMAIN Status | SATURATED? |
|-------|--------------|-----------|
| CH-001 | [status] | [YES / NO] |
| CH-002 | [status] | [YES / NO] |

**Saturation status**: [SATURATED / UNSATURATED]

---

## §5.7 -- LENS COVERAGE TABLE

| Role | Lens Dimension | Applicability | Status | ADVISORY-OPEN-LENS? |
|------|---------------|--------------|--------|---------------------|
| [ROLE] | [lens.verify entry] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES/NO] |
| [LIFECYCLE_ROLE] | [lens.verify entry] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES/NO] |

---

## §5.8 -- DOMAIN COVERAGE CERTIFICATION

*(Formal predicate per §18. S from §1a, |S| pre-declared. R(d) and K(d) computed
from §5.7 Applicability fields.)*

| d (domain from §1a) | R(d) = {roles with HIGH applicability} | K(d) = |R(d)| | Status |
|--------------------|--------------------------------------|---------------|--------|
| [DOMAIN_1] | {[ROLE] or empty} | [N] | [COVERED / ADVISORY-GAP] |
| [DOMAIN_2] | {[ROLE] or empty} | [N] | [COVERED / ADVISORY-GAP] |
| [DOMAIN_3] | {[ROLE] or empty} | [N] | [COVERED / ADVISORY-GAP] |

**COUNT ASSERTION**: §5.8 certified [N] domains, [M] ADVISORY-GAP identified.
*(N must equal |S| = [value from §1a]. If N != |S|: protocol error -- revisit §1a.)*

*(ADVISORY-GAP rows -> ACTION ITEM REGISTER per §18.)*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Saturation confirmed: [SATURATED per §3.8]

**CH-ID Response Table**:

| CH-ID | Challenge Claim | Response | Status |
|-------|----------------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

| F-ID | Finding | Severity |
|------|---------|---------|
| F-01 | [FINDING] | [HIGH / MEDIUM / LOW] |
| F-02 | [FINDING] | [HIGH / MEDIUM / LOW] |

**Section Severity**: [worst(findings)]
**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]

*Local Gate Ledger Row*: | LIFECYCLE | G_lifecycle | [verdict] | [class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

| CH-ID | G_domain | G_lifecycle | Final Status |
|-------|---------|------------|--------------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] |

**Override invoked**: [YES / NO]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**g_null(final)**: [worst-case(G_lifecycle, g_null(post-domain))]

*Local Gate Ledger Row*: | BRACKET CLOSING | GClose | [verdict] | [class] |

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

| §1 Surface | Status | Finding Ref |
|------------|--------|-------------|
| [SURFACE] | [COVERED / GAP] | [F-ID] |

**§5.5 Signal**: [COVERED / PARTIAL]

---

## GATE VECTOR TABLE

| Gate | Verdict | Contract Cite |
|------|---------|---------------|
| GOpen | [copy] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [copy] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [copy] | DISPOSITION_CONTRACT v1 |
| GClose | [copy] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**g_null Progression**: initial=[_] -> post-domain=[_] -> final=[_]
**Conflicts**: [None detected / describe]
**Convergence**: [None / describe]

---

## DISPOSITION

**Gate vector**: GOpen=[_] G_domain_agg=[_] G_lifecycle=[_] GClose=[_]
**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Primary Driver** *(per §16)*: [Gate]

---

## ACTION ITEM REGISTER

| Source | Item | Class | Owner | Resolution |
|--------|------|-------|-------|-----------|
| CH-001 | [item] | [class] | [ROLE] | [criterion] |
| ADVISORY-OPEN-LENS | [lens dim] | ADVISORY-OPEN-LENS | [ROLE] | [when ADDRESSED] |
| ADVISORY-GAP | [§5.5 surface] | ADVISORY-GAP | [ROLE] | [when COVERED] |
| ADVISORY-GAP | [§5.8 domain / K(d)=0] | ADVISORY-GAP | [ROLE] | [when K(d)>=1] |

---

**Artifact to review:**

{{artifact}}

---

## V-04

**Axes**: Lifecycle emphasis + Output format (two-axis) -- V-01 COUNT BINDING (C-35)
+ V-02 TYPED ASSERTION BLOCK (C-33 -> C-34).
**Hypothesis**: V-01 secures C-35 by binding dimension_count and requiring NH TESTIMONY
to reference it by name. V-02 secures C-33 by requiring a verbatim surface_anchor in
each §5.7 assertion block. Together, the two mechanisms address all three criteria: C-35
via count binding, C-33 via typed assertion with verbatim anchor, C-34 as downstream
consequence of valid §17 source data in §5.8. Predicted: 225/225.

---

depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit
any pre-printed heading, label, field, formula, or structural element. Do not add
sections between pre-printed headers. If a field cannot be filled, write
`[N/A -- reason]`.

---

```
==============================================================================
IMMUTABLE PROTOCOL BLOCK -- read all sections before executing any reviewer
==============================================================================

DISPOSITION_CONTRACT v1

§1 -- SCOPE ENUMERATION
  IN-SCOPE surfaces: [enumerate exhaustively -- cited in §5.5]
  OUT-OF-SCOPE: [surface -- reason, or "None"]
§1 COMPLETE

§1a -- ARTIFACT DOMAIN INVENTORY
  1. [DOMAIN_1]
  2. [DOMAIN_2]
  3. [DOMAIN_3]
§1a COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions commitment. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose = FAIL OR any Gi = FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst-case(all G_domain verdicts). FAIL > CONDITIONAL > PASS.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  CH-IDs assigned in Bracket Opening. All sections carry CH-ID response table.
  PASS prohibited if any CH-ID OPEN.

==============================================================================

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row: | Section | Gate | Verdict | Class |. Emit after verdict. Copy verbatim.
  Excluded: §3.5, §3.8, §5.5, §5.7, §5.8.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  §0 -> Role Manifest -> Bracket Opening -> Domain(s) -> §3.5 -> §3.8 ->
  §5.7 -> §5.8 -> Lifecycle -> Bracket Closing -> §5.5 -> Gate Vector ->
  Cross-Role Signals -> Disposition -> Action Register. Reordering = violation.

§8 -- CH-ID SATURATION [IMMUTABLE]
  §3.8 gates LIFECYCLE (SATURATED required). GClose gates on FULLY SATURATED.

§9 -- NULL HYPOTHESIS PROGRESSION [IMMUTABLE]
  g_null(initial) = GOpen. g_null(post-domain) = worst-case(G_domain_agg, Stage 1).
  g_null(final) = worst-case(G_lifecycle, Stage 2). GClose = g_null(final) or override.

§10 -- SCOPE COVERAGE [IMMUTABLE]
  §5.5 after Bracket Closing. GAP -> ADVISORY-GAP in register.

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Section Severity = worst(all finding severities). Derived; not editorial.

§15 -- LENS EXHAUSTION [IMMUTABLE]
  §5.7 after all DOMAIN sections. All lens.verify -> ADDRESSED or OPEN.
  OPEN -> ADVISORY-OPEN-LENS in register.

§16 -- PRIMARY DRIVER DERIVATION [IMMUTABLE]
  [Rules 1-7: see V-01 §16. Must be reproduced verbatim in deployment.]

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  Each §5.7 row carries a TYPED ASSERTION BLOCK (§17a):
    surface_anchor : verbatim text from §1 IN-SCOPE, in double quotes.
    rating_basis   : one sentence linking surface to lens dimension.
    rating         : HIGH, MEDIUM, or LOW.

  CITATION VALIDITY RULE (§17a): surface_anchor MUST contain text that appears
  verbatim in §1 IN-SCOPE. A row whose surface_anchor does not match §1 text
  verbatim is INVALID. Invalid rows must be corrected before §18 executes.
  Generic role-archetype text ("this role covers architecture concerns") does not
  satisfy the verbatim-match requirement regardless of any other content.

  Coverage tiers:
    HIGH -> ADDRESSED required; OPEN -> ADVISORY-OPEN-LENS
    MEDIUM -> OPEN -> ADVISORY-LOW
    LOW -> OPEN acceptable

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  After §5.7 valid rows complete, execute §5.8 for each domain in §1a:
    Source: §17 `rating` field from typed assertion blocks.
    COVERED = at least one reviewer has rating: HIGH for this domain.
    ADVISORY-GAP = highest rating is MEDIUM or LOW or no reviewer.
  ADVISORY-GAP domains -> ACTION ITEM REGISTER.
  §5.8 emits no verdict, no ledger row.

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  PHASE 1: Complete all dimension rows first (min 2).
  Columns: Dimension | Current-State Score | Proposed-State Score |
           Differential | Per-Dim Verdict (BUILD-WINS / STATUS-QUO-WINS / TIED)

  PHASE 2: Emit DIMENSION TABLE LOCKED sentinel.

  PHASE 2a -- DIMENSION COUNT BINDING:
    Immediately after DIMENSION TABLE LOCKED, emit:
      dimension_count = N  (filled integer = number of rows in table above)
    This binding is referenced by name in the g_null derivation and in
    NH TESTIMONY opening sentence. A placeholder [N] is not a bound value.

  PHASE 3 -- NH TESTIMONY:
    Opening sentence required: "Based on dimension_count=[bound value] dimension
    rows in the locked table, ..."
    NH TESTIMONY is derived from locked table only. Off-table assessments are
    structurally inadmissible for g_null derivation.

  g_null(initial) derivation rule:
    Let B = BUILD-WINS count, S = STATUS-QUO-WINS count.
    B > dimension_count/2 -> PASS
    S > dimension_count/2 -> FAIL
    else -> CONDITIONAL
    Formula references dimension_count by name. GOpen consistent with derivation
    or names the overriding dimension(s).

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

Review Parameters: Artifact: {{artifact_id}} | Depth: {{depth}} | Reviewer set: {{reviewer_set}}

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

---

## §0 -- CHALLENGER PRE-GATE

Contract: DISPOSITION_CONTRACT v1

| Dimension | Current-State Score | Proposed-State Score | Differential | Per-Dim Verdict |
|-----------|--------------------|--------------------|--------------|-----------------|
| [DIM_1] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_2] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |

**DIMENSION TABLE LOCKED**

**dimension_count = [N]**

**NH TESTIMONY**: "Based on dimension_count=[N] dimension rows in the locked table,
..." [Continue. No off-table assessments.]

**§0 derivation**: B=[_] S=[_] dimension_count=[N].
B > dimension_count/2? [YES/NO]. S > dimension_count/2? [YES/NO].
**g_null(initial) candidate**: [PASS / CONDITIONAL / FAIL]

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [One sentence.]

| Dimension | Status Quo | Build | Hybrid |
|-----------|-----------|-------|--------|
| [DIM_A] | [score] | [score] | [score] |
| **Total** | [sum] | [sum] | [sum] |

**NULL HYPOTHESIS DERIVATION RULE**: Build > SQ AND Build > Hybrid -> PASS.

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |

**GOpen Verdict**: [must equal §0 candidate or state override]
**g_null(initial)**: [copy GOpen]

*Local Gate Ledger Row*: | BRACKET OPENING | GOpen | [verdict] | [class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1

**CH-ID Response Table**:

| CH-ID | Claim | Response | Status |
|-------|-------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Alternatives Re-score**:

| Dimension | Status Quo | Build | Hybrid |
|-----------|-----------|-------|--------|
| [DIM_A] | [re-score] | [re-score] | [re-score] |
| **Total** | [sum] | [sum] | [sum] |

| F-ID | Finding | Severity |
|------|---------|---------|
| F-01 | [FINDING] | [HIGH / MEDIUM / LOW] |
| F-02 | [FINDING] | [HIGH / MEDIUM / LOW] |

**Section Severity**: [worst(findings)]
**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

*Local Gate Ledger Row*: | DOMAIN | G_domain | [verdict] | [class] |

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

**G_domain Aggregate**: [copy]
**g_null(post-domain)**: [worst-case(G_domain_agg, g_null(initial))]

---

## §3.8 -- CH-ID SATURATION CHECK

| CH-ID | DOMAIN Status | SATURATED? |
|-------|--------------|-----------|
| CH-001 | [status] | [YES / NO] |
| CH-002 | [status] | [YES / NO] |

**Saturation status**: [SATURATED / UNSATURATED]

---

## §5.7 -- LENS COVERAGE TABLE

*(Per §17a: each row carries typed assertion block. surface_anchor must be verbatim
from §1. Invalid rows -> rewrite before §18.)*

| Role | Lens Dimension | Assertion Block | Status | ADVISORY? |
|------|---------------|-----------------|--------|-----------|
| [ROLE] | [lens.verify] | surface_anchor: "[verbatim §1 text]" / rating_basis: "[sentence]" / rating: [H/M/L] | [ADDRESSED / OPEN] | [YES/NO] |
| [LC_ROLE] | [lens.verify] | surface_anchor: "[verbatim §1 text]" / rating_basis: "[sentence]" / rating: [H/M/L] | [ADDRESSED / OPEN] | [YES/NO] |

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

*(Source: `rating` field from §5.7 typed assertion blocks per §18.)*

| Domain (§1a) | Max rating | Gap Status | Disposition |
|-------------|-----------|------------|-------------|
| [DOMAIN_1] | [HIGH/MED/LOW/none] | [COVERED / ADVISORY-GAP] | [-- / ACTION REGISTER] |
| [DOMAIN_2] | [HIGH/MED/LOW/none] | [COVERED / ADVISORY-GAP] | [-- / ACTION REGISTER] |

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1

**CH-ID Response Table**:

| CH-ID | Claim | Response | Status |
|-------|-------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

| F-ID | Finding | Severity |
|------|---------|---------|
| F-01 | [FINDING] | [HIGH / MEDIUM / LOW] |
| F-02 | [FINDING] | [HIGH / MEDIUM / LOW] |

**Section Severity**: [worst(findings)]
**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]

*Local Gate Ledger Row*: | LIFECYCLE | G_lifecycle | [verdict] | [class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

| CH-ID | G_domain | G_lifecycle | Final Status |
|-------|---------|------------|--------------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] |

**Override invoked**: [YES / NO]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**g_null(final)**: [worst-case(G_lifecycle, g_null(post-domain))]

*Local Gate Ledger Row*: | BRACKET CLOSING | GClose | [verdict] | [class] |

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

| §1 Surface | Status | Finding Ref |
|------------|--------|-------------|
| [SURFACE] | [COVERED / GAP] | [F-ID] |

**§5.5 Signal**: [COVERED / PARTIAL]

---

## GATE VECTOR TABLE

| Gate | Verdict | Contract Cite |
|------|---------|---------------|
| GOpen | [copy] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [copy] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [copy] | DISPOSITION_CONTRACT v1 |
| GClose | [copy] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**g_null Progression**: initial=[_] -> post-domain=[_] -> final=[_]
**Conflicts**: [None / describe]
**Convergence**: [None / describe]

---

## DISPOSITION

**Gate vector**: GOpen=[_] G_domain_agg=[_] G_lifecycle=[_] GClose=[_]
**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Primary Driver** *(per §16)*: [Gate]

---

## ACTION ITEM REGISTER

| Source | Item | Class | Owner | Resolution |
|--------|------|-------|-------|-----------|
| CH-001 | [item] | [class] | [ROLE] | [criterion] |
| ADVISORY-OPEN-LENS | [lens dim] | ADVISORY-OPEN-LENS | [ROLE] | [when ADDRESSED] |
| ADVISORY-GAP | [§5.5 surface] | ADVISORY-GAP | [ROLE] | [when COVERED] |
| ADVISORY-GAP | [§5.8 domain] | ADVISORY-GAP | [ROLE] | [when HIGH reviewer found] |

---

**Artifact to review:**

{{artifact}}

---

## V-05

**Axes**: Lifecycle emphasis + Output format + Phrasing register (three-axis) --
V-01 COUNT BINDING (C-35) + V-02 TYPED ASSERTION BLOCK (C-33) + V-03 FORMAL
PREDICATE NOTATION (C-34 with independent enforcement chain).
**Hypothesis**: V-04 achieves C-33 + C-34 via C-33 source data. V-05 adds V-03's
formal predicate notation (K(d) = |R(d)|, count assertion) as a third independent
enforcement mechanism for C-34. With V-03's formal predicate, C-34 is satisfied even
if §17 source data is imperfect -- the count assertion forces enumeration regardless.
The three axes form independent chains: COUNT BINDING -> g_null derivation (C-35);
TYPED ASSERTION BLOCK -> verbatim anchor check (C-33); FORMAL PREDICATE + COUNT
ASSERTION -> domain enumeration completeness (C-34). No single-mechanism failure
cascades to all three. Predicted: 225/225.

---

depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit
any pre-printed heading, label, field, formula, or structural element. Do not add
sections between pre-printed headers. If a field cannot be filled, write
`[N/A -- reason]`.

---

```
==============================================================================
IMMUTABLE PROTOCOL BLOCK -- read all sections before executing any reviewer
==============================================================================

DISPOSITION_CONTRACT v1

§1 -- SCOPE ENUMERATION
  IN-SCOPE surfaces: [enumerate exhaustively -- cited in §5.5]
  OUT-OF-SCOPE: [surface -- reason, or "None"]
§1 COMPLETE

§1a -- ARTIFACT DOMAIN INVENTORY
[Immediately after §1 COMPLETE. Atomic domain concerns from §1 surfaces.
Emit cardinality after list.]
  1. [DOMAIN_1]
  2. [DOMAIN_2]
  3. [DOMAIN_3]
|S| = [N]
§1a COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions commitment. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose = FAIL OR any Gi = FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst-case(all G_domain verdicts). FAIL > CONDITIONAL > PASS.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  CH-IDs in Bracket Opening. All sections carry CH-ID response table.
  PASS prohibited if any CH-ID OPEN.

==============================================================================

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row: | Section | Gate | Verdict | Class |. Emit after verdict. Copy verbatim.
  Excluded: §3.5, §3.8, §5.5, §5.7, §5.8.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  §0 -> Role Manifest -> Bracket Opening -> Domain(s) -> §3.5 -> §3.8 ->
  §5.7 -> §5.8 -> Lifecycle -> Bracket Closing -> §5.5 -> Gate Vector ->
  Cross-Role Signals -> Disposition -> Action Register. Reordering = violation.

§8 -- CH-ID SATURATION [IMMUTABLE]
  §3.8 gates LIFECYCLE. GClose gates on FULLY SATURATED.

§9 -- NULL HYPOTHESIS PROGRESSION [IMMUTABLE]
  g_null(initial) = GOpen. g_null(post-domain) = worst-case(G_domain_agg, Stage 1).
  g_null(final) = worst-case(G_lifecycle, Stage 2). GClose = g_null(final) or override.

§10 -- SCOPE COVERAGE [IMMUTABLE]
  §5.5 after Bracket Closing. GAP -> ADVISORY-GAP.

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Section Severity = worst(all findings). No editorial assignment.

§15 -- LENS EXHAUSTION [IMMUTABLE]
  §5.7 after DOMAIN sections. All lens.verify -> ADDRESSED or OPEN.
  OPEN -> ADVISORY-OPEN-LENS in register.

§16 -- PRIMARY DRIVER DERIVATION [IMMUTABLE]
  [Rules 1-7: see V-01 §16. Reproduce verbatim in deployment.]

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  §17a TYPED ASSERTION BLOCK -- each §5.7 row carries:
    surface_anchor : verbatim text from §1 IN-SCOPE (in double quotes).
    rating_basis   : one sentence linking surface to lens dimension.
    rating         : HIGH, MEDIUM, or LOW.

  CITATION VALIDITY RULE: surface_anchor must contain verbatim §1 text.
  Generic text does not satisfy verbatim-match. Invalid rows -> rewrite before §18.

  Coverage: HIGH -> ADDRESSED required; OPEN -> ADVISORY-OPEN-LENS.
            MEDIUM -> OPEN -> ADVISORY-LOW. LOW -> OPEN acceptable.

§18 -- DOMAIN COVERAGE CERTIFICATION [IMMUTABLE]
  §17a TYPED ASSERTION BLOCK source + FORMAL PREDICATE enforcement:

  Let S = §1a ARTIFACT DOMAIN INVENTORY, |S| pre-declared.
  Let R(d) = {role r | Applicability(r, d) = HIGH}  from §5.7 `rating` fields.
  Let K(d) = |R(d)|

  For each d in S:
    K(d) >= 1  -->  COVERED
    K(d) = 0   -->  ADVISORY-GAP

  COUNT ASSERTION (required): "§5.8 certified [N] domains, [M] ADVISORY-GAP."
  N must equal |S|. Count mismatch = protocol error.

  §17a provides the HIGH/MEDIUM/LOW source for R(d). The formal predicate and the
  count assertion provide independent enforcement: even if §17a source is incomplete,
  K(d) = 0 detection covers any domain with no HIGH reviewer.

  ADVISORY-GAP domains -> ACTION ITEM REGISTER: domain d, K(d) = 0, reason, class ADVISORY-GAP.
  §5.8 emits no verdict, no ledger row.

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  PHASE 1: All dimension rows first (min 2).
  Columns: Dimension | Current-State Score | Proposed-State Score | Differential |
           Per-Dim Verdict (BUILD-WINS / STATUS-QUO-WINS / TIED)

  PHASE 2: Emit DIMENSION TABLE LOCKED sentinel.

  PHASE 2a -- DIMENSION COUNT BINDING:
    Emit: dimension_count = N  (filled integer, equals number of table rows).
    Referenced by name in g_null derivation formula and NH TESTIMONY opening sentence.
    A placeholder [N] is not a bound value and does not satisfy this requirement.

  PHASE 3 -- NH TESTIMONY:
    Opening sentence: "Based on dimension_count=[bound value] dimension rows
    in the locked table, ..."
    Off-table assessments structurally inadmissible for g_null derivation.

  g_null(initial) derivation:
    B = BUILD-WINS count, S = STATUS-QUO-WINS count.
    B > dimension_count/2 -> PASS
    S > dimension_count/2 -> FAIL
    else -> CONDITIONAL
    Formula cites dimension_count by name. GOpen consistent or override named.

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

Review Parameters: Artifact: {{artifact_id}} | Depth: {{depth}} | Reviewer set: {{reviewer_set}}

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

---

## §0 -- CHALLENGER PRE-GATE

Contract: DISPOSITION_CONTRACT v1

| Dimension | Current-State Score | Proposed-State Score | Differential | Per-Dim Verdict |
|-----------|--------------------|--------------------|--------------|-----------------|
| [DIM_1] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_2] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |

**DIMENSION TABLE LOCKED**

**dimension_count = [N]**

**NH TESTIMONY**: "Based on dimension_count=[N] dimension rows in the locked table,
..." [Continue. Off-table assessments structurally inadmissible.]

**§0 derivation**: B=[_] S=[_] dimension_count=[N].
B > [N]/2? [YES/NO]. S > [N]/2? [YES/NO].
**g_null(initial) candidate**: [PASS / CONDITIONAL / FAIL]

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [One sentence.]

| Dimension | Status Quo | Build | Hybrid |
|-----------|-----------|-------|--------|
| [DIM_A] | [score] | [score] | [score] |
| **Total** | [sum] | [sum] | [sum] |

**NULL HYPOTHESIS DERIVATION RULE**: Build > SQ AND Build > Hybrid -> PASS.

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |

**GOpen Verdict**: [must equal §0 candidate or state override]
**g_null(initial)**: [copy GOpen]

*Local Gate Ledger Row*: | BRACKET OPENING | GOpen | [verdict] | [class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1

**CH-ID Response Table**:

| CH-ID | Claim | Response | Status |
|-------|-------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Alternatives Re-score**:

| Dimension | Status Quo | Build | Hybrid |
|-----------|-----------|-------|--------|
| [DIM_A] | [re-score] | [re-score] | [re-score] |
| **Total** | [sum] | [sum] | [sum] |

| F-ID | Finding | Severity |
|------|---------|---------|
| F-01 | [FINDING] | [HIGH / MEDIUM / LOW] |
| F-02 | [FINDING] | [HIGH / MEDIUM / LOW] |

**Section Severity**: [worst(findings)]
**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

*Local Gate Ledger Row*: | DOMAIN | G_domain | [verdict] | [class] |

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

**G_domain Aggregate**: [copy]
**g_null(post-domain)**: [worst-case(G_domain_agg, g_null(initial))]

---

## §3.8 -- CH-ID SATURATION CHECK

| CH-ID | DOMAIN Status | SATURATED? |
|-------|--------------|-----------|
| CH-001 | [status] | [YES / NO] |
| CH-002 | [status] | [YES / NO] |

**Saturation status**: [SATURATED / UNSATURATED]

---

## §5.7 -- LENS COVERAGE TABLE

*(§17a typed assertion blocks. surface_anchor verbatim from §1. Invalid -> rewrite.
Source for §18 K(d) computation.)*

| Role | Lens Dimension | Assertion Block | Status | ADVISORY? |
|------|---------------|-----------------|--------|-----------|
| [ROLE] | [lens.verify] | surface_anchor: "[verbatim §1 text]" / rating_basis: "[sentence]" / rating: [H/M/L] | [ADDRESSED / OPEN] | [YES/NO] |
| [LC_ROLE] | [lens.verify] | surface_anchor: "[verbatim §1 text]" / rating_basis: "[sentence]" / rating: [H/M/L] | [ADDRESSED / OPEN] | [YES/NO] |

---

## §5.8 -- DOMAIN COVERAGE CERTIFICATION

*(Formal predicate per §18. S from §1a with |S| pre-declared.
R(d) from §5.7 typed assertion `rating` fields. Count assertion required.)*

| d (§1a domain) | R(d) = {roles, rating=HIGH} | K(d) | Status |
|---------------|----------------------------|------|--------|
| [DOMAIN_1] | {[ROLE or empty set]} | [N] | [COVERED / ADVISORY-GAP] |
| [DOMAIN_2] | {[ROLE or empty set]} | [N] | [COVERED / ADVISORY-GAP] |
| [DOMAIN_3] | {[ROLE or empty set]} | [N] | [COVERED / ADVISORY-GAP] |

**COUNT ASSERTION**: §5.8 certified [N] domains, [M] ADVISORY-GAP identified.
*(N must equal |S|=[value from §1a]. If N != |S|: protocol error.)*

*(ADVISORY-GAP rows -> ACTION ITEM REGISTER: domain d, K(d)=0, reason, ADVISORY-GAP.)*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1

**CH-ID Response Table**:

| CH-ID | Claim | Response | Status |
|-------|-------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

| F-ID | Finding | Severity |
|------|---------|---------|
| F-01 | [FINDING] | [HIGH / MEDIUM / LOW] |
| F-02 | [FINDING] | [HIGH / MEDIUM / LOW] |

**Section Severity**: [worst(findings)]
**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]

*Local Gate Ledger Row*: | LIFECYCLE | G_lifecycle | [verdict] | [class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

| CH-ID | G_domain | G_lifecycle | Final Status |
|-------|---------|------------|--------------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] |

**Override invoked**: [YES / NO]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**g_null(final)**: [worst-case(G_lifecycle, g_null(post-domain))]

*Local Gate Ledger Row*: | BRACKET CLOSING | GClose | [verdict] | [class] |

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

| §1 Surface | Status | Finding Ref |
|------------|--------|-------------|
| [SURFACE] | [COVERED / GAP] | [F-ID] |

**§5.5 Signal**: [COVERED / PARTIAL]

---

## GATE VECTOR TABLE

| Gate | Verdict | Contract Cite |
|------|---------|---------------|
| GOpen | [copy] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [copy] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [copy] | DISPOSITION_CONTRACT v1 |
| GClose | [copy] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**g_null Progression**: initial=[_] -> post-domain=[_] -> final=[_]
**Conflicts**: [None / describe]
**Convergence**: [None / describe]

---

## DISPOSITION

**Gate vector**: GOpen=[_] G_domain_agg=[_] G_lifecycle=[_] GClose=[_]
**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Primary Driver** *(per §16)*: [Gate]

---

## ACTION ITEM REGISTER

| Source | Item | Class | Owner | Resolution |
|--------|------|-------|-------|-----------|
| CH-001 | [item] | [class] | [ROLE] | [criterion] |
| ADVISORY-OPEN-LENS | [lens dim] | ADVISORY-OPEN-LENS | [ROLE] | [when ADDRESSED] |
| ADVISORY-GAP | [§5.5 surface] | ADVISORY-GAP | [ROLE] | [when COVERED] |
| ADVISORY-GAP | [§5.8 domain / K(d)=0] | ADVISORY-GAP | [ROLE] | [when K(d)>=1] |

---

**Artifact to review:**

{{artifact}}
