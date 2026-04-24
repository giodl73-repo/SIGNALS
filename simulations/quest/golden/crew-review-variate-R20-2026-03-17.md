---
skill: quest-variate
skill_target: org-review
date: 2026-03-17
round: 20
rubric: org-review-rubric-v11-2026-03-16.md
---

# org-review -- Variate R20 (rubric v11)

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis and three-axis combinations (V-04, V-05).

**R20 design target**: R19-v11 generated five variants all predicted at 225/225
via three structural paths: (a) LENS APPLICABILITY PRE-REGISTRATION as a mandatory
step before reviewers run, (b) DOMAIN COVERAGE GAP-CHECK as an independent numbered
section in the ORDER CONTRACT, (c) declarative type definitions with PRIMACY DEVIATION
CASE for table-over-prose precedence. R20 investigates whether 225/225 robustness
holds under three adversarial failure modes not probed in R19: (a) silent Applicability
re-derivation at LENS COVERAGE TABLE time despite pre-registration ("inherits" in
description but actually recalculates), (b) domain list drift in the gap-check from
scope-declaration domains to reviewer-finding-derived domains, (c) back-filling of NH
dimension values after prose testimony is written (table format satisfied but dimension
scores chosen to match prose intent). All five predicted at 225/225; the question is
which structural path most robustly closes each failure mode under adversarial model
behavior.

**R20 gap analysis (from R19-v11 predicted vs potential failure modes):**

| Criterion | R19 approach | Potential failure mode | R20 remediation |
|-----------|-------------|----------------------|----------------|
| C-33 LENS APPLICABILITY | PRE-REGISTRATION step 2 + TYPED FIELD | Model populates LENS COVERAGE TABLE at step 11, re-derives Applicability from current artifact context, and calls it "consistent with" pre-registration; no verbatim-copy prohibition analogous to C-20 | APPLICABILITY INHERITANCE PROTOCOL: LENS COVERAGE TABLE Applicability column is verbatim-copy from PRE-REGISTRATION; deviations require INHERITANCE-DEVIATION-ALERT; no silent recalculation |
| C-34 ADVISORY-GAP DOMAIN COVERAGE | Gap-check as numbered step + MANDATORY OPERATION | Model enumerates domains from reviewer findings rather than from SCOPE DECLARATION's IN-SCOPE list; domains encountered mid-review replace the declared domain set | Annotate IN-SCOPE surfaces with domain tags at SCOPE DECLARATION time; gap-check reads from this annotated list as its sole input; post-review domain inference prohibited |
| C-35 NH CHALLENGER DIMENSION TABLE | PRIMACY DEVIATION CASE + table governs g_null | Challenger writes prose testimony first, then constructs dimension table whose scores happen to produce the same g_null; table format present but back-filled to confirm prose intent | Two-phase construction: Phase 1 registers dimension names and measurement basis before any scores; Phase 2 assigns values; Phase 1 immutable at Phase 2 time |

**R20 variation axes:**

- V-01: C-33 Verbatim Inheritance Lock (single axis) -- APPLICABILITY INHERITANCE
  PROTOCOL added as preamble section; LENS COVERAGE TABLE Applicability column is
  a verbatim-copy operation from LENS APPLICABILITY PRE-REGISTRATION; deviations
  require INHERITANCE-DEVIATION-ALERT with justification; no silent recalculation.
  Analogous to §7 VERBATIM ASSEMBLY PROHIBITION (C-20) but applied to the applicability
  chain rather than the gate ledger chain.
  C-34 via numbered step 11. C-35 via PRIMACY DEVIATION CASE.
  Predicted: 225/225.

- V-02: C-34 Scope-Declaration Domain Anchor (single axis) -- SCOPE DECLARATION
  (step 1) annotates every IN-SCOPE surface with a domain tag at declaration time;
  DOMAIN COVERAGE GAP-CHECK reads the domain list from the annotated step-1 table
  as its sole input; does not infer domains from reviewer findings; domain set is
  committed at step 1 and read-only for gap-check purposes.
  C-33 via PRE-REGISTRATION. C-35 via PRIMACY DEVIATION CASE.
  Predicted: 225/225.

- V-03: C-35 Two-Phase NH Table Construction (single axis) -- NH DIMENSION COMPARISON
  TABLE uses a mandatory two-phase construction protocol; Phase 1 (DIMENSION
  REGISTRATION) commits dimension names and measurement basis before any values are
  assigned; Phase 2 (VALUE ASSIGNMENT) fills scores and computes deltas; Phase 1 is
  immutable once Phase 2 begins; prevents back-filling scores to match prose intent;
  prose testimony follows Phase 2 and cannot change either phase.
  C-33 via PRE-REGISTRATION. C-34 via numbered step 11.
  Predicted: 225/225.

- V-04: C-33 Inheritance Lock + C-34 Domain Anchor (two-axis) -- V-01's APPLICABILITY
  INHERITANCE PROTOCOL combined with V-02's scope-declaration domain annotation; both
  C-33 and C-34 enforced via chain-of-custody protocols (verbatim copy for C-33,
  anchored source list for C-34). C-35 via PRIMACY DEVIATION CASE.
  Predicted: 225/225.

- V-05: C-33 + C-34 + C-35 (three-axis) -- all three: APPLICABILITY INHERITANCE
  PROTOCOL (V-01), scope-declaration domain annotation (V-02), and two-phase table
  construction (V-03); maximum chain-of-custody and back-fill prevention for all
  three new criteria simultaneously.
  Predicted: 225/225.

---

## V-01

**Axis**: C-33 Verbatim Inheritance Lock -- APPLICABILITY INHERITANCE PROTOCOL added
as preamble section; LENS COVERAGE TABLE Applicability column is a verbatim-copy
operation from LENS APPLICABILITY PRE-REGISTRATION; deviations require explicit
INHERITANCE-DEVIATION-ALERT; no silent recalculation permitted

**Hypothesis**: R19's C-33 enforcement pre-commits Applicability ratings at step 2
(LENS APPLICABILITY PRE-REGISTRATION) before any reviewer runs, and §9 IMMUTABLE
declares these values authoritative for downstream steps. However, no R19 variant
includes a verbatim-copy prohibition analogous to §7 (C-20) for gate ledger rows.
At step 11 (LENS COVERAGE TABLE), the model can recalculate Applicability from its
current artifact understanding and frame the result as "consistent with pre-registration"
without triggering a stated protocol violation. The inheritance lock axis closes this
gap: LENS COVERAGE TABLE Applicability is governed by the same chain-of-custody
principle as the gate ledger (verbatim copy; explicit prohibition on re-derivation;
deviation requires a named alert). C-34 via numbered step 11. C-35 via PRIMACY
DEVIATION CASE. Predicted: 225/225 with C-33 chain of custody fully closed.

---

You are running `/org-review`.

Inputs:
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .roles/]
```

Acknowledge injected values before executing any section.

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
```
HIGH = blocks commitment | MEDIUM = conditions commitment | LOW = advisory
Any gate FAIL -> DISPOSITION: BLOCKED
>= 1 CONDITIONAL, no FAIL -> DISPOSITION: CONDITIONAL
All PASS -> DISPOSITION: READY
```
BLOCKED may not be overridden except at BRACKET CLOSING via labeled field
OVERRIDE INVOKED: YES | NO with named justification.

---

**§2 CLASS DERIVATION CONTRACT (C-12)**
```
Gate verdict FAIL        -> Action item class: BLOCKED
Gate verdict CONDITIONAL -> Action item class: CONDITIONAL
Gate verdict PASS        -> Action item class: ADVISORY (omit if no advisory intent)
```
No editorial class assignment at action register assembly time.

---

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23, C-35)**

The challenger's null hypothesis evaluation MUST produce a structured NH DIMENSION
COMPARISON TABLE. Three alternatives required: A (Status Quo), B (Proposed Build),
C (Best-Non-Build-Alt). Required format at BRACKET OPENING:
```
| Dimension | A: Status Quo | B: Proposed Build | C: Best Non-Build Alt | Delta B-A | Delta B-C |
```
Minimum 3 dimensions, consistent scale. g_null derivable from table alone:
```
g_null = PASS        if delta_B_A > 0 AND delta_B_C > 0
g_null = CONDITIONAL if exactly one delta > 0
g_null = FAIL        if delta_B_A <= 0 AND delta_B_C <= 0
```
Prose-only evaluation is invalid as a substitute. The table is the authoritative
source for g_null. The challenger may add prose after the table. BRACKET CLOSING
re-populates columns B and C with revised values; g_null(final) derives from the
revised table per the same formula.

**PRIMACY DEVIATION CASE (C-35)**: If prose testimony asserts a g_null verdict that
differs from the formula applied to the table values, the table formula governs.
Flag: `NH-NARRATIVE-TABLE-MISMATCH: prose asserts [X]; table formula derives [Y];
table governs.` Binding at BRACKET OPENING and BRACKET CLOSING.

---

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
```
Stage 1: g_null(initial)     [BRACKET OPENING -- from NH Dimension Comparison Table]
Stage 2: g_null(post-domain) [CH-ID SATURATION CHECK -- formula over G_domain_agg]
         G_domain_agg = FAIL:        g_null(post-domain) = g_null(initial) [challenger holds]
         G_domain_agg = PASS:        g_null(post-domain) weakens one tier toward PASS
         G_domain_agg = CONDITIONAL: g_null(post-domain) = CONDITIONAL
Stage 3: g_null(final)       [BRACKET CLOSING -- same logic substituting G_lifecycle]
```
GClose verdict MUST equal g_null(final), or OVERRIDE INVOKED: YES with justification.

---

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21, C-25)**

Universal coverage: BRACKET OPENING, every DOMAIN section, LIFECYCLE section, and
BRACKET CLOSING each emit exactly one LOCAL GATE LEDGER ROW at verdict time:
```
| Gate Verdict | Section Severity | Class | Finding References |
```
Non-verdict sections emit no row (see §7). MASTER ACTION REGISTER assembled by
verbatim copy of all LOCAL GATE LEDGER ROWS.

---

**§6 VERBATIM ASSEMBLY PROHIBITION (C-20)**

MASTER ACTION REGISTER assembly: copy all LOCAL GATE LEDGER ROWS verbatim. Do not
re-derive Gate Verdict or Class. The local row is the point of authority.

---

**§7 NON-VERDICT SECTION EXCLUSION (C-25)**

These sections emit NO gate ledger row:
- SCOPE DECLARATION
- LENS APPLICABILITY PRE-REGISTRATION
- CH-ID REGISTRATION TABLE
- CH-ID SATURATION CHECK (emits g_null(post-domain) as labeled field, not a gate row)
- SCOPE COVERAGE RECONCILIATION
- LENS COVERAGE TABLE
- DOMAIN COVERAGE GAP-CHECK

---

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
1.  SCOPE DECLARATION
2.  LENS APPLICABILITY PRE-REGISTRATION
3.  CH-ID REGISTRATION TABLE
4.  BRACKET OPENING (challenger / inertia-advocate)
5.  DOMAIN REVIEWER SECTIONS (one per role, manifest order)
6.  CH-ID SATURATION CHECK
7.  LIFECYCLE REVIEWER SECTION
8.  BRACKET CLOSING (challenger, post-domain)
9.  SCOPE COVERAGE RECONCILIATION
10. LENS COVERAGE TABLE
11. DOMAIN COVERAGE GAP-CHECK
12. DISPOSITION + PRIMARY DRIVER
13. MASTER ACTION REGISTER
14. CROSS-ROLE SIGNALS
```
Reordering any numbered step is a contract violation. LENS APPLICABILITY
PRE-REGISTRATION (step 2) must complete before CH-ID REGISTRATION (step 3) and
BRACKET OPENING (step 4). LIFECYCLE (step 7) must precede BRACKET CLOSING (step 8).
DOMAIN COVERAGE GAP-CHECK (step 11) is a required independent section; executing
step 10 without step 11 is a section-order violation.

---

**§9 LENS APPLICABILITY PRE-REGISTRATION PROTOCOL (C-33)** [IMMUTABLE]

Before any reviewer section, emit the LENS APPLICABILITY PRE-REGISTRATION TABLE:
```
| Reviewer Role | Lens Dimension | Pre-Committed Applicability |
```
- `Pre-Committed Applicability`: HIGH, MEDIUM, or LOW. Artifact-specific, not role-generic.
  HIGH = directly relevant to this artifact's domain and scope.
  MEDIUM = relevant but not central to this artifact's primary risk surface.
  LOW = tangential or minimally applicable.
  Immutable after pre-registration. This table is the applicability authority for all
  downstream steps.

Omitting any active reviewer's lens dimension from this table before that reviewer's
section runs is a protocol violation.

---

**§10 APPLICABILITY INHERITANCE PROTOCOL (C-33)** [IMMUTABLE]

The PRE-REGISTRATION TABLE (step 2, §9) is the Applicability authority. When
populating the LENS COVERAGE TABLE (step 10), the Applicability column MUST be
populated by verbatim-copy from PRE-REGISTRATION -- not re-derived from artifact
context at table-population time.

**Inheritance rule**: for each (Reviewer Role, Lens Dimension) pair, the Applicability
value in the LENS COVERAGE TABLE must equal the Pre-Committed Applicability from step 2.

**Inheritance deviation case**: if the model determines at step 10 that the pre-registered
value appears incorrect for this artifact, it must emit:
```
INHERITANCE-DEVIATION-ALERT: Role=[role] / Dimension=[dimension] /
  Pre-Registered=[X] / Attempted=[Y] / Justification=[rationale]
```
The INHERITANCE-DEVIATION-ALERT does not auto-approve a change. The pre-registered
value governs unless BRACKET CLOSING explicitly invokes OVERRIDE INVOKED: YES with
named justification. The alert is flagged in CROSS-ROLE SIGNALS as an ADVISORY item.
Silent recalculation (changing the value without emitting the alert) is a chain-of-
custody error equivalent to re-deriving a gate verdict at action register assembly time.

---

**§11 CH-ID CHALLENGE REGISTRATION (C-04, C-05)**

Before BRACKET OPENING, register all challenges:
```
| CH-ID | Challenge Statement | Bracket Opening | [Domain roles...] | Lifecycle | Bracket Closing |
```
Populate CH-ID and Challenge Statement at registration time. Response columns populated
during execution. Every reviewer section carries a CH-ID response table.

---

**§12 CH-ID SATURATION REQUIREMENT (C-27)**
```
SATURATED:       every CH-ID has >= 1 DOMAIN section response (verified before LIFECYCLE)
FULLY SATURATED: every CH-ID has domain + lifecycle responses (verified at BRACKET CLOSING)
```
BRACKET CLOSING may not emit PASS when any CH-ID is UNSATURATED without explicit
waiver and stated justification.

---

**§13 LIFECYCLE VERDICT INTEGRATION CONTRACT (C-22)**

LIFECYCLE section (step 7) executes before BRACKET CLOSING (step 8). BRACKET CLOSING
receives g_lifecycle as a labeled input:
`Lifecycle verdict received: g_lifecycle = [FAIL/CONDITIONAL/PASS]`
and factors it into g_null(final) derivation per §4 Stage 3.

---

**§14 DOMAIN-AGGREGATE FORMULA (C-24)**
```
G_domain_agg = median(all DOMAIN reviewer gate verdicts)
median order: FAIL < CONDITIONAL < PASS
```
Labeled input to BRACKET CLOSING for §4 Stage 2 application.

---

**§15 ROLE LENS EXHAUSTION PROTOCOL (C-31, C-34)** [IMMUTABLE]

LENS COVERAGE TABLE (step 10): for each active reviewer role, every `lens.verify`
entry appears in the table. Schema:
```
| Reviewer Role | Lens Dimension | Applicability | Status | Finding Reference(s) |
```
Applicability: inherited from LENS APPLICABILITY PRE-REGISTRATION (step 2) per
APPLICABILITY INHERITANCE PROTOCOL (§10). Status = ADDRESSED (>= 1 finding cites
this dimension) or OPEN. HIGH-applicability + OPEN -> ADVISORY-OPEN-LENS item in
MASTER ACTION REGISTER.

**DOMAIN COVERAGE GAP-CHECK (step 11, mandatory)**: after the LENS COVERAGE TABLE,
enumerate every artifact domain from the SCOPE DECLARATION. For each domain, check
whether any reviewer has HIGH Applicability for a lens dimension covering that domain.
Domains with no HIGH-applicability coverage: classify as ADVISORY-GAP; append to
MASTER ACTION REGISTER (domain name + reason + recommended mitigation).
Emit: `DOMAIN COVERAGE GAP-CHECK: [N domains covered at HIGH | N domains ADVISORY-GAP]`

---

**§16 SCOPE COVERAGE GATE PROTOCOL (C-29)**

After BRACKET CLOSING (step 8): SCOPE COVERAGE RECONCILIATION (step 9) maps every
IN-SCOPE surface to findings. Surfaces with no finding: ADVISORY-GAP, LOW severity,
appended to MASTER ACTION REGISTER. No gate ledger row (§7).

---

**§17 PER-FINDING SEVERITY CHAIN (C-30)** [IMMUTABLE]
```
Section Severity = worst(Severity of all individual findings in this section)
worst order: HIGH > MEDIUM > LOW
```
Every finding row in every reviewer section carries an individual Severity field.
Section Severity in the LOCAL GATE LEDGER ROW derives mechanically from this formula.
No editorial section-level severity assignment.

---

**§18 PRIMARY DRIVER DERIVATION (C-32)** [IMMUTABLE]

After all gate verdicts, emit Primary Driver by first-match precedence:
```
Rule 1: BRACKET CLOSING OVERRIDE INVOKED: YES      -> Primary Driver: BRACKET CLOSING OVERRIDE
Rule 2: BRACKET OPENING gate = FAIL                -> Primary Driver: NULL HYPOTHESIS
Rule 3: Any DOMAIN gate = FAIL (first in manifest)  -> Primary Driver: DOMAIN [role name]
Rule 4: LIFECYCLE gate = FAIL                       -> Primary Driver: LIFECYCLE
Rule 5: Any DOMAIN gate = CONDITIONAL (first)       -> Primary Driver: DOMAIN [role name]
Rule 6: LIFECYCLE gate = CONDITIONAL                -> Primary Driver: LIFECYCLE
Rule 7: All gates = PASS                            -> Primary Driver: CONSENSUS
```
Emit as labeled field `Primary Driver: [value]` at DISPOSITION.

---

**§19 INPUT VARIABLE CONTRACTS (C-08, C-13, C-15)**

Template variables: `{{artifact_id}}`, `{{depth}}`, `{{reviewer_set}}`.
- `deep`: all roles from .roles/ invoked.
- `standard`: roles relevant to artifact type; selection rationale stated.
- `quick`: >= 3 highest-priority roles; abbreviation note included.
- `{{reviewer_set}}` overrides depth-based selection when non-auto.
Output must include an explicit acknowledgment block emitting all three values.

---

### EXECUTION

**Step 1: Acknowledge inputs**
```
Artifact: {{artifact_id}}
Depth: {{depth}}
Reviewer set: {{reviewer_set}}
Role selection rationale: [state if depth=standard or reviewer_set non-auto]
```

**Step 2: SCOPE DECLARATION**
Enumerate all surfaces under review (artifact sections, surfaces, prior decisions).
Explicitly state OUT-OF-SCOPE surfaces. Any surface discovered mid-review that was
not declared is a scope gap -- flag it; do not silently incorporate.

**Step 3: LENS APPLICABILITY PRE-REGISTRATION** (per §9)
For every active reviewer role, pre-commit all lens dimension Applicability ratings.
Emit the PRE-REGISTRATION TABLE before CH-ID REGISTRATION. No reviewer section may
run until this table is complete. These pre-committed values are the applicability
authority for all downstream steps per §10.

**Step 4: CH-ID REGISTRATION TABLE** (per §11)

**Step 5: BRACKET OPENING (challenger / inertia-advocate)**
- State the null hypothesis: what the team does today instead of building this, and
  why that is acceptable.
- Populate NH DIMENSION COMPARISON TABLE per §3: >= 3 dimensions, consistent scale,
  three alternatives, compute Delta B-A and Delta B-C per dimension.
- Emit g_null(initial) as a labeled field derived from the table. Apply PRIMACY
  DEVIATION CASE if prose and table diverge.
- Emit OVERRIDE INVOKED: NO (default).
- CH-ID responses.
- LOCAL GATE LEDGER ROW per §5.

**Step 6: DOMAIN REVIEWER SECTIONS** (one per role, manifest order)
- "As a [role], I evaluate [lens concern]."
- Finding rows: `| Severity | Surface | Finding | Recommendation |`
- CH-ID responses.
- LOCAL GATE LEDGER ROW per §5. Section Severity = worst(finding severities) per §17.

**Step 7: CH-ID SATURATION CHECK**
- Verify SATURATED tier.
- Emit g_null(post-domain) per §4 Stage 2 formula.
- No gate ledger row.

**Step 8: LIFECYCLE REVIEWER SECTION**
- Lifecycle lens over operational phases (creation, active use, change, deprecation, removal).
- Finding rows (same format).
- CH-ID responses.
- LOCAL GATE LEDGER ROW per §5 with g_lifecycle labeled.

**Step 9: BRACKET CLOSING (challenger, post-domain)**
- Receive G_domain_agg (per §14) and g_lifecycle as labeled inputs.
- Re-populate NH table columns B and C with revised values.
- Derive g_null(final) per §3 formula (§4 Stage 3).
- Emit OVERRIDE INVOKED: YES | NO as labeled field.
- LOCAL GATE LEDGER ROW per §5.

**Step 10: SCOPE COVERAGE RECONCILIATION** (per §16; no gate ledger row)

**Step 11: LENS COVERAGE TABLE** (per §15; no gate ledger row)
Populate Applicability by verbatim-copy from LENS APPLICABILITY PRE-REGISTRATION
(step 3) per §10. Emit INHERITANCE-DEVIATION-ALERT for any deviation.

**Step 12: DOMAIN COVERAGE GAP-CHECK** (per §15; no gate ledger row)
Enumerate artifact domains from SCOPE DECLARATION; check HIGH coverage per domain.

**Step 13: DISPOSITION**
- Apply §1 DISPOSITION ALGEBRA.
- Emit `DISPOSITION: READY | CONDITIONAL | BLOCKED`.
- Emit `Primary Driver: [value]` per §18.

**Step 14: MASTER ACTION REGISTER**
Copy LOCAL GATE LEDGER ROWS verbatim (§6). Append ADVISORY-OPEN-LENS, ADVISORY-GAP
items from steps 11, 12, 10. Do not re-derive Gate Verdict or Class.

**Step 15: CROSS-ROLE SIGNALS**
Integration narrative. >= 1 cross-role conflict or convergence. g_null progression
all three stages. Disposition explanation. Flag any INHERITANCE-DEVIATION-ALERTs
from step 11 as ADVISORY items.

---

## V-02

**Axis**: C-34 Scope-Declaration Domain Anchor -- SCOPE DECLARATION (step 1) annotates
every IN-SCOPE surface with a domain tag at declaration time; DOMAIN COVERAGE GAP-CHECK
reads its domain input set from this annotated table; post-review domain inference
prohibited as the source for gap-check enumeration

**Hypothesis**: R19's C-34 enforcement requires the DOMAIN COVERAGE GAP-CHECK to
enumerate "every artifact domain from the SCOPE DECLARATION" and check coverage. In
practice, the model determines what "domains" are at gap-check time, after it has
completed the full review. It may derive domains from the reviewer findings it has
just generated rather than from the scope declaration -- an implicit narrowing to
only domains that appeared in review. The domain anchor axis closes this gap by
requiring domain annotations at SCOPE DECLARATION time. The domain set is committed
when the scope is declared and is read-only for gap-check purposes. The gap-check
has a pre-committed, fixed input set that cannot drift during or after review.
C-33 via PRE-REGISTRATION. C-35 via PRIMACY DEVIATION CASE. Predicted: 225/225
with C-34 domain enumeration anchored to declared scope.

---

You are running `/org-review`.

Inputs:
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .roles/]
```

Acknowledge injected values before executing any section.

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
```
HIGH = blocks commitment | MEDIUM = conditions commitment | LOW = advisory
FAIL -> BLOCKED | >= 1 CONDITIONAL + no FAIL -> CONDITIONAL | All PASS -> READY
```
OVERRIDE: BRACKET CLOSING only, OVERRIDE INVOKED: YES | NO + justification.

---

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY.
No editorial class assignment at assembly time.

---

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23, C-35)**

NH DIMENSION COMPARISON TABLE required at BRACKET OPENING. Three alternatives:
A (Status Quo), B (Proposed Build), C (Best-Non-Build-Alt). Format:
```
| Dimension | A: Status Quo | B: Proposed Build | C: Best Non-Build Alt | Delta B-A | Delta B-C |
```
Minimum 3 dimensions, consistent scale. g_null derivable from table alone:
```
g_null = PASS if both deltas > 0 | CONDITIONAL if one delta > 0 | FAIL if both <= 0
```
Prose evaluation is invalid as a substitute. Table governs g_null. BRACKET CLOSING
re-populates columns B/C; g_null(final) from revised table.

**PRIMACY DEVIATION CASE (C-35)**: prose asserting a different g_null than the table
formula -> flag `NH-NARRATIVE-TABLE-MISMATCH: prose=[X]; table=[Y]; table governs.`
Binding at BRACKET OPENING and BRACKET CLOSING.

---

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
```
Stage 1: g_null(initial)     [BRACKET OPENING]
Stage 2: g_null(post-domain) [CH-ID SATURATION CHECK, G_domain_agg formula]
         FAIL: holds | PASS: weakens one tier | CONDITIONAL: CONDITIONAL
Stage 3: g_null(final)       [BRACKET CLOSING, G_lifecycle formula]
```
GClose = g_null(final) or OVERRIDE INVOKED: YES.

---

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21, C-25)**
Universal: BRACKET OPENING, DOMAIN sections, LIFECYCLE, BRACKET CLOSING emit one row:
```
| Gate Verdict | Section Severity | Class | Finding References |
```
Non-verdict sections: no row (see §7). MASTER ACTION REGISTER: verbatim copy.

---

**§6 VERBATIM ASSEMBLY PROHIBITION (C-20)**
Verbatim copy only. Re-derivation prohibited. Local row is authority.

---

**§7 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate row: SCOPE DECLARATION, LENS APPLICABILITY PRE-REGISTRATION, CH-ID
REGISTRATION TABLE, CH-ID SATURATION CHECK, SCOPE COVERAGE RECONCILIATION,
LENS COVERAGE TABLE, DOMAIN COVERAGE GAP-CHECK.

---

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
1.  SCOPE DECLARATION                  [domain tags annotated here -- §9]
2.  LENS APPLICABILITY PRE-REGISTRATION
3.  CH-ID REGISTRATION TABLE
4.  BRACKET OPENING
5.  DOMAIN REVIEWER SECTIONS (manifest order)
6.  CH-ID SATURATION CHECK
7.  LIFECYCLE REVIEWER SECTION
8.  BRACKET CLOSING
9.  SCOPE COVERAGE RECONCILIATION
10. LENS COVERAGE TABLE
11. DOMAIN COVERAGE GAP-CHECK          [domain input from step 1 scope table -- §9]
12. DISPOSITION + PRIMARY DRIVER
13. MASTER ACTION REGISTER
14. CROSS-ROLE SIGNALS
```
Step 2 completes before step 4. Step 7 precedes step 8. Step 11 is a required
independent section; executing step 10 without step 11 is a section-order violation.

---

**§9 SCOPE-DECLARATION DOMAIN ANNOTATION PROTOCOL (C-34)** [IMMUTABLE]

At SCOPE DECLARATION (step 1), annotate every IN-SCOPE surface with a domain tag.
Extended scope table schema:
```
| Surface | Domain | In/Out of Scope | Note |
```
- `Surface`: the artifact section, API, subsystem, or decision surface under review.
- `Domain`: the functional or technical domain this surface belongs to (e.g., security,
  data-model, UX, API-contract, operations, compliance). Assign the domain most relevant
  to this review's risk surface. Each surface carries one primary domain.
- Domain list is committed at step 1. No new domains may be added at gap-check time.

**DOMAIN COVERAGE GAP-CHECK source rule (C-34)**: step 11 iterates the unique Domain
values from the step 1 scope table as its sole input set. It does not derive domains
from reviewer findings or from LENS COVERAGE TABLE content. Domains appearing in
reviewer findings but not in the step 1 table: flag as UNDECLARED-DOMAIN in CROSS-ROLE
SIGNALS; do not add to the gap-check input set.

---

**§10 LENS APPLICABILITY PRE-REGISTRATION PROTOCOL (C-33)** [IMMUTABLE]

Before any reviewer section, emit:
```
| Reviewer Role | Lens Dimension | Pre-Committed Applicability |
```
Applicability (HIGH/MEDIUM/LOW): artifact-specific, not role-generic. Immutable after
pre-registration. LENS COVERAGE TABLE (step 10) inherits these values. HIGH-applicability
entries govern ADVISORY-OPEN-LENS promotion at step 10.

---

**§11 CH-ID CHALLENGE REGISTRATION (C-04, C-05)**
```
| CH-ID | Challenge Statement | Bracket Opening | [Domain roles...] | Lifecycle | Bracket Closing |
```
Every reviewer section carries a CH-ID response table.

---

**§12 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED: every CH-ID >= 1 DOMAIN response. FULLY SATURATED: + LIFECYCLE.
BRACKET CLOSING PASS blocked when UNSATURATED without waiver.

---

**§13 LIFECYCLE VERDICT INTEGRATION CONTRACT (C-22)**
LIFECYCLE precedes BRACKET CLOSING. Input: `Lifecycle verdict received: g_lifecycle = [value]`.

---

**§14 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(DOMAIN gate verdicts). FAIL < CONDITIONAL < PASS.
Labeled input to BRACKET CLOSING.

---

**§15 ROLE LENS EXHAUSTION PROTOCOL (C-31)** [IMMUTABLE]

LENS COVERAGE TABLE (step 10):
```
| Reviewer Role | Lens Dimension | Applicability | Status | Finding Reference(s) |
```
Applicability: inherited from PRE-REGISTRATION (step 2, §10). HIGH + OPEN ->
ADVISORY-OPEN-LENS in MASTER ACTION REGISTER.

**DOMAIN COVERAGE GAP-CHECK (step 11, mandatory)**: iterate unique Domain values from
the step 1 annotated scope table (§9). For each domain, check whether any reviewer has
HIGH Applicability for a lens dimension covering that domain. Do not derive additional
domains from findings. ADVISORY-GAP for uncovered domains; append to MASTER ACTION REGISTER.
Emit: `DOMAIN COVERAGE GAP-CHECK: [N domains covered at HIGH | N domains ADVISORY-GAP]`

---

**§16 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-BRACKET CLOSING: SCOPE COVERAGE RECONCILIATION maps IN-SCOPE surfaces to findings.
GAP -> ADVISORY-GAP, LOW, appended. No gate row.

---

**§17 PER-FINDING SEVERITY CHAIN (C-30)** [IMMUTABLE]
Section Severity = worst(individual severities). HIGH > MEDIUM > LOW. Per-row Severity
on every finding. No editorial section-level assignment.

---

**§18 PRIMARY DRIVER DERIVATION (C-32)** [IMMUTABLE]
First-match: BRACKET CLOSING OVERRIDE > NULL HYPOTHESIS > DOMAIN FAIL (first) >
LIFECYCLE FAIL > DOMAIN CONDITIONAL (first) > LIFECYCLE CONDITIONAL > CONSENSUS.
`Primary Driver: [value]` at DISPOSITION.

---

**§19 INPUT VARIABLE CONTRACTS (C-08, C-13, C-15)**
Variables: `{{artifact_id}}`, `{{depth}}`, `{{reviewer_set}}`. Acknowledgment block required.

---

### EXECUTION

**Step 1: Acknowledge inputs**

**Step 2: SCOPE DECLARATION** (per §9)
Emit the annotated scope table with domain tags for every IN-SCOPE surface:
`| Surface | Domain | In/Out of Scope | Note |`
Domain list is committed here and read-only for gap-check purposes. OUT-OF-SCOPE
surfaces enumerated. Mid-review discoveries: flag as scope gap.

**Step 3: LENS APPLICABILITY PRE-REGISTRATION** (per §10)
Pre-commit all lens dimension Applicability ratings before CH-ID registration.

**Step 4: CH-ID REGISTRATION TABLE** (per §11)

**Step 5: BRACKET OPENING** -- NH DIMENSION COMPARISON TABLE per §3; g_null(initial)
from table; PRIMACY DEVIATION CASE if applicable; OVERRIDE INVOKED: NO; CH-ID
responses; LOCAL GATE LEDGER ROW.

**Step 6: DOMAIN REVIEWER SECTIONS** -- `| Severity | Surface | Finding | Recommendation |`;
CH-ID responses; LOCAL GATE LEDGER ROW; Section Severity per §17.

**Step 7: CH-ID SATURATION CHECK** -- verify SATURATED; g_null(post-domain) per §4.

**Step 8: LIFECYCLE REVIEWER SECTION** -- lifecycle lens; findings; CH-ID responses;
LOCAL GATE LEDGER ROW with g_lifecycle.

**Step 9: BRACKET CLOSING** -- G_domain_agg and g_lifecycle as labeled inputs; revised
NH table columns B/C; g_null(final); OVERRIDE INVOKED; LOCAL GATE LEDGER ROW.

**Step 10: SCOPE COVERAGE RECONCILIATION** (§16; no gate row)

**Step 11: LENS COVERAGE TABLE** (§15; no gate row) -- inherit Applicability from step 3.

**Step 12: DOMAIN COVERAGE GAP-CHECK** (§15; no gate row) -- iterate unique Domain
values from step 2 scope table; no post-review domain inference.

**Step 13: DISPOSITION** -- §1 algebra; DISPOSITION; Primary Driver per §18.

**Step 14: MASTER ACTION REGISTER** -- verbatim copy (§6); append advisory items; no re-derivation.

**Step 15: CROSS-ROLE SIGNALS** -- integration narrative; cross-role conflict/convergence;
g_null progression; disposition explanation; flag UNDECLARED-DOMAIN discoveries.

---

## V-03

**Axis**: C-35 Two-Phase NH Table Construction -- NH DIMENSION COMPARISON TABLE uses
a mandatory two-phase construction protocol; Phase 1 (DIMENSION REGISTRATION) commits
dimension names and measurement basis before any scores are assigned; Phase 2 (VALUE
ASSIGNMENT) fills scores and computes deltas; Phase 1 is immutable once Phase 2 begins

**Hypothesis**: R19's C-35 enforcement relies on the PRIMACY DEVIATION CASE: if prose
and table values diverge, the table governs. This closes the override path (prose cannot
change the committed g_null verdict). However, a subtler failure mode survives: the
challenger develops prose testimony first, forms an intuition about g_null, then constructs
a dimension table whose scores happen to produce that same g_null. The table format is
present and technically governs, but it was constructed to confirm prose intent rather
than to evaluate it independently. The two-phase construction axis closes this gap:
dimension names and measurement basis are committed before any values are assigned.
The challenger cannot redefine what is being measured in order to produce a desired score
pattern. Phase 1 is the structural anchor; Phase 2 fills values against that anchor;
prose follows Phase 2 and may annotate but cannot change either phase. C-33 via
PRE-REGISTRATION. C-34 via numbered step 11. Predicted: 225/225 with C-35 construction
integrity enforced at the dimension definition layer.

---

You are running `/org-review`.

Inputs:
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .roles/]
```

Acknowledge injected values before executing any section.

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
```
HIGH = blocks commitment | MEDIUM = conditions commitment | LOW = advisory
FAIL -> BLOCKED | >= 1 CONDITIONAL + no FAIL -> CONDITIONAL | All PASS -> READY
```
OVERRIDE: BRACKET CLOSING only, OVERRIDE INVOKED: YES | NO + justification.

---

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (omit if none).
No editorial class assignment at assembly time.

---

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23, C-35)**

**NH DIMENSION COMPARISON TABLE -- Two-Phase Construction Protocol**:

**Phase 1 -- DIMENSION REGISTRATION** (immutable before Phase 2 begins):
Before assigning any scores, the challenger emits a DIMENSION REGISTRY:
```
| # | Dimension | Measurement Basis | Scale |
```
- `Dimension`: the evaluation axis. Must be specific enough to score without further
  interpretation (e.g., "Integration effort for adopting teams" not "effort").
- `Measurement Basis`: the observable being scored (e.g., "estimated developer-days",
  "percentage of users completing task without help in < 2 minutes").
- `Scale`: the scoring range (e.g., "1=worst outcome, 10=best outcome"). Consistent
  across all dimensions and all three alternatives. Declared once in Phase 1.
- Minimum 3 rows. Phase 1 complete when all dimensions are named with measurement basis
  and scale. No dimensions may be added, removed, or renamed in Phase 2.

**Phase 2 -- VALUE ASSIGNMENT** (immediately follows Phase 1):
Using the Phase 1 dimensions and scale, assign scores for all three alternatives:
```
| Dimension | A: Status Quo | B: Proposed Build | C: Best Non-Build Alt | Delta B-A | Delta B-C |
```
Deltas: B minus A and B minus C (sign-significant). g_null derivable from table alone:
```
g_null = PASS        if delta_B_A > 0 AND delta_B_C > 0
g_null = CONDITIONAL if exactly one delta > 0
g_null = FAIL        if delta_B_A <= 0 AND delta_B_C <= 0
```

**Prose testimony** (follows Phase 2): The challenger may add prose elaboration after
Phase 2 completes. Prose may not change Phase 1 dimension definitions or Phase 2 values.

**CONSTRUCTION DEVIATION CASE**: If Phase 2 values reveal a Phase 1 dimension was
poorly specified, emit:
```
NH-CONSTRUCTION-DEVIATION: Dimension=[d] / Phase-1-basis=[original] /
  Issue=[issue] / Proposed-revision=[revision]
```
Phase 1 values govern unless BRACKET CLOSING invokes OVERRIDE INVOKED: YES.
Flag in CROSS-ROLE SIGNALS as ADVISORY item.

**PRIMACY DEVIATION CASE (C-35)**: If prose testimony asserts a g_null verdict that
differs from the Phase 2 formula output, the table formula governs.
Flag: `NH-NARRATIVE-TABLE-MISMATCH: prose=[X]; table=[Y]; table governs.`
Binding at BRACKET OPENING and BRACKET CLOSING.

BRACKET CLOSING re-populates Phase 2 columns B and C with revised values (Phase 1
dimensions immutable). g_null(final) from revised Phase 2 table per formula.

---

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
```
Stage 1: g_null(initial)     [BRACKET OPENING -- from Phase 2 table]
Stage 2: g_null(post-domain) [CH-ID SATURATION CHECK -- G_domain_agg formula]
         FAIL: holds | PASS: weakens one tier | CONDITIONAL: CONDITIONAL
Stage 3: g_null(final)       [BRACKET CLOSING -- same substituting G_lifecycle]
```
GClose = g_null(final) or OVERRIDE INVOKED: YES.

---

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21, C-25)**
Universal: BRACKET OPENING, DOMAIN sections, LIFECYCLE, BRACKET CLOSING emit one row:
```
| Gate Verdict | Section Severity | Class | Finding References |
```
Non-verdict sections: no row (see §7). MASTER ACTION REGISTER: verbatim copy.

---

**§6 VERBATIM ASSEMBLY PROHIBITION (C-20)**
Verbatim copy only. Re-derivation prohibited. Local row is authority.

---

**§7 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate row: SCOPE DECLARATION, LENS APPLICABILITY PRE-REGISTRATION, CH-ID
REGISTRATION TABLE, CH-ID SATURATION CHECK, SCOPE COVERAGE RECONCILIATION,
LENS COVERAGE TABLE, DOMAIN COVERAGE GAP-CHECK.

---

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
1.  SCOPE DECLARATION
2.  LENS APPLICABILITY PRE-REGISTRATION
3.  CH-ID REGISTRATION TABLE
4.  BRACKET OPENING  [Phase 1 DIMENSION REGISTRY then Phase 2 VALUE ASSIGNMENT]
5.  DOMAIN REVIEWER SECTIONS (manifest order)
6.  CH-ID SATURATION CHECK
7.  LIFECYCLE REVIEWER SECTION
8.  BRACKET CLOSING  [re-populate Phase 2 columns B/C; Phase 1 immutable]
9.  SCOPE COVERAGE RECONCILIATION
10. LENS COVERAGE TABLE
11. DOMAIN COVERAGE GAP-CHECK
12. DISPOSITION + PRIMARY DRIVER
13. MASTER ACTION REGISTER
14. CROSS-ROLE SIGNALS
```
Step 2 completes before step 4. Step 7 precedes step 8. Step 11 is a required
independent section.

---

**§9 LENS APPLICABILITY PRE-REGISTRATION PROTOCOL (C-33)** [IMMUTABLE]
Before any reviewer section, emit:
```
| Reviewer Role | Lens Dimension | Pre-Committed Applicability |
```
Applicability (HIGH/MEDIUM/LOW): artifact-specific. Immutable after pre-registration.
LENS COVERAGE TABLE inherits these values. HIGH governs ADVISORY-OPEN-LENS promotion.

---

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-05)**
```
| CH-ID | Challenge Statement | Bracket Opening | [Domain roles...] | Lifecycle | Bracket Closing |
```
Every reviewer section carries a CH-ID response table.

---

**§11 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED: every CH-ID >= 1 DOMAIN response. FULLY SATURATED: + LIFECYCLE.
BRACKET CLOSING PASS blocked when UNSATURATED without waiver.

---

**§12 LIFECYCLE VERDICT INTEGRATION CONTRACT (C-22)**
LIFECYCLE (step 7) precedes BRACKET CLOSING (step 8).
`Lifecycle verdict received: g_lifecycle = [value]` as labeled input.

---

**§13 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(DOMAIN gate verdicts). FAIL < CONDITIONAL < PASS. Labeled input.

---

**§14 ROLE LENS EXHAUSTION PROTOCOL (C-31, C-34)** [IMMUTABLE]

LENS COVERAGE TABLE (step 10):
```
| Reviewer Role | Lens Dimension | Applicability | Status | Finding Reference(s) |
```
Applicability: inherited from PRE-REGISTRATION (step 2, §9). HIGH + OPEN ->
ADVISORY-OPEN-LENS in MASTER ACTION REGISTER.

**DOMAIN COVERAGE GAP-CHECK (step 11, mandatory)**: enumerate artifact domains from
SCOPE DECLARATION; check HIGH Applicability coverage per domain; ADVISORY-GAP for
uncovered; append to MASTER ACTION REGISTER.
Emit: `DOMAIN COVERAGE GAP-CHECK: [N covered at HIGH | N ADVISORY-GAP]`

---

**§15 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-BRACKET CLOSING: SCOPE COVERAGE RECONCILIATION maps IN-SCOPE surfaces to findings.
GAP -> ADVISORY-GAP, LOW, appended. No gate row.

---

**§16 PER-FINDING SEVERITY CHAIN (C-30)** [IMMUTABLE]
Section Severity = worst(individual severities). No editorial assignment.

---

**§17 PRIMARY DRIVER DERIVATION (C-32)** [IMMUTABLE]
First-match: BRACKET CLOSING OVERRIDE > NULL HYPOTHESIS > DOMAIN FAIL (first) >
LIFECYCLE FAIL > DOMAIN CONDITIONAL (first) > LIFECYCLE CONDITIONAL > CONSENSUS.
`Primary Driver: [value]` at DISPOSITION.

---

**§18 INPUT VARIABLE CONTRACTS (C-08, C-13, C-15)**
Variables: `{{artifact_id}}`, `{{depth}}`, `{{reviewer_set}}`. Acknowledgment block required.

---

### EXECUTION

**Step 1**: Acknowledge inputs.

**Step 2: SCOPE DECLARATION** -- enumerate IN-SCOPE and OUT-OF-SCOPE surfaces; mid-review
discoveries flagged as scope gaps.

**Step 3: LENS APPLICABILITY PRE-REGISTRATION** (§9) -- pre-commit all Applicability
ratings before CH-ID registration; these values are the applicability authority.

**Step 4: CH-ID REGISTRATION TABLE** (§10)

**Step 5: BRACKET OPENING** (§3)
- Phase 1 DIMENSION REGISTRATION: emit DIMENSION REGISTRY (>= 3 rows with dimension,
  measurement basis, scale); Phase 1 complete before any scores.
- Phase 2 VALUE ASSIGNMENT: score all three alternatives; compute deltas.
- Emit g_null(initial) from Phase 2 table. Apply PRIMACY DEVIATION CASE if prose and
  table diverge; apply CONSTRUCTION DEVIATION CASE if Phase 1 appears ill-defined.
- OVERRIDE INVOKED: NO. CH-ID responses. LOCAL GATE LEDGER ROW.

**Step 6: DOMAIN REVIEWER SECTIONS** -- `| Severity | Surface | Finding | Recommendation |`;
CH-ID responses; LOCAL GATE LEDGER ROW; Section Severity per §16.

**Step 7: CH-ID SATURATION CHECK** -- verify SATURATED; g_null(post-domain) per §4.

**Step 8: LIFECYCLE REVIEWER SECTION** -- lifecycle lens; findings; CH-ID responses;
LOCAL GATE LEDGER ROW with g_lifecycle.

**Step 9: BRACKET CLOSING** -- G_domain_agg and g_lifecycle as labeled inputs; re-populate
Phase 2 columns B/C (Phase 1 immutable); g_null(final) from revised table; OVERRIDE
INVOKED; LOCAL GATE LEDGER ROW.

**Step 10: SCOPE COVERAGE RECONCILIATION** (§15; no gate row)

**Step 11: LENS COVERAGE TABLE** (§14; no gate row) -- inherit Applicability from step 3.

**Step 12: DOMAIN COVERAGE GAP-CHECK** (§14; no gate row)

**Step 13: DISPOSITION** -- §1 algebra; DISPOSITION; Primary Driver per §17.

**Step 14: MASTER ACTION REGISTER** -- verbatim copy (§6); append advisory items; no re-derivation.

**Step 15: CROSS-ROLE SIGNALS** -- integration narrative; cross-role conflict/convergence;
g_null progression all three stages; disposition explanation; flag NH-CONSTRUCTION-
DEVIATION items from step 5.

---

## V-04

**Axis**: C-33 Verbatim Inheritance Lock + C-34 Scope-Declaration Domain Anchor
(two-axis) -- V-01's APPLICABILITY INHERITANCE PROTOCOL combined with V-02's
scope-declaration domain annotation; both C-33 and C-34 enforced via chain-of-custody
protocols (verbatim copy for C-33; anchored source list for C-34)

**Hypothesis**: V-01 closes the C-33 chain-of-custody gap by prohibiting silent
Applicability re-derivation at lens table time. V-02 closes the C-34 domain anchor
gap by tagging domains at SCOPE DECLARATION time and treating the annotated table as
the sole gap-check input. V-04 combines both: C-33 and C-34 are each enforced by a
chain-of-custody protocol rather than by behavioral mandates alone. The two protocols
are orthogonal -- §10 INHERITANCE governs Applicability inheritance; §9 DOMAIN
ANNOTATION governs the gap-check domain source -- and do not interact. C-35 via
PRIMACY DEVIATION CASE. Predicted: 225/225 with C-33 and C-34 chain of custody
both fully closed.

---

You are running `/org-review`.

Inputs:
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .roles/]
```

Acknowledge injected values before executing any section.

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
```
HIGH = blocks | MEDIUM = conditions | LOW = advisory
FAIL -> BLOCKED | >= 1 CONDITIONAL + no FAIL -> CONDITIONAL | All PASS -> READY
```
OVERRIDE: BRACKET CLOSING only, OVERRIDE INVOKED: YES | NO + justification.

---

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY. No editorial assignment.

---

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23, C-35)**

NH DIMENSION COMPARISON TABLE at BRACKET OPENING. Three alternatives (Status Quo /
Proposed Build / Best-Non-Build-Alt). Format:
```
| Dimension | A: Status Quo | B: Proposed Build | C: Best Non-Build Alt | Delta B-A | Delta B-C |
```
Minimum 3 dimensions, consistent scale. g_null from table alone:
```
g_null = PASS if both deltas > 0 | CONDITIONAL if one > 0 | FAIL if both <= 0
```
Prose is invalid as substitute. Table governs g_null. BRACKET CLOSING re-populates
columns B/C; g_null(final) from revised table.

**PRIMACY DEVIATION CASE (C-35)**: prose asserting different g_null than table formula ->
`NH-NARRATIVE-TABLE-MISMATCH: prose=[X]; table=[Y]; table governs.` Binding at both.

---

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
```
Stage 1: g_null(initial)     [BRACKET OPENING]
Stage 2: g_null(post-domain) [CH-ID SATURATION CHECK, G_domain_agg]
Stage 3: g_null(final)       [BRACKET CLOSING, G_lifecycle]
```
GClose = g_null(final) or OVERRIDE.

---

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21, C-25)**
Universal: BRACKET OPENING, DOMAIN sections, LIFECYCLE, BRACKET CLOSING emit one row:
```
| Gate Verdict | Section Severity | Class | Finding References |
```
Non-verdict sections: no row (see §7). MASTER ACTION REGISTER: verbatim copy.

---

**§6 VERBATIM ASSEMBLY PROHIBITION (C-20)**
Verbatim copy only. Re-derivation prohibited. Local row is authority.

---

**§7 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate row: SCOPE DECLARATION, LENS APPLICABILITY PRE-REGISTRATION, CH-ID REGISTRATION
TABLE, CH-ID SATURATION CHECK, SCOPE COVERAGE RECONCILIATION, LENS COVERAGE TABLE,
DOMAIN COVERAGE GAP-CHECK.

---

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
1.  SCOPE DECLARATION            [domain tags committed here -- §9]
2.  LENS APPLICABILITY PRE-REGISTRATION   [Applicability authority -- §10]
3.  CH-ID REGISTRATION TABLE
4.  BRACKET OPENING
5.  DOMAIN REVIEWER SECTIONS (manifest order)
6.  CH-ID SATURATION CHECK
7.  LIFECYCLE REVIEWER SECTION
8.  BRACKET CLOSING
9.  SCOPE COVERAGE RECONCILIATION
10. LENS COVERAGE TABLE          [Applicability verbatim-copy from step 2 -- §11]
11. DOMAIN COVERAGE GAP-CHECK    [domain input from step 1 -- §9]
12. DISPOSITION + PRIMARY DRIVER
13. MASTER ACTION REGISTER
14. CROSS-ROLE SIGNALS
```
Step 2 completes before step 4. Step 7 precedes step 8. Steps 10 and 11 are required
independent sections.

---

**§9 SCOPE-DECLARATION DOMAIN ANNOTATION + GAP-CHECK SOURCE PROTOCOL (C-34)** [IMMUTABLE]

At SCOPE DECLARATION (step 1), annotate every IN-SCOPE surface with a domain tag:
```
| Surface | Domain | In/Out of Scope | Note |
```
Domain list is committed at step 1 and read-only for gap-check purposes. DOMAIN
COVERAGE GAP-CHECK (step 11) iterates unique Domain values from this table as its
sole input set. Post-review domain inference is prohibited as the source for step 11.
Domains appearing in findings but absent from step 1: flag as UNDECLARED-DOMAIN in
CROSS-ROLE SIGNALS; do not add to gap-check input set.

---

**§10 LENS APPLICABILITY PRE-REGISTRATION PROTOCOL (C-33)** [IMMUTABLE]

Before any reviewer section, emit:
```
| Reviewer Role | Lens Dimension | Pre-Committed Applicability |
```
Applicability (HIGH/MEDIUM/LOW): artifact-specific. Immutable after pre-registration.
This table is the applicability authority for all downstream steps.

---

**§11 APPLICABILITY INHERITANCE PROTOCOL (C-33)** [IMMUTABLE]

PRE-REGISTRATION TABLE (step 2, §10) is the Applicability authority. LENS COVERAGE
TABLE (step 10) Applicability column: verbatim-copy from PRE-REGISTRATION only. No
re-derivation at table-population time.

Deviation: emit INHERITANCE-DEVIATION-ALERT when pre-registered value differs from what
the model would independently assign at step 10:
```
INHERITANCE-DEVIATION-ALERT: Role=[r] / Dimension=[d] /
  Pre-Registered=[X] / Attempted=[Y] / Justification=[z]
```
Pre-registered value governs unless BRACKET CLOSING invokes OVERRIDE INVOKED: YES.
Alert flagged in CROSS-ROLE SIGNALS as ADVISORY. Silent recalculation is a chain-of-
custody error.

---

**§12 CH-ID CHALLENGE REGISTRATION (C-04, C-05)**
```
| CH-ID | Challenge Statement | Bracket Opening | [Domain roles...] | Lifecycle | Bracket Closing |
```
Every reviewer section carries a CH-ID response table.

---

**§13 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED: every CH-ID >= 1 DOMAIN response. FULLY SATURATED: + LIFECYCLE.
BRACKET CLOSING PASS blocked when UNSATURATED without waiver.

---

**§14 LIFECYCLE VERDICT INTEGRATION CONTRACT (C-22)**
LIFECYCLE precedes BRACKET CLOSING. `Lifecycle verdict received: g_lifecycle = [value]`.

---

**§15 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(DOMAIN gate verdicts). FAIL < CONDITIONAL < PASS.

---

**§16 ROLE LENS EXHAUSTION PROTOCOL (C-31)** [IMMUTABLE]

LENS COVERAGE TABLE (step 10):
```
| Reviewer Role | Lens Dimension | Applicability | Status | Finding Reference(s) |
```
Applicability: verbatim-copy from PRE-REGISTRATION per §11. HIGH + OPEN ->
ADVISORY-OPEN-LENS in MASTER ACTION REGISTER.

**DOMAIN COVERAGE GAP-CHECK (step 11, mandatory)**: iterate unique domain values from
step 1 scope table (§9). Check HIGH Applicability per domain. ADVISORY-GAP for uncovered.
Append to MASTER ACTION REGISTER. Emit summary.

---

**§17 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-BRACKET CLOSING: SCOPE COVERAGE RECONCILIATION maps IN-SCOPE surfaces to findings.
GAP -> ADVISORY-GAP, LOW, appended. No gate row.

---

**§18 PER-FINDING SEVERITY CHAIN (C-30)** [IMMUTABLE]
Section Severity = worst(individual severities). Per-row Severity on every finding.
No editorial section-level assignment.

---

**§19 PRIMARY DRIVER DERIVATION (C-32)** [IMMUTABLE]
First-match: BRACKET CLOSING OVERRIDE > NULL HYPOTHESIS > DOMAIN FAIL (first) >
LIFECYCLE FAIL > DOMAIN CONDITIONAL (first) > LIFECYCLE CONDITIONAL > CONSENSUS.
`Primary Driver: [value]` at DISPOSITION.

---

**§20 INPUT VARIABLE CONTRACTS (C-08, C-13, C-15)**
Variables: `{{artifact_id}}`, `{{depth}}`, `{{reviewer_set}}`. Acknowledgment block required.

---

### EXECUTION

**Step 1**: Acknowledge inputs.

**Step 2: SCOPE DECLARATION** (§9) -- emit annotated scope table with domain tags for
every IN-SCOPE surface; domain list committed and read-only for gap-check. OUT-OF-SCOPE
surfaces enumerated. Mid-review discoveries flagged as scope gaps.

**Step 3: LENS APPLICABILITY PRE-REGISTRATION** (§10) -- pre-commit all Applicability
ratings; these are the applicability authority for all downstream steps per §11.

**Step 4: CH-ID REGISTRATION TABLE** (§12)

**Step 5: BRACKET OPENING** -- NH DIMENSION COMPARISON TABLE per §3; g_null(initial)
from table; PRIMACY DEVIATION CASE if applicable; OVERRIDE INVOKED: NO; CH-ID responses;
LOCAL GATE LEDGER ROW.

**Step 6: DOMAIN REVIEWER SECTIONS** -- `| Severity | Surface | Finding | Recommendation |`;
CH-ID responses; LOCAL GATE LEDGER ROW; Section Severity per §18.

**Step 7: CH-ID SATURATION CHECK** -- verify SATURATED; g_null(post-domain) per §4.

**Step 8: LIFECYCLE REVIEWER SECTION** -- lifecycle lens; findings; CH-ID responses;
LOCAL GATE LEDGER ROW with g_lifecycle.

**Step 9: BRACKET CLOSING** -- G_domain_agg (§15) and g_lifecycle as labeled inputs;
revised NH table columns B/C; g_null(final) per §3; OVERRIDE INVOKED; LOCAL GATE LEDGER ROW.

**Step 10: SCOPE COVERAGE RECONCILIATION** (§17; no gate row)

**Step 11: LENS COVERAGE TABLE** (§16; no gate row) -- verbatim-copy Applicability from
step 3 per §11; emit INHERITANCE-DEVIATION-ALERT for any deviation.

**Step 12: DOMAIN COVERAGE GAP-CHECK** (§16; no gate row) -- iterate step 2 domain list;
no post-review domain inference.

**Step 13: DISPOSITION** -- §1 algebra; DISPOSITION; Primary Driver per §19.

**Step 14: MASTER ACTION REGISTER** -- verbatim copy (§6); append advisory items; no re-derivation.

**Step 15: CROSS-ROLE SIGNALS** -- integration narrative; cross-role conflict/convergence;
g_null progression; disposition explanation; flag INHERITANCE-DEVIATION-ALERTs and
UNDECLARED-DOMAIN discoveries.

---

## V-05

**Axis**: C-33 Verbatim Inheritance Lock + C-34 Scope-Declaration Domain Anchor +
C-35 Two-Phase NH Table Construction (three-axis) -- V-01's APPLICABILITY INHERITANCE
PROTOCOL + V-02's scope-declaration domain annotation + V-03's two-phase NH table
construction; maximum chain-of-custody and back-fill prevention for all three new
criteria simultaneously

**Hypothesis**: Each of V-01, V-02, V-03 closes one failure mode independently.
V-04 combines V-01 and V-02. V-05 combines all three. C-33 chain of custody: verbatim
inheritance lock prevents silent Applicability recalculation at lens table time. C-34
domain anchor: scope-declaration domain annotation prevents gap-check domain drift.
C-35 construction integrity: two-phase construction prevents back-filling dimension
scores to match prose intent. The three protocols are orthogonal -- §11 governs
Applicability inheritance, §9 governs domain source, §3 governs NH table construction
-- and no interaction points exist. V-05 tests whether all three failure modes can be
closed simultaneously. Predicted: 225/225, maximum structural closure for all three
new criteria.

---

You are running `/org-review`.

Inputs:
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .roles/]
```

Acknowledge injected values before executing any section.

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
```
HIGH = blocks commitment | MEDIUM = conditions commitment | LOW = advisory
FAIL -> BLOCKED | >= 1 CONDITIONAL + no FAIL -> CONDITIONAL | All PASS -> READY
```
OVERRIDE: BRACKET CLOSING only, OVERRIDE INVOKED: YES | NO + justification.

---

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (omit if none).
No editorial class assignment at assembly time.

---

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23, C-35)**

**NH DIMENSION COMPARISON TABLE -- Two-Phase Construction Protocol**:

**Phase 1 -- DIMENSION REGISTRATION** (immutable before Phase 2 begins):
Emit DIMENSION REGISTRY before assigning any scores:
```
| # | Dimension | Measurement Basis | Scale |
```
- `Dimension`: evaluation axis, specific enough to score without further interpretation.
- `Measurement Basis`: the observable being scored (e.g., "estimated developer-days",
  "% users completing task unassisted in < 2 min").
- `Scale`: scoring range consistent across all dimensions and alternatives (e.g.,
  "1=worst, 10=best"). Declared once in Phase 1.
- Minimum 3 rows. No dimensions may be added, removed, or renamed in Phase 2.

**Phase 2 -- VALUE ASSIGNMENT** (follows Phase 1):
Score all three alternatives using Phase 1 dimensions and scale:
```
| Dimension | A: Status Quo | B: Proposed Build | C: Best Non-Build Alt | Delta B-A | Delta B-C |
```
g_null derivable from table alone:
```
g_null = PASS        if delta_B_A > 0 AND delta_B_C > 0
g_null = CONDITIONAL if exactly one delta > 0
g_null = FAIL        if delta_B_A <= 0 AND delta_B_C <= 0
```

**Prose testimony** follows Phase 2. Prose may not change Phase 1 definitions or
Phase 2 values. Table governs g_null.

**CONSTRUCTION DEVIATION CASE**: If Phase 2 reveals a Phase 1 dimension was poorly
specified, emit:
```
NH-CONSTRUCTION-DEVIATION: Dimension=[d] / Phase-1-basis=[original] /
  Issue=[issue] / Proposed-revision=[revision]
```
Phase 1 values govern unless BRACKET CLOSING invokes OVERRIDE INVOKED: YES.
Flag in CROSS-ROLE SIGNALS.

**PRIMACY DEVIATION CASE (C-35)**: prose asserting different g_null than Phase 2 formula ->
`NH-NARRATIVE-TABLE-MISMATCH: prose=[X]; table=[Y]; table governs.` Binding at both.

BRACKET CLOSING re-populates Phase 2 columns B and C (Phase 1 immutable). g_null(final)
from revised Phase 2 table per formula.

---

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
```
Stage 1: g_null(initial)     [BRACKET OPENING -- from Phase 2 table]
Stage 2: g_null(post-domain) [CH-ID SATURATION CHECK -- G_domain_agg formula]
         FAIL: holds | PASS: weakens one tier | CONDITIONAL: CONDITIONAL
Stage 3: g_null(final)       [BRACKET CLOSING -- same substituting G_lifecycle]
```
GClose = g_null(final) or OVERRIDE INVOKED: YES.

---

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21, C-25)**
Universal: BRACKET OPENING, DOMAIN sections, LIFECYCLE, BRACKET CLOSING emit one row:
```
| Gate Verdict | Section Severity | Class | Finding References |
```
Non-verdict sections: no row (see §7). MASTER ACTION REGISTER: verbatim copy.

---

**§6 VERBATIM ASSEMBLY PROHIBITION (C-20)**
Verbatim copy only. Re-derivation of Gate Verdict or Class prohibited.
Local row is point of authority.

---

**§7 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate row: SCOPE DECLARATION, LENS APPLICABILITY PRE-REGISTRATION, CH-ID REGISTRATION
TABLE, CH-ID SATURATION CHECK, SCOPE COVERAGE RECONCILIATION, LENS COVERAGE TABLE,
DOMAIN COVERAGE GAP-CHECK.

---

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
1.  SCOPE DECLARATION            [domain tags committed here per §9]
2.  LENS APPLICABILITY PRE-REGISTRATION   [Applicability authority per §10]
3.  CH-ID REGISTRATION TABLE
4.  BRACKET OPENING  [Phase 1 DIMENSION REGISTRY then Phase 2 VALUE ASSIGNMENT]
5.  DOMAIN REVIEWER SECTIONS (manifest order)
6.  CH-ID SATURATION CHECK
7.  LIFECYCLE REVIEWER SECTION
8.  BRACKET CLOSING  [re-populate Phase 2 columns B/C; Phase 1 immutable]
9.  SCOPE COVERAGE RECONCILIATION
10. LENS COVERAGE TABLE          [Applicability verbatim-copy from step 2 per §11]
11. DOMAIN COVERAGE GAP-CHECK    [domain input from step 1 per §9]
12. DISPOSITION + PRIMARY DRIVER
13. MASTER ACTION REGISTER
14. CROSS-ROLE SIGNALS
```
Step 2 completes before step 4. Step 7 precedes step 8. Steps 10 and 11 are required
independent sections; executing step 10 without step 11 is a section-order violation.

---

**§9 SCOPE-DECLARATION DOMAIN ANNOTATION + GAP-CHECK SOURCE PROTOCOL (C-34)** [IMMUTABLE]

At SCOPE DECLARATION (step 1), annotate every IN-SCOPE surface with a domain tag:
```
| Surface | Domain | In/Out of Scope | Note |
```
Domain list is committed at step 1 and read-only for gap-check purposes. DOMAIN
COVERAGE GAP-CHECK (step 11) iterates unique Domain values from this table as its
sole input set. Post-review domain inference is prohibited as the gap-check source.
Domains found in findings but absent from step 1: flag UNDECLARED-DOMAIN in CROSS-ROLE
SIGNALS; do not add to gap-check input set.

---

**§10 LENS APPLICABILITY PRE-REGISTRATION PROTOCOL (C-33)** [IMMUTABLE]

Before any reviewer section, emit:
```
| Reviewer Role | Lens Dimension | Pre-Committed Applicability |
```
Applicability (HIGH/MEDIUM/LOW): artifact-specific. Immutable after pre-registration.
This table is the applicability authority for all downstream steps.

---

**§11 APPLICABILITY INHERITANCE PROTOCOL (C-33)** [IMMUTABLE]

PRE-REGISTRATION TABLE (step 2, §10) is the Applicability authority. LENS COVERAGE
TABLE (step 10) Applicability column: verbatim-copy from PRE-REGISTRATION only.
No re-derivation at table-population time.

Deviation: emit INHERITANCE-DEVIATION-ALERT when pre-registered value differs from
what the model would independently assign at step 10:
```
INHERITANCE-DEVIATION-ALERT: Role=[r] / Dimension=[d] /
  Pre-Registered=[X] / Attempted=[Y] / Justification=[z]
```
Pre-registered value governs unless BRACKET CLOSING invokes OVERRIDE INVOKED: YES.
Flag as ADVISORY in CROSS-ROLE SIGNALS. Silent recalculation is a chain-of-custody error.

---

**§12 CH-ID CHALLENGE REGISTRATION (C-04, C-05)**
```
| CH-ID | Challenge Statement | Bracket Opening | [Domain roles...] | Lifecycle | Bracket Closing |
```
Every reviewer section carries a CH-ID response table.

---

**§13 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED: every CH-ID >= 1 DOMAIN response. FULLY SATURATED: + LIFECYCLE.
BRACKET CLOSING PASS blocked when UNSATURATED without waiver.

---

**§14 LIFECYCLE VERDICT INTEGRATION CONTRACT (C-22)**
LIFECYCLE (step 7) precedes BRACKET CLOSING (step 8).
`Lifecycle verdict received: g_lifecycle = [value]` as labeled input.

---

**§15 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(all DOMAIN gate verdicts). FAIL < CONDITIONAL < PASS. Labeled input.

---

**§16 ROLE LENS EXHAUSTION PROTOCOL (C-31)** [IMMUTABLE]

LENS COVERAGE TABLE (step 10):
```
| Reviewer Role | Lens Dimension | Applicability | Status | Finding Reference(s) |
```
Applicability: verbatim-copy from PRE-REGISTRATION per §11. Deviations require
INHERITANCE-DEVIATION-ALERT. HIGH + OPEN -> ADVISORY-OPEN-LENS in MASTER ACTION REGISTER.

**DOMAIN COVERAGE GAP-CHECK (step 11, mandatory)**: iterate unique domain values from
step 1 scope table (§9); no new domains from findings. Check HIGH Applicability per
domain. ADVISORY-GAP for uncovered; append to MASTER ACTION REGISTER.
Emit: `DOMAIN COVERAGE GAP-CHECK: [N covered at HIGH | N ADVISORY-GAP]`

---

**§17 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-BRACKET CLOSING: SCOPE COVERAGE RECONCILIATION maps IN-SCOPE surfaces to findings.
GAP -> ADVISORY-GAP, LOW, appended. No gate row.

---

**§18 PER-FINDING SEVERITY CHAIN (C-30)** [IMMUTABLE]
Section Severity = worst(individual severities). Every finding row carries individual
Severity. No editorial section-level assignment.

---

**§19 PRIMARY DRIVER DERIVATION (C-32)** [IMMUTABLE]
First-match: BRACKET CLOSING OVERRIDE > NULL HYPOTHESIS > DOMAIN FAIL (first) >
LIFECYCLE FAIL > DOMAIN CONDITIONAL (first) > LIFECYCLE CONDITIONAL > CONSENSUS.
`Primary Driver: [value]` at DISPOSITION.

---

**§20 INPUT VARIABLE CONTRACTS (C-08, C-13, C-15)**
Variables: `{{artifact_id}}`, `{{depth}}`, `{{reviewer_set}}`. Acknowledgment block required.

---

### EXECUTION

**Step 1**: Acknowledge inputs -- emit acknowledgment block with all three variable values.

**Step 2: SCOPE DECLARATION** (§9)
Emit annotated scope table with domain tags for every IN-SCOPE surface:
`| Surface | Domain | In/Out of Scope | Note |`
Domain list committed here; read-only for gap-check. OUT-OF-SCOPE surfaces enumerated.
Mid-review discoveries: flag as scope gap.

**Step 3: LENS APPLICABILITY PRE-REGISTRATION** (§10)
Pre-commit all lens dimension Applicability ratings for every active reviewer role.
Emit PRE-REGISTRATION TABLE before CH-ID REGISTRATION. No reviewer runs until complete.
These values are the applicability authority for all downstream steps.

**Step 4: CH-ID REGISTRATION TABLE** (§12)

**Step 5: BRACKET OPENING**
- Phase 1 DIMENSION REGISTRATION (§3): emit DIMENSION REGISTRY (>= 3 dimensions with
  measurement basis and scale); Phase 1 complete before any scores.
- Phase 2 VALUE ASSIGNMENT (§3): score all three alternatives; compute deltas.
- Emit g_null(initial) from Phase 2 table per formula.
- Apply PRIMACY DEVIATION CASE if prose and table diverge.
- Apply CONSTRUCTION DEVIATION CASE if Phase 1 basis appears ill-defined after Phase 2.
- Emit OVERRIDE INVOKED: NO (default).
- CH-ID responses per §12.
- LOCAL GATE LEDGER ROW per §5.

**Step 6: DOMAIN REVIEWER SECTIONS** (one per role, manifest order)
- "As a [role], I evaluate [lens concern]."
- Finding rows: `| Severity | Surface | Finding | Recommendation |`
- CH-ID responses.
- LOCAL GATE LEDGER ROW per §5. Section Severity = worst(finding severities) per §18.

**Step 7: CH-ID SATURATION CHECK**
- Verify SATURATED tier.
- Emit g_null(post-domain) per §4 Stage 2 formula.
- No gate ledger row.

**Step 8: LIFECYCLE REVIEWER SECTION**
- Lifecycle lens over operational phases.
- Finding rows (same format).
- CH-ID responses.
- LOCAL GATE LEDGER ROW per §5 with g_lifecycle labeled.

**Step 9: BRACKET CLOSING**
- Receive G_domain_agg (§15) and g_lifecycle as labeled inputs.
- Re-populate Phase 2 NH table columns B and C (Phase 1 immutable).
- Derive g_null(final) per §3 formula (§4 Stage 3).
- Emit OVERRIDE INVOKED: YES | NO as labeled field.
- LOCAL GATE LEDGER ROW per §5.

**Step 10: SCOPE COVERAGE RECONCILIATION** (§17; no gate ledger row)

**Step 11: LENS COVERAGE TABLE** (§16; no gate ledger row)
Verbatim-copy Applicability from step 3 per §11. Emit INHERITANCE-DEVIATION-ALERT
for any deviation. HIGH + OPEN rows -> ADVISORY-OPEN-LENS in register.

**Step 12: DOMAIN COVERAGE GAP-CHECK** (§16; no gate ledger row)
Iterate unique domain values from step 2 scope table (§9). No post-review domain
inference. ADVISORY-GAP for uncovered domains; append to register.

**Step 13: DISPOSITION**
- Apply §1 DISPOSITION ALGEBRA.
- Emit `DISPOSITION: READY | CONDITIONAL | BLOCKED` as labeled field.
- Emit `Primary Driver: [value]` per §19.

**Step 14: MASTER ACTION REGISTER**
- Copy all LOCAL GATE LEDGER ROWS verbatim per §6.
- Append ADVISORY-OPEN-LENS items from step 11.
- Append ADVISORY-GAP items from step 12.
- Append ADVISORY-GAP items from step 10.
- Do not re-derive Gate Verdict or Class.

**Step 15: CROSS-ROLE SIGNALS**
- Integration narrative: name >= 1 cross-role conflict or convergence.
- Reference g_null progression through all three stages (initial, post-domain, final).
- Explain the disposition rather than restating it.
- Flag any INHERITANCE-DEVIATION-ALERTs from step 11.
- Flag any NH-CONSTRUCTION-DEVIATIONs from step 5.
- Flag any UNDECLARED-DOMAIN discoveries from step 12.
