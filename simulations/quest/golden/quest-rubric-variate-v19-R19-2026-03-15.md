# quest-rubric Variate -- Round 19 (Against rubric v19)
**Date:** 2026-03-15
**Rubric:** v19 (C-01--C-54; denominator /46; adds C-53: Phase 9 PREREQUISITE sufficiency
clause embeds verbatim evaluability gate identifier within the sufficiency clause itself;
C-54: Architecture-labeled STOP consequence clause names the specific structural element
within the affected declaration that the predicate failure leaves absent)
**Target criteria:** C-53 (new, ES-R18-1/V-01); C-54 (new, ES-R18-2/V-02);
C-51 (stability confirmation); C-52 (stability confirmation)

**Round 19 design note:** v19 adds C-53 and C-54. The R18 V-05 full stack satisfies C-01
through C-52 (44 aspirational criteria). Against v19, R18 V-05 scores 44/46 x 10 = 9.565 --
failing only C-53 and C-54. R19 design goals:
(1) probe C-53 via three variations (V-03 single-axis, V-04 combined, V-05 full stack) that
explicitly embed the verbatim gate identifier within the Phase 9 PREREQUISITE sufficiency
clause;
(2) probe C-54 via two variations (V-04, V-05) that name the specific absent structural
element in each Architecture-labeled STOP consequence clause in the NON-REDUNDANCY
DECLARATION;
(3) confirm C-51 and C-52 stability under role-sequence and output-format axes not
previously tested in combination with those two criteria.

**Structural requirements for C-53 and C-54:**

C-53 requires the Phase 9 EMIT PREREQUISITE to read (in substance):
  "PREREQUISITE: EVALUABILITY GATE is complete. A reader can confirm that EVALUABILITY GATE
   is complete by reading this PREREQUISITE line alone, without reading the body of
   ROLE: EVALUABILITY AUDITOR."
  The verbatim identifier "EVALUABILITY GATE" must appear within the sufficiency clause
  ("A reader can confirm that EVALUABILITY GATE is complete..."), not only as the gate-ID
  annotation in the PREREQUISITE header line. A PREREQUISITE that reads "EVALUABILITY GATE
  complete. A reader can confirm Phase 9 was properly gated by reading this line alone,
  without reading ROLE: EVALUABILITY AUDITOR" fails C-53: the sufficiency clause ("properly
  gated") does not embed the verbatim identifier.

C-54 requires each Architecture-labeled STOP consequence in the NON-REDUNDANCY DECLARATION
  to read (in substance): "the Architecture-A competitor entry in the NON-REDUNDANCY
  DECLARATION is absent" -- NOT "the NON-REDUNDANCY DECLARATION is incomplete." The element
  within the declaration (the competitor entry) must be named, not only the declaration
  itself. A consequence that satisfies C-52 (names the declaration by heading) but uses
  declaration-level language fails C-54.

---

**Variation axes used in R19:**

| # | Axis | C-53 probe | C-54 probe | C-51 | C-52 | C-49 |
|---|------|-----------|-----------|------|------|------|
| V-01 | Role sequence (MECHANISM DEFINER before Phase 4) | Carried (R18 level -- fails C-53) | Carried (R18 level -- fails C-54) | Strong | Strong | Ablated |
| V-02 | Output format (NON-REDUNDANCY DECLARATION as numbered list) | Carried | Test -- numbered format vs. Architecture-label blocks | Strong | Test | Strong |
| V-03 | Lifecycle emphasis (Phase 9 PREREQUISITE expanded -- C-53 single-axis) | Strong -- verbatim gate ID within sufficiency clause | Ablated -- no NON-REDUNDANCY DECLARATION | Ablated | Ablated | Ablated |
| V-04 | Role sequence + Lifecycle emphasis (C-53 + C-54 combined) | Strong | Strong | Strong | Strong | Ablated |
| V-05 | Full stack R19 (all R18 V-05 + C-53 + C-54) | Strong | Strong | Strong | Strong | Strong |

---

## Round 19 Variation Map

| Variation | C-53 | C-54 | C-51 | C-52 | C-49 | C-48 | C-47 | C-46 | C-45 | C-43/44 | C-41 | C-42 | C-39 | C-38 | Notes |
|-----------|------|------|------|------|------|------|------|------|------|---------|------|------|------|------|-------|
| V-01 | Carried | Carried | Strong | Strong | Ablated | Strong | Strong | Strong | Strong | Strong | Ablated | Ablated | Strong | Ablated | Single-axis sequence; MECHANISM DEFINER before Phase 4; evaluability architecture present at R18 level; tests C-51/C-52 stability under sequence change |
| V-02 | Carried | Test | Strong | Test | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Ablated | Single-axis format; NON-REDUNDANCY DECLARATION as numbered list; tests whether format change breaks C-47/C-52/C-54; C-49 strong via STATUS QUO COMPETITOR |
| V-03 | Strong | Ablated | Ablated | Ablated | Ablated | Ablated | Ablated | Strong | Strong | Strong | Ablated | Ablated | Strong | Ablated | Single-axis C-53 probe; Phase 9 PREREQUISITE with verbatim gate ID in sufficiency clause; all NON-REDUNDANCY / Architecture elements absent; isolates C-53 signal |
| V-04 | Strong | Strong | Strong | Strong | Ablated | Strong | Strong | Strong | Strong | Strong | Strong | Ablated | Strong | Ablated | Combined role-sequence + lifecycle; MECHANISM DEFINER before Phase 4 + C-53 Phase 9 PREREQUISITE + C-54 NON-REDUNDANCY DECLARATION; STATUS QUO COMPETITOR absent |
| V-05 | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Full stack ceiling; all R18 V-05 elements + C-53 + C-54; if passes all C-01--C-54, composite = 46/46 x 10 = 10.0 |

---

## V-01 -- Role Sequence

**Axis:** Role sequence -- ROLE: MECHANISM DEFINER is promoted to run immediately after
PHASE 3 (essential criteria only), before PHASE 4 (recommended criteria). The independence
map is built on the essential-criteria gap profile alone. Recommended criteria are drafted
in PHASE 4, after the independence map is complete. ROLE: BUILDER ASPIRATIONAL reads the
independence map (derived from essential gaps) and the Falls-short dimension from the
REFERENCE ANCHOR; recommended criteria are available as supplementary input but were not
in scope when the map was built.

All R18 V-05 evaluability architecture structures are carried at R18 level: ROLE:
EVALUABILITY AUDITOR produces EVALUABILITY GATE artifact before Phase 9; EVALUABILITY
ARCHITECTURE -- NON-REDUNDANCY DECLARATION with Architecture A/B labeled STOP conditions
(satisfying C-47, C-50, C-51-level, C-52-level, but NOT C-53 or C-54); Phase 9 EMIT
PREREQUISITE with independence boundary + sufficiency clause naming excluded role (C-51,
C-52 level) but without verbatim gate identifier embedded within the sufficiency clause
(C-53 ablated). STATUS QUO COMPETITOR opening block absent. C-38 ablated.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will show ROLE: MECHANISM DEFINER output between Phase 3 and Phase 4, with the independence map built on essential-criteria gaps alone; any rubric where ROLE: MECHANISM DEFINER output appears after Phase 4 falsifies the sequence hypothesis; the primary falsification signal is a rubric where the independence map follows the full recommended-criteria section. | Promoting the independence map before recommended criteria may narrow the aspirational tier: the map is built on essential gaps only, so aspirational criteria may address only essential-class failures; recommended-class failures are invisible to the independence map in V-01; the secondary test is whether C-46, C-47 are stable when MECHANISM DEFINER GATE and REFERENCE ANCHOR are separated by the full recommended-criteria phase. | C-51 and C-52 are the primary stability tests: the evaluability architecture (NON-REDUNDANCY DECLARATION, Phase 9 PREREQUISITE) is carried from R18 V-05; if C-51 and C-52 both pass despite the sequence change, the evaluability architecture is robust to role-sequence variation. |

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

Generate skill-specific templates from the skill spec.

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form -- wrong implementation with same surface behavior as Y]
```

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form is any
Text that locates causality in the wrong form's consequence: "X causes failure," "failure
occurs when X is present," "X leads to Z," and all semantic equivalents.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

DEFINER OUTPUT GATE is satisfied when: Text template and Pass template are both present in
slot-fillable form, derived from the skill spec, with no additional content. Nothing else.
STOP if this role's output contains anything beyond the two required templates.

ROLES: PHASE 3 and PHASE 4 cannot begin until DEFINER OUTPUT GATE is satisfied.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied when:** Text template and Pass template are
both present in slot-fillable form, derived from the skill spec.

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

Each criterion requires five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: Apply CRITERION DEFINER Text template. "Without [Y], the artifact [fails]
  because [Z]. Not [X], but [Y]."
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass**: Apply CRITERION DEFINER Pass template. No "is clear" or "adequately covers" as
  sole observable.

---

### ROLE: MECHANISM DEFINER

**This role runs after PHASE 3 and before PHASE 4.**

**PREREQUISITE:** REFERENCE ANCHOR is not yet required for this early independence map pass.
Read the essential criteria from Phase 3. For each anticipated aspirational criterion,
identify the structural mechanism it would require. Produce a draft independence map.

**Independence map format:**

```
Mechanism        | Independence             | Affects criterion
[mechanism name] | Yes -- affects C-NN only | [TBD]
```

Each row must be mutually exclusive. Removing any one mechanism leaves exactly one criterion
failing. This is a draft: mechanism rows may be refined after Phase 4 adds recommended
criteria, but no new mechanisms may be added after Phase 4.5.

**MECHANISM DEFINER GATE is satisfied when:** Independence map is complete with "Yes --
affects C-NN only" in every row, and every anticipated aspirational gap has a mechanism row.
Nothing else. STOP if this role's output contains anything beyond the independence map.

ROLE: BUILDER ASPIRATIONAL cannot begin until this gate is satisfied.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied when:** Text template and Pass template are
both present in slot-fillable form.

Draft from suboptimal failure modes. Apply Text template and Pass template to each criterion.
Pass conditions test degree, precision, or specificity -- not whether an element exists.

Each criterion: same five fields as Phase 3. Required annotation:
**Dimension:** [degree | precision | specificity].

**After drafting recommended criteria:** review the independence map from ROLE: MECHANISM
DEFINER. If any recommended criterion opens a new aspirational gap not covered by an
existing map row, add a new row now.

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

#### ISOLATION AUDIT

For each criterion from Phases 3 and 4, run the isolation audit.

**Text field checks (3):**
1. **Direction**: does Text locate causality in Y's absence?
2. **Contrast**: does Text name the rejected form X alongside Y?
3. **Causal chain**: does Text name the downstream consequence Z?

**Pass field checks (3):**
4. **Location**: does Pass name an artifact location, field, or section?
5. **Observable**: does Pass name a specific count, token, or structural property?
6. **No qualitative-only**: does Pass avoid bare qualitative language without an anchor?

Required format:
```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

STOP if any criterion fails one or more flags -- revise before DIVERGENCE CHECK.

#### DIVERGENCE CHECK

Count category assignments per tier. Identify majority category per tier.

```
Essential tier:     [category] x[N] ... -- majority: [category]
Recommended tier:   [category] x[N] ... -- majority: [category]
Aspirational tier:  [category] x[N]     -- majority: [category]
```

STOP if fewer than 2 of 3 tiers have distinct majority categories.

---

### PHASE 5 -- REFERENCE ANCHOR

**Do not proceed to PHASE 5 until Phase 4.5 is complete.**

Identify a specific competitor or prior-version rubric that passes essential and recommended
criteria (C-01--C-08). Record where it falls short of the aspirational bar.

```
REFERENCE ANCHOR:
  Reference:   [specific competitor or prior-version identifier]
  Passes:      [criteria satisfied -- at minimum C-01 through C-08]
  Falls-short: [exact dimension on which it fails to meet the aspirational bar]
  Consumer:    ROLE: MECHANISM DEFINER cannot begin until this anchor is complete.
               The Falls-short dimension defines the aspirational gap that the
               Mechanism Definer's independence map must cover.
```

STOP if this REFERENCE ANCHOR block is absent before ROLE: BUILDER ASPIRATIONAL begins,
or if the Falls-short field is blank, or if the Consumer field does not name
ROLE: MECHANISM DEFINER as the blocked consumer.

---

### PHASE 5.5 -- BUILDER ASPIRATIONAL PRECONDITION CHECK

Before ROLE: BUILDER ASPIRATIONAL begins, confirm:
1. DEFINER OUTPUT GATE satisfied (both templates present, no additional content).
2. MECHANISM DEFINER GATE satisfied (independence map complete, all rows "Yes").
3. REFERENCE ANCHOR complete (Falls-short populated; Consumer field names
   ROLE: MECHANISM DEFINER as the blocked consumer).

STOP if any prerequisite is unsatisfied.

---

### ROLE: BUILDER ASPIRATIONAL

**Input required:**

- **CRITERION DEFINER GATE**: Text template and Pass template in slot-fillable form.
- **MECHANISM DEFINER GATE**: Independence map with all C-NN citations populated.

**ROLE: BUILDER ASPIRATIONAL cannot begin unless both gate artifacts exist.**

Draft aspirational criteria that close the exact gap named in the REFERENCE ANCHOR
Falls-short field. One criterion per mechanism in the independence map.

**Aspirational tier count: 1-2 criteria.** STOP if you draft more than 2 aspirational
criteria. Rewrite to stay within range.

Each criterion requires five fields: ID, Text (slot-filled), Weight: aspirational, Category,
Pass (slot-filled).

Required annotation: **Gap closed:** [independence map mechanism row citation].

---

### ROLE: EVALUABILITY AUDITOR

**This role runs after ROLE: BUILDER ASPIRATIONAL and before PHASE 9.**

For each structural criterion in the rubric (any criterion whose Pass condition references
a named section, block, or artifact), declare:

```
EVALUABILITY DECLARATION -- [criterion ID]:
  Artifact:    [named section or block that enables independent verification]
  Scan method: [heading-scan | content-scan | count-check]
  Excluded:    [instruction content not required to verify compliance -- e.g.,
               "ROLE: MECHANISM DEFINER body not required"]
```

EVALUABILITY GATE is satisfied when: All structural criteria have a completed
EVALUABILITY DECLARATION with Artifact, Scan method, and Excluded fields all populated.
Nothing else. STOP if any declaration is missing a field.

PHASE 9 cannot begin until EVALUABILITY GATE is satisfied.

---

### EVALUABILITY ARCHITECTURE -- NON-REDUNDANCY DECLARATION

Declare the two enforcement points for the evaluability architecture and confirm they are
non-redundant. Use Architecture A/B labels anchored to the EVALUABILITY ARCHITECTURE
COMPETITOR section (below).

```
Architecture A: [pre-Phase-9 gate enforcement -- EVALUABILITY GATE blocking
                Phase 9 entry until all EVALUABILITY DECLARATIONs are complete]
Architecture B: [emit-close terminal table enforcement -- per-criterion evaluability
                mapping at Phase 9 close, independently verifiable by heading scan]
```

**STOP: If Architecture-A gate does not enforce pre-Phase-9 sequencing -- if Phase 9 can
begin before all EVALUABILITY DECLARATIONs are complete -- the Architecture-A gate entry
in the NON-REDUNDANCY DECLARATION is absent. Do not proceed to Phase 9.**

**STOP: If Architecture-B terminal table does not appear as an independently produced
artifact at Phase 9 close -- if the per-criterion evaluability mapping is embedded inline
in instructions rather than produced as a named block -- the Architecture-B terminal table
entry in the NON-REDUNDANCY DECLARATION is absent. Do not proceed to Phase 9.**

#### EVALUABILITY ARCHITECTURE COMPETITOR

> **SINGLE-POINT EVALUABILITY AUDITOR** -- A rubric where the evaluability architecture
> has one enforcement point: the EVALUABILITY AUDITOR role runs and declares evaluability
> for all criteria at once, without a pre-Phase-9 gate or an emit-close terminal table.
> The single auditor is the only mechanism checking evaluability compliance. From this
> description, derive why two non-redundant enforcement points are required before reading
> the Architecture A/B declarations above.

---

### ROLE: DUAL AUDITOR

Run two audit tracks sequentially.

**Audit Track 1 -- Criterion quality (all criteria):**

Output as per-criterion table:

```
| C-NN | Text: D/C/CC | Pass: L/O/Q | Status |
```

- D = Direction (Y/N), C = Contrast (Y/N), CC = Causal chain (Y/N)
- L = Location (Y/N), O = Observable (Y/N), Q = No-qualitative (Y/N)

**Audit Track 2 -- Structural verification:**

1. **Category distribution**: Count category assignments per tier. Record:
   ```
   Essential: [category] x[N] -- majority: [category]
   Recommended: [category] x[N] -- majority: [category]
   Aspirational: [category] x[N] -- majority: [category]
   ```
   STOP if fewer than 2 of 3 tiers have distinct majority categories.

2. **Scoring section**: Confirm composite formula, denominator (/NN annotated with
   criterion ID range), golden threshold, PARTIAL handling (score value + earn conditions).

3. **Competitor coverage bijection**: For each novel aspirational criterion, confirm
   exactly one competitor block accompanies it.

4. **Anchor chain**: Confirm REFERENCE ANCHOR has Falls-short populated and Consumer
   field naming ROLE: MECHANISM DEFINER.

5. **Gate chain**: Confirm:
   - DEFINER OUTPUT GATE ends with exclusion terminal and embedded STOP
   - MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL as blocked consumer
   - EVALUABILITY GATE satisfied before Phase 9 opens

6. **Evaluability architecture**: Confirm NON-REDUNDANCY DECLARATION present with
   Architecture A and B labels; each STOP consequence names the affected declaration
   by its exact heading; Consumer field in REFERENCE ANCHOR names ROLE: MECHANISM
   DEFINER.

---

### PHASE 9 -- EMIT

**PREREQUISITE: EVALUABILITY GATE is complete. A reader can confirm Phase 9 was properly
gated by reading this PREREQUISITE line alone, without reading the body of
ROLE: EVALUABILITY AUDITOR.**

Produce the final rubric in this order:

1. Essential criteria (C-01 through C-NN)
2. Recommended criteria
3. Aspirational criteria
4. Scoring section

**Scoring section must include:**
- Composite formula
- Denominator (/NN, annotated: "/* C-09 through C-NN */")
- Golden threshold (>= NN)
- PARTIAL: score value and earn conditions

**Emit manifest check** -- do not emit until all verified:

| Check | Status |
|-------|--------|
| DEFINER OUTPUT GATE satisfied (both templates, no additional content) | |
| MECHANISM DEFINER GATE satisfied (independence map complete, all C-NN cited) | |
| REFERENCE ANCHOR Falls-short populated | |
| REFERENCE ANCHOR Consumer names ROLE: MECHANISM DEFINER | |
| MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL | |
| EVALUABILITY GATE satisfied (all structural criteria have EVALUABILITY DECLARATION) | |
| NON-REDUNDANCY DECLARATION present with Architecture A and B labels | |
| NON-REDUNDANCY DECLARATION: each STOP consequence names declaration by exact heading | |
| ISOLATION AUDIT complete (all criteria flagged, no FAIL remaining) | |
| Category diversity: >= 3 distinct categories across full rubric | |
| Aspirational tier count: 1-2 criteria | |
| Scoring denominator annotated with criterion ID range | |
| PARTIAL handling stated with score value and earn conditions | |

---

## V-02 -- Output Format

**Axis:** Output format -- the NON-REDUNDANCY DECLARATION is restructured as a numbered
prose list (1. Architecture-A: ..., 2. Architecture-B: ...) instead of bold-header labeled
blocks (Architecture A: ..., Architecture B: ...). Architecture labels are inline rather
than heading-level. STOP conditions appear as parenthetical enforcement notes at the end
of each numbered item.

All R18 V-05 evaluability architecture structures are carried. STATUS QUO COMPETITOR
opening block present with tier-diversity failure in failure list (C-49 strong). C-53
carried (Phase 9 PREREQUISITE with sufficiency clause naming excluded role -- C-51 level,
NOT embedding verbatim gate identifier within the clause). C-38 ablated.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will express the NON-REDUNDANCY DECLARATION as a numbered list with inline Architecture labels; the primary falsification signal is a rubric that reverts to bolded Architecture-A / Architecture-B header blocks despite the numbered-list instruction. | The numbered format may obscure the Architecture-label structure required for C-47 (Architecture A/B labeled anchors resolving to COMPETITOR section entries): if the Architecture label is inline rather than a standalone header, a heading-scan may not detect it as a distinct structural anchor; the secondary test is whether C-52 (STOP consequence names declaration by heading) is stable under the inline label format -- the STOP consequence clause naming requirement applies regardless of how the Architecture label is presented. | C-54 is the primary new at-risk criterion: C-54 requires element-level naming within the STOP consequence (not tested in V-02 -- C-54 is carried at C-52 level, naming only the declaration); the test isolates whether the numbered format itself interacts with C-52 (declaration-level naming) before probing C-54 (element-level naming) in V-04/V-05. |

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
  properties, not consequence of their absence; the Builder cannot distinguish "X causes
  failure" from "without Y, failure occurs."
- Fails to enforce Pass observability by template -- Pass conditions include "is clear,"
  "adequately covers," "is well-structured" as sole observables.
- Fails to name a specific reference anchor with a Falls-short dimension.
- Fails to verify mechanism independence.
- Fails to make role dependencies bidirectionally traceable.
- Fails to verify category diversity by tier.

**From the description above, derive what the required rubric-building procedure must do --
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

**This role runs after Phase 1. Do not write any criterion fields during this role.**

Generate skill-specific templates from the skill spec.

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form -- wrong implementation with same surface behavior as Y]
```

Causal direction rule: "Without Y, Z fails" is the required form.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

DEFINER OUTPUT GATE is satisfied when: Text template and Pass template are both present in
slot-fillable form, derived from the skill spec, with no additional content. Nothing else.
STOP if this role's output contains anything beyond the two required templates.

ROLES: PHASE 3 and PHASE 4 cannot begin until DEFINER OUTPUT GATE is satisfied.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied when:** Text template and Pass template are
both present in slot-fillable form.

Draft from blocking failure modes. Apply the Text template and Pass template to each
criterion.

Each criterion requires five fields: ID (C-NN), Text (slot-filled), Weight: essential,
Category, Pass (slot-filled). No "is clear" or "adequately covers" as sole observable.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied.**

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

Each criterion: same five fields. Required annotation:
**Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT

#### ISOLATION AUDIT

For each criterion from Phases 3 and 4:

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

STOP if any flag is N -- revise before DIVERGENCE CHECK.

#### DIVERGENCE CHECK

Count category assignments per tier:
```
Essential tier:     [category] x[N] ... -- majority: [category]
Recommended tier:   [category] x[N] ... -- majority: [category]
Aspirational tier:  [category] x[N]     -- majority: [category]
```
STOP if fewer than 2 of 3 tiers have distinct majority categories.

---

### PHASE 5 -- REFERENCE ANCHOR

**Do not proceed to PHASE 5 until Phase 4.5 is complete.**

```
REFERENCE ANCHOR:
  Reference:   [specific competitor or prior-version identifier]
  Passes:      [criteria satisfied -- at minimum C-01 through C-08]
  Falls-short: [exact dimension on which it fails to meet the aspirational bar]
  Consumer:    ROLE: MECHANISM DEFINER cannot begin until this anchor is complete.
               The Falls-short dimension defines the aspirational gap that the
               Mechanism Definer's independence map must cover.
```

STOP if Falls-short blank or Consumer does not name ROLE: MECHANISM DEFINER.

---

### PHASE-LOCALITY RULE

The following placement zones are prohibited for all competitor blocks:

1. **Preamble zone**: any block appearing before any construction phase (Phases 3, 4, 6).
2. **Shared-operating-principles zone**: any block preceding more than one construction step.
3. **Multi-criterion zone**: any combined block governing more than one criterion.

A competitor is correctly placed if and only if it does not appear in any of the three
enumerated prohibited zones. This rule is a required Emit manifest verification target.

---

### ROLE: MECHANISM DEFINER

**This role runs after Phase 4.5 and before ROLE: BUILDER ASPIRATIONAL.**

**PREREQUISITE:** REFERENCE ANCHOR is complete (Falls-short populated; Consumer names
ROLE: MECHANISM DEFINER as the blocked consumer).

Produce independence map:

```
Mechanism        | Independence             | Affects criterion
[mechanism name] | Yes -- affects C-NN only | [TBD or C-NN]
```

Each row mutually exclusive. If any row is "No": stop, redesign, restart.

**MECHANISM DEFINER GATE is satisfied when:** Map complete, all rows "Yes -- affects C-NN
only". Nothing else. STOP beyond map.

ROLE: BUILDER ASPIRATIONAL cannot begin until this gate is satisfied.

---

### ROLE: BUILDER ASPIRATIONAL

**Input required:** CRITERION DEFINER GATE (templates) + MECHANISM DEFINER GATE (map).
**ROLE: BUILDER ASPIRATIONAL cannot begin unless both gate artifacts exist.**

Draft 1-2 aspirational criteria from the Falls-short dimension. STOP if more than 2.

If introducing a competitor:

> **[COMPETITOR NAME]** -- [description of wrong implementation]. From the description
> above, derive the required implementation before reading the positive definition below.

Place each competitor block immediately before the criterion. PHASE-LOCALITY RULE applies.

Five fields + **Gap closed:** [independence map row citation, format: "Yes -- affects C-NN
only"].

---

### ROLE: EVALUABILITY AUDITOR

**This role runs after ROLE: BUILDER ASPIRATIONAL and before PHASE 9.**

For each structural criterion, declare:

```
EVALUABILITY DECLARATION -- [criterion ID]:
  Artifact:    [named section or block]
  Scan method: [heading-scan | content-scan | count-check]
  Excluded:    [instruction content not required to verify compliance]
```

EVALUABILITY GATE is satisfied when: All structural criteria have a completed
EVALUABILITY DECLARATION with all three fields populated. STOP if any field is missing.

PHASE 9 cannot begin until EVALUABILITY GATE is satisfied.

---

### EVALUABILITY ARCHITECTURE -- NON-REDUNDANCY DECLARATION

Declare the two enforcement points as a numbered list. Each item names its Architecture
label inline and ends with an enforcement STOP.

```
1. Architecture-A (pre-Phase-9 gate): EVALUABILITY GATE blocks Phase 9 entry until
   all EVALUABILITY DECLARATIONs are complete. (STOP: if Architecture-A gate is absent
   or bypassed, the NON-REDUNDANCY DECLARATION is incomplete -- rewrite before Phase 9.)

2. Architecture-B (emit-close terminal): per-criterion evaluability mapping appears as
   a named block at Phase 9 close, independently verifiable by heading scan without
   reading role instruction bodies. (STOP: if Architecture-B terminal block is absent,
   the NON-REDUNDANCY DECLARATION is incomplete -- rewrite before Phase 9.)
```

#### EVALUABILITY ARCHITECTURE COMPETITOR

> **SINGLE-POINT EVALUABILITY AUDITOR** -- One enforcement point only: the EVALUABILITY
> AUDITOR role produces one audit result without a pre-Phase-9 gate or an emit-close
> terminal. From the description above, derive why two non-redundant enforcement points
> are required before reading the numbered Architecture list above.

---

### ROLE: DUAL AUDITOR

Run two audit tracks sequentially.

**Audit Track 1:** Per-criterion table `| C-NN | Text: D/C/CC | Pass: L/O/Q | Status |`.

**Audit Track 2 -- Structural verification:**

> **TIER-BLIND CATEGORIZER** -- The standard category-distribution audit reads each
> criterion's Category field across all criteria without separating by tier. It does not
> compute a majority category per tier and does not check whether different tiers have
> different majority categories. A rubric where essential and aspirational criteria are
> both predominantly "correctness" passes the standard audit. From the description above,
> derive what the tier-aware divergence check must verify before reading the check below.

1. **Category distribution per tier:**
   ```
   Essential: [category] x[N] -- majority: [category]
   Recommended: [category] x[N] -- majority: [category]
   Aspirational: [category] x[N] -- majority: [category]
   ```
   STOP if < 2 tiers have distinct majority categories.

2. **Scoring section:** composite formula + denominator (annotated "/NN /* C-09 through
   C-NN */") + golden threshold + PARTIAL (score value + earn conditions).

3. **Competitor coverage bijection.**

4. **Anchor chain:** Falls-short populated, Consumer names ROLE: MECHANISM DEFINER.

5. **Gate chain:**
   - DEFINER OUTPUT GATE ends with exclusion terminal + embedded STOP
   - MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL
   - BUILDER ASPIRATIONAL entry quotes MECHANISM DEFINER GATE verbatim
   - PHASE-LOCALITY RULE: no competitor in any of the three prohibited zones
   - TIER-BLIND CATEGORIZER: inline before category-count step, ends with derivation
     instruction, governs exactly one check

6. **Evaluability architecture:** NON-REDUNDANCY DECLARATION present as numbered list;
   Architecture-A and Architecture-B labels inline; each STOP consequence names
   declaration by heading.

---

### PHASE 9 -- EMIT

**PREREQUISITE: EVALUABILITY GATE is complete. A reader can confirm Phase 9 was properly
gated by reading this PREREQUISITE line alone, without reading the body of
ROLE: EVALUABILITY AUDITOR.**

Produce the final rubric: essential -> recommended -> aspirational -> scoring section.

**Scoring section must include:** composite formula, denominator (/NN annotated with
criterion ID range), golden threshold, PARTIAL (score value + earn conditions).

**Emit manifest check** -- do not emit until all verified:

| Check | Status |
|-------|--------|
| DEFINER OUTPUT GATE satisfied | |
| MECHANISM DEFINER GATE satisfied | |
| REFERENCE ANCHOR Falls-short populated + Consumer names ROLE: MECHANISM DEFINER | |
| MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL | |
| BUILDER ASPIRATIONAL entry quotes MECHANISM DEFINER GATE verbatim | |
| PHASE-LOCALITY RULE: no competitor in any prohibited zone | |
| TIER-BLIND CATEGORIZER: inline at category-count step, canonical format | |
| STATUS QUO COMPETITOR failure list: names tier-diversity verification failure | |
| EVALUABILITY GATE satisfied | |
| NON-REDUNDANCY DECLARATION present as numbered list with inline Architecture labels | |
| NON-REDUNDANCY DECLARATION: each STOP consequence names declaration by exact heading | |
| ISOLATION AUDIT complete (all criteria flagged, no FAIL remaining) | |
| Category diversity: >= 3 distinct categories across full rubric | |
| Aspirational tier count: 1-2 criteria | |
| Scoring denominator annotated with criterion ID range | |
| PARTIAL handling stated with score value and earn conditions | |

---

## V-03 -- Lifecycle Emphasis (C-53 Probe)

**Axis:** Lifecycle emphasis -- Phase 9 EMIT is given expanded structural treatment to
enforce C-53. The PREREQUISITE is explicitly structured as a three-part block: (1) gate-ID
annotation, (2) independence boundary declaration naming the excluded role body, (3)
positive sufficiency claim embedding the verbatim gate identifier within the claim text.
The prompt includes an example of the compliant form and the non-compliant form (which
satisfies C-51 but fails C-53).

No STATUS QUO COMPETITOR (C-49 ablated). No NON-REDUNDANCY DECLARATION (C-54 ablated).
No Architecture-labeled anchors (C-47, C-50, C-52 ablated). EVALUABILITY GATE present
and blocking Phase 9 (C-45 strong). MECHANISM DEFINER GATE names ROLE: BUILDER
ASPIRATIONAL (C-46 strong). REFERENCE ANCHOR Consumer names ROLE: MECHANISM DEFINER
(C-47 strong -- anchor Consumer field only, not Architecture-label NON-REDUNDANCY). C-38
ablated.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain a Phase 9 PREREQUISITE whose sufficiency clause includes the verbatim text of the gate identifier (e.g., "A reader can confirm that EVALUABILITY GATE is complete by reading this PREREQUISITE line alone, without reading the body of ROLE: EVALUABILITY AUDITOR"); the primary falsification signal is a rubric where the sufficiency clause uses generic language ("Phase 9 was properly gated") without embedding the verbatim gate identifier. | The expanded lifecycle treatment of Phase 9 may cause the model to produce a more verbose PREREQUISITE block than strictly necessary for C-53; the secondary test is whether the additional structure (example of compliant vs. non-compliant form) helps the model discriminate the C-53 requirement from the C-51 requirement (which it already satisfies). | V-03 is the control for V-04: V-03 isolates C-53 (no C-54 element); V-04 adds C-54 (NON-REDUNDANCY DECLARATION with element-absent consequences); if V-04 passes C-53 but V-03 fails it, the addition of C-54 structure interferes with the Phase 9 PREREQUISITE; if both pass, the two criteria are jointly satisfiable. |

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

Generate skill-specific templates from the skill spec.

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
```

Causal direction rule: "Without Y, Z fails." The prohibited form is any Text locating
causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section]
OBSERVABLE: [specific token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

DEFINER OUTPUT GATE is satisfied when: both templates present in slot-fillable form,
derived from spec, no additional content. STOP if anything else present.

ROLES: PHASE 3 and PHASE 4 cannot begin until DEFINER OUTPUT GATE is satisfied.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE satisfied.**

Draft from blocking failure modes. Five fields per criterion: ID, Text (slot-filled),
Weight: essential, Category, Pass (slot-filled).

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE satisfied.**

Draft from suboptimal failure modes. Five fields per criterion + **Dimension:** [degree |
precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

STOP if any flag N. Count tier majority categories. STOP if < 2 tiers distinct.

---

### PHASE 5 -- REFERENCE ANCHOR

```
REFERENCE ANCHOR:
  Reference:   [identifier]
  Passes:      [at minimum C-01 through C-08]
  Falls-short: [aspirational gap dimension]
  Consumer:    ROLE: MECHANISM DEFINER cannot begin until this anchor is complete.
```

STOP if Falls-short blank or Consumer omits ROLE: MECHANISM DEFINER.

---

### ROLE: MECHANISM DEFINER

**PREREQUISITE:** REFERENCE ANCHOR complete.

```
Mechanism        | Independence             | Affects criterion
[mechanism name] | Yes -- affects C-NN only | [TBD or C-NN]
```

**MECHANISM DEFINER GATE is satisfied when:** map complete, all rows "Yes -- affects C-NN
only". Nothing else. STOP beyond map.

ROLE: BUILDER ASPIRATIONAL cannot begin until this gate is satisfied.

---

### ROLE: BUILDER ASPIRATIONAL

**Input required:** CRITERION DEFINER GATE + MECHANISM DEFINER GATE.
**Cannot begin unless both gate artifacts exist.**

Draft 1-2 aspirational criteria. STOP if more than 2.

Inline competitor before each criterion, ending with derivation instruction. Five fields +
**Gap closed:** [row citation].

---

### ROLE: EVALUABILITY AUDITOR

**Runs after ROLE: BUILDER ASPIRATIONAL, before PHASE 9.**

For each structural criterion:

```
EVALUABILITY DECLARATION -- [criterion ID]:
  Artifact:    [named section or block]
  Scan method: [heading-scan | content-scan | count-check]
  Excluded:    [instruction content not required to verify compliance]
```

EVALUABILITY GATE is satisfied when all structural criteria have complete declarations.
STOP if any field missing. PHASE 9 cannot begin until EVALUABILITY GATE is satisfied.

---

### ROLE: DUAL AUDITOR

**Audit Track 1:** Per-criterion table `| C-NN | Text: D/C/CC | Pass: L/O/Q | Status |`.

**Audit Track 2:** Category distribution per tier; scoring section; competitor bijection;
anchor chain; gate chain (DEFINER OUTPUT GATE terminal + STOP; MECHANISM DEFINER GATE
names ROLE: BUILDER ASPIRATIONAL; EVALUABILITY GATE satisfied before Phase 9).

---

### PHASE 9 -- EMIT

**PREREQUISITE structure -- three required parts:**

**(1) Gate-ID annotation:**
`PREREQUISITE: EVALUABILITY GATE is complete.`

**(2) Independence boundary declaration:**
`Without reading the body of ROLE: EVALUABILITY AUDITOR, Phase 9 sequencing cannot be
circumvented.`

**(3) Positive sufficiency claim -- REQUIRED FORM (satisfies C-53):**
`A reader can confirm that EVALUABILITY GATE is complete by reading this PREREQUISITE
line alone, without reading the body of ROLE: EVALUABILITY AUDITOR.`

**COMPLIANT example (satisfies C-53):**
```
PREREQUISITE: EVALUABILITY GATE is complete. A reader can confirm that EVALUABILITY
GATE is complete by reading this PREREQUISITE line alone, without reading the body of
ROLE: EVALUABILITY AUDITOR.
```
The verbatim identifier "EVALUABILITY GATE" appears within the sufficiency clause itself
("A reader can confirm that **EVALUABILITY GATE** is complete by reading...").

**NON-COMPLIANT example (satisfies C-51 but fails C-53):**
```
PREREQUISITE: EVALUABILITY GATE is complete. A reader can confirm that Phase 9 was
properly gated by reading this PREREQUISITE line alone, without reading the body of
ROLE: EVALUABILITY AUDITOR.
```
"Properly gated" does not embed the verbatim gate identifier. The sufficiency clause
describes the sequencing state without naming which gate was completed.

**Use the compliant form. Write the Phase 9 PREREQUISITE exactly as shown in the compliant
example, substituting the actual EVALUABILITY GATE name.**

Produce the final rubric: essential -> recommended -> aspirational -> scoring section.

**Scoring section must include:** composite formula, denominator (/NN annotated with
criterion ID range), golden threshold, PARTIAL (score value + earn conditions).

**Emit manifest check:**

| Check | Status |
|-------|--------|
| DEFINER OUTPUT GATE satisfied | |
| MECHANISM DEFINER GATE satisfied | |
| REFERENCE ANCHOR Falls-short populated + Consumer names ROLE: MECHANISM DEFINER | |
| MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL | |
| EVALUABILITY GATE satisfied (all EVALUABILITY DECLARATIONs complete) | |
| PHASE 9 PREREQUISITE: verbatim gate identifier embedded within sufficiency clause | |
| PHASE 9 PREREQUISITE form matches compliant example above | |
| ISOLATION AUDIT complete | |
| Category diversity: >= 3 distinct categories | |
| Aspirational tier count: 1-2 criteria | |
| Scoring denominator annotated with criterion ID range | |
| PARTIAL handling stated | |

---

## V-04 -- Role Sequence + Lifecycle Emphasis (C-53 + C-54 Combined)

**Axis:** Combined -- ROLE: MECHANISM DEFINER promoted before Phase 4 (role sequence,
from V-01) combined with expanded Phase 9 PREREQUISITE requiring verbatim gate identifier
in sufficiency clause (lifecycle emphasis, C-53 probe from V-03) and explicit C-54
instruction requiring Architecture-labeled STOP consequence clauses to name the specific
absent structural element within the declaration (not only the declaration by heading).

STATUS QUO COMPETITOR absent (C-49 ablated) to isolate the C-53 + C-54 joint signal.
PHASE-LOCALITY RULE ablated. C-38 ablated. All other evaluability architecture elements
(C-45, C-46, C-47, C-48, C-51) carried from R18 V-05.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain both (1) a Phase 9 PREREQUISITE sufficiency clause embedding the verbatim gate identifier (C-53) and (2) NON-REDUNDANCY DECLARATION STOP consequence clauses naming the specific absent element within the declaration ("the Architecture-A competitor entry in the NON-REDUNDANCY DECLARATION is absent") rather than only the declaration heading ("the NON-REDUNDANCY DECLARATION is incomplete"); the primary falsification signal is a rubric where one of the two elements is present without the other. | If V-04 passes both C-53 and C-54 while V-03 passes only C-53, the addition of the NON-REDUNDANCY DECLARATION C-54 instruction is independently effective without interfering with the Phase 9 PREREQUISITE structure; if V-04 fails C-53 while V-03 passes it, adding the NON-REDUNDANCY DECLARATION instruction competes for model attention with the Phase 9 PREREQUISITE. | The role-sequence change (MECHANISM DEFINER before Phase 4) was confirmed stable for C-51/C-52 in V-01; V-04 tests whether it is also stable for C-53/C-54 under the combined axis -- if C-53 or C-54 fail in V-04 but pass in V-03 (no sequence change), the role-sequence interaction is the differentiator. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### PHASE 1 -- FAILURE MODE ANALYSIS

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. Do not begin ROLE: CRITERION DEFINER
until the failure log contains at least 5 entries.

---

### ROLE: CRITERION DEFINER

**Runs after Phase 1. Do not write criterion fields during this role.**

**Text template:** `Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].`

**Pass template:**
```
LOCATION: [artifact field or section]
OBSERVABLE: [specific token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

DEFINER OUTPUT GATE is satisfied when: both templates present in slot-fillable form, no
additional content. STOP if this role's output contains anything beyond the two templates.

ROLES: PHASE 3 and PHASE 4 cannot begin until DEFINER OUTPUT GATE is satisfied.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE satisfied.**

Draft from blocking failure modes. Apply Text template and Pass template. Five fields:
ID, Text, Weight: essential, Category, Pass. No qualitative-only observables.

---

### ROLE: MECHANISM DEFINER

**Runs after PHASE 3 and before PHASE 4.**

**PREREQUISITE:** REFERENCE ANCHOR not yet required. Read Phase 3 essential criteria only.

```
Mechanism        | Independence             | Affects criterion
[mechanism name] | Yes -- affects C-NN only | [TBD]
```

Each row mutually exclusive. This is a draft; no new mechanisms after Phase 4.5.

**MECHANISM DEFINER GATE satisfied when:** map complete, all rows "Yes -- affects C-NN
only", no additional content. STOP beyond map.

ROLE: BUILDER ASPIRATIONAL cannot begin until this gate is satisfied.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE satisfied.**

Draft from suboptimal failure modes. Five fields + **Dimension:** [degree | precision |
specificity]. After drafting: review independence map; add rows for any new aspirational
gaps.

---

### PHASE 4.5 -- POST-DRAFT AUDIT

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

STOP if any N. Tier majority count. STOP if < 2 tiers distinct.

---

### PHASE 5 -- REFERENCE ANCHOR

**Do not proceed until Phase 4.5 complete.**

```
REFERENCE ANCHOR:
  Reference:   [identifier]
  Passes:      [at minimum C-01 through C-08]
  Falls-short: [aspirational gap dimension]
  Consumer:    ROLE: MECHANISM DEFINER cannot begin until this anchor is complete.
               The Falls-short dimension defines the aspirational gap for the
               Mechanism Definer's independence map.
```

STOP if Falls-short blank or Consumer omits ROLE: MECHANISM DEFINER.

---

### PHASE 5.5 -- BUILDER ASPIRATIONAL PRECONDITION CHECK

Confirm: (1) DEFINER OUTPUT GATE satisfied; (2) MECHANISM DEFINER GATE satisfied;
(3) REFERENCE ANCHOR complete. STOP if unsatisfied.

---

### ROLE: BUILDER ASPIRATIONAL

**Input required:** CRITERION DEFINER GATE + MECHANISM DEFINER GATE (both gates must
exist). **Cannot begin unless both gate artifacts exist.**

Draft 1-2 aspirational criteria from Falls-short dimension. STOP if more than 2.

Inline competitor immediately before each criterion:

> **[COMPETITOR NAME]** -- [wrong implementation description]. From the description above,
> derive the required implementation before reading the positive definition below.

Five fields + **Gap closed:** [independence map row].

---

### ROLE: EVALUABILITY AUDITOR

**Runs after ROLE: BUILDER ASPIRATIONAL. Before PHASE 9.**

For each structural criterion:

```
EVALUABILITY DECLARATION -- [C-NN]:
  Artifact:    [named section]
  Scan method: [heading-scan | content-scan | count-check]
  Excluded:    [content not required for verification]
```

EVALUABILITY GATE satisfied when all declarations complete. PHASE 9 blocked until then.

---

### EVALUABILITY ARCHITECTURE -- NON-REDUNDANCY DECLARATION

Declare Architecture A and B enforcement points. For each, write a STOP consequence
clause that names the specific structural element within the declaration that the
predicate failure leaves absent -- not only the declaration by heading.

**Required STOP form (C-54 compliant):**
```
STOP: If Architecture-A gate does not enforce pre-Phase-9 sequencing, the
Architecture-A gate entry in the NON-REDUNDANCY DECLARATION is absent. Do not proceed.
```

**Non-compliant form (C-52 level, fails C-54):**
```
STOP: If Architecture-A gate is absent, the NON-REDUNDANCY DECLARATION is incomplete.
```

The compliant form names the absent element ("the Architecture-A gate entry") within the
declaration. The non-compliant form names only the declaration.

**Architecture A:** Pre-Phase-9 gate -- EVALUABILITY GATE blocks Phase 9 until all
EVALUABILITY DECLARATIONs are complete, enforcing C-43/C-44 as a pre-Phase-9 structural
condition.

**STOP: If Architecture-A gate does not enforce pre-Phase-9 sequencing -- if Phase 9
can begin before all EVALUABILITY DECLARATIONs are complete -- the Architecture-A gate
entry in the NON-REDUNDANCY DECLARATION is absent. Do not proceed to Phase 9.**

**Architecture B:** Emit-close terminal -- per-criterion evaluability mapping appears as
a named block at Phase 9 close, independently verifiable by heading scan without reading
role instruction bodies, enforcing C-43 as an emit-close structural requirement.

**STOP: If Architecture-B terminal block does not appear as a named heading at Phase 9
close -- if the per-criterion evaluability mapping is embedded inline in instructions
rather than produced as a distinctly named section -- the Architecture-B terminal table
entry in the NON-REDUNDANCY DECLARATION is absent. Do not proceed to Phase 9.**

#### EVALUABILITY ARCHITECTURE COMPETITOR

> **SINGLE-POINT EVALUABILITY AUDITOR** -- One enforcement point: EVALUABILITY AUDITOR
> runs, declares evaluability, no pre-Phase-9 gate and no emit-close terminal. From the
> description above, derive why two non-redundant enforcement points are required before
> reading the Architecture A/B declarations above.

---

### ROLE: DUAL AUDITOR

**Audit Track 1:** `| C-NN | Text: D/C/CC | Pass: L/O/Q | Status |`

**Audit Track 2:**
1. Category distribution per tier (majority per tier; STOP if < 2 distinct).
2. Scoring section: formula + denominator (annotated) + threshold + PARTIAL.
3. Competitor bijection.
4. Anchor chain.
5. Gate chain: DEFINER OUTPUT GATE terminal + STOP; MECHANISM DEFINER GATE names
   ROLE: BUILDER ASPIRATIONAL; EVALUABILITY GATE satisfied before Phase 9.
6. Evaluability architecture: NON-REDUNDANCY DECLARATION present; Architecture A/B
   labeled; each STOP consequence names absent ELEMENT within declaration (C-54 form,
   not C-52 form).

---

### PHASE 9 -- EMIT

**PREREQUISITE -- three-part block (write all three parts):**

**(1)** `PREREQUISITE: EVALUABILITY GATE is complete.`

**(2)** Independence boundary: `Without reading the body of ROLE: EVALUABILITY AUDITOR,
sequencing to Phase 9 cannot be confirmed.`

**(3)** Positive sufficiency claim -- embed verbatim gate identifier within the claim:
`A reader can confirm that EVALUABILITY GATE is complete by reading this PREREQUISITE
line alone, without reading the body of ROLE: EVALUABILITY AUDITOR.`

The phrase "EVALUABILITY GATE" must appear within part (3), not only in part (1).
A sufficiency claim that reads "A reader can confirm Phase 9 was properly gated..." fails
C-53 because the verbatim gate identifier does not appear within the sufficiency clause.

Produce the final rubric: essential -> recommended -> aspirational -> scoring section.

**Scoring section:** composite formula + denominator (/NN /* C-09 through C-NN */) +
golden threshold + PARTIAL (score value + earn conditions).

**Emit manifest check:**

| Check | Status |
|-------|--------|
| DEFINER OUTPUT GATE satisfied | |
| MECHANISM DEFINER GATE satisfied | |
| REFERENCE ANCHOR Falls-short populated + Consumer names ROLE: MECHANISM DEFINER | |
| MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL | |
| EVALUABILITY GATE satisfied | |
| PHASE 9 PREREQUISITE: verbatim "EVALUABILITY GATE" embedded in sufficiency clause | |
| NON-REDUNDANCY DECLARATION present: Architecture A and B labeled | |
| NON-REDUNDANCY DECLARATION: each STOP consequence names absent ELEMENT (C-54 form) | |
| ISOLATION AUDIT complete | |
| Category diversity: >= 3 distinct | |
| Aspirational tier count: 1-2 | |
| Scoring denominator annotated | |
| PARTIAL handling stated | |

---

## V-05 -- Full Stack R19 (Ceiling)

**Axis:** All axes + full stack -- R18 V-05's full element set (STATUS QUO COMPETITOR
opening block with tier-diversity failure [C-49] and class-recognition note absence [C-50
probe] in failure list; DEFINER OUTPUT GATE with predicate + exclusion terminal + embedded
STOP [C-43, C-44]; REFERENCE ANCHOR Consumer field naming ROLE: MECHANISM DEFINER [C-47];
MECHANISM DEFINER GATE naming ROLE: BUILDER ASPIRATIONAL [C-46]; BUILDER ASPIRATIONAL
quoting both gates verbatim [C-41]; PHASE-LOCALITY RULE [C-42]; TIER-BLIND CATEGORIZER
inline at category-count step in canonical derivation format [C-48, C-39]; anchor STOP
at Mechanism Definer entry [C-45]; CLASS RECOGNITION APPLICATION NOTE with structural-
equivalence basis [C-38, C-40]) plus two new elements: (1) Phase 9 PREREQUISITE with
verbatim gate identifier embedded within the sufficiency clause, satisfying C-53 at the
element-embedding level; (2) NON-REDUNDANCY DECLARATION Architecture-labeled STOP
consequence clauses naming the specific absent structural element (the Architecture-A/B
entry) within the declaration rather than only the declaration heading, satisfying C-54
at the element-absent level.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain all structural elements: STATUS QUO COMPETITOR with tier-diversity and class-recognition foil items; CLASS RECOGNITION APPLICATION NOTE with structural-equivalence basis; Phase 9 PREREQUISITE with verbatim gate identifier within the sufficiency clause ("A reader can confirm that EVALUABILITY GATE is complete by reading this PREREQUISITE line alone, without reading the body of ROLE: EVALUABILITY AUDITOR"); NON-REDUNDANCY DECLARATION with Architecture-labeled STOP consequences naming the absent element ("the Architecture-A gate entry in the NON-REDUNDANCY DECLARATION is absent"); the primary falsification signal is any rubric missing any one element. | If V-05 passes all C-01 through C-54 (46/46 aspirational), composite = 10.0. The ablation chain is V-03 (C-53 only, no C-54, no STATUS QUO) -> V-04 (C-53 + C-54, no STATUS QUO) -> V-05 (C-53 + C-54 + full stack); if V-05 passes C-53 and C-54 while V-03 and V-04 also pass them, C-53/C-54 are stable under the full stack; if V-05 fails C-53 or C-54 while V-04 passes them, adding the STATUS QUO COMPETITOR + CLASS RECOGNITION APPLICATION NOTE displaces or competes with the evaluability architecture elements. | C-51 and C-52 stability is confirmed by all five variations passing them (V-01, V-02, V-03 ablated, V-04, V-05); if V-05 fails C-51 or C-52, the full stack competes with the evaluability PREREQUISITE elements despite both being required. |

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
  good output rather than systematic analysis of broken output.
- Fails to produce causal direction templates -- Text fields describe presence of good
  properties, not consequence of their absence.
- Fails to enforce Pass observability by template -- Pass conditions include "is clear,"
  "adequately covers" as sole observables.
- Fails to name a specific reference anchor with a Falls-short dimension.
- Fails to verify mechanism independence.
- Fails to make role dependencies bidirectionally traceable.
- Fails to verify category diversity by tier.
- Fails to include a class-recognition application note -- outputs are scored criterion-
  by-criterion without first identifying whether the rubric belongs to the inertia class,
  making rubrics that satisfy all surface criteria while failing structural equivalence
  invisible to the scoring process.

**From the description above, derive what the required rubric-building procedure must do --
before reading Phase 1. State your derivation, then proceed.**

---

### PHASE 1 -- FAILURE MODE ANALYSIS

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. Do not begin ROLE: CRITERION DEFINER
until the failure log contains at least 5 entries.

---

### ROLE: CRITERION DEFINER

**Runs after Phase 1. Do not write criterion fields during this role.**

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form -- wrong implementation with same surface behavior as Y]
```

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form --
in any phrasing -- is any Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

DEFINER OUTPUT GATE is satisfied when: Text template and Pass template are both present
in slot-fillable form, derived from the skill spec, with no additional content. Nothing
else. STOP if this role's output contains anything beyond the two required templates.

ROLES: PHASE 3 and PHASE 4 cannot begin until DEFINER OUTPUT GATE is satisfied.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied when:** Text template and Pass template
are both present in slot-fillable form, derived from the skill spec.

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

If introducing a competitor:

> **[COMPETITOR NAME]** -- [description of wrong implementation: what it does, what
> surface form it has, why it fails to close the criterion gap]. This competitor IS the
> gap specification -- from the description above, derive the required implementation
> before reading the positive definition below.

Place the competitor block immediately before this criterion's definition. Do not group
competitors in a shared preamble.

Each criterion: five fields -- ID (C-NN), Text (slot-filled), Weight: essential,
Category (correctness | depth | format | coverage | behavior), Pass (slot-filled).
No "is clear" or "adequately covers" as sole observable.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE satisfied.**

Draft from suboptimal failure modes. Apply Text template and Pass template. Pass
conditions test degree, precision, or specificity -- not existence.

If introducing a competitor: inline, ending with derivation instruction.

Five fields + **Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT

#### ISOLATION AUDIT

For each criterion from Phases 3 and 4:

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

STOP if any N -- revise before DIVERGENCE CHECK.

#### DIVERGENCE CHECK

**PREREQUISITE: ISOLATION AUDIT complete.**

```
Essential tier:     [category] x[N] ... -- majority: [category]
Recommended tier:   [category] x[N] ... -- majority: [category]
Aspirational tier:  [category] x[N]     -- majority: [category]
```

STOP if fewer than 2 of 3 tiers have distinct majority categories.

---

### PHASE 5 -- REFERENCE ANCHOR

**Do not proceed until DIVERGENCE CHECK complete.**

```
REFERENCE ANCHOR:
  Reference:   [specific competitor or prior-version identifier]
  Passes:      [criteria satisfied -- at minimum C-01 through C-08]
  Falls-short: [exact dimension on which it fails the aspirational bar]
  Consumer:    ROLE: MECHANISM DEFINER cannot begin until this anchor is complete.
               The Falls-short dimension defines the aspirational gap that the
               Mechanism Definer's independence map must cover.
```

STOP if REFERENCE ANCHOR absent before ROLE: MECHANISM DEFINER begins, or Falls-short
blank, or Consumer does not name ROLE: MECHANISM DEFINER as the blocked consumer.

---

### PHASE-LOCALITY RULE

Prohibited placement zones for all competitor blocks:

1. **Preamble zone**: any block appearing before any construction phase (Phases 3, 4, 6).
2. **Shared-operating-principles zone**: any block preceding more than one construction
   step.
3. **Multi-criterion zone**: any combined block governing more than one criterion.

Correctly placed if and only if not in any prohibited zone. Required Emit manifest
verification target.

---

### ROLE: MECHANISM DEFINER

**Runs after Phase 4.5 and before ROLE: BUILDER ASPIRATIONAL.**

**PREREQUISITE:** REFERENCE ANCHOR complete (Falls-short populated; Consumer names
ROLE: MECHANISM DEFINER as the blocked consumer).

```
Mechanism        | Independence             | Affects criterion
[mechanism name] | Yes -- affects C-NN only | [TBD or C-NN]
```

Each row mutually exclusive. If any row "No": stop, redesign, restart.

**MECHANISM DEFINER GATE is satisfied when:** map complete, all rows "Yes -- affects C-NN
only", nothing else. STOP if anything beyond independence map.

ROLE: BUILDER ASPIRATIONAL cannot begin until this gate is satisfied.

---

### ROLE: BUILDER ASPIRATIONAL

**Input required:**

- **CRITERION DEFINER GATE**: Text template and Pass template in slot-fillable form.
- **MECHANISM DEFINER GATE**: Independence map with all C-NN citations populated.

**ROLE: BUILDER ASPIRATIONAL cannot begin unless both gate artifacts exist.**

Draft aspirational criteria closing the exact gap named in REFERENCE ANCHOR Falls-short.
One criterion per mechanism in the independence map.

**Aspirational tier count: 1-2 criteria.** STOP if more than 2.

If introducing a competitor:

> **[COMPETITOR NAME]** -- [wrong implementation description]. From the description above,
> derive the required implementation before reading the positive definition below.

Place each competitor block immediately before the criterion. PHASE-LOCALITY RULE applies.

Five fields: ID, Text (slot-filled from templates), Weight: aspirational, Category,
Pass (slot-filled from templates).

**Gap closed:** [independence map mechanism row citation, format: "Yes -- affects C-NN
only"].

---

### ROLE: EVALUABILITY AUDITOR

**Runs after ROLE: BUILDER ASPIRATIONAL, before PHASE 9.**

For each structural criterion (any criterion whose Pass condition references a named
section, block, or artifact):

```
EVALUABILITY DECLARATION -- [C-NN]:
  Artifact:    [named section or block enabling independent verification]
  Scan method: [heading-scan | content-scan | count-check]
  Excluded:    [specific instruction content not required to verify compliance --
               e.g., "ROLE: MECHANISM DEFINER body not required"]
```

EVALUABILITY GATE is satisfied when: All structural criteria have a completed
EVALUABILITY DECLARATION with all three fields populated. Nothing else. STOP if any
declaration is missing a field.

PHASE 9 cannot begin until EVALUABILITY GATE is satisfied.

---

### EVALUABILITY ARCHITECTURE -- NON-REDUNDANCY DECLARATION

Declare the two enforcement points and confirm they are non-redundant. Each Architecture
label resolves to a named entry in the EVALUABILITY ARCHITECTURE COMPETITOR section
below. Each STOP consequence clause must name the specific structural element within the
declaration that the predicate failure leaves absent.

**Architecture A:** Pre-Phase-9 gate enforcement -- EVALUABILITY GATE blocks Phase 9
entry until all EVALUABILITY DECLARATIONs are complete, enforcing C-43/C-44 as a
pre-Phase-9 structural condition. Gate failure mode: Phase 9 opens before evaluability
declarations are complete, making criterion-level evaluability unverifiable from Phase 9
entry.

**STOP: If Architecture-A gate does not enforce pre-Phase-9 sequencing -- if Phase 9 can
begin before all EVALUABILITY DECLARATIONs are complete -- the Architecture-A gate entry
in the NON-REDUNDANCY DECLARATION is absent. Do not proceed to Phase 9.**

**Architecture B:** Emit-close terminal table enforcement -- per-criterion evaluability
mapping appears as an independently produced named section block at Phase 9 close,
verifiable by heading scan without reading role instruction bodies, enforcing C-43 as an
emit-close structural requirement. Terminal failure mode: evaluability mapping is embedded
inline in instructions rather than produced as a distinct named block, making heading-scan
verification impossible.

**STOP: If Architecture-B terminal block does not appear as a distinctly named heading
at Phase 9 close -- if the per-criterion evaluability mapping is not independently
produced -- the Architecture-B terminal table entry in the NON-REDUNDANCY DECLARATION
is absent. Do not proceed to Phase 9.**

#### EVALUABILITY ARCHITECTURE COMPETITOR

> **SINGLE-POINT EVALUABILITY AUDITOR** -- One enforcement point only: EVALUABILITY
> AUDITOR runs and declares evaluability for all criteria at once, without a pre-Phase-9
> gate (Architecture A absent) and without an emit-close terminal (Architecture B absent).
> The single audit result is the only mechanism checking evaluability compliance. A rubric
> using this approach has one gate failure mode (Architecture-A) and one terminal failure
> mode (Architecture-B) simultaneously invisible: Phase 9 can open before evaluability
> is confirmed, and the per-criterion evaluability mapping may not appear as an
> independently verifiable artifact. From the description above, derive why two non-
> redundant enforcement points are required before reading the Architecture A/B
> declarations above.

---

### ROLE: DUAL AUDITOR

Run two audit tracks sequentially.

**Audit Track 1 -- Criterion quality (all criteria):**

Output as per-criterion table -- do not substitute narrative:

```
| C-NN | Text: D/C/CC | Pass: L/O/Q | Status |
```

D = Direction (Y/N), C = Contrast (Y/N), CC = Causal chain (Y/N)
L = Location (Y/N), O = Observable (Y/N), Q = No-qualitative (Y/N)

**Audit Track 2 -- Structural verification:**

> **TIER-BLIND CATEGORIZER** -- The standard category-distribution audit reads each
> criterion's Category field, confirms the field is present and non-empty, and notes that
> multiple category names appear across the rubric. It does not separate assignments by
> tier, does not compute a majority category per tier, and does not check whether
> different tiers have different majority categories. A rubric where essential criteria
> are predominantly "correctness" and aspirational criteria are also predominantly
> "correctness" passes the standard audit. The tier convergence is invisible because the
> check is tier-agnostic. From the description above, derive what the category-
> distribution divergence check must verify before reading the check below.

1. **Category distribution**: Count per tier. Identify majority per tier. Record:
   ```
   Essential: [category] x[N] -- majority: [category]
   Recommended: [category] x[N] -- majority: [category]
   Aspirational: [category] x[N] -- majority: [category]
   ```
   STOP if fewer than 2 of 3 tiers have distinct majority categories.

2. **Scoring section**: Confirm:
   - Composite formula
   - Denominator (/NN annotated "/* C-09 through C-NN */")
   - Golden threshold (numeric)
   - PARTIAL handling: score value (e.g., 0.5) AND earn conditions
   - CLASS RECOGNITION APPLICATION NOTE: present, names inertia pattern as FAIL,
     structural-equivalence basis present (closes PARTIAL bypass path)

3. **Competitor coverage bijection**: For each novel aspirational criterion, exactly one
   competitor block. Counts match.

4. **Anchor chain**: REFERENCE ANCHOR has Falls-short populated and Consumer naming
   ROLE: MECHANISM DEFINER.

5. **Gate chain**:
   - DEFINER OUTPUT GATE ends with exclusion terminal and embedded STOP
   - MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL as blocked consumer
   - BUILDER ASPIRATIONAL entry quotes MECHANISM DEFINER GATE verbatim
   - PHASE-LOCALITY RULE: no competitor in any of the three prohibited zones
   - TIER-BLIND CATEGORIZER: inline before category-distribution count step, ends with
     derivation instruction, governs exactly one audit check

6. **Evaluability architecture**:
   - NON-REDUNDANCY DECLARATION present with Architecture A and B labels
   - Each Architecture label resolves to a named entry in EVALUABILITY ARCHITECTURE
     COMPETITOR section
   - Each STOP consequence names the specific absent element within the declaration
     ("the Architecture-A gate entry in the NON-REDUNDANCY DECLARATION is absent"),
     NOT only the declaration heading ("the NON-REDUNDANCY DECLARATION is incomplete")
   - EVALUABILITY GATE satisfied before Phase 9 opens

7. **Phase 9 PREREQUISITE**: Confirm sufficiency clause embeds verbatim gate identifier
   within the clause text (compliant form: "A reader can confirm that EVALUABILITY GATE
   is complete by reading this PREREQUISITE line alone, without reading the body of
   ROLE: EVALUABILITY AUDITOR"). Flag as FAIL if sufficiency clause uses only generic
   language without the verbatim gate identifier.

---

### PHASE 9 -- EMIT

**PREREQUISITE: EVALUABILITY GATE is complete. A reader can confirm that EVALUABILITY
GATE is complete by reading this PREREQUISITE line alone, without reading the body of
ROLE: EVALUABILITY AUDITOR.**

Do not proceed to Phase 9 if EVALUABILITY GATE is not satisfied.

Produce the final rubric in this order:

1. Essential criteria (C-01 through C-NN)
2. Recommended criteria
3. Aspirational criteria
4. Scoring section

**Scoring section must include:**
- Composite formula
- Denominator (/NN, annotated: "/* C-09 through C-NN */")
- Golden threshold (>= NN)
- PARTIAL: score value (e.g., 0.5) and earn conditions

**CLASS RECOGNITION APPLICATION NOTE** (include in scoring section, before composite
formula):

```
CLASS RECOGNITION APPLICATION NOTE:
Before scoring individual criteria, identify the output class of the rubric under
evaluation.

INERTIA PATTERN: A rubric where (a) criteria Text fields describe what good output
  contains rather than what absence of the required property causes, (b) Pass conditions
  use only qualitative language ("is clear," "is complete," "adequately covers") without
  an artifact location or measurable token, or (c) weights (essential / recommended /
  aspirational) are assigned without evidence of a failure-mode analysis. Any one of
  these three signals identifies the inertia pattern.

STRUCTURAL EQUIVALENCE: A rubric that passes the inertia-pattern check but where two or
  more criteria test the same observable -- same artifact location, same token, same
  structural property, only paraphrased -- fails the structural-equivalence check.
  Structurally equivalent criteria are not independent: removing either leaves the rubric
  measuring the same thing. A rubric with N structurally equivalent criteria is
  functionally a rubric with N-1 criteria. The structural-equivalence check requires
  confirming that each criterion's Pass observable is not achievable by the same artifact
  property that satisfies any other criterion's Pass observable.

If the rubric belongs to the inertia class OR fails the structural-equivalence check:
  score = FAIL. Do not apply the composite formula.

If the rubric passes both checks: apply the composite formula below.
```

**Emit manifest check** -- do not emit until all verified:

| Check | Status |
|-------|--------|
| DEFINER OUTPUT GATE satisfied (both templates, no additional content) | |
| MECHANISM DEFINER GATE satisfied (independence map complete, all C-NN cited) | |
| REFERENCE ANCHOR Falls-short populated | |
| REFERENCE ANCHOR Consumer names ROLE: MECHANISM DEFINER | |
| MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL | |
| BUILDER ASPIRATIONAL entry quotes MECHANISM DEFINER GATE verbatim | |
| PHASE-LOCALITY RULE: no competitor in any of the three prohibited zones | |
| TIER-BLIND CATEGORIZER: inline at category-count step, canonical derivation format, governs exactly one check | |
| STATUS QUO COMPETITOR failure list: names tier-diversity verification failure explicitly | |
| STATUS QUO COMPETITOR failure list: names class-recognition note absence explicitly | |
| EVALUABILITY GATE satisfied (all structural criteria have EVALUABILITY DECLARATION) | |
| NON-REDUNDANCY DECLARATION: Architecture A and B labeled; resolves to COMPETITOR section | |
| NON-REDUNDANCY DECLARATION: each STOP consequence names absent ELEMENT within declaration (not only declaration heading) | |
| PHASE 9 PREREQUISITE: verbatim gate identifier "EVALUABILITY GATE" embedded within sufficiency clause | |
| PHASE 9 PREREQUISITE form: "A reader can confirm that EVALUABILITY GATE is complete by reading this PREREQUISITE line alone, without reading the body of ROLE: EVALUABILITY AUDITOR" | |
| CLASS RECOGNITION APPLICATION NOTE: present, names inertia pattern as FAIL | |
| CLASS RECOGNITION APPLICATION NOTE: structural-equivalence basis present, closes PARTIAL bypass path | |
| ISOLATION AUDIT complete (all criteria flagged, no FAIL remaining) | |
| Category diversity: >= 3 distinct categories across full rubric | |
| Aspirational tier count: 1-2 criteria | |
| Scoring denominator annotated with criterion ID range (/* C-09 through C-NN */) | |
| PARTIAL handling stated with score value and earn conditions | |
