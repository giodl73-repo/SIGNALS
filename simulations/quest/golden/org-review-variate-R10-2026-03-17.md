---
skill: quest-variate
skill_target: org-review
date: 2026-03-17
round: 10
rubric: org-review-rubric-v11-2026-03-16.md
---

# org-review -- Variate R10

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis and three-axis combinations (V-04, V-05).

**R10 design target**: V-05 R11 scores 210/225 under v11 (Perfect under v10). Under
v11 the three new criteria (C-33, C-34, C-35) differentiate them. The R11 ceiling
is 210/225: all five R11 variants miss C-33/C-34/C-35 simultaneously. The R10
target is 225/225 -- all three new criteria pass together in at least one variant.

**Gap analysis from R11 under v11:**

| Criterion | R11 V-05 | What it requires |
|-----------|----------|-----------------|
| C-33 Lens Applicability Rating Pre-committed | FAIL | Each LENS COVERAGE TABLE row carries an artifact-specific HIGH/MEDIUM/LOW applicability rating; rating is the basis for ADDRESSED/OPEN determination; not inferred from generic role definition |
| C-34 ADVISORY-GAP Domain Coverage Pre-committed | vacuous (C-33 absent) | After lens table, gap-check names every artifact domain with no HIGH-applicability reviewer; each classified ADVISORY-GAP in action register; pre-committed protocol |
| C-35 Null Hypothesis Challenger Dimension Comparison Table | FAIL | Challenger's NH evaluation uses structured dimension table (current-state / proposed-state / differential / per-dim verdict); g_null derivable from table values without reading prose |

C-34 is vacuous for all R11 variants: C-31 PASS (lens table present) but C-33 FAIL
(no applicability rating column) means there is no HIGH-applicability tier for the
domain gap-check to reference. Without the applicability tier, §18 has no source
data -- C-34 is effectively vacuous.

**R10 variation axes:**

- V-01: Inertia framing (single axis) -- §0 CHALLENGER NULL HYPOTHESIS DIMENSION TABLE
  protocol pre-committed; challenger opens BRACKET OPENING with a structured
  dimension comparison table before any prose challenge claims. C-35 only.

- V-02: Output format (single axis) -- §17 LENS APPLICABILITY PROTOCOL adds a fourth
  Applicability column to the LENS COVERAGE TABLE; §18 DOMAIN COVERAGE GAP-CHECK
  protocol pre-committed, runs at §5.8 after §5.7. C-33 + C-34 only.

- V-03: Lifecycle emphasis (single axis) -- §0 CHALLENGER NULL HYPOTHESIS DIMENSION
  TABLE with explicit binding declared in §9 NULL HYPOTHESIS PROGRESSION CONTRACT:
  g_null(initial) must be consistent with the §0 table verdict. Tighter traceability
  from table format to GOpen. C-35 with §9 extension only.

- V-04: Inertia framing + Output format (two-axis) -- V-01 + V-02 merged. §0 + §17 +
  §18 all present. All three new criteria.

- V-05: Inertia framing + Output format + Lifecycle emphasis (three-axis) -- V-04
  plus the preamble dependency chain co-locating §17/§18/§0 with explicit cross-
  references: §17 feeds §18; §0 feeds GOpen feeds §9 Stage 1. Strongest base.

**R10 single-axis predictions:**
- V-01 -> C-35 PASS (dimension table), C-33 FAIL, C-34 vacuous. Predicted: 215/225
- V-02 -> C-33 PASS (applicability column), C-34 PASS (domain gap-check), C-35 FAIL.
  Predicted: 220/225
- V-03 -> C-35 PASS (table + §9 binding), C-33 FAIL, C-34 vacuous. Predicted: 215/225

**R10 two-axis and three-axis predictions:**
- V-04 -> 225/225 via independent §0 + §17 + §18
- V-05 -> 225/225 via §0 + §17 + §18 + dependency chain

---

## V-01

**Axis**: Inertia framing (single axis) -- §0 CHALLENGER NULL HYPOTHESIS DIMENSION
TABLE pre-committed; challenger opens with structured comparison table before challenge
claims; no §17/§18 additions; C-35 only.
**Hypothesis**: R11 V-05 misses C-35 because the challenger's null hypothesis is
expressed in prose ("Null hypothesis strength: HIGH / MEDIUM / LOW"). The dimension
comparison table is absent. Adding §0 as a pre-committed preamble protocol and
replacing the single NH strength field with a structured table satisfies C-35 while
leaving C-31/C-33/C-34 unchanged. C-33 FAIL (no applicability column), C-34 vacuous.
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

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical execution sequence:
  §0 Challenger Pre-Gate -> Role Manifest -> Bracket Opening -> Domain(s) ->
  §3.5 Domain-Aggregate Checkpoint -> §3.8 CH-ID Saturation Check ->
  §5.7 Lens Coverage Table -> Lifecycle -> Bracket Closing ->
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

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  The challenger's null hypothesis evaluation in BRACKET OPENING must use a
  structured dimension comparison table before any challenge claims are issued.
  Table columns: Dimension | Current-State Score | Proposed-State Score |
                 Differential | Per-Dim Verdict
  Minimum 2 dimensions required.
  Per-Dim Verdict: BUILD-WINS / STATUS-QUO-WINS / TIED
  Current-State Score and Proposed-State Score: numeric (0-10) or labeled
  (HIGH/MEDIUM/LOW/NONE).
  g_null(initial) derivation rule:
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

*(Per §0 protocol: populated before BRACKET OPENING testimony begins.)*

**Null Hypothesis Dimension Comparison Table**:

| Dimension | Current-State Score | Proposed-State Score | Differential | Per-Dim Verdict |
|-----------|--------------------|--------------------|--------------|-----------------|
| [DIM_1 -- e.g., switching cost for team] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_2 -- e.g., value delivered without building] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_3 -- optional] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |

**§0 Table Majority**: [BUILD-WINS / STATUS-QUO-WINS / TIED -- count Per-Dim Verdicts]
**g_null(initial) candidate from §0**: [PASS / CONDITIONAL / FAIL -- derived from majority rule]

*(If GOpen contradicts this candidate, state the override justification below. Otherwise
GOpen must equal the §0-derived candidate.)*

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

*(Produced after all DOMAIN sections complete, before LIFECYCLE. Informational only --
no gate verdict, no local ledger row per §6 exclusion list.)*

| Role | Lens Dimension | Status | ADVISORY-OPEN-LENS? |
|------|---------------|--------|---------------------|
| [ROLE] | [lens.verify entry 1] | [ADDRESSED / OPEN] | [YES if OPEN / NO] |
| [ROLE] | [lens.verify entry 2] | [ADDRESSED / OPEN] | [YES if OPEN / NO] |
| [LIFECYCLE_ROLE] | [lens.verify entry] | [ADDRESSED / OPEN] | [YES if OPEN / NO] |

*(All ADVISORY-OPEN-LENS entries appear in ACTION ITEM REGISTER as ADVISORY-OPEN-LENS
items per §15.)*

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
ADVISORY-OPEN-LENS rows from §5.7. ADVISORY-GAP rows from §5.5. Do not re-derive.)*

| CH-ID / Source | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|---------------|-----------------|------------------|------------|---------------------|
| CH-001 | [derived from PARTIAL or HOLDS status] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE] | [Falsifiable criterion] |
| CH-002 | [Item 2] | [class] | [ROLE] | [Criterion] |
| ADVISORY-OPEN-LENS | [lens dimension not covered in review] | ADVISORY-OPEN-LENS | [ROLE] | [When ADDRESSED] |
| ADVISORY-GAP | [§1 surface with no reviewer finding] | ADVISORY-GAP | [ROLE] | [When COVERED] |
| ADVISORY-OBS | [advisory observation not sourced from CH-ID] | ADVISORY-OBS | [ROLE] | [Criterion] |

*Disposition class per §2: BLOCKED = must resolve before any commitment.
CONDITIONAL = must resolve before next lifecycle phase. ADVISORY = may defer.*

---

**Artifact to review:**

{{artifact}}

---

## V-02

**Axis**: Output format (single axis) -- §17 LENS APPLICABILITY PROTOCOL (C-33) and
§18 DOMAIN COVERAGE GAP-CHECK (C-34) added to preamble; Applicability column added to
§5.7 LENS COVERAGE TABLE; §5.8 DOMAIN COVERAGE GAP-CHECK section added; no §0 or C-35
changes.
**Hypothesis**: R11 V-05 misses C-33 because the LENS COVERAGE TABLE has only
ADDRESSED/OPEN columns with no per-row Applicability rating. Adding §17 as an immutable
protocol with a fourth Applicability column satisfies C-33. §18 then uses the
HIGH-applicability tier to run a domain gap-check, satisfying C-34. C-35 remains FAIL
(challenger still uses prose null hypothesis). Predicted: 220/225.

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
[§6 LOCAL GATE LEDGER PROTOCOL -- identical to V-01, with §5.8 added to
 exclusion list: "§5.8 Domain Coverage Gap-Check -- produces no verdict"]
[§7 SECTION ORDER CONTRACT -- as V-01, with §5.8 added after §5.7:
 "... §5.7 Lens Coverage Table -> §5.8 Domain Coverage Gap-Check ->
  Lifecycle -> ..."]
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
  §5.8 emits no gate verdict and no local ledger row (excluded from §6 per the
  exclusion list addition: "§5.8 Domain Coverage Gap-Check -- produces no verdict").
  §18 requires §17 Applicability ratings; §17 must be complete before §18 executes.

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

[Identical structure to V-01.]

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

**NULL HYPOTHESIS DERIVATION RULE**: [identical to V-01]

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
**g_null(initial)**: [copy GOpen verdict]

*Local Gate Ledger Row*: | BRACKET OPENING | GOpen | [verdict] | [class] |

---

## DOMAIN -- [ROLE_NAME]

[Identical structure to V-01.]

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

[Identical to V-01.]

---

## §3.8 -- CH-ID SATURATION CHECK

[Identical to V-01.]

---

## §5.7 -- LENS COVERAGE TABLE

*(Produced after all DOMAIN sections complete, before LIFECYCLE. Per §17, each row
carries an Applicability rating specific to this artifact. No verdict, no ledger row.)*

| Role | Lens Dimension | Applicability | Status | ADVISORY-OPEN-LENS? |
|------|---------------|--------------|--------|---------------------|
| [ROLE] | [lens.verify entry 1] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN / NO] |
| [ROLE] | [lens.verify entry 2] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN / NO] |
| [LIFECYCLE_ROLE] | [lens.verify entry] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN / NO] |

*(All HIGH-applicability OPEN entries -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.
MEDIUM-applicability OPEN entries -> ADVISORY-LOW. LOW-applicability OPEN: no action.)*

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

*(Executes after §5.7 per §18. No verdict, no ledger row per §6 exclusion list.)*

| Artifact Domain (from §1) | Max Applicability Tier | Coverage Status | ADVISORY-GAP? |
|--------------------------|----------------------|----------------|---------------|
| [DOMAIN_1] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [YES / NO] |
| [DOMAIN_2] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [YES / NO] |
| [DOMAIN_3] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [YES / NO] |

ADVISORY-GAP domains -> appended to ACTION ITEM REGISTER with domain name,
max tier found, reason no HIGH-applicability reviewer covers it, and
disposition class ADVISORY-GAP.

---

## LIFECYCLE -- [ROLE_NAME]

[Identical structure to V-01, with §5.7 Lens Coverage Table completion noted as
a prerequisite: "Received §5.7 Lens Coverage Table: [COMPLETE]".]

---

## BRACKET CLOSING -- CHALLENGER

[Identical structure to V-01.]

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

[Identical to V-01.]

---

## GATE VECTOR TABLE

[Identical to V-01.]

---

## CROSS-ROLE SIGNALS

[Identical structure to V-01, including g_null Progression Ledger.]

---

## DISPOSITION

[Identical structure to V-01, including §3 formula and §16 Primary Driver field.]

---

## ACTION ITEM REGISTER

*(CH-ID-sourced, ADVISORY-OPEN-LENS from §5.7, ADVISORY-GAP from §5.5 and §5.8.
Do not re-derive. Copy verbatim from local ledger rows.)*

| CH-ID / Source | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|---------------|-----------------|------------------|------------|---------------------|
| CH-001 | [derived from status] | [class] | [ROLE] | [Criterion] |
| CH-002 | [Item 2] | [class] | [ROLE] | [Criterion] |
| ADVISORY-OPEN-LENS | [HIGH-applicability lens not ADDRESSED] | ADVISORY-OPEN-LENS | [ROLE] | [When ADDRESSED] |
| ADVISORY-GAP (§5.5) | [§1 surface with no finding] | ADVISORY-GAP | [ROLE] | [When COVERED] |
| ADVISORY-GAP (§5.8) | [artifact domain with no HIGH-applicability reviewer] | ADVISORY-GAP | [ROLE] | [When a HIGH-applicability reviewer covers this domain] |
| ADVISORY-OBS | [advisory observation] | ADVISORY-OBS | [ROLE] | [Criterion] |

---

**Artifact to review:**

{{artifact}}

---

## V-03

**Axis**: Lifecycle emphasis (single axis) -- §0 CHALLENGER NULL HYPOTHESIS DIMENSION
TABLE plus §9 NULL HYPOTHESIS PROGRESSION CONTRACT extension that explicitly binds
GOpen to the §0 table verdict. Adds traceability requirement from table format to gate
verdict. C-35 only (no §17/§18).
**Hypothesis**: V-01 satisfies C-35 by adding §0 and requiring GOpen to be "consistent
with" the table derivation. V-03 strengthens this by explicitly amending §9 to state:
"g_null(initial) = GOpen, and GOpen must equal the §0 Dimension Table Majority verdict
unless an override is declared." This binds the table format directly into the
progression contract -- the §0 table is no longer a standalone pre-gate; it is the
structural source for Stage 1 of §9. Same predicted score as V-01 (215/225) but with
stronger traceability chain. Potential C-36 candidate: §9-anchored table binding.

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
[§7 SECTION ORDER CONTRACT -- as V-01, §0 added as first step:
 "§0 Challenger Pre-Gate -> Role Manifest -> Bracket Opening -> ..."]

[§8 CH-ID SATURATION REQUIREMENT -- identical to V-01]

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE] -- EXTENDED
  Stage 1: g_null(initial)     = GOpen
           BINDING: GOpen must equal the §0 Dimension Table Majority verdict
           unless an explicit override is declared with named justification.
           The §0 table is the structural source for Stage 1 -- g_null(initial)
           is derivable from the §0 table without reading prose testimony.
  Stage 2: g_null(post-domain) = worst-case(G_domain_agg, g_null(initial))
  Stage 3: g_null(final)       = worst-case(G_lifecycle, g_null(post-domain))
  GClose must equal g_null(final). Deviation requires explicit override with
  named justification. All three g_null values emitted as labeled fields at
  their respective checkpoints and summarized in Cross-Role Signals.
  Override chain: a GOpen override of §0 majority must be declared at §0;
  a GClose override of g_null(final) must be declared at BRACKET CLOSING.
  Both override declarations are independent and both are required when both
  apply.

[§10 SCOPE COVERAGE GATE PROTOCOL -- identical to V-01]
[§14 PER-FINDING SEVERITY CHAIN -- identical to V-01]
[§15 LENS EXHAUSTION PROTOCOL -- identical to V-01]
[§16 PRIMARY DRIVER DERIVATION CONTRACT -- identical to V-01]

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  The challenger's null hypothesis evaluation in BRACKET OPENING must use a
  structured dimension comparison table before any challenge claims are issued.
  Table columns: Dimension | Current-State Score | Proposed-State Score |
                 Differential | Per-Dim Verdict
  Minimum 2 dimensions required.
  Per-Dim Verdict: BUILD-WINS / STATUS-QUO-WINS / TIED
  §0 Table Majority verdict feeds Stage 1 of §9 (g_null(initial)):
    BUILD-WINS majority     -> GOpen candidate = PASS
    STATUS-QUO-WINS majority -> GOpen candidate = FAIL
    Mixed / TIED majority   -> GOpen candidate = CONDITIONAL
  GOpen must equal §0 Table Majority verdict. Override requires named
  justification citing the specific dimension(s) driving the override.
  The §0 table appears before BRACKET OPENING body; GOpen is stated after
  the §0 derivation and must be consistent with it.
  The §0 binding to §9 Stage 1 means: a scorer can verify g_null(initial)
  from the §0 table data alone, without reading any challenger prose.

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

[Identical structure to V-01.]

---

## §0 -- CHALLENGER PRE-GATE: NULL HYPOTHESIS DIMENSION TABLE

*(Per §0 protocol: populated before BRACKET OPENING testimony. GOpen is derived
from §0 Table Majority per §9 Stage 1 binding.)*

**Null Hypothesis Dimension Comparison Table**:

| Dimension | Current-State Score | Proposed-State Score | Differential | Per-Dim Verdict |
|-----------|--------------------|--------------------|--------------|-----------------|
| [DIM_1] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_2] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_3 -- optional] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |

**§0 Table Majority**: [BUILD-WINS / STATUS-QUO-WINS / TIED]
**g_null(initial) candidate from §0 -- §9 Stage 1 source**: [PASS / CONDITIONAL / FAIL]

*(GOpen must equal this value per §9 Stage 1 binding, or declare an override below.)*
**Override justification (if applicable)**: [N/A -- or name specific dimension(s) overriding majority]

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today -- one sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table** *(per C-16)*: [as V-01]

**NULL HYPOTHESIS DERIVATION RULE**: [as V-01]

**Challenge claims**: [as V-01]

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL -- must equal §0 candidate per §9 Stage 1
binding, unless override declared at §0]
**GOpen Reason**: [One sentence.]
**g_null(initial)**: [copy GOpen verdict -- confirms §9 Stage 1 = §0 table majority]

*Local Gate Ledger Row*: | BRACKET OPENING | GOpen | [verdict] | [class] |

---

[DOMAIN, §3.5, §3.8, §5.7, LIFECYCLE, BRACKET CLOSING, §5.5, GATE VECTOR TABLE,
CROSS-ROLE SIGNALS, DISPOSITION, ACTION ITEM REGISTER all identical to V-01]

**Artifact to review:**

{{artifact}}

---

## V-04

**Axis**: Inertia framing + Output format (two-axis) -- §0 (C-35) + §17 (C-33) +
§18 (C-34) all present; V-01 + V-02 merged; all three new criteria independently
targeted; §7 SECTION ORDER CONTRACT updated to include §0 and §5.8.
**Hypothesis**: The three new criteria are structurally independent (§0 activates at
pre-bracket challenger format time; §17 activates at lens-table-population time; §18
activates at domain-gap-check time). All three can coexist without interaction. V-01
satisfies C-35; V-02 satisfies C-33+C-34; V-04 merges both. V-05 R11 base (210/225)
plus all three new criteria = 225/225. Predicted: 225/225.

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
[§6 LOCAL GATE LEDGER PROTOCOL -- as V-01, with §5.8 added to exclusion list:
 "§5.8 Domain Coverage Gap-Check -- produces no verdict"]
[§7 SECTION ORDER CONTRACT -- updated for both §0 and §5.8:
 Canonical sequence: §0 Challenger Pre-Gate -> Role Manifest -> Bracket Opening ->
 Domain(s) -> §3.5 Domain-Aggregate Checkpoint -> §3.8 CH-ID Saturation Check ->
 §5.7 Lens Coverage Table -> §5.8 Domain Coverage Gap-Check -> Lifecycle ->
 Bracket Closing -> §5.5 Scope Coverage Reconciliation -> Gate Vector Table ->
 Cross-Role Signals -> Disposition -> Action Item Register
 Reordering is a contract violation.]
[§8 CH-ID SATURATION REQUIREMENT -- identical to V-01]
[§9 NULL HYPOTHESIS PROGRESSION CONTRACT -- identical to V-01]
[§10 SCOPE COVERAGE GATE PROTOCOL -- identical to V-01]
[§14 PER-FINDING SEVERITY CHAIN -- identical to V-01]
[§15 LENS EXHAUSTION PROTOCOL -- identical to V-01]
[§16 PRIMARY DRIVER DERIVATION CONTRACT -- identical to V-01]

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  [identical to V-02 §17 -- Applicability column in §5.7; HIGH/MEDIUM/LOW tiers;
   artifact-specific rating; coverage expectation by tier; §17 completes before §18]

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  [identical to V-02 §18 -- §5.8 section after §5.7; identifies ADVISORY-GAP domains;
   promotes to ACTION ITEM REGISTER; no ledger row; §18 requires §17 complete]

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  [identical to V-01 §0 -- structured table before challenge claims; minimum 2 dimensions;
   BUILD-WINS/STATUS-QUO-WINS/TIED per-dim verdicts; g_null(initial) derivable from
   table majority; GOpen consistent with table or declares override; distinct from C-16]

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

[Identical structure to V-01.]

---

## §0 -- CHALLENGER PRE-GATE: NULL HYPOTHESIS DIMENSION TABLE

*(Per §0 protocol: populated before BRACKET OPENING testimony.)*

**Null Hypothesis Dimension Comparison Table**:

| Dimension | Current-State Score | Proposed-State Score | Differential | Per-Dim Verdict |
|-----------|--------------------|--------------------|--------------|-----------------|
| [DIM_1] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_2] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_3 -- optional] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |

**§0 Table Majority**: [BUILD-WINS / STATUS-QUO-WINS / TIED]
**g_null(initial) candidate from §0**: [PASS / CONDITIONAL / FAIL]
*(GOpen must equal this or state override.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [one sentence]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table** *(per C-16)*: [as V-01]
**NULL HYPOTHESIS DERIVATION RULE**: [as V-01]
**Challenge claims**: [as V-01, with CH-IDs]

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL -- consistent with §0 candidate or override stated]
**GOpen Reason**: [One sentence.]
**g_null(initial)**: [copy GOpen]

*Local Gate Ledger Row*: | BRACKET OPENING | GOpen | [verdict] | [class] |

---

## DOMAIN -- [ROLE_NAME]

[Identical structure to V-01.]

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

[Identical to V-01.]

---

## §3.8 -- CH-ID SATURATION CHECK

[Identical to V-01.]

---

## §5.7 -- LENS COVERAGE TABLE

*(Per §17: each row carries Applicability rating specific to artifact under review.
No verdict, no ledger row.)*

| Role | Lens Dimension | Applicability | Status | ADVISORY-OPEN-LENS? |
|------|---------------|--------------|--------|---------------------|
| [ROLE] | [lens.verify entry 1] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN] |
| [ROLE] | [lens.verify entry 2] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN] |
| [LIFECYCLE_ROLE] | [lens.verify entry] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN] |

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

*(Per §18: executes after §5.7. No verdict, no ledger row.)*

| Artifact Domain (from §1) | Max Applicability Tier | Coverage Status | ADVISORY-GAP? |
|--------------------------|----------------------|----------------|---------------|
| [DOMAIN_1] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [YES / NO] |
| [DOMAIN_2] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [YES / NO] |
| [DOMAIN_3] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [YES / NO] |

ADVISORY-GAP domains -> ACTION ITEM REGISTER per §18.

---

## LIFECYCLE -- [ROLE_NAME]

[Identical structure to V-01.]

---

## BRACKET CLOSING -- CHALLENGER

[Identical structure to V-01.]

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

[Identical to V-01.]

---

## GATE VECTOR TABLE

[Identical to V-01.]

---

## CROSS-ROLE SIGNALS

[Identical structure to V-01, including g_null Progression Ledger.]

---

## DISPOSITION

[Identical structure to V-01, including §3 formula and §16 Primary Driver.]

---

## ACTION ITEM REGISTER

*(CH-ID-sourced, ADVISORY-OPEN-LENS from §5.7, ADVISORY-GAP from §5.5 and §5.8.)*

| CH-ID / Source | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|---------------|-----------------|------------------|------------|---------------------|
| CH-001 | [derived] | [class] | [ROLE] | [Criterion] |
| CH-002 | [derived] | [class] | [ROLE] | [Criterion] |
| ADVISORY-OPEN-LENS | [HIGH-applicability lens not ADDRESSED] | ADVISORY-OPEN-LENS | [ROLE] | [When ADDRESSED] |
| ADVISORY-GAP (§5.5) | [§1 surface with no finding] | ADVISORY-GAP | [ROLE] | [When COVERED] |
| ADVISORY-GAP (§5.8) | [domain with no HIGH-applicability reviewer] | ADVISORY-GAP | [ROLE] | [When COVERED] |
| ADVISORY-OBS | [advisory observation] | ADVISORY-OBS | [ROLE] | [Criterion] |

---

**Artifact to review:**

{{artifact}}

---

## V-05

**Axis**: Inertia framing + Output format + Lifecycle emphasis (three-axis) -- V-04
plus an explicit preamble dependency chain declaration co-locating §0/§17/§18 with
cross-references that bind them into a traceable pipeline: §17 feeds §18; §0 feeds
GOpen feeds §9 Stage 1. The dependency chain is declared as a named contract in the
preamble before any reviewer executes.
**Hypothesis**: V-04 achieves 225/225 via independent §0 + §17 + §18. V-05 adds a
DEPENDENCY CHAIN DECLARATION preamble block that states:
  (1) §17 Applicability ratings are the structural source for §18 gap-check
      (§18 cannot run without §17 complete);
  (2) §0 Dimension Table majority is the structural source for §9 Stage 1
      (g_null(initial) is derivable from §0 table without reading prose);
  (3) The three protocols activate at structurally disjoint phases:
      §0 at pre-bracket challenger time, §17 at lens-table time, §18 at
      domain-gap-check time -- no shared fields, no cascade effects beyond
      the declared dependencies.
This mirrors the pattern from R9 (§5 + §6 + §7 co-located in preamble) and R11
(§14 + §15 + §16 co-located with explicit phase annotations). V-05 is the canonical
T3 target for v12. Predicted: 225/225.

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
[§6 LOCAL GATE LEDGER PROTOCOL -- as V-04: §5.8 in exclusion list]
[§7 SECTION ORDER CONTRACT -- as V-04: §0 first, §5.8 between §5.7 and LIFECYCLE]
[§8 CH-ID SATURATION REQUIREMENT -- identical to V-01]
[§9 NULL HYPOTHESIS PROGRESSION CONTRACT -- EXTENDED as V-03:
   Stage 1 binding: g_null(initial) = GOpen; GOpen must equal §0 Table Majority
   verdict unless override declared. The §0 table is the structural source for
   Stage 1 -- the full chain is: §0 Dimension Table -> GOpen -> §9 Stage 1 ->
   Stage 2 -> Stage 3 -> GClose. Each stage is auditable from prior data alone.]
[§10 SCOPE COVERAGE GATE PROTOCOL -- identical to V-01]
[§14 PER-FINDING SEVERITY CHAIN -- identical to V-01]
[§15 LENS EXHAUSTION PROTOCOL -- identical to V-01]
[§16 PRIMARY DRIVER DERIVATION CONTRACT -- identical to V-01]

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  [identical to V-02/V-04 §17]

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  [identical to V-02/V-04 §18]

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  [identical to V-01/V-04 §0, with §9 Stage 1 binding stated explicitly:
   GOpen must equal §0 Table Majority per §9 Stage 1 or declare override]

DEPENDENCY CHAIN DECLARATION [IMMUTABLE]
  The three new protocols activate at structurally disjoint phases:
    §0  : pre-bracket challenger evaluation time (before BRACKET OPENING)
    §17 : lens-table-population time (§5.7, after all DOMAIN sections)
    §18 : domain-gap-check time (§5.8, after §5.7)
  Declared dependency chain:
    §17 -> §18 : §18 uses §17 Applicability ratings as source data;
                 §17 must be complete before §18 executes.
                 Without §17 ratings, there is no HIGH-applicability tier
                 for §18 to reference.
    §0  -> §9  : §0 Dimension Table Majority feeds GOpen feeds §9 Stage 1;
                 the full g_null chain is: §0 table -> GOpen -> Stage 1 ->
                 Stage 2 -> Stage 3 -> GClose.
                 Each transition is auditable from prior stage data alone.
  No shared fields between §0/§17/§18: §0 operates on the null hypothesis
  evaluation format; §17 operates on the lens dimension applicability column;
  §18 operates on the artifact domain coverage gap. No cascade effects beyond
  the declared §17->§18 and §0->§9 bindings.
  This declaration is pre-committed in the preamble; it does not change
  execution logic -- it makes the pipeline auditable at declaration time.

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

[Identical structure to V-01.]

---

## §0 -- CHALLENGER PRE-GATE: NULL HYPOTHESIS DIMENSION TABLE

*(Per §0 protocol and DEPENDENCY CHAIN DECLARATION: §0 table is the structural source
for §9 Stage 1. GOpen must equal §0 Table Majority or declare override.)*

**Null Hypothesis Dimension Comparison Table**:

| Dimension | Current-State Score | Proposed-State Score | Differential | Per-Dim Verdict |
|-----------|--------------------|--------------------|--------------|-----------------|
| [DIM_1] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_2] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_3 -- optional] | [SCORE_A] | [SCORE_B] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |

**§0 Table Majority**: [BUILD-WINS / STATUS-QUO-WINS / TIED]
**g_null(initial) candidate -- §9 Stage 1 structural source**: [PASS / CONDITIONAL / FAIL]
**Override justification (if applicable)**: [N/A -- or specific dimension(s)]

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [one sentence]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table** *(per C-16)*: [as V-01]
**NULL HYPOTHESIS DERIVATION RULE**: [as V-01]
**Challenge claims**: [as V-01 with CH-IDs]

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL -- must equal §0 candidate per §9 Stage 1]
**GOpen Reason**: [One sentence.]
**g_null(initial)**: [copy GOpen -- §9 Stage 1 confirmed = §0 Table Majority]

*Local Gate Ledger Row*: | BRACKET OPENING | GOpen | [verdict] | [class] |

---

## DOMAIN -- [ROLE_NAME]

[Identical structure to V-01.]

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

[Identical to V-01.]

---

## §3.8 -- CH-ID SATURATION CHECK

[Identical to V-01.]

---

## §5.7 -- LENS COVERAGE TABLE

*(Per §17 and DEPENDENCY CHAIN DECLARATION: Applicability column is the structural
source for §18 gap-check. §17 must be complete before §5.8 runs. No verdict, no
ledger row.)*

| Role | Lens Dimension | Applicability | Status | ADVISORY-OPEN-LENS? |
|------|---------------|--------------|--------|---------------------|
| [ROLE] | [lens.verify entry 1] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN] |
| [ROLE] | [lens.verify entry 2] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN] |
| [LIFECYCLE_ROLE] | [lens.verify entry] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [YES if HIGH+OPEN] |

*(§17 Applicability column complete -- §18 may now execute.)*

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

*(Per §18 and DEPENDENCY CHAIN DECLARATION: references §17 Applicability tiers from
§5.7 above as source data. No verdict, no ledger row.)*

| Artifact Domain (from §1) | Max Applicability Tier | Coverage Status | ADVISORY-GAP? |
|--------------------------|----------------------|----------------|---------------|
| [DOMAIN_1] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [YES / NO] |
| [DOMAIN_2] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [YES / NO] |
| [DOMAIN_3] | [HIGH / MEDIUM / LOW / none] | [COVERED / ADVISORY-GAP] | [YES / NO] |

ADVISORY-GAP domains -> ACTION ITEM REGISTER per §18.

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]
Received G_domain Aggregate: [copy from §3.5]
Saturation confirmed: [SATURATED -- per §3.8]
§5.7 Lens Coverage Table: [COMPLETE -- §18 gap-check complete]

[Remainder identical to V-01 LIFECYCLE structure.]

---

## BRACKET CLOSING -- CHALLENGER

[Identical structure to V-01.]

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

[Identical to V-01.]

---

## GATE VECTOR TABLE

[Identical to V-01.]

---

## CROSS-ROLE SIGNALS

**g_null Progression Ledger** *(per §9 -- full pipeline: §0 table -> GOpen -> Stage 1
-> Stage 2 -> Stage 3 -> GClose)*:
```
§0 Table Majority        = [copy]           [structural source for Stage 1]
g_null(initial)          = [copy GOpen]     [Stage 1: = GOpen; must equal §0 majority]
g_null(post-domain)      = [copy from §3.5] [Stage 2: worst-case(G_domain_agg, Stage 1)]
g_null(final)            = [copy from §BC]  [Stage 3: worst-case(G_lifecycle, Stage 2)]
GClose                   = [copy]           [must equal g_null(final) or override declared]
Trajectory: [e.g., PASS -> PASS -> PASS -> PASS -> PASS]
§0 override declared: [YES / NO]
GClose override declared: [YES / NO]
```

**Dependency Chain Status**:
- §17 -> §18 pipeline: [§17 complete; §18 executed using §17 Applicability source data]
- §0 -> §9 pipeline: [§0 table majority; GOpen = [value]; consistent with §0: YES/NO]

**Conflicts**: [As V-01]
**Convergence**: [As V-01]
**Scope coverage**: [As V-01]

---

## DISPOSITION

**Gate vector** *(from GATE VECTOR TABLE)*:
- GOpen         = [copy]
- G_domain_agg  = [copy]
- G_lifecycle   = [copy]
- GClose        = [copy]

**Apply §3 formula**: [as V-01]

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Primary Driver** *(per §16)*: [Gate name]

**Dependency chain audit** *(informational)*:
- §0 -> §9 chain: [intact / override declared]
- §17 -> §18 chain: [intact / no HIGH-applicability tier found -- noted in §5.8]

**Conditions** *(if CONDITIONAL)*: [as V-01]
**Blocker** *(if BLOCKED)*: [as V-01]

---

## ACTION ITEM REGISTER

*(CH-ID-sourced, ADVISORY-OPEN-LENS from §5.7, ADVISORY-GAP from §5.5 and §5.8.
Dependency chain: §5.8 ADVISORY-GAP items derived using §17 Applicability source data.)*

| CH-ID / Source | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|---------------|-----------------|------------------|------------|---------------------|
| CH-001 | [derived] | [class] | [ROLE] | [Criterion] |
| CH-002 | [derived] | [class] | [ROLE] | [Criterion] |
| ADVISORY-OPEN-LENS | [HIGH-applicability lens not ADDRESSED] | ADVISORY-OPEN-LENS | [ROLE] | [When ADDRESSED] |
| ADVISORY-GAP (§5.5) | [§1 surface with no finding] | ADVISORY-GAP | [ROLE] | [When COVERED] |
| ADVISORY-GAP (§5.8) | [domain with no HIGH-applicability reviewer -- §17 source] | ADVISORY-GAP | [ROLE] | [When a HIGH-applicability reviewer covers this domain] |
| ADVISORY-OBS | [advisory observation] | ADVISORY-OBS | [ROLE] | [Criterion] |

---

**Artifact to review:**

{{artifact}}

---

## Projected v11 Scores

| Rank | Variant | v10 base | C-33 | C-34 | C-35 | v11 projected |
|------|---------|----------|------|------|------|--------------|
| 1 (tie) | **V-04** | 210 | PASS | PASS | PASS | **225/225** |
| 1 (tie) | **V-05** | 210 | PASS | PASS | PASS | **225/225** |
| 3 (tie) | V-02 | 210 | PASS | PASS | FAIL | **220/225** |
| 4 (tie) | V-01 | 210 | FAIL | vac | PASS | **215/225** |
| 4 (tie) | V-03 | 210 | FAIL | vac | PASS | **215/225** |

V-04 vs V-05 distinguisher under v12: V-05 adds two new architectural patterns:
- DEPENDENCY CHAIN DECLARATION as a named pre-committed preamble block
- §9 Stage 1 binding to §0 table (g_null(initial) structurally traceable from
  §0 data, not just "consistent with" it)

**C-36 candidate** (from V-05): *Dependency Chain Declaration Pre-committed as Named
Preamble Block*. V-05 PASS; V-01/V-02/V-03/V-04 FAIL. A named DEPENDENCY CHAIN
DECLARATION block in the preamble enumerates the inter-protocol dependencies (§17->§18,
§0->§9) and the phase assignments for each new protocol, making the pipeline auditable
at declaration time rather than at execution time.

**C-37 candidate** (from V-03/V-05): *§9 Stage 1 Structural Source Binding*. V-03,
V-05 PASS; V-01, V-02, V-04 FAIL. §9 Stage 1 explicitly names the §0 Dimension Table
as the structural source for g_null(initial) -- the stage is derivable from the table
without reading prose. Distinct from C-35 (requires table format) and C-28 (requires
3-stage formula); C-37 requires the §9 contract to name its Stage 1 source, closing
the chain from table data to gate verdict.

---

```json
{"top_score": 225, "all_essential_pass": true, "new_patterns": ["§0 Challenger Null Hypothesis Dimension Table: pre-bracket structured comparison table with current/proposed scores and per-dim BUILD-WINS/STATUS-QUO-WINS/TIED verdicts; g_null(initial) derivable from table majority without reading prose; distinct from C-16 (bracket-wide scaffold) and C-28 (3-stage formula); satisfies C-35 (C-36/C-37 candidates from V-03/V-05 §9 binding)", "§17 Lens Applicability Protocol: fourth Applicability column in LENS COVERAGE TABLE assigns artifact-specific HIGH/MEDIUM/LOW rating to each lens dimension; coverage expectation derived by tier; not inherited from role definition; satisfies C-33", "§18 Domain Coverage Gap-Check: after §5.7 uses §17 Applicability tiers to identify artifact domains with no HIGH-applicability reviewer; each ADVISORY-GAP domain promoted to ACTION ITEM REGISTER; pre-committed protocol; satisfies C-34", "DEPENDENCY CHAIN DECLARATION (V-05): named preamble block enumerates §17->§18 and §0->§9 bindings; phase assignments declared; pipeline auditable at declaration time without reading execution sections; C-36 candidate", "§9 Stage 1 Binding (V-03/V-05): §9 NULL HYPOTHESIS PROGRESSION CONTRACT explicitly names §0 table as structural source for Stage 1; g_null(initial) derivable from table data; C-37 candidate"]}
```
