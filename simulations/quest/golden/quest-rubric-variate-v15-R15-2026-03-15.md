# quest-rubric Variate -- Round 15 (Against rubric v15, targeting C-45/C-46)
**Date:** 2026-03-15
**Rubric:** v15 (C-01--C-46; denominator /38; adds C-45: emit-phase entry condition quotes the evaluability gate identifier verbatim, making evaluability sequencing independently auditable from Phase 9 entry alone; C-46: evaluability gate and emit-phase terminal table declared as non-redundant enforcement points with explicitly stated independent necessity)
**Target criteria:** C-45, C-46

**Round 15 design note:** Round 14 produced excellence signals ES-R14-1 and ES-R14-2 from V-04 and V-05. V-05 passed both C-45 and C-46; V-04 passed C-46 (non-redundancy declared in the gate body) but failed C-45 (Phase 9 PREREQUISITE was present but did not quote the EVALUABILITY GATE identifier verbatim). Rubric v15 elevates both to aspirational criteria, extending the denominator from /36 to /38. R15 targets: (1) isolate whether verbatim gate-ID in Phase 9 PREREQUISITE alone achieves C-45 without a non-redundancy declaration; (2) isolate whether a lifecycle-embedded NON-REDUNDANCY DECLARATION with per-mechanism failure-mode arguments achieves C-46 without verbatim Phase 9 PREREQUISITE; (3) test whether inertia framing (competitor naming gate-only and table-only failure modes) achieves C-46 via negative-example architecture without a positive architectural declaration; (4) combine all three single-axis mechanisms; (5) add phrasing-register enforcement to the combined stack, making independent-auditability a stated property of the Phase 9 PREREQUISITE.

**C-45 vs C-46 -- distinction summary for variation design:**

- C-45 governs the *Phase 9 entry condition*: Phase 9 must open with a PREREQUISITE line quoting the EVALUABILITY GATE identifier verbatim. A Phase 9 that describes a gate requirement in prose ("Phase 9 requires the evaluability gate to be complete") does not satisfy C-45; only a PREREQUISITE line that reproduces the exact gate identifier text -- "EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion rows populated, Verification Artifact named for every row, Scan Method named for every row, and Independence field naming excluded content for every row" -- satisfies C-45. The verbatim quote makes evaluability sequencing auditable from Phase 9's header alone without reading ROLE: EVALUABILITY AUDITOR's body.

- C-46 governs the *explicit non-redundancy declaration*: the skill prompt must declare that the evaluability gate and the Phase 9 terminal table are non-redundant enforcement points, each independently necessary. The declaration must include per-mechanism failure-mode arguments: the gate enforces C-44 (independence declaration) as a pre-Phase-9 structural condition; the terminal table enforces C-43 (terminal-section position) at emit-close. A rubric with both mechanisms present but no explicit non-redundancy statement does not satisfy C-46. The non-redundancy must be stated positively ("each is independently necessary because removing either causes exactly one criterion to fail") rather than shown only by negative example.

---

## Axis Selection

| Axis | Criterion targeted | Mechanism |
|------|-------------------|-----------|
| Role sequence | C-45 | ROLE: EVALUABILITY AUDITOR with named exit gate; Phase 9 PREREQUISITE quotes gate identifier verbatim; C-46 ablated (no non-redundancy declaration) |
| Lifecycle emphasis | C-46 | Phase 8.5 gate includes co-located NON-REDUNDANCY DECLARATION with per-mechanism failure-mode arguments (gate-only fails C-43; table-only fails C-44); Phase 9 PREREQUISITE present but describes gate requirement in prose, does not quote gate-ID verbatim (C-45 ablated) |
| Inertia framing | C-46 partial | EVALUABILITY ARCHITECTURE COMPETITOR before Phase 9 names Architecture A (gate-only, fails C-43) and Architecture B (table-only, fails C-44) as distinct failed patterns; no positive non-redundancy declaration; C-45 ablated |
| (combined) | C-45 + C-46 | ROLE: EVALUABILITY AUDITOR (role sequence for C-45) + NON-REDUNDANCY DECLARATION in gate (lifecycle for C-46) + EVALUABILITY ARCHITECTURE COMPETITOR (inertia for C-46); Phase 9 verbatim PREREQUISITE |
| Role sequence + Phrasing register | C-45 + C-46 + independent-auditability | V-04 mechanisms + Phase 9 PREREQUISITE adds explicit independent-auditability clause ("auditable from Phase 9 entry alone without reading ROLE: EVALUABILITY AUDITOR body") + NON-REDUNDANCY DECLARATION uses Architecture A / Architecture B labeled failure-experiment references |

Single-axis: V-01 (role sequence), V-02 (lifecycle emphasis), V-03 (inertia framing).
Combined: V-04 (three single axes), V-05 (three single axes + phrasing register).

---

## Round 15 Variation Map

| Variation | Axis | C-45 probe | C-46 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Role sequence | Very strong -- ROLE: EVALUABILITY AUDITOR with named exit gate; Phase 9 PREREQUISITE quotes gate identifier verbatim; any output where Phase 9 opens without the exact gate-ID text falsifies the C-45 hypothesis | Ablated -- no NON-REDUNDANCY DECLARATION; gate and terminal table both present but their non-redundancy not declared | Single-axis; isolates whether verbatim PREREQUISITE alone achieves C-45 independently of C-46; Phase 9 terminal CRITERION EVALUABILITY MAP has all 4 columns (satisfies C-43+C-44 baseline) |
| V-02 | Lifecycle emphasis | Ablated -- Phase 9 opens with a descriptive gate-completion requirement in prose, not a verbatim gate-ID quote | Very strong -- Phase 8.5 gate includes NON-REDUNDANCY DECLARATION with two mechanism-necessity arguments: gate enforces C-44 pre-Phase-9 (table-only lets model omit Independence column); terminal table enforces C-43 at emit-close (gate-only leaves declarations in construction record) | Single-axis; isolates whether lifecycle-embedded non-redundancy declaration achieves C-46 without verbatim Phase 9 PREREQUISITE |
| V-03 | Inertia framing | Ablated -- no ROLE: EVALUABILITY AUDITOR, no PREREQUISITE line, no verbatim gate-ID at Phase 9 entry | Partial -- EVALUABILITY ARCHITECTURE COMPETITOR block before Phase 9 names gate-only failure (fails C-43) and table-only failure (fails C-44) as distinct architectures; non-redundancy implied by competitor description but not declared as a positive architectural principle | Single-axis; hypothesis: naming failure modes via inertia competitor does not fully achieve C-46; primary C-46 ablation control for V-02 |
| V-04 | Role sequence + Lifecycle emphasis + Inertia framing | Very strong -- ROLE: EVALUABILITY AUDITOR + verbatim Phase 9 PREREQUISITE (same as V-01) | Very strong -- NON-REDUNDANCY DECLARATION in gate body with per-mechanism failure-mode arguments + EVALUABILITY ARCHITECTURE COMPETITOR (same as V-02 + V-03 combined) | Combined; tests whether C-45 and C-46 simultaneously pass on top of C-43+C-44 baseline |
| V-05 | Role sequence + Lifecycle emphasis + Inertia framing + Phrasing register | Very strong (same as V-04) + Phase 9 PREREQUISITE includes explicit independent-auditability clause stating the purpose of the verbatim quote | Very strong (same as V-04) + NON-REDUNDANCY DECLARATION uses Architecture A / Architecture B as named failure-experiment labels, enabling independent-necessity verification by label | V-04 mechanisms + phrasing register; tests whether making the independent-auditability purpose explicit in the PREREQUISITE adds measurable C-45 scoring value vs V-04's verbatim-but-unexplained PREREQUISITE |

---

## V-01 -- Role Sequence

**Axis:** Role sequence -- ROLE: EVALUABILITY AUDITOR runs after Phase 8 with a named exit
gate "EVALUABILITY GATE: ...". Phase 9 opens with a PREREQUISITE line that quotes the
EVALUABILITY GATE identifier verbatim. This makes evaluability sequencing auditable from
Phase 9's header alone without reading ROLE: EVALUABILITY AUDITOR's body. C-46 is ablated:
gate and terminal table are both present and satisfy C-43/C-44, but no non-redundancy
declaration is included.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-01 will contain a Phase 9 that opens with a PREREQUISITE line reproducing the EVALUABILITY GATE identifier verbatim -- any output where Phase 9 begins with its emit manifest without a PREREQUISITE line, or where the PREREQUISITE paraphrases the gate requirement without quoting the identifier text, falsifies the C-45 hypothesis; the falsification signal is Phase 9 that opens with section headings before the PREREQUISITE, or a PREREQUISITE that uses the identifier in embedded prose ("the Phase 8 EVALUABILITY GATE") rather than as a standalone gate-ID quote. | The named role architecture (ROLE: EVALUABILITY AUDITOR with exit gate + Phase 9 PREREQUISITE quoting gate-ID) creates the same independently auditable sequencing property for the evaluability path that C-41 creates for the aspirational construction path; a reader can verify that Phase 9 was properly gated by reading Phase 9's PREREQUISITE line alone, without reading ROLE: EVALUABILITY AUDITOR's instructions -- this property is present in V-01 outputs and absent in V-02 outputs (which have a descriptive gate requirement in prose rather than a verbatim identifier), making V-02 the primary C-45 ablation control. | V-02 is the primary isolation control: V-02 has a lifecycle gate requiring non-redundancy declaration but a descriptive (non-verbatim) Phase 9 entry condition; comparing C-45 scores across V-01 (verbatim PREREQUISITE, no non-redundancy) and V-02 (non-redundancy, non-verbatim PREREQUISITE) isolates whether the verbatim quote -- not just a gate-completion requirement -- is load-bearing for C-45; prediction: V-01 passes C-45, V-02 fails C-45. |

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

STOP CONDITION -- ROLE: CRITERION DEFINER: Rewrite before proceeding if the output of this
role contains anything beyond the two required templates. The two templates are the complete
and exclusive output of this role.

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

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

STOP CONDITION: Do not satisfy the MECHANISM DEFINER GATE until every row shows "Yes --
affects C-NN only."

#### Step 2 -- PHASE-LOCALITY RULE

**PHASE-LOCALITY RULE: Named competitors may not be placed in:**

1. Preamble or introductory framing that precedes any construction phase.
2. A shared instructional block or role-level preamble that precedes more than one
   construction step.
3. A combined competitor block that introduces or governs more than one criterion.

Violation of any prohibited zone is a STOP condition for ROLE: BUILDER ASPIRATIONAL.

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

### ROLE: EVALUABILITY AUDITOR

**This role runs after Phase 8. Do not begin Phase 9 until this role's exit gate is
satisfied.**

**Exit gate: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.**

Read all structural criteria produced in Phases 3, 4, and ROLE: BUILDER ASPIRATIONAL. For
each criterion, produce:

```
EVALUABILITY GATE -- Criterion Evaluability Map:
| C-NN | Verification Artifact | Scan Method | Independence |
|------|-----------------------|-------------|--------------|
| C-01 | [named section or field in emitted rubric] | [specific check: scan for token X / count Y / confirm structure Z] | Yes -- independently verifiable without reading [named excluded content] |
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

### PHASE 9 -- EMIT

**PREREQUISITE: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.**

This phase's entry is gated on the EVALUABILITY GATE identifier above. If ROLE: EVALUABILITY
AUDITOR has not satisfied the EVALUABILITY GATE, Phase 9 cannot begin.

Output the complete rubric document with sections in this order:

1. **Failure Mode Log** -- all F-NN entries from Phase 1
2. **Design Rationale** -- dominant failure mode, self-application, >= 3 rejected generic
   criteria with reasons; must appear before the first criteria table
3. **Essential Criteria** -- all five fields per criterion
4. **Recommended Criteria** -- all five fields per criterion
5. **Independence Map** -- the MECHANISM DEFINER Step 1 output
6. **PHASE-LOCALITY RULE** -- the MECHANISM DEFINER Step 2 output; all three prohibited zones
   enumerated verbatim
7. **Aspirational Criteria** -- COMPETITOR blocks inline immediately before each criterion;
   Notes cites DEFINER OUTPUT GATE, MECHANISM DEFINER GATE, and PHASE-LOCALITY RULE identifiers
8. **Scoring** -- composite formula, golden threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifier list
10. **vN Candidates** -- patterns approaching promotion; evidence needed per candidate
11. **Criterion Evaluability Map** -- reproduce the EVALUABILITY GATE output from ROLE:
    EVALUABILITY AUDITOR verbatim as the final section; all four columns (C-NN, Verification
    Artifact, Scan Method, Independence) must be present for every structural criterion

STOP CONDITION -- Phase 9: The emit is incomplete until section 11 is present as the final
section with all four columns populated for every structural criterion. A terminal section
missing the Independence column, or with Independence cells stating "independently verifiable"
without naming excluded content, is incomplete.

---

## V-02 -- Lifecycle Emphasis

**Axis:** Lifecycle emphasis -- Phase 8.5 EVALUABILITY GATE runs after Phase 8 and before
Phase 9. The gate body includes a NON-REDUNDANCY DECLARATION that names the gate and the
Phase 9 terminal table as non-redundant enforcement points and provides per-mechanism
failure-mode arguments: removing the gate leaves the terminal table free to omit the
Independence column (fails C-44); removing the terminal table leaves evaluability
declarations in the construction record rather than the emitted document (fails C-43). Phase
9 opens with a descriptive gate-completion requirement in prose -- "Confirm Phase 8.5
EVALUABILITY GATE is complete before emitting" -- but does NOT quote the EVALUABILITY GATE
identifier verbatim as a PREREQUISITE line. C-45 is ablated; C-46 is strongly targeted.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-02 will contain a Phase 8.5 NON-REDUNDANCY DECLARATION block naming both enforcement mechanisms as independently necessary, with two explicit failure-mode arguments: "gate-only fails C-43 because no terminal section appears in the emitted document" and "table-only fails C-44 because the Independence column can be omitted without the pre-Phase-9 gate"; any output that has both mechanisms present without the explicit non-redundancy statement, or that states non-redundancy without the per-mechanism failure-mode arguments, partially satisfies C-46 but does not fully pass. | The Phase 9 entry condition in V-02 is a prose description ("Before writing Phase 9 output, confirm Phase 8.5 EVALUABILITY GATE is complete") rather than a verbatim gate-ID quote; rubrics produced from V-02 will show Phase 9 opening with its emit manifest rather than a PREREQUISITE line reproducing the gate identifier; if V-01 outputs pass C-45 while V-02 outputs fail C-45, the verbatim quote -- not just a gate-completion requirement -- is confirmed as the C-45 load-bearing mechanism. | V-01 is the primary C-45 ablation control; V-03 is the primary C-46 isolation control for V-02 (V-03 has inertia competitor naming failure modes but no positive non-redundancy declaration); if V-02 passes C-46 while V-03 partially passes or fails, positive NON-REDUNDANCY DECLARATION is load-bearing for C-46. |

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

Minimum: 3 blocking entries, 2 suboptimal entries. Do not begin ROLE: CRITERION DEFINER
until the failure log contains at least 5 entries.

---

### ROLE: CRITERION DEFINER

**Exit gate: DEFINER OUTPUT GATE: Two slot-fillable templates (Text template + Pass template),
no additional content.**

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence]
  X = [rejected form]
```

Causal direction rule: "Without Y, Z fails." Prohibited: causality located in wrong form's
consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

**DEFINER OUTPUT GATE satisfied when:** Both templates in slot-fillable form. Nothing else.
Rewrite if output contains anything beyond the two templates.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Draft from blocking failure modes. Apply Text and Pass templates. Competitor immediately
before criterion. Five fields: C-NN, Text, Weight: essential, Category, Pass. No bare
qualitative observables.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**

Same five fields. Dimension annotation required. Pass tests degree, precision, or specificity.

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

**Do not proceed to ROLE: MECHANISM DEFINER until gap zone contains at least G-01.**

---

### ROLE: MECHANISM DEFINER

**Exit gate: MECHANISM DEFINER GATE: Independence Map with all C-NN citations populated and
all rows showing "Yes -- affects C-NN only," AND PHASE-LOCALITY RULE stated.**

#### Step 1 -- Independence Map

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
```

STOP: Any row showing "No -- overlaps" requires redesign before proceeding.

#### Step 2 -- PHASE-LOCALITY RULE

**Named competitors may not be placed in:** (1) preamble preceding any phase; (2) shared
instructional block preceding more than one step; (3) combined block governing more than one
criterion. Violation is a STOP condition for ROLE: BUILDER ASPIRATIONAL.

**MECHANISM DEFINER GATE satisfied when:** Independence Map complete + PHASE-LOCALITY RULE
stated.

---

### PHASE 5.75 -- TIER-DIVERGENCE SCAN

```
TIER-DIVERGENCE SCAN:
| Tier         | Category distribution   | Majority category    |
|--------------|-------------------------|----------------------|
| Essential    | [cat: N, ...]           | [majority or "tied"] |
| Recommended  | [cat: N, ...]           | [majority or "tied"] |
| Aspirational | [after ROLE: BUILDER]   | [To be filled]       |

Distinct majority categories (E+R): [list]. Scan status: [COMPLIANT / BLOCKED]
```

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE: DEFINER OUTPUT GATE: Two slot-fillable templates, no additional content.**
**PREREQUISITE: MECHANISM DEFINER GATE: Independence Map complete + PHASE-LOCALITY RULE
stated.**

Write 1-2 aspirational criteria targeting gap zone. Competitor inline before each criterion
(PHASE-LOCALITY RULE applies). Notes: "closes gap via [mechanism] | DEFINER OUTPUT GATE:
Two slot-fillable templates | MECHANISM DEFINER GATE: Independence Map | PHASE-LOCALITY
RULE: applied | competitor: [first four words]."

STOP: Missing gate/rule identifiers in Notes -> rewrite. Competitor in prohibited zone -> move.

---

### PHASE 6.75 -- COMPETITOR PLACEMENT + COVERAGE AUDIT

```
STEP A: phase-local + zone check. Step A status: [COMPLIANT / BLOCKED]
STEP B: novel aspirational count [N] = competitor count [N]? Step B status: [COMPLIANT / BLOCKED]
STEP C: distinct majority categories (all tiers) >= 2? Final scan status: [COMPLIANT / BLOCKED]
```

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

Complete this block before writing any Phase 9 output. Phase 9 is blocked until all rows
are populated and the NON-REDUNDANCY DECLARATION below is stated.

**NON-REDUNDANCY DECLARATION:**

Before completing the gate rows, produce the following architectural declaration:

```
NON-REDUNDANCY DECLARATION:
This EVALUABILITY GATE (Phase 8.5) and the Phase 9 terminal CRITERION EVALUABILITY MAP are
non-redundant enforcement points. Each is independently necessary:

Gate necessity (this phase): This gate enforces the Independence column (C-44 requirement)
as a pre-Phase-9 structural condition. Removing this gate and keeping only the Phase 9
terminal table allows a model to emit a terminal table without the Independence column
populated -- the terminal table instruction specifies columns but does not block Phase 9
entry on Independence completion. A rubric produced from a table-only architecture (no pre-
Phase-9 gate) fails C-44 because the independence declaration can be omitted without the
gate's pre-commit forcing. A gate-only architecture (without the terminal table) fails C-43
because the evaluability declarations remain in the construction record rather than appearing
as a terminal section in the emitted document.

Terminal table necessity (Phase 9): The Phase 9 terminal CRITERION EVALUABILITY MAP enforces
the terminal-section position of the criterion-to-artifact mapping (C-43 requirement) at
emit-close. Removing the terminal table and keeping only this gate leaves the evaluability
declarations in Phase 8.5 -- a pre-Phase-9 output that does not appear as a named section
in the emitted rubric document. The terminal table is independently necessary because it
places the criterion-to-artifact map into the emitted document as a final section.

Non-redundancy: removing either mechanism causes exactly one of C-43 or C-44 to fail. The
combination cannot be reduced to either enforcement point alone.
```

STOP CONDITION: Phase 8.5 is incomplete until the NON-REDUNDANCY DECLARATION above is
produced with both gate-necessity and terminal-table-necessity arguments present. A Phase 8.5
block that populates the gate rows without the NON-REDUNDANCY DECLARATION does not satisfy
this phase.

After stating the NON-REDUNDANCY DECLARATION, complete the gate rows:

```
EVALUABILITY GATE:
| C-NN | Verification Artifact | Scan Method | Independence |
|------|-----------------------|-------------|--------------|
| C-01 | [named section or field in emitted rubric document] | [specific check: scan for token X / count Y / confirm structure Z] | Yes -- independently verifiable without reading [named excluded content] |
```

Column requirements:
- **Verification Artifact**: name the specific document section or field.
- **Scan Method**: name the specific check. Generic descriptions are not acceptable.
- **Independence**: must name the excluded content. "Yes -- independently verifiable" without
  naming what is excluded is incomplete.

STOP CONDITION -- Phase 8.5: Phase 9 is blocked until the NON-REDUNDANCY DECLARATION is
stated AND every row has all three cells populated in the required form.

---

### PHASE 9 -- EMIT

Before writing Phase 9 output, confirm Phase 8.5 EVALUABILITY GATE is complete and the
NON-REDUNDANCY DECLARATION has been stated.

Output the complete rubric document with sections in this order:

1. **Failure Mode Log**
2. **Design Rationale** -- self-application; >= 3 rejected generic criteria
3. **Essential Criteria**
4. **Recommended Criteria**
5. **Independence Map**
6. **PHASE-LOCALITY RULE** -- all three prohibited zones verbatim
7. **Aspirational Criteria** -- COMPETITOR blocks inline; Notes cites all gate/rule identifiers
8. **Scoring** -- composite formula, threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
10. **vN Candidates**
11. **Criterion Evaluability Map** -- reproduce the Phase 8.5 EVALUABILITY GATE output
    verbatim as the final section; all four columns (C-NN, Verification Artifact, Scan
    Method, Independence) must be present for every structural criterion; the NON-REDUNDANCY
    DECLARATION need not appear in the emitted document

STOP CONDITION -- Phase 9: Emit is incomplete if section 11 is absent, if any row has a
blank cell, or if the Independence column states "independently verifiable" without naming
excluded content.

---

## V-03 -- Inertia Framing

**Axis:** Inertia framing -- before Phase 9, a named EVALUABILITY ARCHITECTURE COMPETITOR
block describes two incomplete architectures: Architecture A (gate-only, fails C-43) and
Architecture B (terminal-table-only, fails C-44). The competitor names each architecture's
failure mode specifically and requires the model to derive the combined approach before
reading the required mechanism. Phase 9 closes with a 4-column CRITERION EVALUABILITY MAP
terminal section. No ROLE: EVALUABILITY AUDITOR. No Phase 8.5 gate. No Phase 9 PREREQUISITE
quoting gate-ID verbatim. C-46 is partial: the competitor block implies non-redundancy by
describing two distinct failure modes, but does not produce a positive architectural
declaration with the "each is independently necessary" framing. C-45 is ablated.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-03 will contain an EVALUABILITY ARCHITECTURE COMPETITOR section before Phase 9 describing Architecture A and Architecture B with their specific failure modes; the Phase 9 terminal section will be a 4-column CRITERION EVALUABILITY MAP (satisfying C-43 and C-44 baseline); the C-46 partial prediction is that the competitor block implies non-redundancy by juxtaposing two distinct failure modes without declaring "each mechanism is independently necessary" as a positive architectural principle -- outputs that reflect this description will show the combined architecture without a standalone non-redundancy statement. | The inertia framing activates the C-46 mechanism at the competitor level; if V-03 outputs show higher C-46 partial scores than V-01 outputs (which have no inertia framing for C-46), the EVALUABILITY ARCHITECTURE COMPETITOR is contributing to C-46 scoring even without a positive declaration; comparing C-46 scores across V-02 (positive declaration) and V-03 (negative-example competitor) isolates whether the positive "independently necessary" framing is required for full C-46 PASS. | V-02 is the primary C-46 isolation control: V-02 has a positive NON-REDUNDANCY DECLARATION without inertia competitor; V-03 has an inertia competitor naming failure modes without the positive declaration; prediction: V-02 passes C-46, V-03 partially passes or fails C-46, confirming that positive declaration is load-bearing for full C-46 satisfaction. |

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

**PREREQUISITE: DEFINER OUTPUT GATE.**

Five fields per criterion. Templates applied. Competitor immediately before criterion. No
bare qualitative observables.

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

Step 2 -- PHASE-LOCALITY RULE: Named competitors may not be placed in: (1) preamble
preceding any phase; (2) shared block preceding more than one step; (3) combined block
governing more than one criterion. Violation is a STOP condition.

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

1-2 aspirational criteria. Competitor inline before each criterion (PHASE-LOCALITY RULE
applies). Notes: "closes gap via [mechanism] | DEFINER OUTPUT GATE: Two slot-fillable
templates | MECHANISM DEFINER GATE: Independence Map | PHASE-LOCALITY RULE: applied |
competitor: [first four words]."

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

### EVALUABILITY ARCHITECTURE COMPETITOR

Before writing Phase 9, name the two incomplete architectures that appear to enforce
evaluability but each fail independently:

```
EVALUABILITY ARCHITECTURE COMPETITOR:

Architecture A -- Gate-only enforcement: A rubric skill that enforces a pre-emit evaluability
gate requiring Verification Artifact, Scan Method, and Independence for every criterion.
The gate is satisfied before Phase 9 begins. The construction record contains the criterion-
to-artifact map with all four columns. Phase 9's emit manifest ends with vN Candidates as
the final section -- the construction record is not reproduced in the emitted document. An
evaluator reading the emitted rubric finds no terminal evaluability section. To verify any
criterion's independence boundary, they must return to the construction record.

Architecture A fails C-43 because the emitted document contains no terminal section
declaring the criterion-to-verification-artifact mapping. The gate enforces the content;
nothing enforces the terminal-section position in the emitted output.

Architecture B -- Terminal-table-only enforcement: A rubric skill that ends Phase 9 with
a CRITERION EVALUABILITY MAP section (C-NN | Verification Artifact | Scan Method columns)
but has no pre-Phase-9 gate. The terminal table is present in the emitted document. The
table has three columns -- it does not include an Independence column. An evaluator reading
the table can find the verification artifact and scan method but cannot determine from the
table alone whether verifying C-NN requires reading construction records.

Architecture B fails C-44 because the terminal table contains no Independence column naming
the excluded content. Without a pre-Phase-9 gate requiring the Independence field, the
terminal section instruction alone does not enforce its presence.

Each architecture has a distinct failure mode. Neither is sufficient. The combined approach
requires both enforcement points: a gate enforcing Independence as a pre-Phase-9 condition
plus a terminal table enforcing terminal-section position and all four columns in the emitted
document.

From this description, derive the combined enforcement structure before reading the required
approach below.

REQUIRED APPROACH: Phase 9 closes with a CRITERION EVALUABILITY MAP terminal section with
four columns (C-NN | Verification Artifact | Scan Method | Independence), where the
Independence column names excluded content for every row. Every structural criterion has a
row. The terminal table is the final section of the emitted document.
```

---

### PHASE 9 -- EMIT

Output the complete rubric document with sections in this order:

1. **Failure Mode Log**
2. **Design Rationale** -- self-application; >= 3 rejected generic criteria; EVALUABILITY
   ARCHITECTURE COMPETITOR embedded in this section to name the prior-state gap the terminal
   CRITERION EVALUABILITY MAP closes
3. **Essential Criteria**
4. **Recommended Criteria**
5. **Independence Map**
6. **PHASE-LOCALITY RULE** -- all three prohibited zones verbatim
7. **Aspirational Criteria** -- COMPETITOR blocks inline; Notes cites all gate/rule identifiers
8. **Scoring** -- composite formula, threshold, three-state table
9. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
10. **vN Candidates**
11. **Criterion Evaluability Map** -- terminal section with four columns (C-NN | Verification
    Artifact | Scan Method | Independence); Independence column must name excluded content
    for every row; every structural criterion must have a row; this is the final section of
    the emitted document

STOP CONDITION -- Phase 9: Emit is incomplete if section 11 is absent, if any row has a
blank cell, or if the Independence column states "independently verifiable" without naming
the excluded content. A terminal section with three columns (no Independence) fails the
STOP condition.

---

## V-04 -- Role Sequence + Lifecycle Emphasis + Inertia Framing

**Axis:** Combined -- ROLE: EVALUABILITY AUDITOR with named exit gate (role sequence for
C-45) + Phase 9 PREREQUISITE quoting the EVALUABILITY GATE identifier verbatim (C-45
target) + NON-REDUNDANCY DECLARATION co-located in the ROLE: EVALUABILITY AUDITOR gate
body with per-mechanism failure-mode arguments (lifecycle for C-46) + EVALUABILITY
ARCHITECTURE COMPETITOR before Phase 9 naming Architecture A and Architecture B failure
modes (inertia for C-46). All three single-axis mechanisms combined; C-45 and C-46
simultaneously targeted on top of C-43/C-44 baseline.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-04 will contain: (a) a ROLE: EVALUABILITY AUDITOR producing the EVALUABILITY GATE with all four columns populated including Independence with named excluded content; AND (b) a Phase 9 PREREQUISITE line quoting the EVALUABILITY GATE identifier verbatim before the emit manifest; AND (c) a NON-REDUNDANCY DECLARATION in the gate body with two mechanism-necessity arguments; AND (d) an EVALUABILITY ARCHITECTURE COMPETITOR before Phase 9 naming Architecture A and Architecture B -- any output lacking the verbatim PREREQUISITE, or with a non-redundancy claim that lacks per-mechanism failure-mode arguments, partially satisfies C-45 or C-46 respectively. | The EVALUABILITY ARCHITECTURE COMPETITOR and the NON-REDUNDANCY DECLARATION both target C-46 by different mechanisms (negative-example vs positive-declaration); if V-04 achieves C-46 PASS while V-03 achieves only C-46 PARTIAL, the NON-REDUNDANCY DECLARATION is the load-bearing mechanism for full C-46, confirming that the positive "independently necessary" framing is required and the inertia competitor contributes but does not suffice alone. | V-01 is the primary C-46 ablation control for V-04 (V-01 has verbatim PREREQUISITE without non-redundancy declaration); V-02 is the primary C-45 ablation control (V-02 has non-redundancy declaration without verbatim PREREQUISITE); V-03 is the C-46 partial control (inertia framing without positive declaration). |

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
Rewrite if output exceeds the two templates.

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

STOP: Missing gate/rule identifiers -> rewrite. Competitor in prohibited zone -> move.

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

### ROLE: EVALUABILITY AUDITOR

**This role runs after Phase 8. Do not begin Phase 9 until this role's exit gate is
satisfied.**

**Exit gate: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.**

**NON-REDUNDANCY DECLARATION (state before completing gate rows):**

Before reading any structural criteria, produce the following architectural declaration:

```
NON-REDUNDANCY DECLARATION:
The EVALUABILITY GATE (produced by this role) and the Phase 9 terminal CRITERION
EVALUABILITY MAP are non-redundant enforcement points. Each is independently necessary:

Gate necessity: This role enforces the Independence column (C-44) as a pre-Phase-9
structural condition. A Phase 9 terminal table instruction specifies the column requirement
but does not block Phase 9 entry on Independence completion -- without this gate, a model
proceeds to Phase 9 and may emit a terminal table without the Independence column populated.
Architecture A (gate-only, without terminal table): fails C-43 because the EVALUABILITY
GATE output is a construction record that does not appear as a named terminal section in
the emitted rubric document.

Terminal table necessity: The Phase 9 CRITERION EVALUABILITY MAP instruction enforces
terminal-section position (C-43) at emit-close. Without the terminal table instruction,
the gate output remains in the construction record and is never reproduced in the emitted
document. Architecture B (terminal-table-only, without this gate): fails C-44 because the
terminal table can be emitted without the Independence column if no pre-Phase-9 gate
required its completion.

Non-redundancy verified: removing the gate causes C-44 to fail; removing the terminal table
causes C-43 to fail; the combination is required for both to pass.
```

STOP CONDITION: Do not proceed to gate rows until the NON-REDUNDANCY DECLARATION is produced
with both gate-necessity and terminal-table-necessity arguments present. A role that reads
criteria without first producing this declaration does not satisfy ROLE: EVALUABILITY AUDITOR.

After stating the NON-REDUNDANCY DECLARATION, read all structural criteria and produce:

```
EVALUABILITY GATE -- Criterion Evaluability Map:
| C-NN | Verification Artifact | Scan Method | Independence |
|------|-----------------------|-------------|--------------|
| C-01 | [named section or field in emitted rubric] | [specific check] | Yes -- independently verifiable without reading [named excluded content] |
```

Column requirements:
- **Verification Artifact**: specific named section or field. Not a Pass-field paraphrase.
- **Scan Method**: specific action. Generic descriptions are not acceptable.
- **Independence**: "Yes -- independently verifiable without reading [excluded content]"
  naming the specific construction records or role instruction bodies excluded. Omitting the
  exclusion name fails this column.

STOP CONDITION -- ROLE: EVALUABILITY AUDITOR: Gate not satisfied until NON-REDUNDANCY
DECLARATION is stated AND every row has all three cells populated in the required form.

**EVALUABILITY GATE is satisfied when:** NON-REDUNDANCY DECLARATION stated with both
mechanism-necessity arguments AND all rows populated with Verification Artifact, Scan
Method, and Independence naming excluded content.

---

### EVALUABILITY ARCHITECTURE COMPETITOR

```
EVALUABILITY ARCHITECTURE COMPETITOR:

Architecture A -- Gate-only: enforces Independence as a pre-Phase-9 construction condition;
the emitted document has no terminal evaluability section. Fails C-43 because the emitted
document contains no criterion-to-artifact mapping as a terminal section.

Architecture B -- Terminal-table-only: Phase 9 closes with a terminal CRITERION EVALUABILITY
MAP table with Verification Artifact and Scan Method columns but no Independence column; no
pre-Phase-9 gate was required. Fails C-44 because no mechanism enforced Independence
completion before Phase 9 began.

The combined approach is non-redundant: gate enforces C-44 pre-Phase-9; terminal table
enforces C-43 at emit-close. Each mechanism closes the failure mode that the other leaves
open.

Derive the combined approach before reading the required mechanism below.

REQUIRED MECHANISM: ROLE: EVALUABILITY AUDITOR produces the EVALUABILITY GATE with all four
columns; Phase 9 PREREQUISITE quotes the EVALUABILITY GATE identifier verbatim; Phase 9
terminal section reproduces the gate output with all four columns.
```

---

### PHASE 9 -- EMIT

**PREREQUISITE: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.**

This phase's entry is gated on the EVALUABILITY GATE identifier above. If ROLE: EVALUABILITY
AUDITOR has not satisfied the EVALUABILITY GATE, Phase 9 cannot begin.

Output the complete rubric document with sections in this order:

1. **Failure Mode Log**
2. **Design Rationale** -- self-application; >= 3 rejected generic criteria; EVALUABILITY
   ARCHITECTURE COMPETITOR embedded in this section to name the Architecture A / Architecture
   B gap the terminal CRITERION EVALUABILITY MAP closes
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
    Artifact, Scan Method, Independence) must be present; the NON-REDUNDANCY DECLARATION is
    a construction-record artifact and need not appear in the emitted document

STOP CONDITION -- Phase 9: Emit is incomplete until section 11 is present as the final
section with all four columns populated for every structural criterion. A terminal section
missing the Independence column or with generic Independence cells is incomplete.

---

## V-05 -- Role Sequence + Lifecycle Emphasis + Inertia Framing + Phrasing Register

**Axis:** V-04 mechanisms plus a phrasing register layer: (1) Phase 9 PREREQUISITE includes
an explicit independent-auditability clause stating the purpose of the verbatim gate-ID
quote; (2) the NON-REDUNDANCY DECLARATION uses Architecture A and Architecture B as named
failure-experiment labels, making the per-mechanism failure-mode claims independently
verifiable by label; (3) both the gate-ID verbatim text and the independent-auditability
clause appear in the Phase 9 PREREQUISITE as a unified statement. Tests whether making the
independent-auditability property explicit adds measurable C-45 scoring value beyond V-04's
verbatim-but-unexplained PREREQUISITE.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-05 will contain a Phase 9 PREREQUISITE that includes both (a) the EVALUABILITY GATE identifier verbatim and (b) an explicit independent-auditability clause stating that the PREREQUISITE is auditable from Phase 9's header alone without reading ROLE: EVALUABILITY AUDITOR; any output where the PREREQUISITE contains the verbatim gate-ID but omits the independent-auditability clause partially satisfies C-45 but does not achieve the additional scoring value V-05 targets above V-04. | The NON-REDUNDANCY DECLARATION in V-05 uses Architecture A / Architecture B as named labeled references; outputs from V-05 will show the failure-experiment labels in the declaration rather than described-inline failure modes; if V-05 achieves higher C-46 scores than V-04 (which has inline descriptions without labels), the named-label architecture provides additional C-46 scoring value by making the per-mechanism failure claims independently verifiable by label-lookup. | V-04 is the primary isolation control: V-04 has verbatim PREREQUISITE without the independent-auditability clause, and NON-REDUNDANCY DECLARATION with inline failure modes without Architecture labels; comparing V-04 and V-05 isolates whether the auditability clause + label architecture add measurable scoring value; prediction: V-05 achieves the same C-45 PASS and C-46 PASS as V-04, but may increase partial-credit margin within the PASS band. |

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

Five fields per criterion. Templates applied. Competitor immediately before criterion. No
bare qualitative observables.

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

**Exit gate: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row.**

**NON-REDUNDANCY DECLARATION (state before completing gate rows):**

```
NON-REDUNDANCY DECLARATION:
The EVALUABILITY GATE (this role) and the Phase 9 terminal CRITERION EVALUABILITY MAP are
non-redundant enforcement points. Each is independently necessary:

Architecture A -- Gate-only failure: a rubric skill with this role's EVALUABILITY GATE but
no Phase 9 terminal table instruction. The gate is satisfied; the Criterion Evaluability
Map exists in the construction record. Phase 9 emits a document ending with vN Candidates.
The emitted document has no terminal evaluability section. Architecture A fails C-43 because
the emitted rubric document contains no terminal section mapping each criterion to its
verification artifact -- the criterion-to-artifact map is in the construction record only.

Architecture B -- Terminal-table-only failure: a rubric skill with a Phase 9 terminal
CRITERION EVALUABILITY MAP instruction (C-NN | Verification Artifact | Scan Method columns)
but no pre-Phase-9 role enforcing the Independence column. Phase 9 emits a terminal table.
The table has three columns. Architecture B fails C-44 because no mechanism required the
Independence column to be populated before Phase 9 began -- the terminal table instruction
specifies columns but does not block Phase 9 entry on their completion.

Gate necessity: removing the gate and keeping only the terminal table (Architecture B) fails
C-44. The gate is independently necessary because it enforces Independence as a pre-Phase-9
structural condition that the terminal table instruction alone cannot enforce.

Terminal table necessity: removing the terminal table and keeping only the gate (Architecture
A) fails C-43. The terminal table is independently necessary because it places the
criterion-to-artifact map in the emitted document as a final section -- the gate alone
produces a construction record.

Non-redundancy verified by Architecture A and Architecture B: removing either mechanism
causes exactly one criterion (C-43 or C-44) to fail. The combination cannot be reduced.
```

STOP CONDITION: Do not begin reading structural criteria until the NON-REDUNDANCY
DECLARATION is produced with Architecture A label, Architecture B label, gate-necessity
argument, and terminal-table-necessity argument all present. A declaration that describes
failure modes without the Architecture A / Architecture B label structure does not satisfy
V-05's independent-verifiability requirement.

After stating the NON-REDUNDANCY DECLARATION, read all structural criteria and produce:

```
EVALUABILITY GATE -- Criterion Evaluability Map:
| C-NN | Verification Artifact | Scan Method | Independence |
|------|-----------------------|-------------|--------------|
| C-01 | [named section or field in emitted rubric] | [specific check: scan for token X / count Y / confirm structure Z] | Yes -- independently verifiable without reading [named excluded content] |
```

Column requirements:
- **Verification Artifact**: specific named section or field. Not a Pass-field paraphrase.
- **Scan Method**: specific action an evaluator takes. Generic checks are not acceptable.
- **Independence**: "Yes -- independently verifiable without reading [excluded content]"
  naming the specific construction records or role instruction bodies excluded from the
  verification path. Omitting the exclusion name fails this column.

STOP CONDITION -- ROLE: EVALUABILITY AUDITOR: Gate not satisfied until NON-REDUNDANCY
DECLARATION (with Architecture A + Architecture B labels) is stated AND every row has all
three cells populated in the required form.

**EVALUABILITY GATE is satisfied when:** NON-REDUNDANCY DECLARATION with Architecture A/B
labels AND all rows populated with specific Verification Artifact, Scan Method, and
Independence naming excluded content.

---

### EVALUABILITY ARCHITECTURE COMPETITOR

```
EVALUABILITY ARCHITECTURE COMPETITOR:

Architecture A (gate-only): ROLE: EVALUABILITY AUDITOR produces the gate; Phase 9 emit
ends with vN Candidates; no terminal evaluability section in emitted document. Fails C-43.

Architecture B (terminal-table-only): Phase 9 closes with three-column CRITERION
EVALUABILITY MAP (no Independence column); no pre-Phase-9 gate. Fails C-44.

Architecture A and Architecture B have distinct, non-overlapping failure modes. The
combined approach is non-redundant: each enforcement point closes the failure mode the
other leaves open. Architecture A and Architecture B are the named failure experiments
that verify the non-redundancy claim in the NON-REDUNDANCY DECLARATION.

Derive the combined approach before reading the required mechanism below.

REQUIRED MECHANISM: This role produces the EVALUABILITY GATE with all four columns. Phase 9
PREREQUISITE quotes the EVALUABILITY GATE identifier verbatim and states that the
PREREQUISITE is independently auditable from Phase 9's header without reading this role's
body. Phase 9 terminal section reproduces the gate output with all four columns.
```

---

### PHASE 9 -- EMIT

**PREREQUISITE: EVALUABILITY GATE: Criterion Evaluability Map with all structural criterion
rows populated, Verification Artifact named for every row, Scan Method named for every row,
and Independence field naming excluded content for every row. An evaluator auditing
evaluability sequencing can confirm this PREREQUISITE was satisfied by reading Phase 9's
header alone, without reading ROLE: EVALUABILITY AUDITOR's body.**

This phase's entry is gated on the EVALUABILITY GATE identifier above. If ROLE: EVALUABILITY
AUDITOR has not satisfied the EVALUABILITY GATE, Phase 9 cannot begin. The PREREQUISITE is
independently auditable: reading "EVALUABILITY GATE: Criterion Evaluability Map with all
structural criterion rows populated..." in this header is sufficient to confirm the gate
requirement without navigating to ROLE: EVALUABILITY AUDITOR's instructions.

Output the complete rubric document with sections in this order:

1. **Failure Mode Log**
2. **Design Rationale** -- self-application; >= 3 rejected generic criteria; EVALUABILITY
   ARCHITECTURE COMPETITOR embedded in this section referencing Architecture A and
   Architecture B as named failure-experiment labels
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
    must be traceable from this section to ROLE: EVALUABILITY AUDITOR's header; the
    NON-REDUNDANCY DECLARATION is a construction-record artifact

An evaluator reading only section 11 (Criterion Evaluability Map) must be able to confirm
three properties for every structural criterion: (a) named verification artifact is a
specific section or field in this document, (b) scan method names a concrete check, (c)
independence guarantee names the excluded instruction content -- all three properties
independently verifiable without reading role instruction bodies.

STOP CONDITION -- Phase 9: Emit is incomplete until section 11 is present as the final
section, the EVALUABILITY GATE identifier appears verbatim in this phase's PREREQUISITE
header, the map contains one row per structural criterion with all four columns populated,
and the Independence column names excluded content for every row.

---

## Set-Level Design Notes

**Axis coverage:** Five distinct axis families across V-01--V-05: role sequence (ROLE:
EVALUABILITY AUDITOR with named exit gate; Phase 9 PREREQUISITE quotes gate-ID verbatim),
lifecycle emphasis (Phase 8.5 NON-REDUNDANCY DECLARATION with per-mechanism failure-mode
arguments co-located at gate), inertia framing (EVALUABILITY ARCHITECTURE COMPETITOR naming
Architecture A and Architecture B as distinct failed patterns), combined (all three single
axes), phrasing register (explicit independent-auditability clause in PREREQUISITE;
Architecture A/B labels in NON-REDUNDANCY DECLARATION).

**C-45 coverage:** V-01 (very strong, single-axis -- verbatim PREREQUISITE, no non-redundancy
declaration), V-04 (very strong, combined -- verbatim PREREQUISITE + non-redundancy +
inertia), V-05 (very strong + phrasing register -- verbatim PREREQUISITE with explicit
independent-auditability clause). V-02 (ablated -- descriptive prose gate requirement, no
verbatim PREREQUISITE) and V-03 (ablated -- no PREREQUISITE line at Phase 9 entry) are
isolation controls confirming the verbatim gate-ID quote is load-bearing for C-45.

**C-46 coverage:** V-02 (very strong, single-axis -- positive NON-REDUNDANCY DECLARATION
with per-mechanism failure-mode arguments, no verbatim PREREQUISITE), V-04 (very strong,
combined -- NON-REDUNDANCY DECLARATION + inertia competitor), V-05 (very strong +
Architecture A/B labels in declaration). V-01 (ablated -- no non-redundancy declaration)
and V-03 (partial -- inertia competitor names failure modes without positive declaration)
are ablation and partial controls confirming positive "independently necessary" declaration
is load-bearing for C-46 and inertia competitor alone is insufficient.

**C-43/C-44 retention:** All five variations satisfy the C-43/C-44 baseline (from R14): the
terminal CRITERION EVALUABILITY MAP with all four columns is required in all variations; the
Independence column naming excluded content is present in all variations.

**Ablation map:**

| | C-45 | C-46 | C-43 | C-44 |
|-|------|------|------|------|
| V-01 | Target | Ablated | Retained | Retained |
| V-02 | Ablated | Target | Retained | Retained |
| V-03 | Ablated | Partial | Retained | Retained |
| V-04 | Target | Target | Retained | Retained |
| V-05 | Target + register | Target + labels | Retained | Retained |

**Isolation logic:** C-45 is isolatable by comparing V-01 (verbatim PREREQUISITE, no
non-redundancy) against V-02 (non-redundancy, non-verbatim PREREQUISITE): if V-01 passes
C-45 and V-02 fails C-45, the verbatim quote is confirmed as load-bearing for C-45
independent of C-46 mechanisms. C-46 is isolatable by comparing V-02 (positive declaration,
no inertia) against V-03 (inertia, no positive declaration): if V-02 passes C-46 and V-03
partially passes, the positive "independently necessary" framing is the C-46 load-bearing
mechanism. V-05 vs V-04 isolates the phrasing register contribution.
