# quest-rubric Variate — Round 12 (Second file: against rubric v12)
**Date:** 2026-03-15
**Rubric:** v12 (C-01--C-36; adds C-35: multi-criterion-closure-efficiency; C-36: competitor-phase-alignment)
**Target criteria:** C-35, C-36

**Round 12 design note:** Round 11 produced mechanisms for C-31 (aspirational tier count bound with operative STOP), C-32 (category diversity STOP before Emit), C-33 (three-state scoring with named earn conditions), and C-34 (independence map with per-entry C-NN citations). Rubric v12 adds two aspirational criteria extracted from Round 11 V-05 excellence signals.

**C-35 vs C-25.** C-25 requires one-to-one mechanism-criterion assignment: each mechanism targets exactly one criterion, each criterion is targeted by exactly one mechanism. It is satisfied by five independent mechanisms closing five criteria (one-to-one, correct). C-35 requires more: a named check for when one structural property independently satisfies >=3 criteria across >=2 criterion clusters -- each criterion is satisfied by the property standing alone, not by a mechanism credited to multiple criteria. Two architectures with identical criterion passes score differently if one achieves coverage through structural economy. The staircase architecture (V-05 Round 11) demonstrated this: the three-competitor design independently closed C-11, C-25, C-27, C-28, and C-30 through a single structural property (each competitor = architecture with one mechanism removed). No criterion from C-01 through C-34 rewards this signal.

**C-36 vs C-27.** C-27 requires the competitor description to constitute the gap specification -- the required function must be derivable from the competitor alone. A competitor can satisfy C-27 while appearing in a shared preamble block at the top of the rubric. C-36 requires phase-local placement: each competitor must appear at the construction boundary where its mechanism is defined -- not recalled from Section 1, but introduced at the phase where its gap is first operationally relevant. A rubric with a preamble block containing all competitors satisfies C-27 (competitor correctly constitutes the gap) while failing C-36 (competitor is not at its operative phase boundary). A rubric with phase-local competitors satisfies C-36 while potentially failing C-27 if the competitor is placed at the right phase but only describes the wrong implementation without constituting the negative-space specification.

**Structural note.** C-35 and C-36 are both aspirational criteria. They are not required for a rubric to reach the golden threshold (composite >= 90, all essential PASS). Their mechanisms must be present in the skill prompt to produce rubrics that score 100 (28/28 aspirational = 10 points). The five variations below probe five distinct mechanisms for embedding these two constraints -- three single-axis and two combined -- following the structural evolution pattern from prior rounds.

---

## Round 12 Variation Map

| Variation | Axis | C-35 probe | C-36 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Lifecycle emphasis | Very strong -- dedicated ECONOMY + PHASE-LOCALITY SCAN phase between Mechanism Definer and Builder Aspirational; STOP A fires if >=3-criterion structural property exists but is unnamed | Very strong -- STOP B fires if any competitor appears outside its operative phase boundary before aspirational building begins | C-31/C-32/C-33/C-34 carried from best Round 11 mechanisms |
| V-02 | Output format | Strong -- Structural Economy Table required output of Mechanism Definer; row with count >=3 across >=2 clusters triggers ECONOMY REGISTER entry; blank C-NN list cell = format violation | Strong -- Competitor Phase Map required output before Scoring; "Phase-local?" column; a "No" cell = format violation blocking Emit | Both constraints visible as table format violations rather than phase STOP conditions |
| V-03 | Inertia framing | Very strong -- Flat-Mechanism Architecture competitor named before Mechanism Definer with derivation instruction; builder must add economy scan from competitor description | Very strong -- Preamble-Block Curator competitor named before competitor placement guidance with derivation instruction; builder must add phase-locality rule from competitor description | Two named competitors, each introduced at the phase where their failure becomes relevant |
| V-04 | Role sequence + lifecycle | Very strong -- Architectural Economy Auditor role inserted between Mechanism Definer and Builder Aspirational; Check 1 fires for economy, Check 2 fires for phase-locality; both are role exit conditions | Very strong -- same Architectural Economy Auditor role handles phase-locality as Check 2; role cannot complete until ECONOMY REPORT + PHASE-LOCALITY REPORT both exist | Role boundary makes concurrent construction structurally impossible |
| V-05 | Phrasing register + inertia framing | Very strong -- imperative: "IF one structural property closes >=3 criteria across >=2 clusters: STOP. NAME it in ECONOMY REGISTER."; Flat-Mechanism Set competitor named immediately before the imperative | Very strong -- imperative: "DO NOT place any competitor outside its operative phase boundary."; Preamble-Aggregator competitor named immediately before the imperative | Starkest phrasing of all five; competitor-then-imperative ordering rather than imperative-then-competitor |

---

## V-01 -- Lifecycle Emphasis (Economy + Phase-Locality Scan Phase)

**Axis:** Lifecycle emphasis
**Hypothesis:** Rounds 5, 8, 10, and 11 established that inserting a named structural phase immediately before a high-risk authoring decision produces reliable compliance: the phase is a construction precondition, not advice. V-01 applies the same mechanism to C-35 and C-36 by inserting an ECONOMY + PHASE-LOCALITY SCAN phase between the Mechanism Definer role and the Builder Aspirational role. The phase has two STOP gates: Check A counts whether any structural property in the Independence Map closes >=3 criteria across >=2 clusters, requiring those properties to be named in an ECONOMY REGISTER before aspirational criteria can be written (C-35 operative); Check B audits every competitor block in the rubric draft for phase-local placement, requiring each competitor to appear at the construction boundary where its gap is operationally relevant, and STOPs if any competitor is placed outside its operative phase (C-36 operative). C-31/C-32/C-33/C-34 are carried from Round 11 V-01's lifecycle architecture: PRE-EMIT VERIFICATION retains Check A (aspirational count gate) and Check B (category diversity gate); Three-State Scoring Table retains earn conditions; Independence Map retains C-NN annotations. Prediction: C-35 very strong (gate fires before aspirational construction); C-36 very strong (gate fires before aspirational construction); C-31 very strong (count gate retained); C-32 very strong (distribution gate retained); C-33 very strong (table format retained); C-34 very strong (map format retained).

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### PHASE 1 -- SKILL PROFILE + FAILURE ANALYSIS

Write a two-sentence skill profile: what does this skill produce, and what does a correct, complete output contain?

Enumerate failure modes. Assign severity:

```
F-NN | failure behavior | structural gap the skill failed to require | severity: blocking / suboptimal / cosmetic
```

Minimum: 3 blocking, 2 suboptimal. **Do not begin Phase 2 until the failure log contains at least 5 entries.**

---

### PHASE 2 -- CRITERION TEMPLATES (DEFINER STEP)

Before writing any criterion, generate skill-specific templates from the skill spec.

**Text template (slot-fillable -- fill slots verbatim; do not paraphrase):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from spec]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form: wrong implementation with same surface behavior as Y]
```

Causal direction rule: "Without Y, Z fails" is required. The prohibited form -- in any phrasing -- is any Text locating causality in the wrong form's consequence: "X causes failure," "failure occurs when X is present," "X leads to Z," and all semantic equivalents. The Auditor check function tests causal structure ("does this locate causality in the wrong form's consequence, in any phrasing?"), not pattern matching.

**Pass template (slot-fillable -- fill slots verbatim; do not paraphrase):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

A propositional statement ("Pass conditions should reference observables") is not a template. Do not substitute propositional form.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

Draft from blocking failure modes. Apply the Phase 2 Text template to each criterion.

Each criterion requires five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: Apply Phase 2 Text template. Write "Without [Y], the artifact [fails] because [Z]. Not [X], but [Y]." with skill-specific values in every slot. Do not substitute propositional form.
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass**: Apply Phase 2 Pass template. No "is clear" or "adequately covers" as sole observable.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity -- not whether an element exists.

Each criterion: same five fields as Phase 3. Required annotation: **Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

For each criterion from Phases 3 and 4, run the isolation audit. Read each field stripped of surrounding context.

**Text field checks (3):**
1. **Direction**: does Text locate causality in Y's absence ("without Y, Z fails")? Flag any Text in the prohibited direction -- any phrasing of "X causes failure" or "failure occurs when X is present."
2. **Contrast**: does Text name the rejected form X alongside the required form Y?
3. **Causal chain**: does Text name the downstream consequence Z of Y's absence?

**Pass field checks (3):**
4. **Location**: does Pass name an artifact location, field, or section?
5. **Observable**: does Pass name a specific count, token, or structural property?
6. **No qualitative-only**: does Pass avoid "clearly," "adequately," "well-structured" without an observable anchor?

**Audit report format -- required; do not substitute a narrative log:**

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Rewrite any flagged criterion before proceeding.

---

### PHASE 5 -- SCOPE CONSTRAINT

Complete this block before writing any aspirational criterion. It is a required input to Phase 7.

```
SCOPE CONSTRAINT:

Essential coverage:
  [C-NN guards against: one-line description of what each essential criterion catches.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per recommended criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property already listed above -- even at a
  higher threshold, stricter count, or narrower pass band -- is not aspirational.
  Tighter is not new territory. Do not use threshold escalation as aspirational
  distinction.

Gap zone (properties NOT covered by essential + recommended):
  Gap G-01: [Specific property an output passing all essential + recommended criteria
    could still lack. Must not be reachable by adjusting a threshold. Name the
    observable: what would an evaluator check to confirm its presence or absence?]
```

**Do not proceed to Phase 6 until the gap zone contains at least G-01.**

---

### PHASE 6 -- MECHANISM DEFINER

Read all criteria produced so far. Produce the Independence Map.

**Independence Map -- required format:**

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

Column requirements:
- **"Criterion affected (C-NN)"**: cite the specific criterion number. Generic "Yes, independent" without a criterion number is a format violation.
- **"Independent?"**: confirm removing this mechanism causes exactly one criterion (the named C-NN) to fail.
- If any row's "Criterion affected" cell is blank or cites multiple criteria: STOP -- resolve before Phase 6.5 runs.

**MECHANISM DEFINER GATE:** Output is Independence Map. Every row must have a non-blank, specific C-NN citation.

---

### PHASE 6.5 -- ECONOMY + PHASE-LOCALITY SCAN

**Complete both checks before writing any aspirational criterion. Output is blocked until both checks show CLEAR.**

```
ECONOMY + PHASE-LOCALITY SCAN:

Check A -- Structural economy (C-35):
  For each mechanism in the Independence Map, identify the structural property it uses.
  List criteria that share a structural property (across all mechanisms):
    Structural property [name]: closes [list C-NN, C-NN, ...] | count: [N] | clusters: [list cluster names]
  Economy threshold: a structural property closing >=3 criteria across >=2 clusters triggers
  a required ECONOMY REGISTER entry.
  ⛔ STOP if any such property exists but is not named in the ECONOMY REGISTER below.
     A structural property that independently closes >=3 criteria is a signal of rubric
     design quality. It must be named before aspirational criteria can be written so that
     the gap zone (Phase 5) accounts for it.

  ECONOMY REGISTER:
    [If no structural property closes >=3 criteria across >=2 clusters: write "No structural
     economy detected at >=3/>=2 threshold." If one or more do: name each property, list
     the criteria it closes, and name the clusters.]
  Check A: CLEAR / BLOCKED

Check B -- Phase-local competitor placement (C-36):
  List every competitor block introduced in this rubric draft so far:
    Competitor [name]: introduced at [Phase N] | gap operationally relevant at [Phase N] | phase-local? [Y/N]
  Requirement: each competitor must appear at the phase where its gap is first operationally
  relevant to construction. A competitor in a shared preamble before Phase 3 is not phase-local.
  ⛔ STOP if any competitor has phase-local = N -- move the competitor block to its operative
     phase before proceeding.
  Check B: CLEAR / BLOCKED
```

**Do not proceed to Phase 7 until both checks show CLEAR.**

---

### PHASE 7 -- ASPIRATIONAL CRITERIA (1-2)

Write aspirational criteria targeting the gap zone named in Phase 5. Each criterion must fall in the gap zone -- not in the essential or recommended coverage zones at any threshold.

Each aspirational criterion: same five fields as Phase 3, plus:

- **Fills gap**: [Cite the specific gap (G-NN) from the Phase 5 gap zone -- required; blank = format error.]

After writing each aspirational criterion, confirm: "Is the cited gap named in Phase 5?" If not, revise before continuing.

---

### PHASE 7.5 -- PRE-EMIT VERIFICATION

**Complete both checks before writing the Scoring section. Output is blocked until both checks show YES.**

```
PRE-EMIT VERIFICATION:

Check A -- Aspirational count (tier bound):
  Aspirational criteria drafted: [list by ID]
  Count: [N]
  Tier bound: 1-2 aspirational criteria maximum.
  ⛔ STOP if count > 2 -- trim before proceeding.
  Compliant? [YES / NO]

Check B -- Category diversity:
  Categories assigned across all criteria: [list each criterion ID and its category]
  Distinct categories present: [list unique values]
  Count of distinct categories: [N]
  Requirement: >= 3 distinct categories across the full criterion set.
  ⛔ STOP if distinct count < 3 -- revise before proceeding.
  Compliant? [YES / NO]
```

**Do not proceed to Phase 8 until both checks show YES.**

---

### PHASE 8 -- SCORING

State the scoring formula:

```
Essential:    (sum of essential PASS values) / N_essential x 60        max 60
Recommended:  (sum of recommended PASS values) / N_recommended x 30    max 30
Aspirational: (sum of aspirational PASS values) / N_aspirational x 10  max 10

Composite = Essential + Recommended + Aspirational                      max 100
```

**Three-State Scoring -- all three rows required; Earn conditions row must be non-blank:**

| State   | Value | Earn conditions |
|---------|-------|-----------------|
| PASS    | 1.0   | All Pass conditions for the criterion are fully and observably met. |
| PARTIAL | 0.5   | [State the specific conditions under which a criterion earns 0.5 rather than 1.0 or 0.0. Required: name what partial satisfaction looks like for this rubric's criteria. A blank Earn conditions cell is a table violation.] |
| FAIL    | 0.0   | No Pass condition is met; PARTIAL earn conditions not satisfied. |

**Tier count bounds (operative):** 3-5 essential | 2-3 recommended | 1-2 aspirational

**Golden threshold:** All essential criteria PASS AND composite >= 90.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences: state the lifecycle principle -- the ECONOMY + PHASE-LOCALITY SCAN phase makes structural economy detection and competitor placement verification construction preconditions before aspirational criteria are written; the PRE-EMIT VERIFICATION phase makes tier-count overflow and category under-diversity additional construction blockers; the Three-State Scoring Table requires PARTIAL earn conditions to be named, not implied), then SCOPE CONSTRAINT block (Phase 5, retained), then ECONOMY REGISTER (Phase 6.5 Check A, retained), then criteria ordered essential -> recommended -> aspirational (Fills gap and Dimension annotations retained; failure log and audit report omitted), then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-02 -- Output Format (Structural Economy Table + Competitor Phase Map)

**Axis:** Output format
**Hypothesis:** R7 V-02 and R11 V-02 established that a mandatory table column makes absent properties visible as blank cells -- format violations -- rather than soft omissions. V-02 applies the same mechanism to C-35 and C-36 simultaneously. For C-35: the Independence Map produced by the Mechanism Definer role is extended with a "Structural Economy" section -- a second required table listing each structural property shared across mechanisms, the criteria it closes (by C-NN list), and the count. A structural property closing >=3 criteria across >=2 clusters requires an ECONOMY REGISTER entry; a blank "C-NN list" cell is a format violation. For C-36: a Competitor Phase Map table is added as a required output before the Scoring section -- columns: competitor name, introduced-at phase, operative phase (where the gap is first relevant), phase-local Y/N. A "No" in the phase-local column is a format violation blocking Emit. The virtue of format enforcement: violations are visible in the output structure itself, not requiring phase gate logic to detect. The limitation: format violations require a reader to inspect the table; a phase STOP is structurally prior and cannot be bypassed by a builder who produces a table with all "Yes" cells. Prediction: C-35 strong (table structure makes economy detection visible); C-36 strong (table structure makes placement violations visible); both at somewhat lower certainty than V-01 because format tables can be completed with valid-looking entries.

---

You are a multi-role rubric construction system. Roles run in strict sequence. **Do not begin a role until the previous role's output is written.**

---

### DUAL DEFINER ROLE

Read the skill spec. Produce two binding templates. Your sole output is these two templates.

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form -- wrong implementation with same surface behavior]
```

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section]
OBSERVABLE: [specific token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

Causal direction rule: "Without Y, Z fails" is required. Prohibited form -- in any phrasing -- locates causality in X's consequence. Check function tests causal structure ("does this locate causality in the wrong form's consequence, in any phrasing?"), not pattern matching. Form-class prohibited: "X causes failure," "failure occurs when X is present," "X leads to Z," and all semantic equivalents.

**DEFINER GATE:** Two templates in slot-fillable form. Nothing else.

---

### BUILDER E+R ROLE

**Failure log** (minimum 5 entries):
```
F-NN | failure behavior | severity: blocking / suboptimal / cosmetic
```

**Essential criteria (3-5).** From blocking failure modes. Fill Text template slots verbatim. Five fields per criterion: ID (C-NN), Text, Weight (essential), Category (correctness | depth | format | coverage | behavior), Pass (fill Pass template slots).

**Recommended criteria (2-3).** From suboptimal failure modes. Pass conditions test degree, precision, or specificity -- not presence. Annotate: **Dimension:** [degree | precision | specificity].

**Post-draft audit.** For each criterion: `C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].` Rewrite flagged criteria before proceeding.

**BUILDER E+R GATE:** Output is failure log + essential + recommended + audit report.

---

### SCOPE GATEKEEPER ROLE

Read essential and recommended criteria. Produce the SCOPE DECLARATION.

```
SCOPE DECLARATION:

Essential coverage:
  [C-NN guards against: one line per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property already listed above -- at any threshold --
  is not aspirational. Tighter is not new territory.

Gap register:
  Gap G-01: [Specific uncovered property. Observable: what would an evaluator check?]
```

**SCOPE GATEKEEPER GATE:** SCOPE DECLARATION with at least G-01 in the gap register.

---

### MECHANISM DEFINER ROLE

Read all criteria produced so far. Produce two required tables.

**Independence Map -- required format:**

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

A blank "Criterion affected" cell or generic "Yes, independent" without a criterion number is a format violation. STOP if any such cell exists.

**Structural Economy Table -- required format (produced immediately after Independence Map):**

```
| Structural property | Used by mechanisms | Criteria closed (C-NN list) | Count | Clusters (>=2 required for economy) | Economy registered? |
|--------------------|--------------------|----------------------------|-------|-------------------------------------|---------------------|
| [property name]    | [mechanism list]   | [C-NN, C-NN, ...]          | [N]   | [cluster A, cluster B, ...]          | [YES / NO / N/A -- count <3] |
```

ECONOMY REGISTER: For any row where Count >= 3 AND Clusters >= 2, write an ECONOMY REGISTER entry:
```
ECONOMY REGISTER:
  Property [name]: independently closes [C-NN, C-NN, ...] across clusters [list]. Economy confirmed.
```

A "Economy registered? YES" cell with no corresponding ECONOMY REGISTER entry is a format violation.

**MECHANISM DEFINER GATE:** Output is Independence Map + Structural Economy Table + ECONOMY REGISTER (or explicit "No economy detected at >=3/>=2 threshold").

---

### BUILDER ASPIRATIONAL ROLE

Read SCOPE DECLARATION and ECONOMY REGISTER.

**Aspirational criteria (1-2).** Targeting gaps from the Scope Gatekeeper gap register. Each criterion must fall in the gap zone -- not in essential or recommended coverage at any threshold.

Aspirational count limit: 1-2 maximum. If drafting a third aspirational criterion: STOP -- trim to 2.

Each aspirational criterion: five fields (ID continuing from recommended) plus:
- **Fills gap**: [Cite G-NN from Scope Gatekeeper -- required; blank = format error.]

---

### DUAL AUDITOR ROLE

For each criterion from Builder E+R and Builder Aspirational, run isolation audit.

**Audit report format -- required:**
```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

**Competitor Phase Map -- required output before Scoring section (produced by Dual Auditor):**

```
| Competitor name | Introduced at phase | Operative phase (gap first relevant) | Phase-local? |
|-----------------|--------------------|------------------------------------|--------------|
| [name]          | Phase [N]           | Phase [N]                           | [YES / NO]   |
```

Phase-locality rule: a competitor must appear at the phase where its gap is first operationally relevant to construction. A "NO" in the Phase-local column is a format violation.
⛔ STOP if any "NO" appears -- move the competitor block to its operative phase before producing the Scoring section.

**Category Inventory (required before Scoring section):**
```
| C-NN | Category |
Distinct categories: [list]
Count: [N]
Requirement: >= 3 distinct categories. STOP if N < 3.
```

**DUAL AUDITOR GATE:** Output is audit report + Competitor Phase Map + Category Inventory. No "NO" cells in Competitor Phase Map.

---

### SCORING SECTION

**Three-State Scoring Table -- all three rows required; Earn conditions must be non-blank:**

| State   | Value | Earn conditions |
|---------|-------|-----------------|
| PASS    | 1.0   | All Pass conditions fully and observably met. |
| PARTIAL | 0.5   | [Required: state conditions under which a criterion earns 0.5 rather than 1.0 or 0.0. Name what partial satisfaction looks like. Blank = table violation.] |
| FAIL    | 0.0   | No Pass condition met; PARTIAL earn conditions not satisfied. |

```
Essential:    (sum) / N_essential x 60      max 60
Recommended:  (sum) / N_recommended x 30    max 30
Aspirational: (sum) / N_aspirational x 10   max 10
Composite = Essential + Recommended + Aspirational    max 100
```

**Tier count bounds:** 3-5 essential | 2-3 recommended | 1-2 aspirational
**Golden threshold:** All essential PASS AND composite >= 90.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences: state the format principle -- the Structural Economy Table makes structural economy visible as a required output cell rather than an optional observation; the Competitor Phase Map makes phase-local placement violations visible as "NO" cells before Scoring; the Three-State Scoring Table requires PARTIAL earn conditions as a required column entry), then SCOPE DECLARATION, then Independence Map + Structural Economy Table + ECONOMY REGISTER, then Competitor Phase Map, then criteria ordered essential -> recommended -> aspirational (Fills gap and Dimension annotations retained), then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-03 -- Inertia Framing (Competitor-First at Operative Phase)

**Axis:** Inertia framing
**Hypothesis:** R11 V-05 established that naming the wrong-implementation competitor before the correct implementation -- at the phase where the competitor's failure becomes relevant -- produces the highest compliance across all four C-31/C-32/C-33/C-34 probes. V-03 applies this mechanism to C-35 and C-36. For C-35: the "Flat-Mechanism Architecture" competitor is named immediately before the Mechanism Definer's economy check instruction. The competitor describes the inertia architecture -- five independent mechanisms, no structural property shared, no economy -- and ends with a derivation instruction: "from the description above, derive what the economy check must require before reading the check below." For C-36: the "Preamble-Block Curator" competitor is named immediately before the competitor placement rule. The competitor describes the inertia placement -- all competitors in a shared preamble block before Phase 3, each derivation instruction reading "from Section 1 above" -- and ends with a derivation instruction: "from the description above, derive where each competitor must be placed before reading the placement rule below." The two competitors are phase-local (each appears at the construction boundary where its failure is first relevant), making V-03 self-demonstrating: the prompt itself satisfies C-36 by placing its own competitors at their operative phases. Prediction: C-35 very strong (derivation instruction makes the economy requirement derivable from the competitor alone); C-36 very strong (derivation instruction makes phase-locality derivable from the competitor alone; prompt is self-demonstrating).

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### PHASE 1 -- SKILL PROFILE + FAILURE ANALYSIS

Write a two-sentence skill profile: what does this skill produce, and what does a correct, complete output contain?

Enumerate failure modes. Assign severity:

```
F-NN | failure behavior | structural gap the skill failed to require | severity: blocking / suboptimal / cosmetic
```

Minimum: 3 blocking, 2 suboptimal. **Do not begin Phase 2 until the failure log contains at least 5 entries.**

---

### PHASE 2 -- CRITERION TEMPLATES (DEFINER STEP)

Before writing any criterion, generate skill-specific templates from the skill spec.

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from spec]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form -- wrong implementation with same surface behavior]
```

Causal direction rule: "Without Y, Z fails" is required. Prohibited form -- in any phrasing -- locates causality in X's consequence: "X causes failure," "failure occurs when X is present," "X leads to Z," and all semantic equivalents. The check function tests causal structure, not pattern matching.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

A propositional statement ("Pass conditions should reference observables") is not a template.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

Draft from blocking failure modes. Apply the Phase 2 Text template to each criterion.

Each criterion: ID (C-NN starting at C-01), Text (apply Phase 2 template), Weight (essential), Category (correctness | depth | format | coverage | behavior), Pass (apply Phase 2 Pass template).

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity -- not whether an element exists. Annotate: **Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT

For each criterion: `C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].`

Rewrite any flagged criterion before proceeding.

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:

Essential coverage:
  [C-NN guards against: one line per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  Aspirational = new territory only. Tighter threshold is not new territory.

Gap zone:
  Gap G-01: [Specific uncovered property. Observable: what would an evaluator check?]
```

**Do not proceed to Phase 6 until the gap zone contains at least G-01.**

---

### PHASE 6 -- MECHANISM DEFINER

Read all criteria produced so far.

**Independence Map:**

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

A blank "Criterion affected" cell or generic "Yes, independent" without a criterion number is a format violation. STOP if any such cell exists.

---

**STRUCTURAL ECONOMY CHECK -- read this before completing Phase 6:**

> **Inertia competitor: the Flat-Mechanism Architecture**
>
> The Flat-Mechanism Architecture assigns one independent mechanism per criterion, exactly. Five criteria: five mechanisms. No mechanism shares a structural property with another. No structural property is shared. The architecture is correct, auditable, and satisfies one-to-one assignment (C-25). It is also structurally opaque: an evaluator inspecting the architecture cannot detect whether any structural property independently closes multiple criteria, because the design principle prohibits sharing at the mechanism level. A rubric built with this architecture passes C-25 regardless of whether any structural economy exists in the underlying design.
>
> This competitor IS the structural economy gap specification. **From the description above, derive what the economy check must require before reading the check below.**

**Economy check (operative after reading the competitor above):**

After completing the Independence Map, scan for structural economy: for each structural property used by any mechanism, list the criteria it independently satisfies. If a single structural property independently closes >=3 criteria across >=2 criterion clusters:

```
ECONOMY REGISTER:
  Property [name]: independently closes [C-NN, C-NN, ...] across clusters [list].
  Derivation: removing this structural property from the architecture would cause [N] criteria
  to fail independently, confirming the property closes each criterion standing alone.
```

If no such property exists: write "No structural economy at >=3/>=2 threshold."

**MECHANISM DEFINER GATE:** Output is Independence Map + Economy Register (or explicit "none").

---

### PHASE 6.5 -- ASPIRATIONAL CRITERIA (1-2)

Targeting gaps from the Phase 5 gap zone. Each criterion must fall in the gap zone -- not in essential or recommended coverage at any threshold.

Each aspirational criterion: same five fields as Phase 3, plus:
- **Fills gap**: [Cite G-NN -- required; blank = format error.]

Aspirational count limit: 1-2 maximum.

---

**COMPETITOR PLACEMENT CHECK -- read this before placing any competitors in Phase 6.5:**

> **Inertia competitor: the Preamble-Block Curator**
>
> The Preamble-Block Curator places all competitors in a shared Section 1 preamble block before Phase 3 begins. The preamble names three competitors -- the Pattern-Matcher Auditor, the Flat-Mechanism Architecture, the Phase-Agnostic Competitor Curator -- each with a derivation instruction that reads "from Section 1 above, derive the required function." The architecture is centralized (all competitors in one place), findable (a reader can navigate to Section 1), and satisfies C-27 (each competitor constitutes the gap specification). It is also phase-decoupled: a builder constructing Phase 4 reads the Mechanism Definer competitor from memory (recalled from Section 1) rather than encountering it at the construction boundary where the mechanism is defined. Derivation from memory differs from derivation at the moment of need.
>
> This competitor IS the phase-locality gap specification. **From the description above, derive where each competitor must be placed before reading the placement rule below.**

**Phase-locality rule (operative after reading the competitor above):**

Each competitor block in this rubric must appear at the construction boundary where its gap is first operationally relevant to construction -- not in a shared preamble, not in a prior section. A competitor placed before Phase 3 when its gap is only relevant at Phase 6 satisfies C-27 (competitor constitutes the gap) while failing C-36 (competitor is not phase-local). Apply this rule to all competitor blocks introduced in this rubric, including the two competitors in Phases 6 and 6.5 above.

---

### PHASE 7 -- PRE-EMIT VERIFICATION

```
PRE-EMIT VERIFICATION:

Check A -- Aspirational count:
  Aspirational criteria: [list by ID] | Count: [N]
  ⛔ STOP if count > 2. Compliant? [YES / NO]

Check B -- Category diversity:
  Categories: [C-NN: category, ...] | Distinct: [list] | Count: [N]
  ⛔ STOP if N < 3. Compliant? [YES / NO]
```

---

### PHASE 8 -- SCORING

**Three-State Scoring Table:**

| State   | Value | Earn conditions |
|---------|-------|-----------------|
| PASS    | 1.0   | All Pass conditions fully and observably met. |
| PARTIAL | 0.5   | [Required: state specific conditions for 0.5 rather than 1.0 or 0.0. Blank = table violation.] |
| FAIL    | 0.0   | No Pass condition met; PARTIAL conditions not satisfied. |

```
Essential:    (sum) / N_essential x 60      max 60
Recommended:  (sum) / N_recommended x 30    max 30
Aspirational: (sum) / N_aspirational x 10   max 10
Composite = Essential + Recommended + Aspirational    max 100
```

**Tier count bounds:** 3-5 essential | 2-3 recommended | 1-2 aspirational
**Golden threshold:** All essential PASS AND composite >= 90.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences: state the inertia principle -- the Flat-Mechanism Architecture competitor makes the structural economy requirement derivable before the economy check is read; the Preamble-Block Curator competitor makes phase-local competitor placement derivable before the placement rule is read; each competitor is introduced at the phase where its failure is first operationally relevant, making the prompt self-demonstrating on C-36), then SCOPE CONSTRAINT block, then Economy Register, then criteria ordered essential -> recommended -> aspirational (Fills gap and Dimension annotations retained), then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-04 -- Role Sequence + Lifecycle (Architectural Economy Auditor Role)

**Axis:** Role sequence + lifecycle emphasis
**Hypothesis:** R11 V-04 established that inserting a named Emit Validator role as the final gate before output release -- whose sole job is to run compliance checks as role exit conditions -- produces the highest compliance when multiple independent checks must all pass before proceeding. V-04 applies the same role-boundary architecture to C-35 and C-36 by inserting an ARCHITECTURAL ECONOMY AUDITOR role between the Mechanism Definer role and the Builder Aspirational role. The Auditor has two sequential checks as role exit conditions: Check 1 (C-35) reads the Independence Map, computes structural economy, and produces the ECONOMY REPORT; Check 2 (C-36) reads all competitor blocks in the rubric draft and produces the PHASE-LOCALITY REPORT. Builder Aspirational cannot begin until both reports exist with status CLEAR. The role boundary makes concurrent construction structurally impossible: the Auditor's output is Builder Aspirational's required input, not a post-draft correction. C-35 and C-36 are closed by the same role through structurally independent checks -- Check 1 and Check 2 can each fail independently, and the Auditor cannot claim completion until both show CLEAR. Prediction: C-35 very strong (Check 1 is role exit condition); C-36 very strong (Check 2 is role exit condition); the mechanism pair satisfies C-25 (independent checks close independent criteria) and C-29 (dedicated prior role step) as structural byproducts.

---

You are a multi-role rubric construction system. Roles run in strict sequence. **Do not begin a role until the previous role's output is written and complete.**

---

### DUAL DEFINER ROLE

Read the skill spec. Produce two binding templates as your sole output.

**Text template (slot-fillable):**
```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form]
```

**Pass template (slot-fillable):**
```
LOCATION: [artifact field or section]
OBSERVABLE: [specific token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

Causal direction rule: "Without Y, Z fails" is required. Prohibited form -- in any phrasing -- locates causality in X's consequence. Check function: "does this locate causality in the wrong form's consequence, in any phrasing?" -- not pattern matching.

**DEFINER GATE:** Two templates, slot-fillable form only.

---

### BUILDER E+R ROLE

**Failure log** (minimum 5): `F-NN | failure behavior | severity: blocking / suboptimal / cosmetic`

**Essential criteria (3-5):** Fill Text and Pass template slots verbatim. Five fields: ID (C-NN), Text, Weight (essential), Category, Pass.

**Recommended criteria (2-3):** Pass tests degree, precision, or specificity. Annotate: **Dimension:** [degree | precision | specificity].

**Post-draft audit:** `C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].`

**BUILDER E+R GATE:** Failure log + essential + recommended + audit report.

---

### SCOPE GATEKEEPER ROLE

```
SCOPE DECLARATION:

Essential coverage:   [C-NN guards against: one line per criterion.]
Recommended coverage: [C-NN guards the [dimension] of [property] -- one line.]
Threshold escalation prohibition: tighter is not new territory.
Gap register:
  Gap G-01: [Specific uncovered property. Observable: what would an evaluator check?]
```

**SCOPE GATEKEEPER GATE:** SCOPE DECLARATION with at least G-01.

---

### MECHANISM DEFINER ROLE

Read all criteria produced so far. Produce Independence Map.

**Independence Map:**
```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

A blank "Criterion affected" cell or generic "Yes, independent" without a criterion number is a format violation. STOP if any such cell exists.

**MECHANISM DEFINER GATE:** Independence Map with all C-NN citations populated.

---

### ARCHITECTURAL ECONOMY AUDITOR ROLE

Read: Independence Map from Mechanism Definer and all competitor blocks in the rubric draft so far.

This role's sole output is two reports. Builder Aspirational cannot run until both reports show CLEAR.

**Check 1 -- Structural Economy (C-35):**

For each mechanism in the Independence Map, identify its structural property (the design decision that makes the mechanism work). List criteria that share a structural property.

```
ECONOMY ANALYSIS:
  Structural property [name]:
    Used by mechanism(s): [list]
    Criteria independently closed: [C-NN, C-NN, ...]
    Count: [N] | Clusters: [list cluster names] | Cluster count: [N]
    Economy threshold met (count >=3 AND cluster count >=2)? [YES / NO]
```

If YES for any property:
```
ECONOMY REGISTER:
  Property [name]: independently closes [C-NN, ...] across [N] clusters. Named.
```

ECONOMY REPORT status: CLEAR (no economy threshold met, or all threshold-meeting properties named in ECONOMY REGISTER) | BLOCKED (threshold met but not named).

**Check 2 -- Phase-Local Competitor Placement (C-36):**

List every named competitor block in the rubric draft. For each, identify: the phase where it is introduced vs. the phase where its gap is first operationally relevant to construction.

```
PHASE-LOCALITY ANALYSIS:
  Competitor [name]:
    Introduced at: Phase [N] / [section name]
    Operationally relevant at: Phase [N] / [section name]
    Phase-local? [YES / NO]
    If NO: required action: move to [operative phase].
```

PHASE-LOCALITY REPORT status: CLEAR (all competitors phase-local) | BLOCKED (one or more competitors not phase-local, with required actions listed).

**ARCHITECTURAL ECONOMY AUDITOR GATE:** Output is ECONOMY REPORT + PHASE-LOCALITY REPORT. Gate passes only when both reports show CLEAR. If either is BLOCKED: Builder Aspirational cannot run. Resolve blocking items and re-run the failed check before proceeding.

---

### BUILDER ASPIRATIONAL ROLE

**Precondition:** ECONOMY REPORT = CLEAR and PHASE-LOCALITY REPORT = CLEAR. Do not begin until both are confirmed.

**Aspirational criteria (1-2).** Targeting gaps from SCOPE GATEKEEPER gap register only.

Aspirational count: 1-2 maximum. If drafting a third: STOP -- trim to 2.

Each aspirational criterion: five fields (ID continuing from recommended) plus:
- **Fills gap:** [Cite G-NN from SCOPE GATEKEEPER -- required; blank = format error.]

---

### PRE-EMIT VERIFICATION

```
Check A -- Aspirational count:
  List: [criteria IDs] | Count: [N] | Bound: 1-2
  ⛔ STOP if count > 2. Compliant? [YES / NO]

Check B -- Category diversity:
  [C-NN: category, ...] | Distinct categories: [list] | Count: [N]
  ⛔ STOP if N < 3. Compliant? [YES / NO]
```

**Do not proceed to Scoring until both show YES.**

---

### SCORING SECTION

**Three-State Scoring Table:**

| State   | Value | Earn conditions |
|---------|-------|-----------------|
| PASS    | 1.0   | All Pass conditions fully and observably met. |
| PARTIAL | 0.5   | [Required: name conditions for 0.5. Blank = table violation.] |
| FAIL    | 0.0   | No Pass condition met; PARTIAL conditions not satisfied. |

```
Essential:    (sum) / N_essential x 60      max 60
Recommended:  (sum) / N_recommended x 30    max 30
Aspirational: (sum) / N_aspirational x 10   max 10
Composite = Essential + Recommended + Aspirational    max 100
```

**Tier count bounds:** 3-5 essential | 2-3 recommended | 1-2 aspirational
**Golden threshold:** All essential PASS AND composite >= 90.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences: state the role-sequence principle -- the Architectural Economy Auditor role is sequentially prior to Builder Aspirational, making structural economy detection and competitor phase-locality verification construction preconditions with role-exit status as the enforcement mechanism; the role produces two independent reports, each a gate, so neither check can be skipped without blocking the role; the Three-State Scoring Table and PRE-EMIT VERIFICATION gates carry forward from the base architecture), then SCOPE DECLARATION, then ECONOMY REGISTER (from Auditor Check 1), then PHASE-LOCALITY REPORT (from Auditor Check 2), then criteria ordered essential -> recommended -> aspirational (Fills gap and Dimension retained; failure log, audit report, role headers omitted), then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-05 -- Phrasing Register + Inertia Framing (Imperative + Competitor-First)

**Axis:** Phrasing register + inertia framing
**Hypothesis:** V-03 (inertia framing with derivation instruction) and V-04 (role-boundary architecture) represent the two strongest structural mechanisms for C-35 and C-36. V-05 tests their phrasing register complement: whether competitor-then-imperative ordering -- naming the wrong implementation first, issuing the operative prohibition second -- produces compliance through the starkest possible instruction surface. The phrasing register is entirely prescriptive and prohibitive. Conjunctions like "you should" and "it is recommended" are absent. Every operative requirement is an imperative or STOP. For C-35: the Flat-Mechanism Set competitor is named immediately before the economy STOP, making the competitor the causal context for the prohibition ("the architecture that motivated this STOP is named above"). For C-36: the Preamble-Aggregator competitor is named immediately before the placement STOP, with the same structure. Both competitors include a derivation instruction. The hypothesis is that competitor-then-STOP is the most direct instruction pattern: the reader encounters the wrong form, derives the requirement, and then confirms derivation with the operative prohibition in one pass. The limitation of this approach: imperatives can be read past; structural gates (V-01/V-04) cannot. Prediction: C-35 very strong (competitor + derivation + STOP is the maximum-information instruction sequence); C-36 very strong (same); slight degradation risk compared to V-01/V-04 because the STOP is procedural rather than structural.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### PHASE 1 -- SKILL PROFILE + FAILURE ANALYSIS

Write a two-sentence skill profile. Then enumerate failure modes:

```
F-NN | failure behavior | structural gap the skill failed to require | severity: blocking / suboptimal / cosmetic
```

Minimum: 3 blocking, 2 suboptimal. **DO NOT BEGIN PHASE 2 UNTIL YOU HAVE AT LEAST 5 ENTRIES.**

---

### PHASE 2 -- CRITERION TEMPLATES

Generate skill-specific templates. **DO NOT WRITE A CRITERION BEFORE THESE TEMPLATES EXIST.**

**Text template (slot-fillable -- fill these slots verbatim in every Text field):**
```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [required property -- specific to this skill, not "good output"]
  Z = [failure consequence -- specific, not "failure"]
  X = [rejected form -- specific wrong implementation, not "bad output"]
```

**Pass template (slot-fillable -- fill these slots verbatim in every Pass field):**
```
LOCATION: [artifact field or section -- specific]
OBSERVABLE: [token, count, or structural property -- specific]
STANDARD: [measurement unit -- specific]
```

Causal direction rule: "Without Y, Z fails" is required. The prohibited direction -- in any phrasing -- locates causality in X's consequence. THE CHECK FUNCTION IS NOT PATTERN MATCHING. The check function is: "does this Text locate causality in the wrong form's consequence, in any phrasing?" A Text that says "X leads to failure" is prohibited. A Text that says "the absence of X causes failure" is prohibited. ONLY "without Y, the artifact fails because Z" is in the required direction.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

From blocking failure modes. FILL THE TEXT TEMPLATE SLOTS VERBATIM. DO NOT WRITE PROPOSITIONAL TEXT.

Five fields per criterion: ID (C-NN starting at C-01), Text, Weight (essential), Category (correctness | depth | format | coverage | behavior), Pass (fill Pass template slots verbatim).

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

From suboptimal failure modes. PASS CONDITIONS MUST TEST DEGREE, PRECISION, OR SPECIFICITY. A Pass condition that tests whether something exists is an essential Pass condition in the wrong tier.

Annotate: **Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT

For every criterion: `C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].`

**REWRITE ANY FLAGGED CRITERION BEFORE PROCEEDING. DO NOT CARRY FLAGGED CRITERIA FORWARD.**

---

### PHASE 5 -- SCOPE CONSTRAINT

```
SCOPE CONSTRAINT:

Essential coverage:   [C-NN guards against: ...]
Recommended coverage: [C-NN guards the [dimension] of [property] ...]
Threshold escalation: ASPIRATIONAL = NEW TERRITORY ONLY. Tighter is not new.
Gap zone:
  Gap G-01: [Specific uncovered property. Observable: what would an evaluator check?]
```

**DO NOT BEGIN PHASE 6 UNTIL G-01 IS NAMED.**

---

### PHASE 6 -- MECHANISM DEFINER

Produce the Independence Map.

```
| Mechanism name | What it does (one sentence) | Criterion affected (C-NN) | Independent? |
|----------------|----------------------------|--------------------------|--------------|
| [name]         | [one sentence]              | C-NN                     | Yes -- affects C-NN only |
```

**A BLANK "CRITERION AFFECTED" CELL OR "YES, INDEPENDENT" WITHOUT A C-NN CITATION IS A FORMAT VIOLATION. STOP AND CORRECT BEFORE PROCEEDING.**

---

**READ THIS BEFORE COMPLETING PHASE 6:**

> **Competitor: the Flat-Mechanism Set**
>
> The Flat-Mechanism Set produces one independent mechanism per criterion, exactly. Five criteria, five mechanisms. Each mechanism targets one criterion; each criterion is targeted by one mechanism. No structural property is shared across mechanisms. The architecture satisfies one-to-one assignment. An evaluator scanning the Independence Map finds five rows, each with a unique C-NN citation, each marked "Yes -- affects C-NN only." The architecture is correct. It is also economically opaque: the architecture produces the same Independence Map whether or not any structural property independently closes multiple criteria. Two rubrics -- one with five independent mechanisms, one with a three-competitor staircase that closes five criteria through one structural property -- produce identical Independence Maps under the Flat-Mechanism Set architecture. The maps are identical; the structural quality is not.
>
> **This competitor IS the structural economy gap specification. From the description above, derive what the economy check must require. Then read the economy check below.**

**ECONOMY CHECK (operative -- run after completing the Independence Map):**

After completing the Independence Map, identify structural properties shared across mechanisms. For each structural property, list the criteria it independently closes.

IF any single structural property independently closes >=3 criteria across >=2 criterion clusters:
⛔ STOP. NAME this property in the ECONOMY REGISTER before writing aspirational criteria.

```
ECONOMY REGISTER:
  Property [name]: closes [C-NN, C-NN, ...] across clusters [list].
  (If no property meets the >=3/>=2 threshold: write "No structural economy at threshold.")
```

**DO NOT PROCEED TO PHASE 7 UNTIL THE ECONOMY REGISTER IS WRITTEN.**

---

### PHASE 7 -- ASPIRATIONAL CRITERIA (1-2)

Targeting gaps from Phase 5. Each criterion must fall in the gap zone -- not in essential or recommended coverage at any threshold.

Each aspirational criterion: five fields plus:
- **Fills gap:** [Cite G-NN -- required; blank = format error.]

**READ THIS BEFORE PLACING ANY COMPETITOR BLOCK IN THIS RUBRIC:**

> **Competitor: the Preamble-Aggregator**
>
> The Preamble-Aggregator places all competitor blocks in a shared preamble section at the start of the rubric, before Phase 3. The preamble names three competitors -- the Pattern-Matcher Auditor, the Flat-Mechanism Set, and the Preamble-Aggregator itself. Each competitor block ends with a derivation instruction that reads: "from Section 1 above, derive the required function." A builder constructing Phase 6 recalls the Flat-Mechanism Set competitor from memory; a builder constructing Phase 7 recalls the Preamble-Aggregator competitor from memory. The architecture is centralized (findable), complete (all competitors present), and satisfies C-27 (each competitor constitutes the gap specification). The architecture fails C-36: derivation from Section 1 recalled at Phase 6 is not the same as derivation from a competitor block encountered at Phase 6. The construction boundary is the moment of need. Encounter at the moment of need is the required placement.
>
> **This competitor IS the phase-locality gap specification. From the description above, derive where each competitor must appear. Then read the placement rule below.**

**PHASE-LOCALITY RULE (operative):**

EACH COMPETITOR BLOCK IN THIS RUBRIC MUST APPEAR AT THE PHASE WHERE ITS GAP IS FIRST OPERATIONALLY RELEVANT TO CONSTRUCTION.

DO NOT PLACE ANY COMPETITOR IN A SHARED PREAMBLE BLOCK.
DO NOT REFERENCE A COMPETITOR FROM A PRIOR SECTION ("from Section 1 above").
A COMPETITOR PLACED BEFORE ITS OPERATIVE PHASE SATISFIES C-27 AND FAILS C-36.

**Aspirational count limit: 1-2 maximum. IF YOU ARE WRITING A THIRD ASPIRATIONAL CRITERION: STOP. TRIM TO 2.**

---

### PHASE 7.5 -- PRE-EMIT VERIFICATION

```
PRE-EMIT VERIFICATION:

Check A -- Aspirational count:
  [list IDs] | Count: [N] | Bound: 1-2
  ⛔ STOP if count > 2. Compliant? [YES / NO]

Check B -- Category diversity:
  [C-NN: category for each criterion]
  Distinct categories: [list] | Count: [N]
  ⛔ STOP if N < 3. Compliant? [YES / NO]
```

**DO NOT PROCEED TO SCORING UNTIL BOTH CHECKS SHOW YES.**

---

### PHASE 8 -- SCORING

**Three-State Scoring Table -- ALL THREE EARN CONDITIONS ROWS MUST BE NON-BLANK. A BLANK EARN CONDITIONS CELL IS A TABLE VIOLATION.**

| State   | Value | Earn conditions |
|---------|-------|-----------------|
| PASS    | 1.0   | All Pass conditions fully and observably met. |
| PARTIAL | 0.5   | [REQUIRED: state the specific conditions under which a criterion earns 0.5. Name what partial satisfaction looks like for this rubric's criteria. DO NOT leave blank. DO NOT write "partial credit at evaluator discretion."] |
| FAIL    | 0.0   | No Pass condition met; PARTIAL conditions not satisfied. |

```
Essential:    (sum) / N_essential x 60      max 60
Recommended:  (sum) / N_recommended x 30    max 30
Aspirational: (sum) / N_aspirational x 10   max 10
Composite = Essential + Recommended + Aspirational    max 100
```

**Tier count bounds:** 3-5 essential | 2-3 recommended | 1-2 aspirational
**Golden threshold:** All essential PASS AND composite >= 90.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences: state the phrasing register principle -- the Flat-Mechanism Set competitor makes the structural economy requirement derivable at Phase 6 before the STOP is read; the Preamble-Aggregator competitor makes the phase-locality requirement derivable at Phase 7 before the placement rule is read; competitor-then-imperative ordering ensures the wrong form is encountered before the prohibition, making the prohibition confirmatory rather than declarative), then SCOPE CONSTRAINT block, then Economy Register, then criteria ordered essential -> recommended -> aspirational (Fills gap and Dimension retained; failure log, audit report, phase headers omitted), then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}
