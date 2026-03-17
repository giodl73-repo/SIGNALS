---
skill: quest-variate
skill_target: org-review
date: 2026-03-17
round: 17
rubric: org-review-rubric-v15-2026-03-17.md
---

# org-review -- Variate R17

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis and three-axis combinations (V-04, V-05).

**R17 design target**: All five R16 variants scored 250/250 under v14 (perfect).
Under v15, the three new criteria (C-41, C-42, C-43) differentiate them. The R16
ceiling is 260/265: V-04 R16 achieves C-41+C-42 (misses C-43), V-05 R16 achieves
C-41+C-43 (misses C-42). No R16 variant achieves all three simultaneously. The R17
target is 265/265 -- all three new criteria pass together.

**Gap analysis from R16:**

| Criterion | R16 V-04 | R16 V-05 | What it requires |
|-----------|----------|----------|-----------------|
| C-41 LIFECYCLE NH SCORE EMISSION | PASS | PASS | LIFECYCLE section emits NH Dimension Scores sub-table; C-39 formula extended to avg(DOMAIN B + LIFECYCLE B) |
| C-42 F-ID NAMED FIELD | PASS | FAIL | Finding column named `F-ID`, not positional `#`; all downstream refs use F-ID values |
| C-43 CH-ID §0 GROUNDING COLUMN | FAIL | PASS | CH-ID table includes §0 column citing preamble commitment authorizing each challenge |

**R17 synthesis path**: V-04 R16 missed C-43 (no §0 column declared at challenge
registration). V-05 R16 missed C-42 (positional `#` column in finding table). R17
must integrate all three. Each variant takes a different structural approach to
co-locating the three new pattern declarations in the preamble.

**R17 variation axes:**

- V-01: Lifecycle emphasis (single axis) -- §18 LIFECYCLE NH SCORE EMISSION expanded
  to a top-level numbered contract rather than an extension clause. F-ID (C-42)
  introduced in the finding schema block at the same structural level as NH emission.
  §0 grounding column (C-43) in the CH-ID registration table.

- V-02: Output format (single axis) -- unified TABLE FORMAT CONTRACT block declared
  before all other preamble contracts. All table schemas (finding table with F-ID
  column, CH-ID table with §0 column, NH dimension table, gate ledger) pre-declared
  in a single structural block. C-42 and C-43 fall out from the table schema
  declarations.

- V-03: Inertia framing (single axis) -- preamble opens with STATUS QUO FRAMING
  CONTRACT naming the inertia-advocate's specific no-build commitments as §0-CID
  values. CH-ID table §0 column cites these §0-CID values. F-ID emerges from the
  inertia-advocate's auditability requirement. LIFECYCLE NH emission from §18.

- V-04: Lifecycle + Output format (two-axis) -- V-01's §18 lifecycle elevation
  combined with V-02's TABLE FORMAT CONTRACT block. Two structural paths enforce
  C-43 and C-42: table schema pre-declaration (V-02) and lifecycle-first preamble
  organization (V-01).

- V-05: Lifecycle + Output format + Inertia framing (three-axis) -- all three
  single-axis patterns combined. §0 commitment IDs from inertia framing populate the
  §0 grounding column declared by the TABLE FORMAT CONTRACT and referenced by the
  lifecycle architecture block.

**R17 single-axis predictions:**
- V-01: C-41 PASS (§18 top-level), C-42 PASS (F-ID in finding schema), C-43 PASS
  (§0 column in CH-ID registration). Predicted: 265/265
- V-02: C-41 PASS (§18 lifecycle clause), C-42 PASS (TABLE FORMAT CONTRACT finding
  schema), C-43 PASS (TABLE FORMAT CONTRACT CH-ID schema). Predicted: 265/265
- V-03: C-41 PASS (§18), C-42 PASS (inertia audit requirement), C-43 PASS (§0-CID
  column grounding). Predicted: 265/265

**R17 two-axis and three-axis predictions:**
- V-04: 265/265 via dual enforcement path (lifecycle block + table schema block)
- V-05: 265/265 with strongest inter-criterion referential chain (all three new
  criteria reinforce each other through inertia framing, table format, and lifecycle
  architecture)

---

## V-01

**Axis**: Lifecycle emphasis -- LIFECYCLE NH SCORE EMISSION as top-level numbered
preamble contract; F-ID in finding schema; §0 grounding in CH-ID registration table

**Hypothesis**: V-05 R16 achieved C-41+C-43 but missed C-42 because the finding
table used positional `#`. The fix is minimal: add a finding schema declaration to
the preamble that names `F-ID` as a required column. The lifecycle emphasis axis
provides the structural motivation: when LIFECYCLE NH emission is elevated to a
top-level contract (§18, same level as §15 DOMAIN NH SCORE EMISSION), the preamble
is already structured as an explicit list of per-section emission requirements.
Adding F-ID to the finding row schema block at that same level makes the F-ID
requirement feel architecturally native rather than bolted on. §0 grounding column
(C-43) is declared at CH-ID registration time as it was in V-05 R16. Predicted
score: 265/265.

---

You are running `/org-review`.

Inputs:
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .craft/roles/]
```

Acknowledge injected values before executing any section.

---

### §0 -- PREAMBLE: ALL CONTRACTS PRE-COMMITTED BEFORE EXECUTION

All contracts in §1 through §22 are binding before any reviewer section runs.
No contract may be revised post-execution. Each contract maps to one or more
rubric criteria; the mapping is auditable from contract ID.

---

**§1 DISPOSITION ALGEBRA (C-10, C-02)**

Severity semantics: HIGH = blocks commitment; MEDIUM = conditions commitment;
LOW = advisory. Overall DISPOSITION derives mechanically:

```
If any gate verdict = FAIL                  -> DISPOSITION: BLOCKED
If no FAIL and >= 1 gate verdict = CONDITIONAL -> DISPOSITION: CONDITIONAL
If all gate verdicts = PASS                 -> DISPOSITION: READY
```

BLOCKED disposition may not be overridden except by an explicit BRACKET CLOSING
override (C-09 override authority). Override requires a labeled OVERRIDE INVOKED:
YES / NO field in BRACKET CLOSING and a named justification.

---

**§2 CLASS DERIVATION CONTRACT (C-12)**

Action item class derives mechanically from the gate verdict that generated it:

```
Gate verdict FAIL        -> Action item class: BLOCKED
Gate verdict CONDITIONAL -> Action item class: CONDITIONAL
Gate verdict PASS        -> Action item class: ADVISORY (optional; skip if no advisory intent)
```

No editorial class assignment is permitted at action register synthesis time.

---

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23)**

The null hypothesis verdict (g_null) derives from the alternatives comparison table.
Three or more alternatives are required (Status Quo, Proposed Build, Best-Non-Build-Alt).
The derivation rule covers both pairwise differentials:

```
Let delta_B_A = (Proposed-Build aggregate score) - (Status-Quo aggregate score)
Let delta_B_C = (Proposed-Build aggregate score) - (Best-Non-Build-Alt aggregate score)

g_null = PASS        if delta_B_A > 0 AND delta_B_C > 0
g_null = CONDITIONAL if (delta_B_A > 0 AND delta_B_C <= 0) OR (delta_B_A <= 0 AND delta_B_C > 0)
g_null = FAIL        if delta_B_A <= 0 AND delta_B_C <= 0
```

This rule is applied at all three g_null checkpoints (§7).

---

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**

The null hypothesis verdict evolves through three labeled stages:

```
Stage 1: g_null(initial)     = GOpen verdict  [emitted at BRACKET OPENING]
Stage 2: g_null(post-domain) = formula(G_domain_agg, g_null(initial))
         -> if G_domain_agg = FAIL: g_null(post-domain) = g_null(initial) (challenger holds)
         -> if G_domain_agg = PASS: g_null(post-domain) weakens toward PASS by one tier
         -> if G_domain_agg = CONDITIONAL: g_null(post-domain) = CONDITIONAL
         [emitted at CH-ID SATURATION CHECK section]
Stage 3: g_null(final)       = formula(G_lifecycle, g_null(post-domain))
         -> same logic as Stage 2 substituting G_lifecycle
         [emitted at BRACKET CLOSING]
```

BRACKET CLOSING GClose verdict MUST equal g_null(final), or declare an explicit
OVERRIDE INVOKED: YES with named justification.

---

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21)**

Each verdict-emitting reviewer section ends with a LOCAL GATE LEDGER ROW in this
exact format:

```
| Gate Verdict | Section Severity | Class | F-ID(s) sourcing this verdict |
|---|---|---|---|
| [FAIL/CONDITIONAL/PASS] | [HIGH/MEDIUM/LOW] | [BLOCKED/CONDITIONAL/ADVISORY] | [comma-separated F-ID values] |
```

Universal coverage: BRACKET OPENING, every DOMAIN reviewer section, LIFECYCLE
reviewer section, and BRACKET CLOSING each emit exactly one LOCAL GATE LEDGER ROW.
The MASTER ACTION REGISTER is assembled by copying all LOCAL GATE LEDGER ROWS
verbatim. Re-derivation of Gate Verdict or Class at assembly time is prohibited.

---

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**

The following sections are NOT verdict-emitting and emit NO gate ledger row:
- §0 PREAMBLE (contract declarations only)
- SCOPE DECLARATION (artifact enumeration only)
- CH-ID REGISTRATION TABLE (challenge registration only; no verdict)
- CH-ID SATURATION CHECK (emits g_null(post-domain) as a labeled field, NOT a gate ledger row)
- SCOPE COVERAGE RECONCILIATION (informational only; see §12)
- LENS COVERAGE TABLE (informational only; see §10)

---

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**

MASTER ACTION REGISTER assembly instruction: Copy all LOCAL GATE LEDGER ROWS
verbatim. Do not re-derive Gate Verdict or Class. The local row is the point of
authority; the register is a copy only.

---

**§8 SECTION ORDER CONTRACT (C-26)**

Canonical execution sequence -- immutable. Reordering is a contract violation:

```
1. SCOPE DECLARATION
2. CH-ID REGISTRATION TABLE (including §0 grounding column)
3. BRACKET OPENING (challenger / inertia-advocate)
4. DOMAIN REVIEWER SECTIONS (one section per role in reviewer set)
5. CH-ID SATURATION CHECK
6. LIFECYCLE REVIEWER SECTION
7. BRACKET CLOSING (challenger post-domain)
8. SCOPE COVERAGE RECONCILIATION
9. LENS COVERAGE TABLE
10. DISPOSITION + PRIMARY DRIVER
11. MASTER ACTION REGISTER
12. CROSS-ROLE SIGNALS (synthesis narrative)
```

No section may execute before its predecessor in this sequence. LIFECYCLE section
(step 6) must execute before BRACKET CLOSING (step 7) so that the lifecycle gate
verdict (g_lifecycle) is available to the bracket closing reassessment.

---

**§9 CH-ID CHALLENGE REGISTRATION (C-04, C-43)**

Before any reviewer section executes, register all challenges in the CH-ID
tracing table. The table is a two-axis structure:

- **Origin axis (§0 column)**: records the specific preamble contract (§1-§22)
  that authorizes each challenge. Populated at registration time. Every CH-ID
  must carry a §0 grounding citation; challenges without preamble authorization
  are invalid and must not be registered.
- **Response axis**: one column per reviewer section (populated during execution).

CH-ID tracing table schema (required columns):

```
| CH-ID | Challenge Statement | §0 Grounding | Bracket Opening | [Domain roles...] | Lifecycle | Bracket Closing |
```

The §0 Grounding column is the backward-traceability axis. It cites the preamble
section whose contract this challenge is designed to probe (e.g., "§1 DISPOSITION
ALGEBRA -- tests whether BLOCKED derivation is applied correctly").

---

**§10 CH-ID SATURATION REQUIREMENT (C-27)**

Two-tier cross-section saturation:

```
SATURATED:       every CH-ID has received a response from >= 1 DOMAIN section
                 (verified before LIFECYCLE executes; emitted at CH-ID SATURATION CHECK)
FULLY SATURATED: every CH-ID has received both domain and lifecycle responses
                 (verified at BRACKET CLOSING)
```

BRACKET CLOSING may not emit a PASS verdict when any CH-ID is UNSATURATED unless
an explicit waiver is stated with justification.

---

**§11 PER-FINDING SEVERITY AGGREGATION CONTRACT (C-30)**

Each finding row carries an individual Severity field (HIGH / MEDIUM / LOW).
Section Severity derives mechanically as:

```
Section Severity = worst(Severity of F-01, F-02, ..., F-N in this section)
worst order: HIGH > MEDIUM > LOW
```

No editorial assignment of section-level severity is permitted. The Section
Severity in the LOCAL GATE LEDGER ROW must equal the worst-case finding severity.

---

**§12 FINDING IDENTIFIER CONTRACT (C-42)**

Every finding row in every reviewer section carries a named, stable identifier as
a required column:

```
F-ID format: F-NN  (e.g., F-01, F-02, F-07)
```

Finding table schema (required columns, in this order):

```
| F-ID | Severity | Surface | Finding | Recommendation |
```

The `F-ID` column is a named field, not a positional row number. F-ID values are
unique within the review output (no two findings share an F-ID). All downstream
references -- action register entries, CH-ID response tracking, lens coverage table
citations -- MUST reference F-ID values, not positional row numbers. Referencing a
finding by "row 3" when an F-ID column exists is a contract violation.

---

**§13 LENS COVERAGE TABLE PROTOCOL (C-31, C-33, C-34)**

After all reviewer sections complete (before DISPOSITION), emit a LENS COVERAGE
TABLE. For each active reviewer role, all `lens.verify` entries from the role
definition must appear with:

- **ADDRESSED**: at least one finding (by F-ID reference) addresses this lens dimension.
- **OPEN**: no finding addressed this lens dimension.

Each row also carries an **Applicability** rating (HIGH / MEDIUM / LOW) specific
to the artifact under review (not a generic role capability rating). The
applicability rating is the basis for the ADDRESSED/OPEN determination: HIGH-
applicability entries that remain OPEN are promoted to ADVISORY-OPEN-LENS items
in the MASTER ACTION REGISTER.

After the LENS COVERAGE TABLE, run a DOMAIN COVERAGE GAP-CHECK: identify artifact
domains (from scope surface domain annotations) that have no reviewer with HIGH
applicability. Each uncovered domain is classified as ADVISORY-GAP and promoted
to the MASTER ACTION REGISTER with domain name and reason for gap.

---

**§14 SCOPE SURFACE DOMAIN ANNOTATION (C-36)**

Every surface in the IN-SCOPE list carries an explicit [DOMAIN: label] annotation
at enumeration time. Domain annotations form the registry consumed by the §13
DOMAIN COVERAGE GAP-CHECK. The C-34 gap-check cites the domain annotation registry
as its source; no editorial domain inference is permitted at gap-check time.

Required format:
```
- [surface name] [DOMAIN: label]
```
Example: `- /api/v2/signals endpoint contract [DOMAIN: API]`

---

**§15 SCOPE COVERAGE GATE PROTOCOL (C-29)**

After BRACKET CLOSING, execute a SCOPE COVERAGE RECONCILIATION section. For each
IN-SCOPE surface, classify:

- **COVERED**: appears in >= 1 finding (by F-ID reference).
- **GAP**: no finding references this surface.

GAP surfaces are automatically assigned LOW advisory severity and promoted to the
MASTER ACTION REGISTER as ADVISORY-GAP items. The reconciliation section emits a
COVERED/PARTIAL signal that is informational only -- it produces no gate ledger row
(see §6 NON-VERDICT SECTION EXCLUSION).

---

**§16 NH DIMENSION TABLE CONTRACT (C-35, C-37, C-38)**

The BRACKET OPENING challenger evaluation uses a structured NH Dimension Comparison
Table with THREE comparison columns:

```
| Dimension | A: Status-Quo | B: Proposed-Build | C: Best-Non-Build-Alt | Delta B-A | Delta B-C |
```

At minimum 3 dimensions, scored on a defined scale (e.g., 1-10). The g_null(initial)
verdict is derivable from Delta B-A and Delta B-C values alone per §3 formula.

BRACKET CLOSING re-populates this table with revised per-dimension values after
receiving domain and lifecycle evidence (§17 re-population contract). The g_null(final)
verdict must be derivable from the revised table values alone.

---

**§17 NH TABLE AGGREGATION RULE WITH LIFECYCLE EXTENSION (C-39, C-40, C-41)**

The NH dimension table column aggregation formula is pre-committed for both the
DOMAIN and LIFECYCLE reviewer archetypes:

```
Column A (Status-Quo):         challenger's opening value carried forward unchanged
Column B (Proposed-Build):     avg(all DOMAIN B scores + LIFECYCLE B score)
Column C (Best-Non-Build-Alt): avg(all DOMAIN C scores + LIFECYCLE C score)
```

**DOMAIN NH SCORE EMISSION REQUIREMENT (C-40)**: Each DOMAIN reviewer section
emits an NH Dimension Scores sub-table before its LOCAL GATE LEDGER ROW:

```
NH Dimension Scores -- [Role Name]
| Dimension | B: Proposed-Build | C: Best-Non-Build-Alt |
|-----------|------------------|----------------------|
| [dim-1]   | [score]          | [score]               |
| [dim-2]   | [score]          | [score]               |
```

**LIFECYCLE NH SCORE EMISSION REQUIREMENT (C-41)**: The LIFECYCLE reviewer section
ALSO emits an NH Dimension Scores sub-table before its LOCAL GATE LEDGER ROW, using
the same dimension rows as the C-35 NH dimension comparison table:

```
NH Dimension Scores -- [Lifecycle Role Name]
| Dimension | B: Proposed-Build | C: Best-Non-Build-Alt |
|-----------|------------------|----------------------|
| [dim-1]   | [score]          | [score]               |
| [dim-2]   | [score]          | [score]               |
```

BRACKET CLOSING reads all DOMAIN sub-tables AND the LIFECYCLE sub-table as input
to the §18 column B and C aggregation. No prose extraction from any reviewer section
is permitted in the NH aggregation chain.

---

**§18 DOMAIN-AGGREGATE FORMULA (C-24)**

Domain gate verdicts aggregate before BRACKET CLOSING applies the disposition rule:

```
G_domain_agg = median(all DOMAIN gate verdicts)
median order: FAIL < CONDITIONAL < PASS
```

BRACKET CLOSING receives G_domain_agg as a labeled input and applies the §4
NULL HYPOTHESIS PROGRESSION formula.

---

**§19 SECTION ORDER CONTRACT ENFORCEMENT (C-26)**

LIFECYCLE reviewer section MUST execute before BRACKET CLOSING (see §8, step 6
before step 7). BRACKET CLOSING receives g_lifecycle as a labeled input field
(G_lifecycle: [FAIL/CONDITIONAL/PASS]) and factors it into the g_null(final)
derivation per §4 Stage 3.

---

**§20 PRIMARY DRIVER DERIVATION CONTRACT (C-32)**

After all gate verdicts are known, the PRIMARY DRIVER of the DISPOSITION is selected
mechanically by this precedence rule-set (applied in order, first match wins):

```
Rule 1: Any gate = FAIL and gate is BRACKET CLOSING (with OVERRIDE INVOKED: YES)
        -> Primary Driver: BRACKET CLOSING OVERRIDE
Rule 2: Any gate = FAIL and gate is BRACKET OPENING (challenger holds null hypothesis)
        -> Primary Driver: NULL HYPOTHESIS
Rule 3: Any gate = FAIL and gate is DOMAIN reviewer
        -> Primary Driver: DOMAIN [role name of first FAIL gate in manifest order]
Rule 4: Any gate = FAIL and gate is LIFECYCLE
        -> Primary Driver: LIFECYCLE
Rule 5: No FAIL; >= 1 DOMAIN gate = CONDITIONAL
        -> Primary Driver: DOMAIN [role name of first CONDITIONAL gate in manifest order]
Rule 6: No FAIL; LIFECYCLE gate = CONDITIONAL
        -> Primary Driver: LIFECYCLE
Rule 7: All gates = PASS
        -> Primary Driver: CONSENSUS
```

Emit as labeled field at DISPOSITION time: `Primary Driver: [value]`.

---

**§21 DEPTH MODE ACKNOWLEDGMENT (C-08)**

The acknowledged {{depth}} value governs reviewer set selection:
- `deep`: all roles from .craft/roles/ are invoked (no filtering)
- `standard`: roles relevant to the artifact type are selected; selection rationale stated
- `quick`: >= 3 highest-priority roles; abbreviation note included in output

The acknowledged {{reviewer_set}} value overrides depth-based selection when non-auto.

---

### EXECUTION

**Step 1: Acknowledge injected values**

```
Artifact: {{artifact_id}}
Depth: {{depth}}
Reviewer set: {{reviewer_set}}
Role selection rationale: [state if depth=standard]
```

**Step 2: SCOPE DECLARATION**

Enumerate all surfaces under review. Every IN-SCOPE surface carries [DOMAIN: label].
Explicitly state OUT-OF-SCOPE surfaces. Any surface discovered mid-review is a scope
gap (flag, do not silently incorporate).

**Step 3: CH-ID REGISTRATION TABLE**

Register all challenges before any reviewer runs. Populate §0 Grounding column at
registration time. Format per §9.

**Step 4: BRACKET OPENING (challenger / inertia-advocate)**

- State the null hypothesis: what the team does today instead of building this, and
  why that is acceptable.
- Populate NH Dimension Comparison Table (§16): three columns (A, B, C), >= 3
  dimensions, per-dimension scores and deltas.
- Emit g_null(initial) as a labeled field.
- Emit LOCAL GATE LEDGER ROW (per §5).

**Step 5: DOMAIN REVIEWER SECTIONS** (one per role in reviewer set, manifest order)

For each role:
- Read role definition from .craft/roles/. State role name and lens as a one-sentence
  Lens declaration ("As a [role], I care about [concern from lens.verify]").
- Evaluate the artifact from this role's frame. Produce finding rows in finding table
  schema (§12): F-ID | Severity | Surface | Finding | Recommendation.
- Respond to any CH-IDs relevant to this role.
- Emit NH Dimension Scores sub-table (§17 DOMAIN NH SCORE EMISSION REQUIREMENT).
- Emit LOCAL GATE LEDGER ROW (§5). Section Severity = worst(finding severities) per §11.

**Step 6: CH-ID SATURATION CHECK**

- Verify SATURATED tier: every CH-ID has >= 1 domain response.
- Emit g_null(post-domain) as a labeled field (per §4 Stage 2 formula).
- Note: this section emits NO gate ledger row (§6).

**Step 7: LIFECYCLE REVIEWER SECTION**

- Apply the lifecycle lens: evaluate the artifact through its operational lifecycle
  phases (creation, active use, change, deprecation, removal), surfacing findings
  specific to lifecycle transitions, operational obligations, or long-term maintenance.
- Produce finding rows in finding table schema (§12).
- Respond to any CH-IDs relevant to the lifecycle perspective.
- Emit NH Dimension Scores sub-table (§17 LIFECYCLE NH SCORE EMISSION REQUIREMENT).
- Emit LOCAL GATE LEDGER ROW (§5) with g_lifecycle labeled.

**Step 8: BRACKET CLOSING (challenger / inertia-advocate, post-domain)**

- Receive all domain and lifecycle gate verdicts as labeled inputs.
- Receive G_domain_agg (per §18) as a labeled input.
- Receive g_lifecycle as a labeled input.
- Re-populate NH Dimension Comparison Table with revised per-dimension values
  (columns B and C computed per §17 column aggregation formula).
- Derive g_null(final) from revised table per §3 formula (Stage 3 of §4).
- Emit OVERRIDE INVOKED: YES | NO as a labeled field.
- Emit LOCAL GATE LEDGER ROW (§5).

**Step 9: SCOPE COVERAGE RECONCILIATION** (per §15; no gate ledger row)

**Step 10: LENS COVERAGE TABLE** (per §13; no gate ledger row)

**Step 11: DISPOSITION**

- Apply §1 DISPOSITION ALGEBRA to gate verdict vector.
- Emit DISPOSITION: READY | CONDITIONAL | BLOCKED as a labeled field.
- Emit Primary Driver: [value] per §20.

**Step 12: MASTER ACTION REGISTER**

Copy all LOCAL GATE LEDGER ROWS verbatim (§7). Append ADVISORY-GAP items from §15
and ADVISORY-OPEN-LENS items from §13. Do not re-derive Gate Verdict or Class.

**Step 13: CROSS-ROLE SIGNALS**

Synthesis narrative integrating findings across roles. Name at least one cross-role
conflict or convergence. Reference g_null progression (all three stages). Explain
the disposition rather than restating it.

---

## V-02

**Axis**: Output format -- unified TABLE FORMAT CONTRACT declares all table schemas
before the individual §§ contracts; §0 grounding column declared structurally in the
CH-ID table schema block; F-ID declared structurally in the finding table schema block

**Hypothesis**: V-04 R16 achieved C-41+C-42 but missed C-43 because there was no
pre-committed structural declaration of the CH-ID table schema -- the §0 grounding
column was absent. V-02 R17 introduces a TABLE FORMAT CONTRACT as the first block
after template variable acknowledgment, before all individual §§ contracts. This
block declares the schema of every structured table in the output, including the
finding table (with `F-ID` column, covering C-42) and the CH-ID table (with `§0
Grounding` column, covering C-43). When the table schemas are pre-declared in a
single structural block, C-42 and C-43 become schema-level declarations rather than
contract-clause additions, reducing the risk that either is omitted under an axis
variation. C-41 (LIFECYCLE NH SCORE EMISSION) is declared in §17 as in V-01.
Predicted score: 265/265.

---

You are running `/org-review`.

Inputs:
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .craft/roles/]
```

Acknowledge injected values before executing any section.

---

### TABLE FORMAT CONTRACT (declared before all §§ contracts)

All tables produced by this review conform to the schemas defined here. Schema
fields are required on every row unless marked optional. Any row that omits a
required field is a format violation.

**Finding Table** (emitted in each reviewer section):
```
| F-ID | Severity | Surface | Finding | Recommendation |
```
- `F-ID`: required. Named stable identifier (F-01, F-02, ...). NOT a positional row
  number. All downstream cross-references use F-ID values, not row positions.
- `Severity`: required. Exactly HIGH / MEDIUM / LOW.
- `Surface`: required. Named artifact surface (section, field, diagram element, or named assumption).
- `Finding`: required. Specific observation on the named surface.
- `Recommendation`: required. What to do and where in the artifact.

**CH-ID Challenge Table** (emitted once before BRACKET OPENING):
```
| CH-ID | Challenge Statement | §0 Grounding | [Section columns...] |
```
- `CH-ID`: required. Named identifier (CH-01, CH-02, ...).
- `Challenge Statement`: required. The specific question or challenge posed.
- `§0 Grounding`: required. The preamble contract section (e.g., "§1 DISPOSITION
  ALGEBRA") that authorizes this challenge. Populated at registration time. Every
  CH-ID must cite a §0 grounding; challenges without preamble authorization are invalid.
- Section columns: one per reviewer section (populated during execution, initially empty).

**NH Dimension Scores Sub-table** (emitted at end of each DOMAIN and LIFECYCLE section):
```
| Dimension | B: Proposed-Build | C: Best-Non-Build-Alt |
```
- Same dimension rows as the NH Dimension Comparison Table (BRACKET OPENING).
- `B` and `C` columns: reviewer's per-dimension score or rating (same scale as BRACKET OPENING).

**NH Dimension Comparison Table** (emitted at BRACKET OPENING and re-populated at BRACKET CLOSING):
```
| Dimension | A: Status-Quo | B: Proposed-Build | C: Best-Non-Build-Alt | Delta B-A | Delta B-C |
```
- Three alternatives required. g_null derivable from Delta B-A and Delta B-C alone.

**LOCAL GATE LEDGER ROW** (emitted at end of each verdict-emitting section):
```
| Gate Verdict | Section Severity | Class | F-ID(s) sourcing this verdict |
```

**MASTER ACTION REGISTER ROW** (assembled by verbatim copy from LOCAL GATE LEDGER ROWS):
```
| F-ID | Gate Verdict | Class | Section | Finding Summary | Recommendation |
```
All F-ID values reference entries in the finding table. No positional references.

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**

```
HIGH = blocks commitment | MEDIUM = conditions | LOW = advisory
FAIL -> BLOCKED | >= 1 CONDITIONAL + no FAIL -> CONDITIONAL | all PASS -> READY
OVERRIDE: labeled field OVERRIDE INVOKED: YES | NO in BRACKET CLOSING
```

**§2 CLASS DERIVATION CONTRACT (C-12)**
`FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (optional)`
No editorial class assignment at assembly time.

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23)**
Three alternatives required. `g_null = PASS` iff `delta_B_A > 0 AND delta_B_C > 0`.
`g_null = CONDITIONAL` iff exactly one delta is positive. `g_null = FAIL` iff both <= 0.

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
Three labeled stages: g_null(initial) at BRACKET OPENING, g_null(post-domain) at
CH-ID SATURATION CHECK, g_null(final) at BRACKET CLOSING. BRACKET CLOSING GClose
must equal g_null(final) or declare OVERRIDE INVOKED: YES with justification.

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21)**
Universal coverage: BRACKET OPENING + all DOMAIN sections + LIFECYCLE section +
BRACKET CLOSING each emit one LOCAL GATE LEDGER ROW per TABLE FORMAT CONTRACT schema.
Assembly: verbatim copy; no re-derivation.

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate ledger row from: preamble, scope declaration, CH-ID registration table,
CH-ID SATURATION CHECK, SCOPE COVERAGE RECONCILIATION, LENS COVERAGE TABLE.

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**
Copy LOCAL GATE LEDGER ROWS to MASTER ACTION REGISTER verbatim. Re-derivation
of Gate Verdict or Class is prohibited.

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
1. Scope Declaration  2. CH-ID Registration  3. Bracket Opening
4. Domain Reviewers   5. CH-ID Saturation Check  6. Lifecycle Reviewer
7. Bracket Closing    8. Scope Coverage Reconciliation
9. Lens Coverage Table  10. Disposition  11. Master Action Register
12. Cross-Role Signals
```
Reordering is a contract violation.

**§9 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED tier verified before LIFECYCLE. FULLY SATURATED verified at BRACKET CLOSING.
BRACKET CLOSING may not PASS when any CH-ID is UNSATURATED without waiver.

**§10 PER-FINDING SEVERITY AGGREGATION CONTRACT (C-30)**
Section Severity = worst(F-ID severities in section). No editorial assignment.

**§11 LENS COVERAGE TABLE PROTOCOL (C-31, C-33, C-34)**
After all reviewer sections: LENS COVERAGE TABLE with ADDRESSED/OPEN per lens.verify
entry and per-entry Applicability (HIGH/MEDIUM/LOW) specific to this artifact.
HIGH-applicability OPEN entries -> ADVISORY-OPEN-LENS action items.
DOMAIN COVERAGE GAP-CHECK: artifact domains with no HIGH-applicability reviewer
-> ADVISORY-GAP action items citing domain name and gap reason.

**§12 SCOPE SURFACE DOMAIN ANNOTATION (C-36)**
Every IN-SCOPE surface carries [DOMAIN: label] at enumeration time.
C-34 gap-check sources the domain registry from these annotations directly.

**§13 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-bracket-closing SCOPE COVERAGE RECONCILIATION. GAP surfaces -> ADVISORY-GAP
action items. No gate ledger row (§6 NON-VERDICT SECTION EXCLUSION).

**§14 NH DIMENSION TABLE CONTRACT (C-35, C-37, C-38)**
BRACKET OPENING: NH Dimension Comparison Table (3 columns: A, B, C per TABLE
FORMAT CONTRACT). BRACKET CLOSING: re-populate with revised B and C values.
g_null(final) derivable from revised table values alone.

**§15 NH TABLE AGGREGATION RULE WITH LIFECYCLE EXTENSION (C-39, C-40, C-41)**
Column A: challenger's opening value, unchanged.
Column B: `avg(all DOMAIN B scores + LIFECYCLE B score)`.
Column C: `avg(all DOMAIN C scores + LIFECYCLE C score)`.
All DOMAIN sections and LIFECYCLE section emit NH Dimension Scores sub-tables per
TABLE FORMAT CONTRACT schema. BRACKET CLOSING reads sub-tables directly; no prose
extraction permitted.

**§16 DOMAIN-AGGREGATE FORMULA (C-24)**
`G_domain_agg = median(all DOMAIN gate verdicts)`. BRACKET CLOSING receives as
labeled input.

**§17 PRIMARY DRIVER DERIVATION CONTRACT (C-32)**
Precedence rule-set (first match wins): BRACKET CLOSING OVERRIDE > NULL HYPOTHESIS >
DOMAIN [first FAIL] > LIFECYCLE [FAIL] > DOMAIN [first CONDITIONAL] > LIFECYCLE
[CONDITIONAL] > CONSENSUS. Emit `Primary Driver: [value]` at DISPOSITION.

**§18 DEPTH MODE (C-08)**
`deep`: all roles. `standard`: relevant roles + rationale stated. `quick`: >= 3
roles + abbreviation note.

---

Execute sections per §8 SECTION ORDER CONTRACT. All table schemas and contract
terms declared above are binding. Acknowledge {{artifact_id}}, {{depth}},
{{reviewer_set}} before Step 1.

---

## V-03

**Axis**: Inertia framing -- STATUS QUO FRAMING CONTRACT names inertia-advocate's
specific no-build commitments as §0-CID values; CH-ID §0 grounding column cites
these values; F-ID enforced by inertia-advocate's auditability requirement

**Hypothesis**: When the inertia-advocate role is the organizing spine of the
preamble (not just a reviewer in the sequence), §0 grounding becomes a first-class
contract term naturally. The inertia-advocate names specific "status quo
commitments" (§0-C01, §0-C02, ...) in the STATUS QUO FRAMING CONTRACT before any
other preamble contract. CH-IDs are then registered as challenges to specific §0-CIDs,
and the §0 grounding column in the CH-ID table cites those §0-CID values. This is
structurally stronger than a preamble clause because the §0-CIDs are named artifacts
that can be cross-referenced. The inertia-advocate's adversarial posture also
motivates F-ID: the inertia-advocate requires named, stable finding identifiers to
audit whether each finding was actually incorporated into the disposition or could be
dismissed through positional reference instability. LIFECYCLE NH emission follows
from the architecture (§17). Predicted score: 265/265.

---

You are running `/org-review`.

Inputs:
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .craft/roles/]
```

Acknowledge injected values before executing any section.

---

### STATUS QUO FRAMING CONTRACT (inertia-advocate pre-commitment)

Before any preamble contract executes, the inertia-advocate registers specific
commitments naming why the status quo is acceptable. These are the §0 Commitments
(§0-CID values) that every CH-ID must trace to.

Register the §0-CID registry here (populated with artifact-specific values at
execution time):

```
| §0-CID | Status Quo Commitment | Strength (HIGH/MEDIUM/LOW) |
|--------|----------------------|---------------------------|
| §0-C01 | [Why not building this is acceptable for dimension 1] | [strength] |
| §0-C02 | [Why not building this is acceptable for dimension 2] | [strength] |
| §0-C03 | [Why not building this is acceptable for dimension N] | [strength] |
```

The inertia-advocate requires that: (a) every CH-ID registered below traces to a
specific §0-CID (the challenge must be probing a stated no-build commitment), and
(b) every finding row carries a stable named F-ID so that the disposition audit can
verify whether the finding overturned a specific §0 commitment or not.

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
HIGH = blocks; MEDIUM = conditions; LOW = advisory.
FAIL -> BLOCKED | >= 1 CONDITIONAL, no FAIL -> CONDITIONAL | all PASS -> READY.
OVERRIDE: OVERRIDE INVOKED: YES | NO labeled field in BRACKET CLOSING.

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (optional).
No editorial class assignment at assembly time.

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23)**
Three alternatives: Status Quo (A), Proposed Build (B), Best-Non-Build-Alt (C).
g_null = PASS iff delta_B_A > 0 AND delta_B_C > 0.
g_null = CONDITIONAL iff exactly one delta > 0.
g_null = FAIL iff both deltas <= 0.

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
g_null(initial) [BRACKET OPENING] -> g_null(post-domain) [CH-ID SATURATION CHECK]
-> g_null(final) [BRACKET CLOSING]. GClose must equal g_null(final) or declare
OVERRIDE INVOKED: YES with justification naming the overriding §0-CID commitment.

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21)**
Every verdict-emitting section (BRACKET OPENING, all DOMAIN sections, LIFECYCLE,
BRACKET CLOSING) emits a LOCAL GATE LEDGER ROW:
```
| Gate Verdict | Section Severity | Class | F-ID(s) sourcing this verdict |
```
Verbatim copy to MASTER ACTION REGISTER. No re-derivation.

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate ledger row from: preamble, scope, CH-ID registration, CH-ID saturation
check, scope coverage reconciliation, lens coverage table.

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**
MASTER ACTION REGISTER: verbatim copy only. Re-derivation prohibited.

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
STATUS QUO FRAMING CONTRACT (already executed above) precedes all §§ contracts.
Execution sequence:
```
1. Scope Declaration  2. CH-ID Registration  3. Bracket Opening
4. Domain Reviewers   5. CH-ID Saturation Check  6. Lifecycle Reviewer
7. Bracket Closing    8. Scope Coverage Reconciliation
9. Lens Coverage Table  10. Disposition  11. Master Action Register
12. Cross-Role Signals
```

**§9 FINDING IDENTIFIER CONTRACT (C-42)**
The inertia-advocate requires named, stable finding identifiers for disposition
auditability. Every finding row in every reviewer section carries:
```
| F-ID | Severity | Surface | Finding | Recommendation |
```
F-ID format: F-NN. Named field, not positional row number. All downstream
references (action register, CH-ID response columns, lens coverage citations)
use F-ID values. Referencing by row position is a contract violation.

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-43)**
CH-ID tracing table:
```
| CH-ID | Challenge Statement | §0 Grounding | [Section columns...] |
```
§0 Grounding column: cites the §0-CID value (from STATUS QUO FRAMING CONTRACT)
that this challenge is designed to probe. Every CH-ID must carry a §0-CID citation.
Challenges that cannot be grounded in a registered §0-CID are invalid.

**§11 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED: every CH-ID has >= 1 domain response (verified before LIFECYCLE).
FULLY SATURATED: domain + lifecycle responses (verified at BRACKET CLOSING).
BRACKET CLOSING may not PASS when any CH-ID is UNSATURATED without waiver.

**§12 PER-FINDING SEVERITY AGGREGATION CONTRACT (C-30)**
Section Severity = worst(F-ID severities in section). No editorial assignment.

**§13 LENS COVERAGE TABLE PROTOCOL (C-31, C-33, C-34)**
Post-execution: LENS COVERAGE TABLE with ADDRESSED/OPEN per lens.verify entry,
per-entry Applicability (HIGH/MEDIUM/LOW) specific to this artifact.
HIGH-applicability OPEN entries -> ADVISORY-OPEN-LENS action items.
DOMAIN COVERAGE GAP-CHECK: uncovered domains -> ADVISORY-GAP action items.

**§14 SCOPE SURFACE DOMAIN ANNOTATION (C-36)**
Every IN-SCOPE surface: [DOMAIN: label] at enumeration time.

**§15 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-bracket-closing SCOPE COVERAGE RECONCILIATION. GAP surfaces -> ADVISORY-GAP.
No gate ledger row.

**§16 NH DIMENSION TABLE CONTRACT (C-35, C-37, C-38)**
BRACKET OPENING: NH Dimension Comparison Table (A, B, C columns; >= 3 dimensions).
Delta B-A and Delta B-C columns. g_null(initial) derivable from deltas alone.
BRACKET CLOSING: re-populate with revised B and C values. g_null(final) from
revised table.

**§17 NH TABLE AGGREGATION RULE WITH LIFECYCLE EXTENSION (C-39, C-40, C-41)**
Column A: challenger's opening value unchanged.
Column B: avg(all DOMAIN B scores + LIFECYCLE B score).
Column C: avg(all DOMAIN C scores + LIFECYCLE C score).

DOMAIN NH SCORE EMISSION REQUIREMENT: each DOMAIN reviewer section emits NH
Dimension Scores sub-table before its gate ledger row.

LIFECYCLE NH SCORE EMISSION REQUIREMENT: LIFECYCLE reviewer section also emits NH
Dimension Scores sub-table before its gate ledger row. Same dimension rows as §16
NH Dimension Comparison Table. BRACKET CLOSING reads LIFECYCLE sub-table alongside
DOMAIN sub-tables when computing columns B and C.

**§18 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(all DOMAIN gate verdicts). Labeled input to BRACKET CLOSING.

**§19 PRIMARY DRIVER DERIVATION CONTRACT (C-32)**
Precedence rule-set: BRACKET CLOSING OVERRIDE > NULL HYPOTHESIS (§0-CID held by
challenger) > DOMAIN [first FAIL] > LIFECYCLE [FAIL] > DOMAIN [first CONDITIONAL]
> LIFECYCLE [CONDITIONAL] > CONSENSUS. Emit `Primary Driver: [value]` at DISPOSITION.

**§20 DEPTH MODE (C-08)**
deep: all roles. standard: relevant roles + rationale. quick: >= 3 roles + note.

---

Execute sections per §8 SECTION ORDER CONTRACT. The STATUS QUO FRAMING CONTRACT
§0-CID registry is the ground truth for CH-ID §0 grounding citations. Every F-ID
in finding tables is the audit trail the inertia-advocate requires to verify that
no finding was dismissed through positional instability.

---

## V-04

**Axis**: Lifecycle emphasis + Output format (two-axis)

**Hypothesis**: V-04 combines V-01's lifecycle-first §17 contract elevation (LIFECYCLE
NH SCORE EMISSION as a top-level numbered section at the same level as DOMAIN NH SCORE
EMISSION) with V-02's TABLE FORMAT CONTRACT block (all table schemas pre-declared in a
single structural block before individual §§). Two structural paths now enforce C-42
and C-43: the TABLE FORMAT CONTRACT pre-declares the CH-ID table schema with §0
Grounding column (C-43) and the finding table schema with F-ID column (C-42); the
lifecycle-first §17 ensures LIFECYCLE NH sub-table emission is an explicit numbered
contract rather than an extension clause. The redundancy is intentional: C-42 and C-43
are declared twice (once in TABLE FORMAT CONTRACT, once in the individual §§), reducing
the risk that either is missed through single-path reliance. Predicted score: 265/265.

---

You are running `/org-review`.

Inputs:
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .craft/roles/]
```

Acknowledge injected values before executing any section.

---

### TABLE FORMAT CONTRACT

All structured tables in this review conform to these schemas. Required fields
are mandatory on every row.

**Finding Table**:
```
| F-ID | Severity | Surface | Finding | Recommendation |
```
`F-ID`: named stable identifier (F-01, F-02, ...). NOT positional. All downstream
references use F-ID values. `Severity`: HIGH / MEDIUM / LOW only.

**CH-ID Challenge Table**:
```
| CH-ID | Challenge Statement | §0 Grounding | [Section columns per reviewer] |
```
`§0 Grounding`: required. Cites the preamble §§ contract section that authorizes
this challenge (e.g., "§2 CLASS DERIVATION CONTRACT"). Populated before any reviewer
runs. Challenges without §0 grounding are invalid.

**NH Dimension Scores Sub-table** (emitted per DOMAIN and LIFECYCLE section):
```
| Dimension | B: Proposed-Build | C: Best-Non-Build-Alt |
```

**NH Dimension Comparison Table** (BRACKET OPENING and BRACKET CLOSING):
```
| Dimension | A: Status-Quo | B: Proposed-Build | C: Best-Non-Build-Alt | Delta B-A | Delta B-C |
```

**LOCAL GATE LEDGER ROW**:
```
| Gate Verdict | Section Severity | Class | F-ID(s) sourcing this verdict |
```

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
HIGH = blocks; MEDIUM = conditions; LOW = advisory.
FAIL -> BLOCKED | >= 1 CONDITIONAL, no FAIL -> CONDITIONAL | all PASS -> READY.
OVERRIDE: OVERRIDE INVOKED: YES | NO in BRACKET CLOSING.

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (optional).

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23)**
Three alternatives (A, B, C). g_null = PASS iff delta_B_A > 0 AND delta_B_C > 0.

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
g_null(initial) [BRACKET OPENING] -> g_null(post-domain) [SATURATION CHECK]
-> g_null(final) [BRACKET CLOSING]. GClose = g_null(final) or OVERRIDE INVOKED: YES.

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21)**
Universal coverage (BRACKET OPENING + all DOMAIN + LIFECYCLE + BRACKET CLOSING).
Schema per TABLE FORMAT CONTRACT. Verbatim copy to MASTER ACTION REGISTER.

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate ledger row from: preamble, scope, CH-ID registration, CH-ID saturation
check, scope coverage reconciliation, lens coverage table.

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**
MASTER ACTION REGISTER: verbatim copy. Re-derivation of Gate Verdict or Class
prohibited.

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
1. Scope Declaration  2. CH-ID Registration  3. Bracket Opening
4. Domain Reviewers   5. CH-ID Saturation Check  6. Lifecycle Reviewer
7. Bracket Closing    8. Scope Coverage Reconciliation  9. Lens Coverage Table
10. Disposition  11. Master Action Register  12. Cross-Role Signals
```

**§9 FINDING IDENTIFIER CONTRACT (C-42)**
Finding table schema: `| F-ID | Severity | Surface | Finding | Recommendation |`
F-ID is a named stable identifier (see TABLE FORMAT CONTRACT). Required on every
finding row in every reviewer section. All downstream references use F-ID values.

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-43)**
CH-ID table schema per TABLE FORMAT CONTRACT. §0 Grounding column required.
Cites the preamble §§ contract section authorizing each challenge. Populated at
registration time before any reviewer runs.

**§11 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED before LIFECYCLE. FULLY SATURATED at BRACKET CLOSING. BRACKET CLOSING
may not PASS when any CH-ID is UNSATURATED without waiver.

**§12 PER-FINDING SEVERITY AGGREGATION CONTRACT (C-30)**
Section Severity = worst(F-ID severities in section).

**§13 LENS COVERAGE TABLE PROTOCOL (C-31, C-33, C-34)**
ADDRESSED/OPEN per lens.verify entry. Applicability (HIGH/MEDIUM/LOW) per entry.
HIGH-applicability OPEN -> ADVISORY-OPEN-LENS items.
DOMAIN COVERAGE GAP-CHECK -> ADVISORY-GAP items.

**§14 SCOPE SURFACE DOMAIN ANNOTATION (C-36)**
Every IN-SCOPE surface: [DOMAIN: label] at enumeration time.

**§15 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-bracket-closing reconciliation. GAP surfaces -> ADVISORY-GAP. No ledger row.

**§16 NH DIMENSION TABLE CONTRACT (C-35, C-37, C-38)**
BRACKET OPENING: NH Dimension Comparison Table per TABLE FORMAT CONTRACT (A, B, C
columns, >= 3 dimensions). BRACKET CLOSING: re-populate columns B and C.
g_null(initial) and g_null(final) derivable from table values alone.

**§17 NH TABLE AGGREGATION RULE (C-39, C-40, C-41)**

Column aggregation formula (pre-committed):
```
Column A: challenger's opening value, unchanged.
Column B: avg(all DOMAIN B scores + LIFECYCLE B score)
Column C: avg(all DOMAIN C scores + LIFECYCLE C score)
```

**DOMAIN NH SCORE EMISSION REQUIREMENT (C-40)**: every DOMAIN reviewer section emits
NH Dimension Scores sub-table per TABLE FORMAT CONTRACT schema before its gate ledger
row. BRACKET CLOSING reads domain sub-tables directly for column B and C computation.

**LIFECYCLE NH SCORE EMISSION REQUIREMENT (C-41)**: LIFECYCLE reviewer section emits
NH Dimension Scores sub-table per TABLE FORMAT CONTRACT schema before its gate ledger
row. Same dimension rows as §16 NH Dimension Comparison Table. BRACKET CLOSING reads
LIFECYCLE sub-table alongside DOMAIN sub-tables when computing columns B and C. No
prose extraction from the lifecycle section in the NH aggregation chain.

**§18 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(all DOMAIN gate verdicts). Labeled input to BRACKET CLOSING.

**§19 PRIMARY DRIVER DERIVATION CONTRACT (C-32)**
Precedence: BRACKET CLOSING OVERRIDE > NULL HYPOTHESIS > DOMAIN [first FAIL] >
LIFECYCLE [FAIL] > DOMAIN [first CONDITIONAL] > LIFECYCLE [CONDITIONAL] > CONSENSUS.
Emit `Primary Driver: [value]` at DISPOSITION.

**§20 DEPTH MODE (C-08)**
deep: all roles. standard: relevant + rationale. quick: >= 3 + note.

---

Execute sections per §8 SECTION ORDER CONTRACT. TABLE FORMAT CONTRACT schemas
and §§ contracts are both binding; the TABLE FORMAT CONTRACT is the structural
declaration, the §§ contracts are the behavioral contracts. They are not redundant
but complementary: schema declares the column; contract declares the requirement.

---

## V-05

**Axis**: Lifecycle emphasis + Output format + Inertia framing (three-axis)

**Hypothesis**: V-05 combines all three single-axis patterns. The STATUS QUO
FRAMING CONTRACT (V-03 axis) names specific §0-CID commitments that serve as the
grounding values for the CH-ID table §0 Grounding column. The TABLE FORMAT CONTRACT
(V-02 axis) pre-declares the finding table with F-ID and the CH-ID table with §0
Grounding column, anchoring C-42 and C-43 at the schema level. The lifecycle-first
§17 (V-01 axis) elevates LIFECYCLE NH SCORE EMISSION as an explicit numbered contract,
not an extension clause, anchoring C-41 at the behavioral contract level. The three
axes are mutually reinforcing: the inertia framing populates the §0-CID registry that
the CH-ID table schema declares a column for, and the lifecycle elevation ensures the
NH aggregation formula explicitly includes the lifecycle sub-table as a named input
alongside domain sub-tables. Predicted score: 265/265.

---

You are running `/org-review`.

Inputs:
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .craft/roles/]
```

Acknowledge injected values before executing any section.

---

### STATUS QUO FRAMING CONTRACT (inertia-advocate pre-commitment)

Before any table schemas or §§ contracts are declared, register the status quo
commitments that justify not building {{artifact_id}}. These §0-CID values are
the ground truth for all CH-ID challenge grounding citations.

```
| §0-CID | Status Quo Commitment (why not building this is acceptable) | Strength |
|--------|-----------------------------------------------------------|----------|
| §0-C01 | [dimension 1: current capability or process that covers this need] | [HIGH/MEDIUM/LOW] |
| §0-C02 | [dimension 2: cost / risk / complexity argument for status quo] | [HIGH/MEDIUM/LOW] |
| §0-C03 | [dimension N: ...] | [HIGH/MEDIUM/LOW] |
```

Populate this table with artifact-specific values before executing any other section.
Every challenge registered in the CH-ID table must trace to a §0-CID from this
registry. Every finding must carry a named F-ID so the disposition audit can verify
whether the finding overturned a specific §0 commitment.

---

### TABLE FORMAT CONTRACT

All structured tables conform to these schemas.

**Finding Table** (all reviewer sections):
```
| F-ID | Severity | Surface | Finding | Recommendation |
```
F-ID: named stable identifier (F-01, F-02, ...). NOT positional row number.
All downstream references (action register, CH-ID response columns, lens coverage
citations) use F-ID values. Positional row references are contract violations.

**CH-ID Challenge Table** (registered before BRACKET OPENING):
```
| CH-ID | Challenge Statement | §0 Grounding | [Section response columns] |
```
§0 Grounding: required. Cites the §0-CID value from STATUS QUO FRAMING CONTRACT
that this challenge probes (e.g., "§0-C01 -- tests whether dimension 1 coverage
argument holds under the proposed build"). Every CH-ID must carry a §0-CID citation.

**NH Dimension Scores Sub-table** (DOMAIN and LIFECYCLE sections):
```
| Dimension | B: Proposed-Build | C: Best-Non-Build-Alt |
```
Same dimension rows as STATUS QUO FRAMING CONTRACT §0-CID dimensions where applicable.

**NH Dimension Comparison Table** (BRACKET OPENING and BRACKET CLOSING):
```
| Dimension | A: Status-Quo | B: Proposed-Build | C: Best-Non-Build-Alt | Delta B-A | Delta B-C |
```
Column A values initialized from STATUS QUO FRAMING CONTRACT strength ratings.

**LOCAL GATE LEDGER ROW** and **MASTER ACTION REGISTER ROW**: per V-04 TABLE FORMAT
CONTRACT.

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
HIGH = blocks; MEDIUM = conditions; LOW = advisory.
FAIL -> BLOCKED | >= 1 CONDITIONAL, no FAIL -> CONDITIONAL | all PASS -> READY.
OVERRIDE: OVERRIDE INVOKED: YES | NO in BRACKET CLOSING, naming the §0-CID being
overridden.

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (optional).

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23)**
Three alternatives (A, B, C). g_null = PASS iff delta_B_A > 0 AND delta_B_C > 0.
g_null = CONDITIONAL iff exactly one delta > 0. g_null = FAIL iff both <= 0.

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
g_null(initial) [BRACKET OPENING] -> g_null(post-domain) [CH-ID SATURATION CHECK]
-> g_null(final) [BRACKET CLOSING]. GClose = g_null(final) or OVERRIDE INVOKED: YES.

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21)**
Universal coverage: BRACKET OPENING + all DOMAIN + LIFECYCLE + BRACKET CLOSING.
Schema per TABLE FORMAT CONTRACT. Verbatim copy to MASTER ACTION REGISTER.

**§6 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate ledger row from: STATUS QUO FRAMING CONTRACT, TABLE FORMAT CONTRACT, §§
preamble, scope declaration, CH-ID registration, CH-ID saturation check, scope
coverage reconciliation, lens coverage table.

**§7 VERBATIM ASSEMBLY PROHIBITION (C-20)**
MASTER ACTION REGISTER: verbatim copy only. Re-derivation prohibited.

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
[STATUS QUO FRAMING CONTRACT -- pre-execution, already complete]
[TABLE FORMAT CONTRACT -- pre-execution, already complete]
[§§ PREAMBLE -- pre-execution, already complete]
1. Scope Declaration  2. CH-ID Registration  3. Bracket Opening
4. Domain Reviewers   5. CH-ID Saturation Check  6. Lifecycle Reviewer
7. Bracket Closing    8. Scope Coverage Reconciliation  9. Lens Coverage Table
10. Disposition  11. Master Action Register  12. Cross-Role Signals
```

**§9 FINDING IDENTIFIER CONTRACT (C-42)**
F-ID: named stable identifier. Required on every finding row per TABLE FORMAT
CONTRACT. All downstream references use F-ID values. Connects to §0-CID audit:
the inertia-advocate traces each finding's F-ID to determine whether it overturned
a specific §0-CID strength claim.

**§10 CH-ID CHALLENGE REGISTRATION (C-04, C-43)**
CH-ID table per TABLE FORMAT CONTRACT. §0 Grounding: cites §0-CID value from STATUS
QUO FRAMING CONTRACT registry. Populated at registration time before any reviewer
runs. Two-axis traceability: backward to §0-CID commitment (§0 Grounding column),
forward to reviewer responses (section columns).

**§11 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED before LIFECYCLE. FULLY SATURATED at BRACKET CLOSING. BRACKET CLOSING
may not PASS when any CH-ID is UNSATURATED without waiver citing §0-CID justification.

**§12 PER-FINDING SEVERITY AGGREGATION CONTRACT (C-30)**
Section Severity = worst(F-ID severities in section).

**§13 LENS COVERAGE TABLE PROTOCOL (C-31, C-33, C-34)**
ADDRESSED/OPEN per lens.verify entry. Applicability (HIGH/MEDIUM/LOW) per entry.
HIGH-applicability OPEN -> ADVISORY-OPEN-LENS items (with F-ID placeholder: F-OL-NN).
DOMAIN COVERAGE GAP-CHECK: uncovered domains -> ADVISORY-GAP items.

**§14 SCOPE SURFACE DOMAIN ANNOTATION (C-36)**
Every IN-SCOPE surface: [DOMAIN: label]. Domain registry consumed by §13 gap-check.

**§15 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-bracket-closing SCOPE COVERAGE RECONCILIATION. GAP surfaces -> ADVISORY-GAP
items (with F-ID placeholder: F-SG-NN). No gate ledger row.

**§16 NH DIMENSION TABLE CONTRACT (C-35, C-37, C-38)**
BRACKET OPENING: NH Dimension Comparison Table per TABLE FORMAT CONTRACT. Column A
values initialized from STATUS QUO FRAMING CONTRACT §0-CID strength ratings.
BRACKET CLOSING: re-populate columns B and C per §17 aggregation formula.
g_null(initial) and g_null(final) derivable from table values alone.

**§17 NH TABLE AGGREGATION RULE (C-39, C-40, C-41)**

Column aggregation (pre-committed):
```
Column A: challenger's §16 opening values, unchanged.
Column B: avg(all DOMAIN B scores + LIFECYCLE B score)
Column C: avg(all DOMAIN C scores + LIFECYCLE C score)
```

**DOMAIN NH SCORE EMISSION REQUIREMENT (C-40)**: every DOMAIN reviewer section emits
NH Dimension Scores sub-table per TABLE FORMAT CONTRACT before its gate ledger row.

**LIFECYCLE NH SCORE EMISSION REQUIREMENT (C-41)**: LIFECYCLE reviewer section emits
NH Dimension Scores sub-table per TABLE FORMAT CONTRACT before its gate ledger row.
Same dimension rows as §16 table. BRACKET CLOSING reads LIFECYCLE sub-table alongside
DOMAIN sub-tables. No prose extraction permitted at any step in the NH aggregation
chain. The lifecycle reviewer's perspective on the proposed-build vs. best-non-build-alt
dimensions is a structured, named input to the bracket closing computation.

**§18 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(all DOMAIN gate verdicts). Labeled input to BRACKET CLOSING.

**§19 PRIMARY DRIVER DERIVATION CONTRACT (C-32)**
Precedence: BRACKET CLOSING OVERRIDE (naming §0-CID overridden) > NULL HYPOTHESIS
(§0-CID held) > DOMAIN [first FAIL] > LIFECYCLE [FAIL] > DOMAIN [first CONDITIONAL]
> LIFECYCLE [CONDITIONAL] > CONSENSUS.
Emit `Primary Driver: [value]` at DISPOSITION, referencing §0-CID where applicable.

**§20 DEPTH MODE (C-08)**
deep: all roles. standard: relevant + rationale. quick: >= 3 + note.

---

Execute sections per §8 SECTION ORDER CONTRACT. The STATUS QUO FRAMING CONTRACT
§0-CID registry, the TABLE FORMAT CONTRACT schemas, and the §§ behavioral contracts
form a three-layer pre-commitment architecture. §0-CID values flow through: (a)
CH-ID §0 Grounding citations, (b) NH Dimension Table Column A initialization, (c)
BRACKET CLOSING OVERRIDE justification when invoked, and (d) PRIMARY DRIVER
attribution language. F-ID values flow through: finding tables -> action register ->
CH-ID response tracking -> lens coverage citations -> disposition audit chain.
LIFECYCLE B and C scores flow through: LIFECYCLE NH sub-table -> §17 aggregation
formula -> BRACKET CLOSING NH Dimension Table re-population -> g_null(final).
All three new C-41/C-42/C-43 criteria are enforced by named, cross-referencing
structural commitments rather than isolated contract clauses.
