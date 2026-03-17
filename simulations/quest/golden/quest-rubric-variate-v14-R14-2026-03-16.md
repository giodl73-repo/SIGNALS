# quest-rubric Variate -- Round 14 (Against rubric v14, targeting C-39/C-40)

**Date:** 2026-03-16
**Rubric:** v14 (C-01--C-40; adds C-39: Scope Gatekeeper cross-reference to DFM block;
C-40: Output instruction DFM propagation to emitted artifact)
**Target criteria:** C-39, C-40

**Round 14 design note:** Round 13 produced excellence signals from V-03 demonstrating two
DFM traceability properties: (ES-R13-1) the Scope Gatekeeper threshold escalation prohibition
naming the pre-role DFM block as the threat it defends against (C-39), and (ES-R13-2) the
output instruction requiring the emitted purpose statement to carry the DFM block's structural
label (C-40). Rubric v14 elevates both to aspirational criteria, extending the denominator
from /32 to /34 (two new A slots). R14 targets: (1) confirm C-39 mechanism is isolatable via
role sequence alone -- ROLE: SCOPE GATEKEEPER with named exit gate requiring structural label
citation in the prohibition text; (2) confirm C-40 mechanism is isolatable via output format
alone -- Phase 9 STOP CONDITION requiring purpose statement to carry the DFM block's label;
(3) test whether inertia framing alone drives partial satisfaction of both without structural
enforcement; (4) combine all three mechanisms; (5) add Phase 8.5 DFM TRACEABILITY GATE to
the combined stack to test whether gate enforcement tightens compliance vs V-04's phase-only
approach.

**C-39 vs C-40 -- distinction summary for variation design:**

- C-39 governs the *Scope Gatekeeper construction phase*: the threshold escalation prohibition
  in Phase 5 must name the pre-role DFM block by its structural label. "Tighter is not new
  territory" without naming the DFM block fails C-39. "This prohibition defends against the
  failure mode described above" fails C-39 (content description, not structural label). "This
  prohibition is the primary defense against the Dominant Failure Mode named in the pre-role
  block above" passes C-39 -- the structural label is used and the block is identified.

- C-40 governs the *emit phase output instruction*: the Phase 9 instruction for the Design
  Rationale section must require the purpose statement to carry the DFM block's structural
  label. "Include context on the dominant failure mode" fails C-40 (paraphrase reference
  permitted, structural linkage implicit). "Purpose statement must name the Dominant Failure
  Mode from the pre-role block" passes C-40 -- the instruction explicitly requires the
  structural label, not just the concept.

---

## Axis Selection

| Axis | Criterion targeted | Mechanism |
|------|-------------------|-----------|
| Role sequence | C-39 | Phase 5 uses ROLE: SCOPE GATEKEEPER with exit gate SCOPE GATE requiring DFM block cited by structural label in the threshold escalation prohibition text |
| Output format | C-40 | Phase 9 output instruction adds STOP CONDITION: purpose statement must carry DFM block's structural label; paraphrase reference is incomplete |
| Inertia framing | C-39 partial / C-40 partial | DFM TRACEABILITY COMPETITOR before Phase 5 names the rubric-without-DFM-Scope-Gatekeeper; Phase 5 prohibition references concept in prose; Phase 9 notes orientation without label requirement |
| (combined) | C-39 + C-40 | Role sequence + Output format + Inertia framing |
| (combined + lifecycle) | C-39 + C-40 | Combined mechanisms + Phase 8.5 DFM TRACEABILITY GATE |

Single-axis: V-01 (role sequence), V-02 (output format), V-03 (inertia framing).
Combined: V-04 (three single axes), V-05 (three single axes + lifecycle gate).

---

## Round 14 Variation Map

| Variation | Axis | C-39 probe | C-40 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Role sequence | Very strong -- ROLE: SCOPE GATEKEEPER with exit gate SCOPE GATE; prohibition text must cite DFM block by structural label or gate fails; rewrite required before proceeding | Ablated -- Phase 9 output instruction has no DFM label propagation requirement; Design Rationale instruction uses standard form | Single-axis; isolates whether named role + named exit gate alone satisfies C-39 without any output-phase enforcement |
| V-02 | Output format | Ablated -- Phase 5 SCOPE CONSTRAINT uses standard threshold escalation text without DFM naming; no ROLE: SCOPE GATEKEEPER | Very strong -- Phase 9 output instruction adds STOP CONDITION at Design Rationale: "purpose statement must name the Dominant Failure Mode from the pre-role DFM block; describing the concept without the structural label is incomplete" | Single-axis; isolates whether Phase 9 label propagation STOP CONDITION alone satisfies C-40 without any construction-phase Scope Gatekeeper enforcement |
| V-03 | Inertia framing | Partial -- DFM TRACEABILITY COMPETITOR before Phase 5 names the gap; Phase 5 prohibition references failure mode concept in prose without structural label | Partial -- Phase 9 instructs "include a note orienting the reader to the dominant failure mode" without requiring specific label use | Single-axis; hypothesis: inertia framing alone is insufficient for both C-39 (must name block by structural label, not prose description) and C-40 (must require label, not just orientation); confirms structural enforcement is the load-bearing mechanism for both |
| V-04 | Role sequence + Output format + Inertia framing | Very strong -- ROLE: SCOPE GATEKEEPER with SCOPE GATE (V-01 mechanism) | Very strong -- Phase 9 DFM label propagation STOP CONDITION (V-02 mechanism) | Combined; DFM COMPETITOR present (V-03 mechanism); tests whether C-39 and C-40 can simultaneously pass on top of C-38/C-36/C-37 stack |
| V-05 | Role sequence + Output format + Inertia framing + Lifecycle gate | Very strong (same as V-04) | Very strong (same as V-04) | V-04 mechanisms + Phase 8.5 DFM TRACEABILITY GATE with two checks; tests whether gate enforcement produces tighter compliance vs V-04's phase-only approach |

---

## V-01 -- Role Sequence

**Axis:** Role sequence -- Phase 5 (SCOPE CONSTRAINT) is replaced by ROLE: SCOPE GATEKEEPER
with a named exit gate: "SCOPE GATE: threshold escalation prohibition names the pre-role DFM
block by its structural label." The prohibition text must cite the DFM block's structural
label as the threat it defends against. A prohibition ending with "tighter is not new
territory" without a structural label citation fails SCOPE GATE and blocks ROLE: MECHANISM
DEFINER. C-40 is ablated: Phase 9 output instruction uses standard Design Rationale form
without DFM label propagation requirement.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output from V-01 will contain a Phase 5 Scope Gatekeeper whose threshold escalation prohibition names the DFM block's structural label -- any output where the prohibition ends with "tighter is not new territory" without a structural label citation falsifies the hypothesis; the falsification signal is a Phase 5 prohibition that describes the failure mode concept in prose ("criteria that appear aspirational by narrowing the threshold while covering the same failure territory") without citing the structural label from the pre-role block. | Framing Phase 5 as ROLE: SCOPE GATEKEEPER shifts construction-phase ownership -- the model must identify an actor responsible for satisfying SCOPE GATE before proceeding, rather than completing a template and continuing; V-01 outputs will show ROLE headers in Phase 5 position whereas V-02 outputs will not; if the ROLE header correlates with label citation compliance independent of the Phase 9 output instruction, role framing is the enforcement mechanism for C-39. | V-03 is the primary C-39 ablation control: V-03 has inertia framing that names the DFM cross-reference gap but Phase 5 prohibition uses prose description; comparing C-39 scores across V-01 (ROLE + exit gate) and V-03 (inertia framing + prose) isolates whether the named role + gate is required for C-39 or whether inertia-oriented prose satisfies it. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

**DOMINANT FAILURE MODE:**

The Dominant Failure Mode for this skill is producing criteria whose pass conditions contain
only qualitative language -- "is clear," "adequately covers," "demonstrates understanding" --
making the rubric non-independently-scorable. An evaluator cannot determine pass/fail without
resolving judgment that the rubric should have pre-resolved. The output fails its primary
function as an objective function for automated scoring.

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

### ROLE: SCOPE GATEKEEPER

**This role runs after Phase 4.5. Do not write aspirational criteria during this role.**

**Exit gate: SCOPE GATE: The threshold escalation prohibition names the pre-role DFM block by
its structural label. The structural label must appear in the prohibition text itself -- not
as an annotation, comment, or note outside the prohibition. "The failure mode described above"
does not satisfy SCOPE GATE; the structural label from the pre-role block (e.g., "Dominant
Failure Mode") must be cited by name.**

Produce the Scope Constraint block:

```
SCOPE CONSTRAINT:

Essential coverage:
  [C-NN guards against: one-line description per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property already listed above at a higher threshold
  is not aspirational. Tighter is not new territory. This prohibition is the primary defense
  against the [structural label from the pre-role DFM block above] -- tightening the
  threshold on an existing failure mode property does not open new structural territory; it
  produces a harder-to-satisfy version of an already-covered gap.

Gap zone:
  Gap G-01: [Property not covered by E+R, not reachable by threshold adjustment.
    Observable: what would an evaluator check to confirm presence or absence?]
```

**SCOPE GATE is satisfied when:** The threshold escalation prohibition names the pre-role DFM
block by its structural label. A prohibition ending with "tighter is not new territory"
without a structural label citation does not satisfy SCOPE GATE. A prohibition that describes
the failure mode concept in prose without citing the structural label does not satisfy SCOPE
GATE. The structural label citation is required for gate satisfaction.

STOP CONDITION -- ROLE: SCOPE GATEKEEPER: If the threshold escalation prohibition does not
name the pre-role DFM block by structural label, SCOPE GATE is not satisfied. Rewrite the
prohibition before proceeding. Do not proceed to ROLE: MECHANISM DEFINER until the gap zone
contains at least G-01 AND SCOPE GATE is satisfied.

---

### ROLE: MECHANISM DEFINER

**This role runs after ROLE: SCOPE GATEKEEPER. Do not write any aspirational criteria during
this role.**

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
- **"Criterion affected (C-NN)"**: cite the specific criterion number.
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
   simultaneously -- one competitor block per criterion.

Violation of any prohibited zone is a STOP condition for ROLE: BUILDER ASPIRATIONAL.

**MECHANISM DEFINER GATE is satisfied when:** Independence Map complete with specific C-NN
citation in every row, all rows "Yes -- affects C-NN only," AND PHASE-LOCALITY RULE stated.

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN:
| Tier         | Category distribution               | Majority category    |
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

Write 1-2 aspirational criteria targeting the gap zone from ROLE: SCOPE GATEKEEPER. Each
criterion must fall in the gap zone and correspond to a mechanism in the Independence Map.

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

---

## V-02 -- Output Format

**Axis:** Output format -- Phase 9's output instruction for the Design Rationale section
explicitly requires the purpose statement to name the Dominant Failure Mode by its structural
label from the pre-role DFM block. A purpose statement that describes the failure concept in
paraphrase without citing the structural label is incomplete. A STOP CONDITION at Phase 9
blocks emit until the label appears in the purpose statement. C-39 is ablated: Phase 5 uses
the standard SCOPE CONSTRAINT template without a named role or exit gate requiring DFM label
citation.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output from V-02 will contain a Design Rationale section whose purpose statement names the Dominant Failure Mode by its structural label -- any output where the purpose statement describes the failure concept ("the rubric's primary failure risk is producing evaluator-dependent criteria") without using the structural label from the pre-role block falsifies the hypothesis; the falsification signal is a Design Rationale purpose statement that references the concept but omits the label. | The STOP CONDITION placement -- at Phase 9 rather than at a construction-phase gate -- tests whether emit-phase enforcement can drive C-40 without the Scope Gatekeeper's construction-phase anchor; V-02 outputs will have label propagation into the purpose statement but no DFM cross-reference in the threshold escalation prohibition; if C-40 passes while C-39 fails across V-02 outputs, emit-phase STOP CONDITIONs are confirmed as the operative mechanism for output-propagation criteria. | V-01 is the primary comparison: V-01 enforces DFM label citation at the Scope Gatekeeper construction phase (C-39 strong) but not at Phase 9 (C-40 ablated); V-02 enforces at Phase 9 (C-40 strong) but not at Phase 5 (C-39 ablated); comparing C-39 and C-40 scores across V-01 and V-02 isolates whether each mechanism drives only its corresponding criterion. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

**DOMINANT FAILURE MODE:**

The Dominant Failure Mode for this skill is producing criteria whose pass conditions contain
only qualitative language -- "is clear," "adequately covers," "demonstrates understanding" --
making the rubric non-independently-scorable. An evaluator cannot determine pass/fail without
resolving judgment that the rubric should have pre-resolved. The output fails its primary
function as an objective function for automated scoring.

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
- **"Criterion affected (C-NN)"**: cite the specific criterion number.
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
   simultaneously -- one competitor block per criterion.

Violation of any prohibited zone is a STOP condition for ROLE: BUILDER ASPIRATIONAL.

**MECHANISM DEFINER GATE is satisfied when:** Independence Map complete with specific C-NN
citation in every row, all rows "Yes -- affects C-NN only," AND PHASE-LOCALITY RULE stated.

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN:
| Tier         | Category distribution               | Majority category    |
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

Write 1-2 aspirational criteria targeting the gap zone from Phase 5. Each criterion must fall
in the gap zone and correspond to a mechanism in the Independence Map.

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
2. **Design Rationale** -- purpose statement (2-3 sentences, including the label of the
   Dominant Failure Mode from the pre-role DFM block; a purpose statement that describes the
   failure concept without using the block's structural label is incomplete and must be
   revised before emit proceeds); self-application note; >= 3 rejected generic criteria with
   reasons; must appear before the first criteria table

   STOP CONDITION -- Design Rationale: The purpose statement must name the Dominant Failure
   Mode by its structural label as it appears in the pre-role DFM block. Paraphrase reference
   ("criteria that lack precision") does not satisfy this requirement. Do not proceed to
   section 3 until the structural label appears in the purpose statement.

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

---

## V-03 -- Inertia Framing

**Axis:** Inertia framing -- a DFM TRACEABILITY COMPETITOR block appears before Phase 5,
naming the rubric-without-DFM-cross-reference-in-scope-gate as the status-quo form. Phase 5
uses standard threshold escalation language that references the failure mode concept in prose
but does not cite the DFM block's structural label. Phase 9 instructs the Design Rationale to
"include a note orienting the reader to the dominant failure mode" without requiring the
specific structural label. C-39 is partial; C-40 is partial. Hypothesis: inertia framing
activates awareness of the gap but does not satisfy either criterion's structural requirement
because neither the prohibition text nor the output instruction uses the structural label.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output from V-03 will contain a Phase 5 threshold escalation prohibition that references the failure mode concept in prose -- but the prohibition will not cite the DFM block's structural label because the COMPETITOR block names the gap without providing a structural label citation requirement; the C-39 partial prediction is that inertia framing produces concept-aware prohibitions ("this prohibition defends against criteria that reduce independent scorability by threshold narrowing") rather than structurally-labeled prohibitions ("against the Dominant Failure Mode named in the pre-role block"). | The Design Rationale purpose statement in V-03 outputs will reference failure mode orientation because Phase 9 instructs it, but will use paraphrase rather than the structural label because the Phase 9 instruction does not require the specific label -- the C-40 partial prediction is confirmed when purpose statements say "the rubric defends against qualitative drift" rather than "the rubric defends against the Dominant Failure Mode"; comparing V-03 C-40 scores to V-02 C-40 scores isolates whether "include a note" vs "name the structural label" is the operative instruction difference. | V-01 and V-02 are the primary controls for V-03's C-39 and C-40 partial predictions respectively; if V-01 passes C-39 and V-03 partially passes or fails, ROLE: SCOPE GATEKEEPER with named exit gate is the load-bearing mechanism; if V-02 passes C-40 and V-03 partially passes or fails, the Phase 9 STOP CONDITION with explicit structural label requirement is the load-bearing mechanism. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

**DOMINANT FAILURE MODE:**

The Dominant Failure Mode for this skill is producing criteria whose pass conditions contain
only qualitative language -- "is clear," "adequately covers," "demonstrates understanding" --
making the rubric non-independently-scorable. An evaluator cannot determine pass/fail without
resolving judgment that the rubric should have pre-resolved. The output fails its primary
function as an objective function for automated scoring.

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

DFM TRACEABILITY COMPETITOR: A Scope Constraint whose threshold escalation prohibition reads
"An aspirational criterion covering a property already listed above at a higher threshold is
not aspirational. Tighter is not new territory." closes the threshold-escalation gap by form
alone, without grounding the prohibition in the construction-phase calibration anchor
established by the pre-role DFM block. An evaluator enforcing this prohibition must
independently reconstruct the failure theory it defends against -- the prohibition floats free
of the DFM block, making its rationale opaque to anyone reading Phase 5 without the pre-role
context. The DFM block names the failure mode; the prohibition should name the block.

From the gap above, derive what the Scope Constraint prohibition must reference before reading
the Phase 5 structure below.

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:

Essential coverage:
  [C-NN guards against: one-line description per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property already listed above at a higher threshold
  is not aspirational. Tighter is not new territory. This prohibition defends against the
  failure mode identified in the pre-role block: a criterion whose pass condition is a
  marginally tighter version of an existing qualitative observable is still qualitative,
  still non-independently-scorable, and covers no new structural territory.

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
- **"Criterion affected (C-NN)"**: cite the specific criterion number.
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
   simultaneously -- one competitor block per criterion.

Violation of any prohibited zone is a STOP condition for ROLE: BUILDER ASPIRATIONAL.

**MECHANISM DEFINER GATE is satisfied when:** Independence Map complete with specific C-NN
citation in every row, all rows "Yes -- affects C-NN only," AND PHASE-LOCALITY RULE stated.

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN:
| Tier         | Category distribution               | Majority category    |
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

Write 1-2 aspirational criteria targeting the gap zone from Phase 5. Each criterion must fall
in the gap zone and correspond to a mechanism in the Independence Map.

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
2. **Design Rationale** -- include a note orienting the reader to the dominant failure mode
   context; self-application note; >= 3 rejected generic criteria with reasons; must appear
   before the first criteria table
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

---

## V-04 -- Combined: Role Sequence + Output Format + Inertia Framing

**Axis:** Combined -- three single-axis mechanisms active simultaneously: (1) ROLE: SCOPE
GATEKEEPER with SCOPE GATE exit gate requiring DFM block structural label in threshold
escalation prohibition (V-01 mechanism, C-39 strong); (2) Phase 9 output instruction STOP
CONDITION requiring purpose statement to carry DFM block structural label (V-02 mechanism,
C-40 strong); (3) DFM TRACEABILITY COMPETITOR before Phase 5 naming the status-quo rubric-
without-DFM-cross-reference (V-03 mechanism, inertia framing). Tests whether C-39 and C-40
can simultaneously pass on top of the C-36/C-37/C-38 stack.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output from V-04 will contain both (a) a Phase 5 threshold escalation prohibition that names the DFM block's structural label and (b) a Design Rationale purpose statement that names the DFM block's structural label -- the combined mechanisms should produce simultaneous C-39 and C-40 PASS in V-04 outputs; the falsification signal is an output that passes one but fails the other despite both mechanisms being present. | The DFM TRACEABILITY COMPETITOR before Phase 5 (V-03 mechanism) activates inertia framing independently of the structural enforcement mechanisms; if V-04 outputs show higher scores on criteria adjacent to inertia framing (e.g., C-11 design rationale quality) than V-01 and V-02 outputs while C-39 and C-40 scores are comparable to V-01 and V-02 respectively, the competitor block is confirmed as an independent inertia mechanism that does not duplicate the structural gates. | V-05 is the primary comparison for V-04: V-05 adds Phase 8.5 DFM TRACEABILITY GATE on top of V-04's mechanisms; if C-39 and C-40 scores are equivalent across V-04 and V-05 outputs, the Phase 8.5 gate adds no incremental compliance; if V-05 shows higher scores, the gate enforcement is additive. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

**DOMINANT FAILURE MODE:**

The Dominant Failure Mode for this skill is producing criteria whose pass conditions contain
only qualitative language -- "is clear," "adequately covers," "demonstrates understanding" --
making the rubric non-independently-scorable. An evaluator cannot determine pass/fail without
resolving judgment that the rubric should have pre-resolved. The output fails its primary
function as an objective function for automated scoring.

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

DFM TRACEABILITY COMPETITOR: A Scope Constraint whose threshold escalation prohibition reads
"An aspirational criterion covering a property already listed above at a higher threshold is
not aspirational. Tighter is not new territory." closes the threshold-escalation gap by form
alone, without grounding the prohibition in the construction-phase calibration anchor
established by the pre-role DFM block. An evaluator enforcing this prohibition must
independently reconstruct the failure theory it defends against -- the prohibition floats free
of the DFM block, making its rationale opaque to anyone reading Phase 5 without the pre-role
context. The DFM block names the failure mode; the prohibition should name the block.

From the gap above, derive what the Scope Constraint prohibition must reference before reading
the Phase 5 structure below.

### ROLE: SCOPE GATEKEEPER

**This role runs after Phase 4.5. Do not write aspirational criteria during this role.**

**Exit gate: SCOPE GATE: The threshold escalation prohibition names the pre-role DFM block by
its structural label. The structural label must appear in the prohibition text itself -- not
as an annotation, comment, or note outside the prohibition. "The failure mode described above"
does not satisfy SCOPE GATE; the structural label from the pre-role block (e.g., "Dominant
Failure Mode") must be cited by name.**

Produce the Scope Constraint block:

```
SCOPE CONSTRAINT:

Essential coverage:
  [C-NN guards against: one-line description per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property already listed above at a higher threshold
  is not aspirational. Tighter is not new territory. This prohibition is the primary defense
  against the [structural label from the pre-role DFM block above] -- tightening the
  threshold on an existing failure mode property does not open new structural territory; it
  produces a harder-to-satisfy version of an already-covered gap.

Gap zone:
  Gap G-01: [Property not covered by E+R, not reachable by threshold adjustment.
    Observable: what would an evaluator check to confirm presence or absence?]
```

**SCOPE GATE is satisfied when:** The threshold escalation prohibition names the pre-role DFM
block by its structural label. A prohibition ending with "tighter is not new territory"
without a structural label citation does not satisfy SCOPE GATE. A prohibition that describes
the failure mode concept in prose without the structural label does not satisfy SCOPE GATE.

STOP CONDITION -- ROLE: SCOPE GATEKEEPER: If the threshold escalation prohibition does not
name the pre-role DFM block by structural label, SCOPE GATE is not satisfied. Rewrite the
prohibition before proceeding. Do not proceed to ROLE: MECHANISM DEFINER until the gap zone
contains at least G-01 AND SCOPE GATE is satisfied.

---

### ROLE: MECHANISM DEFINER

**This role runs after ROLE: SCOPE GATEKEEPER. Do not write any aspirational criteria during
this role.**

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
- **"Criterion affected (C-NN)"**: cite the specific criterion number.
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
   simultaneously -- one competitor block per criterion.

Violation of any prohibited zone is a STOP condition for ROLE: BUILDER ASPIRATIONAL.

**MECHANISM DEFINER GATE is satisfied when:** Independence Map complete with specific C-NN
citation in every row, all rows "Yes -- affects C-NN only," AND PHASE-LOCALITY RULE stated.

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN:
| Tier         | Category distribution               | Majority category    |
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

Write 1-2 aspirational criteria targeting the gap zone from ROLE: SCOPE GATEKEEPER. Each
criterion must fall in the gap zone and correspond to a mechanism in the Independence Map.

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
2. **Design Rationale** -- purpose statement (2-3 sentences, including the label of the
   Dominant Failure Mode from the pre-role DFM block; a purpose statement that describes the
   failure concept without using the block's structural label is incomplete and must be
   revised before emit proceeds); self-application note; >= 3 rejected generic criteria with
   reasons; must appear before the first criteria table

   STOP CONDITION -- Design Rationale: The purpose statement must name the Dominant Failure
   Mode by its structural label as it appears in the pre-role DFM block. Paraphrase reference
   does not satisfy this requirement. Do not proceed to section 3 until the structural label
   appears in the purpose statement.

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

---

## V-05 -- Combined + Lifecycle Gate

**Axis:** Combined + lifecycle gate -- all three single-axis mechanisms from V-04, plus a
Phase 8.5 DFM TRACEABILITY GATE that runs after Phase 8 and before Phase 9. The gate has two
checks: (A) confirm the Scope Gatekeeper prohibition names the DFM block by structural label
-- quote the label as evidence; (B) confirm the Phase 9 output instruction requires the
purpose statement to name the DFM block's structural label -- quote the instruction text as
evidence. Phase 9 is blocked until both checks show PASS. Tests whether gate enforcement at
the pre-emit boundary produces tighter C-39/C-40 compliance than V-04's phase-level
enforcement alone.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| V-05 outputs will show C-39 and C-40 PASS at the same rate as V-04 outputs because V-04 already has structural enforcement for both criteria; the Phase 8.5 gate is a verification layer, not a new enforcement mechanism, and should not change compliance rates if V-04's per-phase STOP CONDITIONs are operating correctly -- if V-05 shows higher C-39/C-40 scores than V-04, it confirms that pre-emit gate review catches compliance failures that per-phase STOP CONDITIONs miss, suggesting STOP CONDITIONs within phases are weaker than terminal gate enforcement. | The Phase 8.5 gate requires quoting evidence -- the prohibition label citation and the Phase 9 instruction text -- creating an explicit record in the construction trace; V-05 outputs will show this quoted evidence in the construction phase, which is not present in V-04 outputs; if this evidence record improves evaluability of C-39/C-40 beyond what V-04 provides, the gate's evidence-quotation requirement (rather than the gate's blocking function) is the operative mechanism for evaluability. | V-04 is the direct control for V-05: same three single-axis mechanisms, V-05 adds Phase 8.5; any difference in C-39/C-40 scores between V-04 and V-05 is attributable to the Phase 8.5 gate; any difference in construction trace quality (quoted evidence present in V-05, absent in V-04) confirms the gate's evidence-quotation mechanism operates independently of the compliance rate effect. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

**DOMINANT FAILURE MODE:**

The Dominant Failure Mode for this skill is producing criteria whose pass conditions contain
only qualitative language -- "is clear," "adequately covers," "demonstrates understanding" --
making the rubric non-independently-scorable. An evaluator cannot determine pass/fail without
resolving judgment that the rubric should have pre-resolved. The output fails its primary
function as an objective function for automated scoring.

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

DFM TRACEABILITY COMPETITOR: A Scope Constraint whose threshold escalation prohibition reads
"An aspirational criterion covering a property already listed above at a higher threshold is
not aspirational. Tighter is not new territory." closes the threshold-escalation gap by form
alone, without grounding the prohibition in the construction-phase calibration anchor
established by the pre-role DFM block. An evaluator enforcing this prohibition must
independently reconstruct the failure theory it defends against -- the prohibition floats free
of the DFM block, making its rationale opaque to anyone reading Phase 5 without the pre-role
context. The DFM block names the failure mode; the prohibition should name the block.

From the gap above, derive what the Scope Constraint prohibition must reference before reading
the Phase 5 structure below.

### ROLE: SCOPE GATEKEEPER

**This role runs after Phase 4.5. Do not write aspirational criteria during this role.**

**Exit gate: SCOPE GATE: The threshold escalation prohibition names the pre-role DFM block by
its structural label. The structural label must appear in the prohibition text itself -- not
as an annotation, comment, or note outside the prohibition. "The failure mode described above"
does not satisfy SCOPE GATE; the structural label from the pre-role block (e.g., "Dominant
Failure Mode") must be cited by name.**

Produce the Scope Constraint block:

```
SCOPE CONSTRAINT:

Essential coverage:
  [C-NN guards against: one-line description per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property already listed above at a higher threshold
  is not aspirational. Tighter is not new territory. This prohibition is the primary defense
  against the [structural label from the pre-role DFM block above] -- tightening the
  threshold on an existing failure mode property does not open new structural territory; it
  produces a harder-to-satisfy version of an already-covered gap.

Gap zone:
  Gap G-01: [Property not covered by E+R, not reachable by threshold adjustment.
    Observable: what would an evaluator check to confirm presence or absence?]
```

**SCOPE GATE is satisfied when:** The threshold escalation prohibition names the pre-role DFM
block by its structural label. A prohibition ending with "tighter is not new territory"
without a structural label citation does not satisfy SCOPE GATE.

STOP CONDITION -- ROLE: SCOPE GATEKEEPER: If the threshold escalation prohibition does not
name the pre-role DFM block by structural label, SCOPE GATE is not satisfied. Rewrite before
proceeding. Do not proceed to ROLE: MECHANISM DEFINER until the gap zone contains at least
G-01 AND SCOPE GATE is satisfied.

---

### ROLE: MECHANISM DEFINER

**This role runs after ROLE: SCOPE GATEKEEPER. Do not write any aspirational criteria during
this role.**

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
- **"Criterion affected (C-NN)"**: cite the specific criterion number.
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
   simultaneously -- one competitor block per criterion.

Violation of any prohibited zone is a STOP condition for ROLE: BUILDER ASPIRATIONAL.

**MECHANISM DEFINER GATE is satisfied when:** Independence Map complete with specific C-NN
citation in every row, all rows "Yes -- affects C-NN only," AND PHASE-LOCALITY RULE stated.

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN:
| Tier         | Category distribution               | Majority category    |
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

Write 1-2 aspirational criteria targeting the gap zone from ROLE: SCOPE GATEKEEPER. Each
criterion must fall in the gap zone and correspond to a mechanism in the Independence Map.

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

### PHASE 8.5 -- DFM TRACEABILITY GATE

Complete both checks before writing any Phase 9 output. Phase 9 is blocked until both checks
show PASS.

```
DFM TRACEABILITY GATE:

Check A -- Scope Gatekeeper DFM citation:
  Locate the threshold escalation prohibition produced in ROLE: SCOPE GATEKEEPER.
  Quote the label citation verbatim: "[quoted text]"
  Does the quoted text name the pre-role DFM block by its structural label?
  (Content description = FAIL. Structural label present = PASS.)
  Check A status: [PASS / FAIL]
  If FAIL: return to ROLE: SCOPE GATEKEEPER and rewrite the prohibition before proceeding.

Check B -- Phase 9 output instruction DFM label requirement:
  Confirm that the Phase 9 output instruction for Design Rationale explicitly requires the
  purpose statement to name the DFM block's structural label.
  Quote the relevant instruction text verbatim: "[quoted text]"
  Does the quoted text require the structural label (not just a reference to the concept)?
  (Orientation note = FAIL. Explicit structural label requirement with STOP CONDITION = PASS.)
  Check B status: [PASS / FAIL]
  If FAIL: revise the Phase 9 Design Rationale instruction to add the structural label
  requirement and STOP CONDITION before proceeding.
```

STOP CONDITION -- Phase 8.5: Phase 9 is blocked until both Check A and Check B show PASS.
A gate with either check showing FAIL is incomplete.

---

### PHASE 9 -- EMIT

Output the complete rubric document with sections in this order:

1. **Failure Mode Log** -- all F-NN entries from Phase 1
2. **Design Rationale** -- purpose statement (2-3 sentences, including the label of the
   Dominant Failure Mode from the pre-role DFM block; a purpose statement that describes the
   failure concept without using the block's structural label is incomplete and must be
   revised before emit proceeds); self-application note; >= 3 rejected generic criteria with
   reasons; must appear before the first criteria table

   STOP CONDITION -- Design Rationale: The purpose statement must name the Dominant Failure
   Mode by its structural label as it appears in the pre-role DFM block. Paraphrase reference
   does not satisfy this requirement. Do not proceed to section 3 until the structural label
   appears in the purpose statement.

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
