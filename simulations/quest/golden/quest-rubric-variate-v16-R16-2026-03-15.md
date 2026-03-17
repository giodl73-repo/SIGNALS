# quest-rubric Variate -- Round 16 (Against rubric v16, targeting C-47/C-48)

**Date:** 2026-03-15
**Rubric:** v16 (C-01--C-48; denominator /40; adds C-47: non-redundancy failure-mode
arguments employ Architecture-labeled experiment anchors with STOP-condition enforcement,
each label resolving to a named competitor entry in the EVALUABILITY ARCHITECTURE COMPETITOR
section, enabling failure-mode verification by label-lookup without re-reading inline prose
arguments; C-48: emit-phase verbatim gate-ID PREREQUISITE includes an explicit auditability
boundary declaration co-located with the gate-ID quote, naming the specific role body
excluded from sequencing verification)
**Target criteria:** C-47, C-48

**Round 16 design note:** Round 15 produced excellence signals ES-R15-1 and ES-R15-2 from
V-05. V-05 passed both C-47 and C-48 (the two new aspirational criteria added to rubric v16).
V-04 passed C-45 (verbatim gate-ID in Phase 9 PREREQUISITE) and C-46 (NON-REDUNDANCY
DECLARATION with per-mechanism failure-mode arguments) but failed C-47 (NON-REDUNDANCY
DECLARATION used inline prose arguments without Architecture labels and without STOP-condition
enforcement) and C-48 (Phase 9 PREREQUISITE quoted gate-ID verbatim per C-45 but had no
independence boundary declaration naming the excluded role body). Rubric v16 elevates both
C-47 and C-48 as aspirational criteria, extending the denominator from /38 to /40. R16
targets: (1) isolate whether Phase 9 PREREQUISITE with verbatim gate-ID plus co-located
independence boundary declaration naming ROLE: EVALUABILITY AUDITOR achieves C-48 without
Architecture-labeled NON-REDUNDANCY anchors; (2) isolate whether Architecture A/B labeled
NON-REDUNDANCY DECLARATION with STOP-condition enforcement and resolved EVALUABILITY
ARCHITECTURE COMPETITOR entries achieves C-47 without the independence boundary in Phase 9;
(3) test whether Architecture A/B labels in a competitor block without STOP conditions
achieves C-47 via negative-example architecture without the positive enforcement requirement;
(4) combine all three single-axis mechanisms; (5) add phrasing register to the combined
stack with explicit auditability purpose clauses.

**C-47 vs C-48 -- distinction summary for variation design:**

- C-47 governs the *NON-REDUNDANCY DECLARATION's proof architecture*: the declaration must
  not use inline prose arguments alone. Instead, it must name Architecture-labeled experiment
  anchors (Architecture A, Architecture B) with co-located STOP-condition enforcement, where
  each label resolves to a named entry in the EVALUABILITY ARCHITECTURE COMPETITOR section.
  The STOP condition converts the label structure from a stylistic choice into a structural
  requirement: "STOP: if Architecture A does not resolve to a named entry in the EVALUABILITY
  ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY DECLARATION is incomplete." A
  NON-REDUNDANCY DECLARATION with prose failure-mode arguments ("Removing the gate causes the
  Independence column to be unverified") does not satisfy C-47; only a declaration with
  Architecture A/B labels, STOP enforcement per label, and an EVALUABILITY ARCHITECTURE
  COMPETITOR section containing entries for each label satisfies C-47. V-01 (prose-only
  NON-REDUNDANCY) is the primary C-47 ablation control.

- C-48 governs the *Phase 9 PREREQUISITE's independence boundary*: the PREREQUISITE must
  not only quote the EVALUABILITY GATE identifier verbatim (C-45 requirement) but must also
  include a co-located independence boundary declaration naming the specific role body
  excluded from sequencing verification. "This PREREQUISITE names ROLE: EVALUABILITY AUDITOR
  as the role body excluded from Phase 9 sequencing verification: a reader can confirm that
  Phase 9 was properly gated by reading this PREREQUISITE alone, without reading the body of
  ROLE: EVALUABILITY AUDITOR." A Phase 9 PREREQUISITE that quotes the gate-ID verbatim
  without the independence boundary declaration satisfies C-45 but not C-48. V-02 (verbatim
  PREREQUISITE, no independence boundary) is the primary C-48 ablation control.

---

## Axis Selection

| Axis | Criterion targeted | Mechanism |
|------|--------------------|-----------|
| Role sequence | C-48 | ROLE: EVALUABILITY AUDITOR with named exit gate; Phase 9 PREREQUISITE quotes gate-ID verbatim AND adds co-located independence boundary declaration naming "ROLE: EVALUABILITY AUDITOR" as excluded content; C-47 ablated (Phase 8.5 NON-REDUNDANCY DECLARATION uses prose-only arguments, no Architecture labels, no STOP enforcement) |
| Lifecycle emphasis | C-47 | EVALUABILITY ARCHITECTURE COMPETITOR section before Phase 8.5; Phase 8.5 NON-REDUNDANCY DECLARATION uses Architecture A/B labeled experiment anchors with co-located STOP-condition enforcement; each label resolves to a named entry in the EVALUABILITY ARCHITECTURE COMPETITOR section; C-48 ablated (Phase 9 PREREQUISITE quotes gate-ID verbatim per C-45 but has no independence boundary declaration) |
| Inertia framing | C-47 partial | EVALUABILITY ARCHITECTURE COMPETITOR section uses Architecture A/B labels; Phase 8.5 NON-REDUNDANCY DECLARATION references Architecture A/B labels but has no STOP-condition enforcement; C-45 ablated (Phase 9 PREREQUISITE describes gate requirement in prose without verbatim gate-ID quote) |
| (combined) | C-47 + C-48 | Role sequence (C-48) + Lifecycle emphasis (C-47) combined; Phase 9 PREREQUISITE: verbatim gate-ID + independence boundary; Phase 8.5: Architecture A/B labels + STOP enforcement + EVALUABILITY ARCHITECTURE COMPETITOR section |
| Role sequence + Phrasing register | C-47 + C-48 + explicit auditability | V-04 mechanisms + Phase 9 PREREQUISITE adds explicit purpose clause ("making evaluability sequencing independently auditable from Phase 9 entry alone, without reading ROLE: EVALUABILITY AUDITOR's construction instructions") + NON-REDUNDANCY DECLARATION adds explicit verifier-guidance clause ("Architecture A and B are named experiment anchors, each resolving to a specific entry in the EVALUABILITY ARCHITECTURE COMPETITOR section above, enabling verification by label-lookup without re-reading inline prose") |

Single-axis: V-01 (role sequence), V-02 (lifecycle emphasis), V-03 (inertia framing).
Combined: V-04 (three single axes), V-05 (three single axes + phrasing register).

---

## Round 16 Variation Map

| Variation | Axis | C-47 probe | C-48 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Role sequence | Ablated -- Phase 8.5 NON-REDUNDANCY uses prose-only arguments; no Architecture labels; no STOP enforcement; no EVALUABILITY ARCHITECTURE COMPETITOR section | Very strong -- Phase 9 PREREQUISITE quotes gate-ID verbatim (C-45 satisfied) AND includes co-located independence boundary declaration naming ROLE: EVALUABILITY AUDITOR as excluded content (C-48 mechanism) | Single-axis; isolates whether independence boundary declaration in Phase 9 PREREQUISITE alone achieves C-48 without Architecture-labeled NON-REDUNDANCY; prediction: V-01 passes C-48, fails C-47 |
| V-02 | Lifecycle emphasis | Very strong -- EVALUABILITY ARCHITECTURE COMPETITOR section with named Architecture A/B entries; Phase 8.5 NON-REDUNDANCY uses Architecture A/B labels with co-located STOP conditions per label; each label resolves to named competitor entry | Ablated -- Phase 9 PREREQUISITE quotes gate-ID verbatim (C-45 satisfied) but has no independence boundary declaration; no naming of excluded role body | Single-axis; isolates whether Architecture-labeled NON-REDUNDANCY with STOP enforcement achieves C-47 without independence boundary in Phase 9; prediction: V-02 passes C-47, fails C-48 |
| V-03 | Inertia framing | Partial -- EVALUABILITY ARCHITECTURE COMPETITOR section uses Architecture A/B labels; Phase 8.5 NON-REDUNDANCY references the labels without STOP enforcement; hypothesis: labels without STOP do not satisfy C-47 | Ablated -- Phase 9 PREREQUISITE is a prose gate-completion requirement without verbatim gate-ID quote; C-45 ablated, C-48 ablated | Single-axis ablation control; tests whether Architecture labels without STOP-condition enforcement achieve C-47; prediction: V-03 fails C-47 (STOP is load-bearing) and fails C-48 |
| V-04 | Role sequence + Lifecycle emphasis + Inertia framing | Very strong -- same as V-02: EVALUABILITY ARCHITECTURE COMPETITOR + Architecture A/B labels + co-located STOP conditions in NON-REDUNDANCY | Very strong -- same as V-01: verbatim gate-ID + co-located independence boundary declaration naming ROLE: EVALUABILITY AUDITOR | Combined; tests whether C-47 and C-48 simultaneously pass on top of C-45/C-46 baseline; prediction: V-04 passes both |
| V-05 | Role sequence + Lifecycle emphasis + Inertia framing + Phrasing register | Very strong (same as V-04) + NON-REDUNDANCY adds explicit verifier-guidance clause naming the label-lookup verification path | Very strong (same as V-04) + Phase 9 PREREQUISITE adds explicit auditability-purpose clause naming the independence guarantee mechanism | V-04 mechanisms + phrasing register; tests whether explicit purpose declarations add measurable C-47/C-48 scoring value vs V-04's implicit mechanism; prediction: V-05 passes C-47 and C-48 with higher criterion expression density |

---

## V-01 -- Role Sequence

**Axis:** Role sequence -- ROLE: EVALUABILITY AUDITOR with named exit gate. Phase 9 opens
with a PREREQUISITE that (1) quotes the EVALUABILITY GATE identifier verbatim (satisfying
C-45) AND (2) adds a co-located independence boundary declaration naming ROLE: EVALUABILITY
AUDITOR as the role body excluded from Phase 9 sequencing verification (C-48 mechanism).
C-47 is ablated: Phase 8.5 NON-REDUNDANCY DECLARATION uses prose-only arguments without
Architecture labels and without STOP-condition enforcement.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-01 will contain a Phase 9 that opens with a PREREQUISITE line that (a) quotes the EVALUABILITY GATE identifier verbatim and (b) includes a co-located sentence naming ROLE: EVALUABILITY AUDITOR as the excluded role body -- any output where the PREREQUISITE is present but lacks the independence boundary sentence, or where the independence boundary names a different role body, falsifies the C-48 hypothesis. | The independence boundary declaration makes Phase 9's gate-adherence independently auditable from Phase 9's entry alone: a reader sees not just "this gate was required" (C-45) but "this gate was implemented by ROLE: EVALUABILITY AUDITOR, which you do not need to read to confirm gating" (C-48); outputs from V-01 will show a two-sentence PREREQUISITE structure (verbatim gate-ID sentence + independence boundary sentence) vs V-02 outputs which show a one-sentence PREREQUISITE (verbatim gate-ID only). | V-02 is the primary C-48 ablation control: V-02 has a verbatim Phase 9 PREREQUISITE (passes C-45) but no independence boundary declaration (fails C-48); comparing PREREQUISITE structure across V-01 (two-sentence: gate-ID + independence boundary) and V-02 (one-sentence: gate-ID only) isolates whether the independence boundary -- not just the verbatim quote -- is load-bearing for C-48; prediction: V-01 passes C-48, V-02 fails C-48. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

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

### PHASE 8.5 -- NON-REDUNDANCY DECLARATION

The EVALUABILITY GATE (Phase 8) and the Phase 9 terminal Criterion Evaluability Map are
non-redundant enforcement points. Each is independently necessary:

- Removing the EVALUABILITY GATE causes the Independence column to be unverified before
  emit: the Phase 9 terminal table may have generic or absent Independence fields, failing
  C-44.
- Removing the Phase 9 terminal Criterion Evaluability Map causes the verified map to remain
  in the construction record only: the emitted artifact has no terminal evaluability section,
  failing C-43.

NON-REDUNDANCY DECLARATION: Each enforcement point governs a distinct failure mode. Neither
can substitute for the other. Both are required.

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
- **Independence**: "Yes -- independently verifiable without reading [named excluded content]"
  where [named excluded content] names the specific construction records, role instruction
  bodies, or phase outputs that a verifier can skip. "Yes -- independently verifiable"
  without the exclusion name fails this column.

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
and Independence field naming excluded content for every row.
This PREREQUISITE names ROLE: EVALUABILITY AUDITOR as the role body excluded from Phase 9
sequencing verification: a reader can confirm that Phase 9 was properly gated by reading
this PREREQUISITE line alone, without reading the body of ROLE: EVALUABILITY AUDITOR.**

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

---

## V-02 -- Lifecycle Emphasis

**Axis:** Lifecycle emphasis -- the EVALUABILITY ARCHITECTURE COMPETITOR section appears
before Phase 8.5 and names Architecture A and Architecture B as distinct labeled entries.
Phase 8.5 NON-REDUNDANCY DECLARATION uses Architecture A/B labels as experiment anchors with
co-located STOP-condition enforcement; each label resolves to its named entry in the
EVALUABILITY ARCHITECTURE COMPETITOR section (C-47 full). C-48 is ablated: Phase 9
PREREQUISITE quotes the EVALUABILITY GATE identifier verbatim (satisfying C-45) but has no
independence boundary declaration naming the excluded role body.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every rubric output produced from V-02 will contain a Phase 8.5 NON-REDUNDANCY DECLARATION with Architecture A and Architecture B labels, each followed by a STOP condition that enforces label resolution against the EVALUABILITY ARCHITECTURE COMPETITOR section -- any output where the NON-REDUNDANCY DECLARATION uses inline prose arguments without Architecture labels, or where the STOP conditions are absent, falsifies the C-47 hypothesis. | The Architecture-labeled + STOP-enforced NON-REDUNDANCY DECLARATION makes failure-mode necessity arguments verifiable by label-lookup: a reader who doubts "Architecture A fails C-43" can look up Architecture A in the EVALUABILITY ARCHITECTURE COMPETITOR section and confirm the failure mode without re-reading the NON-REDUNDANCY DECLARATION prose; outputs from V-02 will show a two-section architecture (EVALUABILITY ARCHITECTURE COMPETITOR section + Phase 8.5 referencing it by label) vs V-01 outputs which show only a prose Phase 8.5 with no competitor section. | V-01 is the primary C-47 ablation control: V-01 has a prose NON-REDUNDANCY DECLARATION (fails C-47); V-03 has Architecture labels without STOP conditions (tests whether labels alone satisfy C-47); comparing C-47 scores across V-01 (no labels), V-02 (labels + STOP), and V-03 (labels, no STOP) isolates whether STOP enforcement -- not just labeling -- is load-bearing for C-47; prediction: V-02 passes C-47, V-01 fails C-47, V-03 fails C-47. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

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

### EVALUABILITY ARCHITECTURE COMPETITOR

Architecture A (gate-only): A skill prompt that runs ROLE: EVALUABILITY AUDITOR and produces
a Criterion Evaluability Map in the construction record but does not require Phase 9 to
include the map as a terminal section in the emitted artifact. Phase 9 omits the Criterion
Evaluability Map entirely, or includes it as an optional annotation rather than a required
terminal section. Architecture A fails C-43: the terminal evaluability section is absent from
the emitted artifact, so a downstream evaluator cannot verify criterion evaluability from the
artifact alone without reading the construction record.

Architecture B (terminal-table-only): A skill prompt that requires Phase 9 to output a
Criterion Evaluability Map as a terminal section but does not run ROLE: EVALUABILITY AUDITOR
as a pre-Phase-9 gate. The emit section produces the table, but the Independence field is
populated by the emit phase rather than verified by a dedicated auditor role before emit.
Architecture B fails C-44: the Independence field naming excluded content is never
independently verified pre-emit, so generic or absent Independence declarations pass through
to the artifact undetected.

---

### PHASE 8.5 -- NON-REDUNDANCY DECLARATION

The EVALUABILITY GATE (Phase 8) and the Phase 9 terminal Criterion Evaluability Map are
non-redundant enforcement points. Each is independently necessary:

- Architecture A (gate-only, no terminal map): fails C-43 -- the Criterion Evaluability Map
  remains in the construction record only; the emitted artifact has no terminal evaluability
  section. See Architecture A in EVALUABILITY ARCHITECTURE COMPETITOR above.
  STOP: if the Architecture A label above does not resolve to a named entry in the
  EVALUABILITY ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY DECLARATION is incomplete.
  Do not proceed to ROLE: EVALUABILITY AUDITOR until Architecture A resolves.

- Architecture B (terminal-table-only, no gate): fails C-44 -- the Independence field is
  populated by the emit phase without pre-Phase-9 verification; generic Independence
  declarations pass through to the artifact. See Architecture B in EVALUABILITY ARCHITECTURE
  COMPETITOR above.
  STOP: if the Architecture B label above does not resolve to a named entry in the
  EVALUABILITY ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY DECLARATION is incomplete.
  Do not proceed to ROLE: EVALUABILITY AUDITOR until Architecture B resolves.

NON-REDUNDANCY DECLARATION: Architecture A fails C-43; Architecture B fails C-44. Both
enforcement points are independently necessary. Neither can substitute for the other.

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
- **Independence**: "Yes -- independently verifiable without reading [named excluded content]"
  where [named excluded content] names the specific construction records, role instruction
  bodies, or phase outputs that a verifier can skip. "Yes -- independently verifiable"
  without the exclusion name fails this column.

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

---

## V-03 -- Inertia Framing

**Axis:** Inertia framing -- the EVALUABILITY ARCHITECTURE COMPETITOR section uses
Architecture A/B labels as named entries. Phase 8.5 NON-REDUNDANCY DECLARATION references
the Architecture A and B labels in its failure-mode arguments but provides no STOP-condition
enforcement per label. Phase 9 PREREQUISITE is a prose gate-completion requirement without
the verbatim EVALUABILITY GATE identifier (C-45 ablated, C-48 ablated). Hypothesis: labels
without STOP enforcement do not satisfy C-47; the STOP conditions are load-bearing for C-47,
not merely stylistic.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| V-03 will produce a Phase 8.5 with Architecture A/B labels present in the NON-REDUNDANCY DECLARATION but no STOP conditions enforcing label resolution against the EVALUABILITY ARCHITECTURE COMPETITOR section -- if outputs from V-03 fail C-47 while V-02 outputs pass, this confirms that STOP-condition enforcement (not merely Architecture labeling) is the load-bearing mechanism for C-47; if V-03 outputs pass C-47, Architecture labels without STOP are sufficient and C-47's STOP requirement is over-specified. | V-03 and V-01 are co-ablation controls for C-47: V-01 has no Architecture labels (pure prose NON-REDUNDANCY), V-03 has Architecture labels but no STOP conditions, V-02 has Architecture labels with STOP enforcement; the three-way comparison isolates the contribution of the STOP mechanism independently from the labeling mechanism. | Phase 9 PREREQUISITE in V-03 is a prose description ("confirm the evaluability audit is complete before Phase 9 begins") without the verbatim gate-ID quote -- V-03 outputs should fail C-45 (no verbatim PREREQUISITE) and fail C-48 (no independence boundary); this makes V-03 the joint ablation control for C-45/C-48, confirming the baseline: outputs from V-03 should score 36/40 (fails C-47 and C-48) or 37/40 (if Architecture labels unexpectedly satisfy C-47 despite missing STOP). |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

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

### EVALUABILITY ARCHITECTURE COMPETITOR

Architecture A (gate-only): A skill prompt that runs ROLE: EVALUABILITY AUDITOR and produces
a Criterion Evaluability Map in the construction record but does not require Phase 9 to emit
the map as a terminal section. Architecture A fails C-43: the terminal evaluability section
is absent from the emitted artifact.

Architecture B (terminal-table-only): A skill prompt that outputs a Criterion Evaluability
Map as a Phase 9 terminal section without running ROLE: EVALUABILITY AUDITOR as a pre-Phase-9
gate. Architecture B fails C-44: the Independence field is populated by the emit phase
without pre-Phase-9 verification by a dedicated auditor role.

---

### PHASE 8.5 -- NON-REDUNDANCY DECLARATION

The EVALUABILITY GATE (Phase 8) and the Phase 9 terminal Criterion Evaluability Map are
non-redundant enforcement points. Architecture A (gate-only) fails C-43 because the map
never reaches the emitted artifact. Architecture B (terminal-table-only) fails C-44 because
the Independence field is never independently verified before emit. Each enforcement point
addresses a distinct failure mode; neither can substitute for the other.

NON-REDUNDANCY DECLARATION: Architecture A fails C-43; Architecture B fails C-44. Both
enforcement points are independently necessary.

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
- **Independence**: "Yes -- independently verifiable without reading [named excluded content]"
  where [named excluded content] names the specific construction records, role instruction
  bodies, or phase outputs that a verifier can skip. "Yes -- independently verifiable"
  without the exclusion name fails this column.

STOP CONDITION -- ROLE: EVALUABILITY AUDITOR: The EVALUABILITY GATE is not satisfied until
every row has all three cells populated in the required form. Any blank cell or generic
Independence claim blocks the gate. Do not proceed to Phase 9 until the EVALUABILITY GATE
is satisfied.

**EVALUABILITY GATE is satisfied when:** All rows populated, Verification Artifact and Scan
Method specific and named, Independence field names excluded content for every row.

---

### PHASE 9 -- EMIT

**PREREQUISITE: The evaluability audit must be complete before Phase 9 begins. Confirm that
ROLE: EVALUABILITY AUDITOR has satisfied all column requirements in the Criterion Evaluability
Map before proceeding.**

This phase's entry requires the evaluability audit to be complete. If ROLE: EVALUABILITY
AUDITOR has not produced a fully populated map with all required columns, Phase 9 cannot
begin.

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

---

## V-04 -- Combined (Role Sequence + Lifecycle Emphasis + Inertia Framing)

**Axis:** Combined -- all three single-axis mechanisms from V-01, V-02, V-03 applied
together. EVALUABILITY ARCHITECTURE COMPETITOR section with named Architecture A/B entries
(inertia framing). Phase 8.5 NON-REDUNDANCY DECLARATION with Architecture A/B labels and
co-located STOP-condition enforcement, each label resolving to a named entry in the
EVALUABILITY ARCHITECTURE COMPETITOR section (lifecycle emphasis, C-47 full). Phase 9
PREREQUISITE quotes gate-ID verbatim and includes a co-located independence boundary
declaration naming ROLE: EVALUABILITY AUDITOR as excluded content (role sequence, C-48 full).

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| V-04 will pass both C-47 (Architecture-labeled NON-REDUNDANCY with STOP enforcement resolving to named EVALUABILITY ARCHITECTURE COMPETITOR entries) and C-48 (verbatim Phase 9 PREREQUISITE with co-located independence boundary declaration naming ROLE: EVALUABILITY AUDITOR) -- any output from V-04 that omits either the STOP conditions from Phase 8.5 or the independence boundary from Phase 9's PREREQUISITE falsifies the combination hypothesis. | The combination test validates that C-47 and C-48 mechanisms are non-interfering: having both Architecture-labeled NON-REDUNDANCY and an independence-boundary Phase 9 PREREQUISITE in the same prompt does not cause structural conflicts, redundant declarations, or omission of one mechanism due to the other's presence; V-04 outputs establish the minimum complete prompt architecture that achieves C-45 through C-48 simultaneously. | Comparison with V-05: V-04 provides the C-47/C-48 mechanism combination without explicit phrasing register additions; if V-04 and V-05 score identically on C-47/C-48, then phrasing register adds no differential scoring value and the implicit label-anchor architecture of V-04 is sufficient; if V-05 scores higher, the explicit auditability-purpose clauses are load-bearing for criterion expression density. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

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

### EVALUABILITY ARCHITECTURE COMPETITOR

Architecture A (gate-only): A skill prompt that runs ROLE: EVALUABILITY AUDITOR and produces
a Criterion Evaluability Map in the construction record but does not require Phase 9 to
include the map as a terminal section in the emitted artifact. Phase 9 omits the Criterion
Evaluability Map or includes it as an optional annotation rather than a required terminal
section. Architecture A fails C-43: the terminal evaluability section is absent from the
emitted artifact, so a downstream evaluator cannot verify criterion evaluability from the
artifact alone without reading the construction record.

Architecture B (terminal-table-only): A skill prompt that requires Phase 9 to output a
Criterion Evaluability Map as a terminal section but does not run ROLE: EVALUABILITY AUDITOR
as a pre-Phase-9 gate. The emit section produces the table, but the Independence field is
populated by the emit phase rather than verified by a dedicated auditor role before emit.
Architecture B fails C-44: the Independence field naming excluded content is never
independently verified pre-emit, so generic or absent Independence declarations pass through
to the artifact undetected.

---

### PHASE 8.5 -- NON-REDUNDANCY DECLARATION

The EVALUABILITY GATE (Phase 8) and the Phase 9 terminal Criterion Evaluability Map are
non-redundant enforcement points. Each is independently necessary:

- Architecture A (gate-only, no terminal map): fails C-43 -- the Criterion Evaluability Map
  remains in the construction record only; the emitted artifact has no terminal evaluability
  section. See Architecture A in EVALUABILITY ARCHITECTURE COMPETITOR above.
  STOP: if the Architecture A label above does not resolve to a named entry in the
  EVALUABILITY ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY DECLARATION is incomplete.
  Do not proceed to ROLE: EVALUABILITY AUDITOR until Architecture A resolves.

- Architecture B (terminal-table-only, no gate): fails C-44 -- the Independence field is
  populated by the emit phase without pre-Phase-9 verification; generic Independence
  declarations pass through to the artifact. See Architecture B in EVALUABILITY ARCHITECTURE
  COMPETITOR above.
  STOP: if the Architecture B label above does not resolve to a named entry in the
  EVALUABILITY ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY DECLARATION is incomplete.
  Do not proceed to ROLE: EVALUABILITY AUDITOR until Architecture B resolves.

NON-REDUNDANCY DECLARATION: Architecture A fails C-43; Architecture B fails C-44. Both
enforcement points are independently necessary. Neither can substitute for the other.

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
- **Independence**: "Yes -- independently verifiable without reading [named excluded content]"
  where [named excluded content] names the specific construction records, role instruction
  bodies, or phase outputs that a verifier can skip. "Yes -- independently verifiable"
  without the exclusion name fails this column.

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
and Independence field naming excluded content for every row.
This PREREQUISITE names ROLE: EVALUABILITY AUDITOR as the role body excluded from Phase 9
sequencing verification: a reader can confirm that Phase 9 was properly gated by reading
this PREREQUISITE line alone, without reading the body of ROLE: EVALUABILITY AUDITOR.**

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

---

## V-05 -- Combined + Phrasing Register (Full Integration)

**Axis:** Role sequence + Lifecycle emphasis + Inertia framing + Phrasing register -- V-04
mechanisms with explicit auditability-purpose declarations added at both the NON-REDUNDANCY
DECLARATION and the Phase 9 PREREQUISITE. The NON-REDUNDANCY DECLARATION adds a verifier-
guidance clause explicitly naming the label-lookup path. The Phase 9 PREREQUISITE adds a
third sentence explicitly stating the auditability property that the independence boundary
declaration provides.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| V-05 will pass C-47 and C-48 with higher criterion expression density than V-04: the explicit verifier-guidance clause in NON-REDUNDANCY ("enabling verification by label-lookup without re-reading inline prose") makes the C-47 mechanism self-describing, and the explicit auditability-purpose clause in Phase 9 PREREQUISITE ("making evaluability sequencing independently auditable from Phase 9 entry alone, without reading ROLE: EVALUABILITY AUDITOR's construction instructions") makes the C-48 mechanism self-describing; if scoring on both criteria is binary (PASS/FAIL), V-04 and V-05 score identically and phrasing register adds no differential value; if scoring is graded, V-05 scores higher than V-04 on both criteria. | The explicit purpose clauses in V-05 create a pattern where both mechanisms are independently self-auditable from the declaration site: a reader at Phase 8.5 can verify C-47 compliance from the NON-REDUNDANCY DECLARATION text alone (labels present + STOP present + verifier-guidance clause names the label-lookup path); a reader at Phase 9 entry can verify C-48 compliance from the PREREQUISITE text alone (verbatim gate-ID + independence boundary + purpose clause names the auditability guarantee); this triple-self-declaration pattern at each site is the R16 excellence signal target. | V-04 vs V-05 discrimination site: the PREREQUISITE structure -- V-04 has two sentences (verbatim gate-ID + independence boundary); V-05 has three sentences (verbatim gate-ID + independence boundary + auditability-purpose clause); the NON-REDUNDANCY DECLARATION -- V-04 has Architecture A/B labels + STOP conditions; V-05 has Architecture A/B labels + STOP conditions + explicit verifier-guidance clause; the presence of purpose clauses at both sites, with no other structural differences, isolates whether purpose-clause phrasing adds measurable C-47/C-48 value. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

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

### EVALUABILITY ARCHITECTURE COMPETITOR

Architecture A (gate-only): A skill prompt that runs ROLE: EVALUABILITY AUDITOR and produces
a Criterion Evaluability Map in the construction record but does not require Phase 9 to
include the map as a terminal section in the emitted artifact. Phase 9 omits the Criterion
Evaluability Map or includes it as an optional annotation rather than a required terminal
section. Architecture A fails C-43: the terminal evaluability section is absent from the
emitted artifact, so a downstream evaluator cannot verify criterion evaluability from the
artifact alone without reading the construction record.

Architecture B (terminal-table-only): A skill prompt that requires Phase 9 to output a
Criterion Evaluability Map as a terminal section but does not run ROLE: EVALUABILITY AUDITOR
as a pre-Phase-9 gate. The emit section produces the table, but the Independence field is
populated by the emit phase rather than verified by a dedicated auditor role before emit.
Architecture B fails C-44: the Independence field naming excluded content is never
independently verified pre-emit, so generic or absent Independence declarations pass through
to the artifact undetected.

---

### PHASE 8.5 -- NON-REDUNDANCY DECLARATION

The EVALUABILITY GATE (Phase 8) and the Phase 9 terminal Criterion Evaluability Map are
non-redundant enforcement points. Each is independently necessary:

- Architecture A (gate-only, no terminal map): fails C-43 -- the Criterion Evaluability Map
  remains in the construction record only; the emitted artifact has no terminal evaluability
  section. See Architecture A in EVALUABILITY ARCHITECTURE COMPETITOR above.
  STOP: if the Architecture A label above does not resolve to a named entry in the
  EVALUABILITY ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY DECLARATION is incomplete.
  Do not proceed to ROLE: EVALUABILITY AUDITOR until Architecture A resolves.

- Architecture B (terminal-table-only, no gate): fails C-44 -- the Independence field is
  populated by the emit phase without pre-Phase-9 verification; generic Independence
  declarations pass through to the artifact. See Architecture B in EVALUABILITY ARCHITECTURE
  COMPETITOR above.
  STOP: if the Architecture B label above does not resolve to a named entry in the
  EVALUABILITY ARCHITECTURE COMPETITOR section, the NON-REDUNDANCY DECLARATION is incomplete.
  Do not proceed to ROLE: EVALUABILITY AUDITOR until Architecture B resolves.

NON-REDUNDANCY DECLARATION: Architecture A fails C-43; Architecture B fails C-44. Both
enforcement points are independently necessary. Neither can substitute for the other.
Architecture A and Architecture B are named experiment anchors, each resolving to a specific
entry in the EVALUABILITY ARCHITECTURE COMPETITOR section above, enabling a verifier to
confirm the necessity argument by label-lookup without re-reading the inline prose arguments
in this NON-REDUNDANCY DECLARATION.

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
- **Independence**: "Yes -- independently verifiable without reading [named excluded content]"
  where [named excluded content] names the specific construction records, role instruction
  bodies, or phase outputs that a verifier can skip. "Yes -- independently verifiable"
  without the exclusion name fails this column.

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
and Independence field naming excluded content for every row.
This PREREQUISITE names ROLE: EVALUABILITY AUDITOR as the role body excluded from Phase 9
sequencing verification: a reader can confirm that Phase 9 was properly gated by reading
this PREREQUISITE line alone, without reading the body of ROLE: EVALUABILITY AUDITOR.
The co-located independence boundary declaration makes evaluability sequencing independently
auditable from Phase 9 entry alone, without reading ROLE: EVALUABILITY AUDITOR's construction
instructions.**

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

---

## Predicted Scores (Rubric v16, denominator /40)

Assuming all essential and recommended criteria pass (E=1.0, R=1.0):

| Variation | C-47 prediction | C-48 prediction | Aspirational (/40) | Composite |
|-----------|----------------|----------------|-------------------|-----------|
| V-01 | FAIL -- prose NON-REDUNDANCY, no Architecture labels, no STOP | PASS -- verbatim gate-ID + independence boundary naming ROLE: EVALUABILITY AUDITOR | 39/40 | 99.750 |
| V-02 | PASS -- Architecture A/B labels + STOP enforcement + EVALUABILITY ARCHITECTURE COMPETITOR section | FAIL -- verbatim gate-ID only, no independence boundary | 39/40 | 99.750 |
| V-03 | FAIL -- Architecture A/B labels present but no STOP enforcement | FAIL -- prose PREREQUISITE, no verbatim gate-ID | 38/40 | 99.500 |
| V-04 | PASS -- Architecture A/B labels + STOP + EVALUABILITY ARCHITECTURE COMPETITOR section | PASS -- verbatim gate-ID + independence boundary | 40/40 | 100.000 |
| V-05 | PASS (same as V-04) + explicit verifier-guidance clause | PASS (same as V-04) + explicit auditability-purpose clause | 40/40 | 100.000 |

**R16 spread hypothesis:** V-01 and V-02 score 99.750 (single criterion isolation each),
V-03 scores 99.500 (double ablation control, baseline), V-04 and V-05 score 100.000 (full
combination). V-04 vs V-05 discrimination requires graded C-47/C-48 scoring (PARTIAL for
mechanism-present-without-purpose-clause vs PASS for mechanism-plus-purpose-clause). If
binary, V-04 = V-05. R16 excellence signal target: V-05 explicit purpose clauses elevate
C-47/C-48 expression to the pattern that triggers C-49/C-50 candidate extraction for v17.
