---
skill: quest-variate
skill_target: org-review
date: 2026-03-17
round: 18
rubric: org-review-rubric-v11-2026-03-16.md
---

# org-review -- Variate R18 (rubric v11)

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis and three-axis combinations (V-04, V-05).

**R18 design target**: V-05 R11 scored 210/225 under v11 (C-33/C-34/C-35 absent). V-02 R12
is the canonical source at ~215/225 (C-33/C-34/C-35 PASS but v10-base criteria weaker than
V-05 R11). The R18 target is 225/225 -- V-05 R11's base (C-30+C-31+C-32 PASS) plus C-33/C-34/C-35
PASS simultaneously. No prior variant has achieved all six simultaneously.

**Gap analysis from V-05 R11 (210/225) and V-02 R12 (~215/225):**

| Criterion | V-05 R11 | V-02 R12 | What it requires |
|-----------|----------|----------|-----------------|
| C-33 LENS APPLICABILITY RATING | FAIL | PASS | Each LENS COVERAGE TABLE row carries artifact-specific HIGH/MEDIUM/LOW Applicability rating; schema pre-committed in preamble |
| C-34 ADVISORY-GAP DOMAIN COVERAGE | vacuous (C-33 FAIL) | PASS | Post-lens DOMAIN COVERAGE GAP-CHECK names every domain with no HIGH-applicability reviewer; each classified ADVISORY-GAP in action register |
| C-35 NH CHALLENGER DIMENSION TABLE | FAIL | PASS | Challenger NH evaluation uses a structured dimension comparison table; g_null derivable from table values alone; no prose-only evaluation permitted |

**Why V-02 R12 scores ~215 not 225**: V-02 R12 achieved C-33/C-34/C-35 but its C-16
(quantified bracket anchor with domain reviewer re-scoring) and possibly C-30/C-32 were
weaker than V-05 R11's architecture. V-05 R11's base has C-16+C-30+C-31+C-32 all PASS
through a deeply integrated bracket scaffold; V-02 R12 introduced the applicability and
table structures but introduced them in a variant (domain-first ordering) that compromised
other criteria. R18 must graft the three new criterion patterns onto V-05 R11's bracket
architecture without disturbing the existing PASS chain.

**R18 synthesis path**: C-35 requires the challenger's BRACKET OPENING to produce a
structured dimension comparison table. C-33 requires the LENS COVERAGE TABLE protocol
(§13) to declare an Applicability column schema before execution. C-34 requires a
DOMAIN COVERAGE GAP-CHECK contract following the lens table. Three independent structural
additions to V-05 R11's base -- none cascade into the others' failure modes.

**R18 variation axes:**

- V-01: Output format (single axis) -- a standalone LENS OUTPUT SCHEMA block pre-§§
  pre-declares the LENS COVERAGE TABLE row format (including Applicability column) and
  the DOMAIN COVERAGE GAP-CHECK mandate. §13 references this block. The format declaration
  makes the schema auditable independently of the §13 behavioral text. C-35 added via §3.

- V-02: Phrasing register (single axis) -- §13 expanded to a self-contained behavioral
  contract with independent enforcement paths for C-33 (applicability column as required
  field with violation conditions) and C-34 (gap-check as mandatory post-table step with
  ADVISORY-GAP promotion rule). No pre-§§ schema block. C-35 added via §3.

- V-03: Inertia framing (single axis) -- the BRACKET OPENING null hypothesis dimensions
  are pre-registered in the §3 NULL HYPOTHESIS DERIVATION RULE by having the prompt
  name the challenger's analysis frame (current-state vs proposed-state axis) before any
  section runs. C-35 strongest: dimensions are contractually anchored to the artifact
  scope declared at §1, not chosen ad hoc by the challenger at execution time. C-33/C-34
  addressed via §13 standard protocol with Applicability column.

- V-04: Output format + Phrasing register (two-axis) -- V-01's LENS OUTPUT SCHEMA block
  combined with V-02's dense behavioral §13. Dual enforcement path for C-33/C-34: schema
  declaration AND behavioral contract independently auditable.

- V-05: Output format + Phrasing register + Inertia framing (three-axis) -- all three
  patterns. LENS OUTPUT SCHEMA (V-01) + dense behavioral §13 (V-02) + challenger dimension
  pre-registration from artifact scope (V-03). Maximum inter-criterion reinforcement.

**R18 single-axis predictions:**
- V-01: C-33 PASS (schema block), C-34 PASS (schema block mandate), C-35 PASS (§3). Predicted: 225/225
- V-02: C-33 PASS (§13 behavioral), C-34 PASS (§13 behavioral), C-35 PASS (§3). Predicted: 225/225
- V-03: C-33 PASS (§13 with Applicability), C-34 PASS (§13 gap-check), C-35 PASS (strongest -- scope-anchored). Predicted: 225/225

**R18 two-axis and three-axis predictions:**
- V-04: 225/225, dual-path C-33/C-34 enforcement (schema + behavioral). C-35 via §3.
- V-05: 225/225, triple-path all criteria, scope-anchored C-35 strongest.

---

## V-01

**Axis**: Output format -- LENS OUTPUT SCHEMA pre-§§ block declares Applicability column
schema and DOMAIN COVERAGE GAP-CHECK mandate; §13 references block; C-35 via §3 NH table

**Hypothesis**: V-05 R11 had §13 ROLE LENS EXHAUSTION with ADDRESSED/OPEN classification
(C-31 PASS) but no Applicability column schema. C-33 fails because the lens table rows
had no per-artifact-specific HIGH/MEDIUM/LOW rating. C-34 was vacuous (no applicability
tier means no HIGH-applicability reviewer tier to gap-check against). The minimal fix for
C-33/C-34: pre-declare the lens table row schema -- including the Applicability field --
in a standalone structural block before the §§ contracts. V-01 uses the output format axis:
a LENS OUTPUT SCHEMA block structurally parallel to the §§ contracts declares the full
lens table format and mandates the gap-check. §13 references this block. The schema
declaration is independently auditable without reading §13's behavioral text. C-35 is
fixed by adding the NH dimension comparison table requirement to §3. Predicted: 225/225.

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

### LENS OUTPUT SCHEMA

Pre-committed lens coverage output format. All lens table rows and the post-table
gap-check conform to this schema. Binding before any reviewer section runs.

**LENS COVERAGE TABLE row schema:**
```
| Reviewer Role | Lens Dimension | Applicability | Status | Finding Reference(s) |
```

- `Reviewer Role`: name from .roles/.
- `Lens Dimension`: one `lens.verify` entry from that role's definition.
- `Applicability`: artifact-specific rating -- **HIGH**, **MEDIUM**, or **LOW**.
  - HIGH: this lens dimension is directly relevant to the artifact's domain and scope.
  - MEDIUM: relevant but not central to this artifact's primary risk surface.
  - LOW: tangential or minimally applicable to this artifact's context.
  Rating is assigned at lens table population time based on the actual artifact, not the
  generic role definition. The same role may carry different ratings in different reviews.
  The Applicability rating is the structural basis for the ADDRESSED/OPEN determination:
  a HIGH-applicability OPEN entry is a gap; a LOW-applicability OPEN entry is advisory only.
- `Status`: ADDRESSED (>= 1 finding references this dimension) or OPEN (no finding does).
- `Finding Reference(s)`: comma-separated finding citations for ADDRESSED entries; `--` if OPEN.

HIGH-applicability rows with Status = OPEN are promoted to ADVISORY-OPEN-LENS items in
the MASTER ACTION REGISTER (dimension name + role + reason OPEN).

**DOMAIN COVERAGE GAP-CHECK** (mandatory; runs immediately after LENS COVERAGE TABLE):
After building the LENS COVERAGE TABLE, enumerate every artifact domain identified in the
SCOPE DECLARATION. For each domain:
- Check whether any Reviewer Role carries HIGH Applicability for a Lens Dimension that
  covers this domain.
- If NO reviewer has HIGH applicability covering the domain: classify as ADVISORY-GAP.
  Promote to MASTER ACTION REGISTER: domain name + reason for gap + recommended mitigation.
If all domains are covered: emit `DOMAIN COVERAGE GAP-CHECK: all artifact domains covered
at HIGH applicability.`

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
```
HIGH = blocks commitment | MEDIUM = conditions commitment | LOW = advisory
If any gate verdict = FAIL                     -> DISPOSITION: BLOCKED
If no FAIL and >= 1 gate verdict = CONDITIONAL -> DISPOSITION: CONDITIONAL
If all gate verdicts = PASS                    -> DISPOSITION: READY
```
BLOCKED disposition may not be overridden except via an explicit BRACKET CLOSING OVERRIDE
(C-09 override authority), emitted as labeled field OVERRIDE INVOKED: YES | NO with
named justification.

---

**§2 CLASS DERIVATION CONTRACT (C-12)**
```
Gate verdict FAIL        -> Action item class: BLOCKED
Gate verdict CONDITIONAL -> Action item class: CONDITIONAL
Gate verdict PASS        -> Action item class: ADVISORY (skip if no advisory intent)
```
No editorial class assignment at action register assembly time.

---

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23, C-35)**

The null hypothesis verdict derives from a structured NH DIMENSION COMPARISON TABLE.
Three alternatives are required: Status Quo (what the team does today instead of building
this), Proposed Build, and Best-Non-Build Alternative.

**Required table format** (emitted at BRACKET OPENING):
```
| Dimension | A: Status Quo | B: Proposed Build | C: Best Non-Build Alt | Delta B-A | Delta B-C |
```
- Minimum 3 dimensions, scored on a consistent scale (e.g., 1-10).
- Dimensions chosen from the artifact's primary evaluation surfaces (e.g., developer
  experience, operational footprint, time-to-value, integration surface).
- The null hypothesis verdict is derivable from Delta B-A and Delta B-C alone:

```
g_null = PASS        if delta_B_A > 0 AND delta_B_C > 0
g_null = CONDITIONAL if exactly one delta > 0
g_null = FAIL        if delta_B_A <= 0 AND delta_B_C <= 0
```

Prose-only null hypothesis evaluation is not permitted when this rule is active. The
challenger may add prose testimony after the table but the table is the authoritative
source for g_null. BRACKET CLOSING re-populates columns B and C after receiving domain
and lifecycle evidence; g_null(final) derives from revised table values per the same rule.

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
BRACKET CLOSING GClose verdict MUST equal g_null(final), or declare OVERRIDE INVOKED: YES
with named justification.

---

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21, C-25)**

Each verdict-emitting section ends with a LOCAL GATE LEDGER ROW:
```
| Gate Verdict | Section Severity | Class | Finding References |
|---|---|---|---|
| [FAIL/CONDITIONAL/PASS] | [HIGH/MEDIUM/LOW] | [BLOCKED/CONDITIONAL/ADVISORY] | [list] |
```
Universal coverage: BRACKET OPENING, every DOMAIN section, LIFECYCLE section, and
BRACKET CLOSING each emit exactly one LOCAL GATE LEDGER ROW. Non-verdict sections
(see §6) emit no row. MASTER ACTION REGISTER assembled by verbatim copy of all rows.

---

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**

These sections emit NO gate ledger row:
- LENS OUTPUT SCHEMA and §§ PREAMBLE (pre-execution contracts only)
- SCOPE DECLARATION
- CH-ID REGISTRATION TABLE
- CH-ID SATURATION CHECK (emits g_null(post-domain) as a labeled field, not a gate row)
- SCOPE COVERAGE RECONCILIATION (informational only)
- LENS COVERAGE TABLE and DOMAIN COVERAGE GAP-CHECK (informational, per LENS OUTPUT SCHEMA)

---

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**

MASTER ACTION REGISTER assembly: copy all LOCAL GATE LEDGER ROWS verbatim. Do not
re-derive Gate Verdict or Class. The local row is the point of authority; the register
is a copy only.

---

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
1. SCOPE DECLARATION
2. CH-ID REGISTRATION TABLE
3. BRACKET OPENING (challenger / inertia-advocate)
4. DOMAIN REVIEWER SECTIONS (one per role, manifest order)
5. CH-ID SATURATION CHECK
6. LIFECYCLE REVIEWER SECTION
7. BRACKET CLOSING (challenger, post-domain)
8. SCOPE COVERAGE RECONCILIATION
9. LENS COVERAGE TABLE + DOMAIN COVERAGE GAP-CHECK
10. DISPOSITION + PRIMARY DRIVER
11. MASTER ACTION REGISTER
12. CROSS-ROLE SIGNALS
```
Reordering any numbered step is a contract violation. LIFECYCLE (step 6) must execute
before BRACKET CLOSING (step 7) so g_lifecycle is available.

---

**§9 CH-ID CHALLENGE REGISTRATION (C-04, C-05)**

Before any reviewer section runs, register all challenges in the CH-ID tracing table:
```
| CH-ID | Challenge Statement | Bracket Opening | [Domain roles...] | Lifecycle | Bracket Closing |
```
Populate the CH-ID and Challenge Statement at registration time. Response columns are
populated during execution as each reviewer section responds. Every reviewer section
carries a CH-ID response table (one row per CH-ID -- ADDRESSED or DEFERRED + rationale).

---

**§10 CH-ID SATURATION REQUIREMENT (C-27)**
```
SATURATED:       every CH-ID has >= 1 DOMAIN section response (verified before LIFECYCLE)
FULLY SATURATED: every CH-ID has domain + lifecycle responses (verified at BRACKET CLOSING)
```
BRACKET CLOSING may not emit PASS when any CH-ID is UNSATURATED without an explicit waiver
and stated justification.

---

**§11 LIFECYCLE VERDICT INTEGRATION CONTRACT (C-22)**

The LIFECYCLE reviewer section executes before BRACKET CLOSING (see §8, step 6 before
step 7). BRACKET CLOSING receives g_lifecycle as a labeled input field:
`Lifecycle verdict received: g_lifecycle = [FAIL/CONDITIONAL/PASS]`
and factors it into the g_null(final) derivation per §4 Stage 3.

---

**§12 DOMAIN-AGGREGATE FORMULA (C-24)**
```
G_domain_agg = median(all DOMAIN reviewer gate verdicts)
median order: FAIL < CONDITIONAL < PASS
```
BRACKET CLOSING receives G_domain_agg as a labeled input and applies the §4 Stage 2
null hypothesis progression formula.

---

**§13 ROLE LENS EXHAUSTION PROTOCOL (C-31, C-33, C-34)**

After all reviewer sections complete and before DISPOSITION, emit the LENS COVERAGE TABLE
and DOMAIN COVERAGE GAP-CHECK per the LENS OUTPUT SCHEMA pre-block. For each active
reviewer role, every `lens.verify` entry from the role's .roles/ definition must
appear in the table with:
- Applicability rating (HIGH/MEDIUM/LOW) per LENS OUTPUT SCHEMA definition.
- Status (ADDRESSED/OPEN) per finding references.

Both the LENS COVERAGE TABLE and the DOMAIN COVERAGE GAP-CHECK are mandatory outputs.
Omitting either is a protocol violation. ADVISORY-OPEN-LENS and ADVISORY-GAP items from
these outputs are appended to the MASTER ACTION REGISTER at step 11.

---

**§14 SCOPE COVERAGE GATE PROTOCOL (C-29)**

After BRACKET CLOSING (step 7), execute SCOPE COVERAGE RECONCILIATION. For each IN-SCOPE
surface from the SCOPE DECLARATION: classify as COVERED (referenced in >= 1 finding) or
GAP (no finding). GAP surfaces are automatically assigned LOW advisory severity and
appended to the MASTER ACTION REGISTER as ADVISORY-GAP items. This section emits no gate
ledger row (§6 NON-VERDICT SECTION EXCLUSION).

---

**§15 PER-FINDING SEVERITY CHAIN (C-30)** [IMMUTABLE]
```
Section Severity = worst(Severity of all individual findings in this section)
worst order: HIGH > MEDIUM > LOW
```
Every finding row in every reviewer section carries an individual Severity field (HIGH /
MEDIUM / LOW). Section Severity in the LOCAL GATE LEDGER ROW derives mechanically from
this formula. No editorial section-level severity assignment is permitted.

---

**§16 PRIMARY DRIVER DERIVATION (C-32)** [IMMUTABLE]

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

**§17 INPUT VARIABLE CONTRACTS (C-08, C-13, C-15)**

Template variables declared: `{{artifact_id}}`, `{{depth}}`, `{{reviewer_set}}`.
- `deep`: all roles from .roles/ invoked.
- `standard`: roles relevant to artifact type; selection rationale stated.
- `quick`: >= 3 highest-priority roles; abbreviation note included.
- `{{reviewer_set}}` overrides depth-based selection when non-auto.

Output must include an explicit acknowledgment block emitting all three injected values.

---

### EXECUTION

**Step 1: Acknowledge inputs**
```
Artifact: {{artifact_id}}
Depth: {{depth}}
Reviewer set: {{reviewer_set}}
Role selection rationale: [state if depth=standard]
```

**Step 2: SCOPE DECLARATION**
Enumerate all surfaces under review (artifact sections, surfaces, prior decisions).
Explicitly state OUT-OF-SCOPE surfaces. Any surface discovered mid-review is a scope
gap -- flag it; do not silently incorporate.

**Step 3: CH-ID REGISTRATION TABLE**
Register all challenges per §9 before any reviewer runs.

**Step 4: BRACKET OPENING (challenger / inertia-advocate)**
- State the null hypothesis: what the team does today instead of building this, and why
  that is acceptable. This is the strongest-case argument for not proceeding.
- Populate NH DIMENSION COMPARISON TABLE per §3: >= 3 dimensions, consistent scale,
  all three alternatives (A/B/C), compute Delta B-A and Delta B-C per dimension.
- Emit g_null(initial) as a labeled field derived from the table (not prose).
- Emit OVERRIDE INVOKED: NO (default -- may be changed to YES at BRACKET CLOSING only).
- Respond to relevant CH-IDs.
- Emit LOCAL GATE LEDGER ROW per §5.

**Step 5: DOMAIN REVIEWER SECTIONS** (one per role in reviewer set, manifest order)

For each role:
- State role name and lens in one sentence: "As a [role], I evaluate [lens concern]."
- Evaluate the artifact from this role's frame. Produce finding rows:
  `| Severity | Surface | Finding | Recommendation |`
- Respond to CH-IDs relevant to this role.
- Emit LOCAL GATE LEDGER ROW per §5. Section Severity = worst(finding severities) per §15.

**Step 6: CH-ID SATURATION CHECK**
- Verify SATURATED tier: every CH-ID has >= 1 domain section response.
- Emit g_null(post-domain) as a labeled field per §4 Stage 2 formula.
- No gate ledger row (§6).

**Step 7: LIFECYCLE REVIEWER SECTION**
- Apply the lifecycle lens: evaluate through operational lifecycle phases (creation,
  active use, change, deprecation, removal). Surface findings specific to lifecycle
  transitions, operational obligations, long-term maintenance costs.
- Produce finding rows (same format as Step 5).
- Respond to relevant CH-IDs.
- Emit LOCAL GATE LEDGER ROW per §5 with g_lifecycle labeled.

**Step 8: BRACKET CLOSING (challenger, post-domain)**
- Receive G_domain_agg (per §12), g_lifecycle, all domain gate verdicts as labeled inputs.
- Re-populate NH Dimension Comparison Table columns B and C with revised values (reflecting
  domain and lifecycle evidence received).
- Derive g_null(final) from revised table per §3 formula (Stage 3 of §4).
- Emit OVERRIDE INVOKED: YES | NO as labeled field.
- Emit LOCAL GATE LEDGER ROW per §5.

**Step 9: SCOPE COVERAGE RECONCILIATION** (per §14; no gate ledger row)

**Step 10: LENS COVERAGE TABLE + DOMAIN COVERAGE GAP-CHECK** (per LENS OUTPUT SCHEMA + §13; no gate ledger row)

**Step 11: DISPOSITION**
- Apply §1 DISPOSITION ALGEBRA to all gate verdicts.
- Emit `DISPOSITION: READY | CONDITIONAL | BLOCKED` as labeled field.
- Emit `Primary Driver: [value]` per §16.

**Step 12: MASTER ACTION REGISTER**
Copy all LOCAL GATE LEDGER ROWS verbatim (§7). Append ADVISORY-OPEN-LENS items from
step 10 and ADVISORY-GAP items from step 10 gap-check and step 9. Do not re-derive
Gate Verdict or Class.

**Step 13: CROSS-ROLE SIGNALS**
Synthesis narrative integrating findings across roles. Name >= 1 cross-role conflict or
convergence. Reference g_null progression through all three stages (initial, post-domain,
final). Explain the disposition rather than restating it.

---

## V-02

**Axis**: Phrasing register -- §13 expanded to a self-contained dense behavioral contract
with independent enforcement paths for C-33 and C-34; no pre-§§ schema block; C-35 via §3

**Hypothesis**: V-01 places C-33/C-34 in a pre-§§ schema block where they are declared
structurally. V-02 tests whether C-33 and C-34 can be enforced equally well through a
dense behavioral §13 that contains its own violation conditions -- without a separate schema
declaration. The hypothesis: a behavioral contract that says explicitly "omitting the
Applicability column is a protocol violation" (C-33) and "the gap-check is mandatory and
its omission is a protocol violation" (C-34) is sufficient for both criteria without the
schema block. If so, V-01 and V-02 both score 225/225 through different structural paths,
confirming robustness. Predicted: 225/225.

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
HIGH = blocks commitment | MEDIUM = conditions commitment | LOW = advisory.
```
Any gate FAIL -> BLOCKED | >= 1 CONDITIONAL, no FAIL -> CONDITIONAL | All PASS -> READY
```
Override: BRACKET CLOSING only, labeled field OVERRIDE INVOKED: YES | NO + justification.

---

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (skip if none intended).
No editorial class assignment at action register assembly time.

---

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23, C-35)**

The challenger's null hypothesis evaluation MUST use a structured NH DIMENSION COMPARISON
TABLE. Three alternatives required (Status Quo / Proposed Build / Best-Non-Build-Alt).
Required table format at BRACKET OPENING:
```
| Dimension | A: Status Quo | B: Proposed Build | C: Best Non-Build Alt | Delta B-A | Delta B-C |
```
Minimum 3 dimensions, consistent scale. The null hypothesis verdict is derivable from
table values alone:
```
g_null = PASS        if delta_B_A > 0 AND delta_B_C > 0
g_null = CONDITIONAL if exactly one delta > 0
g_null = FAIL        if delta_B_A <= 0 AND delta_B_C <= 0
```
Prose evaluation of the null hypothesis is invalid as a substitute for the table.
BRACKET CLOSING re-populates columns B and C; g_null(final) derives from revised values.

---

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
```
Stage 1: g_null(initial)     = GOpen [BRACKET OPENING, from NH table]
Stage 2: g_null(post-domain) [CH-ID SATURATION CHECK, formula over G_domain_agg]
         FAIL -> holds | PASS -> weakens one tier toward PASS | CONDITIONAL -> CONDITIONAL
Stage 3: g_null(final)       [BRACKET CLOSING, same substituting G_lifecycle]
```
GClose = g_null(final) or OVERRIDE INVOKED: YES with justification.

---

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21, C-25)**

Universal coverage: BRACKET OPENING, all DOMAIN sections, LIFECYCLE section, BRACKET
CLOSING each emit one LOCAL GATE LEDGER ROW at verdict time:
```
| Gate Verdict | Section Severity | Class | Finding References |
```
CH-ID SATURATION CHECK and SCOPE COVERAGE RECONCILIATION emit no gate row (non-verdict).
MASTER ACTION REGISTER assembled by verbatim copy of all rows.

---

**§6 VERBATIM ASSEMBLY PROHIBITION (C-20)**
Assembly instruction: copy all LOCAL GATE LEDGER ROWS verbatim. Prohibit re-derivation of
Gate Verdict or Class. Local row is the authority; register is a copy.

---

**§7 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
1. Scope Declaration          2. CH-ID Registration
3. Bracket Opening            4. Domain Reviewer Sections
5. CH-ID Saturation Check     6. Lifecycle Reviewer Section
7. Bracket Closing            8. Scope Coverage Reconciliation
9. Lens Coverage Table + Gap-Check  10. Disposition + Primary Driver
11. Master Action Register    12. Cross-Role Signals
```

---

**§8 CH-ID CHALLENGE REGISTRATION (C-04, C-05)**
CH-ID tracing table registered before any reviewer:
```
| CH-ID | Challenge Statement | Bracket Opening | [Domain roles...] | Lifecycle | Bracket Closing |
```
Every reviewer section carries a CH-ID response table row per registered CH-ID.

---

**§9 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED: every CH-ID has >= 1 DOMAIN response (before LIFECYCLE).
FULLY SATURATED: domain + lifecycle (at BRACKET CLOSING).
BRACKET CLOSING PASS prohibited when any CH-ID UNSATURATED, without explicit waiver.

---

**§10 LIFECYCLE VERDICT INTEGRATION (C-22)**
LIFECYCLE (step 6) executes before BRACKET CLOSING (step 7). BRACKET CLOSING receives
`Lifecycle verdict received: g_lifecycle = [value]` as labeled input.

---

**§11 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(all DOMAIN gate verdicts). FAIL < CONDITIONAL < PASS.
Labeled input to BRACKET CLOSING for §4 Stage 2 application.

---

**§12 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-BRACKET CLOSING: SCOPE COVERAGE RECONCILIATION maps every IN-SCOPE surface to
findings. GAP surfaces -> ADVISORY-GAP, LOW severity, appended to action register.
Emits no gate row (§5 non-verdict).

---

**§13 ROLE LENS EXHAUSTION PROTOCOL (C-31, C-33, C-34)** [IMMUTABLE]

After all reviewer sections (before DISPOSITION), emit a LENS COVERAGE TABLE. For each
active reviewer role from .roles/, every `lens.verify` entry in the role definition
must appear in the table. **The table carries three required fields per row**: Role,
Lens Dimension, **Applicability**, Status, and Finding Reference(s).

**Applicability field (C-33 enforcement)**: Every row MUST carry an Applicability rating
of HIGH, MEDIUM, or LOW. This rating is artifact-specific: it reflects how central this
role's lens dimension is to the artifact under review, not the role's generic capability.
The same role reviewing a different artifact type may carry different ratings. Omitting
the Applicability field from any lens table row is a protocol violation -- the row is
non-compliant and must be corrected before the lens table is considered complete. The
preamble declares: HIGH-applicability OPEN entries become ADVISORY-OPEN-LENS action items;
MEDIUM/LOW-applicability OPEN entries are noted but do not generate action items unless
the reviewer section explicitly flags them.

**DOMAIN COVERAGE GAP-CHECK (C-34 enforcement)**: Immediately after the LENS COVERAGE
TABLE, run a mandatory DOMAIN COVERAGE GAP-CHECK. This step is not optional. Enumerate
every artifact domain from the SCOPE DECLARATION. For each domain, check whether any
reviewer has HIGH Applicability for a lens dimension covering that domain. If no reviewer
does: classify the domain as ADVISORY-GAP and add to the MASTER ACTION REGISTER with:
domain name, reason for gap (no HIGH-applicability coverage), and recommended mitigation
(e.g., add a domain-specific reviewer, defer domain-specific risks to a follow-up). Omitting
the DOMAIN COVERAGE GAP-CHECK is a protocol violation equivalent to omitting the LENS
COVERAGE TABLE itself.

---

**§14 PER-FINDING SEVERITY CHAIN (C-30)** [IMMUTABLE]
```
Section Severity = worst(Severity of all individual finding rows in this section)
```
Every finding row carries individual Severity (HIGH / MEDIUM / LOW). No editorial
section-level assignment. Section Severity in gate ledger row is derived, not chosen.

---

**§15 PRIMARY DRIVER DERIVATION (C-32)** [IMMUTABLE]
First-match precedence over gate verdict vector:
BRACKET CLOSING OVERRIDE > NULL HYPOTHESIS (BRACKET OPENING FAIL) >
DOMAIN [first FAIL] > LIFECYCLE [FAIL] > DOMAIN [first CONDITIONAL] >
LIFECYCLE [CONDITIONAL] > CONSENSUS (all PASS).
Emit `Primary Driver: [value]` at DISPOSITION.

---

**§16 INPUT VARIABLE CONTRACTS (C-08, C-13, C-15)**
Template variables: `{{artifact_id}}`, `{{depth}}`, `{{reviewer_set}}`.
deep: all roles | standard: relevant + rationale | quick: >= 3 + abbreviation note.
Output acknowledges all injected values explicitly.

---

### EXECUTION

Steps 1-13 as V-01. The §13 behavioral enforcement paths for C-33 (Applicability column
required per row, violation condition stated) and C-34 (DOMAIN COVERAGE GAP-CHECK
mandatory, omission is a protocol violation) are the independent enforcement paths of
this variation -- both operative without reference to any pre-§§ schema block.

---

## V-03

**Axis**: Inertia framing -- §3 pre-registers the NH dimension set from artifact scope
before any section runs; C-35 strongest via scope-anchored dimension contract; C-33/C-34
via §13 with Applicability column and gap-check

**Hypothesis**: V-01 and V-02 fix C-35 by requiring an NH Dimension Comparison Table
format in §3 without pre-specifying what the dimensions are. The challenger may choose
dimensions ad hoc at BRACKET OPENING time. V-03 tests whether C-35 is more robustly
achieved when the challenger's analysis frame is pre-anchored to the artifact's scope:
the NULL HYPOTHESIS DERIVATION RULE in §3 instructs the prompt to derive initial
dimension labels from the IN-SCOPE surfaces declared in Step 2 (SCOPE DECLARATION),
before BRACKET OPENING runs. This means the challenger enters with a pre-committed
evaluation framework -- the inertia-advocate's table is anchored to the declared artifact
surfaces rather than freely chosen. The hypothesis: scope-anchored dimensions produce a
more auditable g_null (table values trace directly to declared scope surfaces) and more
reliably satisfy C-35's "derivable from table values alone" requirement. C-33/C-34 are
addressed through §13's standard Applicability protocol. Predicted: 225/225.

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
OVERRIDE: BRACKET CLOSING only, labeled OVERRIDE INVOKED: YES | NO + justification.

---

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY.
No editorial class assignment at assembly time.

---

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23, C-35)**

The challenger's null hypothesis evaluation is anchored to the artifact's declared scope.
After SCOPE DECLARATION (step 2 of execution), derive an initial NH dimension set from
the enumerated IN-SCOPE surfaces -- before BRACKET OPENING runs. The challenger's NH
Dimension Comparison Table uses these scope-derived dimensions as rows.

**NH dimension derivation**: From the IN-SCOPE surface list, group surfaces into 3-5
evaluation dimensions (e.g., API contract surface -> "Integration complexity"; operational
spec surface -> "Operational overhead"). These dimensions are the challenger's lens through
which Status Quo, Proposed Build, and Best-Non-Build-Alt are compared.

**Required table format** (BRACKET OPENING; scope-derived dimensions as rows):
```
| Dimension | A: Status Quo | B: Proposed Build | C: Best Non-Build Alt | Delta B-A | Delta B-C |
```
Three alternatives required. g_null derivable from Delta B-A and Delta B-C:
```
g_null = PASS if delta_B_A > 0 AND delta_B_C > 0
g_null = CONDITIONAL if exactly one delta > 0
g_null = FAIL if delta_B_A <= 0 AND delta_B_C <= 0
```
The challenger may add prose context after the table; the table is the authoritative source.
BRACKET CLOSING re-populates columns B and C; g_null(final) derives from revised table.

---

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
```
Stage 1: g_null(initial)     [BRACKET OPENING -- from scope-anchored NH table]
Stage 2: g_null(post-domain) [CH-ID SATURATION CHECK -- formula over G_domain_agg]
         G_domain_agg = FAIL -> holds | PASS -> weakens one tier | CONDITIONAL -> CONDITIONAL
Stage 3: g_null(final)       [BRACKET CLOSING -- same substituting G_lifecycle]
```
GClose = g_null(final) or OVERRIDE INVOKED: YES with justification.

---

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21, C-25)**
Universal coverage: BRACKET OPENING, all DOMAIN sections, LIFECYCLE section, BRACKET
CLOSING each emit one LOCAL GATE LEDGER ROW:
```
| Gate Verdict | Section Severity | Class | Finding References |
```
Non-verdict sections (CH-ID SATURATION CHECK, SCOPE COVERAGE RECONCILIATION, LENS
COVERAGE TABLE) emit no row. MASTER ACTION REGISTER assembled by verbatim copy.

---

**§6 VERBATIM ASSEMBLY PROHIBITION (C-20)**
Assembly: verbatim copy only. Re-derivation of Gate Verdict or Class at assembly time
is prohibited. Local row is the authority.

---

**§7 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
1. Scope Declaration (derive NH dimensions from scope before proceeding)
2. CH-ID Registration Table
3. Bracket Opening (challenger with scope-anchored NH table)
4. Domain Reviewer Sections (manifest order)
5. CH-ID Saturation Check
6. Lifecycle Reviewer Section
7. Bracket Closing
8. Scope Coverage Reconciliation
9. Lens Coverage Table + Domain Coverage Gap-Check
10. Disposition + Primary Driver
11. Master Action Register
12. Cross-Role Signals
```
Between steps 1 and 3, the NH dimension set is derived from the declared scope surfaces
(§3 scope-anchored derivation). This derivation step is part of the SCOPE DECLARATION
phase and does not emit a gate row.

---

**§8 CH-ID CHALLENGE REGISTRATION (C-04, C-05)**
Before any reviewer: register all challenges:
```
| CH-ID | Challenge Statement | Bracket Opening | [Domain roles...] | Lifecycle | Bracket Closing |
```
Every reviewer section carries a CH-ID response table.

---

**§9 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED: every CH-ID >= 1 DOMAIN response (before LIFECYCLE).
FULLY SATURATED: domain + lifecycle (at BRACKET CLOSING).
BRACKET CLOSING PASS blocked when UNSATURATED without waiver.

---

**§10 LIFECYCLE VERDICT INTEGRATION (C-22)**
LIFECYCLE precedes BRACKET CLOSING. BRACKET CLOSING receives:
`Lifecycle verdict received: g_lifecycle = [value]` as labeled input.

---

**§11 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(all DOMAIN gate verdicts). Labeled input to BRACKET CLOSING.

---

**§12 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-BRACKET CLOSING SCOPE COVERAGE RECONCILIATION. GAP surfaces -> ADVISORY-GAP,
appended to action register. No gate row.

---

**§13 ROLE LENS EXHAUSTION PROTOCOL (C-31, C-33, C-34)** [IMMUTABLE]

After all reviewer sections (before DISPOSITION): emit LENS COVERAGE TABLE.
For each active reviewer role's `lens.verify` entries:

```
| Reviewer Role | Lens Dimension | Applicability | Status | Finding Reference(s) |
```

**Applicability** (HIGH / MEDIUM / LOW): artifact-specific. Assigned at lens table
population time based on the artifact under review. HIGH = directly relevant to the
artifact's primary domain and scope. MEDIUM = relevant but secondary. LOW = tangential.
HIGH-applicability OPEN entries are promoted to ADVISORY-OPEN-LENS action items.

**DOMAIN COVERAGE GAP-CHECK**: After the LENS COVERAGE TABLE, check every artifact domain
from the SCOPE DECLARATION. Domains with no reviewer carrying HIGH Applicability for any
covering lens dimension are classified ADVISORY-GAP and appended to the MASTER ACTION
REGISTER with domain name and reason.

---

**§14 PER-FINDING SEVERITY CHAIN (C-30)** [IMMUTABLE]
Section Severity = worst(individual finding severities in section). HIGH > MEDIUM > LOW.
Every finding row carries individual Severity. No editorial section-level assignment.

---

**§15 PRIMARY DRIVER DERIVATION (C-32)** [IMMUTABLE]
First-match over gate verdict vector:
BRACKET CLOSING OVERRIDE > NULL HYPOTHESIS > DOMAIN [first FAIL] > LIFECYCLE [FAIL] >
DOMAIN [first CONDITIONAL] > LIFECYCLE [CONDITIONAL] > CONSENSUS.
Emit `Primary Driver: [value]` at DISPOSITION.

---

**§16 INPUT VARIABLE CONTRACTS (C-08, C-13, C-15)**
Variables: `{{artifact_id}}`, `{{depth}}`, `{{reviewer_set}}`.
Acknowledge all three in output. Depth governs role selection.

---

### EXECUTION

**Step 1: Acknowledge inputs** (as V-01)

**Step 2: SCOPE DECLARATION**
Enumerate IN-SCOPE and OUT-OF-SCOPE surfaces. After enumerating, derive the NH dimension
set per §3: group IN-SCOPE surfaces into 3-5 evaluation dimensions. State the derived
dimensions as: `NH Dimensions derived from scope: [dim-1], [dim-2], [dim-3], ...`
These dimensions are fixed for this review -- the challenger uses them at BRACKET OPENING.

**Steps 3-13**: as V-01. BRACKET OPENING populates the NH Dimension Comparison Table
using the scope-derived dimensions from Step 2 (not ad hoc dimension selection).

---

## V-04

**Axis**: Output format + Phrasing register (two-axis) -- V-01's LENS OUTPUT SCHEMA
pre-block combined with V-02's dense behavioral §13; dual enforcement path for C-33/C-34

**Hypothesis**: V-01 achieves C-33/C-34 via a pre-§§ schema block (structural declaration);
V-02 achieves them via dense behavioral §13 text (enforcement path). V-04 combines both:
the LENS OUTPUT SCHEMA block pre-declares the row format with Applicability column AND §13
contains its own independent behavioral enforcement text. The combination creates a dual
enforcement path: an auditor checking C-33 can verify compliance from either the LENS
OUTPUT SCHEMA block alone or the §13 behavioral text alone. Neither path depends on the
other. C-35 addressed via §3 (same as V-01 and V-02). Predicted: 225/225 with highest
auditor confidence for C-33/C-34.

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

### LENS OUTPUT SCHEMA

*(Full pre-§§ schema block from V-01 -- LENS COVERAGE TABLE row schema with Applicability
column, HIGH/MEDIUM/LOW definitions, ADVISORY-OPEN-LENS promotion rule, and mandatory
DOMAIN COVERAGE GAP-CHECK. Both declarations are binding before any reviewer section runs.)*

All structured lens outputs conform to schemas declared here:

**LENS COVERAGE TABLE row schema:**
```
| Reviewer Role | Lens Dimension | Applicability | Status | Finding Reference(s) |
```
- `Applicability`: HIGH (directly relevant) / MEDIUM (relevant, secondary) / LOW (tangential).
  Artifact-specific. Not a generic role rating. HIGH-applicability OPEN entries -> ADVISORY-OPEN-LENS.

**DOMAIN COVERAGE GAP-CHECK** (mandatory, after LENS COVERAGE TABLE):
For every artifact domain from SCOPE DECLARATION: identify whether any reviewer carries
HIGH Applicability for a lens dimension covering that domain. Uncovered domains ->
ADVISORY-GAP in MASTER ACTION REGISTER (domain name + reason + mitigation).

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
HIGH = blocks | MEDIUM = conditions | LOW = advisory.
FAIL -> BLOCKED | >= 1 CONDITIONAL, no FAIL -> CONDITIONAL | All PASS -> READY.
OVERRIDE: labeled field OVERRIDE INVOKED: YES | NO in BRACKET CLOSING.

---

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY.
No editorial class assignment at assembly time.

---

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23, C-35)**
*(Same as V-01 §3 -- NH DIMENSION COMPARISON TABLE required format, three alternatives,
g_null derivable from table values alone, prose evaluation invalid as substitute.)*

Three alternatives required (Status Quo / Proposed Build / Best-Non-Build-Alt):
```
| Dimension | A: Status Quo | B: Proposed Build | C: Best Non-Build Alt | Delta B-A | Delta B-C |
```
Minimum 3 dimensions. g_null = PASS if both deltas > 0; CONDITIONAL if one > 0; FAIL if both <= 0.
BRACKET CLOSING re-populates B/C columns; g_null(final) derives from revised table.

---

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
Stage 1: g_null(initial) [BRACKET OPENING] -> Stage 2: g_null(post-domain) [CH-ID SATURATION CHECK]
-> Stage 3: g_null(final) [BRACKET CLOSING]. GClose = g_null(final) or OVERRIDE.

---

**§5-§12**: As V-01 (LOCAL GATE LEDGER PROTOCOL, VERBATIM ASSEMBLY, SECTION ORDER CONTRACT,
CH-ID CHALLENGE REGISTRATION, CH-ID SATURATION, LIFECYCLE VERDICT INTEGRATION,
DOMAIN-AGGREGATE FORMULA, SCOPE COVERAGE GATE PROTOCOL).

---

**§13 ROLE LENS EXHAUSTION PROTOCOL (C-31, C-33, C-34)** [IMMUTABLE]

After all reviewer sections (before DISPOSITION): emit LENS COVERAGE TABLE per LENS
OUTPUT SCHEMA row schema.

**Schema layer (C-33)**: LENS OUTPUT SCHEMA pre-block declares the Applicability column
as a required field. Every row must carry HIGH / MEDIUM / LOW as specified.

**Behavioral enforcement layer (C-33, independent path)**: Every lens table row MUST carry
a populated Applicability value. Omitting the Applicability field is a protocol violation.
An auditor checking this §13 behavioral contract alone (without the LENS OUTPUT SCHEMA
block) can determine: (a) Applicability is required on every row, (b) the rating is
artifact-specific, (c) omission is a violation.

**Schema layer (C-34)**: LENS OUTPUT SCHEMA pre-block declares the DOMAIN COVERAGE
GAP-CHECK as mandatory and specifies ADVISORY-GAP promotion.

**Behavioral enforcement layer (C-34, independent path)**: The DOMAIN COVERAGE GAP-CHECK
is not optional. After completing the LENS COVERAGE TABLE, run the gap-check per LENS
OUTPUT SCHEMA definition. Omitting the gap-check is a protocol violation equivalent to
omitting the lens table. ADVISORY-GAP items from the gap-check are a required output of
this section and must appear in the MASTER ACTION REGISTER.

---

**§14-§16**: As V-01 (PER-FINDING SEVERITY CHAIN, PRIMARY DRIVER DERIVATION,
INPUT VARIABLE CONTRACTS).

---

### EXECUTION

Steps 1-13 as V-01. The §13 behavioral enforcement paths operate independently of the
LENS OUTPUT SCHEMA block: a compliance check may verify C-33/C-34 from either layer
without reference to the other.

---

## V-05

**Axis**: Output format + Phrasing register + Inertia framing (three-axis) -- all three
patterns: LENS OUTPUT SCHEMA pre-block (V-01) + dense behavioral §13 (V-02) + scope-anchored
NH dimension pre-registration (V-03)

**Hypothesis**: V-04 achieves dual-path C-33/C-34 enforcement and V-01/V-02 C-35. V-05
adds V-03's scope-anchored dimension pre-registration: the NH dimension set is derived from
the declared scope surfaces before BRACKET OPENING runs. The combination produces maximum
inter-criterion reinforcement: C-33/C-34 have three independent audit paths (LENS OUTPUT
SCHEMA + behavioral §13 + scope-domain alignment at gap-check time), and C-35 has its
strongest form (scope-anchored, not ad hoc). The hypothesis: scope-anchored NH dimensions
strengthen C-35 while LENS OUTPUT SCHEMA + behavioral §13 provide redundant C-33/C-34
enforcement. If all five R11 criteria (C-09 through C-32) still PASS and all three new
criteria (C-33/C-34/C-35) pass through their respective paths, V-05 achieves 225/225 with
the most robust structural architecture among R18 variants. Predicted: 225/225.

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

### LENS OUTPUT SCHEMA

*(Full pre-§§ schema block from V-01: LENS COVERAGE TABLE row schema with Applicability
column, HIGH/MEDIUM/LOW definitions, ADVISORY-OPEN-LENS promotion rule, and mandatory
DOMAIN COVERAGE GAP-CHECK with ADVISORY-GAP promotion. Binding before any reviewer runs.)*

**LENS COVERAGE TABLE row schema:**
```
| Reviewer Role | Lens Dimension | Applicability | Status | Finding Reference(s) |
```
Applicability: HIGH (directly relevant to artifact domain/scope) / MEDIUM / LOW (tangential).
Artifact-specific. HIGH-applicability OPEN entries -> ADVISORY-OPEN-LENS action items.

**DOMAIN COVERAGE GAP-CHECK** (mandatory, after lens table): Every artifact domain from
SCOPE DECLARATION checked for HIGH-applicability reviewer coverage. Uncovered domains ->
ADVISORY-GAP in MASTER ACTION REGISTER (domain name + reason + mitigation).

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
HIGH = blocks | MEDIUM = conditions | LOW = advisory.
FAIL -> BLOCKED | >= 1 CONDITIONAL, no FAIL -> CONDITIONAL | All PASS -> READY.
OVERRIDE: labeled field OVERRIDE INVOKED: YES | NO in BRACKET CLOSING + justification.

---

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY.
No editorial class assignment.

---

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23, C-35)**

NH dimensions are scope-anchored (V-03 axis): after SCOPE DECLARATION, derive 3-5
evaluation dimensions from the enumerated IN-SCOPE surfaces before BRACKET OPENING runs.
The challenger's NH Dimension Comparison Table uses these scope-derived dimensions as rows.

**Required table format** (BRACKET OPENING, scope-derived dimensions):
```
| Dimension | A: Status Quo | B: Proposed Build | C: Best Non-Build Alt | Delta B-A | Delta B-C |
```
Three alternatives. g_null derivable from table values:
```
g_null = PASS if delta_B_A > 0 AND delta_B_C > 0
g_null = CONDITIONAL if exactly one delta > 0
g_null = FAIL if delta_B_A <= 0 AND delta_B_C <= 0
```
Prose evaluation is invalid as substitute. BRACKET CLOSING re-populates B/C;
g_null(final) from revised table per the same formula.

---

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
```
Stage 1: g_null(initial) [BRACKET OPENING -- scope-anchored NH table]
Stage 2: g_null(post-domain) [CH-ID SATURATION CHECK -- G_domain_agg formula]
Stage 3: g_null(final) [BRACKET CLOSING -- G_lifecycle formula]
```
GClose = g_null(final) or OVERRIDE INVOKED: YES.

---

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21, C-25)**
Universal: BRACKET OPENING + all DOMAIN + LIFECYCLE + BRACKET CLOSING emit one row each:
```
| Gate Verdict | Section Severity | Class | Finding References |
```
Non-verdict sections emit no row. Assembly by verbatim copy.

---

**§6 VERBATIM ASSEMBLY PROHIBITION (C-20)**
Copy LOCAL GATE LEDGER ROWS verbatim. Re-derivation prohibited.

---

**§7 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
1. Scope Declaration (+ scope-anchored NH dimension derivation before step 2)
2. CH-ID Registration Table
3. Bracket Opening (scope-anchored NH table)
4. Domain Reviewer Sections
5. CH-ID Saturation Check
6. Lifecycle Reviewer Section
7. Bracket Closing
8. Scope Coverage Reconciliation
9. Lens Coverage Table + Domain Coverage Gap-Check
10. Disposition + Primary Driver
11. Master Action Register
12. Cross-Role Signals
```

---

**§8-§12**: CH-ID CHALLENGE REGISTRATION (C-04/C-05), CH-ID SATURATION (C-27), LIFECYCLE
VERDICT INTEGRATION (C-22), DOMAIN-AGGREGATE FORMULA (C-24), SCOPE COVERAGE GATE
PROTOCOL (C-29) -- as V-01 §9-§14.

---

**§13 ROLE LENS EXHAUSTION PROTOCOL (C-31, C-33, C-34)** [IMMUTABLE]

Post-execution LENS COVERAGE TABLE per LENS OUTPUT SCHEMA row schema (every `lens.verify`
entry from each active role).

**Schema layer**: LENS OUTPUT SCHEMA block pre-declares Applicability column requirement
and DOMAIN COVERAGE GAP-CHECK mandate.

**Behavioral enforcement layer (independent path)**: Every row MUST carry Applicability
(HIGH/MEDIUM/LOW, artifact-specific). Omission is a protocol violation. DOMAIN COVERAGE
GAP-CHECK is mandatory: identifies every artifact domain from SCOPE DECLARATION with no
HIGH-applicability reviewer. Uncovered domains -> ADVISORY-GAP action items. Omitting
the gap-check is a protocol violation. Both enforcement paths (schema layer and behavioral
layer) are independently auditable.

**Scope alignment (V-03 reinforcement)**: The domain registry for the gap-check comes from
the SCOPE DECLARATION's surface enumeration -- the same surfaces that anchored the NH
dimension derivation in §3. Domain coverage gaps and NH evaluation dimensions share a
common provenance: the declared artifact scope.

---

**§14 PER-FINDING SEVERITY CHAIN (C-30)** [IMMUTABLE]
Section Severity = worst(individual finding severities). HIGH > MEDIUM > LOW.

---

**§15 PRIMARY DRIVER DERIVATION (C-32)** [IMMUTABLE]
BRACKET CLOSING OVERRIDE > NULL HYPOTHESIS > DOMAIN [first FAIL] > LIFECYCLE [FAIL] >
DOMAIN [first CONDITIONAL] > LIFECYCLE [CONDITIONAL] > CONSENSUS.
Emit `Primary Driver: [value]` at DISPOSITION.

---

**§16 INPUT VARIABLE CONTRACTS (C-08, C-13, C-15)**
Variables: `{{artifact_id}}`, `{{depth}}`, `{{reviewer_set}}`. Acknowledge all three.

---

### EXECUTION

**Step 1: Acknowledge inputs** (as V-01)

**Step 2: SCOPE DECLARATION**
Enumerate IN-SCOPE and OUT-OF-SCOPE surfaces. After enumeration, derive the NH dimension
set per §3 scope-anchored rule: group surfaces into 3-5 evaluation dimensions. State:
`NH Dimensions (scope-anchored): [dim-1], [dim-2], [dim-3], ...`

**Step 3: CH-ID REGISTRATION TABLE** (as V-01)

**Step 4: BRACKET OPENING**
- State the null hypothesis (strongest case for not building this).
- Populate NH DIMENSION COMPARISON TABLE using scope-anchored dimensions from Step 2.
- Emit g_null(initial) as labeled field.
- Emit OVERRIDE INVOKED: NO (default).
- Respond to relevant CH-IDs.
- Emit LOCAL GATE LEDGER ROW.

**Steps 5-13**: as V-01. §13 lens table uses LENS OUTPUT SCHEMA row format;
§13 behavioral enforcement operates independently; domain registry from SCOPE DECLARATION
is also the source for the scope-anchored NH dimension set in §3.
