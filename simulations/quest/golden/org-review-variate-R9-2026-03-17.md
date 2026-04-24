---
skill: quest-variate
skill_target: org-review
date: 2026-03-17
round: 9
rubric: org-review-rubric-v11-2026-03-16.md
---

# org-review -- Variate R9

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis and three-axis combinations (V-04, V-05).

**R9 design target**: Under v11, V-05 R8 scores 210/225 -- all criteria through
C-32 pass; C-33/C-34/C-35 absent. The three new criteria each add 5 pts (15 pts
total). A variant passing all three reaches 225/225 (perfect). No single-axis
variant is expected to achieve all three; V-05 is the full-integration target.

**Gap analysis from R8 V-05:**

| Criterion | R8 V-05 | What it requires |
|-----------|---------|-----------------|
| C-33 LENS APPLICABILITY RATING | FAIL | Each LENS COVERAGE TABLE row carries artifact-specific HIGH/MEDIUM/LOW applicability rating as the structural basis for ADDRESSED/OPEN determination |
| C-34 ADVISORY-GAP DOMAIN COVERAGE | FAIL | After lens table is built, gap-check names every artifact domain with no HIGH-applicability reviewer; each classified ADVISORY-GAP in action register |
| C-35 NH DIMENSION COMPARISON TABLE | FAIL | Challenger's null hypothesis uses a structured current-state vs. proposed-state dimension table; g_null derivable from table values alone |

**R9 variation axes:**

- V-01: Lens Applicability Rating (single axis) -- §17 LENS APPLICABILITY RATING
  PROTOCOL added to preamble; LENS COVERAGE TABLE gains Applicability column;
  coverage expectation tiers from applicability rating. C-33 PASS predicted.

- V-02: NH Dimension Comparison Table (single axis) -- BRACKET OPENING null
  hypothesis evaluation restructured as a dimension comparison table (Dimension |
  Current State | Proposed State | Delta | g_null contribution); g_null verdict
  derivable from table values alone. C-35 PASS predicted.

- V-03: ADVISORY-GAP Domain Coverage (single axis) -- §17 DOMAIN COVERAGE
  GAP-CHECK PROTOCOL added to preamble; dedicated gap-check step after LENS
  COVERAGE TABLE names domains with no HIGH-applicability reviewer; each classified
  ADVISORY-GAP in action register. C-34 PASS predicted (requires C-31 active).

- V-04: Lens Applicability + NH Dimension Table (two-axis) -- V-01 + V-02 merged;
  §17 LENS APPLICABILITY in preamble; NH dimension comparison table in BRACKET
  OPENING. C-33 + C-35 PASS predicted.

- V-05: Full integration (three-axis) -- V-01 + V-02 + V-03; §17 LENS
  APPLICABILITY + §18 DOMAIN GAP-CHECK in preamble; NH dimension comparison table
  in BRACKET OPENING. C-33 + C-34 + C-35 PASS predicted. Target: 225/225.

**Predicted R9 scores under v11:**
- V-01: C-33 PASS. Predicted: 215/225
- V-02: C-35 PASS. Predicted: 215/225
- V-03: C-34 PASS (vacuous if C-31 inactive -- but C-31 passes in R8 base). Predicted: 215/225
- V-04: C-33 + C-35 PASS. Predicted: 220/225
- V-05: C-33 + C-34 + C-35 PASS. Predicted: 225/225

---

## V-01

**Axis**: Lens Applicability Rating -- §17 pre-commitment added
**Hypothesis**: The R8 base already passes C-31 (LENS COVERAGE TABLE with
ADDRESSED/OPEN per lens.verify entry). The sole gap is C-33: each row carries no
artifact-specific applicability rating, so the ADDRESSED/OPEN determination is an
editorial judgment at table-population time. Adding §17 LENS APPLICABILITY RATING
PROTOCOL to the preamble and a mandatory Applicability column to the LENS COVERAGE
TABLE converts that judgment to a pre-committed derivation: HIGH-applicability
lenses must be ADDRESSED; LOW-applicability may remain OPEN without penalty. C-33
PASS. C-34 and C-35 remain absent. Predicted: 215/225.

---

You are running `org-review` on the artifact provided below.

**Template variables** (acknowledged before execution):
- `{{depth}}` -- review depth: quick | standard | deep (default: standard)
- `{{artifact}}` -- the artifact under review (injected at end of prompt)
- `{{reviewer_set}}` -- domain reviewer roles from `.roles/` (auto-selected
  from registry if not supplied)

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit
any pre-printed heading, label, field, formula, or structural element. Do not add
sections between pre-printed headers. If a field cannot be filled, write
`[N/A -- reason]`.

---

```
========================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; no reviewer section executes
until §1 COMPLETE marker is reached]
========================================================================

§1 -- SCOPE ENUMERATION
[Fill this section before proceeding. This is the pre-reviewer gate.]
Annotation: these surfaces are cited in §5.5 SCOPE COVERAGE RECONCILIATION.

IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive.)

OUT-OF-SCOPE -- surfaces this review will not evaluate:
  1. [SURFACE -- REASON_EXCLUDED]
  (Write "None" if nothing excluded.)

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
  Formula is applied mechanically. No editorial reasoning at DISPOSITION time.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A missing cite is an audit-trail gap.

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, ...).
  Every downstream section carries a mandatory CH-ID response table.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

§6 -- CLASS DERIVATION CONTRACT [IMMUTABLE]
  Action item class derives mechanically from the gate verdict that sourced it:
    FAIL gate   --> BLOCKED  (must resolve before any commitment)
    CONDITIONAL --> CONDITIONAL  (must resolve before next lifecycle phase)
    PASS gate   --> ADVISORY  (may defer)
  No editorial re-assessment of class at synthesis time. Apply rule; do not judge.

§7 -- NULL HYPOTHESIS DERIVATION RULE [IMMUTABLE]
  g_null is derived from the challenger's Bracket Opening evaluation:
    If the null hypothesis strength is HIGH and no domain evidence substantially
    defeats it: g_null = HOLDS --> GOpen = FAIL
    If material domain evidence reduces the null hypothesis: g_null = PARTIAL
    --> GOpen = CONDITIONAL
    If domain evidence defeats the null hypothesis across its primary claims:
    g_null = DEFEATED --> GOpen = PASS
  This rule is applied at GOpen; g_null is not re-derived editorially downstream.

§8 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Syntax: Gate: [name] | Verdict: [PASS/CONDITIONAL/FAIL] | Class: [class]
          | Severity: [HIGH/MEDIUM/LOW] | Section: [section_name]
  Emit at END of each verdict-emitting section, after verdict is stated.
  Assembly: copy rows to master ACTION ITEM REGISTER verbatim.
  DO NOT re-derive Gate Verdict or Class during assembly.
  EXCLUDED section: §3.5 DOMAIN-AGGREGATE CHECKPOINT produces no verdict and
  emits NO ledger row.

§9 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical execution sequence (reordering is a contract violation):
  ROLE MANIFEST --> BRACKET OPENING --> DOMAIN(s) --> §3.5 DOMAIN-AGGREGATE
  CHECKPOINT --> §3.8 CH-ID SATURATION CHECK --> LIFECYCLE --> BRACKET CLOSING
  --> §5.5 SCOPE COVERAGE RECONCILIATION --> §5.6 LENS COVERAGE TABLE
  --> GATE VECTOR TABLE --> CROSS-ROLE SIGNALS --> DISPOSITION
  --> ACTION ITEM REGISTER

§10 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED      = every CH-ID has >= 1 DOMAIN response before LIFECYCLE executes
  FULLY SATURATED = every CH-ID has domain + lifecycle response before BRACKET
                   CLOSING
  §3.8 CH-ID SATURATION CHECK verifies pre-LIFECYCLE saturation.
  BRACKET CLOSING prohibits a PASS verdict when any CH-ID is UNSATURATED without
  a stated waiver.

§11 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = GOpen
  Stage 2: g_null(post-domain) =
    if G_domain_agg = FAIL     then HOLDS
    if G_domain_agg = CONDITIONAL then PARTIAL
    if G_domain_agg = PASS     then g_null(initial) [unchanged]
  Stage 3: g_null(final) =
    if G_lifecycle = FAIL      then HOLDS
    if G_lifecycle = CONDITIONAL  then PARTIAL
    if G_lifecycle = PASS      then g_null(post-domain) [unchanged]
  GClose verdict must equal g_null(final). Deviation requires explicit override
  with named justification. Emit g_null values as labeled fields at each stage.

§12 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  After BRACKET CLOSING: §5.5 SCOPE COVERAGE RECONCILIATION executes.
  Maps each §1 IN-SCOPE surface to reviewer findings across all sections.
  COVERED = surface appears in >= 1 finding.
  GAP     = no finding references this surface.
  GAP surfaces --> ADVISORY-GAP items in ACTION ITEM REGISTER (LOW severity).
  Gate emits COVERED/PARTIAL signal (informational only -- NO ledger row emitted).

§13 -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(G_domain_1, G_domain_2, ...) -- worst-case rule.
  FAIL > CONDITIONAL > PASS.
  Bracket Closing applies this formula mechanically. No editorial aggregation.
  G_domain_agg is stated explicitly in §3.5 DOMAIN-AGGREGATE CHECKPOINT.

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Each finding row carries an individual Severity field (HIGH / MEDIUM / LOW).
  Section Severity = worst(F-1.Severity, F-2.Severity, ...) over all finding rows
  in that section. Derived; not editorially assigned.
  Section Severity feeds the gate ledger row for that section.

§15 -- LENS COVERAGE TABLE PROTOCOL [IMMUTABLE]
  After all reviewer sections: §5.6 LENS COVERAGE TABLE maps each active
  reviewer's lens.verify entries to ADDRESSED (finding references this dimension)
  or OPEN (no finding referenced this dimension).
  OPEN entries --> ADVISORY-OPEN-LENS items in ACTION ITEM REGISTER.
  Table produced before DISPOSITION.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  After all gate verdicts are known, apply rules in precedence order to select
  exactly one gate as Primary Driver:
  R1: GClose = FAIL             --> Primary Driver = GClose
  R2: GOpen  = FAIL             --> Primary Driver = GOpen
  R3: G_domain_agg = FAIL       --> Primary Driver = G_domain_agg
  R4: G_lifecycle  = FAIL       --> Primary Driver = G_lifecycle
  R5: GClose = CONDITIONAL      --> Primary Driver = GClose
  R6: GOpen  = CONDITIONAL      --> Primary Driver = GOpen
  R7: G_domain_agg = CONDITIONAL --> Primary Driver = G_domain_agg
  R8: G_lifecycle  = CONDITIONAL --> Primary Driver = G_lifecycle
  R9: All PASS                  --> Primary Driver = GOpen
  Emit Primary Driver as a labeled field at DISPOSITION. Derivable from gate
  verdict values alone without reading reviewer narrative.

§17 -- LENS APPLICABILITY RATING PROTOCOL [IMMUTABLE]  *** NEW in V-01 ***
  Each row in §5.6 LENS COVERAGE TABLE carries an explicit Applicability rating
  (HIGH / MEDIUM / LOW) specific to the artifact under review -- not generic.
  Applicability tiers determine coverage expectations:
    HIGH applicability: lens dimension is fully relevant to this artifact.
      OPEN status requires a named reason and generates ADVISORY-OPEN-LENS item.
    MEDIUM applicability: lens dimension is partially relevant.
      OPEN status is permitted with a brief note; no mandatory action item.
    LOW applicability: lens dimension is not meaningfully applicable to this
      artifact. OPEN status requires no explanation.
  The rating is artifact-specific. The same role in a different review may carry
  a different applicability rating. Rating is assigned at table-population time
  against the specific artifact, not copied from role definitions.

========================================================================
END DISPOSITION_CONTRACT v1
========================================================================
```

---

## ROLE MANIFEST

Read `.roles/{{reviewer_set}}/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE -- why this role argues status quo for this artifact] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE -- what expertise this role brings] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE -- what commitment frame this role brings] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3. CHALLENGER positions remain fixed.
State total count.)*

Depth acknowledged: `{{depth}}` mode. Role selection rationale stated per §3.

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one
sentence stating the status quo behavior that makes building unnecessary.]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW -- how defensible is doing
nothing?]

**Null hypothesis alternatives** (>= 3 options for multi-alternative coverage):

| Option | Description | Score (0-10) |
|--------|-------------|-------------|
| A: Status Quo | [current behavior without building] | [score] |
| B: Proposed | [what this artifact enables] | [score] |
| C: Incremental | [lowest-effort improvement to status quo] | [score] |

**NULL HYPOTHESIS DERIVATION RULE applied**:
  g_null = HOLDS if B score <= max(A, C) -- proposed does not beat best alternative
  g_null = DEFEATED if B score > max(A, C) -- proposed beats all alternatives
  g_null(initial) = [HOLDS / PARTIAL / DEFEATED]

**Challenge claims** *(assign CH-IDs; carry to every downstream section per §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence grounded in g_null(initial) and challenge claims.]

*Local Gate Ledger Row*:
Gate: GOpen | Verdict: [_] | Class: [per §6] | Severity: [per §14] | Section: BRACKET OPENING

*GOpen and all CH-IDs carry forward to every downstream section.*

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]

**CH-ID Response Table** *(mandatory per §5 -- PASS prohibited if any row = OPEN)*:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

*(PARTIAL requires a named resolution path. OPEN = claim not addressable from
this role's frame.)*

**Dimension re-scoring** (re-score same A/B/C options from this role's frame):

| Option | This Role's Score (0-10) | Rationale |
|--------|--------------------------|-----------|
| A: Status Quo | [score] | [one sentence] |
| B: Proposed | [score] | [one sentence] |
| C: Incremental | [score] | [one sentence] |

**Additional Findings**:

| F-ID | Finding | Surface | Severity |
|------|---------|---------|---------|
| F-1 | [FINDING_1 from this role's `lens.verify`; names an in-scope surface] | [surface] | [HIGH/MEDIUM/LOW] |
| F-2 | [FINDING_2] | [surface] | [HIGH/MEDIUM/LOW] |
| F-3 | [FINDING_3 -- optional] | [surface] | [HIGH/MEDIUM/LOW] |

Section Severity = worst(F-1, F-2, ...) per §14: [HIGH / MEDIUM / LOW]

**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*Local Gate Ledger Row*:
Gate: G_domain | Verdict: [_] | Class: [per §6] | Severity: [per §14] | Section: DOMAIN

*(For `--depth deep`: repeat labeled DOMAIN-2, DOMAIN-3. Each emits its own
ledger row.)*

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*EXCLUDED from gate ledger per §8 -- this section produces no gate verdict.*

G_domain_agg = worst(G_domain_1 [, G_domain_2, ...]) per §13:
**G_domain_agg = [PASS / CONDITIONAL / FAIL]**

g_null(post-domain) per §11 Stage 2:
  G_domain_agg = [value] --> g_null(post-domain) = [HOLDS / PARTIAL / DEFEATED]

---

## §3.8 CH-ID SATURATION CHECK

*(Executes after DOMAIN sections; before LIFECYCLE; per §10)*

| CH-ID | Domain Response(s) | Saturation Status |
|-------|-------------------|------------------|
| CH-001 | [DOMAIN role(s) that responded] | [SATURATED / UNSATURATED] |
| CH-002 | [DOMAIN role(s) that responded] | [SATURATED / UNSATURATED] |
| CH-003 | [if active] | [SATURATED / UNSATURATED] |

**Pre-LIFECYCLE saturation gate**: [SATURATED / UNSATURATED]
If UNSATURATED: [Name the unsaturated CH-ID and state whether a waiver applies.]
LIFECYCLE may not begin if any CH-ID is UNSATURATED without a stated waiver.

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]
Received G_domain_agg: [copy from §3.5]
g_null(post-domain): [copy from §3.5]

**CH-ID Response Table** *(mandatory per §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [Is evidence sufficient for commitment given
both received verdicts? One paragraph referencing GOpen and G_domain_agg
explicitly.]

**Null hypothesis status**: [Given GOpen and G_domain_agg, has the null hypothesis
been defeated? yes / partial / no -- one sentence.]

**Additional Findings**:

| F-ID | Finding | Surface | Severity |
|------|---------|---------|---------|
| F-1 | [FINDING_1 from this role's `lens.verify`; commitment or program concerns] | [surface] | [HIGH/MEDIUM/LOW] |
| F-2 | [FINDING_2] | [surface] | [HIGH/MEDIUM/LOW] |

Section Severity = worst(F-1, F-2, ...) per §14: [HIGH / MEDIUM / LOW]

**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

g_null(final) per §11 Stage 3:
  G_lifecycle = [value], g_null(post-domain) = [value]
  --> g_null(final) = [HOLDS / PARTIAL / DEFEATED]

*Local Gate Ledger Row*:
Gate: G_lifecycle | Verdict: [_] | Class: [per §6] | Severity: [per §14] | Section: LIFECYCLE

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: §1 scope, all CH-ID tables, all gate verdicts.*

Lifecycle verdict received: G_lifecycle = [copy from LIFECYCLE]
g_null(final) = [copy from LIFECYCLE]

**CH-ID FULLY SATURATED check** (per §10):

| CH-ID | Domain Status | Lifecycle Status | Fully Saturated? |
|-------|--------------|-----------------|-----------------|
| CH-001 | [copy from DOMAIN] | [copy from LIFECYCLE] | [YES / NO] |
| CH-002 | [copy] | [copy] | [YES / NO] |
| CH-003 | [copy if active] | [copy] | [YES / NO] |

If any row = NO: PASS verdict is prohibited unless waiver stated.

**Aggregated dimension table** (domain re-scores applied; per §13):

| Option | GOpen Score | G_domain Avg | G_lifecycle Score | Aggregated Score |
|--------|------------|-------------|-------------------|-----------------|
| A: Status Quo | [from BRACKET OPENING] | [avg of domain re-scores] | [lifecycle assessment] | [composite] |
| B: Proposed | [from BRACKET OPENING] | [avg] | [lifecycle] | [composite] |
| C: Incremental | [from BRACKET OPENING] | [avg] | [lifecycle] | [composite] |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [one sentence] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [What was not fully addressed. If none: "None -- all CH-IDs
DEFEATED."]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
  GClose must equal g_null(final) = [value] per §11. State if override invoked.

**Override invoked**: [YES / NO]
  If YES: [Justification for deviation from g_null(final).]

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts.
A HOLDS verdict from the challenger is not overturned by G_domain or G_lifecycle
PASses. Pre-stated in §3; not subject to editorial revision at DISPOSITION.

**GClose Rationale**: [2-3 sentences.]

*Local Gate Ledger Row*:
Gate: GClose | Verdict: [_] | Class: [per §6] | Severity: [per §14] | Section: BRACKET CLOSING

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(Executes after BRACKET CLOSING; per §12. Informational only -- no ledger row.)*

| §1 Surface | Reviewer(s) with Finding | Coverage |
|-----------|--------------------------|----------|
| [SURFACE_1] | [reviewer or "None"] | [COVERED / GAP] |
| [SURFACE_2] | [reviewer or "None"] | [COVERED / GAP] |
| [SURFACE_3] | [reviewer or "None"] | [COVERED / GAP] |

GAP surfaces --> ADVISORY-GAP items appended to ACTION ITEM REGISTER (LOW, per §12).

**Gate signal**: [COVERED (all surfaces have findings) / PARTIAL (>= 1 GAP)] -- informational only.

---

## §5.6 LENS COVERAGE TABLE

*(Executes after §5.5; per §15 and §17.)*

| Reviewer | Lens Dimension | Applicability | Status |
|----------|---------------|---------------|--------|
| [CHALLENGER_ROLE] | [lens.verify entry 1] | [HIGH / MEDIUM / LOW -- artifact-specific per §17] | [ADDRESSED / OPEN] |
| [CHALLENGER_ROLE] | [lens.verify entry 2] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] |
| [DOMAIN_ROLE] | [lens.verify entry 1] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] |
| [DOMAIN_ROLE] | [lens.verify entry 2] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] |
| [LIFECYCLE_ROLE] | [lens.verify entry 1] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] |
| [LIFECYCLE_ROLE] | [lens.verify entry 2] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] |

Coverage expectations per §17:
- HIGH applicability + OPEN --> ADVISORY-OPEN-LENS item in ACTION ITEM REGISTER
- MEDIUM applicability + OPEN --> note only; no mandatory item
- LOW applicability + OPEN --> no action required

*(Add rows for all lens.verify entries from each active role definition.)*

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen -- bracket opening | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain_agg -- domain aggregate | [DOMAIN_ROLE(S)] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle -- lifecycle | [LIFECYCLE_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose -- bracket closing | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Two reviewers with incompatible CH-ID responses or incompatible
findings -- name roles and tension. If none: "None detected."]

**Convergence**: [Any CH-ID or concern named independently by two or more
reviewers -- name it and state why it is the highest-confidence signal.]

**Null hypothesis progression** (per §11):
  g_null(initial) = [copy from BRACKET OPENING]
  g_null(post-domain) = [copy from §3.5]
  g_null(final) = [copy from LIFECYCLE]

**Scope coverage**: [Any §1 IN-SCOPE surface not covered by any reviewer. If all
covered: "None -- full in-scope surface reviewed."]

---

## DISPOSITION

**Gate vector** *(from GATE VECTOR TABLE)*:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply §3 formula** *(do not alter; evaluate mechanically)*:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Primary Driver** (per §16 precedence rules): [gate name] -- [one sentence]

**Conditions** *(complete only if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate -- gate order: GOpen, G_domain, G_lifecycle, GClose.]
2. [Additional conditions if present.]

**Blocker** *(complete only if BLOCKED)*: [Specific finding from the FAIL gate.
If GClose = FAIL, lead with: "Challenger final verdict HOLDS -- [GClose Rationale
summary]."]

---

## ACTION ITEM REGISTER

*Assembly: copy local gate ledger rows verbatim per §8. DO NOT re-derive Gate
Verdict or Class. Add scope gap items from §5.5. Add lens items from §5.6.*

| CH-ID | Item Description | Disposition Class | Gate Verdict | Owner Role | Resolution Criterion |
|-------|-----------------|------------------|-------------|------------|---------------------|
| CH-001 | [derived from PARTIAL or HOLDS status] | [BLOCKED/CONDITIONAL/ADVISORY per §6] | [copy from ledger] | [ROLE_NAME] | [specific resolution statement] |
| CH-002 | [Item 2] | [class] | [verdict] | [ROLE_NAME] | [criterion] |
| -- | [ADVISORY-GAP: scope surface [name] has no reviewer finding] | ADVISORY-GAP | N/A | [ROLE_NAME] | [criterion] |
| -- | [ADVISORY-OPEN-LENS: [role] lens dimension [name] was OPEN with HIGH applicability] | ADVISORY-OPEN-LENS | N/A | [ROLE_NAME] | [criterion] |

*Disposition class per §6:*
- **BLOCKED**: Must resolve before any commitment.
- **CONDITIONAL**: Must resolve before next lifecycle phase.
- **ADVISORY**: May defer.
- **ADVISORY-GAP**: Scope surface with no reviewer finding (§5.5).
- **ADVISORY-OPEN-LENS**: HIGH-applicability lens dimension not addressed (§5.6 per §17).

---

**Artifact to review:**

{{artifact}}

---

## V-02

**Axis**: NH Dimension Comparison Table -- BRACKET OPENING restructured
**Hypothesis**: The R8 base uses prose null hypothesis testimony at BRACKET
OPENING. g_null(initial) is stated as a verdict but the derivation is narrative.
C-35 requires a structured dimension comparison table (>= 2 dimensions, current-
state rating, proposed-state rating, per-dimension differential) such that g_null
is derivable from table values alone without reading prose. Replacing the prose NH
evaluation with a dimension comparison table in BRACKET OPENING achieves C-35.
C-33 and C-34 remain absent. Predicted: 215/225.

---

You are running `org-review` on the artifact provided below.

**Template variables** (acknowledged before execution):
- `{{depth}}` -- review depth: quick | standard | deep (default: standard)
- `{{artifact}}` -- the artifact under review (injected at end of prompt)
- `{{reviewer_set}}` -- domain reviewer roles from `.roles/`

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit
any pre-printed heading, label, field, formula, or structural element. If a field
cannot be filled, write `[N/A -- reason]`.

---

```
========================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK]
========================================================================

§1 -- SCOPE ENUMERATION
Annotation: these surfaces are cited in §5.5 SCOPE COVERAGE RECONCILIATION.

IN-SCOPE:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]

§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions commitment. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose = FAIL OR exists Gi = FAIL
  CONDITIONAL <-- no FAIL AND exists CONDITIONAL
  READY <-- all PASS
  Apply mechanically. No editorial reasoning at DISPOSITION time.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Challenge claims receive CH-IDs. Every downstream section carries CH-ID
  response table. PASS prohibited if any CH-ID row = OPEN.

§6 -- CLASS DERIVATION CONTRACT [IMMUTABLE]
  FAIL --> BLOCKED | CONDITIONAL --> CONDITIONAL | PASS --> ADVISORY
  No editorial re-assessment at synthesis time.

§7 -- NULL HYPOTHESIS DERIVATION RULE [IMMUTABLE]  *** UPDATED for C-35 ***
  g_null is derived mechanically from the NH Dimension Comparison Table:
    Per-dimension verdict: HOLDS if proposed-state <= current-state on this
    dimension; DEFEATED if proposed-state > current-state.
    g_null(initial) = DEFEATED if majority of HIGH-weight dimensions show
    DEFEATED; PARTIAL if mixed; HOLDS if majority show HOLDS.
    The table values alone determine g_null; no prose argument may contradict
    the table-derived verdict.

§8 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Syntax: Gate: [name] | Verdict: [_] | Class: [_] | Severity: [_] | Section: [_]
  Emit at end of each verdict-emitting section.
  Assembly: copy verbatim. DO NOT re-derive.
  EXCLUDED: §3.5 emits NO ledger row.

§9 -- SECTION ORDER CONTRACT [IMMUTABLE]
  ROLE MANIFEST --> BRACKET OPENING --> DOMAIN(s) --> §3.5 DOMAIN-AGGREGATE
  CHECKPOINT --> §3.8 CH-ID SATURATION CHECK --> LIFECYCLE --> BRACKET CLOSING
  --> §5.5 SCOPE COVERAGE RECONCILIATION --> §5.6 LENS COVERAGE TABLE
  --> GATE VECTOR TABLE --> CROSS-ROLE SIGNALS --> DISPOSITION
  --> ACTION ITEM REGISTER
  Reordering is a contract violation.

§10 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED = every CH-ID has >= 1 DOMAIN response before LIFECYCLE.
  FULLY SATURATED = domain + lifecycle response before BRACKET CLOSING.
  BRACKET CLOSING prohibits PASS when any CH-ID UNSATURATED without waiver.

§11 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = GOpen
  Stage 2: g_null(post-domain) = f(G_domain_agg, g_null(initial))
    FAIL->HOLDS | CONDITIONAL->PARTIAL | PASS->unchanged
  Stage 3: g_null(final) = f(G_lifecycle, g_null(post-domain))
    FAIL->HOLDS | CONDITIONAL->PARTIAL | PASS->unchanged
  GClose = g_null(final) or declare override with justification.

§12 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 after BRACKET CLOSING. GAP surfaces -> ADVISORY-GAP in ACTION REGISTER.
  Gate signal: COVERED/PARTIAL (informational -- NO ledger row).

§13 -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts). Applied mechanically at §3.5.

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Each finding row carries Severity. Section Severity = worst(F-n.Severity).

§15 -- LENS COVERAGE TABLE PROTOCOL [IMMUTABLE]
  §5.6 after §5.5. Maps lens.verify entries to ADDRESSED/OPEN.
  OPEN entries -> ADVISORY-OPEN-LENS items in ACTION REGISTER.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  R1:GClose=FAIL->GClose | R2:GOpen=FAIL->GOpen | R3:G_dom=FAIL->G_dom
  R4:G_life=FAIL->G_life | R5:GClose=COND->GClose | R6:GOpen=COND->GOpen
  R7:G_dom=COND->G_dom | R8:G_life=COND->G_life | R9:all PASS->GOpen
  Emit as labeled field at DISPOSITION.

========================================================================
END DISPOSITION_CONTRACT v1
========================================================================
```

---

## ROLE MANIFEST

Read `.roles/{{reviewer_set}}/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

Depth acknowledged: `{{depth}}` mode.

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null Hypothesis Dimension Comparison Table** *(C-35 -- g_null derivable from
table values alone; table appears before any domain section)*:

| Dimension | Current State | Proposed State | Delta | Per-dim Verdict |
|-----------|---------------|----------------|-------|----------------|
| [DIM_1 -- e.g., user effort required] | [current rating or score] | [proposed rating or score] | [+/-/=] | [DEFEATED / HOLDS] |
| [DIM_2 -- e.g., error/failure risk] | [current] | [proposed] | [+/-/=] | [DEFEATED / HOLDS] |
| [DIM_3 -- e.g., adoption friction] | [current] | [proposed] | [+/-/=] | [DEFEATED / HOLDS] |
| [DIM_4 -- optional] | [current] | [proposed] | [+/-/=] | [DEFEATED / HOLDS] |

g_null(initial) per §7 (derived from table -- majority rule on DEFEATED/HOLDS):
  Dimension verdicts: [list]
  **g_null(initial) = [HOLDS / PARTIAL / DEFEATED]**

**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Challenge claims** *(assign CH-IDs)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL -- must equal g_null(initial) per §11]
**GOpen Reason**: [One sentence grounded in table-derived g_null(initial).]

*Local Gate Ledger Row*:
Gate: GOpen | Verdict: [_] | Class: [per §6] | Severity: [per §14] | Section: BRACKET OPENING

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Dimension re-scoring** (re-score same dimensions from this role's technical frame):

| Dimension | This Role's Current State | This Role's Proposed State | Delta |
|-----------|--------------------------|---------------------------|-------|
| [DIM_1] | [score] | [score] | [+/-/=] |
| [DIM_2] | [score] | [score] | [+/-/=] |
| [DIM_3] | [score] | [score] | [+/-/=] |

**Additional Findings**:

| F-ID | Finding | Surface | Severity |
|------|---------|---------|---------|
| F-1 | [FINDING_1] | [surface] | [HIGH/MEDIUM/LOW] |
| F-2 | [FINDING_2] | [surface] | [HIGH/MEDIUM/LOW] |

Section Severity = worst(F-n.Severity) per §14: [HIGH / MEDIUM / LOW]

**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*Local Gate Ledger Row*:
Gate: G_domain | Verdict: [_] | Class: [per §6] | Severity: [per §14] | Section: DOMAIN

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*EXCLUDED from gate ledger -- no verdict emitted.*

G_domain_agg = worst(all G_domain verdicts) per §13: **[PASS / CONDITIONAL / FAIL]**

g_null(post-domain) per §11 Stage 2: **[HOLDS / PARTIAL / DEFEATED]**

---

## §3.8 CH-ID SATURATION CHECK

| CH-ID | Domain Response(s) | Saturation Status |
|-------|-------------------|------------------|
| CH-001 | [DOMAIN role] | [SATURATED / UNSATURATED] |
| CH-002 | [DOMAIN role] | [SATURATED / UNSATURATED] |

Pre-LIFECYCLE saturation gate: [SATURATED / UNSATURATED]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy] | G_domain_agg: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | Commitment-Frame Response | Status |
|-------|----------------------|--------------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph citing GOpen and G_domain_agg.]

**Null hypothesis status**: [yes / partial / no -- one sentence.]

**Additional Findings**:

| F-ID | Finding | Surface | Severity |
|------|---------|---------|---------|
| F-1 | [FINDING_1] | [surface] | [HIGH/MEDIUM/LOW] |
| F-2 | [FINDING_2] | [surface] | [HIGH/MEDIUM/LOW] |

Section Severity per §14: [HIGH / MEDIUM / LOW]

**Recommendation**: [One concrete action.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

g_null(final) per §11 Stage 3: **[HOLDS / PARTIAL / DEFEATED]**

*Local Gate Ledger Row*:
Gate: G_lifecycle | Verdict: [_] | Class: [per §6] | Severity: [per §14] | Section: LIFECYCLE

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
G_lifecycle received: [copy] | g_null(final): [copy]

**CH-ID FULLY SATURATED check**:

| CH-ID | Domain | Lifecycle | Fully Saturated? |
|-------|--------|-----------|-----------------|
| CH-001 | [status] | [status] | [YES/NO] |
| CH-002 | [status] | [status] | [YES/NO] |

**Aggregated dimension table** (domain + lifecycle re-scores incorporated):

| Dimension | GOpen Score | Domain Avg | Lifecycle | Aggregated | Final Verdict |
|-----------|------------|------------|-----------|------------|--------------|
| [DIM_1] | [from BRACKET OPENING] | [avg domain re-scores] | [lifecycle] | [composite] | [DEFEATED/HOLDS] |
| [DIM_2] | [from BRACKET OPENING] | [avg] | [lifecycle] | [composite] | [DEFEATED/HOLDS] |
| [DIM_3] | [from BRACKET OPENING] | [avg] | [lifecycle] | [composite] | [DEFEATED/HOLDS] |

g_null(final) confirmed from aggregated table: [HOLDS / PARTIAL / DEFEATED]

**CH-ID Final Assessment**:

| CH-ID | G_domain | G_lifecycle | Final Status | Notes |
|-------|----------|-------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |

**GClose Verdict**: [PASS / CONDITIONAL / FAIL -- must equal g_null(final)]
**Override invoked**: [YES / NO]
**GClose Rationale**: [2-3 sentences.]

*Local Gate Ledger Row*:
Gate: GClose | Verdict: [_] | Class: [per §6] | Severity: [per §14] | Section: BRACKET CLOSING

---

## §5.5 SCOPE COVERAGE RECONCILIATION

| §1 Surface | Reviewer(s) with Finding | Coverage |
|-----------|--------------------------|----------|
| [SURFACE_1] | [reviewer or "None"] | [COVERED / GAP] |
| [SURFACE_2] | [reviewer or "None"] | [COVERED / GAP] |

GAP surfaces --> ADVISORY-GAP in ACTION ITEM REGISTER.
Gate signal: [COVERED / PARTIAL] -- informational only.

---

## §5.6 LENS COVERAGE TABLE

| Reviewer | Lens Dimension | Status |
|----------|---------------|--------|
| [CHALLENGER] | [lens.verify entry] | [ADDRESSED / OPEN] |
| [DOMAIN] | [lens.verify entry] | [ADDRESSED / OPEN] |
| [LIFECYCLE] | [lens.verify entry] | [ADDRESSED / OPEN] |

OPEN entries --> ADVISORY-OPEN-LENS items in ACTION ITEM REGISTER.

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER] | [_] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [_] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [_] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [_] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [name or "None detected."]
**Convergence**: [name or "None detected."]
**Null hypothesis progression**: g_null(initial)=[_] -> g_null(post-domain)=[_] -> g_null(final)=[_]
**Scope coverage**: [gaps or "None."]

---

## DISPOSITION

**Gate vector**: GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]

```
GClose=FAIL? -> BLOCKED | any FAIL? -> BLOCKED | any COND? -> CONDITIONAL | all PASS? -> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Primary Driver** (per §16): [gate] -- [one sentence]

---

## ACTION ITEM REGISTER

*Copy local gate ledger rows verbatim per §8. DO NOT re-derive.*

| CH-ID | Item | Class | Gate Verdict | Owner | Resolution |
|-------|------|-------|-------------|-------|-----------|
| CH-001 | [description] | [class per §6] | [copy] | [role] | [criterion] |
| CH-002 | [description] | [class] | [copy] | [role] | [criterion] |
| -- | [ADVISORY-GAP: scope surface] | ADVISORY-GAP | N/A | [role] | [criterion] |
| -- | [ADVISORY-OPEN-LENS: lens dimension] | ADVISORY-OPEN-LENS | N/A | [role] | [criterion] |

---

**Artifact to review:**

{{artifact}}

---

## V-03

**Axis**: ADVISORY-GAP Domain Coverage -- §17 DOMAIN GAP-CHECK PROTOCOL added
**Hypothesis**: The R8 base already passes C-31 (LENS COVERAGE TABLE) and now V-01
passes C-33 (applicability ratings). V-03 is a clean single-axis test of C-34 only:
after the LENS COVERAGE TABLE is populated with applicability ratings (C-31 active),
a dedicated §5.7 DOMAIN COVERAGE GAP-CHECK step identifies every artifact domain
with no HIGH-applicability reviewer and classifies each as ADVISORY-GAP. Note:
C-34 is vacuous without C-31 active. V-03 includes the C-31 table but NOT the C-33
applicability column -- it tests C-34 using the C-31 ADDRESSED/OPEN classification
as a proxy for coverage. C-33 and C-35 remain absent. Predicted: 215/225.

*(Note: because C-34 requires C-31 active and the C-34 rubric says "C-31 FAIL
automatically makes C-34 vacuous," V-03 must include C-31 to earn C-34 credit.
The axis variation is: only C-34's gap-check machinery is new; C-33 applicability
ratings are absent.)*

---

You are running `org-review` on the artifact provided below.

**Template variables**:
- `{{depth}}` | `{{artifact}}` | `{{reviewer_set}}`

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter or omit pre-printed
structure.

---

```
========================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK]
========================================================================

§1 -- SCOPE ENUMERATION
Annotation: cited in §5.5 SCOPE COVERAGE RECONCILIATION.
IN-SCOPE:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
OUT-OF-SCOPE:
  1. [SURFACE -- REASON]
§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks. MEDIUM = Conditions. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
§6 -- CLASS DERIVATION CONTRACT [IMMUTABLE]
  FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY
§7 -- NULL HYPOTHESIS DERIVATION RULE [IMMUTABLE]
  g_null(initial) = HOLDS if NH strength HIGH and no defeating evidence;
  PARTIAL if material evidence reduces it; DEFEATED if evidence defeats it.
§8 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Syntax: Gate:[name]|Verdict:[_]|Class:[_]|Severity:[_]|Section:[_]
  Emit end of each verdict section. Copy verbatim to register. No re-derive.
  EXCLUDED: §3.5 emits NO row.
§9 -- SECTION ORDER CONTRACT [IMMUTABLE]
  ROLE MANIFEST -> BRACKET OPENING -> DOMAIN(s) -> §3.5 -> §3.8 -> LIFECYCLE
  -> BRACKET CLOSING -> §5.5 -> §5.6 -> §5.7 -> GATE VECTOR -> CROSS-ROLE
  -> DISPOSITION -> ACTION ITEM REGISTER. Reordering prohibited.
§10 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED = CH-ID has >=1 DOMAIN response pre-LIFECYCLE.
  FULLY SATURATED = domain+lifecycle pre-BRACKET CLOSING.
  BRACKET CLOSING: PASS prohibited if any CH-ID UNSATURATED without waiver.
§11 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage1: g_null(initial)=GOpen
  Stage2: g_null(post-domain)=f(G_domain_agg,g_null(initial))
  Stage3: g_null(final)=f(G_lifecycle,g_null(post-domain))
  GClose=g_null(final) or declare override.
§12 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 post-BRACKET CLOSING. GAP->ADVISORY-GAP. Signal: COVERED/PARTIAL, no row.
§13 -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(G_domain_n). Applied at §3.5.
§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Each finding row: Severity field. Section Severity = worst(F-n.Severity).
§15 -- LENS COVERAGE TABLE PROTOCOL [IMMUTABLE]
  §5.6 post-§5.5. Maps lens.verify to ADDRESSED/OPEN.
  OPEN -> ADVISORY-OPEN-LENS in ACTION REGISTER.
§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  R1:GClose=FAIL->GClose|R2:GOpen=FAIL->GOpen|R3:G_dom=FAIL->G_dom|
  R4:G_life=FAIL->G_life|R5:GClose=COND->GClose|R6:GOpen=COND->GOpen|
  R7:G_dom=COND->G_dom|R8:G_life=COND->G_life|R9:all PASS->GOpen
§17 -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]  *** NEW in V-03 ***
  After §5.6 LENS COVERAGE TABLE is populated, §5.7 DOMAIN COVERAGE GAP-CHECK
  executes as follows:
  1. For each artifact domain identified in §1 IN-SCOPE, determine whether any
     active reviewer has their relevant lens dimension marked ADDRESSED in §5.6.
  2. A domain is COVERED if >= 1 reviewer has an ADDRESSED lens dimension for it.
     A domain is UNCOVERED if no reviewer has an ADDRESSED lens dimension for it.
  3. Each UNCOVERED domain is classified ADVISORY-GAP and promoted to the ACTION
     ITEM REGISTER, naming the uncovered domain and the reason (absent role,
     all lenses OPEN, or no role with relevant coverage).
  4. This gap-check is pre-committed here; it does not run editorially at review
     time. §5.7 always executes after §5.6.

========================================================================
END DISPOSITION_CONTRACT v1
========================================================================
```

---

## ROLE MANIFEST

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

Depth: `{{depth}}`.

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today -- one sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Null hypothesis alternatives**:

| Option | Description | Score (0-10) |
|--------|-------------|-------------|
| A: Status Quo | [description] | [score] |
| B: Proposed | [description] | [score] |
| C: Incremental | [description] | [score] |

g_null(initial) per §7: [HOLDS / PARTIAL / DEFEATED]

**Challenge claims**:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [severity] |
| CH-002 | [CLAIM_2] | [severity] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

*Local Gate Ledger Row*:
Gate: GOpen | Verdict:[_] | Class:[per §6] | Severity:[per §14] | Section: BRACKET OPENING

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table**:

| CH-ID | Claim (copy) | Response | Status |
|-------|-------------|----------|--------|
| CH-001 | [copy] | [response] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | [response] | [ADDRESSED/PARTIAL/OPEN] |

**Dimension re-scoring**:

| Option | Score | Rationale |
|--------|-------|-----------|
| A | [score] | [note] |
| B | [score] | [note] |
| C | [score] | [note] |

**Additional Findings**:

| F-ID | Finding | Surface | Severity |
|------|---------|---------|---------|
| F-1 | [finding] | [surface] | [severity] |
| F-2 | [finding] | [surface] | [severity] |

Section Severity per §14: [_]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*Local Gate Ledger Row*:
Gate: G_domain | Verdict:[_] | Class:[per §6] | Severity:[per §14] | Section: DOMAIN

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*EXCLUDED from ledger.*

G_domain_agg per §13: **[PASS / CONDITIONAL / FAIL]**
g_null(post-domain) per §11: **[HOLDS / PARTIAL / DEFEATED]**

---

## §3.8 CH-ID SATURATION CHECK

| CH-ID | Domain Response | Saturated? |
|-------|----------------|-----------|
| CH-001 | [domain] | [YES/NO] |
| CH-002 | [domain] | [YES/NO] |

Pre-LIFECYCLE gate: [SATURATED / UNSATURATED]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received: GOpen=[copy] | G_domain_agg=[copy] | g_null(post-domain)=[copy]

**CH-ID Response Table**:

| CH-ID | Claim (copy) | Commitment Response | Status |
|-------|-------------|--------------------|----- --|
| CH-001 | [copy] | [response] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | [response] | [ADDRESSED/PARTIAL/OPEN] |

**Decision-readiness**: [One paragraph citing GOpen and G_domain_agg.]
**NH status**: [yes / partial / no]

**Additional Findings**:

| F-ID | Finding | Surface | Severity |
|------|---------|---------|---------|
| F-1 | [finding] | [surface] | [severity] |

Section Severity per §14: [_]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

g_null(final) per §11: **[HOLDS / PARTIAL / DEFEATED]**

*Local Gate Ledger Row*:
Gate: G_lifecycle | Verdict:[_] | Class:[per §6] | Severity:[per §14] | Section: LIFECYCLE

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
G_lifecycle received: [copy] | g_null(final): [copy]

**CH-ID FULLY SATURATED check**:

| CH-ID | Domain | Lifecycle | Fully Saturated? |
|-------|--------|-----------|-----------------|
| CH-001 | [status] | [status] | [YES/NO] |
| CH-002 | [status] | [status] | [YES/NO] |

**CH-ID Final Assessment**:

| CH-ID | G_domain | G_lifecycle | Final | Notes |
|-------|----------|-------------|-------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**GClose Rationale**: [2-3 sentences.]

*Local Gate Ledger Row*:
Gate: GClose | Verdict:[_] | Class:[per §6] | Severity:[per §14] | Section: BRACKET CLOSING

---

## §5.5 SCOPE COVERAGE RECONCILIATION

| §1 Surface | Reviewer(s) | Coverage |
|-----------|------------|----------|
| [SURFACE_1] | [reviewer or "None"] | [COVERED/GAP] |
| [SURFACE_2] | [reviewer or "None"] | [COVERED/GAP] |

GAP -> ADVISORY-GAP in ACTION REGISTER.
Gate signal: [COVERED/PARTIAL] -- informational only.

---

## §5.6 LENS COVERAGE TABLE

| Reviewer | Lens Dimension | Status |
|----------|---------------|--------|
| [CHALLENGER] | [lens.verify entry] | [ADDRESSED/OPEN] |
| [DOMAIN] | [lens.verify entry] | [ADDRESSED/OPEN] |
| [LIFECYCLE] | [lens.verify entry] | [ADDRESSED/OPEN] |

OPEN -> ADVISORY-OPEN-LENS in ACTION REGISTER.

---

## §5.7 DOMAIN COVERAGE GAP-CHECK  *** NEW in V-03 ***

*(Executes after §5.6; per §17.)*

For each artifact domain in §1 IN-SCOPE: does any reviewer have an ADDRESSED
lens dimension covering this domain?

| Artifact Domain | Reviewer(s) with ADDRESSED Coverage | Domain Status |
|-----------------|-------------------------------------|--------------|
| [domain from SURFACE_1] | [reviewer name or "None"] | [COVERED / ADVISORY-GAP] |
| [domain from SURFACE_2] | [reviewer name or "None"] | [COVERED / ADVISORY-GAP] |
| [domain from SURFACE_3] | [reviewer name or "None"] | [COVERED / ADVISORY-GAP] |

Each ADVISORY-GAP domain --> ACTION ITEM REGISTER entry per §17.

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER] | [_] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [_] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [_] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [_] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [name or "None."]
**Convergence**: [name or "None."]
**NH progression**: g_null(initial)=[_] -> g_null(post-domain)=[_] -> g_null(final)=[_]
**Scope coverage**: [gaps or "None."]

---

## DISPOSITION

GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]

```
GClose=FAIL?->BLOCKED | any FAIL?->BLOCKED | any COND?->CONDITIONAL | all PASS?->READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Primary Driver** per §16: [gate] -- [one sentence]

---

## ACTION ITEM REGISTER

*Copy local gate ledger rows verbatim per §8. NO re-derivation.*

| CH-ID | Item | Class | Gate Verdict | Owner | Resolution |
|-------|------|-------|-------------|-------|-----------|
| CH-001 | [description] | [class per §6] | [copy] | [role] | [criterion] |
| -- | [ADVISORY-GAP: scope surface] | ADVISORY-GAP | N/A | [role] | [criterion] |
| -- | [ADVISORY-GAP: domain [name] has no reviewer coverage per §5.7] | ADVISORY-GAP | N/A | [role] | [criterion] |
| -- | [ADVISORY-OPEN-LENS: lens dimension OPEN] | ADVISORY-OPEN-LENS | N/A | [role] | [criterion] |

---

**Artifact to review:**

{{artifact}}

---

## V-04

**Axis**: Lens Applicability + NH Dimension Comparison Table (two-axis)
**Hypothesis**: V-01 (C-33) + V-02 (C-35) merged. §17 LENS APPLICABILITY RATING
PROTOCOL in preamble; LENS COVERAGE TABLE has Applicability column; BRACKET
OPENING NH evaluation uses dimension comparison table. Both C-33 and C-35 pass.
C-34 remains absent. Predicted: 220/225.

The structural integration challenge: the NH dimension comparison table (C-35)
and the applicability ratings (C-33) are independent additions that operate at
different execution points (BRACKET OPENING vs §5.6). No structural conflict.
V-04 co-locates both §17 contracts and verifies each operates independently.

---

You are running `org-review` on the artifact provided below.

**Template variables**: `{{depth}}` | `{{artifact}}` | `{{reviewer_set}}`

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter structure.

---

```
========================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK]
========================================================================

§1 -- SCOPE ENUMERATION
Annotation: cited in §5.5.
IN-SCOPE:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
OUT-OF-SCOPE:
  1. [SURFACE -- REASON]
§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks. MEDIUM=Conditions. LOW=Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED<--GClose=FAIL OR any Gi=FAIL
  CONDITIONAL<--no FAIL AND any CONDITIONAL
  READY<--all PASS

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]

§6 -- CLASS DERIVATION CONTRACT [IMMUTABLE]
  FAIL->BLOCKED | CONDITIONAL->CONDITIONAL | PASS->ADVISORY

§7 -- NULL HYPOTHESIS DERIVATION RULE [IMMUTABLE]  *** UPDATED for C-35 ***
  g_null(initial) is derived mechanically from the NH Dimension Comparison Table:
  Each dimension carries a per-dim verdict (HOLDS if proposed <= current;
  DEFEATED if proposed > current). g_null = majority verdict across all dimensions.
  Table values alone determine g_null; prose may not contradict table.

§8 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Syntax: Gate:[name]|Verdict:[_]|Class:[_]|Severity:[_]|Section:[_]
  Emit at end of each verdict section. Copy verbatim. No re-derive.
  EXCLUDED: §3.5 emits NO row.

§9 -- SECTION ORDER CONTRACT [IMMUTABLE]
  ROLE MANIFEST -> BRACKET OPENING -> DOMAIN(s) -> §3.5 -> §3.8 -> LIFECYCLE
  -> BRACKET CLOSING -> §5.5 -> §5.6 -> GATE VECTOR -> CROSS-ROLE
  -> DISPOSITION -> ACTION REGISTER. Reordering prohibited.

§10 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED=CH-ID has >=1 DOMAIN response pre-LIFECYCLE.
  FULLY SATURATED=domain+lifecycle pre-BRACKET CLOSING.
  BRACKET CLOSING: PASS prohibited if any UNSATURATED without waiver.

§11 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage1: g_null(initial)=GOpen
  Stage2: g_null(post-domain)=f(G_domain_agg,g_null(initial))
  Stage3: g_null(final)=f(G_lifecycle,g_null(post-domain))
  GClose=g_null(final) or declare override.

§12 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 post-BRACKET CLOSING. GAP->ADVISORY-GAP. No ledger row.

§13 -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg=worst(G_domain_n). Applied mechanically at §3.5.

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Each finding row: Severity. Section Severity=worst(F-n.Severity).

§15 -- LENS COVERAGE TABLE PROTOCOL [IMMUTABLE]
  §5.6 post-§5.5. Maps lens.verify to ADDRESSED/OPEN.
  OPEN->ADVISORY-OPEN-LENS in ACTION REGISTER.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  R1:GClose=FAIL->GClose|R2:GOpen=FAIL->GOpen|R3:G_dom=FAIL->G_dom|
  R4:G_life=FAIL->G_life|R5:GClose=COND->GClose|R6:GOpen=COND->GOpen|
  R7:G_dom=COND->G_dom|R8:G_life=COND->G_life|R9:all PASS->GOpen

§17 -- LENS APPLICABILITY RATING PROTOCOL [IMMUTABLE]  *** NEW in V-04 ***
  Each §5.6 LENS COVERAGE TABLE row carries an Applicability rating
  (HIGH / MEDIUM / LOW) specific to this artifact (not generic role capability).
  HIGH: lens fully applicable; OPEN requires named reason + ADVISORY-OPEN-LENS.
  MEDIUM: partially applicable; OPEN permitted with brief note; no mandatory item.
  LOW: not meaningfully applicable; OPEN requires no action.
  Rating is assigned at table-population time against the specific artifact.

========================================================================
END DISPOSITION_CONTRACT v1
========================================================================
```

---

## ROLE MANIFEST

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

Depth: `{{depth}}`.

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null Hypothesis Dimension Comparison Table** *(per §7 -- C-35 -- g_null derivable
from table values alone; populated before any domain section)*:

| Dimension | Current State | Proposed State | Delta | Per-dim Verdict |
|-----------|---------------|----------------|-------|----------------|
| [DIM_1] | [rating] | [rating] | [+/-/=] | [DEFEATED/HOLDS] |
| [DIM_2] | [rating] | [rating] | [+/-/=] | [DEFEATED/HOLDS] |
| [DIM_3] | [rating] | [rating] | [+/-/=] | [DEFEATED/HOLDS] |

**g_null(initial)** (majority rule over per-dim verdicts per §7):
  [count] DEFEATED, [count] HOLDS --> **g_null(initial) = [HOLDS/PARTIAL/DEFEATED]**

**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Challenge claims**:

| CH-ID | Claim | Severity |
|-------|-------|---------|
| CH-001 | [CLAIM_1] | [severity] |
| CH-002 | [CLAIM_2] | [severity] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL -- must equal g_null(initial)]
**GOpen Reason**: [One sentence grounded in table-derived g_null.]

*Local Gate Ledger Row*:
Gate: GOpen | Verdict:[_] | Class:[per §6] | Severity:[per §14] | Section: BRACKET OPENING

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table**:

| CH-ID | Claim (copy) | Response | Status |
|-------|-------------|----------|--------|
| CH-001 | [copy] | [response] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | [response] | [ADDRESSED/PARTIAL/OPEN] |

**Dimension re-scoring** (same dimensions as BRACKET OPENING):

| Dimension | Current State | Proposed State | Delta |
|-----------|---------------|----------------|-------|
| [DIM_1] | [score] | [score] | [+/-] |
| [DIM_2] | [score] | [score] | [+/-] |
| [DIM_3] | [score] | [score] | [+/-] |

**Additional Findings**:

| F-ID | Finding | Surface | Severity |
|------|---------|---------|---------|
| F-1 | [finding] | [surface] | [severity] |
| F-2 | [finding] | [surface] | [severity] |

Section Severity per §14: [_]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*Local Gate Ledger Row*:
Gate: G_domain | Verdict:[_] | Class:[per §6] | Severity:[per §14] | Section: DOMAIN

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*EXCLUDED from ledger.*
G_domain_agg per §13: **[PASS / CONDITIONAL / FAIL]**
g_null(post-domain) per §11: **[HOLDS / PARTIAL / DEFEATED]**

---

## §3.8 CH-ID SATURATION CHECK

| CH-ID | Domain | Saturated? |
|-------|--------|-----------|
| CH-001 | [domain] | [YES/NO] |
| CH-002 | [domain] | [YES/NO] |

Gate: [SATURATED / UNSATURATED]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received: GOpen=[copy] | G_domain_agg=[copy] | g_null(post-domain)=[copy]

**CH-ID Response Table**:

| CH-ID | Claim (copy) | Commitment Response | Status |
|-------|-------------|---------------------|--------|
| CH-001 | [copy] | [response] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | [response] | [ADDRESSED/PARTIAL/OPEN] |

**Decision-readiness**: [One paragraph.]
**NH status**: [yes / partial / no]

**Additional Findings**:

| F-ID | Finding | Surface | Severity |
|------|---------|---------|---------|
| F-1 | [finding] | [surface] | [severity] |

Section Severity per §14: [_]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]
g_null(final) per §11: **[HOLDS / PARTIAL / DEFEATED]**

*Local Gate Ledger Row*:
Gate: G_lifecycle | Verdict:[_] | Class:[per §6] | Severity:[per §14] | Section: LIFECYCLE

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
G_lifecycle: [copy] | g_null(final): [copy]

**CH-ID FULLY SATURATED check**:

| CH-ID | Domain | Lifecycle | Fully Saturated? |
|-------|--------|-----------|-----------------|
| CH-001 | [status] | [status] | [YES/NO] |
| CH-002 | [status] | [status] | [YES/NO] |

**Aggregated dimension table** (domain re-scores integrated):

| Dimension | GOpen | Domain Avg | Lifecycle | Aggregated | Final Verdict |
|-----------|-------|-----------|-----------|------------|--------------|
| [DIM_1] | [score] | [avg] | [score] | [composite] | [DEFEATED/HOLDS] |
| [DIM_2] | [score] | [avg] | [score] | [composite] | [DEFEATED/HOLDS] |
| [DIM_3] | [score] | [avg] | [score] | [composite] | [DEFEATED/HOLDS] |

g_null(final) confirmed from table: [HOLDS / PARTIAL / DEFEATED]

**CH-ID Final Assessment**:

| CH-ID | G_domain | G_lifecycle | Final | Notes |
|-------|----------|-------------|-------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**GClose Rationale**: [2-3 sentences.]

*Local Gate Ledger Row*:
Gate: GClose | Verdict:[_] | Class:[per §6] | Severity:[per §14] | Section: BRACKET CLOSING

---

## §5.5 SCOPE COVERAGE RECONCILIATION

| §1 Surface | Reviewer(s) | Coverage |
|-----------|------------|----------|
| [SURFACE_1] | [reviewer or "None"] | [COVERED/GAP] |
| [SURFACE_2] | [reviewer or "None"] | [COVERED/GAP] |

GAP -> ADVISORY-GAP. Signal: [COVERED/PARTIAL] -- informational.

---

## §5.6 LENS COVERAGE TABLE

*(Per §15 and §17 -- includes Applicability column)*

| Reviewer | Lens Dimension | Applicability | Status |
|----------|---------------|---------------|--------|
| [CHALLENGER] | [lens.verify entry] | [HIGH/MEDIUM/LOW -- artifact-specific] | [ADDRESSED/OPEN] |
| [DOMAIN] | [lens.verify entry] | [HIGH/MEDIUM/LOW] | [ADDRESSED/OPEN] |
| [LIFECYCLE] | [lens.verify entry] | [HIGH/MEDIUM/LOW] | [ADDRESSED/OPEN] |

Coverage per §17:
- HIGH + OPEN -> ADVISORY-OPEN-LENS item
- MEDIUM + OPEN -> note only
- LOW + OPEN -> no action

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Cite |
|------|----------|---------|------|
| GOpen | [CHALLENGER] | [_] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [_] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [_] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [_] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [name or "None."]
**Convergence**: [name or "None."]
**NH progression**: g_null(initial)=[_]->g_null(post-domain)=[_]->g_null(final)=[_]
**Scope coverage**: [gaps or "None."]

---

## DISPOSITION

GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]

```
GClose=FAIL?->BLOCKED|any FAIL?->BLOCKED|any COND?->CONDITIONAL|all PASS?->READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Primary Driver** per §16: [gate] -- [one sentence]

---

## ACTION ITEM REGISTER

*Copy local gate ledger rows verbatim. DO NOT re-derive.*

| CH-ID | Item | Class | Gate Verdict | Owner | Resolution |
|-------|------|-------|-------------|-------|-----------|
| CH-001 | [description] | [class] | [copy] | [role] | [criterion] |
| -- | [ADVISORY-GAP: scope surface] | ADVISORY-GAP | N/A | [role] | [criterion] |
| -- | [ADVISORY-OPEN-LENS: [role] lens [dim] HIGH applicability, OPEN] | ADVISORY-OPEN-LENS | N/A | [role] | [criterion] |

---

**Artifact to review:**

{{artifact}}

---

## V-05

**Axis**: Full integration (C-33 + C-34 + C-35 -- three-axis)
**Hypothesis**: V-01 + V-02 + V-03 merged. §17 LENS APPLICABILITY RATING PROTOCOL
+ §18 DOMAIN COVERAGE GAP-CHECK PROTOCOL in preamble. BRACKET OPENING NH
evaluation uses dimension comparison table (C-35). LENS COVERAGE TABLE has
Applicability column (C-33). §5.7 DOMAIN COVERAGE GAP-CHECK runs after §5.6 with
ADVISORY-GAP promotion (C-34). All three criteria pass simultaneously.
Target: 225/225.

**Integration note**: C-34 requires C-31 active (LENS COVERAGE TABLE). C-33
adds the applicability column to C-31's table. C-34's gap-check operates on the
applicability tiers introduced by C-33 -- it checks for domains with no
HIGH-applicability reviewer, which requires C-33's Applicability column to exist.
Therefore, C-34 in V-05 uses C-33's applicability data as its source, creating
a tighter dependency than in V-03 (which operated without C-33). This is the
canonical V-02 R12-equivalent architecture for org-review.

---

You are running `org-review` on the artifact provided below.

**Template variables**: `{{depth}}` | `{{artifact}}` | `{{reviewer_set}}`

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter or omit structure.

---

```
========================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- §1 must complete before any reviewer section executes]
========================================================================

§1 -- SCOPE ENUMERATION
Annotation: these surfaces are cited in §5.5 SCOPE COVERAGE RECONCILIATION
and serve as the domain inventory for §5.7 DOMAIN COVERAGE GAP-CHECK.

IN-SCOPE:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
  Silent scope expansion violates this contract.

§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions commitment. LOW = Advisory.
  Definitions apply universally; not restated at any gate.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose = FAIL OR exists Gi = FAIL
  CONDITIONAL  <-- no Gi = FAIL AND exists Gi = CONDITIONAL
  READY        <-- all Gi = PASS
  Apply formula mechanically at DISPOSITION. No editorial reasoning.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Challenge claims receive CH-IDs. Every downstream section: CH-ID response
  table. PASS prohibited if any CH-ID row = OPEN.

§6 -- CLASS DERIVATION CONTRACT [IMMUTABLE]
  Gate verdict -> action item class (derived, not editorial):
    FAIL        --> BLOCKED
    CONDITIONAL --> CONDITIONAL
    PASS        --> ADVISORY

§7 -- NULL HYPOTHESIS DERIVATION RULE [IMMUTABLE]  *** UPDATED for C-35 ***
  g_null(initial) is derived from the NH Dimension Comparison Table in BRACKET
  OPENING. Each table dimension carries a per-dimension verdict:
    per-dim HOLDS    = proposed-state rating <= current-state rating
    per-dim DEFEATED = proposed-state rating >  current-state rating
  g_null(initial) =
    HOLDS    if majority of dimensions show HOLDS
    PARTIAL  if dimensions are evenly split
    DEFEATED if majority show DEFEATED
  The table alone determines g_null. Prose testimony may not contradict
  the table-derived verdict.

§8 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: Gate:[name]|Verdict:[PASS/CONDITIONAL/FAIL]|Class:[class]
              |Severity:[HIGH/MEDIUM/LOW]|Section:[section_name]
  Timing: emit at END of each verdict-emitting section, after verdict stated.
  Assembly: copy all rows to ACTION ITEM REGISTER verbatim.
  PROHIBITION: do NOT re-derive Gate Verdict or Class during assembly.
  EXCLUDED sections: §3.5 DOMAIN-AGGREGATE CHECKPOINT and §5.7 DOMAIN COVERAGE
  GAP-CHECK emit NO ledger rows (neither produces a gate verdict).

§9 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical execution sequence (reordering is a contract violation):
  ROLE MANIFEST -> BRACKET OPENING -> DOMAIN(s) -> §3.5 DOMAIN-AGGREGATE
  CHECKPOINT -> §3.8 CH-ID SATURATION CHECK -> LIFECYCLE -> BRACKET CLOSING
  -> §5.5 SCOPE COVERAGE RECONCILIATION -> §5.6 LENS COVERAGE TABLE
  -> §5.7 DOMAIN COVERAGE GAP-CHECK -> GATE VECTOR TABLE -> CROSS-ROLE
  SIGNALS -> DISPOSITION -> ACTION ITEM REGISTER

§10 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED      = every CH-ID has >= 1 DOMAIN section response before
                   LIFECYCLE executes
  FULLY SATURATED = every CH-ID has domain + lifecycle response before
                   BRACKET CLOSING
  §3.8 CH-ID SATURATION CHECK: gate between DOMAIN(s) and LIFECYCLE.
  BRACKET CLOSING: PASS verdict prohibited if any CH-ID UNSATURATED without
  explicit waiver stated.

§11 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Three-stage mechanical derivation:
  Stage 1: g_null(initial) = GOpen  [from §7 table derivation]
  Stage 2: g_null(post-domain) =
    G_domain_agg = FAIL        --> HOLDS
    G_domain_agg = CONDITIONAL --> PARTIAL
    G_domain_agg = PASS        --> g_null(initial) unchanged
  Stage 3: g_null(final) =
    G_lifecycle = FAIL         --> HOLDS
    G_lifecycle = CONDITIONAL  --> PARTIAL
    G_lifecycle = PASS         --> g_null(post-domain) unchanged
  GClose verdict must equal g_null(final). Deviation requires explicit override
  declaration with named justification. Emit g_null values as labeled fields.
  Summary in CROSS-ROLE SIGNALS.

§12 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 executes after BRACKET CLOSING.
  Maps each §1 IN-SCOPE surface to reviewer findings.
  COVERED = >= 1 reviewer finding references this surface.
  GAP     = no finding. GAP -> ADVISORY-GAP item in ACTION REGISTER (LOW).
  Gate signal: COVERED (all surfaces hit) / PARTIAL (>= 1 GAP).
  Informational only. NO ledger row.

§13 -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(G_domain_1, G_domain_2, ...) where FAIL > COND > PASS.
  §3.5 applies formula and states G_domain_agg. BRACKET CLOSING copies from §3.5.
  No editorial aggregation.

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Each finding row carries an individual Severity field (HIGH/MEDIUM/LOW).
  Section Severity = worst(F-1.Severity, F-2.Severity, ...) for all finding
  rows in section. Derived mechanically. No editorial section-level assignment.
  Section Severity feeds the gate ledger row for that section.

§15 -- LENS COVERAGE TABLE PROTOCOL [IMMUTABLE]
  §5.6 executes after §5.5.
  For each active reviewer: all lens.verify entries appear in table with
  ADDRESSED (finding references this dimension) or OPEN (none referenced it).
  OPEN entries -> ADVISORY-OPEN-LENS items in ACTION REGISTER.
  Table produced before DISPOSITION.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  After all gate verdicts known, apply in precedence order:
  R1: GClose = FAIL        --> Primary Driver = GClose
  R2: GOpen  = FAIL        --> Primary Driver = GOpen
  R3: G_domain_agg = FAIL  --> Primary Driver = G_domain_agg
  R4: G_lifecycle  = FAIL  --> Primary Driver = G_lifecycle
  R5: GClose = CONDITIONAL --> Primary Driver = GClose
  R6: GOpen  = CONDITIONAL --> Primary Driver = GOpen
  R7: G_domain_agg = COND  --> Primary Driver = G_domain_agg
  R8: G_lifecycle  = COND  --> Primary Driver = G_lifecycle
  R9: All PASS             --> Primary Driver = GOpen
  Primary Driver emitted as labeled field at DISPOSITION. Derivable from gate
  verdict values alone.

§17 -- LENS APPLICABILITY RATING PROTOCOL [IMMUTABLE]  *** NEW in V-05 ***
  Each row in §5.6 LENS COVERAGE TABLE carries an Applicability rating
  (HIGH / MEDIUM / LOW) specific to the artifact under review -- not generic.
  Applicability tiers govern coverage expectations:
    HIGH:   lens fully applicable to this artifact.
            OPEN status requires a named reason + ADVISORY-OPEN-LENS item.
    MEDIUM: lens partially applicable.
            OPEN permitted with brief note; no mandatory action item.
    LOW:    lens not meaningfully applicable to this artifact.
            OPEN requires no explanation.
  Rating is assigned at table-population time against the specific artifact.
  The same role reviewing a different artifact may carry different ratings.
  Applicability ratings also serve as the data source for §5.7 gap-check (§18).

§18 -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]  *** NEW in V-05 ***
  §5.7 executes after §5.6 LENS COVERAGE TABLE is populated.
  Step 1: For each artifact domain identified in §1 IN-SCOPE, determine whether
          any active reviewer has Applicability = HIGH for a lens dimension
          covering that domain in §5.6.
  Step 2: Classify each domain:
          COVERED      = >= 1 reviewer has HIGH applicability to a relevant lens
                         dimension AND that dimension is ADDRESSED.
          ADVISORY-GAP = no reviewer has HIGH applicability to any lens dimension
                         relevant to this domain, OR all HIGH-applicability
                         reviewers have that dimension as OPEN.
  Step 3: Each ADVISORY-GAP domain is promoted to the ACTION ITEM REGISTER,
          recording: domain name, reason for gap (absent role / HIGH-app OPEN /
          no HIGH-app reviewer assigned), and resolution criterion.
  §5.7 is informational. It emits NO gate ledger row.

========================================================================
END DISPOSITION_CONTRACT v1
========================================================================
```

---

## ROLE MANIFEST

Read `.roles/{{reviewer_set}}/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE -- why this role argues status quo for this artifact] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE -- expertise brought] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE -- commitment frame] |

Depth acknowledged: `{{depth}}` mode. Role selection rationale stated per §3.

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null Hypothesis Dimension Comparison Table** *(per §7 -- C-35 -- all values
populated before any domain section; g_null derivable from table alone)*:

| Dimension | Current State | Proposed State | Delta | Per-dim Verdict |
|-----------|---------------|----------------|-------|----------------|
| [DIM_1 e.g., effort-to-accomplish] | [current rating 0-10 or H/M/L] | [proposed rating] | [+/-/=] | [DEFEATED if proposed>current; HOLDS otherwise] |
| [DIM_2 e.g., error rate / failure risk] | [current] | [proposed] | [+/-/=] | [DEFEATED / HOLDS] |
| [DIM_3 e.g., adoption friction] | [current] | [proposed] | [+/-/=] | [DEFEATED / HOLDS] |
| [DIM_4 e.g., reversibility / rollback] | [current] | [proposed] | [+/-/=] | [DEFEATED / HOLDS] |

**g_null(initial)** derived from table per §7:
  Dimension verdicts: DIM_1=[_], DIM_2=[_], DIM_3=[_], DIM_4=[_]
  Majority rule: [N] DEFEATED, [N] HOLDS
  **g_null(initial) = [HOLDS / PARTIAL / DEFEATED]**

**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Challenge claims** *(assign CH-IDs; carry to every downstream section)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or friction] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL -- must equal g_null(initial) per §11]
**GOpen Reason**: [One sentence grounded in table-derived g_null(initial).]

*Local Gate Ledger Row*:
Gate: GOpen | Verdict:[_] | Class:[per §6] | Severity:[per §14] | Section: BRACKET OPENING

*GOpen and all CH-IDs carry forward to every downstream section.*

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]

**CH-ID Response Table** *(mandatory per §5; PASS prohibited if any row = OPEN)*:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Dimension re-scoring** (same dimensions as BRACKET OPENING, from this role's frame):

| Dimension | Current State | Proposed State | Delta |
|-----------|---------------|----------------|-------|
| [DIM_1] | [score] | [score] | [+/-] |
| [DIM_2] | [score] | [score] | [+/-] |
| [DIM_3] | [score] | [score] | [+/-] |
| [DIM_4] | [score] | [score] | [+/-] |

**Additional Findings**:

| F-ID | Finding | Surface | Severity |
|------|---------|---------|---------|
| F-1 | [FINDING from this role's `lens.verify`; names in-scope surface] | [surface] | [HIGH/MEDIUM/LOW] |
| F-2 | [FINDING_2] | [surface] | [HIGH/MEDIUM/LOW] |
| F-3 | [optional] | [surface] | [HIGH/MEDIUM/LOW] |

Section Severity = worst(F-1, F-2, ...) per §14: [HIGH / MEDIUM / LOW]

**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*Local Gate Ledger Row*:
Gate: G_domain | Verdict:[_] | Class:[per §6] | Severity:[per §14] | Section: DOMAIN

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*EXCLUDED from gate ledger per §8 -- this section produces no gate verdict.*

G_domain_agg = worst(G_domain_1 [, G_domain_2, ...]) per §13:
**G_domain_agg = [PASS / CONDITIONAL / FAIL]**

g_null(post-domain) per §11 Stage 2:
  G_domain_agg = [value] --> **g_null(post-domain) = [HOLDS / PARTIAL / DEFEATED]**

---

## §3.8 CH-ID SATURATION CHECK

*(Between DOMAIN(s) and LIFECYCLE; per §10)*

| CH-ID | Domain Response(s) | Saturation Status |
|-------|-------------------|------------------|
| CH-001 | [DOMAIN role(s)] | [SATURATED / UNSATURATED] |
| CH-002 | [DOMAIN role(s)] | [SATURATED / UNSATURATED] |
| CH-003 | [if active] | [SATURATED / UNSATURATED] |

**Pre-LIFECYCLE saturation gate**: [SATURATED / UNSATURATED]
If UNSATURATED: [Name CH-ID and state waiver if applicable.]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy] | G_domain_agg: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table** *(mandatory per §5)*:

| CH-ID | Challenge Claim (copy) | Commitment-Frame Response | Status |
|-------|----------------------|--------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph citing GOpen and G_domain_agg.]
**Null hypothesis status**: [yes / partial / no -- one sentence.]

**Additional Findings**:

| F-ID | Finding | Surface | Severity |
|------|---------|---------|---------|
| F-1 | [FINDING from this role's `lens.verify`] | [surface] | [HIGH/MEDIUM/LOW] |
| F-2 | [FINDING_2] | [surface] | [HIGH/MEDIUM/LOW] |

Section Severity per §14: [HIGH / MEDIUM / LOW]

**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

g_null(final) per §11 Stage 3:
  G_lifecycle=[value], g_null(post-domain)=[value]
  --> **g_null(final) = [HOLDS / PARTIAL / DEFEATED]**

*Local Gate Ledger Row*:
Gate: G_lifecycle | Verdict:[_] | Class:[per §6] | Severity:[per §14] | Section: LIFECYCLE

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: §1 scope, all CH-ID tables, all gate verdicts.*

Lifecycle verdict received: G_lifecycle = [copy from LIFECYCLE]
g_null(final) = [copy from LIFECYCLE]

**CH-ID FULLY SATURATED check** (per §10):

| CH-ID | Domain Status | Lifecycle Status | Fully Saturated? |
|-------|--------------|-----------------|-----------------|
| CH-001 | [from DOMAIN] | [from LIFECYCLE] | [YES / NO] |
| CH-002 | [from DOMAIN] | [from LIFECYCLE] | [YES / NO] |
| CH-003 | [if active] | [from LIFECYCLE] | [YES / NO] |

If any row = NO: PASS verdict prohibited unless waiver declared.

**Aggregated dimension table** (domain + lifecycle re-scores integrated):

| Dimension | GOpen | Domain Avg | Lifecycle | Aggregated | Final Verdict |
|-----------|-------|-----------|-----------|------------|--------------|
| [DIM_1] | [from opener] | [avg of domain re-scores] | [lifecycle] | [composite] | [DEFEATED/HOLDS] |
| [DIM_2] | [from opener] | [avg] | [lifecycle] | [composite] | [DEFEATED/HOLDS] |
| [DIM_3] | [from opener] | [avg] | [lifecycle] | [composite] | [DEFEATED/HOLDS] |
| [DIM_4] | [from opener] | [avg] | [lifecycle] | [composite] | [DEFEATED/HOLDS] |

g_null(final) confirmed from aggregated table: [HOLDS / PARTIAL / DEFEATED]
Must equal §11 Stage 3 value; override if not.

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [from DOMAIN] | [from LIFECYCLE] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [from DOMAIN] | [from LIFECYCLE] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [if active] | [from LIFECYCLE] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [All PARTIAL/HOLDS CH-IDs, or "None -- all CH-IDs DEFEATED."]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL -- must equal g_null(final)]
**Override invoked**: [YES / NO -- per §11]
  If YES: [Justification for override.]

**GClose override authority**: GClose=FAIL overrides all prior gate verdicts.
HOLDS verdict not overturned by G_domain or G_lifecycle PASses. Pre-stated §3.

**GClose Rationale**: [2-3 sentences.]

*Local Gate Ledger Row*:
Gate: GClose | Verdict:[_] | Class:[per §6] | Severity:[per §14] | Section: BRACKET CLOSING

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(After BRACKET CLOSING; per §12. NO ledger row.)*

| §1 Surface | Reviewer(s) with Finding | Coverage |
|-----------|--------------------------|----------|
| [SURFACE_1] | [reviewer or "None"] | [COVERED / GAP] |
| [SURFACE_2] | [reviewer or "None"] | [COVERED / GAP] |
| [SURFACE_3] | [reviewer or "None"] | [COVERED / GAP] |

GAP surfaces --> ADVISORY-GAP items in ACTION ITEM REGISTER (LOW severity, per §12).
**Gate signal**: [COVERED / PARTIAL] -- informational only.

---

## §5.6 LENS COVERAGE TABLE

*(Per §15 and §17 -- Applicability column mandatory)*

| Reviewer | Lens Dimension | Applicability | Status |
|----------|---------------|---------------|--------|
| [CHALLENGER] | [lens.verify entry 1] | [HIGH/MEDIUM/LOW -- artifact-specific per §17] | [ADDRESSED / OPEN] |
| [CHALLENGER] | [lens.verify entry 2] | [HIGH/MEDIUM/LOW] | [ADDRESSED / OPEN] |
| [DOMAIN] | [lens.verify entry 1] | [HIGH/MEDIUM/LOW] | [ADDRESSED / OPEN] |
| [DOMAIN] | [lens.verify entry 2] | [HIGH/MEDIUM/LOW] | [ADDRESSED / OPEN] |
| [LIFECYCLE] | [lens.verify entry 1] | [HIGH/MEDIUM/LOW] | [ADDRESSED / OPEN] |
| [LIFECYCLE] | [lens.verify entry 2] | [HIGH/MEDIUM/LOW] | [ADDRESSED / OPEN] |

Coverage expectations per §17:
- HIGH + OPEN --> ADVISORY-OPEN-LENS item required
- MEDIUM + OPEN --> brief note; no mandatory item
- LOW + OPEN --> no action required

*(This table is also the applicability data source for §5.7 per §18.)*

---

## §5.7 DOMAIN COVERAGE GAP-CHECK

*(Per §18 -- executes after §5.6. NO ledger row.)*

For each artifact domain in §1 IN-SCOPE: identify reviewers with HIGH
Applicability to a lens dimension covering that domain in §5.6.

| Artifact Domain | Reviewer(s) with HIGH Applicability | Their §5.6 Status | Domain Coverage |
|-----------------|-------------------------------------|------------------|----------------|
| [domain from SURFACE_1] | [reviewer or "None"] | [ADDRESSED/OPEN or "N/A"] | [COVERED / ADVISORY-GAP] |
| [domain from SURFACE_2] | [reviewer or "None"] | [ADDRESSED/OPEN or "N/A"] | [COVERED / ADVISORY-GAP] |
| [domain from SURFACE_3] | [reviewer or "None"] | [ADDRESSED/OPEN or "N/A"] | [COVERED / ADVISORY-GAP] |

Classification per §18:
- COVERED = >= 1 reviewer has HIGH applicability AND lens dimension is ADDRESSED
- ADVISORY-GAP = no HIGH-applicability reviewer, OR all HIGH-app reviewers have
  OPEN lens dimensions for this domain

Each ADVISORY-GAP domain --> ACTION ITEM REGISTER per §18.

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN_ROLE(S)] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Two reviewers with incompatible CH-ID responses or findings.
If none: "None detected."]

**Convergence**: [Any CH-ID or concern named by 2+ reviewers independently.
Name it; state why it is the highest-confidence signal.]

**Null hypothesis progression** (per §11):
  g_null(initial) = [copy from BRACKET OPENING]
  g_null(post-domain) = [copy from §3.5]
  g_null(final) = [copy from LIFECYCLE]
  Trajectory summary: [one sentence characterizing the arc]

**Scope coverage**: [Any §1 surface uncovered. If all: "None -- full coverage."]

---

## DISPOSITION

**Gate vector** *(from GATE VECTOR TABLE)*:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply §3 formula** *(mechanical; no editorial reasoning)*:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Primary Driver** per §16 (precedence rules applied to gate vector):
  [gate name] -- [one sentence stating why this gate is primary]

**Conditions** *(complete only if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]
2. [Additional conditions.]

**Blocker** *(complete only if BLOCKED)*:
[If GClose=FAIL: "Challenger final verdict HOLDS -- [GClose Rationale summary]."
Otherwise: specific finding from the FAIL gate.]

---

## ACTION ITEM REGISTER

*Assembly per §8: copy all local gate ledger rows verbatim. DO NOT re-derive
Gate Verdict or Class. Append scope gap items (§5.5), lens items (§5.6 per §17),
and domain gap items (§5.7 per §18).*

| CH-ID | Item Description | Class | Gate Verdict | Owner Role | Resolution Criterion |
|-------|-----------------|-------|-------------|------------|---------------------|
| CH-001 | [description derived from PARTIAL/HOLDS status] | [BLOCKED/CONDITIONAL/ADVISORY per §6] | [copy from ledger] | [ROLE] | [specific resolution] |
| CH-002 | [Item 2] | [class] | [copy] | [ROLE] | [criterion] |
| -- | [ADVISORY-GAP: §1 surface [name] has no reviewer finding] | ADVISORY-GAP | N/A | [ROLE] | [criterion] |
| -- | [ADVISORY-OPEN-LENS: [role] lens "[dim]" HIGH applicability, OPEN] | ADVISORY-OPEN-LENS | N/A | [ROLE] | [criterion] |
| -- | [ADVISORY-GAP: domain "[name]" has no HIGH-applicability reviewer per §5.7] | ADVISORY-GAP | N/A | [ROLE] | [criterion] |

*Item classes per §6 and §12/§15/§18:*
- **BLOCKED**: Resolve before any commitment.
- **CONDITIONAL**: Resolve before next lifecycle phase.
- **ADVISORY**: May defer.
- **ADVISORY-GAP**: Scope surface with no finding (§5.5) or domain with no
  HIGH-applicability reviewer (§5.7).
- **ADVISORY-OPEN-LENS**: HIGH-applicability lens dimension not addressed (§5.6).

---

**Artifact to review:**

{{artifact}}
