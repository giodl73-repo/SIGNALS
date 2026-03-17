---
skill: quest-variate
skill_target: org-review
date: 2026-03-17
round: 15
rubric: org-review-rubric-v11-2026-03-16.md
---

# org-review -- Variate R15

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis and three-axis combinations (V-04, V-05).

**R15 design target**: V-05 R11 scores 210/225 under v11 (C-09 through C-32 all
PASS; C-33/C-34/C-35 absent). V-02 R12 scores ~215/225 (C-33+C-34+C-35 PASS but
C-30 and C-32 lost from V-05 R11 base). Perfect 225/225 requires combining V-05
R11's §14/§15/§16 contracts (C-30+C-31+C-32) with V-02 R12's three new patterns
(C-33+C-34+C-35) simultaneously. R15 isolates each new criterion, confirms the
dependency chain, and produces V-05 as the first candidate for 225/225.

**R15 gap analysis from V-05 R11:**

| Criterion | V-05 R11 | What it requires |
|-----------|----------|-----------------|
| **C-33** | FAIL | LENS COVERAGE TABLE rows carry explicit HIGH/MEDIUM/LOW applicability rating specific to the artifact under review; preamble pre-commits that applicability determines coverage expectations |
| **C-34** | vacuous (C-33 FAIL -> no HIGH-applicability tier to check) | DOMAIN COVERAGE GAP-CHECK pre-committed: after LENS COVERAGE TABLE, identify every artifact domain with no HIGH-applicability reviewer; classify each as ADVISORY-GAP in action register |
| **C-35** | FAIL | Challenger null hypothesis uses structured dimension comparison table (>= 2 dims, current-state score + proposed-state score + per-dim differential); g_null derivable from table values alone |

**Variation axes selected (3 single-axis, then combined):**

- **Inertia framing**: how the challenger evaluates the status quo — prose testimony vs. structured dimension comparison table. C-35 activates here.
- **Output format**: format of the LENS COVERAGE TABLE — two-column (ADDRESSED/OPEN) vs. three-column with Applicability rating. C-33 activates here.
- **Lifecycle emphasis**: scope of coverage protocols post-review — lens exhaustion only vs. lens exhaustion + domain gap-check. C-34 activates here (requires C-33 active as precondition).

**Variation plan:**

| Variant | Axis | C-33 | C-34 | C-35 | Predicted |
|---------|------|------|------|------|-----------|
| V-01 | Inertia framing (single) | FAIL | vacuous | PASS | 215/225 |
| V-02 | Output format (single) | PASS | FAIL | FAIL | 215/225 |
| V-03 | Lifecycle emphasis (single — C-33 included as C-34 precondition) | PASS | PASS | FAIL | 220/225 |
| V-04 | Inertia framing + Output format (two-axis) | PASS | FAIL | PASS | 220/225 |
| V-05 | Inertia framing + Output format + Lifecycle emphasis (three-axis) | PASS | PASS | PASS | **225/225** |

**Isolation hypotheses:**

- **V-01**: Does C-35 alone score +5 on V-05 R11 base without disturbing C-33 (FAIL) and C-34 (vacuous)?
- **V-02**: Does the applicability rating column alone satisfy C-33 (+5), with C-34 now non-vacuous but FAIL (C-31+C-33 both PASS activates C-34, which fails without gap-check)?
- **V-03**: Does the coupled C-33+C-34 package score +10? Confirms C-34 is not vacuous once C-33 is active and multi-domain artifact present.
- **V-04**: Does C-33+C-35 together score +10? C-34 FAIL (active but no gap-check).
- **V-05**: Does the three-axis combination achieve 225/225? No criterion among C-01 through C-35 remains FAIL or vacuous (beyond inherent vacuity chains).

---

## V-01

**Axis**: Inertia framing -- challenger uses structured NULL HYPOTHESIS DIMENSION TABLE
at BRACKET OPENING; LENS COVERAGE TABLE has no applicability ratings (C-33 FAIL);
no domain gap-check (C-34 vacuous -- C-33 FAIL means no HIGH-applicability tier).

**Hypothesis**: Adding the dimension comparison table (C-35) to V-05 R11's base earns
+5 pts. C-33 remains FAIL. C-34 vacuous. Score: 210+5 = 215/225.

---

You are running `/org-review`.

**Inputs:**
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .craft/roles/]
```

Acknowledge injected values -- state `artifact_id`, `depth`, and `reviewer_set` -- before executing any section.

---

### ORG-REVIEW EXECUTION CONTRACTS v4

```
======================================================================
ORG-REVIEW EXECUTION CONTRACTS v4
[IMMUTABLE BLOCK -- do not alter, reorder, or add between items.
All contracts are pre-committed before any reviewer section runs.]
======================================================================

§1 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical execution sequence (reordering is a contract violation):
    1.  ROLE MANIFEST
    2.  BRACKET OPENING (challenger / inertia-advocate)
    3.  DOMAIN reviewer section(s) -- one per active reviewer in {{reviewer_set}}
    4.  §3.5 DOMAIN-AGGREGATE CHECKPOINT     [excluded from gate ledger -- §6]
    5.  §3.8 CH-ID SATURATION CHECK          [excluded from gate ledger -- §6]
    6.  LIFECYCLE reviewer section
    7.  BRACKET CLOSING (challenger / inertia-advocate)
    8.  MASTER GATE VECTOR TABLE
    9.  LENS COVERAGE TABLE
   10.  §5.5 SCOPE COVERAGE RECONCILIATION   [excluded from gate ledger -- §6]
   11.  CROSS-ROLE SIGNALS
   12.  DISPOSITION
   13.  ACTION ITEM REGISTER

§2 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED     <- GClose = FAIL  (override: null hypothesis holds)
               OR any Gi in {GOpen, G_domain_agg, G_lifecycle} = FAIL
  CONDITIONAL <- no Gi = FAIL  AND  exists Gi = CONDITIONAL
  READY       <- all Gi = PASS

§3 -- CLASS DERIVATION CONTRACT [IMMUTABLE]
  Gate verdict -> action item class (derived mechanically, not editorially):
    FAIL gate                  -> BLOCKED
    CONDITIONAL gate           -> CONDITIONAL
    PASS gate (advisory obs.)  -> ADVISORY / ADVISORY-OBS

§4 -- NULL HYPOTHESIS DERIVATION RULE [IMMUTABLE]
  Three-alternative form (Status Quo / Build / Best Non-Build Alternative):
    g_null = DEFEATED if diff(Build, Status Quo) > 0 AND diff(Build, Best Alt) > 0
    g_null = PARTIAL  if exactly one differential > 0
    g_null = HOLDS    if both differentials <= 0
  Derivable from dimension table values without reading challenger prose.

§5 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Syntax of a local gate ledger row:
    GATE-LEDGER | Role: [name] | Gate: [label] | Verdict: [P/C/F] |
                  Section-Severity: [H/M/L] | Class: [BLOCKED/CONDITIONAL/ADVISORY]
  Emit: at the end of each verdict-emitting reviewer section, after the verdict.
  Assembly: copy all local rows verbatim into MASTER GATE VECTOR TABLE.
            Do NOT re-derive Gate Verdict or Class during assembly.

§6 -- NON-VERDICT SECTION EXCLUSIONS [IMMUTABLE]
  The following sections emit NO gate ledger rows:
    §3.5 DOMAIN-AGGREGATE CHECKPOINT  -- produces no gate verdict
    §3.8 CH-ID SATURATION CHECK        -- produces no gate verdict
    §5.5 SCOPE COVERAGE RECONCILIATION -- informational only
  Listing any of these sections under §5 universal coverage is a protocol error.

§7 -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  When multiple domain reviewers are active:
    G_domain_agg = worst(G_domain_1, G_domain_2, ...) where FAIL > CONDITIONAL > PASS
  §3.5 applies this formula. §3.5 emits no ledger row (§6).

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED      = every CH-ID has received >= 1 domain response before LIFECYCLE runs.
  FULLY SATURATED = every CH-ID has received both a domain and a lifecycle response
                    before BRACKET CLOSING.
  §3.8 verifies SATURATED status after domain sections and before LIFECYCLE.
  BRACKET CLOSING prohibits PASS if any CH-ID is UNSATURATED without a named waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Three-stage mechanical derivation:
    Stage 1: g_null(initial)     = GOpen                                [BRACKET OPENING]
    Stage 2: g_null(post-domain) = worst(G_domain_agg, g_null(initial)) [§3.5]
    Stage 3: g_null(final)       = worst(G_lifecycle, g_null(post-domain)) [BRACKET CLOSING]
  GClose verdict must equal g_null(final). Deviation requires explicit override + justification.
  The three g_null values are emitted as labeled fields at their respective checkpoints.
  Progression summary appears in CROSS-ROLE SIGNALS.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  After BRACKET CLOSING: §5.5 SCOPE COVERAGE RECONCILIATION executes.
  Classification of each §1 IN-SCOPE surface:
    COVERED = surface appears in >= 1 finding across all reviewer sections.
    GAP     = no finding references this surface.
  GAP surfaces -> LOW advisory severity -> ACTION ITEM REGISTER as ADVISORY-GAP.
  §5.5 emits no gate ledger row (§6). Output is informational only.
  §1 IN-SCOPE rows carry the annotation: "[cited in §5.5 SCOPE COVERAGE RECONCILIATION]"

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Every finding row in every reviewer section carries an individual Severity (HIGH/MEDIUM/LOW).
  Section Severity = worst(F-1-sev, F-2-sev, ...) over all individual finding rows.
    worst() precedence: HIGH > MEDIUM > LOW
  Section Severity feeds the gate ledger row. No editorial section-level severity permitted.

§15 -- LENS COVERAGE TABLE PROTOCOL [IMMUTABLE]
  After all reviewer sections complete, before DISPOSITION:
  For each active reviewer role, every lens.verify entry from that role's definition
  must appear in the LENS COVERAGE TABLE with status:
    ADDRESSED = a finding in this review references this lens dimension
    OPEN      = no finding referenced this lens dimension
  OPEN entries -> ADVISORY-OPEN-LENS items in ACTION ITEM REGISTER.
  Table is produced before DISPOSITION.
  Schema:
  | Role | Lens.Verify Entry | Status |
  |------|------------------|--------|
  | [ROLE] | [LENS_ENTRY] | [ADDRESSED / OPEN] |

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  After all gate verdicts are known, apply the following precedence rules in order
  to derive the Primary Driver of the DISPOSITION:
    Rule 1: GClose = FAIL         -> Primary Driver = GClose
    Rule 2: GOpen  = FAIL         -> Primary Driver = GOpen
    Rule 3: G_domain_agg = FAIL   -> Primary Driver = G_domain_agg
    Rule 4: G_lifecycle  = FAIL   -> Primary Driver = G_lifecycle
    Rule 5: No FAIL, first CONDITIONAL in {GOpen, G_domain_agg, G_lifecycle, GClose}
                                  -> Primary Driver = that gate
    Rule 6: All PASS              -> Primary Driver = GClose (final confirmation)
  Primary Driver emitted as labeled field at DISPOSITION. Auditable from gate verdict
  vector alone without reading reviewer narrative.

======================================================================
END ORG-REVIEW EXECUTION CONTRACTS v4
======================================================================
```

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§5;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
[Fill this section before proceeding.]

IN-SCOPE -- surfaces this review will evaluate: [cited in §5.5 SCOPE COVERAGE RECONCILIATION]
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive.)

OUT-OF-SCOPE -- surfaces this review will not evaluate:
  1. [SURFACE -- REASON_EXCLUDED]

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
  Silent scope expansion violates this contract.

§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment. No commitment proceeds with open HIGH findings.
  MEDIUM = Conditions commitment. Proceeds only after named resolution.
  LOW    = Advisory. Commitment may proceed.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  (Applied per §2 of ORG-REVIEW EXECUTION CONTRACTS v4.)

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, ...).
  Every downstream section carries a mandatory CH-ID response table.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/` filtered by `{{reviewer_set}}`. If `{{reviewer_set}} = auto`,
select roles matching the artifact domain. Assign each slot:

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `{{depth}} = deep`: add DOMAIN-2, DOMAIN-3. State total count.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*g_null(initial) emitted here per §9.*

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**NULL HYPOTHESIS DIMENSION TABLE**
*(C-35: populate before domain testimony; g_null(initial) derivable from table values alone
without reading prose; apply §4 rule to table differentials to derive verdict)*:

| Dimension | Current-State | Proposed-State | Delta | Dim-Verdict |
|-----------|--------------|----------------|-------|-------------|
| [DIM_1]   | [SCORE_OR_RATING] | [SCORE_OR_RATING] | [+/−/=] | [ADV / NEUTRAL / DISADV] |
| [DIM_2]   | [SCORE_OR_RATING] | [SCORE_OR_RATING] | [+/−/=] | [ADV / NEUTRAL / DISADV] |
| [DIM_3]   | [SCORE_OR_RATING] | [SCORE_OR_RATING] | [+/−/=] | [ADV / NEUTRAL / DISADV] |

*g_null(initial): DEFEATED if ADV > DISADV AND build beats best non-build alt;
PARTIAL if mixed; HOLDS if DISADV dominant or no advantage over best alternative.*

**g_null(initial)**: [DEFEATED / PARTIAL / HOLDS]

**Challenge claims** *(assign CH-IDs; carry to every downstream section per §5)*:

| CH-ID  | Challenge Claim | Severity |
|--------|----------------|----------|
| CH-001 | [switching cost, workaround viability, or adoption friction -- one sentence] | [H/M/L] |
| CH-002 | [CLAIM_2] | [H/M/L] |
| CH-003 | [CLAIM_3 -- optional] | [H/M/L] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

*GOpen and all CH-IDs carry forward to every downstream section.*

GATE-LEDGER | Role: [CHALLENGER_ROLE] | Gate: GOpen | Verdict: [P/C/F] | Section-Severity: [H/M/L] | Class: [BLOCKED/CONDITIONAL/ADVISORY per §3]

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]

**CH-ID Response Table** *(mandatory per §5 -- PASS verdict prohibited if any row = OPEN)*:

| CH-ID  | Challenge Claim (copy) | This Role's Technical Response | Status |
|--------|----------------------|-------------------------------|--------|
| CH-001 | [copy full claim] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

*(PARTIAL requires a named resolution path. OPEN = claim not addressable from this frame.)*

**Findings** *(each row carries individual Severity per §14)*:

| #   | Finding | Severity |
|-----|---------|----------|
| F-1 | [from this role's `lens.verify` -- names an in-scope surface] | [H/M/L] |
| F-2 | [finding] | [H/M/L] |
| F-3 | [optional] | [H/M/L] |
| F-4 | [optional] | [H/M/L] |

**Section Severity**: [worst(F-1, F-2, ...) per §14]

**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence. If CONDITIONAL: name condition. If FAIL: name gap.]

*(For `{{depth}} = deep`: repeat labeled DOMAIN-2, DOMAIN-3.)*

**G_domain Aggregate**: [worst(all DOMAIN verdicts) per §7]

GATE-LEDGER | Role: [DOMAIN_ROLE] | Gate: G_domain | Verdict: [P/C/F] | Section-Severity: [H/M/L] | Class: [class per §3]

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*Excluded from gate ledger per §6 -- no ledger row emitted here.*

**G_domain_agg**: [copy from DOMAIN Aggregate above]
**g_null(post-domain)**: [worst(G_domain_agg, g_null(initial)) per §9]

---

## §3.8 CH-ID SATURATION CHECK

*Excluded from gate ledger per §6.*

| CH-ID  | Domain Response Received | Saturation Status |
|--------|--------------------------|-------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED] |

Pre-LIFECYCLE saturation: [SATURATED / UNSATURATED]
*(If UNSATURATED: name waiver or block LIFECYCLE from proceeding.)*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]
Received G_domain_agg: [copy]

**CH-ID Response Table** *(mandatory per §5)*:

| CH-ID  | Challenge Claim (copy) | Commitment-Frame Response | Status |
|--------|----------------------|--------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [Is evidence sufficient for commitment given GOpen
and G_domain_agg? One paragraph referencing both received verdicts explicitly.]

**Null hypothesis status**: [Given GOpen and G_domain, has the null hypothesis been
defeated? yes / partial / no -- one sentence justification.]

**Findings** *(each row carries individual Severity per §14)*:

| #   | Finding | Severity |
|-----|---------|----------|
| F-1 | [commitment, program, or decision concern from this role's `lens.verify`] | [H/M/L] |
| F-2 | [finding] | [H/M/L] |

**Section Severity**: [worst(F-1, F-2, ...) per §14]

**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

GATE-LEDGER | Role: [LIFECYCLE_ROLE] | Gate: G_lifecycle | Verdict: [P/C/F] | Section-Severity: [H/M/L] | Class: [class per §3]

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: scope declaration, all CH-ID tables, all gate verdicts.*

Received GOpen: [copy]
Received G_domain_agg: [copy]
Received G_lifecycle: [copy]

**g_null(final)**: [worst(G_lifecycle, g_null(post-domain)) per §9 -- must equal GClose or explicit override required]

**CH-ID Final Assessment**:

| CH-ID  | G_domain Status | G_lifecycle Status | Final Status | Notes |
|--------|-----------------|--------------------|--------------|-------|
| CH-001 | [copy from DOMAIN] | [copy from LIFECYCLE] | [DEFEATED / PARTIAL / HOLDS] | [one sentence] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

Saturation check: [FULLY SATURATED / UNSATURATED -- per §8; PASS prohibited if UNSATURATED without waiver]

**Remaining gaps**: [What was not fully addressed. "None -- all CH-IDs DEFEATED." if clean.]

**Override invoked**: [YES / NO]
*(If YES: state justification. Override authority per §§2, §3, §8, §9 of EXECUTION CONTRACTS.)*

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
- PASS (= DEFEATED): All CH-IDs DEFEATED -- record defeats null hypothesis.
- CONDITIONAL (= PARTIAL): Some CH-IDs PARTIAL -- material gaps remain; name them.
- FAIL (= HOLDS): At least one CH-ID HOLDS -- null hypothesis survives.

**GClose Rationale**: [2-3 sentences explaining the verdict.]

GATE-LEDGER | Role: [CHALLENGER_ROLE] | Gate: GClose | Verdict: [P/C/F] | Section-Severity: [H/M/L] | Class: [class per §3]

---

## MASTER GATE VECTOR TABLE

*Assembled by verbatim copy of local gate ledger rows per §5. Do not re-derive Gate Verdict or Class.*

| Gate | Role | Verdict | Section-Severity | Class | Contract Cite |
|------|------|---------|-----------------|-------|---------------|
| GOpen | [CHALLENGER_ROLE] | [P/C/F] | [H/M/L] | [class] | DISPOSITION_CONTRACT v1 |
| G_domain | [DOMAIN_ROLE(S)] | [P/C/F] | [H/M/L] | [class] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE_ROLE] | [P/C/F] | [H/M/L] | [class] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER_ROLE] | [P/C/F] | [H/M/L] | [class] | DISPOSITION_CONTRACT v1 |

---

## LENS COVERAGE TABLE

*Per §15: every lens.verify entry from each active role. Produced after all reviewer
sections and before DISPOSITION. OPEN entries -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.*

| Role | Lens.Verify Entry | Status |
|------|------------------|--------|
| [ROLE_1] | [LENS_ENTRY] | [ADDRESSED / OPEN] |
| [ROLE_2] | [LENS_ENTRY] | [ADDRESSED / OPEN] |

*(No applicability rating column in this variant -- C-33 absent.)*

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*Excluded from gate ledger per §6 -- informational only.*

| §1 IN-SCOPE Surface | Covered By | Status |
|--------------------|-----------|--------|
| [SURFACE_1] | [ROLE / finding ref] | [COVERED / GAP] |
| [SURFACE_2] | [ROLE / finding ref] | [COVERED / GAP] |

GAP surfaces appended to ACTION ITEM REGISTER as ADVISORY-GAP (LOW advisory severity).

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Two reviewers with incompatible CH-ID responses or incompatible findings.
"None detected." if clean.]

**Convergence**: [CH-ID or concern named independently by two or more reviewers -- name it
and state why it is the highest-confidence signal.]

**g_null progression** *(per §9)*:
- g_null(initial): [copy from BRACKET OPENING]
- g_null(post-domain): [copy from §3.5]
- g_null(final): [copy from BRACKET CLOSING]
- Progression summary: [One sentence describing trajectory and whether it was defeated.]

**Scope coverage**: [In-scope surfaces not covered by any reviewer. "None -- full coverage." if clean.]

---

## DISPOSITION

**Gate vector** *(from MASTER GATE VECTOR TABLE)*:
- GOpen        = [copy]
- G_domain_agg = [copy]
- G_lifecycle  = [copy]
- GClose       = [copy]

**Apply §2 DISPOSITION ALGEBRA** *(do not reason editorially -- evaluate formula)*:
```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Primary Driver** *(apply §16 precedence rules in order)*:
[Rule applied: Rule N -- Primary Driver = [gate name] -- [one-sentence derivation]]

**Conditions** *(complete only if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate. Gate order: GOpen before G_domain before G_lifecycle before GClose.]

**Blocker** *(complete only if BLOCKED)*: [Specific finding from the FAIL gate. If GClose = FAIL,
lead with: "Challenger final verdict HOLDS -- [GClose Rationale summary]."]

---

## ACTION ITEM REGISTER

*Sources: (a) PARTIAL/HOLDS CH-IDs from BRACKET CLOSING; (b) ADVISORY-OPEN-LENS from §15;
(c) ADVISORY-GAP from §5.5; (d) advisory observations not CH-ID-sourced (class ADVISORY-OBS).
Assembly: verbatim copy per §5. Class derives from gate verdict per §3 -- do not reassign.*

| CH-ID | Gate | Gate Verdict | Item Description | Class | Owner Role | Resolution Criterion |
|-------|------|-------------|-----------------|-------|------------|---------------------|
| CH-001 | [gate] | [P/C/F] | [What must be done] | [BLOCKED/CONDITIONAL/ADVISORY] | [ROLE] | [Specific resolution criterion] |
| -- | §15 (ADVISORY-OPEN-LENS) | -- | [Lens dimension that was OPEN] | ADVISORY | [ROLE] | [Criterion] |
| -- | §5.5 (ADVISORY-GAP) | -- | [Surface with no covering finding] | ADVISORY | [ROLE] | [Criterion] |

---

**Artifact to review:**

{{artifact_id}}

---

---

## V-02

**Axis**: Output format -- LENS COVERAGE TABLE rows carry explicit HIGH/MEDIUM/LOW
applicability rating per lens entry (C-33 PASS); no domain gap-check (C-34 FAIL --
C-31+C-33 both PASS activates C-34 as non-vacuous, but no gap-check is present);
no challenger dimension table (C-35 FAIL).

**Hypothesis**: Adding applicability ratings to the LENS COVERAGE TABLE earns +5.
C-34 becomes active (no longer vacuous) but fails because §17 is absent. C-35
absent. Score: 210+5 = 215/225.

---

You are running `/org-review`.

**Inputs:**
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .craft/roles/]
```

Acknowledge injected values -- state `artifact_id`, `depth`, and `reviewer_set` -- before executing any section.

---

### ORG-REVIEW EXECUTION CONTRACTS v4

```
======================================================================
ORG-REVIEW EXECUTION CONTRACTS v4
[IMMUTABLE BLOCK]
======================================================================

§1 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical execution sequence:
    1.  ROLE MANIFEST
    2.  BRACKET OPENING (challenger)
    3.  DOMAIN reviewer section(s)
    4.  §3.5 DOMAIN-AGGREGATE CHECKPOINT     [excluded -- §6]
    5.  §3.8 CH-ID SATURATION CHECK          [excluded -- §6]
    6.  LIFECYCLE reviewer section
    7.  BRACKET CLOSING (challenger)
    8.  MASTER GATE VECTOR TABLE
    9.  LENS COVERAGE TABLE
   10.  §5.5 SCOPE COVERAGE RECONCILIATION   [excluded -- §6]
   11.  CROSS-ROLE SIGNALS
   12.  DISPOSITION
   13.  ACTION ITEM REGISTER

§2 through §14 -- [identical to V-01]

§15 -- LENS COVERAGE TABLE PROTOCOL [IMMUTABLE]
  After all reviewer sections complete, before DISPOSITION:
  For each active reviewer role, every lens.verify entry must appear in the
  LENS COVERAGE TABLE. Each row carries:
    (a) APPLICABILITY RATING (HIGH / MEDIUM / LOW) specific to the artifact under
        review -- not a generic role-capability rating attached to the role definition.
    (b) COVERAGE STATUS: ADDRESSED (a finding references this lens dimension) or
        OPEN (no finding referenced this lens dimension).
  Coverage tier expectations (pre-committed):
    HIGH-applicability lens: must be ADDRESSED.
                             OPEN generates ADVISORY-OPEN-LENS action item.
    MEDIUM-applicability lens: OPEN is flagged as a coverage note; no action item.
    LOW-applicability lens: OPEN is expected; no action item generated.
  Table produced before DISPOSITION.
  Schema:
  | Role | Lens.Verify Entry | Applicability | Status |
  |------|------------------|---------------|--------|
  | [ROLE] | [LENS_ENTRY] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] |

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  [identical to V-01]

======================================================================
END ORG-REVIEW EXECUTION CONTRACTS v4
======================================================================
```

---

[DISPOSITION_CONTRACT v1 -- identical to V-01]

---

## ROLE MANIFEST

[identical to V-01]

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*g_null(initial) emitted here per §9.*

**Null hypothesis**: [What the team does today instead -- one sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives considered**:
- Status Quo: [describe current approach]
- Build: [describe the proposed artifact]
- Best Non-Build Alternative: [describe -- e.g., incremental improvement, buy/partner]

**Challenger evaluation**: [2-3 sentences: why the status quo is viable. Names switching
cost, workaround adequacy, and adoption friction.]

**g_null(initial)**: [DEFEATED / PARTIAL / HOLDS -- one sentence applying §4 rule to alternatives]

*(No dimension comparison table in this variant -- C-35 absent.)*

**Challenge claims** *(assign CH-IDs)*:

| CH-ID  | Challenge Claim | Severity |
|--------|----------------|----------|
| CH-001 | [switching cost, workaround viability, or adoption friction] | [H/M/L] |
| CH-002 | [CLAIM_2] | [H/M/L] |
| CH-003 | [CLAIM_3 -- optional] | [H/M/L] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

GATE-LEDGER | Role: [CHALLENGER_ROLE] | Gate: GOpen | Verdict: [P/C/F] | Section-Severity: [H/M/L] | Class: [class per §3]

---

[DOMAIN, §3.5, §3.8, LIFECYCLE, BRACKET CLOSING, MASTER GATE VECTOR TABLE --
identical to V-01]

---

## LENS COVERAGE TABLE

*Per §15: three-column schema with Applicability rating (C-33 PASS). Produced after
all reviewer sections, before DISPOSITION. HIGH-applicability OPEN entries ->
ADVISORY-OPEN-LENS in ACTION ITEM REGISTER. MEDIUM/LOW OPEN entries noted only.*

| Role | Lens.Verify Entry | Applicability | Status |
|------|------------------|---------------|--------|
| [ROLE_1] | [LENS_ENTRY_A] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] |
| [ROLE_1] | [LENS_ENTRY_B] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] |
| [ROLE_2] | [LENS_ENTRY_A] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] |

*(No §9.5 DOMAIN COVERAGE GAP-CHECK in this variant -- C-34 absent.)*

---

[§5.5, CROSS-ROLE SIGNALS, DISPOSITION, ACTION ITEM REGISTER -- identical to V-01]

---

**Artifact to review:**

{{artifact_id}}

---

---

## V-03

**Axis**: Lifecycle emphasis -- LENS COVERAGE TABLE has applicability ratings (C-33
PASS, precondition for C-34) AND DOMAIN COVERAGE GAP-CHECK pre-committed (C-34 PASS);
no challenger dimension table (C-35 FAIL).

**Hypothesis**: C-33+C-34 as a coupled unit earns +10. C-34 is not vacuous because
C-31+C-33 both PASS and multi-domain artifact is present. C-35 absent. Score:
210+5+5 = 220/225.

*Note: C-34 without C-33 is vacuous (no HIGH-applicability tier to check against).
This variant treats C-33 as the structural precondition for C-34; the combined
"lifecycle emphasis" axis covers both the table format and the gap-check protocol
that depends on it.*

---

You are running `/org-review`.

**Inputs:**
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .craft/roles/]
```

Acknowledge injected values before executing any section.

---

### ORG-REVIEW EXECUTION CONTRACTS v4

```
======================================================================
ORG-REVIEW EXECUTION CONTRACTS v4
[IMMUTABLE BLOCK]
======================================================================

§1 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical execution sequence:
    1.  ROLE MANIFEST
    2.  BRACKET OPENING (challenger)
    3.  DOMAIN reviewer section(s)
    4.  §3.5 DOMAIN-AGGREGATE CHECKPOINT     [excluded -- §6]
    5.  §3.8 CH-ID SATURATION CHECK          [excluded -- §6]
    6.  LIFECYCLE reviewer section
    7.  BRACKET CLOSING (challenger)
    8.  MASTER GATE VECTOR TABLE
    9.  LENS COVERAGE TABLE
   10.  §9.5 DOMAIN COVERAGE GAP-CHECK        [excluded -- §6]   <- NEW in V-03
   11.  §5.5 SCOPE COVERAGE RECONCILIATION    [excluded -- §6]
   12.  CROSS-ROLE SIGNALS
   13.  DISPOSITION
   14.  ACTION ITEM REGISTER

§2 through §14 -- [identical to V-01]

§15 -- LENS COVERAGE TABLE PROTOCOL [IMMUTABLE]
  [identical to V-02 -- three-column schema with Applicability rating]
  Schema:
  | Role | Lens.Verify Entry | Applicability | Status |
  |------|------------------|---------------|--------|

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  [identical to V-01]

§17 -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  After LENS COVERAGE TABLE is populated (§15), §9.5 executes:
  Step 1: Enumerate all artifact domains derived from §1 IN-SCOPE surfaces.
  Step 2: For each artifact domain, identify the highest applicability tier among
          all active reviewer roles for that domain (from LENS COVERAGE TABLE).
  Step 3: Classify:
            COVERED = >= 1 reviewer has HIGH applicability to this domain
            GAP     = no reviewer has HIGH applicability to this domain
  Step 4: GAP domains -> ACTION ITEM REGISTER as ADVISORY-GAP items, recording:
            - Domain name
            - Highest applicability among all reviewers for this domain (MEDIUM/LOW/absent)
            - Reason for gap (absent role, all lenses OPEN, or applicability ceiling MEDIUM/LOW)
  §9.5 emits no gate ledger row (informational only -- §6).
  This protocol is pre-committed and does not run editorially.
  Schema:
  | Artifact Domain | Highest Reviewer Applicability | Coverage Status |
  |----------------|-------------------------------|-----------------|
  | [DOMAIN] | [HIGH / MEDIUM / LOW / absent] | [COVERED / GAP] |

======================================================================
END ORG-REVIEW EXECUTION CONTRACTS v4
======================================================================
```

---

[DISPOSITION_CONTRACT v1 -- identical to V-01]
[ROLE MANIFEST -- identical to V-01]

---

## BRACKET OPENING -- CHALLENGER [V-03: standard prose, no dimension table]

Contract: DISPOSITION_CONTRACT v1
*g_null(initial) emitted here per §9.*

**Null hypothesis**: [one sentence]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives considered**:
- Status Quo: [describe]
- Build: [describe]
- Best Non-Build Alternative: [describe]

**Challenger evaluation**: [2-3 sentences. Names switching cost, workaround adequacy,
adoption friction.]

**g_null(initial)**: [DEFEATED / PARTIAL / HOLDS -- applying §4 rule]

*(No dimension comparison table -- C-35 absent.)*

**Challenge claims**:

| CH-ID  | Challenge Claim | Severity |
|--------|----------------|----------|
| CH-001 | [claim] | [H/M/L] |
| CH-002 | [claim] | [H/M/L] |
| CH-003 | [optional] | [H/M/L] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

GATE-LEDGER | Role: [CHALLENGER_ROLE] | Gate: GOpen | Verdict: [P/C/F] | Section-Severity: [H/M/L] | Class: [class]

---

[DOMAIN, §3.5, §3.8, LIFECYCLE, BRACKET CLOSING, MASTER GATE VECTOR TABLE --
identical to V-01]

---

## LENS COVERAGE TABLE [V-03: three-column with Applicability -- same as V-02]

| Role | Lens.Verify Entry | Applicability | Status |
|------|------------------|---------------|--------|
| [ROLE_1] | [LENS_ENTRY] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] |
| [ROLE_2] | [LENS_ENTRY] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] |

---

## §9.5 DOMAIN COVERAGE GAP-CHECK

*Per §17 -- excluded from gate ledger (§6). Runs after LENS COVERAGE TABLE.*

| Artifact Domain | Highest Reviewer Applicability | Coverage Status |
|----------------|-------------------------------|-----------------|
| [DOMAIN_1] | [HIGH / MEDIUM / LOW] | [COVERED / GAP] |
| [DOMAIN_2] | [MEDIUM] | [GAP] |

GAP domains appended to ACTION ITEM REGISTER as ADVISORY-GAP, naming domain, highest
applicability tier, and reason for gap.

---

[§5.5, CROSS-ROLE SIGNALS, DISPOSITION -- identical to V-01]

---

## ACTION ITEM REGISTER [V-03: includes ADVISORY-GAP items from §9.5]

| CH-ID | Gate | Gate Verdict | Item Description | Class | Owner Role | Resolution Criterion |
|-------|------|-------------|-----------------|-------|------------|---------------------|
| CH-001 | [gate] | [P/C/F] | [description] | [class] | [ROLE] | [criterion] |
| -- | §15 (ADVISORY-OPEN-LENS) | -- | [OPEN lens dimension with HIGH applicability] | ADVISORY | [ROLE] | [criterion] |
| -- | §9.5 (ADVISORY-GAP) | -- | [Artifact domain with no HIGH-applicability reviewer] | ADVISORY | [ROLE] | [criterion] |
| -- | §5.5 (ADVISORY-GAP) | -- | [Surface with no covering finding] | ADVISORY | [ROLE] | [criterion] |

---

**Artifact to review:**

{{artifact_id}}

---

---

## V-04

**Axes**: Inertia framing + Output format -- challenger uses dimension comparison
table (C-35 PASS) AND LENS COVERAGE TABLE has applicability ratings (C-33 PASS);
no domain gap-check (C-34 FAIL -- C-31+C-33 both PASS so C-34 is active/non-vacuous,
but no §17 protocol is present).

**Hypothesis**: C-33+C-35 combined earn +10 over V-05 R11 base. C-34 is active
(non-vacuous) but fails. Score: 210+5+5 = 220/225.

---

You are running `/org-review`.

**Inputs:**
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .craft/roles/]
```

Acknowledge injected values before executing any section.

---

### ORG-REVIEW EXECUTION CONTRACTS v4

```
======================================================================
ORG-REVIEW EXECUTION CONTRACTS v4
[IMMUTABLE BLOCK]
======================================================================

§1 -- SECTION ORDER CONTRACT [IMMUTABLE]
  [identical to V-01 -- no §9.5 section]

§2 through §14 -- [identical to V-01]

§15 -- LENS COVERAGE TABLE PROTOCOL [IMMUTABLE]
  [identical to V-02 -- three-column with Applicability rating]

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  [identical to V-01]

======================================================================
END ORG-REVIEW EXECUTION CONTRACTS v4
======================================================================
```

---

[DISPOSITION_CONTRACT v1 -- identical to V-01]
[ROLE MANIFEST -- identical to V-01]

---

## BRACKET OPENING -- CHALLENGER [V-04: dimension table from V-01]

Contract: DISPOSITION_CONTRACT v1
*g_null(initial) emitted here per §9.*

**Null hypothesis**: [one sentence]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**NULL HYPOTHESIS DIMENSION TABLE**
*(C-35: g_null derivable from table values alone; apply §4 rule to table differentials)*:

| Dimension | Current-State | Proposed-State | Delta | Dim-Verdict |
|-----------|--------------|----------------|-------|-------------|
| [DIM_1]   | [SCORE] | [SCORE] | [+/−/=] | [ADV / NEUTRAL / DISADV] |
| [DIM_2]   | [SCORE] | [SCORE] | [+/−/=] | [ADV / NEUTRAL / DISADV] |
| [DIM_3]   | [SCORE] | [SCORE] | [+/−/=] | [ADV / NEUTRAL / DISADV] |

**g_null(initial)**: [DEFEATED / PARTIAL / HOLDS]

**Challenge claims**:

| CH-ID  | Challenge Claim | Severity |
|--------|----------------|----------|
| CH-001 | [claim] | [H/M/L] |
| CH-002 | [claim] | [H/M/L] |
| CH-003 | [optional] | [H/M/L] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

GATE-LEDGER | Role: [CHALLENGER_ROLE] | Gate: GOpen | Verdict: [P/C/F] | Section-Severity: [H/M/L] | Class: [class]

---

[DOMAIN, §3.5, §3.8, LIFECYCLE, BRACKET CLOSING, MASTER GATE VECTOR TABLE --
identical to V-01]

---

## LENS COVERAGE TABLE [V-04: three-column with Applicability]

| Role | Lens.Verify Entry | Applicability | Status |
|------|------------------|---------------|--------|
| [ROLE_1] | [LENS_ENTRY] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] |
| [ROLE_2] | [LENS_ENTRY] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] |

*(No §9.5 DOMAIN COVERAGE GAP-CHECK -- C-34 absent.)*

---

[§5.5, CROSS-ROLE SIGNALS, DISPOSITION, ACTION ITEM REGISTER -- identical to V-01]

---

**Artifact to review:**

{{artifact_id}}

---

---

## V-05

**Axes**: Inertia framing + Output format + Lifecycle emphasis -- full integration.
Challenger uses dimension comparison table (C-35 PASS). LENS COVERAGE TABLE has
applicability ratings (C-33 PASS). DOMAIN COVERAGE GAP-CHECK pre-committed (C-34 PASS).
V-05 R11 base (C-09 through C-32 all PASS) + all three new criteria simultaneously.

**Hypothesis**: First candidate for 225/225. No criterion among C-01 through C-35
remains FAIL. C-34 is not vacuous (C-31+C-33 both PASS + multi-domain artifact present).
Score: 210+5+5+5 = 225/225.

---

You are running `/org-review`.

**Inputs:**
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .craft/roles/]
```

Acknowledge injected values -- state `artifact_id`, `depth`, and `reviewer_set` -- before executing any section.

---

### ORG-REVIEW EXECUTION CONTRACTS v4

```
======================================================================
ORG-REVIEW EXECUTION CONTRACTS v4
[IMMUTABLE BLOCK -- do not alter, reorder, or add between items.
All contracts pre-committed before any reviewer section runs.]
======================================================================

§1 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical execution sequence (reordering is a contract violation):
    1.  ROLE MANIFEST
    2.  BRACKET OPENING (challenger / inertia-advocate)
    3.  DOMAIN reviewer section(s)
    4.  §3.5 DOMAIN-AGGREGATE CHECKPOINT     [excluded from gate ledger -- §6]
    5.  §3.8 CH-ID SATURATION CHECK          [excluded from gate ledger -- §6]
    6.  LIFECYCLE reviewer section
    7.  BRACKET CLOSING (challenger / inertia-advocate)
    8.  MASTER GATE VECTOR TABLE
    9.  LENS COVERAGE TABLE
   10.  §9.5 DOMAIN COVERAGE GAP-CHECK        [excluded from gate ledger -- §6]
   11.  §5.5 SCOPE COVERAGE RECONCILIATION    [excluded from gate ledger -- §6]
   12.  CROSS-ROLE SIGNALS
   13.  DISPOSITION
   14.  ACTION ITEM REGISTER

§2 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED     <- GClose = FAIL  (override: null hypothesis holds)
               OR any Gi in {GOpen, G_domain_agg, G_lifecycle} = FAIL
  CONDITIONAL <- no Gi = FAIL  AND  exists Gi = CONDITIONAL
  READY       <- all Gi = PASS

§3 -- CLASS DERIVATION CONTRACT [IMMUTABLE]
  FAIL gate                  -> BLOCKED
  CONDITIONAL gate           -> CONDITIONAL
  PASS gate (advisory obs.)  -> ADVISORY / ADVISORY-OBS

§4 -- NULL HYPOTHESIS DERIVATION RULE [IMMUTABLE]
  Three-alternative form (Status Quo / Build / Best Non-Build Alternative):
    g_null = DEFEATED if diff(Build, Status Quo) > 0 AND diff(Build, Best Alt) > 0
    g_null = PARTIAL  if exactly one differential > 0
    g_null = HOLDS    if both differentials <= 0
  Derivable from dimension table values without reading prose.

§5 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Syntax:
    GATE-LEDGER | Role: [name] | Gate: [label] | Verdict: [P/C/F] |
                  Section-Severity: [H/M/L] | Class: [BLOCKED/CONDITIONAL/ADVISORY]
  Emit: end of each verdict-emitting reviewer section, after verdict.
  Assembly: copy all local rows verbatim into MASTER GATE VECTOR TABLE.
            Do NOT re-derive Gate Verdict or Class during assembly.

§6 -- NON-VERDICT SECTION EXCLUSIONS [IMMUTABLE]
  The following sections emit NO gate ledger rows:
    §3.5 DOMAIN-AGGREGATE CHECKPOINT  -- no gate verdict
    §3.8 CH-ID SATURATION CHECK        -- no gate verdict
    §9.5 DOMAIN COVERAGE GAP-CHECK     -- informational only
    §5.5 SCOPE COVERAGE RECONCILIATION -- informational only

§7 -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(G_domain_1, G_domain_2, ...) where FAIL > CONDITIONAL > PASS
  Applied at §3.5. §3.5 emits no ledger row (§6).

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED      = every CH-ID has >= 1 domain response before LIFECYCLE runs.
  FULLY SATURATED = every CH-ID has domain + lifecycle response before BRACKET CLOSING.
  §3.8 verifies SATURATED. BRACKET CLOSING prohibits PASS if UNSATURATED without waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial)     = GOpen                                [BRACKET OPENING]
  Stage 2: g_null(post-domain) = worst(G_domain_agg, g_null(initial)) [§3.5]
  Stage 3: g_null(final)       = worst(G_lifecycle, g_null(post-domain)) [BRACKET CLOSING]
  GClose must equal g_null(final). Deviation requires explicit override + justification.
  Three g_null values emitted as labeled fields at their checkpoints.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  After BRACKET CLOSING: §5.5 executes.
  COVERED = surface appears in >= 1 finding. GAP = no finding.
  GAP -> LOW advisory -> ACTION ITEM REGISTER as ADVISORY-GAP.
  §5.5 emits no ledger row (§6).
  §1 IN-SCOPE rows annotated: "[cited in §5.5 SCOPE COVERAGE RECONCILIATION]"

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Every finding row carries individual Severity (HIGH/MEDIUM/LOW).
  Section Severity = worst(F-1, F-2, ...) over all finding rows in that section.
  Feeds gate ledger row. No editorial section-level severity permitted.

§15 -- LENS COVERAGE TABLE PROTOCOL [IMMUTABLE]
  After all reviewer sections, before DISPOSITION:
  For each active reviewer role, every lens.verify entry appears in the table with:
    (a) APPLICABILITY RATING (HIGH / MEDIUM / LOW) -- artifact-specific, not generic.
    (b) COVERAGE STATUS: ADDRESSED or OPEN.
  Coverage tier expectations (pre-committed):
    HIGH applicability, OPEN -> ADVISORY-OPEN-LENS action item
    MEDIUM applicability, OPEN -> coverage note only
    LOW applicability, OPEN -> expected; no action item
  Schema:
  | Role | Lens.Verify Entry | Applicability | Status |
  |------|------------------|---------------|--------|

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  Apply in order to derive Primary Driver of DISPOSITION:
    Rule 1: GClose = FAIL         -> Primary Driver = GClose
    Rule 2: GOpen  = FAIL         -> Primary Driver = GOpen
    Rule 3: G_domain_agg = FAIL   -> Primary Driver = G_domain_agg
    Rule 4: G_lifecycle  = FAIL   -> Primary Driver = G_lifecycle
    Rule 5: No FAIL, first CONDITIONAL in {GOpen, G_domain_agg, G_lifecycle, GClose}
                                  -> Primary Driver = that gate
    Rule 6: All PASS              -> Primary Driver = GClose
  Emitted as labeled field at DISPOSITION. Auditable from gate vector alone.

§17 -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  After LENS COVERAGE TABLE (§15), §9.5 executes:
  Step 1: Enumerate all artifact domains from §1 IN-SCOPE surfaces.
  Step 2: For each domain, identify highest applicability among active reviewer roles
          (from LENS COVERAGE TABLE Applicability column).
  Step 3: Classify:
            COVERED = >= 1 reviewer has HIGH applicability to this domain
            GAP     = no reviewer has HIGH applicability to this domain
  Step 4: GAP domains -> ACTION ITEM REGISTER as ADVISORY-GAP, recording:
            - Domain name
            - Highest applicability among reviewers for this domain
            - Reason (absent role / all lenses OPEN / applicability ceiling MEDIUM or LOW)
  §9.5 emits no gate ledger row (§6).
  Schema:
  | Artifact Domain | Highest Reviewer Applicability | Coverage Status |
  |----------------|-------------------------------|-----------------|

======================================================================
END ORG-REVIEW EXECUTION CONTRACTS v4
======================================================================
```

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK]
======================================================================

§1 -- SCOPE ENUMERATION
[Fill before proceeding.]

IN-SCOPE: [cited in §5.5 SCOPE COVERAGE RECONCILIATION]
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

§1 COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions commitment. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  (Applied per §2 of ORG-REVIEW EXECUTION CONTRACTS v4.)

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  CH-IDs assigned at BRACKET OPENING. Every downstream section carries mandatory
  CH-ID response table. PASS prohibited if any CH-ID row = OPEN.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/` filtered by `{{reviewer_set}}`.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `{{depth}} = deep`: add DOMAIN-2, DOMAIN-3.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*g_null(initial) emitted here per §9.*

**Null hypothesis**: [one sentence]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**NULL HYPOTHESIS DIMENSION TABLE**
*(C-35: g_null derivable from table values alone; apply §4 rule to differentials;
populate before domain testimony)*:

| Dimension | Current-State | Proposed-State | Delta | Dim-Verdict |
|-----------|--------------|----------------|-------|-------------|
| [DIM_1]   | [SCORE_OR_RATING] | [SCORE_OR_RATING] | [+/−/=] | [ADV / NEUTRAL / DISADV] |
| [DIM_2]   | [SCORE_OR_RATING] | [SCORE_OR_RATING] | [+/−/=] | [ADV / NEUTRAL / DISADV] |
| [DIM_3]   | [SCORE_OR_RATING] | [SCORE_OR_RATING] | [+/−/=] | [ADV / NEUTRAL / DISADV] |

*g_null(initial): DEFEATED if ADV > DISADV AND build beats best non-build alt;
PARTIAL if mixed; HOLDS if DISADV dominant.*

**g_null(initial)**: [DEFEATED / PARTIAL / HOLDS]

**Challenge claims** *(assign CH-IDs)*:

| CH-ID  | Challenge Claim | Severity |
|--------|----------------|----------|
| CH-001 | [switching cost, workaround viability, or adoption friction] | [H/M/L] |
| CH-002 | [CLAIM_2] | [H/M/L] |
| CH-003 | [CLAIM_3 -- optional] | [H/M/L] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

GATE-LEDGER | Role: [CHALLENGER_ROLE] | Gate: GOpen | Verdict: [P/C/F] | Section-Severity: [H/M/L] | Class: [class per §3]

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table**:

| CH-ID  | Challenge Claim (copy) | Technical Response | Status |
|--------|----------------------|-------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Findings** *(individual Severity per §14)*:

| #   | Finding | Severity |
|-----|---------|----------|
| F-1 | [lens.verify finding naming in-scope surface] | [H/M/L] |
| F-2 | [finding] | [H/M/L] |
| F-3 | [optional] | [H/M/L] |
| F-4 | [optional] | [H/M/L] |

**Section Severity**: [worst(F-1, F-2, ...) per §14]

**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]
**G_domain Aggregate**: [worst among all DOMAIN rows per §7]

GATE-LEDGER | Role: [DOMAIN_ROLE] | Gate: G_domain | Verdict: [P/C/F] | Section-Severity: [H/M/L] | Class: [class per §3]

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*Excluded per §6.*

**G_domain_agg**: [copy]
**g_null(post-domain)**: [worst(G_domain_agg, g_null(initial)) per §9]

---

## §3.8 CH-ID SATURATION CHECK

*Excluded per §6.*

| CH-ID  | Domain Response | Saturation Status |
|--------|----------------|-------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |

Pre-LIFECYCLE saturation: [SATURATED / UNSATURATED]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]
Received G_domain_agg: [copy]

**CH-ID Response Table**:

| CH-ID  | Challenge Claim (copy) | Commitment-Frame Response | Status |
|--------|----------------------|--------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph referencing GOpen and G_domain_agg explicitly.]

**Null hypothesis status**: [yes / partial / no -- one sentence.]

**Findings** *(individual Severity per §14)*:

| #   | Finding | Severity |
|-----|---------|----------|
| F-1 | [commitment or program concern] | [H/M/L] |
| F-2 | [finding] | [H/M/L] |

**Section Severity**: [worst(F-1, F-2, ...) per §14]

**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

GATE-LEDGER | Role: [LIFECYCLE_ROLE] | Gate: G_lifecycle | Verdict: [P/C/F] | Section-Severity: [H/M/L] | Class: [class per §3]

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]
Received G_domain_agg: [copy]
Received G_lifecycle: [copy]

**g_null(final)**: [worst(G_lifecycle, g_null(post-domain)) per §9]

**CH-ID Final Assessment**:

| CH-ID  | G_domain Status | G_lifecycle Status | Final Status | Notes |
|--------|-----------------|--------------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

Saturation check: [FULLY SATURATED / UNSATURATED -- per §8]

**Remaining gaps**: [What was not addressed. "None -- all CH-IDs DEFEATED." if clean.]

**Override invoked**: [YES / NO]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose Rationale**: [2-3 sentences.]

GATE-LEDGER | Role: [CHALLENGER_ROLE] | Gate: GClose | Verdict: [P/C/F] | Section-Severity: [H/M/L] | Class: [class per §3]

---

## MASTER GATE VECTOR TABLE

*Verbatim copy from local gate ledger rows per §5. Do not re-derive.*

| Gate | Role | Verdict | Section-Severity | Class | Contract Cite |
|------|------|---------|-----------------|-------|---------------|
| GOpen | [CHALLENGER] | [P/C/F] | [H/M/L] | [class] | DISPOSITION_CONTRACT v1 |
| G_domain | [DOMAIN] | [P/C/F] | [H/M/L] | [class] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [P/C/F] | [H/M/L] | [class] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [P/C/F] | [H/M/L] | [class] | DISPOSITION_CONTRACT v1 |

---

## LENS COVERAGE TABLE

*Per §15 -- three-column schema with Applicability (C-33 PASS). HIGH-applicability
OPEN entries -> ADVISORY-OPEN-LENS. MEDIUM/LOW OPEN entries noted only.*

| Role | Lens.Verify Entry | Applicability | Status |
|------|------------------|---------------|--------|
| [ROLE_1] | [LENS_ENTRY_A] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] |
| [ROLE_1] | [LENS_ENTRY_B] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] |
| [ROLE_2] | [LENS_ENTRY_A] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] |
| [LIFECYCLE_ROLE] | [LENS_ENTRY] | [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] |

---

## §9.5 DOMAIN COVERAGE GAP-CHECK

*Per §17 -- excluded from gate ledger (§6). Runs after LENS COVERAGE TABLE.*

| Artifact Domain | Highest Reviewer Applicability | Coverage Status |
|----------------|-------------------------------|-----------------|
| [DOMAIN_1] | [HIGH / MEDIUM / LOW] | [COVERED / GAP] |
| [DOMAIN_2] | [MEDIUM] | [GAP] |

GAP domains -> ACTION ITEM REGISTER as ADVISORY-GAP (domain name + highest applicability
+ reason for gap).

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*Excluded per §6 -- informational only.*

| §1 IN-SCOPE Surface | Covered By | Status |
|--------------------|-----------|--------|
| [SURFACE_1] | [ROLE / finding ref] | [COVERED / GAP] |
| [SURFACE_2] | [ROLE / finding ref] | [COVERED / GAP] |

GAP surfaces -> ACTION ITEM REGISTER as ADVISORY-GAP.

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Incompatible CH-ID responses or findings across roles. "None detected." if clean.]

**Convergence**: [CH-ID or concern named by 2+ reviewers -- highest-confidence signal.]

**g_null progression** *(per §9)*:
- g_null(initial): [copy from BRACKET OPENING]
- g_null(post-domain): [copy from §3.5]
- g_null(final): [copy from BRACKET CLOSING]
- Progression: [one sentence describing trajectory]

**Scope coverage**: ["None -- full coverage." or list uncovered surfaces.]

---

## DISPOSITION

**Gate vector**:
- GOpen        = [copy]
- G_domain_agg = [copy]
- G_lifecycle  = [copy]
- GClose       = [copy]

**Apply §2 DISPOSITION ALGEBRA**:
```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Primary Driver** *(apply §16 rules in order)*:
[Rule N -- Primary Driver = [gate name] -- [one-sentence derivation from gate vector]]

**Conditions** *(if CONDITIONAL)*:
1. [From first CONDITIONAL gate. Order: GOpen -> G_domain -> G_lifecycle -> GClose.]

**Blocker** *(if BLOCKED)*: [From FAIL gate. If GClose = FAIL: lead with "Challenger final verdict HOLDS."]

---

## ACTION ITEM REGISTER

*Sources: CH-ID PARTIAL/HOLDS (BRACKET CLOSING) + ADVISORY-OPEN-LENS (§15) +
ADVISORY-GAP (§9.5, §5.5) + ADVISORY-OBS (non-CH-ID observations).
Assembly verbatim per §5. Class from §3 -- do not reassign.*

| CH-ID | Gate | Gate Verdict | Item Description | Class | Owner Role | Resolution Criterion |
|-------|------|-------------|-----------------|-------|------------|---------------------|
| CH-001 | [gate] | [P/C/F] | [description] | [class] | [ROLE] | [criterion] |
| -- | §15 (ADVISORY-OPEN-LENS) | -- | [OPEN lens with HIGH applicability] | ADVISORY | [ROLE] | [criterion] |
| -- | §9.5 (ADVISORY-GAP) | -- | [Domain with no HIGH-applicability reviewer: name domain + reason] | ADVISORY | [ROLE] | [criterion] |
| -- | §5.5 (ADVISORY-GAP) | -- | [Surface with no covering finding] | ADVISORY | [ROLE] | [criterion] |

---

**Artifact to review:**

{{artifact_id}}
