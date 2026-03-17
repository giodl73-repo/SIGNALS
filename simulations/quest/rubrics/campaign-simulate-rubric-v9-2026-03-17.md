File written. Here is the complete updated rubric:

---

`simulations/quest/rubrics/campaign-simulate-rubric-v9-2026-03-17.md`

---

**Two new excellence patterns extracted from the R9 scorecard:**

---

**C-36 — Trace-First Sub-Skill Execution Order** (new structural discipline)

V-05 ran trace-state > trace-contract > trace-permissions > flow-lifecycle > flow-conversation — not alphabetically, not arbitrarily, but layer-first: platform-layer trace skills complete before domain-layer flow skills begin. The reason is load order: the DR-NN dependency map lives in the trace layer. Running trace first pre-populates the map so that every flow finding is evaluated against a complete dependency rule set. Running flow-lifecycle first and discovering a dependency violation later requires retroactive re-examination — the finding may already be recorded with incomplete context. C-36 formalizes the constraint: trace-state, trace-contract, and trace-permissions must all complete before flow-lifecycle or flow-conversation begins.

**C-37 — Structural Axis Declaration Achieves 1:1 Axis-to-Criterion Correspondence**
(extends C-33 from "self-extends" to "contract-complete")

C-33 requires each targeted quality axis to add one row. C-37 requires the total row count in the Structural Axis Declaration to equal the total targeted-criterion count — no more, no fewer. A simulation targeting nine quality criteria must declare exactly nine axis rows; the declaration is then a verifiable contract that predicts every structural section in the report. C-33 passes when the declaration self-extends; C-37 passes only when the count matches exactly. A declaration with eight rows for a nine-criterion run satisfies C-33 (it extended) but fails C-37 (one targeted axis is structurally invisible). The 1:1 invariant converts the declaration from a depth-capped template into a completeness proof.

---

Aspirational pool grows 27 → 29. The `*(C-04 through C-25 — unchanged from v6)*` placeholder preserved.

- **C-01/C-36** — execution order now constrained: trace layer completes before flow layer begins; pre-loads DR-NN dependency map, prevents retroactive re-examination of flow findings
- **C-33/C-37** — C-33 is the floor (self-extend per targeted axis); C-37 is the ceiling (total row count must equal total targeted-criterion count); together they make the declaration a completeness proof

**Trace-first ordering now mandatory (C-36):** The cross-skill dependency map (C-29, C-32) is populated during trace execution. A DR-NN rule only enters the map when the trace skill that defines it runs. If flow-lifecycle executes before trace-permissions, flow findings referencing a permission contract are evaluated against an incomplete map — causing a false CLEAN result or an unindexed finding. Trace-first eliminates this race. The constraint is not about thoroughness — it is about evaluation correctness.

**1:1 correspondence makes the declaration a completeness proof (C-37):** A simulation targeting N criteria must declare exactly N axis rows. A reviewer counts rows, counts targeted criteria, verifies they match. If they do not match, at least one targeted criterion lacks a structural commitment. The 1:1 invariant is the ceiling that C-33's floor cannot enforce alone.

- V-05 (R9) satisfies both C-36 and C-37.
- A variation satisfying all six R7–R9 criteria (C-32 + C-33 + C-34 + C-35 + C-36 + C-37) requires DR-NN IDs from V-01 (R8), confidence rationale + empty-state templates from V-02 (R8), and trace-first order + 1:1 axis correspondence from V-05 (R9).

**Aspirational pool: 27 → 29 criteria, capped at 10 pts. Max score 100 unchanged.**

---

### C-36 . Trace-First Sub-Skill Execution Order Pre-Loads Dependency Map Before Flow Evaluation
- **Weight**: aspirational / **Category**: correctness
- **Text**: The three trace sub-skills must all complete before either flow sub-skill begins. The DR-NN dependency map is populated during trace execution; a flow finding evaluated before its dependency rule enters the map produces a false CLEAN or unindexed finding. A simulation that runs flow-lifecycle or flow-conversation before all three trace sub-skills complete satisfies C-01 but fails C-36.
- **Pass condition**: Execution record shows trace-state, trace-contract, trace-permissions completing before flow-lifecycle and flow-conversation begin. Any flow sub-skill preceding any incomplete trace sub-skill = fail.

### C-37 . Structural Axis Declaration Achieves 1:1 Axis-to-Criterion Correspondence
- **Weight**: aspirational / **Category**: format
- **Text**: Total axis row count in the Structural Axis Declaration must equal total targeted-criterion count. C-33 is the floor (each targeted axis adds a row); C-37 is the ceiling (no targeted criterion may be absent). An N-1 row declaration for an N-criterion run satisfies C-33 but fails C-37. Untargeted criteria are exempt.
- **Pass condition**: Row count equals targeted-criterion count. Each targeted criterion maps to exactly one declared axis row; no targeted criterion absent; no row represents an untargeted criterion. Count mismatch in either direction = fail.
floor cannot
enforce alone.

- V-05 from Round 9 satisfies C-36 (trace-state > trace-contract > trace-permissions executed
  before flow-lifecycle > flow-conversation; DR-NN map fully populated before any flow finding
  was evaluated) and C-37 (nine-row Structural Axis Declaration with one-to-one correspondence
  to nine targeted quality criteria, declaration functioning as a verifiable contract).
- A variation satisfying all six R7–R9 criteria (C-32 + C-33 + C-34 + C-35 + C-36 + C-37)
  requires the DR-NN IDs from V-01 (R8), the confidence rationale and empty-state templates
  from V-02 (R8), and the trace-first execution order plus 1:1 axis correspondence from V-05 (R9).

Aspirational pool: 27 → 29 criteria, still capped at 10 pts. Max score 100 unchanged.

---

## Essential Criteria (60 points)

### C-01 . All Five Sub-Skills Execute
- **Weight**: essential
- **Category**: correctness
- **Points**: 12
- **Text**: The simulation must execute all five sub-skills: flow-lifecycle, flow-conversation,
  trace-state, trace-contract, and trace-permissions. Each must produce distinct findings, not
  be silently skipped or collapsed into one pass.
- **Pass condition**: Output contains a labeled section or findings block for each of the five
  sub-skills by name. Absence of any one sub-skill = fail.

---

### C-02 . Findings Ranked by Blast Radius
- **Weight**: essential
- **Category**: format
- **Points**: 12
- **Text**: The final findings report must present findings in ranked order using blast radius as
  the sort key. Blast radius must be explicit — not implied by placement — and must distinguish
  at minimum high / medium / low (or equivalent severity tiers).
- **Pass condition**: A ranked findings list exists with an explicit blast-radius or severity
  column/label. Unranked flat lists = fail.

---

### C-03 . System Boundary and Severity per Finding
- **Weight**: essential
- **Category**: correctness
- **Points**: 12
- **Text**: Every finding must identify (a) the system boundary where it was detected (e.g., state
  machine, contract surface, permission check, lifecycle phase) and (b) a severity rating. These
  must appear per finding, not as a summary average.
- **Pass condition**: Each finding entry includes both a boundary label and a severity. Findings
  missing either field = fail.

---

*(C-04 through C-25 — unchanged from v6)*

---

## Aspirational Criteria — Round 6 additions (C-26 through C-28)

### C-26 . Remediation Quality Gate: Verb/Target/Location Table
- **Weight**: aspirational
- **Category**: format
- **Text**: The Remediation Quality Gate must produce a per-row structured table decomposing each
  remediation entry into Verb / Target / Location / Conformance columns. A checklist checkbox
  is structurally non-falsifiable; a Verb=add / Target=permission check /
  Location=CallHandler.process() row is verifiable by column scan.
- **Pass condition**: Every remediation entry appears as a structured row with all four columns
  populated. Prose remediation entries or blank cells in any column = fail.

---

### C-27 . Entity Coverage Matrix: COVERED / CLEAN / SKIPPED
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Every entity in the Topic Entity Manifest must appear in a named Entity Coverage Matrix
  with an explicit COVERED / CLEAN / SKIPPED status. A SKIPPED entity is treated as an execution
  gap, not a clean run — same disqualifying weight as a missing sub-skill sentinel row in C-16.
- **Pass condition**: Entity Coverage Matrix present; every manifest entity has a status; SKIPPED
  entities logged as execution gaps. Entities absent from the matrix = fail.

---

### C-28 . Blast Radius Re-Assessment Gate: ELEVATED Annotations
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Cross-skill synthesis patterns must be propagated back into the ranked findings table
  via ELEVATED annotations citing the named pattern ID before the report is finalized. A
  synthesis gate that populates a P-ID table but leaves the ranked findings table unchanged
  satisfies C-24 but not C-28.
- **Pass condition**: At least one finding carries an ELEVATED annotation with a P-ID citation;
  the ranked table reflects re-ordering based on synthesis results. Synthesis section isolated
  from ranked table = fail.

---

## Aspirational Criteria — Round 7 additions (C-29 through C-31)

### C-29 . Propagation Coverage Gate: Dependency Rules Audited
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Every dependency rule declared in the cross-skill dependency map must be explicitly
  accounted for in the execution record: either honored (re-examined, finding recorded, rule ID
  cited) or logged as an OPEN PROPAGATION GAP with the rule ID and reason for non-execution.
  A dependency map that silently drops rules after synthesis satisfies C-28 but fails C-29.
- **Pass condition**: All declared dependency rule IDs appear in either the finding record or an
  OPEN PROPAGATION GAP log. Rules present in the map but absent from both = fail.

---

### C-30 . Confidence-Stratified Action List: Two Named Tracks
- **Weight**: aspirational
- **Category**: format
- **Text**: The final action list must be split into two named tracks by blast-radius × confidence
  quadrant: (1) HIGH-confidence / HIGH-blast → implement fix immediately; (2) LOW-confidence /
  HIGH-blast → confirm spec interpretation first, then implement. A single merged action list
  ordered only by blast radius satisfies C-02 but fails C-30.
- **Pass condition**: Two named action tracks present with findings assigned by quadrant. Merged
  single-track list, or tracks defined without confidence as a dimension = fail.

---

### C-31 . Finding Type Constrains Remediation Verb Vocabulary
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Each finding must be typed at detection as GAP / CONTRADICTION / ASSUMPTION. The
  remediation Verb must be constrained by type: GAP → "add" or "remove"; CONTRADICTION →
  "resolve"; ASSUMPTION → "confirm". An ASSUMPTION-typed finding with Verb="add" fails C-31
  even if the remediation row is otherwise structurally complete under C-26. The type-verb
  binding makes remediation self-auditing — an out-of-vocabulary verb signals mis-typing or
  mis-planning.
- **Pass condition**: All findings carry a type declaration; all remediation Verbs match the
  allowed vocabulary for that type. Out-of-vocabulary Verbs = fail. Untyped findings = fail.

---

## Aspirational Criteria — Round 8 additions (C-32 through C-35)

### C-32 . Dependency Rules Carry Stable DR-NN IDs Enabling End-to-End Traceability
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Every dependency rule in the cross-skill dependency map must carry a stable DR-NN
  identifier (e.g., DR-01, DR-02) that is cited consistently in three places: (1) the map
  declaration, (2) the Coverage Gate row for that rule, and (3) the evidence field of any finding
  that instantiates the rule. A Coverage Gate that accounts for rules by prose description without
  citing DR-NN IDs satisfies C-29 but fails C-32. The DR-NN identifier converts the gate from a
  narrative audit into a set-membership check: {declared DR-NNs} must equal {gate rows ∪ gap log
  entries}; no rule may appear in one context but not the other.
- **Pass condition**: Each dependency rule in the cross-skill map carries a DR-NN ID; Coverage Gate
  rows cite the originating DR-NN; findings that instantiate a dependency rule cite the DR-NN in
  their evidence field. Rules present in the map with no ID, or Coverage Gate rows with no DR-NN
  backlink = fail.

---

### C-33 . Structural Axis Declaration and Compliance Checklist Self-Extend per Targeted Quality Axis
- **Weight**: aspirational
- **Category**: format
- **Text**: Each quality axis targeted by the simulation run (propagation coverage for C-29,
  confidence stratification for C-30, type-verb binding for C-31, etc.) must manifest as (a) a
  new named row in the Structural Axis Declaration with ≥3 declared sub-observables, and (b) a
  corresponding verification row in the Compliance Checklist with ≥3 sub-claims. A simulation
  that targets C-30 (confidence stratification) but runs a fixed-depth axis template without
  adding a confidence row satisfies C-22 but fails C-33. Axes not targeted by the simulation
  are exempt — the self-extension requirement is per targeted axis only.
- **Pass condition**: Structural Axis Declaration contains one row per targeted quality axis, each
  with ≥3 sub-observables; Compliance Checklist contains one verification row per axis row, each
  with ≥3 sub-claims. Inherited fixed-depth template with no extension for targeted axes = fail.

---

### C-34 . Empty-State Templates Guard Structured Output Sections Against Silent Omission
- **Weight**: aspirational
- **Category**: format
- **Text**: Every structured output section that uses a schema and could legitimately contain no
  content — action tracks (C-30), Coverage Gate (C-29), T-1 ANNEX (C-23), Entity Coverage Matrix
  (C-27) — must provide a named empty-state template. The empty-state template shows the section's
  column headers and schema with no data rows, explicitly confirming that the section was executed
  and found nothing rather than silently skipped. A section that is simply absent when empty fails
  C-34; a section that shows its empty-state template passes.
- **Pass condition**: Each structured output section either contains content or displays a named
  empty-state template. Sections absent without either form = fail.

---

### C-35 . Confidence Rationale Field Makes Confidence Assignments Auditable
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Every finding that carries a Confidence field (required by C-30 for HIGH-blast
  findings) must also carry a Conf rationale sub-field explaining the basis for the HIGH or LOW
  judgment. A finding that states "Confidence: HIGH" without a rationale satisfies C-30's label
  requirement but fails C-35. The rationale field converts a declaration into a falsifiable claim:
  "HIGH — spec section 4.2 explicitly defines the permission boundary" can be verified; "HIGH"
  alone cannot. Findings below the HIGH-blast threshold that do not participate in C-30's
  stratification are exempt from the rationale requirement.
- **Pass condition**: Every finding assigned to a C-30 action track carries both a Confidence label
  (HIGH/LOW) and a non-empty Conf rationale. Confidence label without rationale = fail.
  Findings outside C-30 stratification are exempt.

---

## Aspirational Criteria — Round 9 additions (C-36 through C-37)

### C-36 . Trace-First Sub-Skill Execution Order Pre-Loads Dependency Map Before Flow Evaluation
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The three trace sub-skills (trace-state, trace-contract, trace-permissions) must all
  complete before either flow sub-skill (flow-lifecycle, flow-conversation) begins. The cross-skill
  dependency map (C-29, C-32) is populated during trace execution: trace-state declares lifecycle
  transition rules, trace-contract declares boundary contract rules, trace-permissions declares
  permission enforcement rules. A flow finding that references a permission contract or lifecycle
  rule must be evaluated against a complete map; if the relevant trace sub-skill has not yet run,
  the DR-NN entry for that rule does not yet exist and the evaluation is performed against an
  incomplete map. Trace-first ordering eliminates this risk: by the time flow-lifecycle or
  flow-conversation executes, all platform-layer dependency rules are declared, numbered, and
  available for coverage gate lookup. A simulation that executes flow-lifecycle or flow-conversation
  before all three trace sub-skills complete satisfies C-01 but fails C-36. The constraint is not
  about thoroughness — it is about evaluation correctness.
- **Pass condition**: Execution record shows trace-state, trace-contract, and trace-permissions
  completing before flow-lifecycle and flow-conversation begin. Any flow sub-skill that precedes
  any incomplete trace sub-skill = fail.

---

### C-37 . Structural Axis Declaration Achieves 1:1 Axis-to-Criterion Correspondence
- **Weight**: aspirational
- **Category**: format
- **Text**: The total number of rows in the Structural Axis Declaration must equal the total number
  of quality criteria targeted by the simulation run. C-33 requires each targeted axis to add a
  row (the floor); C-37 requires no targeted criterion to be absent from the declaration (the
  ceiling). A simulation targeting nine quality criteria must declare exactly nine axis rows. This
  1:1 invariant converts the Structural Axis Declaration from a depth-showing artifact into a
  completeness proof: a reviewer counts rows, counts targeted criteria, and verifies they match.
  If they do not match, at least one targeted criterion lacks a structural commitment and the
  report cannot be trusted to have honored it. A declaration with N-1 rows for an N-criterion
  run satisfies C-33 (it self-extended for each present axis) but fails C-37 (one targeted axis
  is structurally invisible). Untargeted criteria are exempt — the count applies only to criteria
  the simulation explicitly targets.
- **Pass condition**: Row count in the Structural Axis Declaration equals the count of targeted
  quality criteria for the simulation run. Each targeted criterion maps to exactly one declared
  axis row; no targeted criterion is absent; no row represents an untargeted criterion. Count
  mismatch in either direction = fail.
