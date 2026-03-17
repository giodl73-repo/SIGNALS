# quest-variate Variate — Round 8

**Date:** 2026-03-15
**Skill:** quest-variate
**Rubric:** v8 (C-01 through C-37; essential C-01–C-05)
**Round:** R8 — 4 single-axis passes (V-01, V-02, V-03, V-04) + 1 combination pass (V-05)
**Status:** in-progress

---

## Pre-Generation: Per-Axis Pole Declaration (C-16)

**Champion baseline:** R7 V-01 body — a three-phase generator with a standalone pre-phase
`## VARIATION MAP` section carrying an immutability instruction and a declaration that the
AXIS-FREEZE PROTOCOL reads axis assignments from this table (C-29). All three phases carry
`Declared responsibility:` as an explicitly labeled key with action-verb content: Phase 1
"lock axis assignments by writing a complete variation header for each planned variation",
Phase 2 "write each committed variation body in full under the AXIS-FREEZE PROTOCOL",
Phase 3 "confirm in-loop axis consistency (post-generation audit), calibrate VARIATION MAP
predictions, identify combination candidates, rank evaluation order, designate anchor."
Step 2B emits `Consistency verdict: [CONSISTENT | AXIS DIVERGENCE]` with bracket notation
at the declaration site (C-32 satisfied, C-35 satisfied in V-01). Hypothesis blocks use
`failure-condition-outcome:` and `failure-condition-implementation:` as separately labeled
keys (C-25 satisfied in V-01). AXIS-FREEZE PROTOCOL includes six-entry count gate (C-28).
NO STRUCTURAL KEY CONTRACT exists in the preamble to enforce key propagation across all
variation bodies (C-37 not enforced). NO Structural Key Uniformity Auditor role exists
(C-37 enforcement is post-hoc, not in-loop). No prohibition of title-echo content in
`Declared responsibility:` label text (C-36 partially satisfied but not enforced as a
structural constraint).

| Axis | Baseline Pole (R7 V-01 champion) | R8 Committed Variation Pole |
|------|-----------------------------------|------------------------------|
| output-format | No STRUCTURAL KEY CONTRACT in preamble; required keys (`Consistency verdict: [CONSISTENT \| AXIS DIVERGENCE]`, `Declared responsibility:`, `failure-condition-outcome:`, `failure-condition-implementation:`) are structurally present in V-01 but not declared as an invariant contract; axis changes in V-02, V-03 caused these keys to regress (C-37 fail) | V-01 single: add a `STRUCTURAL KEY CONTRACT` section to the preamble before Phase 1 that explicitly declares all required structural keys for every variation body in the set, with a structural-incompleteness assertion for any body that omits them |
| phrasing-register | `Declared responsibility:` key content uses action-verb phrases (lock, write, confirm) in R7 V-01; no explicit prohibition of title-echo or generic-label content in the template; C-36 intent is present but not enforced as a structural constraint — a generator that writes "Declared responsibility: Phase 1 — plan" passes C-33 without triggering a rewrite | V-02 single: add explicit prohibition of title-echo and generic-label content in `Declared responsibility:` keys across all phases; require that content names the specific protocol mechanism operated by each phase; a label that echoes the phase title or uses generic terms (planning, generation, review) is declared a required rewrite |
| role-sequence | No Structural Key Uniformity Auditor role exists in the role sequence; C-37 compliance can only be detected post-hoc by a scorecard; regression in generated variation bodies is not caught and required-fixed before Step 3 begins | V-03 single: insert a `Structural Key Uniformity Auditor` role as role 3 (after Variation Author, before Dependency Cataloger); the role scans all N variation bodies after Step 2 and before Step 3, emits per-key uniformity results, and blocks Step 3 until a PASS is emitted |
| inertia-framing | VARIATION MAP does not carry a `champion-structural-keys:` declaration row; the prior-round champion's structural key names are implicit from the champion description in the pre-generation section only; no per-body structural key inheritance check in AXIS-FREEZE PROTOCOL | V-04 single: add a `champion-structural-keys:` declaration row at the top of VARIATION MAP listing all required structural keys from the R7 V-01 champion; add Step 2A to AXIS-FREEZE PROTOCOL requiring each body to confirm each champion key is present before writing begins |
| lifecycle-emphasis | Three-phase structure (commit / generate / findings); AXIS-FREEZE fires per-body before writing | Not tested R8; held at baseline |
| scoring-granularity | VARIATION MAP carries per-variation per-criterion directional predictions and failure-condition predictions (C-24, C-30) | Not tested R8; held at baseline |

This table is the isolation reference. Only the committed axis changes per variation body.
V-05 is a combination pass (output-format × role-sequence) and is exempt from C-04
single-axis isolation via explicit C-04 exception (invoked in V-05 body).

---

## VARIATION MAP — Immutable after Phase 2 begins (C-27, C-29, C-30)

**[AUTHORITATIVE SOURCE] The AXIS-FREEZE PROTOCOL in Phase 2 reads axis assignments from
this table. Do not revise after Phase 2 begins.**

| V | Axis | Pass Type | Criterion Target | C-01 Direction | C-04 Direction | C-07 Direction | failure-condition-outcome prediction | failure-condition-implementation prediction |
|---|------|-----------|-----------------|----------------|----------------|----------------|--------------------------------------|----------------------------------------------|
| V-01 | output-format | single-axis | C-35, C-37 | no-change: adding a STRUCTURAL KEY CONTRACT to the preamble does not alter section completeness requirements for variation bodies themselves | no-change: preamble contract addition is confined to the pre-generation section and does not tempt drift into phase structure or hypothesis content | no-change: key contract enforcement does not alter hypothesis falsifiability quality | STRUCTURAL KEY CONTRACT is present in the preamble but C-35 and C-37 pass rates do not improve beyond R7 V-01; the contract declares required keys but does not include a structural-incompleteness assertion for bodies that omit them, leaving enforcement advisory rather than blocking | STRUCTURAL KEY CONTRACT is present and carries a structural-incompleteness assertion, but the assertion does not name the specific required-rewrite trigger (e.g., which key is missing in which body), independently failing C-23 because a structural-incompleteness assertion must be traceable to a specific violation to constitute an actionable gate |
| V-02 | phrasing-register | single-axis | C-36 | no-change: prohibition of title-echo labels does not change section completeness requirements | risk-low: requiring action-verb content names the phase mechanism, which could tempt over-specificity bleeding into a second axis, but the change is confined to `Declared responsibility:` key content only | no-change: responsibility label phrasing does not alter hypothesis falsifiability | C-36 pass rate does not improve beyond R7 V-01 partial result; explicit prohibition adds no constraint beyond what action-verb prompting already achieves in R7 V-01, making C-36 a formatting recommendation rather than an enforced structural gate | `Declared responsibility:` keys carry action-verb content in all phases but at least one label uses a phase-title synonym that was not caught by the prohibition (e.g., "execute the variation generation loop" — present but echoes the phase heading), independently failing C-36 because the prohibition must cover all near-synonym forms, not just exact title reuse |
| V-03 | role-sequence | single-axis | C-37 | no-change: adding an auditor role does not change section completeness requirements for variation bodies | no-change: auditor role fires after generation, not during — does not affect axis isolation per body | no-change: auditor role does not alter hypothesis quality | C-37 pass rate does not improve beyond zero (C-37 not targeted in any prior round); Structural Key Uniformity Auditor role is present but fires after generation — it detects regression after it has already occurred rather than preventing it; detection-without-prevention is insufficient for C-37 | Structural Key Uniformity Auditor role fires after Step 2 and emits per-key scan results correctly (FAIL for any regressed key), but the role instruction does not include a "fix before advancing to Step 3" directive — the FAIL result is emitted but Step 3 proceeds regardless, independently failing C-37 because detection without a required-fix enforcement gate does not constitute structural key uniformity |
| V-04 | inertia-framing | single-axis | C-37 | no-change: champion-structural-keys row does not change section completeness requirements | risk-medium: referencing champion key names in VARIATION MAP and AXIS-FREEZE could tempt the generator to copy additional champion structure beyond the axis change | no-change: champion key reference does not alter hypothesis quality | C-37 pass rate does not improve beyond zero; champion-structural-keys row is present in VARIATION MAP and Step 2A per-body inheritance check is present in AXIS-FREEZE, but the Step 2A check does not declare a required-entry count (how many keys must be confirmed present), leaving completeness unverifiable by count alone | Step 2A structural key inheritance check is present and names each required key, but the check does not declare the exact number of keys required and does not include a "fewer than N key confirmations is incomplete — do not proceed" instruction, independently failing C-28's count-completeness requirement applied to the structural key inheritance check |
| V-05 | output-format × role-sequence | combination (C-04 exception explicitly invoked) | C-35, C-37 | up: STRUCTURAL KEY CONTRACT in preamble + Structural Key Uniformity Auditor role creates both a declaration-level and a post-generation-scan mechanism; compound effect makes C-37 failure detectable at two independent checkpoints | risk-high: two structural additions to preamble and role sequence increase axis drift surface — contract addition touches preamble, auditor role addition touches role sequence; changes are structurally independent but both affect document architecture | no-change: combination of preamble contract and auditor role does not alter hypothesis quality | C-35 and C-37 pass rates do not jointly exceed V-01 R8 alone (C-35 single-axis baseline) and V-03 R8 alone (C-37 single-axis baseline); STRUCTURAL KEY CONTRACT and Auditor role are structurally independent — each can fail independently; combination does not create a protocol chain linking the contract to the auditor | STRUCTURAL KEY CONTRACT is present in preamble and Structural Key Uniformity Auditor role fires after Step 2, but the contract does not declare the auditor role as the enforcement mechanism for the contract's required-key list — the two artifacts are structurally disconnected, independently failing C-29's read-source declaration requirement applied to the contract-auditor link |

---

## V-01 -- Output Format: Structural Key Contract in Preamble

**axis:** output-format
**criterion-targeted:** C-35, C-37
**baseline-delta:** A STRUCTURAL KEY CONTRACT section is added to the preamble between
the EVALUATION ORDER TABLE SCHEMA and ROLES. The contract lists every structural key that
every variation body in the set must carry, declares bracket-notation as required for verdict
token fields at the field definition site, and includes a structural-incompleteness assertion
blocking advancement past any body that omits a listed key. No other section, role, step,
or protocol changes.
**completeness-risk:** The blocking directive in the structural-incompleteness assertion --
generators may omit "do not advance to next body," making the contract advisory only.

**hypothesis:**
- criterion-target: C-35 (bracket-notation binary option declaration) and C-37 (structural
  key names propagate uniformly across all variation bodies in the set)
- direction: increases C-35 and C-37 pass rates from zero (R7 V-02 and V-03 regressed
  bracket-notation and key presence when axis changed); STRUCTURAL KEY CONTRACT makes
  omission detectable at preamble level before any body is written
- mechanism: the STRUCTURAL KEY CONTRACT block is declared in the preamble before Phase 1
  executes -- listing each required structural key as an invariant that every variation body
  must carry is a required input to writing variation bodies; a generator cannot produce a
  conforming variation body without having first committed to the key list, because the
  structural-incompleteness assertion explicitly prohibits a variation body that omits any
  listed key; the preamble contract is required input to producing a body that satisfies C-35
  and C-37
- failure-condition-outcome:
    round-label:      R7
    source-variation: V-01
    criterion-born:   C-35
    evaluative-label:
      rank-label:       "first to demonstrate bracket-notation binary option declaration
                         at the verdict token field definition site"
      quality-dimension: "cleanest demonstration of C-35 compliance as a self-contained
                          field definition -- the bracket form at the declaration site makes
                          the full decision space readable without tracing conditional
                          branches; no prior variation declared both option values at the
                          definition site"
    consequence: if C-35 and C-37 pass rates do not improve beyond R7 V-01 (C-35 partial
                 for V-01 only, C-37 not satisfied as a set), redirect output-format axis
                 to an execution-site co-location mechanism embedding the key list inside
                 Phase 2 AXIS-FREEZE PROTOCOL Step 2A in R9
- failure-condition-implementation:
    round-label:      R7
    source-variation: V-02
    criterion-born:   C-37
    evaluative-label:
      rank-label:       "first to demonstrate C-37 failure via axis-change-induced key regression"
      quality-dimension: "cleanest demonstration that structural key regression is a drift
                          artifact -- the phrasing-register axis change did not target hypothesis
                          key naming yet failure-condition-outcome: regressed to failure-condition:"
    consequence: if the STRUCTURAL KEY CONTRACT is present but its structural-incompleteness
                 assertion omits the blocking directive, the contract is advisory and C-37 is not
                 enforced -- independently fails C-37 because detection without a required-fix gate
                 does not constitute key-name uniformity enforcement

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

NON-SUPPRESSION INVARIANT CONTRACT

The compliance audit in this run contains two independent checkpoints (Declaration
Check and Population Check). This contract governs their execution behavior.

Invariant: Both checkpoints must emit their labeled results regardless of the
pass/fail state of either checkpoint. A FAIL result on the Declaration Check does
not suppress execution or result emission for the Population Check. A FAIL result
on the Population Check does not suppress the Declaration Check result.

Prohibited pattern -- SHORT-CIRCUIT SUPPRESSION: emitting only the Declaration
Check result when it fails, and omitting the Population Check output entirely.
Any audit section that exhibits short-circuit suppression is structurally incomplete.

NON-SUPPRESSION STRUCTURAL INCOMPLETENESS ASSERTION: An audit section that does not
explicitly state the non-suppression invariant is structurally incomplete and must
be rewritten before the step is declared complete.

Compliance: The audit section in Step 4 item 4 must include the following statement
before the checkpoints run:
  "NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
   regardless of each other's pass/fail state."

COLUMN CONTRACT

Before any evaluation order table is written in this run, declare all required
columns here. A table written without first completing this Column Contract is
structurally incomplete and must not be committed.

Required columns:
  [ ] Tier
  [ ] V
  [ ] Axis
  [ ] Evaluation Cost
  [ ] Axis Cost Rationale
  [ ] Independence
  [ ] Cross-Round Dependency
  [ ] Catalog Source

STRUCTURAL INCOMPLETENESS ASSERTION: A generator that writes any evaluation order
table in this run without first completing the Column Contract above (all boxes
checked, Axis Cost Rationale and Catalog Source columns explicitly declared)
produces structurally incomplete output. The table must not be committed until the
contract is complete.

EVALUATION ORDER TABLE SCHEMA

(Apply only after Column Contract is complete and all columns are checked above.)

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

Column definitions:
- "Tier": evaluation priority tier; Tier 1 = evaluate first.
- "V": variation label (V-01 through V-0N).
- "Axis": canonical axis name.
- "Evaluation Cost": low / medium / high with a one-line explanation.
- "Axis Cost Rationale": per-axis structural reason for this row's tier position. Must
  state: (a) structural property of this axis driving the cost level; (b) why this
  variation is independent or what prior-round result it requires.
- "Independence": yes / partial / no with a dependency note.
- "Cross-Round Dependency": Round + Variation + Metric, or "none."
- "Catalog Source": the specific Step 3 row from which this entry was derived.

REQUIRED: Every row must have a non-blank "Axis Cost Rationale" value containing
a per-axis structural reason.

STRUCTURAL KEY CONTRACT

Every variation body generated in this run must carry each of the following structural
keys. A variation body that omits any key listed below is structurally incomplete and
must be rewritten before advancing to the next variation.

Required structural keys -- every variation body must carry all of these:

  1. Consistency verdict: [CONSISTENT | AXIS DIVERGENCE] -- bracket-notation binary
     option declaration at the verdict token field definition site in Step 2B. The bracket
     form must appear at the declaration site. A Step 2B that emits the token without
     declaring both option values using bracket notation at the field definition site does
     not satisfy this key requirement.

  2. Declared responsibility: -- present as an explicitly labeled key immediately after
     the phase title in Phase 1, Phase 2, and Phase 3. All three phases must carry the key.
     A phase that communicates responsibility through prose or title alone does not satisfy
     this key requirement.

  3. failure-condition-outcome: -- present as a separately labeled key in every hypothesis
     block. Must not be collapsed into a single failure-condition: field.

  4. failure-condition-implementation: -- present as a separately labeled key in every
     hypothesis block, distinct from failure-condition-outcome:. Must name the criterion ID
     that the implementation failure would independently violate.

STRUCTURAL KEY CONTRACT INCOMPLETENESS ASSERTION: A variation body that does not carry
all four required structural keys above is structurally incomplete. Do not advance to the
next variation until all four keys are present in the current body. An evaluation that
declares a variation body complete without checking for all four keys produces structurally
incomplete output.

ROLES

1. Axis Selector
   Responsibility: Execute Step 1. Select {N} distinct axes from the canonical list.
   Commit the axis list before Step 2 begins.

2. Variation Author
   Responsibility: Execute Step 2. For each selected axis, write one complete,
   standalone variation body with fully populated hypothesis block including
   failure-condition chain. Do not begin the next variation until the current
   body is complete. Before advancing, verify all four STRUCTURAL KEY CONTRACT
   keys are present in the completed body.

3. Dependency Cataloger
   Responsibility: Execute Step 3. Produce the cross-round dependency catalog.
   All four columns must be non-blank in every row. A blank column means the
   hypothesis is incomplete -- return to Step 2 before proceeding. Step 4 must
   not begin until this catalog is complete.

4. Column Schema Auditor
   Responsibility: Two independent verification passes.

   PASS 1 -- DECLARATION CHECK (runs after Step 3, before Step 4 item 3):
     Verify:
       [ ] Column Contract block present in output: yes / no
       [ ] "Axis Cost Rationale" column explicitly named in contract: yes / no
       [ ] "Catalog Source" column explicitly named in contract: yes / no
     Emit: "Column Schema Auditor Pass 1 complete. Declaration check: [PASS /
     FAIL -- name failing item]."

   PASS 2 -- POPULATION CHECK (runs after Step 4 item 3):
     For each variation in the evaluation order table, verify:
       [ ] Axis Cost Rationale value non-blank with per-axis reason: yes / no
       [ ] Catalog Source value non-blank: yes / no
     Emit per row: "V-NN Axis Cost Rationale: [present / missing -- rewrite required].
     V-NN Catalog Source: [populated / blank -- rewrite required]."
     Emit summary: "Column Schema Auditor Pass 2 complete. Population check:
     [PASS -- all rows populated / FAIL -- list blank rows]."

   INDEPENDENCE REQUIREMENT: Pass 1 and Pass 2 are structurally independent.
   A FAIL on Pass 1 does not suppress Pass 2. Both passes must appear.

5. Findings Synthesizer
   Responsibility: Execute Step 4. May not declare Step 4 item 3 complete until
   Column Schema Auditor has completed both passes AND Axis Cost Quality Gate emits PASS.

6. Axis Cost Quality Gate
   Responsibility: Runs after Column Schema Auditor completes both passes. Classifies
   each Axis Cost Rationale cell as STRUCTURAL or GENERIC.
   Emit per row: "V-NN Rationale Quality: STRUCTURAL [quoted] /
     GENERIC -- rewrite required [quoted]."
   Emit summary: "Axis Cost Quality Gate: PASS -- all rows structural /
     FAIL -- rows [list] contain generic rationale; rewrite required."
   Findings Synthesizer must not declare item 3 complete until this role emits PASS.

STEP 1 -- SELECT AXES

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} selected axes. Do not begin Step 2 until the list is committed.

STEP 2 -- VARIATION BODIES

For each selected axis, write one complete variation body.

VARIATION MAP -- Immutable after Phase 2 begins

Before Phase 1 begins, commit the axis assignment and per-variation per-criterion
directional predictions for each of the {N} planned variations.

| V | Assigned Axis | Criterion Target | C-01 Direction | C-04 Direction | C-07 Direction | Notes |
|---|--------------|-----------------|----------------|----------------|----------------|-------|
[Fill all {N} rows. Each direction cell: verdict + mechanism sentence.
Do not proceed to Phase 1 until all rows are filled.]

Do not revise this table after Phase 2 begins.
The AXIS-FREEZE PROTOCOL in Phase 2 reads axis assignments from this table.

PHASE 1 -- COMMIT VARIATION HEADERS
Declared responsibility: lock axis assignments by writing a complete variation header
for each planned variation -- every field populated, axis value must exactly match
the VARIATION MAP assignment for that row.

Header format (all fields required, none blank):

  variation: V-NN
  axis: [must match VARIATION MAP]
  pole: [specific change this variation makes]
  baseline-delta: [single structural element that changes]
  completeness-risk: [section most at risk of omission]
  criterion-target: [C-NN by ID]
  direction: [increases / decreases / stabilizes] [criterion] pass rates
  mechanism: [structural pathway -- necessity language required]
  failure-condition-outcome: [if criterion does not exceed prior baseline, mechanism refuted]
  failure-condition-implementation: [which C-NN independently violated if mechanism wrong]

Review all {N} headers. Verify every axis matches the VARIATION MAP. Commit.
Do not revise axis assignments after Phase 2 begins.

PHASE 2 -- GENERATE VARIATION BODIES
Declared responsibility: write each committed variation body in full under the
AXIS-FREEZE PROTOCOL -- committed axis is the only element that changes from the
baseline; every section written out; no placeholders; no cross-references to other
variations.

AXIS-FREEZE PROTOCOL (fires once per body, before writing begins):

  Step 1 -- Read: state the axis assigned in the VARIATION MAP for this body.

  Step 2 -- Write one freeze declaration for every axis:
    - role-sequence:       [FROZEN | COMMITTED -- read from VARIATION MAP]
    - output-format:       [FROZEN | COMMITTED -- read from VARIATION MAP]
    - lifecycle-emphasis:  [FROZEN | COMMITTED -- read from VARIATION MAP]
    - phrasing-register:   [FROZEN | COMMITTED -- read from VARIATION MAP]
    - inertia-framing:     [FROZEN | COMMITTED -- read from VARIATION MAP]
    - scoring-granularity: [FROZEN | COMMITTED -- read from VARIATION MAP]

  All six canonical axes must appear. Exactly one COMMITTED. Five FROZEN.
  A freeze list with fewer than six entries is incomplete -- do not proceed.

  Step 2B -- Cross-artifact axis consistency check (fires before Step 3):
    - VARIATION MAP assigned axis for this V-NN: [read from VARIATION MAP]
    - Phase 1 header declared axis for this V-NN: [read from Phase 1 header]
    - Consistency verdict: [CONSISTENT | AXIS DIVERGENCE]
    - If AXIS DIVERGENCE: halt -- do not proceed until resolved.

  Step 3 -- Write the body. Change only the COMMITTED axis. Write every section
  in full. Before advancing to next body, verify all four STRUCTURAL KEY CONTRACT
  keys are present.

Do not begin the next variation until the current body is complete, the
AXIS-FREEZE PROTOCOL shows all six canonical axis entries, Step 2B shows
CONSISTENT, and all four STRUCTURAL KEY CONTRACT keys are confirmed present.

PHASE 3 -- FINDINGS
Declared responsibility: confirm in-loop axis consistency (post-generation audit),
calibrate VARIATION MAP predictions against actual body structures, identify
combination candidates, rank evaluation order, designate anchor.

1. Axis alignment confirmation:
| V | Axis (VARIATION MAP) | Axis (Phase 1 header) | Step 2B Result | Post-Gen Match? |
|---|---------------------|----------------------|----------------|-----------------|

2. Prediction calibration:
| V | Axis | C-07 Predicted | C-07 in Body | Correct? | Mis-prediction Mechanism |
|---|------|----------------|-------------|----------|--------------------------|

3. Combination candidates:
| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness | Compound Effect | Criteria |
|----------|-----------|------------|------------------------|-------------------|-----------------|----------|

4. Evaluation order:
| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

5. Anchor: one variation. Justify structural impact, isolation quality, detectable
   failure condition -- one sentence each.

STEP 3 -- CROSS-ROUND DEPENDENCY CATALOG

| V | Axis | Comparative Claim (quoted) | Prior-Round Result Required | Round + Variation + Metric | Independent |
|---|------|----------------------------|-----------------------------|----------------------------|-------------|

STEP 4 -- FINDINGS

Complete the Column Contract before writing any table. Write "Column Contract complete.
Proceeding to findings." before any table.

1. Variation map:
| V | Axis | Change Made | Hypothesis Summary | C-04 Prediction | C-07 Prediction |
|---|------|-------------|-------------------|-----------------|-----------------|

2. Combination candidates: [compound-effects model, four sub-elements per pair]

[Column Schema Auditor Pass 1 emitted here -- after Step 3, before item 3.]

3. Evaluation order:
| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

[Column Schema Auditor Pass 2 emitted here.]
[Axis Cost Quality Gate emitted here.]

4. Compliance audit:

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

4a -- DECLARATION CHECK:
  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4a):
    EXECUTION DIRECTIVE: Advance to 4b regardless of this checkpoint's result.
  [ ] Column Contract block present: yes / no
  [ ] Axis Cost Rationale column named: yes / no
  [ ] Catalog Source column named: yes / no
  4a Declaration Check Result: PASS (all yes) / FAIL (name failing item)

4b -- POPULATION CHECK:
  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4b):
    EXECUTION DIRECTIVE: Execute this check. Do not suppress based on 4a result.
  (Executing 4b regardless of 4a result.)
  | V | Axis Cost Rationale Value | Catalog Source Value | Row Result |
  |---|--------------------------|---------------------|------------|
  4b Population Check Result: PASS (all rows populated) / FAIL (list incomplete rows)

Both passes must appear regardless of either pass result.
C-24 Pass: yes only if Declaration Check Result is PASS AND Population Check Result is PASS.

5. Anchor: one variation. Justify structural impact, isolation quality, detectable
   failure condition -- one sentence each.

---

## V-02 -- Phrasing Register: Action-Verb Declared Responsibility Prohibition

**axis:** phrasing-register
**criterion-targeted:** C-36
**baseline-delta:** In Phase 1, Phase 2, and Phase 3, the Declared responsibility: key
definition adds an explicit prohibition: "A Declared responsibility: label whose content
echoes the phase title or uses a generic term (planning, generation, review) is a required
rewrite." The key must name the specific protocol mechanism the phase operates (lock, write,
confirm), not describe the phase category. No other section, role, step, or protocol changes.
**completeness-risk:** The "required rewrite" trigger -- generators may add the prohibition
text but produce a label that is a near-synonym of the title without triggering the rewrite
rule (e.g., "execute the generation loop" is generic but not a literal title echo).

**hypothesis:**
- criterion-target: C-36 (responsibility label content grounded in protocol action verb)
- direction: increases C-36 pass rates; C-33 retention: no-change (Declared responsibility:
  key is already present in all phases -- the prohibition constrains the key's content, not
  its presence)
- mechanism: adding an explicit prohibition of title-echo and generic-label content at each
  Declared responsibility: key definition site constrains the generator's label choices at
  the point of production -- a generator encountering "required rewrite" for a generic label
  must substitute the specific protocol mechanism name; the prohibition is a required input
  to producing a C-36-compliant label because without the constraint, a generator can satisfy
  C-33 (key present) while failing C-36 (content generic); the prohibition converts C-36 from
  a post-production judgment into a point-of-production constraint
- failure-condition-outcome:
    round-label:      R7
    source-variation: V-01
    criterion-born:   C-36
    evaluative-label:
      rank-label:       "first to demonstrate action-verb-grounded Declared responsibility:
                         content -- lock axis assignments / write committed variation bodies
                         / confirm in-loop axis consistency each directly name the protocol
                         mechanism"
      quality-dimension: "cleanest demonstration of C-36 compliance as self-checking label
                          content -- each action verb is falsifiable against the phase's
                          protocol operation; a scorecard can verify that 'lock' names the
                          Phase 1 commitment operation without parsing the phase narrative"
    consequence: if C-36 pass rate does not improve beyond R7 V-01 partial result (action-verb
                 content present but not enforced as a structural constraint), the prohibition
                 adds no constraint benefit over action-verb prompting alone; redirect
                 phrasing-register axis to structural enforcement via a per-phase
                 content-validation step in R9
- failure-condition-implementation:
    round-label:      R7
    source-variation: V-02
    criterion-born:   C-37
    evaluative-label:
      rank-label:       "first to demonstrate C-37 failure via Declared responsibility: key
                         dropout when phrasing-register axis changed"
      quality-dimension: "cleanest demonstration that a phrasing-register axis change induces
                          C-33 dropout in Phase 1 and Phase 2 -- the axis does not target phase
                          structure, yet the key disappeared; established that C-37 requires
                          set-level enforcement independent of axis targeting"
    consequence: if the action-verb prohibition is present but a near-synonym of the phase
                 title passes without triggering the rewrite rule (e.g., "execute variation
                 generation" for Phase 2), the prohibition is incomplete -- independently
                 fails C-36 because near-synonyms that do not name the specific protocol
                 mechanism (AXIS-FREEZE PROTOCOL for Phase 2) satisfy C-33 while failing C-36

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

NON-SUPPRESSION INVARIANT CONTRACT

The compliance audit in this run contains two independent checkpoints (Declaration
Check and Population Check). This contract governs their execution behavior.

Invariant: Both checkpoints must emit their labeled results regardless of the
pass/fail state of either checkpoint. A FAIL result on the Declaration Check does
not suppress execution or result emission for the Population Check. A FAIL result
on the Population Check does not suppress the Declaration Check result.

Prohibited pattern -- SHORT-CIRCUIT SUPPRESSION: emitting only the Declaration
Check result when it fails, and omitting the Population Check output entirely.
Any audit section that exhibits short-circuit suppression is structurally incomplete.

NON-SUPPRESSION STRUCTURAL INCOMPLETENESS ASSERTION: An audit section that does not
explicitly state the non-suppression invariant is structurally incomplete and must
be rewritten before the step is declared complete.

Compliance: The audit section in Step 4 item 4 must include the following statement
before the checkpoints run:
  "NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
   regardless of each other's pass/fail state."

COLUMN CONTRACT

Before any evaluation order table is written in this run, declare all required
columns here. A table written without first completing this Column Contract is
structurally incomplete and must not be committed.

Required columns:
  [ ] Tier
  [ ] V
  [ ] Axis
  [ ] Evaluation Cost
  [ ] Axis Cost Rationale
  [ ] Independence
  [ ] Cross-Round Dependency
  [ ] Catalog Source

STRUCTURAL INCOMPLETENESS ASSERTION: A generator that writes any evaluation order
table in this run without first completing the Column Contract above (all boxes
checked, Axis Cost Rationale and Catalog Source columns explicitly declared)
produces structurally incomplete output. The table must not be committed until the
contract is complete.

EVALUATION ORDER TABLE SCHEMA

(Apply only after Column Contract is complete and all columns are checked above.)

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

Column definitions:
- "Tier": evaluation priority tier; Tier 1 = evaluate first.
- "V": variation label (V-01 through V-0N).
- "Axis": canonical axis name.
- "Evaluation Cost": low / medium / high with a one-line explanation.
- "Axis Cost Rationale": per-axis structural reason for this row's tier position. Must
  state: (a) structural property of this axis driving the cost level; (b) why this
  variation is independent or what prior-round result it requires.
- "Independence": yes / partial / no with a dependency note.
- "Cross-Round Dependency": Round + Variation + Metric, or "none."
- "Catalog Source": the specific Step 3 row from which this entry was derived.

REQUIRED: Every row must have a non-blank "Axis Cost Rationale" value containing
a per-axis structural reason.

ROLES

1. Axis Selector
   Responsibility: Execute Step 1. Select {N} distinct axes from the canonical list.
   Commit the axis list before Step 2 begins.

2. Variation Author
   Responsibility: Execute Step 2. For each selected axis, write one complete,
   standalone variation body with fully populated hypothesis block including
   failure-condition chain. Do not begin the next variation until the current
   body is complete.

3. Dependency Cataloger
   Responsibility: Execute Step 3. Produce the cross-round dependency catalog.
   All four columns must be non-blank in every row. A blank column means the
   hypothesis is incomplete -- return to Step 2 before proceeding. Step 4 must
   not begin until this catalog is complete.

4. Column Schema Auditor
   Responsibility: Two independent verification passes.

   PASS 1 -- DECLARATION CHECK (runs after Step 3, before Step 4 item 3):
     Verify:
       [ ] Column Contract block present in output: yes / no
       [ ] "Axis Cost Rationale" column explicitly named in contract: yes / no
       [ ] "Catalog Source" column explicitly named in contract: yes / no
     Emit: "Column Schema Auditor Pass 1 complete. Declaration check: [PASS /
     FAIL -- name failing item]."

   PASS 2 -- POPULATION CHECK (runs after Step 4 item 3):
     For each variation in the evaluation order table, verify:
       [ ] Axis Cost Rationale value non-blank with per-axis reason: yes / no
       [ ] Catalog Source value non-blank: yes / no
     Emit per row: "V-NN Axis Cost Rationale: [present / missing -- rewrite required].
     V-NN Catalog Source: [populated / blank -- rewrite required]."
     Emit summary: "Column Schema Auditor Pass 2 complete. Population check:
     [PASS -- all rows populated / FAIL -- list blank rows]."

   INDEPENDENCE REQUIREMENT: Pass 1 and Pass 2 are structurally independent.
   A FAIL on Pass 1 does not suppress Pass 2. Both passes must appear.

5. Findings Synthesizer
   Responsibility: Execute Step 4. May not declare Step 4 item 3 complete until
   Column Schema Auditor has completed both passes AND Axis Cost Quality Gate emits PASS.

6. Axis Cost Quality Gate
   Responsibility: Runs after Column Schema Auditor completes both passes. Classifies
   each Axis Cost Rationale cell as STRUCTURAL or GENERIC.
   Emit per row: "V-NN Rationale Quality: STRUCTURAL [quoted] /
     GENERIC -- rewrite required [quoted]."
   Emit summary: "Axis Cost Quality Gate: PASS -- all rows structural /
     FAIL -- rows [list] contain generic rationale; rewrite required."
   Findings Synthesizer must not declare item 3 complete until this role emits PASS.

STEP 1 -- SELECT AXES

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} selected axes. Do not begin Step 2 until the list is committed.

STEP 2 -- VARIATION BODIES

For each selected axis, write one complete variation body.

VARIATION MAP -- Immutable after Phase 2 begins

Before Phase 1 begins, commit the axis assignment and per-variation per-criterion
directional predictions for each of the {N} planned variations.

| V | Assigned Axis | Criterion Target | C-01 Direction | C-04 Direction | C-07 Direction | Notes |
|---|--------------|-----------------|----------------|----------------|----------------|-------|
[Fill all {N} rows. Each direction cell: verdict + mechanism sentence.
Do not proceed to Phase 1 until all rows are filled.]

Do not revise this table after Phase 2 begins.
The AXIS-FREEZE PROTOCOL in Phase 2 reads axis assignments from this table.

PHASE 1 -- COMMIT VARIATION HEADERS
Declared responsibility: lock axis assignments by writing a complete variation header
for each planned variation -- every field populated, axis value must exactly match
the VARIATION MAP assignment for that row.
[PROHIBITION: A Declared responsibility: label whose content echoes the phase title
(e.g., "Declared responsibility: Phase 1 -- commit headers") or uses a generic term
(planning, setup, preparation) is a required rewrite. The label must name the specific
protocol mechanism this phase operates: for Phase 1, the mechanism is locking axis
assignments by populating and committing variation headers before generation begins.]

Header format (all fields required, none blank):

  variation: V-NN
  axis: [must match VARIATION MAP]
  pole: [specific change this variation makes]
  baseline-delta: [single structural element that changes]
  completeness-risk: [section most at risk of omission]
  criterion-target: [C-NN by ID]
  direction: [increases / decreases / stabilizes] [criterion] pass rates
  mechanism: [structural pathway -- necessity language required]
  failure-condition-outcome: [if criterion does not exceed prior baseline, mechanism refuted]
  failure-condition-implementation: [which C-NN independently violated if mechanism wrong]

Review all {N} headers. Verify every axis matches the VARIATION MAP. Commit.
Do not revise axis assignments after Phase 2 begins.

PHASE 2 -- GENERATE VARIATION BODIES
Declared responsibility: write each committed variation body in full under the
AXIS-FREEZE PROTOCOL -- committed axis is the only element that changes from the
baseline; every section written out; no placeholders; no cross-references to other
variations.
[PROHIBITION: A Declared responsibility: label whose content echoes the phase title
(e.g., "Declared responsibility: Phase 2 -- generate bodies") or uses a generic term
(generation, execution, output) is a required rewrite. The label must name the specific
protocol mechanism this phase operates: for Phase 2, the mechanism is writing each
committed variation body under the AXIS-FREEZE PROTOCOL with per-body pre-write
enforcement before each body is written.]

AXIS-FREEZE PROTOCOL (fires once per body, before writing begins):

  Step 1 -- Read: state the axis assigned in the VARIATION MAP for this body.

  Step 2 -- Write one freeze declaration for every axis:
    - role-sequence:       [FROZEN | COMMITTED -- read from VARIATION MAP]
    - output-format:       [FROZEN | COMMITTED -- read from VARIATION MAP]
    - lifecycle-emphasis:  [FROZEN | COMMITTED -- read from VARIATION MAP]
    - phrasing-register:   [FROZEN | COMMITTED -- read from VARIATION MAP]
    - inertia-framing:     [FROZEN | COMMITTED -- read from VARIATION MAP]
    - scoring-granularity: [FROZEN | COMMITTED -- read from VARIATION MAP]

  All six canonical axes must appear. Exactly one COMMITTED. Five FROZEN.
  A freeze list with fewer than six entries is incomplete -- do not proceed.

  Step 2B -- Cross-artifact axis consistency check (fires before Step 3):
    - VARIATION MAP assigned axis for this V-NN: [read from VARIATION MAP]
    - Phase 1 header declared axis for this V-NN: [read from Phase 1 header]
    - Consistency verdict: [CONSISTENT | AXIS DIVERGENCE]
    - If AXIS DIVERGENCE: halt -- do not proceed until resolved.

  Step 3 -- Write the body. Change only the COMMITTED axis. Write every section
  in full.

Do not begin the next variation until the current body is complete.

PHASE 3 -- FINDINGS
Declared responsibility: confirm in-loop axis consistency (post-generation audit),
calibrate VARIATION MAP predictions against actual body structures, identify
combination candidates, rank evaluation order, designate anchor.
[PROHIBITION: A Declared responsibility: label whose content echoes the phase title
(e.g., "Declared responsibility: Phase 3 -- findings") or uses a generic term
(review, synthesis, reporting) is a required rewrite. The label must name the specific
protocol mechanism this phase operates: for Phase 3, the mechanism is confirming in-loop
axis consistency, calibrating predictions, generating combination candidates, ranking
evaluation order, and designating the anchor variation.]

1. Axis alignment confirmation:
| V | Axis (VARIATION MAP) | Axis (Phase 1 header) | Step 2B Result | Post-Gen Match? |
|---|---------------------|----------------------|----------------|-----------------|

2. Prediction calibration:
| V | Axis | C-07 Predicted | C-07 in Body | Correct? | Mis-prediction Mechanism |
|---|------|----------------|-------------|----------|--------------------------|

3. Combination candidates:
| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness | Compound Effect | Criteria |
|----------|-----------|------------|------------------------|-------------------|-----------------|----------|

4. Evaluation order:
| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

5. Anchor: one variation. Justify structural impact, isolation quality, detectable
   failure condition -- one sentence each.

STEP 3 -- CROSS-ROUND DEPENDENCY CATALOG

| V | Axis | Comparative Claim (quoted) | Prior-Round Result Required | Round + Variation + Metric | Independent |
|---|------|----------------------------|-----------------------------|----------------------------|-------------|

STEP 4 -- FINDINGS

Complete the Column Contract before writing any table. Write "Column Contract complete.
Proceeding to findings." before any table.

1. Variation map:
| V | Axis | Change Made | Hypothesis Summary | C-04 Prediction | C-07 Prediction |
|---|------|-------------|-------------------|-----------------|-----------------|

2. Combination candidates: [compound-effects model, four sub-elements per pair]

[Column Schema Auditor Pass 1 emitted here -- after Step 3, before item 3.]

3. Evaluation order:
| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

[Column Schema Auditor Pass 2 emitted here.]
[Axis Cost Quality Gate emitted here.]

4. Compliance audit:

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

4a -- DECLARATION CHECK:
  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4a):
    EXECUTION DIRECTIVE: Advance to 4b regardless of this checkpoint's result.
  [ ] Column Contract block present: yes / no
  [ ] Axis Cost Rationale column named: yes / no
  [ ] Catalog Source column named: yes / no
  4a Declaration Check Result: PASS (all yes) / FAIL (name failing item)

4b -- POPULATION CHECK:
  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4b):
    EXECUTION DIRECTIVE: Execute this check. Do not suppress based on 4a result.
  (Executing 4b regardless of 4a result.)
  | V | Axis Cost Rationale Value | Catalog Source Value | Row Result |
  |---|--------------------------|---------------------|------------|
  4b Population Check Result: PASS (all rows populated) / FAIL (list incomplete rows)

Both passes must appear regardless of either pass result.
C-24 Pass: yes only if Declaration Check Result is PASS AND Population Check Result is PASS.

5. Anchor: one variation. Justify structural impact, isolation quality, detectable
   failure condition -- one sentence each.

---

## V-03 -- Role Sequence: Structural Key Uniformity Auditor

**axis:** role-sequence
**criterion-targeted:** C-37
**baseline-delta:** A Structural Key Uniformity Auditor is inserted as role 3 in the
ROLES section (after Variation Author, before Dependency Cataloger; existing roles 3
through 6 renumbered 4 through 7). The role fires after Step 2 is complete and before
Step 3 begins. It scans all N variation bodies for required structural keys, emits per-key
uniformity results, and blocks Step 3 until it emits PASS. No other section, step, or
protocol changes. The role numbering in role references throughout the skill body updates
to match (Dependency Cataloger is now role 4, Column Schema Auditor is role 5, Findings
Synthesizer is role 6, Axis Cost Quality Gate is role 7).
**completeness-risk:** The blocking directive -- generators may omit "Step 3 must not begin
until this role emits PASS," making the auditor informational rather than enforced.

**hypothesis:**
- criterion-target: C-37 (structural key names propagate uniformly across all variation
  bodies in the set)
- direction: increases C-37 pass rates from zero (no set-level structural key uniformity
  scan existed in any prior round); the Structural Key Uniformity Auditor role makes key
  regression visible as a named FAIL before Step 3 and the findings phase begin
- mechanism: inserting a Structural Key Uniformity Auditor role between Step 2 (generation)
  and Step 3 (dependency catalog) creates a required checkpoint that scans all N variation
  bodies for structural key consistency before the findings phase begins; the role's "Step 3
  must not begin until PASS" directive converts C-37 detection from a post-hoc scorecard
  check into a protocol gate that blocks downstream steps; a set of variation bodies cannot
  advance to Step 3 without passing the structural key uniformity scan, making the scan a
  required input to completing the run
- failure-condition-outcome:
    round-label:      R7
    source-variation: V-03
    criterion-born:   C-37
    evaluative-label:
      rank-label:       "first inertia-framing variation in R7 -- champion-baseline field
                         added at body scope without key-uniformity enforcement"
      quality-dimension: "cleanest demonstration that inertia-framing alone does not prevent
                          key regression -- champion-baseline citation is body-local; the
                          scan needed is set-level, not per-body reference"
    consequence: if C-37 pass rate does not improve beyond zero (Structural Key Uniformity
                 Auditor detects regression but the blocking directive is missing), the role
                 is informational rather than enforced; combine with output-format axis
                 (V-01 R8 STRUCTURAL KEY CONTRACT) in R9 to create a declaration-level
                 contract that the auditor enforces
- failure-condition-implementation:
    round-label:      R7
    source-variation: V-02
    criterion-born:   C-37
    evaluative-label:
      rank-label:       "first to demonstrate C-37 failure via phrasing-register axis
                         change causing Declared responsibility: key dropout"
      quality-dimension: "cleanest evidence that set-level key uniformity requires an
                          active scan role -- the phrasing-register axis change silently
                          dropped Declared responsibility: from Phase 1 and Phase 2
                          without triggering any existing gate; only a post-generation
                          set scan would have caught this before advancing"
    consequence: if the Structural Key Uniformity Auditor role is present and emits FAIL
                 correctly for a regressed key, but the skill body does not include a
                 "required rewrite before advancing" directive in the role, Step 3 proceeds
                 regardless -- independently fails C-37 because emission of FAIL without
                 blocking advancement does not enforce structural key uniformity

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

NON-SUPPRESSION INVARIANT CONTRACT

The compliance audit in this run contains two independent checkpoints (Declaration
Check and Population Check). This contract governs their execution behavior.

Invariant: Both checkpoints must emit their labeled results regardless of the
pass/fail state of either checkpoint. A FAIL result on the Declaration Check does
not suppress execution or result emission for the Population Check. A FAIL result
on the Population Check does not suppress the Declaration Check result.

Prohibited pattern -- SHORT-CIRCUIT SUPPRESSION: emitting only the Declaration
Check result when it fails, and omitting the Population Check output entirely.
Any audit section that exhibits short-circuit suppression is structurally incomplete.

NON-SUPPRESSION STRUCTURAL INCOMPLETENESS ASSERTION: An audit section that does not
explicitly state the non-suppression invariant is structurally incomplete and must
be rewritten before the step is declared complete.

Compliance: The audit section in Step 4 item 4 must include the following statement
before the checkpoints run:
  "NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
   regardless of each other's pass/fail state."

COLUMN CONTRACT

Before any evaluation order table is written in this run, declare all required
columns here. A table written without first completing this Column Contract is
structurally incomplete and must not be committed.

Required columns:
  [ ] Tier
  [ ] V
  [ ] Axis
  [ ] Evaluation Cost
  [ ] Axis Cost Rationale
  [ ] Independence
  [ ] Cross-Round Dependency
  [ ] Catalog Source

STRUCTURAL INCOMPLETENESS ASSERTION: A generator that writes any evaluation order
table in this run without first completing the Column Contract above (all boxes
checked, Axis Cost Rationale and Catalog Source columns explicitly declared)
produces structurally incomplete output. The table must not be committed until the
contract is complete.

EVALUATION ORDER TABLE SCHEMA

(Apply only after Column Contract is complete and all columns are checked above.)

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

Column definitions:
- "Tier": evaluation priority tier; Tier 1 = evaluate first.
- "V": variation label (V-01 through V-0N).
- "Axis": canonical axis name.
- "Evaluation Cost": low / medium / high with a one-line explanation.
- "Axis Cost Rationale": per-axis structural reason for this row's tier position. Must
  state: (a) structural property of this axis driving the cost level; (b) why this
  variation is independent or what prior-round result it requires.
- "Independence": yes / partial / no with a dependency note.
- "Cross-Round Dependency": Round + Variation + Metric, or "none."
- "Catalog Source": the specific Step 3 row from which this entry was derived.

REQUIRED: Every row must have a non-blank "Axis Cost Rationale" value containing
a per-axis structural reason.

ROLES

1. Axis Selector
   Responsibility: Execute Step 1. Select {N} distinct axes from the canonical list.
   Commit the axis list before Step 2 begins.

2. Variation Author
   Responsibility: Execute Step 2. For each selected axis, write one complete,
   standalone variation body with fully populated hypothesis block including
   failure-condition chain. Do not begin the next variation until the current
   body is complete.

3. Structural Key Uniformity Auditor
   Responsibility: Runs after Step 2 is complete, before Step 3 begins. Scans all N
   variation bodies for required structural keys. Emits per-key uniformity results.
   Step 3 must not begin until this role emits PASS.

   Required structural keys to scan for across all N variation bodies:
     - Consistency verdict: [CONSISTENT | AXIS DIVERGENCE] -- in Step 2B of AXIS-FREEZE
       PROTOCOL; bracket notation must appear at the field definition site.
     - Declared responsibility: -- in Phase 1, Phase 2, and Phase 3 of each body.
     - failure-condition-outcome: -- in every hypothesis block of each body.
     - failure-condition-implementation: -- in every hypothesis block of each body.

   Emit for each required key:
     "Key [key name]: [list V-NN labels where key is present] /
      Missing from: [list V-NN labels where key is absent or regressed]."

   Emit summary:
     "Structural Key Uniformity Audit: PASS -- all required keys present uniformly
      across all {N} variation bodies." or
     "Structural Key Uniformity Audit: FAIL -- [list key names] missing or regressed
      in [list V-NN labels]. Required rewrite before Step 3 may begin."

   Step 3 must not begin until this role emits PASS. A FAIL result requires: return
   to Step 2, rewrite the identified bodies to include the missing keys, and re-run
   this role before advancing.

4. Dependency Cataloger
   Responsibility: Execute Step 3. Produce the cross-round dependency catalog.
   All four columns must be non-blank in every row. A blank column means the
   hypothesis is incomplete -- return to Step 2 before proceeding. Step 4 must
   not begin until this catalog is complete.

5. Column Schema Auditor
   Responsibility: Two independent verification passes.

   PASS 1 -- DECLARATION CHECK (runs after Step 3, before Step 4 item 3):
     Verify:
       [ ] Column Contract block present in output: yes / no
       [ ] "Axis Cost Rationale" column explicitly named in contract: yes / no
       [ ] "Catalog Source" column explicitly named in contract: yes / no
     Emit: "Column Schema Auditor Pass 1 complete. Declaration check: [PASS /
     FAIL -- name failing item]."

   PASS 2 -- POPULATION CHECK (runs after Step 4 item 3):
     For each variation in the evaluation order table, verify:
       [ ] Axis Cost Rationale value non-blank with per-axis reason: yes / no
       [ ] Catalog Source value non-blank: yes / no
     Emit per row: "V-NN Axis Cost Rationale: [present / missing -- rewrite required].
     V-NN Catalog Source: [populated / blank -- rewrite required]."
     Emit summary: "Column Schema Auditor Pass 2 complete. Population check:
     [PASS -- all rows populated / FAIL -- list blank rows]."

   INDEPENDENCE REQUIREMENT: Pass 1 and Pass 2 are structurally independent.
   A FAIL on Pass 1 does not suppress Pass 2. Both passes must appear.

6. Findings Synthesizer
   Responsibility: Execute Step 4. May not declare Step 4 item 3 complete until
   Column Schema Auditor has completed both passes AND Axis Cost Quality Gate emits PASS.

7. Axis Cost Quality Gate
   Responsibility: Runs after Column Schema Auditor completes both passes. Classifies
   each Axis Cost Rationale cell as STRUCTURAL or GENERIC.
   Emit per row: "V-NN Rationale Quality: STRUCTURAL [quoted] /
     GENERIC -- rewrite required [quoted]."
   Emit summary: "Axis Cost Quality Gate: PASS -- all rows structural /
     FAIL -- rows [list] contain generic rationale; rewrite required."
   Findings Synthesizer must not declare item 3 complete until this role emits PASS.

STEP 1 -- SELECT AXES

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} selected axes. Do not begin Step 2 until the list is committed.

STEP 2 -- VARIATION BODIES

For each selected axis, write one complete variation body.

VARIATION MAP -- Immutable after Phase 2 begins

Before Phase 1 begins, commit the axis assignment and per-variation per-criterion
directional predictions for each of the {N} planned variations.

| V | Assigned Axis | Criterion Target | C-01 Direction | C-04 Direction | C-07 Direction | Notes |
|---|--------------|-----------------|----------------|----------------|----------------|-------|
[Fill all {N} rows. Each direction cell: verdict + mechanism sentence.
Do not proceed to Phase 1 until all rows are filled.]

Do not revise this table after Phase 2 begins.
The AXIS-FREEZE PROTOCOL in Phase 2 reads axis assignments from this table.

PHASE 1 -- COMMIT VARIATION HEADERS
Declared responsibility: lock axis assignments by writing a complete variation header
for each planned variation -- every field populated, axis value must exactly match
the VARIATION MAP assignment for that row.

Header format (all fields required, none blank):

  variation: V-NN
  axis: [must match VARIATION MAP]
  pole: [specific change this variation makes]
  baseline-delta: [single structural element that changes]
  completeness-risk: [section most at risk of omission]
  criterion-target: [C-NN by ID]
  direction: [increases / decreases / stabilizes] [criterion] pass rates
  mechanism: [structural pathway -- necessity language required]
  failure-condition-outcome: [if criterion does not exceed prior baseline, mechanism refuted]
  failure-condition-implementation: [which C-NN independently violated if mechanism wrong]

Review all {N} headers. Verify every axis matches the VARIATION MAP. Commit.
Do not revise axis assignments after Phase 2 begins.

PHASE 2 -- GENERATE VARIATION BODIES
Declared responsibility: write each committed variation body in full under the
AXIS-FREEZE PROTOCOL -- committed axis is the only element that changes from the
baseline; every section written out; no placeholders; no cross-references to other
variations.

AXIS-FREEZE PROTOCOL (fires once per body, before writing begins):

  Step 1 -- Read: state the axis assigned in the VARIATION MAP for this body.

  Step 2 -- Write one freeze declaration for every axis:
    - role-sequence:       [FROZEN | COMMITTED -- read from VARIATION MAP]
    - output-format:       [FROZEN | COMMITTED -- read from VARIATION MAP]
    - lifecycle-emphasis:  [FROZEN | COMMITTED -- read from VARIATION MAP]
    - phrasing-register:   [FROZEN | COMMITTED -- read from VARIATION MAP]
    - inertia-framing:     [FROZEN | COMMITTED -- read from VARIATION MAP]
    - scoring-granularity: [FROZEN | COMMITTED -- read from VARIATION MAP]

  All six canonical axes must appear. Exactly one COMMITTED. Five FROZEN.
  A freeze list with fewer than six entries is incomplete -- do not proceed.

  Step 2B -- Cross-artifact axis consistency check (fires before Step 3):
    - VARIATION MAP assigned axis for this V-NN: [read from VARIATION MAP]
    - Phase 1 header declared axis for this V-NN: [read from Phase 1 header]
    - Consistency verdict: [CONSISTENT | AXIS DIVERGENCE]
    - If AXIS DIVERGENCE: halt -- do not proceed until resolved.

  Step 3 -- Write the body. Change only the COMMITTED axis. Write every section
  in full.

Do not begin the next variation until the current body is complete.

After all {N} bodies are complete, role 3 (Structural Key Uniformity Auditor)
must fire before Step 3 begins. Step 3 must not begin until the Structural Key
Uniformity Auditor emits PASS.

PHASE 3 -- FINDINGS
Declared responsibility: confirm in-loop axis consistency (post-generation audit),
calibrate VARIATION MAP predictions against actual body structures, identify
combination candidates, rank evaluation order, designate anchor.

1. Axis alignment confirmation:
| V | Axis (VARIATION MAP) | Axis (Phase 1 header) | Step 2B Result | Post-Gen Match? |
|---|---------------------|----------------------|----------------|-----------------|

2. Prediction calibration:
| V | Axis | C-07 Predicted | C-07 in Body | Correct? | Mis-prediction Mechanism |
|---|------|----------------|-------------|----------|--------------------------|

3. Combination candidates:
| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness | Compound Effect | Criteria |
|----------|-----------|------------|------------------------|-------------------|-----------------|----------|

4. Evaluation order:
| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

5. Anchor: one variation. Justify structural impact, isolation quality, detectable
   failure condition -- one sentence each.

STEP 3 -- CROSS-ROUND DEPENDENCY CATALOG

| V | Axis | Comparative Claim (quoted) | Prior-Round Result Required | Round + Variation + Metric | Independent |
|---|------|----------------------------|-----------------------------|----------------------------|-------------|

STEP 4 -- FINDINGS

Complete the Column Contract before writing any table. Write "Column Contract complete.
Proceeding to findings." before any table.

1. Variation map:
| V | Axis | Change Made | Hypothesis Summary | C-04 Prediction | C-07 Prediction |
|---|------|-------------|-------------------|-----------------|-----------------|

2. Combination candidates: [compound-effects model, four sub-elements per pair]

[Column Schema Auditor Pass 1 emitted here -- after Step 3, before item 3.]

3. Evaluation order:
| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

[Column Schema Auditor Pass 2 emitted here.]
[Axis Cost Quality Gate emitted here.]

4. Compliance audit:

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

4a -- DECLARATION CHECK:
  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4a):
    EXECUTION DIRECTIVE: Advance to 4b regardless of this checkpoint's result.
  [ ] Column Contract block present: yes / no
  [ ] Axis Cost Rationale column named: yes / no
  [ ] Catalog Source column named: yes / no
  4a Declaration Check Result: PASS (all yes) / FAIL (name failing item)

4b -- POPULATION CHECK:
  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4b):
    EXECUTION DIRECTIVE: Execute this check. Do not suppress based on 4a result.
  (Executing 4b regardless of 4a result.)
  | V | Axis Cost Rationale Value | Catalog Source Value | Row Result |
  |---|--------------------------|---------------------|------------|
  4b Population Check Result: PASS (all rows populated) / FAIL (list incomplete rows)

Both passes must appear regardless of either pass result.
C-24 Pass: yes only if Declaration Check Result is PASS AND Population Check Result is PASS.

5. Anchor: one variation. Justify structural impact, isolation quality, detectable
   failure condition -- one sentence each.

---

## V-04 -- Inertia Framing: Champion Structural Key Template in VARIATION MAP

**axis:** inertia-framing
**criterion-targeted:** C-37
**baseline-delta:** The VARIATION MAP section gains a champion-structural-keys: row
at the top of the table (before variation rows) listing the exact structural key names
carried by the R7 V-01 champion. The AXIS-FREEZE PROTOCOL gains a Step 2A between
Step 2 and Step 2B: a per-body structural key inheritance check that reads the champion-
structural-keys list and confirms each key will be present in this body before writing
begins. No other section, role, step, or protocol changes.
**completeness-risk:** Step 2A -- generators may list keys but omit the "fewer than N
key confirmations is incomplete -- do not proceed" count gate, leaving completeness
unverifiable by count.

**hypothesis:**
- criterion-target: C-37 (structural key names propagate uniformly across all variation
  bodies in the set)
- direction: increases C-37 pass rates from zero; champion-structural-keys row makes the
  prior-round champion's structural key names an explicit per-body reference rather than
  an implicit baseline inference; Step 2A fires before each body is written, not after
- mechanism: placing the champion-structural-keys list in the VARIATION MAP (the
  authoritative pre-generation artifact) and requiring the AXIS-FREEZE PROTOCOL to check
  against it before writing each body converts structural key inheritance from an implicit
  baseline expectation into an explicit per-body pre-write checklist; a generator cannot
  write a variation body without having first confirmed each champion structural key will
  be present, because Step 2A fires before Step 2B (the consistency check) and before
  Step 3 (the body write); the champion-structural-keys list is a required input to
  producing a body that satisfies C-37
- failure-condition-outcome:
    round-label:      R7
    source-variation: V-03
    criterion-born:   C-37
    evaluative-label:
      rank-label:       "first inertia-framing variation in R7 -- champion-baseline field
                         at body scope without key-uniformity enforcement"
      quality-dimension: "cleanest demonstration that per-body champion reference is
                          insufficient for C-37 -- champion-baseline: citation names the
                          prior variation but does not enumerate its structural keys; a
                          generator can cite the champion by label without inheriting its
                          key names"
    consequence: if C-37 pass rate does not improve beyond zero, the champion-structural-keys
                 row in VARIATION MAP adds inertia reference overhead without changing generator
                 behavior; redirect inertia-framing axis to a champion-key-mirror instruction
                 that requires each body to echo the champion's exact key names before writing
                 in R9
- failure-condition-implementation:
    round-label:      R7
    source-variation: V-04
    criterion-born:   C-37
    evaluative-label:
      rank-label:       "first combination pass in R7 -- output-format x inertia-framing
                         combining Declared responsibility: keys with champion-baseline field"
      quality-dimension: "cleanest demonstration that combination of C-33 and champion-baseline
                          does not enforce set-level key uniformity -- both structural additions
                          are body-local; the gap is that no set-scan role or per-body count
                          gate exists to enforce that all keys in the champion appear in all
                          bodies"
    consequence: if Step 2A is present and confirms each champion key by name but does not
                 declare the required confirmation count ("fewer than 4 key confirmations is
                 incomplete -- do not proceed"), key completeness is unverifiable by count --
                 independently fails C-28's count-completeness requirement applied to the
                 structural key inheritance check

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

NON-SUPPRESSION INVARIANT CONTRACT

The compliance audit in this run contains two independent checkpoints (Declaration
Check and Population Check). This contract governs their execution behavior.

Invariant: Both checkpoints must emit their labeled results regardless of the
pass/fail state of either checkpoint. A FAIL result on the Declaration Check does
not suppress execution or result emission for the Population Check. A FAIL result
on the Population Check does not suppress the Declaration Check result.

Prohibited pattern -- SHORT-CIRCUIT SUPPRESSION: emitting only the Declaration
Check result when it fails, and omitting the Population Check output entirely.
Any audit section that exhibits short-circuit suppression is structurally incomplete.

NON-SUPPRESSION STRUCTURAL INCOMPLETENESS ASSERTION: An audit section that does not
explicitly state the non-suppression invariant is structurally incomplete and must
be rewritten before the step is declared complete.

Compliance: The audit section in Step 4 item 4 must include the following statement
before the checkpoints run:
  "NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
   regardless of each other's pass/fail state."

COLUMN CONTRACT

Before any evaluation order table is written in this run, declare all required
columns here. A table written without first completing this Column Contract is
structurally incomplete and must not be committed.

Required columns:
  [ ] Tier
  [ ] V
  [ ] Axis
  [ ] Evaluation Cost
  [ ] Axis Cost Rationale
  [ ] Independence
  [ ] Cross-Round Dependency
  [ ] Catalog Source

STRUCTURAL INCOMPLETENESS ASSERTION: A generator that writes any evaluation order
table in this run without first completing the Column Contract above (all boxes
checked, Axis Cost Rationale and Catalog Source columns explicitly declared)
produces structurally incomplete output. The table must not be committed until the
contract is complete.

EVALUATION ORDER TABLE SCHEMA

(Apply only after Column Contract is complete and all columns are checked above.)

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

Column definitions:
- "Tier": evaluation priority tier; Tier 1 = evaluate first.
- "V": variation label (V-01 through V-0N).
- "Axis": canonical axis name.
- "Evaluation Cost": low / medium / high with a one-line explanation.
- "Axis Cost Rationale": per-axis structural reason for this row's tier position. Must
  state: (a) structural property of this axis driving the cost level; (b) why this
  variation is independent or what prior-round result it requires.
- "Independence": yes / partial / no with a dependency note.
- "Cross-Round Dependency": Round + Variation + Metric, or "none."
- "Catalog Source": the specific Step 3 row from which this entry was derived.

REQUIRED: Every row must have a non-blank "Axis Cost Rationale" value containing
a per-axis structural reason.

ROLES

1. Axis Selector
   Responsibility: Execute Step 1. Select {N} distinct axes from the canonical list.
   Commit the axis list before Step 2 begins.

2. Variation Author
   Responsibility: Execute Step 2. For each selected axis, write one complete,
   standalone variation body with fully populated hypothesis block including
   failure-condition chain. Do not begin the next variation until the current
   body is complete.

3. Dependency Cataloger
   Responsibility: Execute Step 3. Produce the cross-round dependency catalog.
   All four columns must be non-blank in every row. A blank column means the
   hypothesis is incomplete -- return to Step 2 before proceeding. Step 4 must
   not begin until this catalog is complete.

4. Column Schema Auditor
   Responsibility: Two independent verification passes.

   PASS 1 -- DECLARATION CHECK (runs after Step 3, before Step 4 item 3):
     Verify:
       [ ] Column Contract block present in output: yes / no
       [ ] "Axis Cost Rationale" column explicitly named in contract: yes / no
       [ ] "Catalog Source" column explicitly named in contract: yes / no
     Emit: "Column Schema Auditor Pass 1 complete. Declaration check: [PASS /
     FAIL -- name failing item]."

   PASS 2 -- POPULATION CHECK (runs after Step 4 item 3):
     For each variation in the evaluation order table, verify:
       [ ] Axis Cost Rationale value non-blank with per-axis reason: yes / no
       [ ] Catalog Source value non-blank: yes / no
     Emit per row: "V-NN Axis Cost Rationale: [present / missing -- rewrite required].
     V-NN Catalog Source: [populated / blank -- rewrite required]."
     Emit summary: "Column Schema Auditor Pass 2 complete. Population check:
     [PASS -- all rows populated / FAIL -- list blank rows]."

   INDEPENDENCE REQUIREMENT: Pass 1 and Pass 2 are structurally independent.
   A FAIL on Pass 1 does not suppress Pass 2. Both passes must appear.

5. Findings Synthesizer
   Responsibility: Execute Step 4. May not declare Step 4 item 3 complete until
   Column Schema Auditor has completed both passes AND Axis Cost Quality Gate emits PASS.

6. Axis Cost Quality Gate
   Responsibility: Runs after Column Schema Auditor completes both passes. Classifies
   each Axis Cost Rationale cell as STRUCTURAL or GENERIC.
   Emit per row: "V-NN Rationale Quality: STRUCTURAL [quoted] /
     GENERIC -- rewrite required [quoted]."
   Emit summary: "Axis Cost Quality Gate: PASS -- all rows structural /
     FAIL -- rows [list] contain generic rationale; rewrite required."
   Findings Synthesizer must not declare item 3 complete until this role emits PASS.

STEP 1 -- SELECT AXES

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} selected axes. Do not begin Step 2 until the list is committed.

STEP 2 -- VARIATION BODIES

For each selected axis, write one complete variation body.

VARIATION MAP -- Immutable after Phase 2 begins

champion-structural-keys: (read this row before writing any variation body -- the
AXIS-FREEZE PROTOCOL Step 2A checks each body against these keys before writing begins)
  Key 1: Consistency verdict: [CONSISTENT | AXIS DIVERGENCE] -- in Step 2B
  Key 2: Declared responsibility: -- in Phase 1, Phase 2, and Phase 3
  Key 3: failure-condition-outcome: -- in every hypothesis block
  Key 4: failure-condition-implementation: -- in every hypothesis block
  Required confirmations per body: 4. A body with fewer than 4 confirmed keys is
  structurally incomplete -- do not proceed to write that body.

Before Phase 1 begins, commit the axis assignment and per-variation per-criterion
directional predictions for each of the {N} planned variations.

| V | Assigned Axis | Criterion Target | C-01 Direction | C-04 Direction | C-07 Direction | Notes |
|---|--------------|-----------------|----------------|----------------|----------------|-------|
[Fill all {N} rows. Each direction cell: verdict + mechanism sentence.
Do not proceed to Phase 1 until all rows are filled.]

Do not revise this table after Phase 2 begins.
The AXIS-FREEZE PROTOCOL in Phase 2 reads axis assignments from this table.

PHASE 1 -- COMMIT VARIATION HEADERS
Declared responsibility: lock axis assignments by writing a complete variation header
for each planned variation -- every field populated, axis value must exactly match
the VARIATION MAP assignment for that row.

Header format (all fields required, none blank):

  variation: V-NN
  axis: [must match VARIATION MAP]
  pole: [specific change this variation makes]
  baseline-delta: [single structural element that changes]
  completeness-risk: [section most at risk of omission]
  criterion-target: [C-NN by ID]
  direction: [increases / decreases / stabilizes] [criterion] pass rates
  mechanism: [structural pathway -- necessity language required]
  failure-condition-outcome: [if criterion does not exceed prior baseline, mechanism refuted]
  failure-condition-implementation: [which C-NN independently violated if mechanism wrong]

Review all {N} headers. Verify every axis matches the VARIATION MAP. Commit.
Do not revise axis assignments after Phase 2 begins.

PHASE 2 -- GENERATE VARIATION BODIES
Declared responsibility: write each committed variation body in full under the
AXIS-FREEZE PROTOCOL -- committed axis is the only element that changes from the
baseline; every section written out; no placeholders; no cross-references to other
variations.

AXIS-FREEZE PROTOCOL (fires once per body, before writing begins):

  Step 1 -- Read: state the axis assigned in the VARIATION MAP for this body.

  Step 2 -- Write one freeze declaration for every axis:
    - role-sequence:       [FROZEN | COMMITTED -- read from VARIATION MAP]
    - output-format:       [FROZEN | COMMITTED -- read from VARIATION MAP]
    - lifecycle-emphasis:  [FROZEN | COMMITTED -- read from VARIATION MAP]
    - phrasing-register:   [FROZEN | COMMITTED -- read from VARIATION MAP]
    - inertia-framing:     [FROZEN | COMMITTED -- read from VARIATION MAP]
    - scoring-granularity: [FROZEN | COMMITTED -- read from VARIATION MAP]

  All six canonical axes must appear. Exactly one COMMITTED. Five FROZEN.
  A freeze list with fewer than six entries is incomplete -- do not proceed.

  Step 2A -- Structural key inheritance check (fires before Step 2B):
    Read the champion-structural-keys list from the VARIATION MAP.
    For each champion structural key, confirm the key will be present in this body:
      Key 1 (Consistency verdict: [CONSISTENT | AXIS DIVERGENCE] in Step 2B):
        [present -- this body includes Step 2B with bracket-notation verdict field |
         omitted -- required rewrite before proceeding]
      Key 2 (Declared responsibility: in Phase 1, Phase 2, Phase 3):
        [present -- all three phases carry Declared responsibility: labeled key |
         omitted -- required rewrite before proceeding]
      Key 3 (failure-condition-outcome: in hypothesis block):
        [present -- hypothesis block includes failure-condition-outcome: as separate key |
         omitted -- required rewrite before proceeding]
      Key 4 (failure-condition-implementation: in hypothesis block):
        [present -- hypothesis block includes failure-condition-implementation: as separate key |
         omitted -- required rewrite before proceeding]
    Confirmation count: [number] of 4 required keys confirmed.
    A confirmation count fewer than 4 is incomplete -- do not proceed to Step 2B until
    all 4 keys are confirmed present.

  Step 2B -- Cross-artifact axis consistency check (fires after Step 2A):
    - VARIATION MAP assigned axis for this V-NN: [read from VARIATION MAP]
    - Phase 1 header declared axis for this V-NN: [read from Phase 1 header]
    - Consistency verdict: [CONSISTENT | AXIS DIVERGENCE]
    - If AXIS DIVERGENCE: halt -- do not proceed until resolved.

  Step 3 -- Write the body. Change only the COMMITTED axis. Write every section
  in full.

Do not begin the next variation until the current body is complete.

PHASE 3 -- FINDINGS
Declared responsibility: confirm in-loop axis consistency (post-generation audit),
calibrate VARIATION MAP predictions against actual body structures, identify
combination candidates, rank evaluation order, designate anchor.

1. Axis alignment confirmation:
| V | Axis (VARIATION MAP) | Axis (Phase 1 header) | Step 2B Result | Post-Gen Match? |
|---|---------------------|----------------------|----------------|-----------------|

2. Prediction calibration:
| V | Axis | C-07 Predicted | C-07 in Body | Correct? | Mis-prediction Mechanism |
|---|------|----------------|-------------|----------|--------------------------|

3. Combination candidates:
| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness | Compound Effect | Criteria |
|----------|-----------|------------|------------------------|-------------------|-----------------|----------|

4. Evaluation order:
| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

5. Anchor: one variation. Justify structural impact, isolation quality, detectable
   failure condition -- one sentence each.

STEP 3 -- CROSS-ROUND DEPENDENCY CATALOG

| V | Axis | Comparative Claim (quoted) | Prior-Round Result Required | Round + Variation + Metric | Independent |
|---|------|----------------------------|-----------------------------|----------------------------|-------------|

STEP 4 -- FINDINGS

Complete the Column Contract before writing any table. Write "Column Contract complete.
Proceeding to findings." before any table.

1. Variation map:
| V | Axis | Change Made | Hypothesis Summary | C-04 Prediction | C-07 Prediction |
|---|------|-------------|-------------------|-----------------|-----------------|

2. Combination candidates: [compound-effects model, four sub-elements per pair]

[Column Schema Auditor Pass 1 emitted here -- after Step 3, before item 3.]

3. Evaluation order:
| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

[Column Schema Auditor Pass 2 emitted here.]
[Axis Cost Quality Gate emitted here.]

4. Compliance audit:

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

4a -- DECLARATION CHECK:
  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4a):
    EXECUTION DIRECTIVE: Advance to 4b regardless of this checkpoint's result.
  [ ] Column Contract block present: yes / no
  [ ] Axis Cost Rationale column named: yes / no
  [ ] Catalog Source column named: yes / no
  4a Declaration Check Result: PASS (all yes) / FAIL (name failing item)

4b -- POPULATION CHECK:
  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4b):
    EXECUTION DIRECTIVE: Execute this check. Do not suppress based on 4a result.
  (Executing 4b regardless of 4a result.)
  | V | Axis Cost Rationale Value | Catalog Source Value | Row Result |
  |---|--------------------------|---------------------|------------|
  4b Population Check Result: PASS (all rows populated) / FAIL (list incomplete rows)

Both passes must appear regardless of either pass result.
C-24 Pass: yes only if Declaration Check Result is PASS AND Population Check Result is PASS.

5. Anchor: one variation. Justify structural impact, isolation quality, detectable
   failure condition -- one sentence each.

---

## V-05 -- Combination: Output Format x Role Sequence (C-35 + C-37)

**axis:** output-format x role-sequence
**C-04 exception explicitly invoked**
**criterion-targeted:** C-35, C-37
**baseline-delta:** Combines V-01 R8 (STRUCTURAL KEY CONTRACT in preamble) with V-03 R8
(Structural Key Uniformity Auditor role). The preamble gains the STRUCTURAL KEY CONTRACT
section listing all four required structural keys including bracket-notation verdict declaration.
Role 3 becomes Structural Key Uniformity Auditor (existing roles 3-6 renumber to 4-7). The
STRUCTURAL KEY CONTRACT declares that the Structural Key Uniformity Auditor is the enforcement
mechanism for the contract's required-key list, linking the two artifacts. No other section,
step, or protocol changes.
**completeness-risk:** The link between the STRUCTURAL KEY CONTRACT and the Structural Key
Uniformity Auditor -- the contract must explicitly name the auditor as its enforcement mechanism;
if this link is absent the two artifacts are structurally independent and C-29's read-source
requirement applied to the contract-auditor link fails.

**combination-failure-condition:** if C-35 and C-37 pass rates do not jointly exceed
V-01 R8 alone (C-35 single-axis baseline) and V-03 R8 alone (C-37 single-axis baseline),
the STRUCTURAL KEY CONTRACT and Structural Key Uniformity Auditor provide no compound benefit
over independent single-axis results; redirect combination to output-format x phrasing-register
(V-01 R8 x V-02 R8) to test whether preamble contract + action-verb prohibition jointly
exceed either single-axis result in R9.

**hypothesis:**
- criterion-target: C-35 (bracket-notation) and C-37 (set-level structural key uniformity)
- direction: increases C-35 and C-37 pass rates beyond V-01 R8 and V-03 R8 individually;
  the compound effect is that the preamble STRUCTURAL KEY CONTRACT provides the declaration
  (C-35 bracket-notation listed as a required key) while the Structural Key Uniformity
  Auditor role provides the post-generation enforcement (scans all bodies for the bracket-
  notation key and blocks Step 3 on FAIL)
- mechanism: the STRUCTURAL KEY CONTRACT block lists the bracket-notation verdict field as
  a required structural key for every variation body -- this is the declaration phase; the
  Structural Key Uniformity Auditor scans all N bodies for this key after generation and
  blocks Step 3 on FAIL -- this is the enforcement phase; the two mechanisms are linked
  because the STRUCTURAL KEY CONTRACT explicitly names the Structural Key Uniformity Auditor
  as the enforcement mechanism for the contract's required-key list, making the declaration
  a required input to the audit and the audit a required completion gate for the declaration;
  neither artifact alone closes the loop between declaration and enforcement, but together
  they create a traceable protocol chain from required-key commitment to post-generation
  key-presence verification
- failure-condition-outcome:
    round-label:      R8
    source-variation: V-01
    criterion-born:   C-35
    evaluative-label:
      rank-label:       "single-axis baseline for C-35 in R8 -- STRUCTURAL KEY CONTRACT
                         preamble only, no post-generation scan"
      quality-dimension: "cleanest single-axis demonstration of C-35 enforcement via
                          preamble contract -- establishes the declaration mechanism in
                          isolation; the enforcement gap (no auditor role) is the residual
                          weakness this combination targets"
    consequence: if C-35 and C-37 pass rates do not jointly exceed V-01 R8 alone and
                 V-03 R8 alone, the compound declaration-plus-enforcement mechanism adds
                 no benefit over independent mechanisms; redirect combination to a single
                 execution-site co-location variant that places both the declaration and
                 the enforcement trigger at the same site (inside Phase 2 AXIS-FREEZE
                 PROTOCOL Step 2A) in R9
- failure-condition-implementation:
    round-label:      R8
    source-variation: V-03
    criterion-born:   C-37
    evaluative-label:
      rank-label:       "single-axis baseline for C-37 in R8 -- Structural Key Uniformity
                         Auditor role only, no preamble contract"
      quality-dimension: "cleanest single-axis demonstration of C-37 enforcement via
                          post-generation scan role -- establishes the enforcement mechanism
                          in isolation; the declaration gap (no preamble contract) is the
                          residual weakness this combination targets"
    consequence: if the STRUCTURAL KEY CONTRACT is present and the Structural Key Uniformity
                 Auditor role is present but the STRUCTURAL KEY CONTRACT does not explicitly
                 name the auditor role as its enforcement mechanism, the two artifacts are
                 structurally independent -- independently fails the C-29 read-source
                 declaration requirement applied to the contract-auditor link, because neither
                 artifact names the other as its authoritative source or enforcement gate

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

NON-SUPPRESSION INVARIANT CONTRACT

The compliance audit in this run contains two independent checkpoints (Declaration
Check and Population Check). This contract governs their execution behavior.

Invariant: Both checkpoints must emit their labeled results regardless of the
pass/fail state of either checkpoint. A FAIL result on the Declaration Check does
not suppress execution or result emission for the Population Check. A FAIL result
on the Population Check does not suppress the Declaration Check result.

Prohibited pattern -- SHORT-CIRCUIT SUPPRESSION: emitting only the Declaration
Check result when it fails, and omitting the Population Check output entirely.
Any audit section that exhibits short-circuit suppression is structurally incomplete.

NON-SUPPRESSION STRUCTURAL INCOMPLETENESS ASSERTION: An audit section that does not
explicitly state the non-suppression invariant is structurally incomplete and must
be rewritten before the step is declared complete.

Compliance: The audit section in Step 4 item 4 must include the following statement
before the checkpoints run:
  "NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
   regardless of each other's pass/fail state."

COLUMN CONTRACT

Before any evaluation order table is written in this run, declare all required
columns here. A table written without first completing this Column Contract is
structurally incomplete and must not be committed.

Required columns:
  [ ] Tier
  [ ] V
  [ ] Axis
  [ ] Evaluation Cost
  [ ] Axis Cost Rationale
  [ ] Independence
  [ ] Cross-Round Dependency
  [ ] Catalog Source

STRUCTURAL INCOMPLETENESS ASSERTION: A generator that writes any evaluation order
table in this run without first completing the Column Contract above (all boxes
checked, Axis Cost Rationale and Catalog Source columns explicitly declared)
produces structurally incomplete output. The table must not be committed until the
contract is complete.

EVALUATION ORDER TABLE SCHEMA

(Apply only after Column Contract is complete and all columns are checked above.)

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

Column definitions:
- "Tier": evaluation priority tier; Tier 1 = evaluate first.
- "V": variation label (V-01 through V-0N).
- "Axis": canonical axis name.
- "Evaluation Cost": low / medium / high with a one-line explanation.
- "Axis Cost Rationale": per-axis structural reason for this row's tier position. Must
  state: (a) structural property of this axis driving the cost level; (b) why this
  variation is independent or what prior-round result it requires.
- "Independence": yes / partial / no with a dependency note.
- "Cross-Round Dependency": Round + Variation + Metric, or "none."
- "Catalog Source": the specific Step 3 row from which this entry was derived.

REQUIRED: Every row must have a non-blank "Axis Cost Rationale" value containing
a per-axis structural reason.

STRUCTURAL KEY CONTRACT

Every variation body generated in this run must carry each of the following structural
keys. A variation body that omits any key listed below is structurally incomplete and
must be rewritten before advancing to the next variation.

Required structural keys -- every variation body must carry all of these:

  1. Consistency verdict: [CONSISTENT | AXIS DIVERGENCE] -- bracket-notation binary
     option declaration at the verdict token field definition site in Step 2B. The bracket
     form must appear at the declaration site. A Step 2B that emits the token without
     declaring both option values using bracket notation at the field definition site does
     not satisfy this key requirement.

  2. Declared responsibility: -- present as an explicitly labeled key immediately after
     the phase title in Phase 1, Phase 2, and Phase 3. All three phases must carry the key.

  3. failure-condition-outcome: -- present as a separately labeled key in every hypothesis
     block. Must not be collapsed into a single failure-condition: field.

  4. failure-condition-implementation: -- present as a separately labeled key in every
     hypothesis block, distinct from failure-condition-outcome:. Must name the criterion ID
     that the implementation failure would independently violate.

STRUCTURAL KEY CONTRACT INCOMPLETENESS ASSERTION: A variation body that does not carry
all four required structural keys above is structurally incomplete. Do not advance to the
next variation until all four keys are present in the current body.

ENFORCEMENT: The Structural Key Uniformity Auditor (role 3) is the enforcement mechanism
for this STRUCTURAL KEY CONTRACT. The Structural Key Uniformity Auditor reads the required-
key list from this contract and scans all N variation bodies against it after Step 2 is
complete. The Structural Key Uniformity Auditor must emit PASS before Step 3 may begin.
The STRUCTURAL KEY CONTRACT and the Structural Key Uniformity Auditor role form a protocol
chain: this contract is the authoritative required-key source; role 3 is the post-generation
verification gate. Neither is complete without the other.

ROLES

1. Axis Selector
   Responsibility: Execute Step 1. Select {N} distinct axes from the canonical list.
   Commit the axis list before Step 2 begins.

2. Variation Author
   Responsibility: Execute Step 2. For each selected axis, write one complete,
   standalone variation body with fully populated hypothesis block including
   failure-condition chain. Do not begin the next variation until the current
   body is complete. Before advancing, verify all four STRUCTURAL KEY CONTRACT
   keys are present in the completed body.

3. Structural Key Uniformity Auditor
   Responsibility: Runs after Step 2 is complete, before Step 3 begins. Reads the
   required-key list from the STRUCTURAL KEY CONTRACT. Scans all N variation bodies
   for each required key. Emits per-key uniformity results. Step 3 must not begin
   until this role emits PASS.

   Required structural keys (read from STRUCTURAL KEY CONTRACT above):
     Key 1: Consistency verdict: [CONSISTENT | AXIS DIVERGENCE] in Step 2B
     Key 2: Declared responsibility: in Phase 1, Phase 2, and Phase 3
     Key 3: failure-condition-outcome: in every hypothesis block
     Key 4: failure-condition-implementation: in every hypothesis block

   Emit for each required key:
     "Key [key name]: present in [list V-NN] / Missing from [list V-NN]."

   Emit summary:
     "Structural Key Uniformity Audit: PASS -- all required keys present uniformly." or
     "Structural Key Uniformity Audit: FAIL -- [list keys] missing in [list V-NN].
      Required rewrite before Step 3 may begin."

   Step 3 must not begin until this role emits PASS.

4. Dependency Cataloger
   Responsibility: Execute Step 3. Produce the cross-round dependency catalog.
   All four columns must be non-blank in every row. Step 4 must not begin until
   this catalog is complete.

5. Column Schema Auditor
   Responsibility: Two independent verification passes.

   PASS 1 -- DECLARATION CHECK (runs after Step 3, before Step 4 item 3):
     Verify:
       [ ] Column Contract block present in output: yes / no
       [ ] "Axis Cost Rationale" column explicitly named in contract: yes / no
       [ ] "Catalog Source" column explicitly named in contract: yes / no
     Emit: "Column Schema Auditor Pass 1 complete. Declaration check: [PASS /
     FAIL -- name failing item]."

   PASS 2 -- POPULATION CHECK (runs after Step 4 item 3):
     For each variation in the evaluation order table, verify:
       [ ] Axis Cost Rationale value non-blank with per-axis reason: yes / no
       [ ] Catalog Source value non-blank: yes / no
     Emit per row: "V-NN Axis Cost Rationale: [present / missing -- rewrite required].
     V-NN Catalog Source: [populated / blank -- rewrite required]."
     Emit summary: "Column Schema Auditor Pass 2 complete. Population check:
     [PASS -- all rows populated / FAIL -- list blank rows]."

   INDEPENDENCE REQUIREMENT: Pass 1 and Pass 2 are structurally independent.
   A FAIL on Pass 1 does not suppress Pass 2. Both passes must appear.

6. Findings Synthesizer
   Responsibility: Execute Step 4. May not declare Step 4 item 3 complete until
   Column Schema Auditor has completed both passes AND Axis Cost Quality Gate emits PASS.

7. Axis Cost Quality Gate
   Responsibility: Runs after Column Schema Auditor completes both passes. Classifies
   each Axis Cost Rationale cell as STRUCTURAL or GENERIC.
   Emit per row: "V-NN Rationale Quality: STRUCTURAL [quoted] /
     GENERIC -- rewrite required [quoted]."
   Emit summary: "Axis Cost Quality Gate: PASS -- all rows structural /
     FAIL -- rows [list] contain generic rationale; rewrite required."
   Findings Synthesizer must not declare item 3 complete until this role emits PASS.

STEP 1 -- SELECT AXES

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} selected axes. Do not begin Step 2 until the list is committed.

STEP 2 -- VARIATION BODIES

For each selected axis, write one complete variation body.

VARIATION MAP -- Immutable after Phase 2 begins

Before Phase 1 begins, commit the axis assignment and per-variation per-criterion
directional predictions for each of the {N} planned variations.

| V | Assigned Axis | Criterion Target | C-01 Direction | C-04 Direction | C-07 Direction | Notes |
|---|--------------|-----------------|----------------|----------------|----------------|-------|
[Fill all {N} rows. Each direction cell: verdict + mechanism sentence.
Do not proceed to Phase 1 until all rows are filled.]

Do not revise this table after Phase 2 begins.
The AXIS-FREEZE PROTOCOL in Phase 2 reads axis assignments from this table.

PHASE 1 -- COMMIT VARIATION HEADERS
Declared responsibility: lock axis assignments by writing a complete variation header
for each planned variation -- every field populated, axis value must exactly match
the VARIATION MAP assignment for that row.

Header format (all fields required, none blank):

  variation: V-NN
  axis: [must match VARIATION MAP]
  pole: [specific change this variation makes]
  baseline-delta: [single structural element that changes]
  completeness-risk: [section most at risk of omission]
  criterion-target: [C-NN by ID]
  direction: [increases / decreases / stabilizes] [criterion] pass rates
  mechanism: [structural pathway -- necessity language required]
  failure-condition-outcome: [if criterion does not exceed prior baseline, mechanism refuted]
  failure-condition-implementation: [which C-NN independently violated if mechanism wrong]

Review all {N} headers. Verify every axis matches the VARIATION MAP. Commit.
Do not revise axis assignments after Phase 2 begins.

PHASE 2 -- GENERATE VARIATION BODIES
Declared responsibility: write each committed variation body in full under the
AXIS-FREEZE PROTOCOL -- committed axis is the only element that changes from the
baseline; every section written out; no placeholders; no cross-references to other
variations.

AXIS-FREEZE PROTOCOL (fires once per body, before writing begins):

  Step 1 -- Read: state the axis assigned in the VARIATION MAP for this body.

  Step 2 -- Write one freeze declaration for every axis:
    - role-sequence:       [FROZEN | COMMITTED -- read from VARIATION MAP]
    - output-format:       [FROZEN | COMMITTED -- read from VARIATION MAP]
    - lifecycle-emphasis:  [FROZEN | COMMITTED -- read from VARIATION MAP]
    - phrasing-register:   [FROZEN | COMMITTED -- read from VARIATION MAP]
    - inertia-framing:     [FROZEN | COMMITTED -- read from VARIATION MAP]
    - scoring-granularity: [FROZEN | COMMITTED -- read from VARIATION MAP]

  All six canonical axes must appear. Exactly one COMMITTED. Five FROZEN.
  A freeze list with fewer than six entries is incomplete -- do not proceed.

  Step 2B -- Cross-artifact axis consistency check (fires before Step 3):
    - VARIATION MAP assigned axis for this V-NN: [read from VARIATION MAP]
    - Phase 1 header declared axis for this V-NN: [read from Phase 1 header]
    - Consistency verdict: [CONSISTENT | AXIS DIVERGENCE]
    - If AXIS DIVERGENCE: halt -- do not proceed until resolved.

  Step 3 -- Write the body. Change only the COMMITTED axis. Write every section
  in full. Before advancing to next body, verify all four STRUCTURAL KEY CONTRACT
  keys are present.

After all {N} bodies are complete, role 3 (Structural Key Uniformity Auditor) reads
the required-key list from the STRUCTURAL KEY CONTRACT and scans all bodies. Step 3
must not begin until the Structural Key Uniformity Auditor emits PASS.

PHASE 3 -- FINDINGS
Declared responsibility: confirm in-loop axis consistency (post-generation audit),
calibrate VARIATION MAP predictions against actual body structures, identify
combination candidates, rank evaluation order, designate anchor.

1. Axis alignment confirmation:
| V | Axis (VARIATION MAP) | Axis (Phase 1 header) | Step 2B Result | Post-Gen Match? |
|---|---------------------|----------------------|----------------|-----------------|

2. Prediction calibration:
| V | Axis | C-07 Predicted | C-07 in Body | Correct? | Mis-prediction Mechanism |
|---|------|----------------|-------------|----------|--------------------------|

3. Combination candidates:
| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness | Compound Effect | Criteria |
|----------|-----------|------------|------------------------|-------------------|-----------------|----------|

4. Evaluation order:
| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

5. Anchor: one variation. Justify structural impact, isolation quality, detectable
   failure condition -- one sentence each.

STEP 3 -- CROSS-ROUND DEPENDENCY CATALOG

| V | Axis | Comparative Claim (quoted) | Prior-Round Result Required | Round + Variation + Metric | Independent |
|---|------|----------------------------|-----------------------------|----------------------------|-------------|

STEP 4 -- FINDINGS

Complete the Column Contract before writing any table. Write "Column Contract complete.
Proceeding to findings." before any table.

1. Variation map:
| V | Axis | Change Made | Hypothesis Summary | C-04 Prediction | C-07 Prediction |
|---|------|-------------|-------------------|-----------------|-----------------|

2. Combination candidates: [compound-effects model, four sub-elements per pair]

[Column Schema Auditor Pass 1 emitted here -- after Step 3, before item 3.]

3. Evaluation order:
| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

[Column Schema Auditor Pass 2 emitted here.]
[Axis Cost Quality Gate emitted here.]

4. Compliance audit:

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

4a -- DECLARATION CHECK:
  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4a):
    EXECUTION DIRECTIVE: Advance to 4b regardless of this checkpoint's result.
  [ ] Column Contract block present: yes / no
  [ ] Axis Cost Rationale column named: yes / no
  [ ] Catalog Source column named: yes / no
  4a Declaration Check Result: PASS (all yes) / FAIL (name failing item)

4b -- POPULATION CHECK:
  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4b):
    EXECUTION DIRECTIVE: Execute this check. Do not suppress based on 4a result.
  (Executing 4b regardless of 4a result.)
  | V | Axis Cost Rationale Value | Catalog Source Value | Row Result |
  |---|--------------------------|---------------------|------------|
  4b Population Check Result: PASS (all rows populated) / FAIL (list incomplete rows)

Both passes must appear regardless of either pass result.
C-24 Pass: yes only if Declaration Check Result is PASS AND Population Check Result is PASS.

5. Anchor: one variation. Justify structural impact, isolation quality, detectable
   failure condition -- one sentence each.

---

## Step 3 -- Cross-Round Dependency Catalog

| V | Axis | Comparative Claim (quoted) | Prior-Round Result Required | Round + Variation + Metric | Independent |
|---|------|----------------------------|-----------------------------|----------------------------|-------------|
| V-01 | output-format | "C-35 and C-37 pass rates do not improve beyond R7 V-01 (C-35 partial for V-01 only, C-37 not satisfied as a set)" | R7 V-01 C-35 partial pass result (bracket-notation present in V-01 body, absent from V-02 and V-03) | R7 / V-01 / C-35 partial pass | no -- depends on R7/V-01/C-35 partial pass |
| V-02 | phrasing-register | "C-36 pass rate does not improve beyond R7 V-01 partial result (action-verb content present but not enforced as structural constraint)" | R7 V-01 C-36 partial pass result (action-verb labels present without prohibition) | R7 / V-01 / C-36 partial pass | no -- depends on R7/V-01/C-36 partial pass |
| V-03 | role-sequence | "C-37 pass rate does not improve beyond zero (C-37 not targeted in any prior round)" | R7 V-02 C-37 failure result (Declared responsibility: dropout confirmed) | R7 / V-02 / C-37 fail | no -- depends on R7/V-02/C-37 fail (requires confirmed failure evidence) |
| V-04 | inertia-framing | "C-37 pass rate does not improve beyond zero via champion-structural-keys row" | R7 V-03 inertia-framing result (champion-baseline field body-local, no key enumeration) | R7 / V-03 / C-37 fail | no -- depends on R7/V-03/C-37 fail |
| V-05 | output-format x role-sequence | "C-35 and C-37 pass rates do not jointly exceed V-01 R8 alone (C-35 single-axis baseline) and V-03 R8 alone (C-37 single-axis baseline)" | V-01 R8 C-35 result AND V-03 R8 C-37 result | R8 / V-01 / C-35 pass rate AND R8 / V-03 / C-37 pass rate | no -- depends on R8/V-01/C-35 and R8/V-03/C-37 |

---

## Step 4 -- Findings

### 4.1 Variation Map

Column Contract complete. Proceeding to findings.

| V | Axis | Change Made | Hypothesis Summary | C-04 Prediction | C-07 Prediction |
|---|------|-------------|-------------------|-----------------|-----------------|
| V-01 | output-format | STRUCTURAL KEY CONTRACT section added to preamble with 4 required keys and structural-incompleteness blocking assertion | Preamble contract forces generators to commit to required structural keys before Phase 1; C-35 (bracket-notation) and C-37 (uniform propagation) are both named in the required-key list | no-change: preamble contract change is confined to pre-generation section; does not cross into hypothesis or phase structure | no-change: preamble contract does not alter hypothesis quality or falsifiability requirements |
| V-02 | phrasing-register | PROHIBITION added to Phase 1, Phase 2, Phase 3 Declared responsibility: key definitions; title-echo and generic-label content declared a required rewrite | Prohibition forces action-verb content grounded in protocol mechanism name; C-36 (content grounded in protocol action verb) is directly enforced as a point-of-production constraint | risk-low: prohibition is confined to Declared responsibility: key content; the committed change does not touch hypothesis structure, AXIS-FREEZE PROTOCOL, or VARIATION MAP | no-change: responsibility label content prohibition does not alter hypothesis falsifiability or mechanism quality |
| V-03 | role-sequence | Structural Key Uniformity Auditor inserted as role 3; scans all N bodies after Step 2; blocks Step 3 on FAIL | Post-generation set-level scan makes C-37 failure detectable as a named gate result before findings begin; blocking directive converts detection to enforcement | no-change: auditor role fires after generation, not during; does not affect per-body axis isolation | no-change: auditor role does not alter hypothesis quality |
| V-04 | inertia-framing | champion-structural-keys row added to VARIATION MAP; Step 2A added to AXIS-FREEZE PROTOCOL for per-body key inheritance check with 4-confirmation count gate | Per-body pre-write check against champion key list makes structural key inheritance explicit and count-verifiable before each body is written | risk-medium: champion-structural-keys reference names prior-round variation, which could tempt generator to adopt additional champion structure; confined to key names only | no-change: champion key reference does not alter hypothesis quality |
| V-05 | output-format x role-sequence | STRUCTURAL KEY CONTRACT (from V-01 R8) + Structural Key Uniformity Auditor role (from V-03 R8) combined; contract declares auditor as enforcement mechanism; C-04 exception invoked | Declaration-level contract + post-generation scan role create a traceable protocol chain; compound effect closes the loop between required-key commitment and post-generation verification | risk-high: two structural additions (preamble section + role); both touch document architecture; combination exception invoked per C-04 | no-change: combination does not alter hypothesis quality |

### 4.2 Combination Candidates

**V-01 R8 x V-02 R8: output-format x phrasing-register (Priority: HIGH)**
- Failure modes: V-01 targets C-35 failure (bracket-notation absent at declaration site); V-02 targets C-36 failure (generic label content in Declared responsibility:)
- Residual weakness after V-01 only: STRUCTURAL KEY CONTRACT declares bracket-notation as required, but no prohibition of title-echo in responsibility label content; C-36 can still fail even with the contract present
- Compound criterion effect (both active): C-35 and C-36 are simultaneously enforced -- the contract lists bracket-notation as required and the prohibition enforces action-verb label content; both C-35 and C-36 become point-of-production constraints rather than post-production judgments; no single-axis body targets both simultaneously
- Priority rationale: C-35 and C-36 are both new in v8 and both apply to every variation body; a compound pass would demonstrate that two v8 criteria can be simultaneously enforced at the preamble and phase-header levels without structural interference

**V-03 R8 x V-04 R8: role-sequence x inertia-framing (Priority: MEDIUM)**
- Failure modes: V-03 targets C-37 failure via post-generation scan (detects key regression after it occurs); V-04 targets C-37 failure via per-body pre-write check (prevents key regression before it occurs)
- Residual weakness after V-03 only: Structural Key Uniformity Auditor detects regression after all bodies are written -- a FAIL still requires rewriting bodies; the detection is after-the-fact
- Compound criterion effect (both active): C-37 is enforced at two points -- per-body pre-write (Step 2A champion key check) and post-generation scan (role 3 audit); together they create a prevention + detection protocol for structural key uniformity; no single-axis body targets C-37 at both stages simultaneously
- Priority rationale: lower than V-01xV-02 because both axes target the same criterion (C-37) via different mechanisms rather than two different criteria; the compound effect is defense-in-depth rather than criterion coverage expansion

**Axis tension note (pre-combination):** V-01 (output-format) and V-02 (phrasing-register) can interfere if the STRUCTURAL KEY CONTRACT section and the Declared responsibility: prohibition both modify the preamble/phase-header regions -- if combined carelessly, the prohibition text in each phase header may be interpreted as part of the key contract rather than a separate instruction. In a combination pass, the STRUCTURAL KEY CONTRACT must be placed in the preamble only; the prohibition must remain attached to each Declared responsibility: key definition in each phase header. The phrasing-register prohibition is the dominant variable in this combination: if the prohibition is correctly positioned at the phase-header level, the preamble contract placement has no ambiguity.

### 4.3 Evaluation Order

Column Schema Auditor Pass 1 complete. Declaration check: PASS -- Column Contract block
present, Axis Cost Rationale column named, Catalog Source column named.

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |
|------|---|------|-----------------|---------------------|--------------|----------------------|----------------|
| 1 | V-01 | output-format | low -- preamble addition only; no protocol or role changes; evaluation requires checking for STRUCTURAL KEY CONTRACT section presence and structural-incompleteness assertion completeness | output-format axis changes are confined to document structure (preamble section addition); no interaction with hypothesis blocks or phase mechanics; the only contamination risk is whether the blocking directive is present in the assertion -- a binary check; independent of all other R8 variations | yes | none | Step 3 row V-01: independent |
| 1 | V-02 | phrasing-register | low -- prohibition text addition to three phase headers only; no protocol or role changes; evaluation requires checking prohibition presence and testing whether a near-synonym of the phase title would trigger the rewrite rule | phrasing-register axis changes are confined to Declared responsibility: key content definition at each phase header; the prohibition is self-contained and does not interact with AXIS-FREEZE PROTOCOL or hypothesis structure; independent of all other R8 variations | yes | none | Step 3 row V-02: independent |
| 1 | V-03 | role-sequence | medium -- new role with a post-generation scan and blocking directive; evaluation requires running all N bodies through the role and verifying the FAIL result correctly blocks Step 3 | role-sequence axis changes affect the execution sequence (new role 3 fires between Step 2 and Step 3); evaluation cost is medium because the auditor role requires reading all N variation bodies to scan for required keys -- not a single-artifact check; independent of V-01 and V-02 (the auditor scans for keys whose presence is influenced by V-01 and V-02 but the scan mechanism itself is independent) | yes | none | Step 3 row V-03: independent |
| 1 | V-04 | inertia-framing | medium -- champion-structural-keys row addition to VARIATION MAP plus Step 2A addition to AXIS-FREEZE PROTOCOL; evaluation requires tracing Step 2A execution per body and verifying the 4-confirmation count gate fires correctly | inertia-framing axis changes affect both the VARIATION MAP (new row) and AXIS-FREEZE PROTOCOL (new Step 2A); evaluation cost is medium because both artifacts must be verified -- the champion-structural-keys row must list all 4 keys and Step 2A must confirm all 4 per body; independent of V-01 through V-03 | yes | none | Step 3 row V-04: independent |
| 2 | V-05 | output-format x role-sequence | high -- combination of two structural additions plus the protocol chain link between STRUCTURAL KEY CONTRACT and Structural Key Uniformity Auditor; evaluation requires verifying both artifacts are present, the link declaration is explicit, and the auditor reads from the contract | combination axis changes require evaluating three artifacts: the STRUCTURAL KEY CONTRACT, the Structural Key Uniformity Auditor role, and the ENFORCEMENT link between them; the compound protocol chain is the primary evaluation target and requires that neither artifact can be declared complete independently; depends on R8 V-01 (C-35 single-axis baseline) and R8 V-03 (C-37 single-axis baseline) being evaluated first | no -- depends on R8/V-01/C-35 and R8/V-03/C-37 | R8 / V-01 / C-35 pass rate AND R8 / V-03 / C-37 pass rate | Step 3 row V-05: depends on R8/V-01/C-35 and R8/V-03/C-37 |

Column Schema Auditor Pass 2 complete. Population check: PASS -- all rows populated
with per-axis structural reasons and non-blank Catalog Source values.

Axis Cost Quality Gate:
V-01 Rationale Quality: STRUCTURAL ["output-format axis changes are confined to document
  structure (preamble section addition); the only contamination risk is whether the blocking
  directive is present -- a binary check"]
V-02 Rationale Quality: STRUCTURAL ["phrasing-register axis changes are confined to Declared
  responsibility: key content definition at each phase header; the prohibition does not interact
  with AXIS-FREEZE PROTOCOL or hypothesis structure"]
V-03 Rationale Quality: STRUCTURAL ["evaluation cost is medium because the auditor role requires
  reading all N variation bodies to scan for required keys -- not a single-artifact check"]
V-04 Rationale Quality: STRUCTURAL ["evaluation cost is medium because both VARIATION MAP
  (champion-structural-keys row) and AXIS-FREEZE PROTOCOL (Step 2A) must be verified"]
V-05 Rationale Quality: STRUCTURAL ["compound protocol chain requires evaluating three artifacts:
  the STRUCTURAL KEY CONTRACT, the Structural Key Uniformity Auditor role, and the ENFORCEMENT
  link between them; neither artifact can be declared complete independently"]
Axis Cost Quality Gate: PASS -- all rows structural.

### 4.4 Compliance Audit

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

4a -- DECLARATION CHECK:
  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4a):
    EXECUTION DIRECTIVE: Advance to 4b regardless of this checkpoint's result.
  [ ] Column Contract block present: yes
  [ ] Axis Cost Rationale column explicitly named in contract: yes
  [ ] Catalog Source column explicitly named in contract: yes
  4a Declaration Check Result: PASS -- all items yes.

4b -- POPULATION CHECK:
  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4b):
    EXECUTION DIRECTIVE: Execute this check. Do not suppress based on 4a result.
  (Executing 4b regardless of 4a result.)

  | V | Axis Cost Rationale Value | Catalog Source Value | Row Result |
  |---|--------------------------|---------------------|------------|
  | V-01 | "output-format axis changes are confined to document structure (preamble section addition); the only contamination risk is whether the blocking directive is present -- a binary check" | Step 3 row V-01: independent | populated |
  | V-02 | "phrasing-register axis changes are confined to Declared responsibility: key content definition at each phase header; does not interact with AXIS-FREEZE PROTOCOL or hypothesis structure" | Step 3 row V-02: independent | populated |
  | V-03 | "evaluation cost is medium because the auditor role requires reading all N variation bodies to scan for required keys -- not a single-artifact check" | Step 3 row V-03: independent | populated |
  | V-04 | "evaluation cost is medium because both VARIATION MAP and AXIS-FREEZE PROTOCOL must be verified" | Step 3 row V-04: independent | populated |
  | V-05 | "compound protocol chain requires evaluating three artifacts; neither artifact can be declared complete independently" | Step 3 row V-05: depends on R8/V-01/C-35 and R8/V-03/C-37 | populated |

  4b Population Check Result: PASS -- all rows populated.

Both passes emitted. C-24 Pass: yes (4a PASS and 4b PASS).

### 4.5 Anchor

**Anchor: V-03 (role-sequence: Structural Key Uniformity Auditor)**

- Structural impact: inserts a post-generation set-level scan role that is the only mechanism
  in this set capable of detecting C-37 failures across all N bodies simultaneously, converting
  a scorecard-only check into a protocol gate before findings begin.
- Isolation quality: role-sequence axis change is confined to the role sequence and the
  Step 2 completion boundary; no interaction with hypothesis structure, VARIATION MAP,
  or AXIS-FREEZE PROTOCOL content.
- Detectable failure condition: if the Structural Key Uniformity Auditor emits FAIL for
  a key that regressed (e.g., failure-condition-outcome: absent in V-02 body), the failure
  condition is directly observable as a named key absence in a specific variation body --
  the mechanism (auditor fires, FAIL emitted, Step 3 blocked) is falsifiable by the absence
  of the blocking directive in the role instruction.
