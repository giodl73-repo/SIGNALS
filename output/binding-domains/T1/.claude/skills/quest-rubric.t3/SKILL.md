---
name: quest-rubric
description: "Define what good output looks like for a skill. Given a skill spec and sample outputs, produce a scoring rubric: a ranked list of criteria (C-01, C-02...) each with a pass condition, weight, and category (correctness, depth, format, coverage). The rubric is the objective function for /quest:golden. Start with 3-5 essential criteria; the rubric grows as /quest:golden discovers excellence patterns.
"
allowed-tools: [Read, Write, Glob]
param_set: lean
---
You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### STATUS QUO COMPETITOR

The standard rubric-building approach:

1. Read the skill spec. Draft criteria for what good output looks like.
2. Assign essential / recommended / aspirational by editorial judgment.
3. Write Pass conditions on-the-fly, using whatever language describes the pass state.
4. State a composite formula and golden threshold.
5. Add aspirational criteria as an afterthought tier for advanced cases.

This approach produces a rubric. It may be directionally correct. It may pass a basic
completeness check.

**What it does not do:**

- Fails to enumerate failure modes before drafting -- criteria come from intuition about
  good output rather than from systematic analysis of broken output.
- Fails to produce causal direction templates -- Text fields describe presence of good
  properties, not consequence of their absence.
- Fails to enforce Pass observability by template -- Pass conditions include qualitative
  language as sole observables.
- Fails to name a specific reference anchor with a Falls-short dimension.
- Fails to verify mechanism independence.
- Fails to make role dependencies bidirectionally traceable.
- Fails to verify category diversity by tier -- category distribution is checked globally
  rather than per tier, making tier convergence invisible.
- Fails to declare combined-form joint satisfiability for co-extension pairs -- when two
  criteria both constrain the same structural clause in different embedding dimensions,
  the rubric provides only per-criterion examples; a builder cannot know from the rubric
  alone whether both embedding requirements can coexist in a single clause expression or
  must be satisfied in separate clauses.
- Fails to name form-embedding criteria by ID in Dual Auditor Track 2 -- form-compliance
  verification steps use generic language without naming which criterion each step tests;
  a builder correcting a Track 2 failure cannot confirm which criterion's form requirement
  they are satisfying, and a maintainer cannot update Track 2 without reading all criterion
  definitions to identify which criteria are form-embedding.
- Fails to include per-criterion form-verification rows in the emit manifest -- the manifest
  verifies structural completeness but does not gate emission on the specific embedded-form
  conditions; a rubric with correct overall structure but incorrect sufficiency-clause or
  consequence-clause form passes the manifest check, creating a third independent
  verification gap above instruction level and Track 2.

**From the description above, derive what the required rubric-building procedure must supply --
before reading Phase 1. State your derivation, then proceed.**

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

This role receives the failure log from Phase 1. Its output is two slot-fillable templates
derived from the skill spec. It does not produce criterion fields during this role.

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form -- wrong implementation with same surface behavior as Y]
```

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form -- in
any phrasing -- is any Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

**DEFINER OUTPUT GATE** is satisfied when: Text template and Pass template are both present
in slot-fillable form, derived from the skill spec, with no additional content. Nothing else.
STOP if this role's output contains anything beyond the two required templates -- rewrite
before proceeding to Phase 3.

ROLES: PHASE 3 and PHASE 4 cannot begin until DEFINER OUTPUT GATE is satisfied.

**Scope note:** A rubric-building output satisfying this gate contains exactly two templates
in slot-fillable form. A failing output either omits a template, provides it in
non-slot-fillable form, or adds content beyond the two templates. These two outputs are
structurally distinct.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied.**

Draft from blocking failure modes. Apply Text template and Pass template from ROLE: CRITERION
DEFINER to each criterion.

Each criterion: ID (C-NN, sequential from C-01), Text (slot-filled), Weight (essential),
Category (correctness | depth | format | coverage | behavior), Pass (slot-filled). No "is
clear" or "adequately covers" as sole observable.

Competitor blocks follow PHASE-LOCALITY RULE: immediately before the governed criterion,
ending with derivation instruction.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied.**

Draft from suboptimal failure modes. Same five fields as Phase 3 + **Dimension:**
[degree | precision | specificity].

---

### PHASE-LOCALITY RULE

Prohibited competitor block placement zones:
1. **Preamble zone**: before any construction phase.
2. **Shared-operating-principles zone**: preceding more than one construction step.
3. **Multi-criterion zone**: governing more than one criterion.

Correctly placed: does not appear in any prohibited zone. Required Emit manifest target.

---

### PHASE 4.5 -- POST-DRAFT AUDIT

#### ISOLATION AUDIT

All criteria from Phases 3 and 4 audited stripped of surrounding context.

**Text field checks (3):**
1. Direction: does Text locate causality in Y's absence?
2. Contrast: does Text name the rejected form X alongside Y?
3. Causal chain: does Text name the downstream consequence Z?

**Pass field checks (3):**
4. Location: does Pass name an artifact location, field, or section?
5. Observable: does Pass name a specific count, token, or structural property?
6. No qualitative-only: does Pass avoid bare qualitative language without anchor?

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

Revise any criterion with a failing flag before DIVERGENCE CHECK proceeds.

#### DIVERGENCE CHECK

> **TIER-BLIND CATEGORIZER** -- The standard category-distribution audit reads each
> criterion's Category field, confirms the field is present and non-empty, and notes that
> multiple category names appear across the rubric. It does not separate assignments by tier
> (essential / recommended / aspirational), does not compute a majority category per tier,
> and does not check whether different tiers have different majority categories. A rubric
> where essential criteria are predominantly "correctness" and aspirational criteria are also
> predominantly "correctness" passes the standard audit: both tiers assign valid category
> names, variety exists in the rubric overall. The tier convergence is invisible to the
> standard check. From the description above, derive what the category-distribution divergence
> check must verify before reading the check below.

Count category assignments per tier. Record:

```
Essential tier:    [category] x[N] ... -- majority: [category]
Recommended tier:  [category] x[N] ... -- majority: [category]
Aspirational tier: [category] x[N]     -- majority: [category]
```

Fewer than 2 of 3 tiers with distinct majority categories requires revision before PHASE 5.

---

### PHASE 5 -- REFERENCE ANCHOR

**Input:** Phase 4.5 complete.

```
REFERENCE ANCHOR:
  Reference:   [specific competitor or prior-version identifier]
  Passes:      [criteria satisfied -- at minimum C-01 through C-08]
  Falls-short: [exact dimension on which it fails to meet the aspirational bar]
  Consumer:    ROLE: MECHANISM DEFINER cannot begin until this anchor is complete.
               The Falls-short dimension defines the aspirational gap that the
               Mechanism Definer's independence map must cover.
```

ROLE: MECHANISM DEFINER does not begin until REFERENCE ANCHOR is complete with Falls-short
populated and Consumer naming ROLE: MECHANISM DEFINER as the blocked consumer.

---

### PHASE 5.5 -- BUILDER ASPIRATIONAL PRECONDITION CHECK

Confirm before ROLE: BUILDER ASPIRATIONAL begins:
1. DEFINER OUTPUT GATE satisfied (both templates present, no additional content).
2. MECHANISM DEFINER GATE satisfied (independence map complete, all rows "Yes").
3. REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE: MECHANISM DEFINER).

ROLE: BUILDER ASPIRATIONAL begins only after all three confirmed.

---

### ROLE: MECHANISM DEFINER

**Input:** REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE: MECHANISM
DEFINER as the blocked consumer).

Produces independence map for anticipated aspirational gaps.

**Independence map format:**

```
Mechanism        | Independence             | Affects criterion
[mechanism name] | Yes -- affects C-NN only | [TBD or C-NN]
```

Each row mutually exclusive. Removing any one mechanism leaves exactly one criterion failing.

**MECHANISM DEFINER GATE:** independence map complete, all rows "Yes -- affects C-NN only,"
all gaps have a row. ROLE: BUILDER ASPIRATIONAL begins only after satisfied.

---

### ROLE: BUILDER ASPIRATIONAL

**Input required:**
- **CRITERION DEFINER GATE**: Text template and Pass template in slot-fillable form.
- **MECHANISM DEFINER GATE**: Independence Map with all C-NN citations populated.

ROLE: BUILDER ASPIRATIONAL begins only when both gate artifacts exist.

Drafts aspirational criteria closing the REFERENCE ANCHOR Falls-short gap. One criterion per
mechanism. Aspirational tier count: 1-2. Competitor blocks follow PHASE-LOCALITY RULE.

Each criterion: ID, Text (slot-filled), Weight: aspirational, Category, Pass (slot-filled).
Annotation: **Gap closed:** [independence map mechanism row citation].

---

### BASELINE -- EVALUABILITY ARCHITECTURE

Before building EVALUABILITY ARCHITECTURE, produce the following sub-sections in order.

#### PAIRED EXTENSION EXAMPLE DERIVATION

Enumerate all co-extension pairs in the current criterion set. A co-extension pair consists
of two criteria that constrain the same structural clause in different information-embedding
dimensions.

For each pair:

```
CO-EXTENSION PAIR [A/B/...]:
  Criteria:        [C-NN + C-NN]
  Shared clause:   [name of the structural clause both criteria constrain]
  Dimension 1 (C-NN): [what this criterion requires embedded in the clause]
  Dimension 2 (C-NN): [what this criterion requires embedded in the clause]
  Combined example: "[single clause expression satisfying both dimensions simultaneously]"
  Structural independence note: a baseline providing only per-criterion examples without
    this combined expression fails to declare joint satisfiability as a rubric property.
    A builder receiving only per-criterion examples must independently verify whether
    a single combined clause is possible -- this derivation section eliminates that gap.
```

**STOP if any co-extension pair lacks a combined example before EVALUABILITY ARCHITECTURE
proceeds.**

**Canonical combined forms for known pairs:**

- **Pair A (C-51 + C-53 -- Phase 9 PREREQUISITE sufficiency clause):**
  Combined form: "a reader can confirm that EVALUABILITY GATE is complete by reading this
  PREREQUISITE line alone, without reading the body of ROLE: EVALUABILITY AUDITOR"
  - C-51 satisfied: excluded role body name "ROLE: EVALUABILITY AUDITOR" embedded within
    the sufficiency clause (not only in a co-located independence boundary sentence).
  - C-53 satisfied: verbatim gate identifier "EVALUABILITY GATE" embedded within the
    sufficiency clause body.
  - Joint satisfiability confirmed: both embedding requirements coexist in this single clause
    expression without conflict.

- **Pair B (C-52 + C-54 -- Architecture-labeled STOP consequence clause):**
  Combined form: "the Architecture-A competitor entry in the NON-REDUNDANCY DECLARATION
  is absent"
  - C-52 satisfied: exact section heading name "NON-REDUNDANCY DECLARATION" present in
    consequence clause.
  - C-54 satisfied: specific absent element "Architecture-A competitor entry" named in
    consequence clause.
  - Joint satisfiability confirmed: both embedding requirements coexist in this single clause
    expression without conflict.

A baseline providing only separate examples -- one example for C-51, one for C-53, one for
C-52, one for C-54 -- without these combined expressions fails to declare joint satisfiability
as a rubric design principle. These two outputs are structurally distinct: separate examples
leave co-extension as an empirical discovery; combined examples declare it as a verified
rubric property that a builder can rely on without running isolation experiments.

---

### EVALUABILITY ARCHITECTURE

**EVALUABILITY GATE:** The emit phase begins only when an independent audit confirms that
every structural criterion (those satisfying C-15/C-19) maps to a named artifact enabling
independent verification.

**EVALUABILITY AUDITOR** role:

Produce a per-criterion evaluability declaration for each structural criterion. Format:

```
[C-NN]: artifact = [named section block]; scan method = [heading scan / table row count / field presence]; excluded from verification path: [instruction content that need NOT be read]
```

**ROLE: EVALUABILITY AUDITOR** is complete when every structural criterion has a declaration.

---

### NON-REDUNDANCY DECLARATION

**EVALUABILITY ARCHITECTURE COMPETITOR section:**

| Architecture label | Competing design | Failure class |
|--------------------|-----------------|---------------|
| Architecture-A     | [description]   | [failure class missed] |

**STOP if the EVALUABILITY ARCHITECTURE COMPETITOR section is not complete before
NON-REDUNDANCY DECLARATION proceeds.**

Architecture-labeled failure-mode arguments:

- [Architecture-A]: without the pre-emit gate, [specific criterion] is unenforced at Phase 9
  entry -- the Architecture-A competitor entry in the EVALUABILITY ARCHITECTURE COMPETITOR
  section is absent if this STOP condition is not resolved.
- [Architecture-B]: without the emit-close terminal table, [specific criterion] is partially
  enforced without independent production -- the Architecture-B competitor entry in the
  EVALUABILITY ARCHITECTURE COMPETITOR section is absent if this STOP condition is not
  resolved.

**NON-REDUNDANCY DECLARATION:** The pre-emit gate enforces C-44 as a pre-Phase-9 structural
condition. The emit-close terminal table enforces C-43 as an emit-close requirement. These
are non-redundant: a rubric satisfying the gate condition while omitting the terminal table
fails C-43; a rubric satisfying the terminal table while omitting the gate fails C-44. Each
is independently necessary.

---

### ROLE: DUAL AUDITOR

Two audit tracks run sequentially.

**Audit Track 1 -- Criterion quality (all criteria):**

```
| C-NN | Text: D/C/CC | Pass: L/O/Q | Status |
```

- D = Direction (Y/N), C = Contrast (Y/N), CC = Causal chain (Y/N)
- L = Location (Y/N), O = Observable (Y/N), Q = No-qualitative (Y/N)

**Audit Track 2 -- Structural verification:**

> **TIER-BLIND CATEGORIZER** -- The standard category-distribution audit reads each
> criterion's Category field, confirms the field is present and non-empty, and notes that
> multiple category names appear across the rubric. It does not separate assignments by tier
> (essential / recommended / aspirational), does not compute a majority category per tier,
> and does not check whether different tiers have different majority categories. A rubric
> where essential criteria are predominantly "correctness" and aspirational criteria are also
> predominantly "correctness" passes the standard audit: both tiers assign valid category
> names, variety exists in the rubric overall. The tier convergence is invisible to the
> standard check. From the description above, derive what the category-distribution divergence
> check must verify before reading the check below.

1. **Category distribution per tier:**
   ```
   Essential:    [category] x[N] -- majority: [category]
   Recommended:  [category] x[N] -- majority: [category]
   Aspirational: [category] x[N] -- majority: [category]
   ```
   Fewer than 2 of 3 tiers with distinct majority categories requires revision before Emit.

2. **Scoring section**: composite formula, denominator, golden threshold, PARTIAL (score +
   earn conditions), named-tier table supplementing formula.

3. **Competitor coverage bijection**: one block per novel aspirational criterion.

4. **Anchor chain**: REFERENCE ANCHOR Falls-short populated, Consumer names ROLE: MECHANISM
   DEFINER.

5. **Gate chain**: DEFINER OUTPUT GATE complete (both templates, no additional content,
   embedded STOP); MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL; BUILDER
   ASPIRATIONAL entry quotes both gate artifacts verbatim; PHASE-LOCALITY RULE no prohibited-
   zone violations; TIER-BLIND CATEGORIZER inline at category-count step, canonical format.

6. **PAIRED EXTENSION EXAMPLES**: BASELINE PAIRED EXTENSION EXAMPLE DERIVATION present with
   Pair A (C-51+C-53) and Pair B (C-52+C-54) combined-form examples, each with quoted
   combined expression and joint satisfiability confirmation.

#### CRITERION-ID NAMED FORM STEPS

For each form-embedding criterion, perform a dedicated named step identifying the criterion
by ID, stating both the compliant form and the non-compliant form, and providing a Flag
condition:

**Step C-53 form verification:**
- **Criterion:** C-53 (verbatim gate identifier embedded in sufficiency clause)
- **Compliant form:** Phase 9 PREREQUISITE sufficiency clause contains a verbatim evaluability
  gate identifier token (e.g., "EVALUABILITY GATE") embedded within the body of the
  sufficiency assertion itself, not only in a co-located annotation.
- **Non-compliant form:** sufficiency clause uses only generic language (e.g., "a reader can
  confirm that gate completion is verifiable from this PREREQUISITE line") without embedding
  the specific gate identifier token. This non-compliant form passes C-48 (independence
  boundary declaration present) while failing C-53 (gate identifier not verbatim-embedded).
- **Flag condition:** Flag FAIL if Phase 9 PREREQUISITE sufficiency clause omits the verbatim
  gate identifier. The compliant/non-compliant distinction is form-level: both forms have the
  same structural position and the same logical content, but only the compliant form embeds
  the identifier as a verbatim token within the sufficiency clause itself.

**Step C-54 form verification:**
- **Criterion:** C-54 (specific absent element named in STOP consequence clause)
- **Compliant form:** each Architecture-labeled STOP consequence clause names the specific
  structural element within the affected declaration that the predicate failure leaves absent
  (e.g., "the Architecture-A competitor entry in the NON-REDUNDANCY DECLARATION is absent").
- **Non-compliant form:** STOP consequence names only the section heading without the absent
  element (e.g., "the NON-REDUNDANCY DECLARATION is incomplete"). This non-compliant form
  passes C-52 (section heading named) while failing C-54 (absent element not named). The
  distinction is form-level: both forms name the affected section, but only the compliant
  form names the specific absent element.
- **Flag condition:** Flag FAIL if any Architecture-labeled STOP consequence clause omits
  the specific absent element name. Scan all STOP consequence clauses in the NON-REDUNDANCY
  DECLARATION for element-name tokens.

---

### PHASE 9 -- EMIT

**PREREQUISITE: EVALUABILITY GATE complete** -- a reader can confirm that EVALUABILITY GATE
is complete by reading this PREREQUISITE line alone, without reading the body of ROLE:
EVALUABILITY AUDITOR.

Produce the final rubric in order:

1. Essential criteria (C-01 through C-NN)
2. Recommended criteria
3. Aspirational criteria
4. Scoring section

**Scoring section must include:**
- Composite formula (Essential score + Recommended score + Aspirational score)
- Denominator (/NN where NN = total criterion count)
- Named-tier table supplementing the composite formula:

  | Tier | Weight | Count | Max |
  |------|--------|-------|-----|
  | Essential    | 1.0 | [N] | [N] |
  | Recommended  | 0.5 | [N] | [N/2] |
  | Aspirational | 0.25 | [N] | [N/4] |

- Golden threshold (>= NN)
- PARTIAL: score value AND earn conditions

**Per-criterion evaluability declaration (emit-close terminal table):**

| C-NN | Artifact | Scan method | Excluded from verification path |
|------|----------|-------------|----------------------------------|
| [structural criteria only] | [named section block] | [method] | [excluded content] |

This table is complete when every structural criterion has a row. A partial table (some
structural criteria missing rows) fails C-43 even if the EVALUABILITY GATE passed.

**Emit manifest check** -- the rubric is not complete until all are verified:

| Check | Status |
|-------|--------|
| DEFINER OUTPUT GATE satisfied (both templates, no additional content) | |
| MECHANISM DEFINER GATE satisfied (independence map complete, all C-NN cited) | |
| REFERENCE ANCHOR Falls-short populated | |
| REFERENCE ANCHOR Consumer names ROLE: MECHANISM DEFINER | |
| MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL | |
| BUILDER ASPIRATIONAL entry quotes both gate artifacts verbatim | |
| PHASE-LOCALITY RULE: no competitor in any of the three prohibited zones | |
| TIER-BLIND CATEGORIZER: inline at category-count step, canonical format, one check governed | |
| ISOLATION AUDIT complete (all criteria flagged, no failing flags remaining) | |
| Category diversity: >= 3 distinct categories across full rubric | |
| Aspirational tier count: 1-2 criteria | |
| PARTIAL handling stated with score value and earn conditions | |
| Named-tier table present in scoring section supplementing composite formula | |
| PAIRED EXTENSION EXAMPLE DERIVATION: present in BASELINE with Pair A and Pair B combined examples, each with quoted combined expression and joint satisfiability confirmation | |
| C-53 form verification step: present in Track 2, names C-53 by ID, states compliant form, states non-compliant form, states Flag condition | |
| C-54 form verification step: present in Track 2, names C-54 by ID, states compliant form, states non-compliant form, states Flag condition | |
| C-53 form: verbatim gate identifier present in Phase 9 PREREQUISITE sufficiency clause (not only generic language) | |
| C-54 form: absent element named in each Architecture-labeled STOP consequence clause (not only section heading) | |