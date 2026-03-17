# quest-rubric Variate — Round 14 (Against rubric v14, targeting C-43/C-44)
**Date:** 2026-03-15
**Rubric:** v14 (C-01--C-44; denominator /36; adds C-43: emit-phase criterion-to-artifact evaluability map; C-44: evaluability declaration includes named exclusion guarantee)
**Target criteria:** C-43, C-44

**Round 14 design note:** Round 13 produced excellence signal ES-R13-1 from V-04 and V-05. V-04 passed C-43 (criterion→artifact map present in emit phase) but failed C-44 (no named exclusion in independence guarantee). V-05 passed both C-43 and C-44. Rubric v14 elevates both to aspirational criteria, extending the denominator from /34 to /36. R14 targets: (1) confirm C-43 mechanism is isolatable without C-44; (2) test whether C-44 can be achieved by a lifecycle gate alone without a terminal table; (3) test whether inertia framing (competitor before Phase 9) drives C-43 via prose form or requires a formal table; (4) combine all mechanisms; (5) add role-gate enforcement to the combined stack.

**C-43 vs C-44 -- distinction summary for variation design:**

- C-43 governs the *emit phase terminal position*: Phase 9 must close with a per-criterion evaluability declaration mapping each structural criterion to (a) its named verification artifact and (b) its scan method. An emit that has these facts somewhere in the document but not as a terminal section of Phase 9 does not satisfy C-43; the requirement is both the content and the position.

- C-44 governs the *independence falsifiability* of each declaration: each row in the evaluability map must include an explicit independence guarantee that names the specific instruction content excluded from the verification path. "Independently verifiable" without naming the excluded content is a non-falsifiable claim and fails C-44; "independently verifiable without reading role instruction bodies" names the excluded content and satisfies C-44.

---

## Axis Selection

| Axis | Criterion targeted | Mechanism |
|------|-------------------|-----------|
| Output format | C-43 | Phase 9 closes with a named CRITERION EVALUABILITY MAP table: C-NN \| Verification Artifact \| Scan Method. No Independence column. |
| Lifecycle emphasis | C-43 partial / C-44 strong | Phase 8.5 EVALUABILITY GATE: before Phase 9, each criterion must declare its verification artifact, scan method, AND named excluded content. Phase 9 emit manifest references gate output as terminal section. |
| Inertia framing | C-43 partial | EVALUABILITY COMPETITOR block before Phase 9 names the rubric-without-evaluability-map; Phase 9 closes with prose evaluability notes per criterion (no formal table). |
| (combined) | C-43 + C-44 | Phase 8.5 gate + terminal CRITERION EVALUABILITY MAP with Independence column (named excluded content). Inertia competitor present. |
| Role sequence | C-43 + C-44 | ROLE: EVALUABILITY AUDITOR between Phase 8 and Phase 9; exit gate EVALUABILITY GATE; Phase 9 opens with PREREQUISITE quoting gate identifier verbatim. |

Single-axis: V-01 (output format), V-02 (lifecycle emphasis), V-03 (inertia framing).
Combined: V-04 (three single axes), V-05 (three single axes + role sequence).

---

## Round 14 Variation Map

| Variation | Axis | C-43 probe | C-44 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Output format | Very strong -- CRITERION EVALUABILITY MAP as named terminal section of Phase 9; columns: C-NN, Verification Artifact, Scan Method; every structural criterion required to have a row | Ablated -- no Independence column, no exclusion content required | Single-axis; isolates whether named terminal table with artifact+scan columns alone satisfies C-43 without exclusion naming |
| V-02 | Lifecycle emphasis | Partial -- Phase 8.5 EVALUABILITY GATE produces declarations before Phase 9; Phase 9 emit manifest includes gate output as last section via reference; Phase 9 does not independently produce the terminal section at close | Strong -- Phase 8.5 gate requires named excluded content in Independence field for each criterion; content reproduced in Phase 9 | Single-axis; tests whether Phase 8.5 gate + Phase 9 reference (vs Phase 9 terminal production) is sufficient for C-43; and whether Phase 8.5 gate alone drives C-44 |
| V-03 | Inertia framing | Partial -- EVALUABILITY COMPETITOR before Phase 9 names the gap; Phase 9 closes with prose evaluability notes per criterion; prose form may not satisfy the "named verification artifact" + "scan method" structural requirement of C-43 | Ablated -- no exclusion naming in prose notes | Single-axis; hypothesis: inertia framing alone does not satisfy C-43 because prose notes lack named field-level artifact + scan method separation; confirms formal table is the load-bearing mechanism |
| V-04 | Output format + Lifecycle emphasis + Inertia framing | Very strong -- Phase 8.5 gate required; Phase 9 closes with CRITERION EVALUABILITY MAP table with all four columns including Independence | Very strong -- Phase 8.5 gate requires named excluded content; reproduced in Phase 9 terminal table Independence column | Combined; tests whether C-43+C-44 can simultaneously pass on top of three-gate stack (C-40+C-41+C-42) |
| V-05 | Output format + Lifecycle emphasis + Inertia framing + Role sequence | Very strong (same as V-04) | Very strong (same as V-04) | V-04 mechanisms + ROLE: EVALUABILITY AUDITOR; tests whether role-gate enforcement changes C-43/C-44 satisfaction vs V-04's phase-gate approach |

---

## V-01 -- Output Format

**Axis:** Output format -- Phase 9 closes with a required terminal section titled CRITERION EVALUABILITY MAP. The section is a table with three columns: C-NN | Verification Artifact | Scan Method. Every structural criterion must have a row. A Phase 9 output that ends after vN Candidates without this table is incomplete. C-44 is ablated: no Independence column, no exclusion naming required.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-01 will contain a CRITERION EVALUABILITY MAP section as the final section of the document, after vN Candidates, with one row per structural criterion naming the specific verification artifact (a named field or section in the emitted rubric) and the scan method (the specific check an evaluator performs) -- any output where the rubric ends with vN Candidates or where the evaluability section is present but lists criteria without separate named-artifact and scan-method columns falsifies the C-43 hypothesis; the falsification signal is any terminal section that describes evaluability in prose without column separation of artifact and method. | Naming the terminal section as a formal requirement in Phase 9 -- rather than describing evaluability as a property of individual criteria in Phase 3-6 -- makes criterion-to-artifact mapping a document-structure obligation rather than a criterion-drafting preference; outputs from V-01 will show this mapping as a standalone final section rather than embedded in criterion Notes fields; if outputs produced from V-03 (inertia framing, prose notes) embed evaluability information in criterion body text while V-01 outputs produce a separate terminal section, the Phase 9 terminal section instruction is the load-bearing mechanism for the distinct structural placement C-43 requires. | V-03 is the primary ablation control: V-03 has inertia framing that names the rubric-without-evaluability-map as a gap and requires Phase 9 to close with evaluability notes, but in prose form rather than a formal table; comparing C-43 scores across V-01 (formal terminal table) and V-03 (prose terminal notes) isolates whether the table format -- specifically the column separation of named artifact and scan method -- is required for C-43 or whether any terminal evaluability section satisfies it. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Read the skill spec. For every way an output of this skill can fail, record:

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. **Do not begin ROLE: CRITERION DEFINER
until the failure log contains at least 5 entries.**

---

### ROLE: CRITERION DEFINER

**This role runs after Phase 1. Do not write any criterion fields during this role.**

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates (Text template + Pass template),
no additional content.**

Generate skill-specific templates from the skill spec.

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence]
  X = [rejected form]
```

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form -- in
any phrasing -- is any Text that locates causality in the wrong form's consequence. The
Auditor check function tests causal structure, not pattern matching.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

**DEFINER OUTPUT GATE is satisfied when:** Both templates above are produced in slot-fillable
form. Nothing else. No explanatory commentary, structural rationale, context notes, or
template-adjacent content is permitted. A CRITERION DEFINER output containing any content
other than the two slot-fillable templates is incomplete.

STOP CONDITION -- ROLE: CRITERION DEFINER: If the output of this role contains anything
beyond the two required templates, the DEFINER OUTPUT GATE is not satisfied. Rewrite before
proceeding. The two templates are the complete and exclusive output of this role.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

If introducing a competitor: **place the competitor block immediately before this criterion.**

Each criterion: C-NN, Text (template applied), Weight: essential, Category, Pass (template
applied). No bare qualitative observables.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: **place the competitor block immediately before the criterion.**

Each criterion: same five fields. Annotation: **Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

Isolation audit for each criterion from Phases 3 and 4.

Text field checks: (1) Direction, (2) Contrast, (3) Causal chain.
Pass field checks: (4) Location, (5) Observable, (6) No qualitative-only.

**Audit report format:**

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:

Essential coverage:
  [C-NN guards against: one-line description per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property already listed above at a higher threshold
  is not aspirational. Tighter is not new territory.

Gap zone:
  Gap G-01: [Property not covered by E+R, not reachable by threshold adjustment.
    Observable: what would an evaluator check to confirm presence or absence?]
```

**Do not proceed to ROLE: MECHANISM DEFINER until the gap zone contains at least G-01.**

---

### ROLE: MECHANISM DEFINER

**This role runs after Phase 5. Do not write any aspirational criteria during this role.**

**Exit gate: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated and
all rows showing "Yes -- affects C-NN only," AND PHASE-LOCALITY RULE stated.**

#### Step 1 -- Independence Map

Read all criteria produced so far. Produce the Independence Map.

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

Column requirements:
- **"Criterion affected (C-NN)"**: cite the specific criterion number. A generic assertion
  without criterion number is a format violation.
- **"Independent?"**: confirm removing this mechanism causes exactly one criterion to fail.

STOP CONDITION: Do not satisfy the MECHANISM DEFINER GATE until every row shows "Yes --
affects C-NN only."

#### Step 2 -- PHASE-LOCALITY RULE

Before the MECHANISM DEFINER GATE is satisfied, state the following rule.

**PHASE-LOCALITY RULE: Named competitors may not be placed in:**

1. Preamble or introductory framing that precedes any construction phase -- a competitor
   introduced before any criterion-construction step begins is not phase-local regardless
   of how precisely it names the wrong implementation.
2. An operating-principles section, shared instructional block, or role-level preamble
   that precedes more than one construction step -- a competitor in a shared block applying
   to multiple criteria is not at any single construction step.
3. A combined competitor block that introduces or governs more than one criterion
   simultaneously -- one competitor block per criterion; "this competitor covers C-NN and
   C-MM" is not phase-local for either criterion.

Each named competitor must appear inline at the specific construction step where the wrong
implementation would most naturally be produced. Violation of any prohibited zone is a
STOP condition for ROLE: BUILDER ASPIRATIONAL.

**Both Step 1 and Step 2 must be complete before the MECHANISM DEFINER GATE is satisfied.**

**MECHANISM DEFINER GATE is satisfied when:** Independence Map complete with specific C-NN
citation in every row, all rows "Yes -- affects C-NN only," AND PHASE-LOCALITY RULE stated.

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN:
| Tier         | Category distribution              | Majority category    |
|--------------|-------------------------------------|----------------------|
| Essential    | [cat: N, cat: N, ...]               | [majority or "tied"] |
| Recommended  | [cat: N, ...]                       | [majority or "tied"] |
| Aspirational | [To be filled after ROLE: BUILDER]  | [To be filled]       |

Distinct majority categories (essential + recommended only):
  [List unique majority values]

STOP if essential and recommended majority categories are identical AND aspirational is
unlikely to diverge.
Scan status: [COMPLIANT / BLOCKED]
```

**Do not begin ROLE: BUILDER ASPIRATIONAL until scan status shows COMPLIANT.**

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**
**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated
and all rows showing "Yes -- affects C-NN only," and PHASE-LOCALITY RULE stated.**

This role's entry is gated on both ROLE identifiers above. If either gate has not been
satisfied, this role cannot begin.

Write 1-2 aspirational criteria targeting the gap zone from Phase 5. Each criterion must
fall in the gap zone and correspond to a mechanism in the Independence Map.

For each criterion, introduce its competitor immediately before the criterion definition,
subject to the PHASE-LOCALITY RULE:

```
COMPETITOR: [Name the specific wrong implementation. Describe with specificity sufficient
for a reader to identify any instantiation without reading the required mechanism below.]

From the description above, derive the required function before reading the positive
definition below.

REQUIRED MECHANISM: [State the mechanism that closes the gap.]
```

Then write the five-field criterion. Notes: "closes gap via [mechanism name] per independence
map | DEFINER OUTPUT GATE: Two slot-fillable templates | MECHANISM DEFINER GATE: Independence
Map | PHASE-LOCALITY RULE: applied | competitor: [first four words]."

STOP conditions:
- An aspirational criterion whose Notes field lacks all three gate/rule identifiers: rewrite.
- COMPETITOR block ending with failure description rather than derivation instruction: rewrite.
- Competitor placed in any PHASE-LOCALITY RULE prohibited zone: move before proceeding.

---

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

```
COMPETITOR PLACEMENT + COVERAGE AUDIT:

STEP A -- Phase-local placement audit:
  Competitor [name]: introduced at [Phase/Role N] | gap operationally relevant at [N] |
  phase-local? [Y/N] | PHASE-LOCALITY RULE zone violated? [zone 1/2/3 / None]
  STOP if any competitor fails either column.
  Step A status: [COMPLIANT / BLOCKED]

STEP B -- Coverage completeness audit:
  Novel aspirational criteria: [list by ID and G-NN]
  Count: [N]
  Competitors: [list each and criterion governed]
  Count: [N]
  STOP if counts differ.
  Step B status: [COMPLIANT / BLOCKED]

STEP C -- Tier-divergence re-run:
  [Three-tier table with aspirational row populated]
  Distinct majority categories: [N]
  STOP if < 2.
  Final scan status: [COMPLIANT / BLOCKED]
```

**Do not write the Scoring section until all three status fields show COMPLIANT.**

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1-2). Compliant? [YES / NO]
Check B: distinct categories [N] (requirement >= 3). Compliant? [YES / NO]
```

**Do not proceed to Phase 8 until both checks show YES.**

---

### PHASE 8 -- SCORING

```
THREE-STATE SCORING TABLE:
| State   | Score value | Earn condition (observable anchor required) |
|---------|-------------|---------------------------------------------|
| PASS    | 1.0         | [observable anchor]                         |
| PARTIAL | 0.5         | [observable anchor]                         |
| FAIL    | 0.0         | [observable anchor]                         |
```

Every criterion must have all three states named. A scoring section naming PASS and FAIL
without PARTIAL is incomplete.

---

### PHASE 9 -- EMIT

Output the complete rubric document with sections in this order:

1. **Failure Mode Log** -- all F-NN entries from Phase 1
2. **Design Rationale** -- dominant failure mode, self-application, >= 3 rejected generic
   criteria with reasons; must appear before the first criteria table
3. **Essential Criteria** -- all five fields per criterion
4. **Recommended Criteria** -- all five fields per criterion
5. **Independence Map** -- the MECHANISM DEFINER Step 1 output; format: Mechanism | What it
   does | C-NN | Independent?
6. **PHASE-LOCALITY RULE** -- the MECHANISM DEFINER Step 2 output, published as a named
   section before Aspirational Criteria; all three prohibited zones enumerated verbatim
7. **Aspirational Criteria** -- COMPETITOR blocks inline immediately before each criterion;
   Notes cites all three gate/rule identifiers
8. **Scoring** -- composite formula, golden threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifier list
10. **vN Candidates** -- patterns approaching promotion; evidence needed per candidate

**After vN Candidates, close the document with this section:**

```
CRITERION EVALUABILITY MAP:
| C-NN | Verification Artifact | Scan Method |
|------|-----------------------|-------------|
| C-01 | [the named field or section in this rubric document where evidence of C-01 appears] | [the specific check: count this token / confirm this structure / verify this property is present] |
| ...  | ...                   | ...         |
```

Every structural criterion must appear as a row. A CRITERION EVALUABILITY MAP row with a
blank Verification Artifact cell or a Scan Method cell containing only "see Pass field"
is incomplete -- name the specific document location and the specific check separately.

STOP CONDITION -- Phase 9: The emit is incomplete until the CRITERION EVALUABILITY MAP
section is present as the final section of the document, after vN Candidates, with one
populated row for every structural criterion. Do not mark Phase 9 complete if any row
is blank or the section is absent.

---

## V-02 -- Lifecycle Emphasis

**Axis:** Lifecycle emphasis -- a Phase 8.5 EVALUABILITY GATE runs after Phase 8 and before
Phase 9. The gate requires each structural criterion to have three fields populated: (a)
Verification Artifact, (b) Scan Method, (c) Independence (named excluded content). Phase 9
is blocked until all rows in the gate are complete. Phase 9's emit manifest references the
gate output as the terminal section ("include the Phase 8.5 EVALUABILITY GATE output as
the final section of the emitted document"). Phase 9 itself does not independently produce
a terminal section -- it references. C-43 is partial; C-44 is strong.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-02 will contain an evaluability section as the final section of the document because Phase 9 instructs "include Phase 8.5 EVALUABILITY GATE output as the final section" -- but the section will have been produced at Phase 8.5, not at Phase 9 close; the C-43 partial prediction is that a rubric evaluator can find the criterion-to-artifact map but may not classify it as "emit phase closes with" if the emit phase merely references rather than produces the terminal section; the falsification signal is rubric output where the final section is absent despite the Phase 9 reference instruction. | The Phase 8.5 gate requires naming excluded content (Independence field) before Phase 9 begins, so the excluded content appears in the gate output and is reproduced in the final section; this is the C-44 strong hypothesis: outputs from V-02 will show named excluded content in the evaluability section because the gate blocks Phase 9 until the Independence field is populated, not because Phase 9 instructs it directly; if V-01 outputs (no lifecycle gate, no Independence column) fail C-44 while V-02 outputs pass C-44, the Phase 8.5 gate is the operative mechanism for C-44, not the Phase 9 terminal section instruction. | V-01 is the primary C-44 ablation control; V-04 adds the terminal section production instruction from V-01 on top of V-02's lifecycle gate to test whether the combination achieves both C-43 PASS and C-44 PASS simultaneously. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Read the skill spec. For every way an output of this skill can fail, record:

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. **Do not begin ROLE: CRITERION DEFINER
until the failure log contains at least 5 entries.**

---

### ROLE: CRITERION DEFINER

**This role runs after Phase 1. Do not write any criterion fields during this role.**

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates (Text template + Pass template),
no additional content.**

Generate skill-specific templates from the skill spec.

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence]
  X = [rejected form]
```

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form -- in
any phrasing -- is any Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

**DEFINER OUTPUT GATE is satisfied when:** Both templates above are produced in slot-fillable
form. Nothing else. A CRITERION DEFINER output containing any content other than the two
slot-fillable templates is incomplete.

STOP CONDITION -- ROLE: CRITERION DEFINER: Rewrite if output contains anything beyond the
two required templates. The two templates are the complete and exclusive output of this role.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER. Competitor blocks immediately before their criterion. No bare qualitative
observables. Five fields per criterion: C-NN, Text, Weight: essential, Category, Pass.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.
Same five fields. Annotation: **Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:

Essential coverage: [C-NN guards against: ...]
Recommended coverage: [C-NN guards the [dimension] of [property].]
Threshold escalation prohibition: tighter is not new territory.
Gap zone:
  Gap G-01: [Property not in E+R, not reachable by threshold adjustment. Observable.]
```

**Do not proceed to ROLE: MECHANISM DEFINER until the gap zone contains at least G-01.**

---

### ROLE: MECHANISM DEFINER

**This role runs after Phase 5. Do not write any aspirational criteria during this role.**

**Exit gate: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated and
all rows showing "Yes -- affects C-NN only," AND PHASE-LOCALITY RULE stated.**

#### Step 1 -- Independence Map

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

STOP: Any row showing "No -- overlaps" requires redesign before proceeding.

#### Step 2 -- PHASE-LOCALITY RULE

**PHASE-LOCALITY RULE: Named competitors may not be placed in:**

1. Preamble or introductory framing that precedes any construction phase.
2. A shared instructional block or role-level preamble that precedes more than one
   construction step.
3. A combined competitor block that introduces or governs more than one criterion.

Violation of any zone is a STOP condition for ROLE: BUILDER ASPIRATIONAL.

**MECHANISM DEFINER GATE is satisfied when:** Independence Map complete, all rows "Yes --
affects C-NN only," AND PHASE-LOCALITY RULE stated above.

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN:
| Tier         | Category distribution   | Majority category    |
|--------------|-------------------------|----------------------|
| Essential    | [cat: N, ...]           | [majority or "tied"] |
| Recommended  | [cat: N, ...]           | [majority or "tied"] |
| Aspirational | [after ROLE: BUILDER]   | [To be filled]       |

Distinct majority categories (E+R): [list]
STOP if identical and aspirational unlikely to diverge.
Scan status: [COMPLIANT / BLOCKED]
```

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**
**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated
and all rows showing "Yes -- affects C-NN only," and PHASE-LOCALITY RULE stated.**

Write 1-2 aspirational criteria targeting the gap zone. Competitor block inline before each
criterion, subject to PHASE-LOCALITY RULE. Then five-field criterion.

Notes: "closes gap via [mechanism name] per independence map | DEFINER OUTPUT GATE: Two
slot-fillable templates | MECHANISM DEFINER GATE: Independence Map | PHASE-LOCALITY RULE:
applied | competitor: [first four words]."

STOP: Missing gate/rule identifiers in Notes → rewrite. Competitor in prohibited zone → move.

---

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

```
STEP A: phase-local? [Y/N] | PHASE-LOCALITY RULE zone violated? [None / zone N]
  Step A status: [COMPLIANT / BLOCKED]
STEP B: novel aspirational count [N] = competitor count [N]?
  Step B status: [COMPLIANT / BLOCKED]
STEP C: distinct majority categories (all tiers) >= 2?
  Final scan status: [COMPLIANT / BLOCKED]
```

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1-2). Compliant? [YES / NO]
Check B: distinct categories [N] (requirement >= 3). Compliant? [YES / NO]
```

---

### PHASE 8 -- SCORING

```
THREE-STATE SCORING TABLE:
| State   | Score value | Earn condition (observable anchor required) |
|---------|-------------|---------------------------------------------|
| PASS    | 1.0         | [observable anchor]                         |
| PARTIAL | 0.5         | [observable anchor]                         |
| FAIL    | 0.0         | [observable anchor]                         |
```

---

### PHASE 8.5 -- EVALUABILITY GATE

Complete this block before writing any Phase 9 output. Phase 9 is blocked until all rows
are populated.

```
EVALUABILITY GATE:
| C-NN | Verification Artifact | Scan Method | Independence |
|------|-----------------------|-------------|--------------|
| C-01 | [the specific named section or field in the emitted rubric document where evidence of this criterion appears -- not "see Pass field" but the actual section title or field name] | [the specific check an evaluator performs: scan for token X / count Y / confirm structure Z] | [Yes -- independently verifiable without reading [name the specific excluded content, e.g., "role instruction bodies" or "Phase 5 gap zone text"]] |
| ...  | ...                   | ...         | ...          |
```

Column requirements:
- **Verification Artifact**: name the specific document section or field, not a paraphrase
  of the criterion. "Design Rationale section" is acceptable; "the section about rationale"
  is not.
- **Scan Method**: name the specific check. "Scan for 'Not [X], but [Y]' pattern in Text
  field" is acceptable; "check that criterion is correctly written" is not.
- **Independence**: must name the excluded content. "Yes -- independently verifiable" without
  naming what is excluded is incomplete. "Yes -- without reading role instruction bodies" is
  the required form.

STOP CONDITION -- Phase 8.5: Phase 9 is blocked until every row in the EVALUABILITY GATE
has all three cells populated in the required form. A gate with blank cells or generic
Independence claims is incomplete.

---

### PHASE 9 -- EMIT

Output the complete rubric document with sections in this order:

1. **Failure Mode Log**
2. **Design Rationale** -- before first criteria table; self-application; >= 3 rejected
   generic criteria
3. **Essential Criteria**
4. **Recommended Criteria**
5. **Independence Map**
6. **PHASE-LOCALITY RULE** -- published as named section; all three prohibited zones verbatim
7. **Aspirational Criteria** -- COMPETITOR blocks inline; Notes cites all gate/rule identifiers
8. **Scoring** -- composite formula, threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
10. **vN Candidates**
11. **Criterion Evaluability Map** -- reproduce the Phase 8.5 EVALUABILITY GATE output
    verbatim as the final section of this document

STOP CONDITION -- Phase 9: The emit is incomplete if section 11 is absent or if the
reproduced EVALUABILITY GATE has any unpopulated row.

---

## V-03 -- Inertia Framing

**Axis:** Inertia framing -- before Phase 9, a named EVALUABILITY COMPETITOR block describes
the rubric-without-evaluability-map and makes its gap specific. Phase 9 then closes with a
required EVALUABILITY NOTES section, but the section is prose (one sentence per criterion)
rather than a formal table. No Phase 8.5 gate. C-43 is partial (declarations present, but
prose form may not satisfy "named verification artifact" + "scan method" as distinct labeled
columns); C-44 is ablated.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-03 will contain an EVALUABILITY NOTES section at the end of the document because Phase 9 requires it -- but the notes will be in prose form ("C-01 is verifiable by scanning the Essential Criteria section for the 'Not [X], but [Y]' pattern") rather than as a table with Verification Artifact and Scan Method as labeled column headers; the C-43 partial prediction is that prose declarations may name the artifact and method but do not satisfy the "named verification artifact" + "scan method" structural separation that a formal table enforces, making the declarations unambiguous to a rubric evaluator reading the Aspirational Criteria section independent of Phase 9 construction instructions. | Placing an EVALUABILITY COMPETITOR block before Phase 9 -- naming the gap as "a rubric whose Phase 9 ends with vN Candidates, leaving the evaluator to infer verification paths" -- activates the inertia framing mechanism for C-11 independent of C-43/C-44; if V-03 outputs show higher C-11 scores than V-01 and V-02 outputs (which have no competitor before Phase 9), the EVALUABILITY COMPETITOR block is confirmed as the C-11 operative mechanism; the C-43/C-44 partial score from V-03 then isolates whether inertia framing alone -- without formal table structure -- can satisfy C-43. | V-01 is the primary C-43 control for V-03: V-01 has a formal table with labeled columns and no competitor block; comparing C-43 scores across V-01 (table, no competitor) and V-03 (competitor, prose) isolates whether the table format or the inertia framing is the C-43 operative mechanism; prediction: V-01 passes C-43 and V-03 partially passes or fails, confirming table structure as load-bearing. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### PHASE 1 -- FAILURE MODE ANALYSIS

```
F-NN | failure behavior | structural gap | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. Do not begin ROLE: CRITERION DEFINER
until 5 entries are present.

---

### ROLE: CRITERION DEFINER

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates (Text template + Pass template),
no additional content.**

**Text template:**
```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property]
  Z = [downstream failure consequence]
  X = [rejected form]
```

Causal direction rule: "Without Y, Z fails." Prohibited: causality located in wrong form's
consequence. Auditor tests causal structure, not pattern matching.

**Pass template:**
```
LOCATION: [artifact field or section]
OBSERVABLE: [specific token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

**DEFINER OUTPUT GATE satisfied when:** Both templates in slot-fillable form. Nothing else.
Rewrite if output contains anything beyond the two templates.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE.**

Five fields per criterion: C-NN, Text (template applied), Weight: essential, Category, Pass
(template applied). Competitor immediately before criterion. No bare qualitative observables.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE.**

Same five fields. Dimension annotation. Pass tests degree, precision, or specificity.

---

### PHASE 4.5 -- POST-DRAFT AUDIT

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite flagged criteria before proceeding.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:
Essential coverage: [C-NN guards against: ...]
Recommended coverage: [C-NN guards the [dimension] of [property].]
Gap zone:
  Gap G-01: [Property not in E+R, not reachable by threshold adjustment. Observable.]
```

---

### ROLE: MECHANISM DEFINER

**Exit gate: MECHANISM DEFINER GATE: Independence Map complete, all rows "Yes -- affects
C-NN only," AND PHASE-LOCALITY RULE stated.**

Step 1 -- Independence Map:
```
| Mechanism name | What it does | Criterion affected (C-NN) | Independent? |
```

Step 2 -- PHASE-LOCALITY RULE:

**Named competitors may not be placed in:** (1) preamble preceding any phase; (2) shared
block preceding more than one step; (3) combined block governing more than one criterion.
Violation is a STOP condition.

**MECHANISM DEFINER GATE satisfied when:** Independence Map complete + PHASE-LOCALITY RULE
stated.

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN: [three rows: Essential / Recommended / Aspirational]
Distinct majority categories (E+R): [list]. Scan status: [COMPLIANT / BLOCKED]
```

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE.**
**PREREQUISITE: MECHANISM DEFINER GATE.**

1-2 aspirational criteria. Competitor block inline before each criterion (subject to
PHASE-LOCALITY RULE). Notes: "closes gap via [mechanism] | DEFINER OUTPUT GATE: Two
slot-fillable templates | MECHANISM DEFINER GATE: Independence Map | PHASE-LOCALITY RULE:
applied | competitor: [first four words]."

---

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

STEP A: phase-local + zone check. STEP B: counts match. STEP C: >= 2 distinct majorities.
All three COMPLIANT before Scoring.

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1-2). Compliant? [YES / NO]
Check B: distinct categories [N] (>= 3). Compliant? [YES / NO]
```

---

### PHASE 8 -- SCORING

```
THREE-STATE SCORING TABLE:
| State | Score value | Earn condition (observable anchor required) |
```

---

### EVALUABILITY COMPETITOR

Before writing Phase 9, name the specific implementation that has the surface form of a
complete rubric but leaves the evaluability path unspecified:

```
EVALUABILITY COMPETITOR: A rubric whose Phase 9 emit manifest ends with vN Candidates as
the final section. The rubric has a complete Pass field for every criterion, and each Pass
field names a location, observable, and standard. An evaluator reading the rubric can
therefore find the required observable -- but to verify a specific criterion, they must
read the criterion's Pass field, then navigate to the named location, then apply the scan
method. The three steps are not stated anywhere as a unified mapping; they must be
reconstructed per criterion. The rubric appears evaluable because Pass fields exist; the
gap is the absence of a criterion-level declaration that names the full verification path
as a single statement an evaluator can scan without re-reading criterion fields.

From this description, derive what Phase 9 must add before reading the required approach
below.

REQUIRED APPROACH: Phase 9 closes with an EVALUABILITY NOTES section that provides, for
each structural criterion, a one-sentence declaration of the verification path.
```

---

### PHASE 9 -- EMIT

Output the complete rubric document with sections in this order:

1. **Failure Mode Log**
2. **Design Rationale**
3. **Essential Criteria**
4. **Recommended Criteria**
5. **Independence Map**
6. **PHASE-LOCALITY RULE**
7. **Aspirational Criteria**
8. **Scoring**
9. **Notes**
10. **vN Candidates**
11. **Evaluability Notes** -- one sentence per structural criterion in the form:
    "C-NN is verifiable by [description of what to scan and where]."
    Every structural criterion must have an entry. An entry of the form "C-NN is verifiable;
    see Pass field" is incomplete -- the sentence must state the scan description inline.

STOP CONDITION -- Phase 9: Emit is incomplete if section 11 is absent or if any entry in
Evaluability Notes defers to another section rather than stating the verification path inline.

---

## V-04 -- Output Format + Lifecycle Emphasis + Inertia Framing

**Axis:** Combined -- three-gate stack from R14 V-04 baseline plus C-43/C-44 mechanisms:
(1) Phase 8.5 EVALUABILITY GATE with Verification Artifact + Scan Method + Independence
columns (C-44 target via lifecycle gate); (2) Phase 9 terminal CRITERION EVALUABILITY MAP
table reproducing the gate output with all four columns (C-43 target via terminal table);
(3) EVALUABILITY COMPETITOR block before Phase 9 naming the rubric-without-evaluability-map
(inertia framing for C-11). All three single-axis mechanisms combined; C-43 and C-44
simultaneously targeted.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-04 will contain: (a) a Phase 8.5 EVALUABILITY GATE with all four columns populated including Independence with named excluded content; AND (b) a CRITERION EVALUABILITY MAP as the final section of the emitted document with the same four columns reproduced verbatim; AND (c) an EVALUABILITY COMPETITOR block embedded before the Phase 9 emit instructions -- any output lacking the terminal four-column table, or containing a terminal table without an Independence column, or containing an Independence column that does not name specific excluded content, falsifies the corresponding C-43 or C-44 sub-hypothesis independently. | The Phase 8.5 gate forces the model to populate Independence fields before Phase 9 begins, removing the option to emit the terminal table without exclusion naming; rubrics produced from V-04 will show named excluded content in the terminal table's Independence column because the gate blocked Phase 9 until the field was populated, not because Phase 9's terminal section instruction specified exclusion naming; if V-02 (Phase 8.5 gate, no terminal table) achieves C-44 PASS while V-01 (terminal table, no gate) achieves C-44 FAIL, V-04's Phase 8.5 gate is confirmed as the C-44 load-bearing mechanism even when the terminal table also carries the field. | V-01 and V-02 are the ablation controls: V-01 has terminal table without gate (expected: C-43 PASS, C-44 FAIL); V-02 has gate without terminal production instruction (expected: C-43 PARTIAL, C-44 PASS); V-04 combines both (expected: C-43 PASS + C-44 PASS). If V-04 fails C-43 while V-02 fails C-43, the terminal production instruction (V-01) is confirmed as load-bearing for C-43 position. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### PHASE 1 -- FAILURE MODE ANALYSIS

```
F-NN | failure behavior | structural gap | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking, 2 suboptimal. Do not begin ROLE: CRITERION DEFINER until 5 entries.

---

### ROLE: CRITERION DEFINER

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates (Text template + Pass template),
no additional content.**

**Text template:**
```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property]   Z = [downstream failure consequence]   X = [rejected form]
```
Causal direction rule: "Without Y, Z fails." Prohibited: causality in wrong form's consequence.

**Pass template:**
```
LOCATION: [artifact field or section]
OBSERVABLE: [specific token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

**DEFINER OUTPUT GATE satisfied when:** Both templates in slot-fillable form. Nothing else.
Rewrite if output contains anything beyond the two templates.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Apply Text and Pass templates. Competitor immediately before criterion. Five fields: C-NN,
Text, Weight: essential, Category, Pass. No bare qualitative observables.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Same five fields. Dimension annotation required.

---

### PHASE 4.5 -- POST-DRAFT AUDIT

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite flagged criteria.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:
Essential coverage: [C-NN guards against: ...]
Recommended coverage: [C-NN guards the [dimension] of [property].]
Threshold escalation prohibition: tighter is not new territory.
Gap zone:
  Gap G-01: [Property not in E+R, not reachable by threshold adjustment. Observable.]
```

**Do not proceed to ROLE: MECHANISM DEFINER until gap zone has at least G-01.**

---

### ROLE: MECHANISM DEFINER

**Exit gate: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated and
all rows showing "Yes -- affects C-NN only," AND PHASE-LOCALITY RULE stated.**

#### Step 1 -- Independence Map

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
```

STOP: Any row showing "No -- overlaps" requires redesign.

#### Step 2 -- PHASE-LOCALITY RULE

**Named competitors may not be placed in:** (1) preamble preceding any phase; (2) shared
block preceding more than one construction step; (3) combined block governing more than one
criterion. Violation is a STOP condition for ROLE: BUILDER ASPIRATIONAL.

**MECHANISM DEFINER GATE satisfied when:** Independence Map complete + PHASE-LOCALITY RULE
stated.

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN: [Essential / Recommended / Aspirational rows]
Distinct majority categories (E+R): [list]. Scan status: [COMPLIANT / BLOCKED]
```

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**
**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map complete + PHASE-LOCALITY RULE
stated.**

1-2 aspirational criteria. Competitor inline before each criterion (PHASE-LOCALITY RULE
applies). Notes: "closes gap via [mechanism] | DEFINER OUTPUT GATE: Two slot-fillable
templates | MECHANISM DEFINER GATE: Independence Map | PHASE-LOCALITY RULE: applied |
competitor: [first four words]."

STOP: Missing gate/rule identifiers → rewrite. Competitor in prohibited zone → move.

---

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

STEP A: phase-local + zone check. STEP B: counts match. STEP C: >= 2 distinct majorities.
All three COMPLIANT before Scoring.

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
Check A: aspirational count [N] (bound 1-2). Compliant? [YES / NO]
Check B: distinct categories [N] (>= 3). Compliant? [YES / NO]
```

---

### PHASE 8 -- SCORING

```
THREE-STATE SCORING TABLE:
| State   | Score value | Earn condition (observable anchor required) |
|---------|-------------|---------------------------------------------|
| PASS    | 1.0         |                                             |
| PARTIAL | 0.5         |                                             |
| FAIL    | 0.0         |                                             |
```

---

### PHASE 8.5 -- EVALUABILITY GATE

Complete before Phase 9. Phase 9 is blocked until all rows are populated.

```
EVALUABILITY GATE:
| C-NN | Verification Artifact | Scan Method | Independence |
|------|-----------------------|-------------|--------------|
| C-01 | [named section or field in emitted rubric document] | [specific check: scan for X / count Y / confirm structure Z] | Yes -- independently verifiable without reading [name the excluded content] |
| ...  | ...                   | ...         | ...          |
```

Column requirements:
- **Verification Artifact**: name the specific document section or field. "Essential Criteria
  section" is acceptable; "see Pass field" is not -- name the section, not a pointer.
- **Scan Method**: name the specific check. Generic checks ("verify criterion is satisfied")
  are not acceptable.
- **Independence**: state "Yes -- independently verifiable without reading [excluded content]"
  where [excluded content] is the specific instruction section, role body, or construction
  record excluded from the verification path. "Independently verifiable" without naming the
  excluded content fails this column.

STOP CONDITION: Phase 9 is blocked until every row has all three cells populated in the
required form above.

---

### EVALUABILITY COMPETITOR

```
EVALUABILITY COMPETITOR: A rubric whose emit manifest ends with vN Candidates as the final
section. Each criterion has a complete Pass field (Location, Observable, Standard). A reader
can verify any criterion by finding the Pass field and checking the named observable. The
rubric appears fully evaluable. The gap: the Pass field tells the reader what to check but
not whether checking it requires reading the construction record (role instructions, phase
outputs) or only the emitted document. An evaluator who needs to know whether they can verify
C-NN without reading the role bodies must check the criterion definition, the Pass field, the
Independence Map, and the Notes field to reconstruct the independence boundary. No single
document section states "C-NN is verifiable by checking [X] in [section], without reading
[Y]" as a unified claim.

From this description, derive what the emitted document must add before reading the required
mechanism below.

REQUIRED MECHANISM: A CRITERION EVALUABILITY MAP as the terminal section of the emitted
document, with one row per structural criterion mapping C-NN to (a) Verification Artifact,
(b) Scan Method, and (c) Independence guarantee naming the excluded content. The map makes
the criterion-to-verification-path mapping available as a standalone terminal section
readable without returning to criterion fields.
```

---

### PHASE 9 -- EMIT

Output the complete rubric document with sections in this order:

1. **Failure Mode Log**
2. **Design Rationale** -- self-application; >= 3 rejected generic criteria; EVALUABILITY
   COMPETITOR block embedded in this section to name the prior-state gap the terminal
   CRITERION EVALUABILITY MAP closes
3. **Essential Criteria**
4. **Recommended Criteria**
5. **Independence Map** -- MECHANISM DEFINER Step 1 output
6. **PHASE-LOCALITY RULE** -- MECHANISM DEFINER Step 2 output; all three zones verbatim
7. **Aspirational Criteria** -- COMPETITOR blocks inline; Notes cites all gate/rule identifiers
8. **Scoring** -- composite formula, threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
10. **vN Candidates**
11. **Criterion Evaluability Map** -- reproduce the Phase 8.5 EVALUABILITY GATE output
    verbatim as the final section; all four columns (C-NN, Verification Artifact, Scan
    Method, Independence) must be present for every structural criterion

STOP CONDITION -- Phase 9: Emit is incomplete until section 11 is present as the final
section with all four columns populated for every structural criterion. A terminal section
missing the Independence column, or with Independence cells stating "independently verifiable"
without naming excluded content, is incomplete. Do not mark Phase 9 complete until the
CRITERION EVALUABILITY MAP passes all column requirements from Phase 8.5.

An evaluator reading only the Criterion Evaluability Map section must be able to answer
three questions for every structural criterion: (a) which section of the rubric document
holds the evidence, (b) what specific property to scan for, (c) what instruction content
they are not required to read -- all three answers readable from the map section alone,
independently, without reading role instruction bodies.

---

## V-05 -- Output Format + Lifecycle Emphasis + Inertia Framing + Role Sequence

**Axis:** Same three-mechanism combined stack as V-04 plus a named role enforcement layer:
ROLE: EVALUABILITY AUDITOR runs between Phase 8 and Phase 8.5. The AUDITOR must produce the
EVALUABILITY GATE output and satisfy the EVALUABILITY GATE identifier before Phase 9 opens.
Phase 9 opens with a PREREQUISITE quoting the EVALUABILITY GATE identifier verbatim. This
tests whether role-gate enforcement for the evaluability declaration (as opposed to V-04's
phase-gate enforcement) changes C-43/C-44 satisfaction -- and whether the EVALUABILITY GATE
identifier appearing in Phase 9's PREREQUISITE creates independent auditability of the
evaluability path from Phase 9 alone, parallel to how C-41's MECHANISM DEFINER GATE is
independently auditable from ROLE: BUILDER ASPIRATIONAL's header.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-05 will contain a ROLE: EVALUABILITY AUDITOR section producing the EVALUABILITY GATE output, and Phase 9 will open with a PREREQUISITE line quoting "EVALUABILITY GATE: Criterion Evaluability Map with all C-NN rows populated including Independence column with named excluded content" verbatim -- any output where Phase 9 opens without this PREREQUISITE line, or where the EVALUABILITY GATE output exists but is not quoted in Phase 9's entry condition, falsifies the role-gate auditability hypothesis; the falsification signal is Phase 9 that begins with its emit manifest without a PREREQUISITE naming the gate identifier. | Adding a ROLE: EVALUABILITY AUDITOR with a named exit gate and quoting that gate identifier in Phase 9's PREREQUISITE creates the same independently auditable sequencing property for the evaluability path that C-41 creates for the aspirational construction path; rubrics produced from V-05 will show Phase 9 entry conditions that a reader can verify from the Phase 9 header alone -- without reading ROLE: EVALUABILITY AUDITOR instructions -- in the same way that ROLE: BUILDER ASPIRATIONAL's PREREQUISITE is independently auditable without reading ROLE: MECHANISM DEFINER; this property is the V-05 contribution above V-04's equivalent content. | V-04 is the primary isolation control: V-04 has Phase 8.5 phase-gate (not role-gate) + terminal table; comparing C-43/C-44 scores across V-04 and V-05 isolates whether the role-gate enforcement layer adds measurable scoring value; if V-04 achieves C-43 PASS + C-44 PASS and V-05 achieves identical scores, role-gate enforcement is confirmed as redundant to phase-gate enforcement for C-43/C-44; if V-05 scores higher, the named role adds evaluation-path auditability beyond what a phase-gate achieves. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### PHASE 1 -- FAILURE MODE ANALYSIS

```
F-NN | failure behavior | structural gap | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking, 2 suboptimal. Do not begin ROLE: CRITERION DEFINER until 5 entries.

---

### ROLE: CRITERION DEFINER

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates (Text template + Pass template),
no additional content.**

**Text template:**
```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property]
  Z = [downstream failure consequence]
  X = [rejected form]
```
Causal direction: "Without Y, Z fails." Prohibited: causality in wrong form's consequence.

**Pass template:**
```
LOCATION: [artifact field or section]
OBSERVABLE: [specific token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

**DEFINER OUTPUT GATE satisfied when:** Both templates in slot-fillable form. Nothing else.
Rewrite if output exceeds the two templates.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Five fields per criterion. Templates applied. Competitor inline before criterion. No bare
qualitative observables.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Same five fields. Dimension annotation. Pass tests degree, precision, or specificity.

---

### PHASE 4.5 -- POST-DRAFT AUDIT

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite flagged criteria.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:
Essential coverage: [C-NN guards against: ...]
Recommended coverage: [C-NN guards the [dimension] of [property].]
Gap zone:
  Gap G-01: [Property not in E+R. Observable.]
```

---

### ROLE: MECHANISM DEFINER

**Exit gate: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated and
all rows showing "Yes -- affects C-NN only," AND PHASE-LOCALITY RULE stated.**

Step 1 -- Independence Map:
```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
```

Step 2 -- PHASE-LOCALITY RULE: Named competitors may not be placed in (1) preamble preceding
any phase; (2) shared block preceding more than one step; (3) combined block governing more
than one criterion. Violation is a STOP condition.

**MECHANISM DEFINER GATE satisfied when:** Independence Map complete + PHASE-LOCALITY RULE
stated.

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN: [three rows] Scan status: [COMPLIANT / BLOCKED]
```

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**
**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map complete + PHASE-LOCALITY RULE
stated.**

1-2 aspirational criteria. Competitor inline before each (PHASE-LOCALITY RULE applies).
Notes: "closes gap via [mechanism] | DEFINER OUTPUT GATE: Two slot-fillable templates |
MECHANISM DEFINER GATE: Independence Map | PHASE-LOCALITY RULE: applied | competitor:
[first four words]."

---

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

STEP A: phase-local + zone check. STEP B: counts match. STEP C: >= 2 distinct majorities.

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
Check A: aspirational count (bound 1-2). Compliant? [YES / NO]
Check B: distinct categories (>= 3). Compliant? [YES / NO]
```

---

### PHASE 8 -- SCORING

```
THREE-STATE SCORING TABLE: [PASS / PARTIAL / FAIL with observable anchors]
```

---

### ROLE: EVALUABILITY AUDITOR

**This role runs after Phase 8. Do not begin Phase 9 until this role's exit gate is
satisfied.**

**Exit gate: EVALUABILITY GATE: Criterion Evaluability Map with all C-NN rows populated,
Verification Artifact and Scan Method named for every structural criterion, and Independence
field naming excluded content for every row.**

Read all structural criteria produced in Phases 3, 4, and ROLE: BUILDER ASPIRATIONAL. For
each criterion, produce:

```
EVALUABILITY GATE -- Criterion Evaluability Map:
| C-NN | Verification Artifact | Scan Method | Independence |
|------|-----------------------|-------------|--------------|
| C-01 | [named section or field in emitted rubric] | [specific check] | Yes -- independently verifiable without reading [named excluded content] |
```

Column requirements:
- **Verification Artifact**: the specific named section or field in the emitted rubric where
  a reader finds the criterion's evidence. Not a paraphrase of the Pass field -- the actual
  section title or field name.
- **Scan Method**: the specific action an evaluator takes. "Check the Essential Criteria
  section for a Text field matching 'Without [Y]...Not [X], but [Y]'" is acceptable; "verify
  the criterion" is not.
- **Independence**: "Yes -- independently verifiable without reading [excluded content]"
  where [excluded content] names the specific construction records, role instruction bodies,
  or phase outputs that a verifier can skip. "Yes -- independently verifiable" without the
  exclusion name fails this column.

STOP CONDITION -- ROLE: EVALUABILITY AUDITOR: The EVALUABILITY GATE is not satisfied until
every row has all three cells populated in the required form. Any blank cell or generic
Independence claim blocks the gate. Do not proceed to Phase 9 until the EVALUABILITY GATE
is satisfied.

**EVALUABILITY GATE is satisfied when:** All rows populated, Verification Artifact and Scan
Method specific and named, Independence field names excluded content for every row.

---

### EVALUABILITY COMPETITOR

```
EVALUABILITY COMPETITOR: A rubric that ends with vN Candidates as the final section. Every
criterion has a Pass field naming Location, Observable, and Standard. An evaluator verifying
any criterion follows three steps: (1) find the criterion, (2) read its Pass field to get
the location and observable, (3) navigate to that location and check. The rubric is
evaluable in the sense that a path exists. The gap is that the path is reconstructed per
criterion from the criterion body -- it is not stated as a unified criterion-to-artifact
declaration anywhere in the document. To know whether criterion C-NN is verifiable without
reading the role instruction bodies, an evaluator must read the Pass field, check the
Independence Map, and search the Notes field. No section makes an explicit "without reading
[excluded content]" statement for any criterion.

Derive what the terminal section must provide.

REQUIRED MECHANISM: A CRITERION EVALUABILITY MAP as the final section of the emitted
document, produced from the ROLE: EVALUABILITY AUDITOR EVALUABILITY GATE output, with
one row per structural criterion mapping C-NN to Verification Artifact, Scan Method, and
Independence guarantee naming the excluded content. The map makes the full verification
path -- including the independence boundary -- available without reading criterion fields
or role instruction bodies.
```

---

### PHASE 9 -- EMIT

**PREREQUISITE: EVALUABILITY GATE: Criterion Evaluability Map with all C-NN rows populated,
Verification Artifact and Scan Method named for every structural criterion, and Independence
field naming excluded content for every row.**

This phase's entry is gated on the EVALUABILITY GATE identifier above. If the ROLE:
EVALUABILITY AUDITOR has not satisfied the EVALUABILITY GATE, Phase 9 cannot begin.

Output the complete rubric document with sections in this order:

1. **Failure Mode Log**
2. **Design Rationale** -- self-application; >= 3 rejected generic criteria; EVALUABILITY
   COMPETITOR block embedded in this section
3. **Essential Criteria**
4. **Recommended Criteria**
5. **Independence Map** -- MECHANISM DEFINER Step 1 output
6. **PHASE-LOCALITY RULE** -- MECHANISM DEFINER Step 2 output; all three zones verbatim
7. **Aspirational Criteria** -- COMPETITOR blocks inline; Notes cites DEFINER OUTPUT GATE,
   MECHANISM DEFINER GATE, and PHASE-LOCALITY RULE identifiers
8. **Scoring** -- composite formula, threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
10. **vN Candidates**
11. **Criterion Evaluability Map** -- reproduce the EVALUABILITY GATE output from ROLE:
    EVALUABILITY AUDITOR verbatim as the final section; all four columns (C-NN, Verification
    Artifact, Scan Method, Independence) must be present; the EVALUABILITY GATE identifier
    must be traceable from this section to the ROLE: EVALUABILITY AUDITOR header

An evaluator reading only section 11 (Criterion Evaluability Map) must be able to confirm
three properties for every structural criterion: (a) the named verification artifact is a
specific section or field in this document, (b) the scan method names a concrete check
rather than a general description, (c) the independence guarantee names the excluded
instruction content -- all three properties independently verifiable without reading role
instruction bodies. Both (a) and (c) are independently verifiable without reading role
instruction bodies.

STOP CONDITION -- Phase 9: Emit is incomplete until section 11 is present as the final
section, the EVALUABILITY GATE identifier appears in the Phase 9 PREREQUISITE header, the
map contains one row per structural criterion with all four columns populated, and the
Independence column names excluded content for every row. A map with "independently
verifiable" in the Independence column without naming the excluded content fails the
emit STOP condition.

---

## Set-Level Design Notes

**Axis coverage:** Five distinct axis families across V-01--V-05: output format (formal table
with labeled columns as terminal section of Phase 9), lifecycle emphasis (Phase 8.5 gate
requiring artifact+method+exclusion before Phase 9), inertia framing (EVALUABILITY COMPETITOR
before Phase 9 naming the rubric-without-evaluability-map gap), combined (all three single
axes together), role sequence (ROLE: EVALUABILITY AUDITOR with named exit gate quoted in
Phase 9 PREREQUISITE).

**C-43 coverage:** V-01 (very strong, single-axis -- formal CRITERION EVALUABILITY MAP table
as terminal section of Phase 9, artifact+scan columns required), V-04 (very strong, combined
-- Phase 8.5 gate + terminal table + inertia), V-05 (very strong, combined + role gate).
V-02 (partial -- gate produces declarations but Phase 9 references rather than produces
terminal section) and V-03 (partial -- prose notes present but no formal column separation)
are ablation controls confirming that table format and terminal production are load-bearing.

**C-44 coverage:** V-02 (strong, single-axis -- Phase 8.5 gate requires named excluded
content in Independence column), V-04 (very strong, combined -- gate + terminal table both
require Independence column with named exclusion), V-05 (very strong, same as V-04 plus
role-gate enforcement). V-01 (no Independence column) and V-03 (no exclusion naming) are
ablation controls confirming that either the lifecycle gate or the explicit column requirement
is load-bearing for C-44.

**C-11 coverage (secondary):** V-03 (partial -- EVALUABILITY COMPETITOR block before Phase
9 names the gap, inertia framing activated), V-04 (partial -- EVALUABILITY COMPETITOR
embedded in Design Rationale), V-05 (partial -- same as V-04). V-01 and V-02 ablate C-11
to isolate whether inertia framing adds scoring value.

**Ablation map:**

| | C-43 | C-44 | C-11 |
|-|------|------|------|
| V-01 | Target | Ablated | Ablated |
| V-02 | Partial | Target | Ablated |
| V-03 | Partial | Ablated | Partial |
| V-04 | Target | Target | Partial |
| V-05 | Target | Target | Partial |

**Isolation logic:**
- V-01 vs V-02: isolates C-43 terminal-production vs lifecycle-gate for C-43 satisfaction.
- V-01 vs V-03: isolates formal-table vs prose-notes for C-43 satisfaction.
- V-02 vs V-04: isolates terminal-table addition for C-43 when C-44 mechanism is held constant.
- V-04 vs V-05: isolates role-gate enforcement contribution when C-43+C-44 mechanisms are held constant.

**R14 → R15 candidate:** If V-04 passes C-43+C-44 simultaneously, the four-column terminal
table with Phase 8.5 gate is confirmed as sufficient for both criteria. R15 should test
whether the EVALUABILITY GATE can be simplified -- specifically, whether a Phase 9 terminal
table instruction alone (without Phase 8.5) can achieve C-44 PASS if the Phase 9 table
instruction explicitly requires the Independence column with named exclusion (combining
V-01's formal table with the Independence column requirement V-04 introduces via the Phase
8.5 gate). If V-05 scores higher than V-04 on any criterion not in the ablation map, the
role-gate mechanism adds value and R15 should incorporate ROLE: EVALUABILITY AUDITOR into
the three-gate stack alongside ROLE: CRITERION DEFINER, ROLE: MECHANISM DEFINER, and
ROLE: BUILDER ASPIRATIONAL.
