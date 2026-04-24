I have everything I need. The existing variate files target a different rubric track (/26 system with Phase 9b risk propagation). The v11 rubric I need to target is the /30 system with OPTION ANATOMY CONTRACT, CAUSAL CHAIN CONTRACT, PREREQUISITE GATE dual-contract coverage (C-36, C-37). The R11 variate for this system doesn't exist yet — writing it from scratch.

---

# draft-proposal Variate — Round 11

Rubric version: v11 · Formula: /30 · New criteria: C-36 (PREREQUISITE GATE extension for Phase 0 option anatomy contract verification), C-37 (PREREQUISITE GATE dual-contract coverage)

Single-axis variations first (V-01..V-03), then combinations (V-04..V-05).

Axes explored:
- **V-01**: Role sequence (Architect-first) — designed fail: C-34, C-36, C-37 (causal contract present, anatomy contract absent)
- **V-02**: Output format (compact tables, PM-first) — designed fail: C-33, C-35, C-37 (anatomy contract present, causal contract absent)
- **V-03**: Lifecycle emphasis (split-gate) — designed fail: C-37 alone (both binaries present in separate blocks, not co-present)
- **V-04**: Phrasing register (conversational) — designed fail: C-25 alone (T-GUARD listed last, not first)
- **V-05**: Inertia framing + motivated — designed pass: C-28–C-37 all pass → 30/30 → 100.0

Predicted scores: V-01 → 99.33 · V-02 → 99.33 · V-03 → 99.67 · V-04 → 99.67 · V-05 → 100.0

---

## V-01 — Architect-First | Axis: Role Sequence | Designed fail: C-34, C-36, C-37

**Hypothesis**: An Architect-first variation declares a Phase 0 CAUSAL CHAIN CONTRACT (`TEMPORAL ANCHOR − INERTIA OFFSET = DECISION LEAD TIME`) with source attribution and T-GUARD routing rule (C-33 PASS). The PREREQUISITE GATE includes a causal chain contract binary (C-35 PASS). However, the option anatomy template embeds `PM FRAMING:` and `ARCHITECT VALIDATION:` as the first two typed slots in every option (C-32 PASS) without a Phase 0 OPTION ANATOMY CONTRACT declaring that structure prospectively (C-34 FAIL). Because C-34 fails, the gate has no anatomy contract binary to include (C-36 FAIL). Because C-36 fails, the gate holds only one Phase 0 contract binary — asymmetric auditability — and C-37 fails. Two open triggers at finalization: T-34 and T-36/T-37 cascade. PM sign-off block appears first in recommendation (C-28 PASS). T-GUARD listed first in amendment table (C-25 PASS). Score: 27/30 aspirational pass → composite 99.00.

```
ROLE SEQUENCE: Architect → PM

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- Architect: Leads option framing, register construction, Phase 0 causal contract,
  gate audit, feasibility validation.
- PM: Leads business framing, adoption trade-off commentary, amend phase, and
  recommendation rationale.

---

PHASE 0 — PRE-DOCUMENT INITIALIZATION

Architect: Declare the role sequence (Architect → PM) as a typed header at the top
of the output. Apply this sequence in every subsequent phase header.

AMENDMENT TRACKING TABLE — initialize now, before any content phase executes.

Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
Rows: T-GUARD first, then T-01 through T-37. Total: 38 rows.

T-GUARD: Scope = "any required typed slot, phase block, or gate item absent from
the document — catches all structural gaps not covered by a specific T-NN trigger."
T-GUARD PHASE = PRE-DOCUMENT. STATUS = PENDING.

T-01..T-37: One trigger row per rubric criterion C-01..C-37. Assign a PHASE value
to every row (PRE-DOCUMENT, OPTION COMPOSITION, FINALIZATION, or named phase).
Leave STATUS = PENDING for all rows at initialization.

COMPLETION STATUS slot: Add a COMPLETION STATUS field to the amendment table,
initialized to: "PENDING — document in progress."

PHASE MANIFEST — list all phases to be produced, in sequence:
  Phase 0: PRE-DOCUMENT INITIALIZATION
  Phase 1: DECISION FRAMING
  Phase 2: SCOUT ARTIFACT INVENTORY
  Phase 3: OPTION COMPOSITION
  Phase 4: ASSUMPTION REGISTER
  Phase 5: RISK REGISTER
  Phase 6: FAILURE MODE REGISTER
  Phase 7: COMPARISON MATRIX
  Phase 8: AMEND PHASE
  Phase 9: INERTIA OFFSET + DECISION LEAD TIME
  Phase 10: PREREQUISITE GATE
  Phase 11: RECOMMENDATION
  Phase 12: FINALIZATION

CAUSAL CHAIN CONTRACT — declare at Phase 0 before any term-contributing phase:

  CONTRACT: TEMPORAL ANCHOR − INERTIA OFFSET = DECISION LEAD TIME
  SOURCE — TEMPORAL ANCHOR: Phase 1 (DECISION FRAMING), TEMPORAL ANCHOR field.
  SOURCE — INERTIA OFFSET: Phase 3 (OPTION COMPOSITION), do-nothing option
    INERTIA COST field; each alternative's INERTIA OFFSET field.
  T-GUARD ROUTING: If TEMPORAL ANCHOR is absent at Phase 1 or INERTIA OFFSET is
    absent from any alternative at Phase 3, T-GUARD fires at Phase 0 initialization
    rather than deferring to the recommendation phase.

[NOTE: No OPTION ANATOMY CONTRACT block is declared in this variation. The option
anatomy template embeds PM FRAMING: and ARCHITECT VALIDATION: as typed slots
directly in the Phase 3 template, without a Phase 0 prospective declaration.]

---

PHASE 1 — DECISION FRAMING

Architect: State the decision context using the following typed fields:

  PROBLEM: [shared problem all options address]
  TEMPORAL ANCHOR: [specific named date, sprint, or event — vague language
    such as "soon" or "in the near term" is not permitted]
  INACTION CONSEQUENCE: [concrete named outcome of not deciding — teams blocked,
    capability lost, or window closed; "missed feature" statements do not qualify]
  DECISION REQUIRED: [the question being decided]

PM: Confirm the framing captures business urgency and stakeholder stakes.

---

PHASE 2 — SCOUT ARTIFACT INVENTORY

PM: Before composing any option, inventory available signal artifacts.

SCOUT INVENTORY:
  Available artifacts: [list each artifact found by name and finding]
  Absent artifacts: [list expected artifact types not available]
  Fallback: [if no scout artifacts exist, state an inline assessment substituting
    for each missing artifact category]

---

PHASE 3 — OPTION COMPOSITION

Compose at least 3 options. The do-nothing (status-quo) option must be included.

For each option, use this anatomy template:

  OPTION [label]: [description]
  PM FRAMING: [PM states the business case — value proposition, adoption path,
    and business risk category for this option]
  ARCHITECT VALIDATION: [Architect states technical constraints, integration
    dependencies, and technical risk category for this option]
  PROS: [bulleted strengths]
  CONS: [bulleted weaknesses]
  RISK: [risk summary — register linkage added in Phase 9]
  EFFORT: [timeline and team or dependency requirements]
  RATIONALE: [why this option belongs in the shortlist]

Do-nothing option additionally requires:
  INERTIA COST: [per-sprint numeric P×I value using the 1-5 scale defined in
    Phase 5 anchors — compute as P×I where P = probability of inertia compounding
    and I = impact of each compounding cycle]

Non-do-nothing alternatives additionally require:
  INERTIA OFFSET: [the sprint at which cumulative implementation cost equals
    cumulative inertia cost of not acting — to be computed in Phase 9]

---

PHASE 4 — ASSUMPTION REGISTER

Architect: Build the assumption register as a structured table:

  A-NN | ASSUMPTION | VALIDATION PLAN

At least 3 entries. Each VALIDATION PLAN names the method and owner for validating
the assumption before the recommendation becomes binding.
PM: Add at least one adoption-related assumption.

---

PHASE 5 — RISK REGISTER

Architect: Define project-specific scoring anchors before any entry is scored:

  P=1: [project-specific definition]  P=3: [project-specific definition]  P=5: [project-specific definition]
  I=1: [project-specific definition]  I=3: [project-specific definition]  I=5: [project-specific definition]

Build the risk register as a structured table:

  R-NN | RISK | P | I | P×I | MITIGATION

At least 4 entries. P and I on 1-5 scale. P×I compound score computed and stated.
PM: Add at least one adoption or schedule risk entry.

---

PHASE 6 — FAILURE MODE REGISTER

Architect: Build the failure mode register as a structured table:

  F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION

At least 3 entries. Each row names the exact condition under which the failure
mode activates and a named escalation path or mitigation action.
PM: Add at least one business-process failure mode (adoption collapse, budget cut).

---

PHASE 7 — COMPARISON MATRIX

Build a comparison matrix with OPTIONS as column headers.
Rows (dimensions): Effort | Risk (P×I cited) | Time-to-value | Reversibility |
  Inertia cost baseline (do-nothing P×I) | PM adoption friction

PM leads dimension selection. Architect validates technical dimension scoring.
Score or characterize each cell consistently across all options.

---

PHASE 8 — AMEND PHASE

Self-audit the proposal using three required categories. Each entry uses this template:

MISSING OPTION:
  OPTION: [a candidate option not explored in Phase 3]
  OWNER: [name or role responsible for investigating]
  DEADLINE: [specific sprint name, date, or milestone — "TBD" does not satisfy]

UNWEIGHTED CRITERION:
  CRITERION: [a decision dimension that was equally weighted but should be
    recalibrated for this context]
  OWNER: [name or role responsible for recalibrating]
  DEADLINE: [specific sprint name, date, or milestone]

FOLLOW-UP:
  ACTION: [next step required before the recommendation is binding]
  OWNER: [name or role responsible]
  DEADLINE: [specific sprint name, date, or milestone]

At least one entry per category. OWNER and DEADLINE appear as typed slots in every
entry across all three categories.

---

PHASE 9 — INERTIA OFFSET AND DECISION LEAD TIME

For each non-do-nothing alternative, compute:

  INERTIA OFFSET: [sprint N at which cumulative implementation cost = do-nothing
    INERTIA COST × N]
  DECISION LEAD TIME: TEMPORAL ANCHOR sprint − INERTIA OFFSET sprint
    = [computed value in sprints]
  Positive lead time: team has runway to act.
  Zero or negative lead time: alternative has entered an inertia trap.

ESCALATION FLAG: If any alternative's DECISION LEAD TIME is zero or negative,
add a typed ESCALATION FLAG field on that option naming the inertia trap condition.

---

PHASE 10 — PREREQUISITE GATE

Verify all gate conditions before the recommendation phase. Each item is a named
binary: COMPLETE or NOT COMPLETE.

  [ ] Assumption register: at least 3 A-NN entries with VALIDATION PLAN — COMPLETE / NOT COMPLETE
  [ ] Risk register: at least 4 R-NN entries with P, I, P×I computed — COMPLETE / NOT COMPLETE
  [ ] Failure mode register: at least 3 F-NN entries with canonical column labels — COMPLETE / NOT COMPLETE
  [ ] Register ordering: all three registers appear before Phase 11 in phase manifest sequence — COMPLETE / NOT COMPLETE
  [ ] Inertia axis: INERTIA COST present on do-nothing option; at least one alternative names INERTIA OFFSET — COMPLETE / NOT COMPLETE
  [ ] Lead-time axis: DECISION LEAD TIME computed per alternative; ESCALATION FLAG on any zero/negative result — COMPLETE / NOT COMPLETE
  [ ] Phase 0 causal chain contract: TEMPORAL ANCHOR − INERTIA OFFSET = DECISION LEAD TIME formula declared at Phase 0 with source attribution and T-GUARD routing rule — COMPLETE / NOT COMPLETE

[NOTE: No Phase 0 option anatomy contract binary is included in this gate. C-34
was not satisfied — the gate cannot verify anatomy contract presence from this
block; a reviewer must scroll to Phase 0 to confirm whether a contract exists.]

---

PHASE 11 — RECOMMENDATION

PM SIGN-OFF:
  RECOMMENDED OPTION: [name the option]
  RATIONALE: [cite at least two comparison matrix dimensions]
  CONDITIONS: [qualifying conditions — reference at least one F-NN by ID]
  F-ROW ANCHOR: [the F-row whose trigger condition most directly invalidates
    this PM sign-off if it fires]

ARCHITECT SIGN-OFF:
  TECHNICAL FEASIBILITY: [confirm the recommended option is technically viable]
  CONSTRAINTS: [any technical preconditions for the recommendation to hold]
  F-ROW ANCHOR: [the F-row whose trigger condition most directly invalidates
    this Architect sign-off if it fires]

---

PHASE 12 — FINALIZATION

Execute coverage verification as an explicitly numbered four-step list:

Step 1: Review the amendment table for trigger rules with STATUS = OPEN.
  For each open trigger T-NN, produce a finding entry:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing from this document]."
  Enumerate sequentially. One finding per trigger. Do not bundle.

Step 2: Verify all E-tier criteria (C-01..C-04) are satisfied. Update coverage
  table STATUS for any E-tier criterion found incomplete.

Step 3: Verify all R-tier criteria (C-05..C-07) are satisfied. Update coverage
  table STATUS for any R-tier criterion found incomplete.

Step 4: Update the amendment table COMPLETION STATUS field:
  If no open triggers: "T-GUARD enforced all requirements successfully —
    no violations detected."
  If open triggers exist: list each open T-NN and its finding number.

---

AMENDMENT TABLE SPECIFICATION

T-GUARD: Scope = any required typed slot, phase block, or gate item absent.
  PHASE = PRE-DOCUMENT. Must appear as row 1 (before T-01).

T-01..T-37: One row per criterion C-01..C-37. Total rows: 38 (T-GUARD + T-01..T-37).
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE

Key phase assignments:
  T-GUARD PHASE = PRE-DOCUMENT
  T-25  PHASE = PRE-DOCUMENT  (fires if T-GUARD is not listed first in trigger table)
  T-26  PHASE = PRE-DOCUMENT  (fires if COMPLETION STATUS slot absent at Phase 0)
  T-28  PHASE = FINALIZATION  (fires if Architect sign-off block appears before PM)
  T-32  PHASE = OPTION COMPOSITION  (fires if PM FRAMING: is not the first typed
                                      field in any option anatomy entry)
  T-33  PHASE = PRE-DOCUMENT  (fires if no Phase 0 causal chain contract declared)
  T-34  PHASE = PRE-DOCUMENT  (fires if no Phase 0 option anatomy contract declared)
  T-35  PHASE = FINALIZATION  (fires if PREREQUISITE GATE omits causal chain binary)
  T-36  PHASE = FINALIZATION  (fires if PREREQUISITE GATE omits anatomy contract binary)
  T-37  PHASE = FINALIZATION  (fires if PREREQUISITE GATE does not contain BOTH Phase 0
                                contract binaries in the same gate block)

T-34 fires because no Phase 0 OPTION ANATOMY CONTRACT block was declared (C-34 FAIL).
T-36 fires because no anatomy contract binary exists in the PREREQUISITE GATE (C-36 FAIL).
T-37 fires because the gate holds only one Phase 0 contract binary (C-37 FAIL).
Three open triggers at finalization: T-34, T-36, T-37.

COMPLETION STATUS: initialized "PENDING — document in progress."
At document completion update to final state.
```

---

## V-02 — PM-First, Compact Tables | Axis: Output Format | Designed fail: C-33, C-35, C-37

**Hypothesis**: A compact-table variation with PM leading declares a Phase 0 OPTION ANATOMY CONTRACT naming `PM FRAMING:` as the first required field with `ARCHITECT VALIDATION:` second and a named T-34 trigger for role-slot violations (C-34 PASS). The PREREQUISITE GATE includes a binary confirming anatomy contract presence (C-36 PASS). However, no Phase 0 CAUSAL CHAIN CONTRACT is declared (C-33 FAIL) — the TEMPORAL ANCHOR and INERTIA OFFSET fields appear correctly at their source phases but no prospective initialization contract declares the computation chain before those phases execute. Because C-33 fails, the gate has no causal chain binary to include (C-35 FAIL). Because C-35 fails, the gate holds only the anatomy binary — asymmetric auditability — and C-37 fails. Two open triggers at finalization: T-33, T-35/T-37 cascade. T-GUARD first in amendment table (C-25 PASS). Score: 27/30 aspirational pass → composite 99.00.

```
ROLE SEQUENCE: PM → Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

OUTPUT FORMAT: Compact tables throughout. Minimize prose between tables.
Concise cell values. Each phase produces a table or structured block.

ROLE ASSIGNMENTS:
- PM: Leads business framing, option anatomy (PM FRAMING: slots), recommendation,
  amend phase.
- Architect: Leads register construction, gate audit, technical feasibility.

---

PHASE 0 — PRE-DOCUMENT INITIALIZATION

PM: Declare role sequence (PM → Architect) as a typed header. Apply in all phase headers.

AMENDMENT TRACKING TABLE — initialize now:

Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
Rows: T-GUARD first, then T-01..T-37. Total: 38 rows.

T-GUARD: Scope = "any required typed slot, phase block, or gate item absent."
  PHASE = PRE-DOCUMENT. STATUS = PENDING.

T-01..T-37: One trigger per criterion. Assign PHASE value per row. STATUS = PENDING.

COMPLETION STATUS: "PENDING — document in progress."

PHASE MANIFEST:
  Phase 0: PRE-DOCUMENT INITIALIZATION
  Phase 1: DECISION FRAMING
  Phase 2: SCOUT ARTIFACT INVENTORY
  Phase 3: OPTION COMPOSITION
  Phase 4: ASSUMPTION REGISTER
  Phase 5: RISK REGISTER
  Phase 6: FAILURE MODE REGISTER
  Phase 7: COMPARISON MATRIX
  Phase 8: AMEND PHASE
  Phase 9: INERTIA OFFSET + DECISION LEAD TIME
  Phase 10: PREREQUISITE GATE
  Phase 11: RECOMMENDATION
  Phase 12: FINALIZATION

OPTION ANATOMY CONTRACT — declare now, before any option is authored:

  CONTRACT: Every option entry must include the following fields in this order:
    1. PM FRAMING: [required — first typed field in every option entry]
    2. ARCHITECT VALIDATION: [required — second typed field in every option entry]
    3. PROS, CONS, RISK, EFFORT, RATIONALE [follow in any order]
  T-34 TRIGGER: Fires if PM FRAMING: is absent, out of sequence, or follows a
    non-role typed field in any option entry.

[NOTE: No CAUSAL CHAIN CONTRACT is declared in this variation. TEMPORAL ANCHOR
and INERTIA OFFSET will appear at their source phases, but no Phase 0 block
declares the computation chain prospectively. C-33 is not satisfied.]

---

PHASE 1 — DECISION FRAMING

PM compact block:

  PROBLEM: [shared problem]
  TEMPORAL ANCHOR: [specific named date, sprint, or event]
  INACTION CONSEQUENCE: [concrete named outcome — teams blocked, capability lost]
  DECISION REQUIRED: [the question being decided]

Architect: Note technical constraints that bound the decision space.

---

PHASE 2 — SCOUT ARTIFACT INVENTORY

PM: Compact inventory block:

  AVAILABLE: [artifact name — finding summary] (repeat per artifact)
  ABSENT: [artifact type — fallback assessment] (repeat per missing type)

---

PHASE 3 — OPTION COMPOSITION

Minimum 3 options including do-nothing. Do-nothing appears as Option A.

For each option, produce a compact anatomy block using the Phase 0 contract:

  OPTION [label]: [brief description]
  PM FRAMING: [PM business case — value proposition and adoption risk category]
  ARCHITECT VALIDATION: [technical constraints and technical risk category]
  PROS: [bulleted]
  CONS: [bulleted]
  RISK: [risk category — register linkage added in Phase 9 — compact label only]
  EFFORT: [timeline and dependency summary]
  RATIONALE: [one sentence]

Do-nothing option additionally requires:
  INERTIA COST: [per-sprint P×I value using Phase 5 anchors]

Alternatives additionally require:
  INERTIA OFFSET: [sprint crossover point — computed in Phase 9]

---

PHASE 4 — ASSUMPTION REGISTER

Compact table:
  A-NN | ASSUMPTION | VALIDATION PLAN

At least 3 entries. PM leads adoption assumptions. Architect leads technical.

---

PHASE 5 — RISK REGISTER

Define anchors (compact inline): P=1/3/5 and I=1/3/5 project-specific definitions.

Compact table:
  R-NN | RISK | P | I | P×I | MITIGATION

At least 4 entries. PM adds adoption/schedule risks.

---

PHASE 6 — FAILURE MODE REGISTER

Compact table:
  F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION

At least 3 entries. Canonical column labels required.

---

PHASE 7 — COMPARISON MATRIX

Compact matrix — OPTIONS as column headers.
Rows: Effort | Risk (P×I) | Time-to-value | Reversibility | Inertia baseline | Adoption friction

---

PHASE 8 — AMEND PHASE

Three required categories. Each entry uses this compact template:

MISSING OPTION:
  OPTION: [unexplored candidate]
  OWNER: [role]
  DEADLINE: [specific sprint or date]

UNWEIGHTED CRITERION:
  CRITERION: [dimension needing recalibration]
  OWNER: [role]
  DEADLINE: [specific sprint or date]

FOLLOW-UP:
  ACTION: [next step]
  OWNER: [role]
  DEADLINE: [specific sprint or date]

At least one entry per category.

---

PHASE 9 — INERTIA OFFSET AND DECISION LEAD TIME

For each non-do-nothing alternative:

  INERTIA OFFSET: [sprint N]
  DECISION LEAD TIME: TEMPORAL ANCHOR − INERTIA OFFSET = [value in sprints]
  ESCALATION FLAG: [if zero or negative: name the inertia trap condition]

---

PHASE 10 — PREREQUISITE GATE

Named binaries — COMPLETE or NOT COMPLETE:

  [ ] Assumption register: >= 3 A-NN entries, VALIDATION PLAN present
  [ ] Risk register: >= 4 R-NN entries, P, I, P×I computed, anchors defined
  [ ] Failure mode register: >= 3 F-NN entries, canonical labels (FAILURE MODE /
      TRIGGER CONDITION / MITIGATION)
  [ ] Register ordering: all registers precede Phase 11 in phase manifest sequence
  [ ] Inertia axis: INERTIA COST on do-nothing; INERTIA OFFSET on each alternative
  [ ] Lead-time axis: DECISION LEAD TIME computed; ESCALATION FLAG where <= 0
  [ ] Phase 0 option anatomy contract: PM FRAMING: declared first, ARCHITECT
      VALIDATION: second, T-34 trigger named — COMPLETE / NOT COMPLETE

[NOTE: No Phase 0 causal chain contract binary is included. C-33 was not
satisfied — the gate cannot verify causal contract presence from this block;
a reviewer must locate the source phases directly. C-35 FAIL. C-37 FAIL.]

---

PHASE 11 — RECOMMENDATION

PM SIGN-OFF:
  RECOMMENDED OPTION: [option label]
  RATIONALE: [cite two comparison matrix dimensions]
  CONDITIONS: [qualifying conditions referencing at least one F-NN]
  F-ROW ANCHOR: [F-NN whose trigger most directly invalidates this PM sign-off]

ARCHITECT SIGN-OFF:
  TECHNICAL FEASIBILITY: [confirmation or qualification]
  CONSTRAINTS: [preconditions]
  F-ROW ANCHOR: [F-NN whose trigger most directly invalidates this Architect sign-off]

---

PHASE 12 — FINALIZATION

Execute as an explicitly numbered four-step list:

Step 1: Review amendment table for STATUS = OPEN triggers. For each open T-NN:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what required].
     Absent/incomplete: [what is missing]."
  One finding per trigger. Enumerate sequentially.

Step 2: Verify all E-tier criteria (C-01..C-04) satisfied.
Step 3: Verify all R-tier criteria (C-05..C-07) satisfied.
Step 4: Update COMPLETION STATUS to final state.

---

AMENDMENT TABLE SPECIFICATION

T-GUARD first, then T-01..T-37. Total: 38 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE

Key phase assignments:
  T-GUARD PHASE = PRE-DOCUMENT
  T-25 PHASE = PRE-DOCUMENT  (fires if T-GUARD not listed first)
  T-26 PHASE = PRE-DOCUMENT  (fires if COMPLETION STATUS slot absent at Phase 0)
  T-28 PHASE = FINALIZATION  (fires if Architect sign-off appears before PM)
  T-33 PHASE = PRE-DOCUMENT  (fires if no Phase 0 causal chain contract declared)
  T-34 PHASE = PRE-DOCUMENT  (fires if no Phase 0 option anatomy contract declared)
  T-35 PHASE = FINALIZATION  (fires if PREREQUISITE GATE omits causal chain binary)
  T-36 PHASE = FINALIZATION  (fires if PREREQUISITE GATE omits anatomy binary)
  T-37 PHASE = FINALIZATION  (fires if both Phase 0 contract binaries not co-present
                               in the same gate block)

T-33 fires: no Phase 0 CAUSAL CHAIN CONTRACT declared (C-33 FAIL).
T-35 fires: no causal chain binary in PREREQUISITE GATE (C-35 FAIL).
T-37 fires: gate holds only anatomy binary — C-37 requires both (C-37 FAIL).
Three open triggers at finalization: T-33, T-35, T-37.
```

---

## V-03 — Lifecycle-Heavy, Split-Gate | Axis: Lifecycle Emphasis | Designed fail: C-37 alone

**Hypothesis**: A lifecycle-heavy variation introduces explicit verification checkpoints after every major phase block. Phase 0 concludes with a POST-INITIALIZATION GATE that verifies contract completeness immediately — this block includes the anatomy contract binary (C-36 axis: C-34 PASS, anatomy binary in post-init gate). The main PREREQUISITE GATE before the recommendation phase verifies register ordering and the causal chain contract (C-35 axis: C-33 PASS, causal binary in prerequisite gate). C-35 PASS (causal binary in PREREQUISITE GATE). C-36 PASS (anatomy binary in POST-INITIALIZATION GATE). C-37 FAIL — the two binaries reside in different gate blocks. A reviewer can confirm either Phase 0 contract from its own gate, but cannot confirm both from a single block. Asymmetric single-block auditability. One open trigger at finalization: T-37. Score: 29/30 aspirational pass → composite 99.67.

```
ROLE SEQUENCE: Architect → PM

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

LIFECYCLE DESIGN: Every major phase group concludes with an explicit gate check
before proceeding to the next group. Gate failures detected early are recorded as
OPEN triggers and reported in finalization. Group structure:
  Group A: Phase 0 (initialization) — concludes with POST-INITIALIZATION GATE
  Group B: Phases 1-3 (framing + options) — concludes with POST-OPTION GATE
  Group C: Phases 4-6 (registers) — concludes with POST-REGISTER GATE
  Group D: Phases 7-9 (matrix + amend + inertia) — concludes with PRE-RECOMMENDATION GATE
  Group E: Phases 11-12 (recommendation + finalization)

ROLE ASSIGNMENTS:
- Architect: Owns phase gate checks, register construction, causal contract, and audit.
- PM: Owns business framing, option anatomy (PM FRAMING: slots), amend phase,
  recommendation rationale.

---

PHASE 0 — PRE-DOCUMENT INITIALIZATION

Architect: Declare role sequence (Architect → PM) as a typed header.

AMENDMENT TRACKING TABLE — initialize now:

Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
Rows: T-GUARD first, then T-01..T-37. Total: 38 rows.

T-GUARD: Scope = "any required typed slot, phase block, or gate item absent."
  PHASE = PRE-DOCUMENT. STATUS = PENDING.

T-01..T-37: One trigger per criterion. PHASE value assigned per row. STATUS = PENDING.

COMPLETION STATUS: "PENDING — document in progress."

PHASE MANIFEST — list all phases by sequence number and name:
  Phase 0: PRE-DOCUMENT INITIALIZATION
  Phase 0-gate: POST-INITIALIZATION GATE
  Phase 1: DECISION FRAMING
  Phase 2: SCOUT ARTIFACT INVENTORY
  Phase 3: OPTION COMPOSITION
  Phase 3-gate: POST-OPTION GATE
  Phase 4: ASSUMPTION REGISTER
  Phase 5: RISK REGISTER
  Phase 6: FAILURE MODE REGISTER
  Phase 6-gate: POST-REGISTER GATE
  Phase 7: COMPARISON MATRIX
  Phase 8: AMEND PHASE
  Phase 9: INERTIA OFFSET + DECISION LEAD TIME
  Phase 9-gate: PRE-RECOMMENDATION GATE (PREREQUISITE GATE)
  Phase 11: RECOMMENDATION
  Phase 12: FINALIZATION

CAUSAL CHAIN CONTRACT:

  CONTRACT: TEMPORAL ANCHOR − INERTIA OFFSET = DECISION LEAD TIME
  SOURCE — TEMPORAL ANCHOR: Phase 1 (DECISION FRAMING).
  SOURCE — INERTIA OFFSET: Phase 3 (OPTION COMPOSITION), per alternative.
  T-GUARD ROUTING: If either input term is absent at its source phase,
    T-GUARD fires at initialization.

OPTION ANATOMY CONTRACT:

  CONTRACT: Every option entry declares fields in this order:
    1. PM FRAMING: [first typed field]
    2. ARCHITECT VALIDATION: [second typed field]
    3. PROS, CONS, RISK, EFFORT, RATIONALE [follow]
  T-34 TRIGGER: Fires if PM FRAMING: is absent or out of sequence in any option entry.

---

PHASE 0-gate — POST-INITIALIZATION GATE

Immediately after Phase 0, before entering Group B. Named binaries:

  [ ] Amendment table initialized with T-GUARD first — COMPLETE / NOT COMPLETE
  [ ] COMPLETION STATUS slot present — COMPLETE / NOT COMPLETE
  [ ] Phase manifest present with all phases listed — COMPLETE / NOT COMPLETE
  [ ] Causal chain contract declared (TEMPORAL ANCHOR − INERTIA OFFSET = DECISION LEAD TIME,
      source attribution, T-GUARD routing) — COMPLETE / NOT COMPLETE
  [ ] Option anatomy contract declared (PM FRAMING: first, ARCHITECT VALIDATION: second,
      T-34 trigger named) — COMPLETE / NOT COMPLETE

[NOTE: This gate block contains the option anatomy contract binary (C-36 axis).
The PREREQUISITE GATE at Phase 9-gate will contain the causal chain contract binary
(C-35 axis). The two binaries are in separate gate blocks — not co-present.]

---

PHASE 1 — DECISION FRAMING

Architect: Typed fields:

  PROBLEM: [shared problem]
  TEMPORAL ANCHOR: [specific named date, sprint, or event]
  INACTION CONSEQUENCE: [concrete named outcome]
  DECISION REQUIRED: [the question being decided]

PM: Confirm framing captures business urgency.

---

PHASE 2 — SCOUT ARTIFACT INVENTORY

PM: Before composing options:

  AVAILABLE ARTIFACTS: [name + finding per artifact]
  ABSENT ARTIFACTS: [type + inline fallback assessment]

---

PHASE 3 — OPTION COMPOSITION

Minimum 3 options. Do-nothing is Option A.

For each option, apply the Phase 0 anatomy contract:

  OPTION [label]: [description]
  PM FRAMING: [business case — value proposition, adoption risk category]
  ARCHITECT VALIDATION: [technical constraints, technical risk category]
  PROS: [bulleted]
  CONS: [bulleted]
  RISK: [risk category label — register linkage added in Phase 9]
  EFFORT: [timeline and dependencies]
  RATIONALE: [one sentence]

Option A (do-nothing):
  INERTIA COST: [per-sprint P×I using Phase 5 anchors]

Alternatives:
  INERTIA OFFSET: [sprint crossover — computed in Phase 9]

---

PHASE 3-gate — POST-OPTION GATE

  [ ] Option count >= 3 — COMPLETE / NOT COMPLETE
  [ ] Do-nothing option present — COMPLETE / NOT COMPLETE
  [ ] Every option carries PM FRAMING: as first typed field — COMPLETE / NOT COMPLETE
  [ ] INERTIA COST present on do-nothing option — COMPLETE / NOT COMPLETE

---

PHASE 4 — ASSUMPTION REGISTER

Table:
  A-NN | ASSUMPTION | VALIDATION PLAN
At least 3 entries.

---

PHASE 5 — RISK REGISTER

Define P/I anchors (P=1, P=3, P=5; I=1, I=3, I=5) with project-specific language.

Table:
  R-NN | RISK | P | I | P×I | MITIGATION
At least 4 entries.

---

PHASE 6 — FAILURE MODE REGISTER

Table:
  F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION
At least 3 entries. Canonical column labels.

---

PHASE 6-gate — POST-REGISTER GATE

  [ ] Assumption register complete (>= 3 entries, VALIDATION PLAN present)
  [ ] Risk register complete (>= 4 entries, anchors defined, P×I computed)
  [ ] Failure mode register complete (>= 3 entries, canonical labels)
  [ ] All registers appear before Phase 11 in phase manifest sequence

---

PHASE 7 — COMPARISON MATRIX

OPTIONS as column headers.
Rows: Effort | Risk (P×I) | Time-to-value | Reversibility | Inertia baseline | Adoption friction

---

PHASE 8 — AMEND PHASE

Three categories. OWNER and DEADLINE typed slots in every entry:

MISSING OPTION: OPTION: / OWNER: / DEADLINE:
UNWEIGHTED CRITERION: CRITERION: / OWNER: / DEADLINE:
FOLLOW-UP: ACTION: / OWNER: / DEADLINE:

At least one entry per category.

---

PHASE 9 — INERTIA OFFSET AND DECISION LEAD TIME

Per alternative:
  INERTIA OFFSET: [sprint N]
  DECISION LEAD TIME: TEMPORAL ANCHOR − INERTIA OFFSET = [value]
  ESCALATION FLAG: [if <= 0: name the trap condition]

---

PHASE 9-gate — PRE-RECOMMENDATION GATE (PREREQUISITE GATE)

Named binaries — COMPLETE or NOT COMPLETE:

  [ ] Assumption register complete (>= 3 entries)
  [ ] Risk register complete (>= 4 entries, P×I, anchors)
  [ ] Failure mode register complete (>= 3 entries, canonical labels)
  [ ] Register ordering: all registers precede Phase 11
  [ ] Inertia axis: INERTIA COST on do-nothing; INERTIA OFFSET on each alternative
  [ ] Lead-time axis: DECISION LEAD TIME per alternative; ESCALATION FLAG if <= 0
  [ ] Phase 0 causal chain contract: formula declared, source attribution present,
      T-GUARD routing rule stated at initialization — COMPLETE / NOT COMPLETE

[NOTE: C-35 binary is in this gate (causal chain contract verification).
C-36 binary is in Phase 0-gate (anatomy contract verification).
The two Phase 0 contract binaries are in separate gate blocks.
C-37 requires co-presence in the same gate block — C-37 FAIL.]

---

PHASE 11 — RECOMMENDATION

PM SIGN-OFF:
  RECOMMENDED OPTION: [label]
  RATIONALE: [two matrix dimensions cited]
  CONDITIONS: [reference at least one F-NN by ID]
  F-ROW ANCHOR: [F-NN invalidating PM sign-off]

ARCHITECT SIGN-OFF:
  TECHNICAL FEASIBILITY: [confirmation]
  CONSTRAINTS: [preconditions]
  F-ROW ANCHOR: [F-NN invalidating Architect sign-off]

---

PHASE 12 — FINALIZATION

Explicitly numbered four-step list:

Step 1: Amendment table review — STATUS = OPEN triggers.
  "Finding N: T-NN — [criterion]. Expected: [X]. Absent: [Y]."
  One finding per trigger.

Step 2: Verify E-tier (C-01..C-04).
Step 3: Verify R-tier (C-05..C-07).
Step 4: Update COMPLETION STATUS to final state.

---

AMENDMENT TABLE SPECIFICATION

T-GUARD first, T-01..T-37. Total: 38 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE

Key phase assignments:
  T-GUARD PHASE = PRE-DOCUMENT
  T-25  PHASE = PRE-DOCUMENT  (fires if T-GUARD not first in trigger table)
  T-26  PHASE = PRE-DOCUMENT  (fires if COMPLETION STATUS slot absent at Phase 0)
  T-35  PHASE = FINALIZATION  (fires if PREREQUISITE GATE omits causal chain binary —
                                note: causal binary IS in Phase 9-gate; C-35 PASS)
  T-36  PHASE = FINALIZATION  (fires if PREREQUISITE GATE omits anatomy contract binary —
                                note: anatomy binary IS in Phase 0-gate; C-36 PASS by
                                technical reading, as C-36 criterion says "a gate block")
  T-37  PHASE = FINALIZATION  (fires if both Phase 0 contract binaries are not co-present
                                in the SAME gate block — they are in different blocks here;
                                C-37 FAIL → T-37 fires)

One open trigger at finalization: T-37.
Finding 1: T-37 — C-37 (PREREQUISITE GATE dual-contract coverage).
  Expected: Both causal chain binary AND anatomy contract binary present in the same gate block.
  Absent: Anatomy binary in Phase 0-gate; causal binary in Phase 9-gate; not co-present.
```

---

## V-04 — Conversational Register | Axis: Phrasing Register | Designed fail: C-25 alone

**Hypothesis**: A conversational, explanatory-register variation satisfies C-33 (Phase 0 CAUSAL CHAIN CONTRACT with typed formula, source attribution, T-GUARD routing) and C-34 (Phase 0 OPTION ANATOMY CONTRACT with PM FRAMING: first, ARCHITECT VALIDATION: second, T-34 trigger). The PREREQUISITE GATE includes both the causal chain binary (C-35 PASS) and the anatomy contract binary (C-36 PASS) co-present in the same gate block (C-37 PASS). All other aspirational criteria pass. The single designed failure: T-GUARD is defined in the amendment table but listed after T-01..T-37 rather than as the first entry (C-25 FAIL). A reviewer reads position 1 in the trigger table and finds T-01 rather than T-GUARD — enforcement direction is backstop, not frontline. One open trigger at finalization: T-25. Score: 29/30 aspirational pass → composite 99.67.

```
ROLE SEQUENCE: PM → Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

STYLE: Conversational and explanatory throughout. Explain reasoning and trade-offs
in natural language. Tables where structure adds clarity; transitional prose between
major phases. Role contributions read as coherent perspective, not isolated fields.

ROLE ASSIGNMENTS:
- PM: Leads narrative framing, option business cases, amend phase, and recommendation.
- Architect: Provides technical constraints, register construction, and feasibility.

---

PHASE 0 — PRE-DOCUMENT INITIALIZATION

Begin by declaring: "This proposal follows a PM → Architect role sequence." Apply
this attribution in each subsequent phase header.

AMENDMENT TRACKING TABLE — initialize now:

Columns: ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules in this order: T-01 through T-37 (one per criterion C-01..C-37),
then T-GUARD as the final entry. Total: 38 rows.

T-01..T-37: Named trigger per criterion. PHASE value per row. STATUS = PENDING.

T-GUARD (final entry): Scope = "any required typed slot, phase block, or gate item
absent from the document — catch-all for structural gaps not covered by T-01..T-37."
PHASE = FINALIZATION. STATUS = PENDING.

[NOTE: T-GUARD appears last in the trigger table, after T-01..T-37. C-25 requires
T-GUARD as the FIRST entry. C-25 FAIL. T-25 fires at finalization.]

COMPLETION STATUS: "PENDING — document in progress."

PHASE MANIFEST:
  Phase 0: PRE-DOCUMENT INITIALIZATION
  Phase 1: DECISION FRAMING
  Phase 2: SCOUT ARTIFACT INVENTORY
  Phase 3: OPTION COMPOSITION
  Phase 4: ASSUMPTION REGISTER
  Phase 5: RISK REGISTER
  Phase 6: FAILURE MODE REGISTER
  Phase 7: COMPARISON MATRIX
  Phase 8: AMEND PHASE
  Phase 9: INERTIA OFFSET + DECISION LEAD TIME
  Phase 10: PREREQUISITE GATE
  Phase 11: RECOMMENDATION
  Phase 12: FINALIZATION

CAUSAL CHAIN CONTRACT — before any term-contributing phase:

  CONTRACT: TEMPORAL ANCHOR − INERTIA OFFSET = DECISION LEAD TIME
  SOURCE — TEMPORAL ANCHOR: Phase 1 (DECISION FRAMING), TEMPORAL ANCHOR field.
  SOURCE — INERTIA OFFSET: Phase 3 (OPTION COMPOSITION), INERTIA OFFSET per alternative.
  T-GUARD ROUTING: If TEMPORAL ANCHOR or INERTIA OFFSET absent at source phase,
    T-GUARD fires at initialization rather than deferring to Phase 11.

OPTION ANATOMY CONTRACT — before any option is composed:

  CONTRACT: Every option entry must open with these fields in order:
    1. PM FRAMING: [first typed field — PM introduces the business case]
    2. ARCHITECT VALIDATION: [second typed field — Architect evaluates feasibility]
    3. PROS, CONS, RISK, EFFORT, RATIONALE in any order after
  T-34 TRIGGER: Fires if PM FRAMING: is absent or out of sequence in any option entry.

---

PHASE 1 — DECISION FRAMING

PM: Open with a brief paragraph explaining the business context. Then provide:

  PROBLEM: [the shared problem all options address]
  TEMPORAL ANCHOR: [specific named date, sprint, or event — name it precisely]
  INACTION CONSEQUENCE: [concrete named outcome of not deciding]
  DECISION REQUIRED: [the question being put to the team]

Architect: Add a sentence on technical constraints shaping the decision space.

---

PHASE 2 — SCOUT ARTIFACT INVENTORY

PM: Walk through available signal artifacts before composing options:

  AVAILABLE ARTIFACTS: [name each artifact found, with its key finding]
  ABSENT ARTIFACTS: [name expected types not available, with inline fallback
    assessment substituting for each absent artifact category]

---

PHASE 3 — OPTION COMPOSITION

Present each option as a narrative block applying the Phase 0 anatomy contract.
Minimum 3 options; do-nothing appears first as Option A.

  OPTION [label]: [description — PM introduces the option's value proposition]
  PM FRAMING: [business case, adoption path, business risk category]
  ARCHITECT VALIDATION: [technical constraints, integration requirements, technical
    risk category]
  PROS: [strengths in bullet form]
  CONS: [weaknesses in bullet form]
  RISK: [risk category — quantified linkage added in Phase 9]
  EFFORT: [timeline and team or dependency summary]
  RATIONALE: [why this option belongs in the shortlist]

Option A (do-nothing) adds:
  INERTIA COST: [per-sprint P×I using Phase 5 anchors — PM explains inertia
    argument; Architect validates the cost model]

Alternatives add:
  INERTIA OFFSET: [estimated sprint crossover — computed precisely in Phase 9]

---

PHASE 4 — ASSUMPTION REGISTER

Architect: Build the assumption register as a structured table:

  A-NN | ASSUMPTION | VALIDATION PLAN

At least 3 entries with named validation method and owner per row.
PM: Add adoption-related assumptions.

---

PHASE 5 — RISK REGISTER

Architect: Define project-specific anchors conversationally — explain what P=1, P=3,
P=5 and I=1, I=3, I=5 mean for this specific context, then produce the table:

  R-NN | RISK | P | I | P×I | MITIGATION

At least 4 entries. P and I on 1-5 scale. P×I computed.
PM: Add adoption and schedule risk entries.

---

PHASE 6 — FAILURE MODE REGISTER

Architect: Explain the failure mode framing briefly, then produce the table:

  F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION

At least 3 entries. Use canonical column labels — FAILURE MODE, TRIGGER CONDITION,
MITIGATION — exactly as named.
PM: Add business failure modes (adoption collapse, budget cut scenarios).

---

PHASE 7 — COMPARISON MATRIX

Present a comparison matrix with OPTIONS as column headers.
Dimensions: Effort | Risk (P×I cited) | Time-to-value | Reversibility |
  Inertia cost baseline | PM adoption friction

PM frames the dimension selection with a brief rationale. Architect validates scoring.

---

PHASE 8 — AMEND PHASE

PM: Walk through the self-audit as a narrative, then enumerate entries using the
following template for each category:

MISSING OPTION:
  OPTION: [unexplored candidate]
  OWNER: [role responsible for investigating]
  DEADLINE: [specific sprint or date]

UNWEIGHTED CRITERION:
  CRITERION: [dimension needing recalibration]
  OWNER: [role responsible]
  DEADLINE: [specific sprint or date]

FOLLOW-UP:
  ACTION: [required next step]
  OWNER: [role responsible]
  DEADLINE: [specific sprint or date]

At least one entry per category. OWNER and DEADLINE are required typed slots in every
entry across all three categories.

---

PHASE 9 — INERTIA OFFSET AND DECISION LEAD TIME

Architect: For each non-do-nothing alternative, compute and narrate:

  INERTIA OFFSET: [sprint N]
  DECISION LEAD TIME: TEMPORAL ANCHOR − INERTIA OFFSET = [value in sprints]
  ESCALATION FLAG: [if zero or negative — name the inertia trap condition and
    its implications for the recommendation timeline]

---

PHASE 10 — PREREQUISITE GATE

A named binary checklist immediately before the recommendation. Each item COMPLETE
or NOT COMPLETE:

  [ ] Assumption register: >= 3 A-NN entries with VALIDATION PLAN
  [ ] Risk register: >= 4 R-NN entries, P/I anchors defined, P×I computed
  [ ] Failure mode register: >= 3 F-NN entries, canonical labels
  [ ] Register ordering: all registers precede Phase 11 in manifest sequence
  [ ] Inertia axis: INERTIA COST on Option A; INERTIA OFFSET on each alternative
  [ ] Lead-time axis: DECISION LEAD TIME per alternative; ESCALATION FLAG where <= 0
  [ ] Phase 0 causal chain contract: formula declared with source attribution and
      T-GUARD routing rule at initialization — COMPLETE / NOT COMPLETE
  [ ] Phase 0 option anatomy contract: PM FRAMING: first, ARCHITECT VALIDATION:
      second, T-34 trigger named at initialization — COMPLETE / NOT COMPLETE

[NOTE: Both Phase 0 contract binaries co-present in this single gate block.
C-35 PASS. C-36 PASS. C-37 PASS — dual-contract coverage from a single block.]

---

PHASE 11 — RECOMMENDATION

PM SIGN-OFF:
  PM: Name the recommended option and explain reasoning in narrative form, citing
  at least two comparison matrix dimensions.

  RECOMMENDED OPTION: [label]
  RATIONALE: [narrative — two dimensions cited]
  CONDITIONS: [qualifying conditions referencing at least one F-NN by ID]
  F-ROW ANCHOR: [F-NN whose trigger most directly invalidates this sign-off]

ARCHITECT SIGN-OFF:
  Architect: Confirm technical viability conversationally.

  TECHNICAL FEASIBILITY: [narrative confirmation or qualification]
  CONSTRAINTS: [preconditions for the recommendation to hold]
  F-ROW ANCHOR: [F-NN whose trigger most directly invalidates this sign-off]

---

PHASE 12 — FINALIZATION

Review the document for completeness in narrative form, surfacing gaps as named
findings using the format "Finding N: T-NN" inline.

Execute as an explicitly numbered four-step list:

Step 1: Review the amendment table for STATUS = OPEN triggers. For each open T-NN:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what required].
     Absent/incomplete: [what is missing]."
  One finding per trigger. Enumerate sequentially.

Step 2: Verify E-tier criteria (C-01..C-04). Discuss briefly.
Step 3: Verify R-tier criteria (C-05..C-07). Discuss briefly.
Step 4: Update COMPLETION STATUS to final state.

---

AMENDMENT TABLE SPECIFICATION

Columns: ID | TRIGGER | CONDITION | STATUS | PHASE

Populate T-01 through T-37 first (one per criterion), then T-GUARD as the last row.
Total: 38 rows. T-GUARD PHASE = FINALIZATION.

Key phase assignments:
  T-25 PHASE = FINALIZATION  (fires if T-GUARD is not the FIRST entry in trigger
                               table — T-GUARD is listed LAST here → T-25 fires)
  T-26 PHASE = PRE-DOCUMENT  (fires if COMPLETION STATUS slot absent at Phase 0)
  T-33 PHASE = PRE-DOCUMENT  (fires if Phase 0 causal chain contract absent)
  T-34 PHASE = PRE-DOCUMENT  (fires if Phase 0 option anatomy contract absent)
  T-35 PHASE = FINALIZATION  (fires if PREREQUISITE GATE omits causal chain binary)
  T-36 PHASE = FINALIZATION  (fires if PREREQUISITE GATE omits anatomy binary)
  T-37 PHASE = FINALIZATION  (fires if both binaries not co-present in same gate)

T-25 fires: T-GUARD listed last, not first (C-25 FAIL).
One open trigger at finalization: T-25.
Finding 1: T-25 — C-25 (Sentinel-first trigger ordering).
  Expected: T-GUARD as the first entry in the trigger definition table at Phase 0.
  Absent: T-GUARD appears as row 38, after T-01..T-37.
```

---

## V-05 — Inertia-Forward + Motivated | Axis: Inertia Framing | Designed pass: C-28–C-37 all pass

**Hypothesis**: An inertia-forward variation that foregrounds the do-nothing option as the cost baseline and evaluates every alternative against the trajectory cost of not acting. Combines all axes required to satisfy C-28 through C-37 simultaneously: T-GUARD listed first (C-25 PASS), COMPLETION STATUS slot at Phase 0 (C-26 PASS), INERTIA COST + INERTIA OFFSET (C-27 PASS), PM sign-off first (C-28 PASS), table-format registers (C-29 PASS), phase manifest (C-30 PASS), DECISION LEAD TIME + ESCALATION FLAG (C-31 PASS), PM FRAMING: first in option anatomy (C-32 PASS), Phase 0 CAUSAL CHAIN CONTRACT (C-33 PASS), Phase 0 OPTION ANATOMY CONTRACT (C-34 PASS), causal chain gate binary (C-35 PASS), anatomy gate binary (C-36 PASS), both binaries co-present in same gate block (C-37 PASS). Score: 30/30 aspirational pass → composite 100.0.

```
ROLE SEQUENCE: PM → Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

INERTIA FRAMING: Open by foregrounding inaction as the default trajectory. The
do-nothing option (Option A) represents the current path and is evaluated first in
every comparative dimension. Every alternative is explicitly measured against the
cumulative cost of remaining on the do-nothing trajectory. The decision frame names
the sprint at which each alternative's implementation cost is recovered by inertia
cost savings.

ROLE ASSIGNMENTS:
- PM: Leads inertia cost framing, business cases, amend phase, recommendation.
  PM FRAMING: appears as the first typed field in every option anatomy entry.
- Architect: Leads register construction, causal contracts, gate audits, feasibility.
  ARCHITECT VALIDATION: appears as the second typed field in every option anatomy entry.

---

PHASE 0 — PRE-DOCUMENT INITIALIZATION

PM: Declare role sequence (PM → Architect) as a typed header. Apply in all phase headers.
State inertia framing principle: "Option A (do-nothing) is evaluated first as the
default trajectory in every comparison dimension."

AMENDMENT TRACKING TABLE — initialize now:

Columns: ID | TRIGGER | CONDITION | STATUS | PHASE

Row 1 — T-GUARD (sentinel, listed FIRST):
  T-GUARD: Scope = "any required typed slot, phase block, or gate item absent from
    the document — catch-all for all structural gaps not covered by T-01..T-37."
  PHASE = PRE-DOCUMENT. STATUS = PENDING.

Rows 2–38 — T-01 through T-37: One trigger per criterion C-01..C-37. Assign PHASE
value per row. STATUS = PENDING.

COMPLETION STATUS: typed slot, initialized to "PENDING — document in progress."

PHASE MANIFEST — all phases in sequence:
  Phase 0: PRE-DOCUMENT INITIALIZATION
  Phase 1: DECISION FRAMING
  Phase 2: SCOUT ARTIFACT INVENTORY
  Phase 3: OPTION COMPOSITION
  Phase 4: ASSUMPTION REGISTER
  Phase 5: RISK REGISTER
  Phase 6: FAILURE MODE REGISTER
  Phase 7: COMPARISON MATRIX
  Phase 8: AMEND PHASE
  Phase 9: INERTIA OFFSET + DECISION LEAD TIME
  Phase 10: PREREQUISITE GATE
  Phase 11: RECOMMENDATION
  Phase 12: FINALIZATION

CAUSAL CHAIN CONTRACT — declared before any term-contributing phase:

  CONTRACT: TEMPORAL ANCHOR − INERTIA OFFSET = DECISION LEAD TIME
  SOURCE — TEMPORAL ANCHOR: Phase 1 (DECISION FRAMING), TEMPORAL ANCHOR typed field.
  SOURCE — INERTIA OFFSET: Phase 3 (OPTION COMPOSITION), INERTIA OFFSET field on
    each non-do-nothing alternative; INERTIA COST on do-nothing (Option A) provides
    the per-sprint accumulation rate.
  T-GUARD ROUTING: If TEMPORAL ANCHOR is absent at Phase 1 or INERTIA OFFSET is
    absent from any alternative at Phase 3, T-GUARD fires at Phase 0 initialization
    rather than deferring the gap to Phase 11.

OPTION ANATOMY CONTRACT — declared before any option is composed:

  CONTRACT: Every option entry must include the following fields in this exact order:
    1. PM FRAMING: [FIRST required typed field — PM introduces the business case
       and inertia framing for this option before technical assessment]
    2. ARCHITECT VALIDATION: [SECOND required typed field — Architect evaluates
       technical constraints and integration requirements]
    3. PROS, CONS, RISK, EFFORT, RATIONALE [in this order, after the two role fields]
  T-34 TRIGGER: Fires if PM FRAMING: is absent from any option entry, appears out
    of sequence, or is preceded by any non-role typed field.
  Note: DESCRIPTION, if used, must not precede PM FRAMING: — it follows the role
    fields or is absorbed into PM FRAMING:.

---

PHASE 1 — DECISION FRAMING

PM: Frame the decision with inertia cost foregrounded:

  PROBLEM: [the shared problem all options address — stated as the inertia-generating
    condition that accumulates cost per sprint if unresolved]
  TEMPORAL ANCHOR: [specific named date, sprint, or event at which the cost of
    inaction reaches a binding threshold — name it precisely; vague language such as
    "soon" or "before it is too late" is not permitted]
  INACTION CONSEQUENCE: [concrete named outcome of not deciding by TEMPORAL ANCHOR —
    teams blocked, capability lost, or window closed; "missed feature" statements
    do not qualify]
  DECISION REQUIRED: [the question being decided]

Architect: Note technical constraints that create the inertia accumulation mechanism.

---

PHASE 2 — SCOUT ARTIFACT INVENTORY

PM: Inventory signal artifacts before composing options:

  AVAILABLE ARTIFACTS:
    [artifact name] — [key finding relevant to inertia or option selection]
    (repeat per artifact found)
  ABSENT ARTIFACTS:
    [artifact type] — [inline fallback assessment substituting for absence]
    (repeat per missing type)

---

PHASE 3 — OPTION COMPOSITION

Minimum 3 options. Option A is do-nothing and appears first.

For every option, apply the Phase 0 anatomy contract exactly:

  OPTION [label]: [description]
  PM FRAMING: [PM introduces the option's business case — value proposition, adoption
    path, inertia reduction argument, and business risk category. For Option A, PM
    states the inertia accumulation argument — cost per sprint of remaining on this
    trajectory.]
  ARCHITECT VALIDATION: [Architect assesses technical constraints, integration
    dependencies, and technical risk category. For Option A, Architect validates
    the inertia cost model.]
  PROS: [bulleted strengths]
  CONS: [bulleted weaknesses]
  RISK: [risk category label — quantified linkage from register added in Phase 9]
  EFFORT: [timeline, team size, and dependency requirements]
  RATIONALE: [why this option belongs in the shortlist]

Option A (do-nothing) additionally requires:
  INERTIA COST: [per-sprint P×I value using Phase 5 scoring anchors.
    P = probability that inertia compounds this sprint (1–5).
    I = impact of one compounding cycle (1–5).
    State: INERTIA COST = P×I = [value] per sprint.]

Each non-do-nothing alternative additionally requires:
  INERTIA OFFSET: [estimated sprint at which cumulative implementation cost equals
    cumulative INERTIA COST × sprint-count — to be computed precisely in Phase 9]

---

PHASE 4 — ASSUMPTION REGISTER

Architect: Build as a structured table:

  A-NN | ASSUMPTION | VALIDATION PLAN

At least 3 entries. VALIDATION PLAN names the method and responsible owner.
PM: Add at least one adoption-related assumption and one inertia-model assumption.

---

PHASE 5 — RISK REGISTER

Architect: Define project-specific scoring anchors before any entry is scored:

  P=1: [project-specific — e.g., observed once in last 10 sprints]
  P=3: [project-specific — e.g., happens roughly half the sprints]
  P=5: [project-specific — e.g., near-certain each sprint]
  I=1: [project-specific — e.g., one engineer-day recovery]
  I=3: [project-specific — e.g., one-sprint delay or rework]
  I=5: [project-specific — e.g., feature blocked or data lost]

Build as a structured table:

  R-NN | RISK | P | I | P×I | MITIGATION

At least 4 entries. Include inertia-specific risks for Option A (schedule drift,
compounding technical debt). PM adds adoption and schedule risk entries.

---

PHASE 6 — FAILURE MODE REGISTER

Architect: Build as a structured table:

  F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION

At least 3 entries. Use these exact canonical column labels. Each row names a
concrete trigger condition and a named escalation path.
PM: Add business failure modes — adoption collapse, budget cut, sponsor departure.

---

PHASE 7 — COMPARISON MATRIX

Comparison matrix with OPTIONS as column headers. Option A (do-nothing) appears
as the first column — the inertia baseline.

Rows (dimensions):
  Inertia cost baseline (P×I per sprint) | Implementation effort | Risk (P×I cited) |
  Time-to-value | Reversibility | PM adoption friction | INERTIA OFFSET sprint

PM leads dimension selection, foregrounding inertia-axis rows. Architect validates.
Score or characterize each cell consistently.

---

PHASE 8 — AMEND PHASE

Self-audit using three required categories. OWNER and DEADLINE appear as typed slots
in every entry across all three categories:

MISSING OPTION:
  OPTION: [an unexplored candidate not in Phase 3, especially any partial-inertia-
    reduction alternative between Option A and full alternatives]
  OWNER: [name or role]
  DEADLINE: [specific sprint name, named date, or milestone — "TBD" does not satisfy]

UNWEIGHTED CRITERION:
  CRITERION: [a comparison matrix dimension treated as equally weighted that deserves
    recalibration — inertia cost weight is a candidate]
  OWNER: [name or role]
  DEADLINE: [specific sprint, date, or milestone]

FOLLOW-UP:
  ACTION: [next required step before the recommendation becomes binding]
  OWNER: [name or role]
  DEADLINE: [specific sprint, date, or milestone]

At least one entry per category.

---

PHASE 9 — INERTIA OFFSET AND DECISION LEAD TIME

For each non-do-nothing alternative, compute using the Phase 0 causal chain contract:

  INERTIA OFFSET: [Sprint N — the sprint at which cumulative implementation cost
    equals cumulative Option A INERTIA COST × N sprints]
  DECISION LEAD TIME: TEMPORAL ANCHOR (Sprint X) − INERTIA OFFSET (Sprint N)
    = [value] sprints
  Interpretation: Positive = runway to act. Zero or negative = inertia trap entered.
  ESCALATION FLAG: [Required if DECISION LEAD TIME <= 0. Name the inertia trap
    condition: which team is blocked, what window closes, what alternative is lost.]

---

PHASE 10 — PREREQUISITE GATE

Named binaries — COMPLETE or NOT COMPLETE — verified before Phase 11 executes:

  [ ] Assumption register: >= 3 A-NN entries, VALIDATION PLAN present on every row
  [ ] Risk register: >= 4 R-NN entries, P/I anchors defined, P×I computed per row
  [ ] Failure mode register: >= 3 F-NN entries, canonical labels (FAILURE MODE /
      TRIGGER CONDITION / MITIGATION) — COMPLETE / NOT COMPLETE
  [ ] Register ordering: assumption register, risk register, and failure mode register
      all appear before Phase 11 in the phase manifest sequence — COMPLETE / NOT COMPLETE
  [ ] Inertia axis: INERTIA COST present on Option A (do-nothing); INERTIA OFFSET
      present on every alternative — COMPLETE / NOT COMPLETE
  [ ] Lead-time axis: DECISION LEAD TIME computed per alternative; ESCALATION FLAG
      on any alternative with DECISION LEAD TIME <= 0 — COMPLETE / NOT COMPLETE
  [ ] Phase 0 causal chain contract: formula TEMPORAL ANCHOR − INERTIA OFFSET =
      DECISION LEAD TIME declared at Phase 0 with source phase attribution for both
      input terms and T-GUARD routing rule — COMPLETE / NOT COMPLETE
  [ ] Phase 0 option anatomy contract: PM FRAMING: declared as first required field,
      ARCHITECT VALIDATION: as second required field, T-34 trigger named for role-slot
      violations, declared at Phase 0 before any option authored — COMPLETE / NOT COMPLETE

[NOTE: Both Phase 0 contract binaries are present in this single gate block.
C-35 PASS (causal chain binary). C-36 PASS (anatomy contract binary).
C-37 PASS — both binaries co-present in the same gate block; a reviewer confirms
both Phase 0 contracts from a single block read without scrolling to Phase 0.]

---

PHASE 11 — RECOMMENDATION

PM SIGN-OFF — appears first:

  RECOMMENDED OPTION: [option label]
  RATIONALE: [explain recommendation against the inertia baseline; cite at least
    two comparison matrix dimensions; name the INERTIA OFFSET sprint at which the
    recommended option recovers its implementation cost relative to Option A]
  CONDITIONS: [qualifying conditions — reference at least one F-NN by ID; state
    the sprint or event at which the conditions must be validated]
  F-ROW ANCHOR: [the F-row ID whose trigger condition most directly invalidates
    this PM sign-off if it fires — PM independently names this F-row]

ARCHITECT SIGN-OFF — appears second:

  TECHNICAL FEASIBILITY: [confirm the recommended option is technically viable;
    state any preconditions that must hold for the INERTIA OFFSET estimate to be valid]
  CONSTRAINTS: [technical preconditions for the recommendation to hold]
  F-ROW ANCHOR: [the F-row ID whose trigger condition most directly invalidates
    this Architect sign-off — Architect independently names this F-row; may be
    the same or different F-row from PM's F-ROW ANCHOR]

---

PHASE 12 — FINALIZATION

Execute coverage verification as an explicitly numbered four-step list:

Step 1: Review the amendment table for trigger rules with STATUS = OPEN.
  For each open trigger T-NN, produce a finding entry:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing from this document]."
  Enumerate sequentially (Finding 1, Finding 2, ...). One finding per trigger.
  Do not bundle two open triggers into a single finding.

Step 2: Verify all E-tier criteria (C-01..C-04) are satisfied. Update amendment
  table STATUS for any E-tier criterion found incomplete.

Step 3: Verify all R-tier criteria (C-05..C-07) are satisfied. Update amendment
  table STATUS for any R-tier criterion found incomplete.

Step 4: Update the amendment table COMPLETION STATUS field to its terminal value:
  If no open triggers remain:
    "T-GUARD enforced all requirements successfully — no violations detected."
  If open triggers remain:
    List each open T-NN and its corresponding finding number.

---

AMENDMENT TABLE SPECIFICATION

Row 1 — T-GUARD (sentinel, FIRST):
  Scope = any required typed slot, phase block, or gate item absent.
  PHASE = PRE-DOCUMENT. STATUS = PENDING at init.

Rows 2–38 — T-01 through T-37:
  One row per criterion C-01..C-37. PHASE value per row. STATUS = PENDING.

Columns: ID | TRIGGER | CONDITION | STATUS | PHASE

Key phase assignments:
  T-GUARD PHASE = PRE-DOCUMENT
  T-25  PHASE = PRE-DOCUMENT  (fires if T-GUARD is not the first entry — PASSES here)
  T-26  PHASE = PRE-DOCUMENT  (fires if COMPLETION STATUS slot absent at Phase 0)
  T-27  PHASE = OPTION COMPOSITION  (fires if INERTIA COST absent on do-nothing option)
  T-28  PHASE = FINALIZATION  (fires if Architect sign-off appears before PM sign-off)
  T-29  PHASE = FINALIZATION  (fires if any register uses prose format instead of table)
  T-30  PHASE = PRE-DOCUMENT  (fires if phase manifest absent or incomplete)
  T-31  PHASE = FINALIZATION  (fires if DECISION LEAD TIME absent on any alternative,
                                or ESCALATION FLAG absent where DECISION LEAD TIME <= 0)
  T-32  PHASE = OPTION COMPOSITION  (fires if PM FRAMING: is not the first typed field
                                      overall in any option anatomy entry)
  T-33  PHASE = PRE-DOCUMENT  (fires if no Phase 0 causal chain contract declared)
  T-34  PHASE = PRE-DOCUMENT  (fires if no Phase 0 option anatomy contract declared)
  T-35  PHASE = FINALIZATION  (fires if PREREQUISITE GATE omits causal chain binary)
  T-36  PHASE = FINALIZATION  (fires if PREREQUISITE GATE omits anatomy contract binary)
  T-37  PHASE = FINALIZATION  (fires if both Phase 0 contract binaries not co-present
                                in the same gate block)

Expected at completion: all triggers STATUS = PASS or no-fire.
COMPLETION STATUS terminal value: "T-GUARD enforced all requirements successfully —
  no violations detected."
```

---

## Predicted Scoring

| Variation | Axis | Designed Fail | C-25 | C-33 | C-34 | C-35 | C-36 | C-37 | A score | Composite |
|-----------|------|---------------|------|------|------|------|------|------|---------|-----------|
| V-01 | Role sequence | C-34, C-36, C-37 | PASS | PASS | FAIL | PASS | FAIL | FAIL | 27/30 | **99.00** |
| V-02 | Output format | C-33, C-35, C-37 | PASS | FAIL | PASS | FAIL | PASS | FAIL | 27/30 | **99.00** |
| V-03 | Lifecycle emphasis | C-37 alone | PASS | PASS | PASS | PASS | PASS | FAIL | 29/30 | **99.67** |
| V-04 | Phrasing register | C-25 alone | FAIL | PASS | PASS | PASS | PASS | PASS | 29/30 | **99.67** |
| V-05 | Inertia framing + motivated | none | PASS | PASS | PASS | PASS | PASS | PASS | 30/30 | **100.0** |

**V-01 anatomy-contract-absent path**: Architect-first variation omits Phase 0 OPTION ANATOMY CONTRACT (C-34 FAIL). Option template embeds PM FRAMING:/ARCHITECT VALIDATION: typed slots directly (C-32 PASS) but no Phase 0 contract declares the structure prospectively. PREREQUISITE GATE holds only causal chain binary (C-35 PASS). Anatomy binary absent from gate (C-36 FAIL). Single binary in gate — C-37 FAIL. Three open triggers: T-34, T-36, T-37.

**V-02 causal-contract-absent path**: PM-first compact variation omits Phase 0 CAUSAL CHAIN CONTRACT (C-33 FAIL). TEMPORAL ANCHOR and INERTIA OFFSET appear correctly at source phases but no prospective initialization contract declares the computation chain. PREREQUISITE GATE holds only anatomy binary (C-36 PASS). Causal chain binary absent from gate (C-35 FAIL). Single binary in gate — C-37 FAIL. Three open triggers: T-33, T-35, T-37.

**V-03 split-gate isolation**: Both contracts declared at Phase 0 (C-33 PASS, C-34 PASS). Anatomy binary placed in POST-INITIALIZATION GATE (Phase 0-gate). Causal chain binary placed in PREREQUISITE GATE (Phase 9-gate). Each binary is verifiable from its own gate block — C-35 PASS (causal in Phase 9-gate), C-36 PASS (anatomy in Phase 0-gate). C-37 FAIL: the two binaries are not co-present in the same gate block. A reviewer must read two separate gate blocks to confirm both Phase 0 contracts. One open trigger: T-37.

**V-04 sentinel-ordering isolation**: Both contracts present (C-33 PASS, C-34 PASS). PREREQUISITE GATE carries both binaries co-present (C-35 PASS, C-36 PASS, C-37 PASS). Single failure: T-GUARD listed last in amendment table (after T-01..T-37) instead of first. C-25 FAIL. One open trigger: T-25.

**V-05 motivated combination**: All ten v11 axes (C-28–C-37) combined. T-GUARD first (C-25). COMPLETION STATUS at Phase 0 (C-26). INERTIA COST/OFFSET (C-27). PM sign-off first (C-28). Table-format registers (C-29). Phase manifest (C-30). DECISION LEAD TIME + ESCALATION FLAG (C-31). PM FRAMING: first in option anatomy (C-32). Phase 0 CAUSAL CHAIN CONTRACT (C-33). Phase 0 OPTION ANATOMY CONTRACT (C-34). Causal chain gate binary (C-35). Anatomy gate binary (C-36). Both binaries co-present in same gate block (C-37). Score: 30/30.

**V-01/V-02 symmetry**: V-01 has causal contract without anatomy contract; V-02 has anatomy contract without causal contract. Together they demonstrate that C-33/C-35 and C-34/C-36 are independently absent — neither axis supplies what the other supplies. The R10 discriminator pattern (which identified V-01 and V-02 of that round as the structural sources of C-36 and C-37) is reproduced here as single-axis designed failures, confirming independence in both directions.

**C-37 isolation tiers**: V-01 and V-02 fail C-37 by failing a prerequisite (C-36 or C-35 respectively). V-03 fails C-37 directly — both prerequisite criteria pass, but co-presence in the same gate block fails. Three distinct C-37 failure paths documented across two rounds.

**New tier introduced at 29/30**: V-03 and V-04 each produce 29/30 aspirational pass → composite 99.67. V-03's path (C-37 alone via split-gate) and V-04's path (C-25 alone via sentinel ordering) are the first demonstrations of the 99.67 tier for this rubric, separating from the 99.33 tier (V-01, V-02) and the 99.00 tier (R10 V-01/V-02 ported to v11).
