---
skill: quest-variate
skill_target: org-review
date: 2026-03-17
round: 19
rubric: org-review-rubric-v11-2026-03-16.md
---

# org-review -- Variate R19 (rubric v11)

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis and three-axis combinations (V-04, V-05).

**R19 design target**: R18-v11 generated five variants all predicted at 225/225
through three axis paths: (a) pre-§§ LENS OUTPUT SCHEMA block, (b) dense
behavioral §13 with violation conditions, (c) scope-anchored NH dimension
derivation. R19 investigates whether robustness holds under three fresh single
axes not explored in R18: role sequence (Applicability pre-registration before
reviewers run), lifecycle emphasis (DOMAIN COVERAGE GAP-CHECK as a first-class
numbered step in the section order), and phrasing register (declarative
contract specification with explicit deviation cases, replacing imperative
enforcement). All five predicted at 225/225; the question is which structural
path most reliably satisfies C-33's "pre-committed" requirement and C-34's
mandatory gap-check under adversarial conditions.

**R19 gap analysis (from R18-v11 predicted vs potential failure modes):**

| Criterion | R18 approach | Potential failure mode | R19 remediation |
|-----------|-------------|----------------------|----------------|
| C-33 LENS APPLICABILITY RATING | Schema block + behavioral §13 | Model populates lens table at §13 without consulting the pre-committed schema; Applicability column added ad hoc or omitted | Pre-register Applicability at LENS APPLICABILITY PRE-REGISTRATION step (before reviewers run); model commits ratings before it can forget |
| C-34 ADVISORY-GAP DOMAIN COVERAGE | Behavioral mandate within §13 | Gap-check treated as optional annotation after lens table, not a required section | Promote to numbered step in SECTION ORDER CONTRACT; gap-check is structurally required by the order, not just by §13 text |
| C-35 NH CHALLENGER DIMENSION TABLE | §3 NH DERIVATION RULE + scope-anchoring | Challenger uses the table format but derives g_null from prose narrative alongside table | Add explicit DEVIATION CASE: table produces g_null=X; if prose narrative says otherwise, table wins; no silent override |

**R19 variation axes:**

- V-01: Role sequence (single axis) -- LENS APPLICABILITY PRE-REGISTRATION step
  inserted between CH-ID REGISTRATION TABLE and BRACKET OPENING. Applicability
  ratings for every active reviewer's lens dimensions are declared before any
  section runs. BRACKET OPENING cannot begin until this registry exists. C-33:
  Applicability is structurally pre-committed via execution order, not just via
  schema or behavioral contract. C-34 via §13. C-35 via §3.
  Predicted: 225/225.

- V-02: Lifecycle emphasis (single axis) -- DOMAIN COVERAGE GAP-CHECK promoted
  to step 10a in the §8 SECTION ORDER CONTRACT (between LENS COVERAGE TABLE
  and DISPOSITION). Gap-check is an independent numbered step, not a sub-step
  of §13. §13 references step 10a rather than hosting the gap-check behavior.
  C-34: structurally mandatory by section order, not just by §13 protocol.
  C-33 via §13. C-35 via §3. Predicted: 225/225.

- V-03: Phrasing register (single axis) -- declarative specification language
  throughout. §3 and §13 written as TYPE DEFINITIONS and DEVIATION CASES rather
  than imperative mandates. C-35: NH Dimension Comparison Table type definition
  includes an explicit deviation case declaring table primacy over prose. C-33:
  Applicability defined as a TYPED FIELD with domain (HIGH|MEDIUM|LOW) and
  explicit constraints (artifact-specific, not role-generic, immutable after
  lens table population). C-34: DOMAIN COVERAGE GAP-CHECK defined as a
  MANDATORY OPERATION with enumerated exception classes (only one: all domains
  covered). Predicted: 225/225.

- V-04: Role sequence + Lifecycle emphasis (two-axis) -- V-01's LENS APPLICABILITY
  PRE-REGISTRATION step + V-02's gap-check as numbered step 10a. Both C-33
  and C-34 enforced via section order rather than via text contracts alone.
  Predicted: 225/225, strongest enforcement for C-33/C-34 via structural
  ordering.

- V-05: Role sequence + Lifecycle emphasis + Phrasing register (three-axis) --
  all three: LENS APPLICABILITY PRE-REGISTRATION (V-01), numbered gap-check step
  (V-02), and declarative type definitions with deviation cases (V-03). Maximum
  structural and contractual reinforcement for all three new criteria.
  Predicted: 225/225.

---

## V-01

**Axis**: Role sequence -- LENS APPLICABILITY PRE-REGISTRATION inserted as a
mandatory step between CH-ID REGISTRATION TABLE and BRACKET OPENING; Applicability
ratings committed before any reviewer section executes

**Hypothesis**: R18's C-33 enforcement relied on pre-§§ schema blocks or
behavioral §13 contracts that declare Applicability as a required field. Both
approaches ask the model to remember the requirement at §13 time and apply it
retroactively. The role sequence axis tests an alternative: make Applicability a
first-class step that executes before any reviewer runs. Once the LENS APPLICABILITY
PRE-REGISTRATION exists (a table of reviewer × lens dimension × Applicability),
the model has already committed the ratings before producing findings. §13 becomes
a verification step (do the table rows match the pre-registration?) rather than the
only enforcement point. C-34 via §13. C-35 via §3 NH table format. Predicted:
225/225 with structurally earlier commitment for C-33.

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
COMPARISON TABLE. Three alternatives are required: A (Status Quo -- what the team
does today instead of building this), B (Proposed Build), C (Best-Non-Build-Alt).

**Required table format** (emitted at BRACKET OPENING):
```
| Dimension | A: Status Quo | B: Proposed Build | C: Best Non-Build Alt | Delta B-A | Delta B-C |
```

Minimum 3 dimensions, scored on a consistent scale. The null hypothesis verdict
derives from the table alone:
```
g_null = PASS        if delta_B_A > 0 AND delta_B_C > 0
g_null = CONDITIONAL if exactly one delta > 0
g_null = FAIL        if delta_B_A <= 0 AND delta_B_C <= 0
```

Prose-only null hypothesis evaluation is invalid as a substitute for the table.
The challenger may add prose testimony after the table; the table is the
authoritative source for g_null. BRACKET CLOSING re-populates columns B and C
with revised values (post-domain and lifecycle evidence received); g_null(final)
derives from the revised table per the same formula.

---

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
```
Stage 1: g_null(initial)     [BRACKET OPENING -- from NH Dimension Comparison Table]
Stage 2: g_null(post-domain) [CH-ID SATURATION CHECK -- formula over G_domain_agg + g_null(initial)]
         G_domain_agg = FAIL:        g_null(post-domain) = g_null(initial) [challenger holds]
         G_domain_agg = PASS:        g_null(post-domain) weakens one tier toward PASS
         G_domain_agg = CONDITIONAL: g_null(post-domain) = CONDITIONAL
Stage 3: g_null(final)       [BRACKET CLOSING -- same logic substituting G_lifecycle]
```
BRACKET CLOSING GClose verdict MUST equal g_null(final), or declare OVERRIDE
INVOKED: YES with named justification.

---

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21, C-25)**

Universal coverage: BRACKET OPENING, every DOMAIN section, LIFECYCLE section,
and BRACKET CLOSING each emit exactly one LOCAL GATE LEDGER ROW at verdict time:
```
| Gate Verdict | Section Severity | Class | Finding References |
|---|---|---|---|
| [FAIL/CONDITIONAL/PASS] | [HIGH/MEDIUM/LOW] | [BLOCKED/CONDITIONAL/ADVISORY] | [list] |
```
Non-verdict sections emit no row (see §6). MASTER ACTION REGISTER assembled by
verbatim copy of all LOCAL GATE LEDGER ROWS.

---

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**

These sections emit NO gate ledger row:
- §§ PREAMBLE CONTRACTS (pre-execution contracts)
- SCOPE DECLARATION
- LENS APPLICABILITY PRE-REGISTRATION
- CH-ID REGISTRATION TABLE
- CH-ID SATURATION CHECK (emits g_null(post-domain) as labeled field, not gate row)
- SCOPE COVERAGE RECONCILIATION (informational)
- LENS COVERAGE TABLE and DOMAIN COVERAGE GAP-CHECK (informational)

---

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**

MASTER ACTION REGISTER assembly: copy all LOCAL GATE LEDGER ROWS verbatim. Do not
re-derive Gate Verdict or Class. The local row is the point of authority; the
register is a copy only.

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
before BRACKET OPENING (step 4). LIFECYCLE (step 7) must execute before BRACKET
CLOSING (step 8). The LENS COVERAGE TABLE (step 10) and DOMAIN COVERAGE GAP-CHECK
(step 11) execute after BRACKET CLOSING and before DISPOSITION.

---

**§9 LENS APPLICABILITY PRE-REGISTRATION PROTOCOL (C-33)** [IMMUTABLE]

Before any reviewer section executes, emit the LENS APPLICABILITY PRE-REGISTRATION
TABLE. For each active reviewer role (as determined by {{depth}} and
{{reviewer_set}}), every `lens.verify` entry from the role's .roles/
definition must appear in this table with a pre-committed Applicability rating:

```
| Reviewer Role | Lens Dimension | Pre-Committed Applicability |
```

- `Pre-Committed Applicability`: HIGH, MEDIUM, or LOW.
  - HIGH: this lens dimension is directly relevant to this artifact's domain and scope.
  - MEDIUM: relevant but not central to this artifact's primary risk surface.
  - LOW: tangential or minimally applicable to this artifact's context.
  The rating is artifact-specific, not role-generic. The same role reviewing a
  different artifact may carry different ratings. Once committed in this table,
  the Applicability rating is authoritative for all downstream steps.

Omitting any reviewer's lens dimension from this table before that reviewer's
section runs is a protocol violation. The LENS COVERAGE TABLE (step 10) inherits
Applicability from this pre-registration; rows in the lens table must match the
pre-committed values. Deviations must be explicitly flagged with justification.

HIGH-applicability entries in this table govern ADVISORY-OPEN-LENS promotion:
a lens dimension pre-registered as HIGH that has Status=OPEN at step 10 becomes
an ADVISORY-OPEN-LENS item in the MASTER ACTION REGISTER.

---

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-05)**

Before BRACKET OPENING (step 4), register all challenges in the CH-ID tracing table:
```
| CH-ID | Challenge Statement | Bracket Opening | [Domain roles...] | Lifecycle | Bracket Closing |
```
Populate CH-ID and Challenge Statement at registration time. Response columns are
populated during execution as each reviewer section responds. Every reviewer section
carries a CH-ID response table (one row per CH-ID -- ADDRESSED or DEFERRED + rationale).

---

**§11 CH-ID SATURATION REQUIREMENT (C-27)**
```
SATURATED:       every CH-ID has >= 1 DOMAIN section response (verified before LIFECYCLE)
FULLY SATURATED: every CH-ID has domain + lifecycle responses (verified at BRACKET CLOSING)
```
BRACKET CLOSING may not emit PASS when any CH-ID is UNSATURATED without explicit
waiver and stated justification.

---

**§12 LIFECYCLE VERDICT INTEGRATION CONTRACT (C-22)**

LIFECYCLE section (step 7) executes before BRACKET CLOSING (step 8). BRACKET
CLOSING receives g_lifecycle as a labeled input:
`Lifecycle verdict received: g_lifecycle = [FAIL/CONDITIONAL/PASS]`
and factors it into the g_null(final) derivation per §4 Stage 3.

---

**§13 DOMAIN-AGGREGATE FORMULA (C-24)**
```
G_domain_agg = median(all DOMAIN reviewer gate verdicts)
median order: FAIL < CONDITIONAL < PASS
```
Labeled input to BRACKET CLOSING for §4 Stage 2 application.

---

**§14 ROLE LENS EXHAUSTION PROTOCOL (C-31, C-34)**

After step 10 (LENS COVERAGE TABLE), execute step 11 (DOMAIN COVERAGE GAP-CHECK)
per the SECTION ORDER CONTRACT (§8). The LENS COVERAGE TABLE row schema:
```
| Reviewer Role | Lens Dimension | Applicability | Status | Finding Reference(s) |
```
Applicability values are inherited from the LENS APPLICABILITY PRE-REGISTRATION
(step 2, §9). Status = ADDRESSED (>= 1 finding cites this dimension) or OPEN.

**DOMAIN COVERAGE GAP-CHECK** (step 11, mandatory): After the LENS COVERAGE TABLE,
enumerate every artifact domain from the SCOPE DECLARATION. For each domain, check
whether any reviewer has HIGH Applicability for a lens dimension covering that
domain. Domains with no HIGH-applicability coverage: classify as ADVISORY-GAP and
append to MASTER ACTION REGISTER (domain name + reason + recommended mitigation).
Emit: `DOMAIN COVERAGE GAP-CHECK: [N domains covered at HIGH | N domains ADVISORY-GAP]`

---

**§15 SCOPE COVERAGE GATE PROTOCOL (C-29)**

After BRACKET CLOSING (step 8): SCOPE COVERAGE RECONCILIATION maps every IN-SCOPE
surface to findings. Surfaces with no finding: ADVISORY-GAP, LOW severity, appended
to MASTER ACTION REGISTER. No gate ledger row (§6).

---

**§16 PER-FINDING SEVERITY CHAIN (C-30)** [IMMUTABLE]
```
Section Severity = worst(Severity of all individual findings in this section)
worst order: HIGH > MEDIUM > LOW
```
Every finding row in every reviewer section carries an individual Severity field
(HIGH / MEDIUM / LOW). Section Severity in the LOCAL GATE LEDGER ROW derives
mechanically from this formula. No editorial section-level severity assignment.

---

**§17 PRIMARY DRIVER DERIVATION (C-32)** [IMMUTABLE]

After all gate verdicts are known, emit Primary Driver by first-match precedence:
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

**§18 INPUT VARIABLE CONTRACTS (C-08, C-13, C-15)**

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
run until this table is complete.

**Step 4: CH-ID REGISTRATION TABLE** (per §10)
Register all challenges before any reviewer section runs.

**Step 5: BRACKET OPENING (challenger / inertia-advocate)**
- State the null hypothesis: what the team does today instead of building this, and
  why that is acceptable. This is the strongest-case argument for not proceeding.
- Populate NH DIMENSION COMPARISON TABLE per §3: >= 3 dimensions, consistent scale,
  all three alternatives (A/B/C), compute Delta B-A and Delta B-C per dimension.
- Emit g_null(initial) as a labeled field derived from the table (not prose).
- Emit OVERRIDE INVOKED: NO (default -- may be changed to YES at BRACKET CLOSING only).
- Respond to relevant CH-IDs.
- Emit LOCAL GATE LEDGER ROW per §5.

**Step 6: DOMAIN REVIEWER SECTIONS** (one per role, manifest order)

For each role:
- State role name and lens in one sentence: "As a [role], I evaluate [lens concern]."
- Evaluate the artifact from this role's frame. Produce finding rows:
  `| Severity | Surface | Finding | Recommendation |`
- Respond to CH-IDs relevant to this role.
- Emit LOCAL GATE LEDGER ROW per §5. Section Severity = worst(finding severities) per §16.

**Step 7: CH-ID SATURATION CHECK**
- Verify SATURATED tier: every CH-ID has >= 1 domain section response.
- Emit g_null(post-domain) as a labeled field per §4 Stage 2 formula.
- No gate ledger row (§6).

**Step 8: LIFECYCLE REVIEWER SECTION**
- Apply the lifecycle lens: evaluate through operational lifecycle phases (creation,
  active use, change, deprecation, removal). Surface findings specific to lifecycle
  transitions, operational obligations, long-term maintenance costs.
- Produce finding rows (same format as Step 6).
- Respond to relevant CH-IDs.
- Emit LOCAL GATE LEDGER ROW per §5 with g_lifecycle labeled.

**Step 9: BRACKET CLOSING (challenger, post-domain)**
- Receive G_domain_agg (per §13), g_lifecycle, all domain gate verdicts as labeled inputs.
- Re-populate NH Dimension Comparison Table columns B and C with revised values
  (reflecting domain and lifecycle evidence received).
- Derive g_null(final) from revised table per §3 formula (Stage 3 of §4).
- Emit OVERRIDE INVOKED: YES | NO as labeled field.
- Emit LOCAL GATE LEDGER ROW per §5.

**Step 10: SCOPE COVERAGE RECONCILIATION** (per §15; no gate ledger row)

**Step 11: LENS COVERAGE TABLE** (per §14; no gate ledger row)
Populate from LENS APPLICABILITY PRE-REGISTRATION values. Flag any deviation
from pre-committed Applicability with justification.

**Step 12: DOMAIN COVERAGE GAP-CHECK** (per §14; no gate ledger row)
Run for every artifact domain from SCOPE DECLARATION.

**Step 13: DISPOSITION**
- Apply §1 DISPOSITION ALGEBRA to all gate verdicts.
- Emit `DISPOSITION: READY | CONDITIONAL | BLOCKED` as labeled field.
- Emit `Primary Driver: [value]` per §17.

**Step 14: MASTER ACTION REGISTER**
Copy all LOCAL GATE LEDGER ROWS verbatim (§7). Append ADVISORY-OPEN-LENS items
(HIGH-applicability OPEN entries from step 11), ADVISORY-GAP items from step 12,
and ADVISORY-GAP items from step 10. Do not re-derive Gate Verdict or Class.

**Step 15: CROSS-ROLE SIGNALS**
Synthesis narrative integrating findings across roles. Name >= 1 cross-role
conflict or convergence. Reference g_null progression through all three stages
(initial, post-domain, final). Explain the disposition rather than restating it.

---

## V-02

**Axis**: Lifecycle emphasis -- DOMAIN COVERAGE GAP-CHECK promoted to a first-class
numbered step in the SECTION ORDER CONTRACT (step 11); §14 ROLE LENS EXHAUSTION
PROTOCOL references step 11 rather than hosting the gap-check behavior

**Hypothesis**: R18's C-34 enforcement placed the DOMAIN COVERAGE GAP-CHECK as a
behavioral mandate within §13's text ("immediately after the LENS COVERAGE TABLE,
run a mandatory DOMAIN COVERAGE GAP-CHECK"). The lifecycle emphasis axis tests
whether C-34 is more robustly enforced when the gap-check is a numbered step in the
SECTION ORDER CONTRACT (§8), structurally parallel to the LENS COVERAGE TABLE,
DISPOSITION, and MASTER ACTION REGISTER. If the gap-check has its own section
number, omitting it is a section-order violation, not just a §13 behavioral
violation. The structural mandate operates independently of any §13 text. C-33 via
§14 (behavioral contract). C-35 via §3. Predicted: 225/225 with C-34 enforced by
section order rather than behavioral text.

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
FAIL -> BLOCKED | >= 1 CONDITIONAL, no FAIL -> CONDITIONAL | All PASS -> READY
```
OVERRIDE: BRACKET CLOSING only, labeled OVERRIDE INVOKED: YES | NO + justification.

---

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (skip if none).
No editorial class assignment at assembly time.

---

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23, C-35)**

The challenger's null hypothesis evaluation MUST use a structured NH DIMENSION
COMPARISON TABLE. Three alternatives required (Status Quo / Proposed Build /
Best-Non-Build-Alt). Required table format at BRACKET OPENING:
```
| Dimension | A: Status Quo | B: Proposed Build | C: Best Non-Build Alt | Delta B-A | Delta B-C |
```
Minimum 3 dimensions, consistent scale. Null hypothesis verdict derivable from
table alone:
```
g_null = PASS        if delta_B_A > 0 AND delta_B_C > 0
g_null = CONDITIONAL if exactly one delta > 0
g_null = FAIL        if delta_B_A <= 0 AND delta_B_C <= 0
```
Prose evaluation of the null hypothesis is invalid as a substitute for the table.
The challenger may add prose testimony after the table; the table governs g_null.
BRACKET CLOSING re-populates columns B and C; g_null(final) derives from revised
table per the same formula.

---

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
```
Stage 1: g_null(initial)     [BRACKET OPENING -- from NH table]
Stage 2: g_null(post-domain) [CH-ID SATURATION CHECK -- formula over G_domain_agg]
         G_domain_agg = FAIL: holds | PASS: weakens one tier | CONDITIONAL: CONDITIONAL
Stage 3: g_null(final)       [BRACKET CLOSING -- same substituting G_lifecycle]
```
GClose = g_null(final) or OVERRIDE INVOKED: YES with justification.

---

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21, C-25)**

Universal coverage: BRACKET OPENING, all DOMAIN sections, LIFECYCLE section,
BRACKET CLOSING each emit exactly one LOCAL GATE LEDGER ROW:
```
| Gate Verdict | Section Severity | Class | Finding References |
```
Non-verdict sections emit no row. MASTER ACTION REGISTER assembled by verbatim copy.

---

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**

No gate ledger row from: SCOPE DECLARATION, CH-ID REGISTRATION TABLE,
CH-ID SATURATION CHECK, SCOPE COVERAGE RECONCILIATION, LENS COVERAGE TABLE,
DOMAIN COVERAGE GAP-CHECK.

---

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**
Assembly: verbatim copy only. Re-derivation prohibited. Local row is authority.

---

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
1.  SCOPE DECLARATION
2.  CH-ID REGISTRATION TABLE
3.  BRACKET OPENING (challenger / inertia-advocate)
4.  DOMAIN REVIEWER SECTIONS (one per role, manifest order)
5.  CH-ID SATURATION CHECK
6.  LIFECYCLE REVIEWER SECTION
7.  BRACKET CLOSING (challenger, post-domain)
8.  SCOPE COVERAGE RECONCILIATION
9.  LENS COVERAGE TABLE
10. DOMAIN COVERAGE GAP-CHECK
11. DISPOSITION + PRIMARY DRIVER
12. MASTER ACTION REGISTER
13. CROSS-ROLE SIGNALS
```
Steps 9 and 10 are independent numbered sections. Step 10 (DOMAIN COVERAGE GAP-CHECK)
is a required section; omitting it is a section-order violation equivalent to
omitting step 9 (LENS COVERAGE TABLE) or step 11 (DISPOSITION). LIFECYCLE (step 6)
executes before BRACKET CLOSING (step 7).

---

**§9 CH-ID CHALLENGE REGISTRATION (C-04, C-05)**
Before BRACKET OPENING, register all challenges:
```
| CH-ID | Challenge Statement | Bracket Opening | [Domain roles...] | Lifecycle | Bracket Closing |
```
Every reviewer section carries a CH-ID response table.

---

**§10 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED: every CH-ID >= 1 DOMAIN response (before LIFECYCLE).
FULLY SATURATED: domain + lifecycle (at BRACKET CLOSING).
BRACKET CLOSING PASS blocked when UNSATURATED without waiver.

---

**§11 LIFECYCLE VERDICT INTEGRATION CONTRACT (C-22)**
LIFECYCLE (step 6) executes before BRACKET CLOSING (step 7). BRACKET CLOSING
receives `Lifecycle verdict received: g_lifecycle = [value]` as labeled input.

---

**§12 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(all DOMAIN gate verdicts). FAIL < CONDITIONAL < PASS.
Labeled input to BRACKET CLOSING for §4 Stage 2 application.

---

**§13 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-BRACKET CLOSING: SCOPE COVERAGE RECONCILIATION maps every IN-SCOPE surface
to findings. GAP surfaces -> ADVISORY-GAP, LOW severity, appended to action register.
No gate row.

---

**§14 ROLE LENS EXHAUSTION PROTOCOL (C-31, C-33)** [IMMUTABLE]

Step 9 (LENS COVERAGE TABLE): For each active reviewer role from .roles/,
every `lens.verify` entry must appear in the table. Row schema:
```
| Reviewer Role | Lens Dimension | Applicability | Status | Finding Reference(s) |
```

**Applicability field (C-33)**: Every row MUST carry an Applicability rating of HIGH,
MEDIUM, or LOW. This rating is artifact-specific: it reflects how central this lens
dimension is to the artifact under review, assigned at lens table population time.
The same role reviewing a different artifact may carry different ratings. Omitting
the Applicability field from any row is a protocol violation. The Applicability
rating is the basis for ADVISORY-OPEN-LENS promotion: HIGH-applicability rows with
Status=OPEN become ADVISORY-OPEN-LENS items in the MASTER ACTION REGISTER.

Step 10 (DOMAIN COVERAGE GAP-CHECK): Per §8 SECTION ORDER CONTRACT, step 10 is a
required independent section. For every artifact domain from the SCOPE DECLARATION,
determine whether any reviewer carries HIGH Applicability for a lens dimension
covering that domain. Domains with no HIGH-applicability coverage: classify as
ADVISORY-GAP. Emit per-domain classification. ADVISORY-GAP domains are appended
to the MASTER ACTION REGISTER with: domain name, reason (no HIGH-applicability
reviewer), recommended mitigation. Completing step 9 without executing step 10 is
a section-order violation.

---

**§15 PER-FINDING SEVERITY CHAIN (C-30)** [IMMUTABLE]
Section Severity = worst(individual finding severities). HIGH > MEDIUM > LOW.
Every finding row carries individual Severity. No editorial section-level assignment.

---

**§16 PRIMARY DRIVER DERIVATION (C-32)** [IMMUTABLE]
First-match precedence:
BRACKET CLOSING OVERRIDE > NULL HYPOTHESIS > DOMAIN [first FAIL] > LIFECYCLE [FAIL] >
DOMAIN [first CONDITIONAL] > LIFECYCLE [CONDITIONAL] > CONSENSUS.
Emit `Primary Driver: [value]` at DISPOSITION.

---

**§17 INPUT VARIABLE CONTRACTS (C-08, C-13, C-15)**
Variables: `{{artifact_id}}`, `{{depth}}`, `{{reviewer_set}}`.
deep: all roles | standard: relevant + rationale | quick: >= 3 + abbreviation note.
Output acknowledges all three values explicitly.

---

### EXECUTION

Steps 1-13 (acknowledge inputs; scope declaration; CH-ID registration; bracket
opening with NH table; domain reviewer sections; CH-ID saturation check; lifecycle
reviewer section; bracket closing; scope coverage reconciliation; lens coverage
table; domain coverage gap-check; disposition; master action register; cross-role
signals) follow the SECTION ORDER CONTRACT (§8 steps 1-13). Step 10 (DOMAIN COVERAGE
GAP-CHECK) executes as a required independent section after step 9 (LENS COVERAGE
TABLE) and before step 11 (DISPOSITION). Its output feeds into the MASTER ACTION
REGISTER at step 12.

---

## V-03

**Axis**: Phrasing register -- declarative type definitions and explicit deviation
cases throughout; §3 NH table contract includes a primacy deviation case; §14 lens
protocol uses TYPED FIELD definitions with domain constraints for Applicability

**Hypothesis**: R18 used imperative phrasing for C-33/C-34/C-35 enforcement ("must
carry", "is required", "is mandatory", "is a protocol violation"). Imperative phrasing
relies on the model treating prohibition statements as behavioral contracts. The
phrasing register axis tests whether declarative type definitions with explicit
deviation cases produce more consistent behavior. A type definition specifies WHAT
a field is and its valid domain (not just whether it is required); a deviation case
specifies the exact condition under which the stated behavior is violated and what
happens. C-35: the NH Dimension Comparison Table type definition includes a PRIMACY
DEVIATION CASE -- "if prose narrative yields a different g_null than the table formula,
the table governs; the prose deviation is flagged as a narrative-table mismatch."
C-33: Applicability is defined as a TYPED FIELD: domain={HIGH,MEDIUM,LOW},
constraint=artifact-specific, immutable-after-population. C-34: DOMAIN COVERAGE
GAP-CHECK is defined as a MANDATORY OPERATION with a single exception class (all
domains HIGH-covered). Predicted: 225/225 with tightest type-system enforcement.

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

Type: disposition-verdict. Domain: {READY, CONDITIONAL, BLOCKED}.
Derivation rule:
```
input: gate-verdict-vector = [v1, v2, ..., vn] where each vi in {FAIL, CONDITIONAL, PASS}
if FAIL in vector     -> BLOCKED
if CONDITIONAL in vector AND FAIL not in vector -> CONDITIONAL
if all PASS           -> READY
```
Override type: BRACKET-CLOSING-OVERRIDE. Activates only at BRACKET CLOSING.
Form: labeled field `OVERRIDE INVOKED: YES | NO` with justification string.
Deviation case: BLOCKED disposition without OVERRIDE INVOKED: YES in output
is a disposition-derivation error.

---

**§2 CLASS DERIVATION CONTRACT (C-12)**

Type: action-item-class. Domain: {BLOCKED, CONDITIONAL, ADVISORY}.
Derivation: BLOCKED <- FAIL; CONDITIONAL <- CONDITIONAL; ADVISORY <- PASS.
Constraint: class is read-only after local gate ledger row emission.
Deviation case: editorial re-assignment of class at action register assembly time
is a class-derivation error.

---

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23, C-35)**

Type definition: NH-DIMENSION-COMPARISON-TABLE.
Schema:
```
| Dimension | A: Status Quo | B: Proposed Build | C: Best Non-Build Alt | Delta B-A | Delta B-C |
```
Field constraints:
- `Dimension`: string, artifact-specific evaluation axis. Minimum 3 rows.
- `A / B / C`: numeric score on a declared consistent scale (e.g., 1-10).
- `Delta B-A`: B minus A (sign-significant). `Delta B-C`: B minus C (sign-significant).
- Scale declaration: state the scale once above the table (e.g., "Scale: 1=worst, 10=best").

Type definition: g_null-verdict.
Derivation formula:
```
g_null = PASS        if delta_B_A > 0 AND delta_B_C > 0
g_null = CONDITIONAL if (delta_B_A > 0 XOR delta_B_C > 0)
g_null = FAIL        if delta_B_A <= 0 AND delta_B_C <= 0
```
Source of authority: the NH-DIMENSION-COMPARISON-TABLE values are the sole
authoritative input for g_null derivation.

**PRIMACY DEVIATION CASE (C-35)**: If prose testimony in BRACKET OPENING asserts a
g_null verdict that differs from the formula applied to the table values, the table
formula governs. The discrepancy is flagged: `NH-NARRATIVE-TABLE-MISMATCH: prose
asserts [X]; table formula derives [Y]; table governs.` This deviation case is binding
at both BRACKET OPENING (initial) and BRACKET CLOSING (final).

Usage: emitted at BRACKET OPENING (initial table) and BRACKET CLOSING (revised
columns B and C, revised g_null(final)).

---

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**

Type: g_null-stage-progression.
Stages:
```
Stage 1: g_null(initial)     = output of NH-DIMENSION-COMPARISON-TABLE at BRACKET OPENING
Stage 2: g_null(post-domain) = apply G_domain_agg adjustment rule to g_null(initial)
         Adjustment rule:
           G_domain_agg = FAIL:        g_null(post-domain) = g_null(initial) [challenger holds]
           G_domain_agg = PASS:        g_null(post-domain) = weaken(g_null(initial)) by one tier
           G_domain_agg = CONDITIONAL: g_null(post-domain) = CONDITIONAL
Stage 3: g_null(final)       = apply G_lifecycle adjustment rule to g_null(post-domain)
         Adjustment rule: same substituting G_lifecycle for G_domain_agg
```
Output at CH-ID SATURATION CHECK: `g_null(post-domain) = [value]` (labeled field).
Output at BRACKET CLOSING: GClose = g_null(final), or OVERRIDE INVOKED: YES + justification.

---

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21, C-25)**

Type: gate-ledger-row. Schema:
```
| Gate Verdict | Section Severity | Class | Finding References |
```
Emission rule: one row per verdict-emitting section (BRACKET OPENING, each DOMAIN
section, LIFECYCLE section, BRACKET CLOSING). Non-verdict sections: no row (see §6).
Constraint: gate-ledger-row is immutable after emission. Class field set per §2 rule.

---

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**

Section type: non-verdict-section. Members: SCOPE DECLARATION, CH-ID REGISTRATION
TABLE, CH-ID SATURATION CHECK, SCOPE COVERAGE RECONCILIATION, LENS COVERAGE TABLE,
DOMAIN COVERAGE GAP-CHECK. Constraint: non-verdict-sections emit no gate-ledger-row.

---

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**

MASTER ACTION REGISTER assembly operation: COPY-VERBATIM from all gate-ledger-rows.
Prohibited operation: re-derivation of Gate Verdict or Class at assembly time.
Deviation case: any MASTER ACTION REGISTER row whose Gate Verdict or Class differs
from its source gate-ledger-row is an assembly error.

---

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
1.  SCOPE DECLARATION
2.  CH-ID REGISTRATION TABLE
3.  BRACKET OPENING
4.  DOMAIN REVIEWER SECTIONS (manifest order)
5.  CH-ID SATURATION CHECK
6.  LIFECYCLE REVIEWER SECTION
7.  BRACKET CLOSING
8.  SCOPE COVERAGE RECONCILIATION
9.  LENS COVERAGE TABLE
10. DOMAIN COVERAGE GAP-CHECK
11. DISPOSITION + PRIMARY DRIVER
12. MASTER ACTION REGISTER
13. CROSS-ROLE SIGNALS
```
Constraint: section order is immutable. A section that executes before its
predecessor is a section-order error.

---

**§9 CH-ID CHALLENGE REGISTRATION (C-04, C-05)**

Type: CH-ID-registration-table. Schema:
```
| CH-ID | Challenge Statement | Bracket Opening | [Domain roles...] | Lifecycle | Bracket Closing |
```
Registration rule: all CH-IDs populated before BRACKET OPENING. Response columns
populated during execution. Every reviewer section includes a CH-ID response sub-table.

---

**§10 CH-ID SATURATION REQUIREMENT (C-27)**

Type: saturation-state. Domain: {UNSATURATED, SATURATED, FULLY-SATURATED}.
SATURATED: every CH-ID has >= 1 DOMAIN section response.
FULLY-SATURATED: every CH-ID has DOMAIN + LIFECYCLE response.
Constraint: BRACKET CLOSING gate verdict = PASS is invalid when saturation-state =
UNSATURATED, unless an explicit waiver with justification is recorded.

---

**§11 LIFECYCLE VERDICT INTEGRATION CONTRACT (C-22)**

Ordering constraint: LIFECYCLE section (step 6) precedes BRACKET CLOSING (step 7).
BRACKET CLOSING input declaration: `Lifecycle verdict received: g_lifecycle = [value]`
as a labeled field before g_null(final) derivation.

---

**§12 DOMAIN-AGGREGATE FORMULA (C-24)**

Type: G_domain_agg. Derivation: median of all DOMAIN gate verdicts, where
FAIL < CONDITIONAL < PASS. BRACKET CLOSING input: labeled field
`G_domain_agg = [value]`.

---

**§13 SCOPE COVERAGE GATE PROTOCOL (C-29)**

Operation type: SCOPE-COVERAGE-RECONCILIATION. Executes at step 8.
For each IN-SCOPE surface: classify as COVERED (>= 1 finding) or GAP (no finding).
GAP surfaces: ADVISORY-GAP type, LOW severity, appended to MASTER ACTION REGISTER.
Constraint: emits no gate-ledger-row (non-verdict-section per §6).

---

**§14 ROLE LENS EXHAUSTION PROTOCOL (C-31, C-33, C-34)** [IMMUTABLE]

**LENS COVERAGE TABLE (step 9)**: For each active reviewer role from .roles/,
every `lens.verify` entry in the role definition appears in the table. Schema:
```
| Reviewer Role | Lens Dimension | Applicability | Status | Finding Reference(s) |
```

**TYPED FIELD: Applicability (C-33)**
- Type: applicability-rating. Domain: {HIGH, MEDIUM, LOW}.
- Constraint 1 (artifact-specific): the rating reflects this artifact's domain and
  scope, not the role's generic capability. The same role applied to a different
  artifact may carry different ratings.
- Constraint 2 (population-time): the rating is assigned when the lens table is
  built (step 9), not before and not after.
- Constraint 3 (completeness): every lens table row carries a populated
  applicability-rating value. A row without an Applicability value is a
  schema-completeness error.
- Constraint 4 (immutability): after lens table population, Applicability values are
  read-only. Retrospective changes require a flagged amendment with justification.
- Derivation rule: HIGH-applicability rows with Status=OPEN -> ADVISORY-OPEN-LENS
  item in MASTER ACTION REGISTER (lens dimension + role + reason OPEN).

**MANDATORY OPERATION: DOMAIN COVERAGE GAP-CHECK (C-34)**
- Operation class: mandatory (no conditional execution; executes after step 9 as
  step 10 per §8 SECTION ORDER CONTRACT).
- Input: artifact domain list from SCOPE DECLARATION; Applicability column from
  LENS COVERAGE TABLE.
- Procedure: for each artifact domain, determine whether at least one reviewer has
  HIGH applicability for a lens dimension covering that domain.
- Output rule: covered domains (>= 1 HIGH-applicability reviewer): emit COVERED.
  Uncovered domains: classify as ADVISORY-GAP. Append to MASTER ACTION REGISTER:
  domain name, reason (no HIGH-applicability reviewer found), recommended mitigation.
- Exception class: exactly one exception exists: "all artifact domains are covered
  at HIGH applicability." In this case emit: `DOMAIN COVERAGE GAP-CHECK: all domains
  covered at HIGH applicability. No ADVISORY-GAP items.`
- Deviation case: omitting the DOMAIN COVERAGE GAP-CHECK when >= 1 artifact domain
  exists is a section-completeness error.

---

**§15 PER-FINDING SEVERITY CHAIN (C-30)** [IMMUTABLE]

Type: section-severity. Derivation: worst(individual finding severity values in section).
Ordering: HIGH > MEDIUM > LOW. Every finding row carries individual Severity.
Constraint: editorial section-level severity assignment is a severity-derivation error.

---

**§16 PRIMARY DRIVER DERIVATION (C-32)** [IMMUTABLE]

Type: primary-driver. Derivation: first-match over gate-verdict-vector.
```
Precedence:
1. BRACKET-CLOSING-OVERRIDE activated      -> BRACKET CLOSING OVERRIDE
2. BRACKET OPENING verdict = FAIL          -> NULL HYPOTHESIS
3. Any DOMAIN verdict = FAIL (first match) -> DOMAIN [role name]
4. LIFECYCLE verdict = FAIL                -> LIFECYCLE
5. Any DOMAIN verdict = CONDITIONAL (first)-> DOMAIN [role name]
6. LIFECYCLE verdict = CONDITIONAL         -> LIFECYCLE
7. All verdicts = PASS                     -> CONSENSUS
```
Output: labeled field `Primary Driver: [value]` at DISPOSITION.

---

**§17 INPUT VARIABLE CONTRACTS (C-08, C-13, C-15)**

Type: input-variable. Members: `{{artifact_id}}`, `{{depth}}`, `{{reviewer_set}}`.
Depth rules: deep -> all roles; standard -> relevant roles + selection rationale;
quick -> >= 3 highest-priority roles + abbreviation note.
Output constraint: explicit acknowledgment block emitting all three values.

---

### EXECUTION

Steps 1-13 follow §8 SECTION ORDER CONTRACT. At each step, apply the type definitions
and deviation cases from the relevant §§ contracts. BRACKET OPENING applies the
NH-DIMENSION-COMPARISON-TABLE type definition and the PRIMACY DEVIATION CASE for
g_null. DOMAIN reviewer sections apply the finding row schema with individual Severity.
Step 9 applies the TYPED FIELD Applicability constraints. Step 10 applies the
MANDATORY OPERATION DOMAIN COVERAGE GAP-CHECK with its single exception class.
All deviation cases are binding: flag them as named errors if encountered.

---

## V-04

**Axis**: Role sequence + Lifecycle emphasis (two-axis) -- V-01's LENS APPLICABILITY
PRE-REGISTRATION step (C-33 via structural pre-commitment before reviewers run)
combined with V-02's DOMAIN COVERAGE GAP-CHECK as a numbered step in the SECTION
ORDER CONTRACT (C-34 via section-order mandate)

**Hypothesis**: V-01 achieves C-33 by making Applicability ratings a pre-committed
step (step 2 in V-01's section order) before any reviewer runs. V-02 achieves C-34
by making the gap-check a required numbered step in the section order. V-04 combines
both: Applicability is committed before reviewers run AND the gap-check has its own
section number. The two axes address C-33 and C-34 through structural ordering alone,
independent of §14's behavioral text. C-35 via §3 NH table. V-04 tests whether
dual-axis structural enforcement outperforms behavioral text enforcement for these
two criteria. Predicted: 225/225, strongest structural mandate for C-33/C-34.

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
FAIL -> BLOCKED | >= 1 CONDITIONAL, no FAIL -> CONDITIONAL | All PASS -> READY
```
OVERRIDE: labeled OVERRIDE INVOKED: YES | NO at BRACKET CLOSING.

---

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY. No editorial assignment.

---

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23, C-35)**

NH DIMENSION COMPARISON TABLE required at BRACKET OPENING. Three alternatives
(Status Quo / Proposed Build / Best-Non-Build-Alt). Format:
```
| Dimension | A: Status Quo | B: Proposed Build | C: Best Non-Build Alt | Delta B-A | Delta B-C |
```
Minimum 3 dimensions, consistent scale. g_null derivable from table alone:
```
g_null = PASS if both deltas > 0 | CONDITIONAL if one > 0 | FAIL if both <= 0
```
Prose evaluation is invalid as a substitute. Table governs g_null.
BRACKET CLOSING re-populates B/C; g_null(final) from revised table.

---

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
```
Stage 1: g_null(initial) [BRACKET OPENING]
Stage 2: g_null(post-domain) [CH-ID SATURATION CHECK, G_domain_agg adjustment]
Stage 3: g_null(final) [BRACKET CLOSING, G_lifecycle adjustment]
```
GClose = g_null(final) or OVERRIDE.

---

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21, C-25)**
Universal: BRACKET OPENING, DOMAIN sections, LIFECYCLE, BRACKET CLOSING emit one row:
```
| Gate Verdict | Section Severity | Class | Finding References |
```
Non-verdict sections: no row. MASTER ACTION REGISTER: verbatim copy of all rows.

---

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate row: SCOPE DECLARATION, LENS APPLICABILITY PRE-REGISTRATION, CH-ID
REGISTRATION TABLE, CH-ID SATURATION CHECK, SCOPE COVERAGE RECONCILIATION,
LENS COVERAGE TABLE, DOMAIN COVERAGE GAP-CHECK.

---

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**
Verbatim copy only. Re-derivation of Gate Verdict or Class at assembly time: prohibited.

---

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
1.  SCOPE DECLARATION
2.  LENS APPLICABILITY PRE-REGISTRATION         [C-33 structural commitment]
3.  CH-ID REGISTRATION TABLE
4.  BRACKET OPENING
5.  DOMAIN REVIEWER SECTIONS (manifest order)
6.  CH-ID SATURATION CHECK
7.  LIFECYCLE REVIEWER SECTION
8.  BRACKET CLOSING
9.  SCOPE COVERAGE RECONCILIATION
10. LENS COVERAGE TABLE
11. DOMAIN COVERAGE GAP-CHECK                   [C-34 structural mandate]
12. DISPOSITION + PRIMARY DRIVER
13. MASTER ACTION REGISTER
14. CROSS-ROLE SIGNALS
```
LENS APPLICABILITY PRE-REGISTRATION (step 2): must complete before CH-ID REGISTRATION
(step 3) and BRACKET OPENING (step 4). Applicability ratings declared here are binding
for the LENS COVERAGE TABLE at step 10.
DOMAIN COVERAGE GAP-CHECK (step 11): independent required section. Executing step 10
without executing step 11 is a section-order violation.

---

**§9 LENS APPLICABILITY PRE-REGISTRATION PROTOCOL (C-33)** [IMMUTABLE]

Step 2 output. For every active reviewer role, every `lens.verify` entry:
```
| Reviewer Role | Lens Dimension | Pre-Committed Applicability |
```
Applicability domain: {HIGH, MEDIUM, LOW}. Artifact-specific. Immutable after
pre-registration. The LENS COVERAGE TABLE at step 10 inherits these values.
HIGH-applicability entries govern ADVISORY-OPEN-LENS promotion at step 10.

---

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-05)**
Before BRACKET OPENING:
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
LIFECYCLE precedes BRACKET CLOSING. BRACKET CLOSING input:
`Lifecycle verdict received: g_lifecycle = [value]`.

---

**§13 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(all DOMAIN gate verdicts). Labeled input to BRACKET CLOSING.

---

**§14 ROLE LENS EXHAUSTION PROTOCOL (C-31, C-34)** [IMMUTABLE]

Step 10 (LENS COVERAGE TABLE): Row schema:
```
| Reviewer Role | Lens Dimension | Applicability | Status | Finding Reference(s) |
```
Applicability inherited from step 2 pre-registration (§9). Deviations flagged.
HIGH-applicability OPEN entries -> ADVISORY-OPEN-LENS in MASTER ACTION REGISTER.

Step 11 (DOMAIN COVERAGE GAP-CHECK): Required section (§8 SECTION ORDER CONTRACT).
Enumerate every artifact domain from SCOPE DECLARATION. For each domain: check
whether any reviewer has HIGH Applicability for a covering lens dimension. Uncovered
domains -> ADVISORY-GAP. Append to MASTER ACTION REGISTER: domain, reason, mitigation.
Emit: `DOMAIN COVERAGE GAP-CHECK: [covered count] covered | [gap count] ADVISORY-GAP`

---

**§15 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-BRACKET CLOSING: SCOPE COVERAGE RECONCILIATION. GAP surfaces -> ADVISORY-GAP.
No gate row.

---

**§16 PER-FINDING SEVERITY CHAIN (C-30)** [IMMUTABLE]
Section Severity = worst(individual finding severities). No editorial assignment.

---

**§17 PRIMARY DRIVER DERIVATION (C-32)** [IMMUTABLE]
BRACKET CLOSING OVERRIDE > NULL HYPOTHESIS > DOMAIN [first FAIL] > LIFECYCLE [FAIL] >
DOMAIN [first CONDITIONAL] > LIFECYCLE [CONDITIONAL] > CONSENSUS.
Emit `Primary Driver: [value]` at DISPOSITION.

---

**§18 INPUT VARIABLE CONTRACTS (C-08, C-13, C-15)**
Variables: `{{artifact_id}}`, `{{depth}}`, `{{reviewer_set}}`.
Acknowledge all three explicitly. Depth governs role selection.

---

### EXECUTION

**Step 1**: Acknowledge inputs.

**Step 2**: SCOPE DECLARATION -- enumerate IN-SCOPE and OUT-OF-SCOPE surfaces.

**Step 3**: LENS APPLICABILITY PRE-REGISTRATION (§9) -- pre-commit Applicability
ratings for every active reviewer's lens dimensions. Table must be complete before
step 4 (CH-ID REGISTRATION TABLE).

**Step 4**: CH-ID REGISTRATION TABLE -- register all challenges (§10).

**Step 5**: BRACKET OPENING -- null hypothesis + NH DIMENSION COMPARISON TABLE
per §3; g_null(initial) as labeled field; CH-ID responses; LOCAL GATE LEDGER ROW.

**Step 6**: DOMAIN REVIEWER SECTIONS -- one per role, manifest order. Each emits
finding rows, CH-ID responses, LOCAL GATE LEDGER ROW.

**Step 7**: CH-ID SATURATION CHECK -- verify SATURATED; emit g_null(post-domain).

**Step 8**: LIFECYCLE REVIEWER SECTION -- lifecycle lens; finding rows; CH-ID
responses; LOCAL GATE LEDGER ROW.

**Step 9**: BRACKET CLOSING -- receive G_domain_agg + g_lifecycle; re-populate
NH table columns B/C; derive g_null(final); OVERRIDE INVOKED field;
LOCAL GATE LEDGER ROW.

**Step 10**: SCOPE COVERAGE RECONCILIATION (§15).

**Step 11**: LENS COVERAGE TABLE (§14) -- inherit Applicability from step 3 pre-registration.

**Step 12**: DOMAIN COVERAGE GAP-CHECK (§14) -- required section; run against
all artifact domains; emit ADVISORY-GAP items.

**Step 13**: DISPOSITION -- §1 algebra; Primary Driver per §17.

**Step 14**: MASTER ACTION REGISTER -- verbatim copy of all LOCAL GATE LEDGER ROWS;
append ADVISORY-OPEN-LENS (from step 11), ADVISORY-GAP from step 12, ADVISORY-GAP
from step 10.

**Step 15**: CROSS-ROLE SIGNALS -- cross-role synthesis; g_null progression narrative.

---

## V-05

**Axis**: Role sequence + Lifecycle emphasis + Phrasing register (three-axis) --
V-01's LENS APPLICABILITY PRE-REGISTRATION (structural pre-commitment, C-33) +
V-02's DOMAIN COVERAGE GAP-CHECK as numbered step (section-order mandate, C-34) +
V-03's declarative type definitions with deviation cases (C-35 PRIMACY DEVIATION CASE,
C-33 TYPED FIELD, C-34 MANDATORY OPERATION)

**Hypothesis**: The three R19 axes independently target C-33, C-34, and C-35 through
distinct structural mechanisms. V-05 combines all three: Applicability is
pre-committed as a first-class step before reviewers run (role sequence); the
gap-check is numbered in the section order (lifecycle emphasis); and all three
criteria are backed by type definitions and explicit deviation cases that name error
conditions precisely (phrasing register). The combination creates triple-layer
enforcement: structural ordering commits Applicability early (no forgetting), section
order mandates the gap-check at the right moment (no elision), and type definitions
make deviation conditions auditable by name. C-35's PRIMACY DEVIATION CASE handles
the specific failure mode where prose narrative and table produce different g_null
values. Predicted: 225/225, maximum multi-layer reinforcement for C-33/C-34/C-35.

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

Type: disposition-verdict. Domain: {READY, CONDITIONAL, BLOCKED}. Derivation:
```
FAIL in gate-verdict-vector     -> BLOCKED
CONDITIONAL in vector, no FAIL  -> CONDITIONAL
All PASS                        -> READY
```
Override type: BRACKET-CLOSING-OVERRIDE. Form: `OVERRIDE INVOKED: YES | NO`.
Deviation case: BLOCKED without OVERRIDE INVOKED: YES is a disposition error.

---

**§2 CLASS DERIVATION CONTRACT (C-12)**

Type: action-item-class. Domain: {BLOCKED, CONDITIONAL, ADVISORY}.
Derivation: FAIL -> BLOCKED; CONDITIONAL -> CONDITIONAL; PASS -> ADVISORY.
Deviation case: editorial re-assignment at action register assembly time is a
class-derivation error.

---

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23, C-35)**

Type definition: NH-DIMENSION-COMPARISON-TABLE. Schema:
```
| Dimension | A: Status Quo | B: Proposed Build | C: Best Non-Build Alt | Delta B-A | Delta B-C |
```
Field constraints: Dimension is an artifact-specific evaluation axis. Minimum 3 rows.
A/B/C scores on a declared consistent scale (state scale above table). Delta fields
are signed (B minus A; B minus C).

Type definition: g_null-verdict. Derivation:
```
g_null = PASS        if delta_B_A > 0 AND delta_B_C > 0
g_null = CONDITIONAL if (delta_B_A > 0 XOR delta_B_C > 0)
g_null = FAIL        if delta_B_A <= 0 AND delta_B_C <= 0
```
Authority: NH-DIMENSION-COMPARISON-TABLE values are the sole input for g_null.

**PRIMACY DEVIATION CASE (C-35)**: If prose testimony in BRACKET OPENING or BRACKET
CLOSING asserts a g_null verdict that differs from the formula output, flag as:
`NH-NARRATIVE-TABLE-MISMATCH: prose asserts [X]; table formula derives [Y]; table
governs.` The table-derived g_null stands. The mismatch is noted in CROSS-ROLE SIGNALS.

Emitted at BRACKET OPENING (initial; g_null(initial)) and BRACKET CLOSING (revised
B/C columns; g_null(final)).

---

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**

Type: g_null-stage-progression.
```
Stage 1: g_null(initial) [BRACKET OPENING, NH table]
Stage 2: g_null(post-domain) [CH-ID SATURATION CHECK]
  G_domain_agg = FAIL:        g_null(post-domain) = g_null(initial)
  G_domain_agg = PASS:        g_null(post-domain) = weaken(g_null(initial)) one tier toward PASS
  G_domain_agg = CONDITIONAL: g_null(post-domain) = CONDITIONAL
Stage 3: g_null(final) [BRACKET CLOSING, same substituting G_lifecycle]
```
Output: g_null stage values as labeled fields at each stage.

---

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21, C-25)**

Type: gate-ledger-row. Schema:
```
| Gate Verdict | Section Severity | Class | Finding References |
```
Emission: one row per verdict-emitting section. Immutable after emission.

---

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**

Non-verdict sections (no gate-ledger-row): SCOPE DECLARATION, LENS APPLICABILITY
PRE-REGISTRATION, CH-ID REGISTRATION TABLE, CH-ID SATURATION CHECK, SCOPE COVERAGE
RECONCILIATION, LENS COVERAGE TABLE, DOMAIN COVERAGE GAP-CHECK.

---

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**

MASTER ACTION REGISTER: COPY-VERBATIM operation from all gate-ledger-rows.
Deviation case: re-derived Gate Verdict or Class in MASTER ACTION REGISTER is
an assembly error.

---

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
1.  SCOPE DECLARATION
2.  LENS APPLICABILITY PRE-REGISTRATION         [C-33: structural pre-commitment]
3.  CH-ID REGISTRATION TABLE
4.  BRACKET OPENING
5.  DOMAIN REVIEWER SECTIONS (manifest order)
6.  CH-ID SATURATION CHECK
7.  LIFECYCLE REVIEWER SECTION
8.  BRACKET CLOSING
9.  SCOPE COVERAGE RECONCILIATION
10. LENS COVERAGE TABLE
11. DOMAIN COVERAGE GAP-CHECK                   [C-34: numbered section mandate]
12. DISPOSITION + PRIMARY DRIVER
13. MASTER ACTION REGISTER
14. CROSS-ROLE SIGNALS
```
Section-order constraints:
- Step 2 before step 3 and before step 4: Applicability committed before reviewers run.
- Step 7 before step 8: LIFECYCLE before BRACKET CLOSING.
- Step 10 before step 11: LENS COVERAGE TABLE before DOMAIN COVERAGE GAP-CHECK.
- Step 11 before step 12: GAP-CHECK before DISPOSITION.
- Omitting any step is a section-order error.

---

**§9 LENS APPLICABILITY PRE-REGISTRATION PROTOCOL (C-33)** [IMMUTABLE]

Step 2 output. Typed field: Applicability. Domain: {HIGH, MEDIUM, LOW}.
Constraint 1 (artifact-specific): rating reflects this artifact, not role generic.
Constraint 2 (pre-committed): declared at step 2, before any reviewer section.
Constraint 3 (completeness): every reviewer's every lens.verify entry appears.
Constraint 4 (immutability): values are read-only after step 2 completes; amendments
require explicit flagging with justification.

Schema:
```
| Reviewer Role | Lens Dimension | Pre-Committed Applicability |
```

Downstream: LENS COVERAGE TABLE at step 10 inherits Applicability from this table.
HIGH-applicability entries define ADVISORY-OPEN-LENS promotion rule: HIGH + Status=OPEN
-> ADVISORY-OPEN-LENS item in MASTER ACTION REGISTER.

Deviation case: a lens table row at step 10 whose Applicability differs from the
pre-registered value without a flagged amendment is a pre-commitment violation.

---

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-05)**
Schema:
```
| CH-ID | Challenge Statement | Bracket Opening | [Domain roles...] | Lifecycle | Bracket Closing |
```
Registration before BRACKET OPENING (step 4). Every reviewer section includes
CH-ID response sub-table.

---

**§11 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED: every CH-ID >= 1 DOMAIN response. FULLY SATURATED: + LIFECYCLE.
Deviation case: BRACKET CLOSING gate = PASS when UNSATURATED without waiver
is a saturation violation.

---

**§12 LIFECYCLE VERDICT INTEGRATION CONTRACT (C-22)**
Ordering constraint: step 7 before step 8. BRACKET CLOSING input declaration:
`Lifecycle verdict received: g_lifecycle = [value]`.

---

**§13 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(DOMAIN gate verdicts). Labeled input at BRACKET CLOSING.

---

**§14 ROLE LENS EXHAUSTION PROTOCOL (C-31, C-34)** [IMMUTABLE]

**Step 10 (LENS COVERAGE TABLE)**: Schema:
```
| Reviewer Role | Lens Dimension | Applicability | Status | Finding Reference(s) |
```
Applicability: inherited from step 2 (§9). Deviation case: value mismatch without
flagged amendment is a pre-commitment violation. HIGH + OPEN -> ADVISORY-OPEN-LENS.

**Step 11 (DOMAIN COVERAGE GAP-CHECK)**:
- Operation class: MANDATORY-OPERATION. No conditional execution.
- Input: artifact domains from SCOPE DECLARATION; Applicability from step 10.
- Procedure: for each artifact domain, identify whether >= 1 reviewer has HIGH
  Applicability for a lens dimension covering that domain.
- Output rules:
  - Covered domains: emit `COVERED: [domain name]`.
  - Uncovered domains: emit `ADVISORY-GAP: [domain name] -- reason: no HIGH-applicability
    reviewer -- mitigation: [recommended action]`. Append to MASTER ACTION REGISTER.
- Exception class: "all domains covered" -> emit summary `DOMAIN COVERAGE GAP-CHECK:
  all artifact domains covered at HIGH applicability. No ADVISORY-GAP items generated.`
- Deviation case: omitting step 11 when >= 1 artifact domain exists is a
  section-completeness error per §8 SECTION ORDER CONTRACT.

---

**§15 SCOPE COVERAGE GATE PROTOCOL (C-29)**
SCOPE COVERAGE RECONCILIATION at step 9. GAP surfaces -> ADVISORY-GAP, LOW severity.
No gate-ledger-row.

---

**§16 PER-FINDING SEVERITY CHAIN (C-30)** [IMMUTABLE]

Type: section-severity. Derivation: worst(finding row Severity values).
Constraint: editorial section-level assignment is a severity-derivation error.

---

**§17 PRIMARY DRIVER DERIVATION (C-32)** [IMMUTABLE]

First-match over gate-verdict-vector:
```
1. BRACKET-CLOSING-OVERRIDE active -> BRACKET CLOSING OVERRIDE
2. BRACKET OPENING = FAIL          -> NULL HYPOTHESIS
3. Any DOMAIN = FAIL (first)       -> DOMAIN [role name]
4. LIFECYCLE = FAIL                -> LIFECYCLE
5. Any DOMAIN = CONDITIONAL (first)-> DOMAIN [role name]
6. LIFECYCLE = CONDITIONAL         -> LIFECYCLE
7. All PASS                        -> CONSENSUS
```
Output: `Primary Driver: [value]` at DISPOSITION.

---

**§18 INPUT VARIABLE CONTRACTS (C-08, C-13, C-15)**

Variables: `{{artifact_id}}`, `{{depth}}`, `{{reviewer_set}}`.
Depth rules: deep -> all; standard -> relevant + rationale; quick -> >= 3 + note.
Constraint: explicit acknowledgment block emitting all three values.

---

### EXECUTION

**Step 1**: Acknowledge inputs (all three variables, selection rationale if applicable).

**Step 2**: SCOPE DECLARATION -- enumerate IN-SCOPE and OUT-OF-SCOPE surfaces.

**Step 3**: LENS APPLICABILITY PRE-REGISTRATION (§9) -- for every active reviewer,
emit the pre-committed Applicability table. Apply constraint checks: artifact-specific,
complete coverage, immutable after this step.

**Step 4**: CH-ID REGISTRATION TABLE (§10) -- register all challenges.

**Step 5**: BRACKET OPENING -- state null hypothesis; populate NH DIMENSION COMPARISON
TABLE per §3 (>= 3 dimensions, all three alternatives, signed deltas); apply PRIMACY
DEVIATION CASE if prose and table diverge; emit g_null(initial) as labeled field;
OVERRIDE INVOKED: NO; CH-ID responses; LOCAL GATE LEDGER ROW.

**Step 6**: DOMAIN REVIEWER SECTIONS -- one per role, manifest order. Each: role
lens statement; finding rows with individual Severity; CH-ID response table; LOCAL
GATE LEDGER ROW (Section Severity = worst findings per §16).

**Step 7**: CH-ID SATURATION CHECK -- verify SATURATED; emit g_null(post-domain)
as labeled field per §4 Stage 2.

**Step 8**: LIFECYCLE REVIEWER SECTION -- lifecycle lens; finding rows; CH-ID responses;
LOCAL GATE LEDGER ROW with g_lifecycle labeled.

**Step 9**: BRACKET CLOSING -- receive G_domain_agg + g_lifecycle as labeled inputs;
re-populate NH table columns B/C with post-evidence values; apply PRIMACY DEVIATION
CASE if needed; derive g_null(final); OVERRIDE INVOKED field; LOCAL GATE LEDGER ROW.

**Step 10**: SCOPE COVERAGE RECONCILIATION (§15).

**Step 11**: LENS COVERAGE TABLE (§14 step 10) -- inherit Applicability from step 3;
flag pre-commitment deviations; ADVISORY-OPEN-LENS for HIGH + OPEN rows.

**Step 12**: DOMAIN COVERAGE GAP-CHECK (§14 step 11) -- MANDATORY-OPERATION; classify
all artifact domains; emit ADVISORY-GAP items; append to MASTER ACTION REGISTER.

**Step 13**: DISPOSITION -- §1 derivation; Primary Driver per §17.

**Step 14**: MASTER ACTION REGISTER -- COPY-VERBATIM of all LOCAL GATE LEDGER ROWS;
append ADVISORY-OPEN-LENS (step 11), ADVISORY-GAP (step 12), ADVISORY-GAP (step 10).

**Step 15**: CROSS-ROLE SIGNALS -- cross-role synthesis; g_null progression through
all three stages; NH-NARRATIVE-TABLE-MISMATCH notes if any; disposition explanation.
