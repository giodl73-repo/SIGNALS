Here is the complete updated rubric. The four new criteria extracted from the R8 scorecard:

---

**C-32 — Dependency Rule Stable IDs** (upgrades C-29)

V-01 didn't just satisfy C-29's "every rule accounted for" — it numbered the rules `DR-01…DR-NN`. That's a qualitatively different artifact: a prose Coverage Gate requires reading to verify; a DR-NN-keyed gate is a set-membership check. C-32 formalizes this: the DR-NN must appear in the map declaration, the gate row, and the finding's evidence field — three-point citation or fail.

**C-33 — Structural Axis Declaration Self-Extension** (upgrades C-16/C-22/C-18)

Both V-01 and V-02 extended their axis templates rather than inheriting a fixed skeleton. V-01 added Row 6 (propagation coverage, three sub-observables) + Checklist row 7. V-02 added a confidence stratification row in both places. C-33 makes this mandatory: each quality axis you target must produce one axis row plus one Checklist row. Fixed-depth template = C-22 pass, C-33 fail.

**C-34 — Empty-State Templates** (upgrades C-19/C-23)

V-02 showed an empty-state template for each action track. This distinguishes "Track 2 executed and found zero qualifying findings" from "Track 2 was skipped." C-34 extends this to all structured output sections: Coverage Gate, T-1 ANNEX, Entity Coverage Matrix, action tracks. Absence without an empty-state marker = structurally indistinguishable from a skipped section = fail.

**C-35 — Confidence Rationale Sub-Field** (upgrades C-30)

V-02 added `Conf rationale` alongside `Confidence: HIGH / LOW` in the Finding Schema. C-30 requires the label; C-35 requires the label to be accompanied by a rationale that makes the assignment falsifiable. "HIGH" is an assertion. "HIGH — spec section 4.2 explicitly defines the permission boundary" is an argument a reviewer can check.

---

Rubric written to `simulations/quest/rubrics/campaign-simulate-rubric-v8-2026-03-17.md`. Aspirational pool grows 23 → 27. The `*(C-04 through C-25 — unchanged from v6)*` placeholder is preserved from v7 since those criteria are unchanged.
 depth → they now self-extend: each quality axis targeted by the simulation (C-29 propagation, C-30 confidence, C-31 type-verb) adds one axis row (≥3 sub-observables) and one Checklist verification row (≥3 sub-claims); a simulation that inherits a fixed-depth template without extending it satisfies C-16/C-22 but fails C-33
- **C-19/C-23/C-34** — Templates exist for T-1 ANNEX and genre glossary → every structured output section that could be empty requires a named empty-state template; silence is not allowed as a representation of "no content"
- **C-30/C-35** — Confidence field in Finding Schema is a typed label → it now carries a Conf rationale sub-field; a label without a rationale is an assertion, not an argument, and fails C-35

**Rule ID chain now complete (C-29/C-32):** C-29 requires every dependency rule declared in the
cross-skill dependency map to be either re-examined (finding recorded) or logged as an OPEN
PROPAGATION GAP. C-32 requires every such rule to carry a stable DR-NN identifier cited
consistently in three places: (1) the map declaration, (2) the Coverage Gate row for that rule,
and (3) the evidence field of any finding that instantiates the rule. A Coverage Gate row that
audits rule "lifecycle event precedes permission check" without citing a DR-NN ID satisfies C-29
but fails C-32. The DR-NN identifier converts the Coverage Gate from a prose narrative into a
lookup table where every row has a unique key and every finding can be traced back to the rule
that motivated it. Without the IDs, verifying completeness requires reading all prose; with them,
it requires only a set membership check: {declared DR-NNs} ⊆ {gate rows ∪ gap log entries}.

**Structural self-extension now mandatory (C-33):** C-22 requires each axis row in the Structural
Axis Declaration to declare ≥3 sub-observables. C-33 requires the number of axis rows — and the
number of Compliance Checklist verification rows — to scale with the quality axes targeted by the
specific simulation run. A simulation targeting C-29 (propagation coverage) must add a propagation
axis row to the declaration and a propagation verification row to the checklist; a simulation
targeting C-30 (confidence stratification) must add a confidence stratification row to each. A
simulation that uses a fixed five-row template without extending it satisfies C-16/C-22 but fails
C-33. Axes not targeted by the simulation are exempt — the extension requirement is per targeted
axis, not per all possible axes. The criterion prevents the structural framework from being a
static boilerplate; it requires the framework to reflect the simulation's actual quality commitments.

**Silent-omission defense now structural (C-34):** C-19 requires genre glossary and T-1 rules
before execution; C-23 requires T-1 ANNEX with withheld-T1 examples. C-34 extends this to all
structured output sections with a schema: every such section (action tracks, Coverage Gate,
T-1 ANNEX, Entity Coverage Matrix) must provide a named empty-state template that is shown when
the section has no content to report. A simulation that simply omits "Track 2: Confirm Spec First"
when no LOW-confidence/HIGH-blast findings exist is structurally indistinguishable from one that
skipped the confidence stratification step entirely. The empty-state template eliminates that
ambiguity: "Track 2 — executed; zero findings qualified" is a verifiable execution record;
silence is not. C-34 passes only when every structured section either contains content or displays
its empty-state template. A section absent without either form = fail.

**Confidence auditability now enforced (C-35):** C-30 requires findings to carry a Confidence
field (HIGH/LOW) and the final action list to split into two named tracks by confidence tier.
C-35 requires the Confidence field to carry a Conf rationale sub-field alongside the label.
A finding that states "Confidence: HIGH" without a rationale satisfies C-30's label requirement
but fails C-35. The rationale field converts a declaration into an argument: "HIGH — spec
section 4.2 explicitly defines the permission boundary" is falsifiable; "HIGH" alone is not.
A reviewer can check whether the rationale justifies the label; without a rationale there is
nothing to check. Findings that do not participate in C-30's stratification (MEDIUM or LOW
blast-radius findings not assigned to a track) are exempt from C-35.

- V-01 from Round 8 satisfies C-32 (DR-NN IDs throughout dependency map and Coverage Gate)
  and C-33 (propagation coverage as Row 6 + Checklist row 7 with three sub-claims). V-01 does
  not target C-34 or C-35.
- V-02 from Round 8 satisfies C-33 (confidence stratification axis row + Checklist row with
  three sub-claims), C-34 (empty-state templates for both action tracks), and C-35 (Conf
  rationale field in Finding Schema). V-02 does not target C-32.
- A variation satisfying all four (C-32 + C-33 + C-34 + C-35) requires the dependency map
  with DR-NN IDs from V-01 and the confidence rationale + empty-state templates from V-02.

Aspirational pool: 23 → 27 criteria, still capped at 10 pts. Max score 100 unchanged.

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
