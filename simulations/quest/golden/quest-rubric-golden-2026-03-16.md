---
skill: quest-golden
skill_target: quest-rubric
date: 2026-03-15
rounds: 20
rubric_final: quest-rubric-rubric-v21-2026-03-15.md
score: 9.96
status: GOLDEN
---

# Golden Prompt — quest-rubric

**Winning variation:** V-05 (Full Stack R20)
**Score:** 9.96 / 10 (48/49 active criteria PASS; C-38 ablated by design across all 20 rounds)
**Tied with:** V-04 (9.96) — V-05 preferred as ceiling form with verbatim canonical examples

---

## What Made It Golden

**1. Three-level form-compliance verification stack with non-overlapping defect classes.**
V-05 activates C-55 + C-56 + C-57 simultaneously: the BASELINE PAIRED EXTENSION EXAMPLE DERIVATION catches missing combined forms at instruction level; CRITERION-ID NAMED FORM STEPS in Dual Auditor Track 2 catches generic audit steps without criterion-ID discrimination; per-criterion manifest rows catch completeness-only emission gates. Each level is structurally independent — V-02 confirmed C-56 can pass while C-57 fails, proving the stack is not a cascade artifact. V-01 and V-02 each activated only one level; V-05 activates all three.

**2. Verbatim canonical combined-form examples (not procedural instructions).**
The PAIRED EXTENSION EXAMPLE DERIVATION embeds the exact quoted clause text for both co-extension pairs:
- Pair A: `"a reader can confirm that EVALUABILITY GATE is complete by reading this PREREQUISITE line alone, without reading the body of ROLE: EVALUABILITY AUDITOR"`
- Pair B: `"the Architecture-A competitor entry in the NON-REDUNDANCY DECLARATION is absent"`

A builder can verify compliance by string-comparison against their output. V-01 had the derivation step but without verbatim canonical forms — the combined examples were instructions to construct, not quotations to match. ES-R20-3 identified this as the strongest form of C-55.

**3. Criterion-ID naming in Dual Auditor Track 2.**
V-05 includes dedicated named steps `Step C-53 form verification` and `Step C-54 form verification`, each with criterion ID, compliant form, non-compliant form (including which prior criterion the non-compliant form passes while failing the target), and Flag condition. V-01 had no Track 2 form steps; V-02 had them but without BASELINE combined examples. V-05 combines both.

**4. Emit manifest per-criterion form rows.**
Two dedicated manifest rows gate emission on specific embedded-form conditions beyond structural completeness: one for C-53 (verbatim gate identifier in Phase 9 PREREQUISITE sufficiency clause) and one for C-54 (absent element named in STOP consequence clause). This creates a third independent verification mechanism above instruction-level (C-55) and audit-step level (C-56). V-04 showed the proximity cascade hypothesis was confirmed but not automatic — the manifest rows must be explicitly specified.

**5. Full R19 mechanism stack preservation under new-criteria load.**
V-05 adds three new structural mechanisms (C-55/C-56/C-57) without disrupting any prior stable criterion (C-41 through C-54 all remain PASS). ES-R20-1 confirmed joint activation is structurally non-conflicting. The ceiling is bounded only by C-38 (format-compliance STOP co-located at declaration step), which has been ablated in every round R1–R20 by design — a dedicated targeted probe is needed in a future round.

---

## Prompt Body

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

---

## Final Rubric Criteria Summary (v21)

**Denominator:** 52 active criteria (C-09 through C-60)
**Baseline for R21:** 49/52 x 10 = 9.423 (V satisfying all R20 criteria but failing C-58/59/60)

### Essential (Weight 1.0)

| ID | Name | Category |
|----|------|----------|
| C-01 | Failure-mode log precedes criteria | correctness |
| C-02 | Composite formula + denominator + threshold + PARTIAL | correctness |
| C-03 | Text field causal direction (Without Y, Z fails) | correctness |
| C-04 | Text field contrast (Not X, but Y) | correctness |
| C-05 | Pass field observable (no qualitative-only) | correctness |
| C-06 | Pass field location named | correctness |
| C-07 | Tier assignment matches failure severity | correctness |
| C-08 | Criteria grounded in target skill spec | correctness |

### Recommended (Weight 0.5)

| ID | Name | Category |
|----|------|----------|
| C-09 | Dimension field on recommended criteria | depth |
| C-10 | Failure log minimum counts met (3 blocking, 2 suboptimal) | coverage |
| C-11 | Aspirational tier count 1-2 | format |
| C-12 | Category diversity >= 3 across rubric | coverage |
| C-13 | ISOLATION AUDIT complete, no failing flags | format |
| C-14 | DIVERGENCE CHECK per-tier majority categories, >= 2 of 3 distinct | coverage |
| C-15 | Structural criteria identified for evaluability mapping | depth |
| C-16 | REFERENCE ANCHOR present with Falls-short populated | depth |

### Aspirational (Weight 0.25) — C-17 through C-60

| ID | Name | Source |
|----|------|--------|
| C-17 | Inertia test: aspirational criterion distinguishable from weaker baseline | R1/V-05 |
| C-18 | Concrete discrimination example per aspirational criterion | R1/V-04 |
| C-19 | Phase-gate enforcement: STOP conditions block phase entry | R1/V-01 |
| C-20 | Calibration pair lifecycle position declared | R2/V-03 |
| C-21 | Sub-step output sequencing declared | R2/V-03 |
| C-22 | Multi-level gate architecture (nested gates) | R2/V-03 |
| C-23 | Audit role separation (builder vs auditor) | R2/V-05 |
| C-24 | Audit trail captures reasoning (not just verdict) | R2/V-05 |
| C-25 | Named-block artifact architecture | R3/V-02/V-04 |
| C-26 | Gate-blocking vs retroactive-repair distinction | R3/V-02 |
| C-27 | Cross-criterion audit consolidation | R3/V-03/V-05 |
| C-28 | Structural enforcement + behavioral anti-deferral co-located | R3/V-01/V-04/V-05 |
| C-29 | Structural verification as Auditor entry gate | R4/V-05 |
| C-30 | Three-level verification chain with non-overlapping defect classes | R4/V-05 |
| C-31 | Anti-deferral prohibition at sub-step level | R4/V-05 |
| C-32 | Phase transitions marked by named section headings | R5/ES-R5-1 |
| C-33 | Cross-criterion verification produces named artifact with forward-blocking gate | R5/ES-R5-2 |
| C-34 | Scoring formula denominators explicitly stated and matched to criterion count | R5/ES-R5-3 |
| C-35 | Mechanism overview declares structural output format alongside behavioral requirement | R6/ES-R6-1 |
| C-36 | Structural verification declares phase-bounded coverage scope + deferral destination | R6/ES-R6-2 |
| C-37 | Pre-phase output skeleton declared from MECHANISMS, cross-referenced in SV | R7/ES-R7-1 |
| C-38 | Format-compliance STOP conditions co-located at declaration step | R8/ES (ablated R1-R20) |
| C-39 | Mechanism overview declares pre-phase skeleton as named mechanism with heading pattern | R8/ES-R8-1/V-05 |
| C-40 | Structural Verification opens with two-source preamble (C-38 dependent -- PARTIAL until C-38 activates) | R8/ES-R8-2/V-05 |
| C-41 | Pre-phase skeleton labeled as Phase 0 (or positional marker) in scannable phase sequence | R8/ES-R8-3/V-04/V-05 |
| C-42 | Competitor-defeat annotations co-located at mechanism introduction points | R9/ES-R9-1/V-01 |
| C-43 | Pre-phase skeleton formatted as operational tick-off checklist with live-construction tracking | R9/ES-R9-2/V-02 |
| C-44 | Competing Implementations Preamble as tabular mapping (mechanism x competing protocol x failure class) | R10/ES-R10-1/V-01 |
| C-45 | Format-compliance criterion with structural boundary enforcement | R10/ES-R10-2/V-05 |
| C-46 | Non-redundancy declaration for co-present mechanism pairs | R11/ES-R11-1 |
| C-47 | REFERENCE ANCHOR Consumer field names ROLE: MECHANISM DEFINER as blocked consumer | R12/ES-R12-1 |
| C-48 | TIER-BLIND CATEGORIZER competitor block inline at category-count step, canonical format | R13/ES-R13-1 |
| C-49 | Tier-diversity failure item in STATUS QUO COMPETITOR | R14/ES-R14-1 |
| C-50 | Named-tier table in scoring section supplementing composite formula | R15/ES-R15-1 |
| C-51 | Phase 9 PREREQUISITE sufficiency clause embeds excluded role body name | R16/ES-R16-1 |
| C-52 | Architecture-labeled STOP consequence clause embeds section heading name | R17/ES-R17-1 |
| C-53 | Phase 9 PREREQUISITE sufficiency clause embeds verbatim gate identifier | R18/ES-R18-1 |
| C-54 | Architecture-labeled STOP consequence clause names specific absent element | R19/ES-R19-1 |
| C-55 | BASELINE declares combined-form joint satisfiability for co-extension pairs | R20/ES-R20 |
| C-56 | Dual Auditor Track 2 names form-embedding criteria by ID with compliant/non-compliant forms | R20/ES-R20 |
| C-57 | Emit manifest includes per-criterion form-verification rows | R20/ES-R20 |
| C-58 | BASELINE combined-form examples are verbatim canonical clause expressions (not procedural instructions) | R20/ES-R20-3/V-05 |
| C-59 | Form-compliance stack architecture declared as three-level system with non-overlapping defect classes and structural independence asserted | R20/ES-R20-2/V-04/V-05 |
| C-60 | Form-compliance stack criteria include explicit compatibility declaration asserting non-conflict with C-41-C-54 | R20/ES-R20-1/V-04/V-05 |

---

## Persistent Gap (R21 Target)

**C-38** (format-compliance STOP conditions co-located at declaration step) has been ablated
in every round R1-R20. It is the sole criterion that has never been activated. **C-40**
(two-source SV preamble) remains PARTIAL because it depends structurally on C-38.

A dedicated targeted probe is required -- not bundled into a full-stack variation.
