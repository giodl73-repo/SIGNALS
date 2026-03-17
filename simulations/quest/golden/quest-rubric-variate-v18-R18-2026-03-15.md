# quest-rubric Variate -- Round 18 (Against rubric v17)
**Date:** 2026-03-15
**Rubric:** v17 (C-01--C-47; denominator /39; adds C-47: anchor-successor-role-named)
**Target criteria:** C-47 (stability under new axes); C-39 (persistent fail -- Tier-Blind
Categorizer at Dual Auditor category-distribution step); C-48 candidate:
`audit-divergence-competitor-placed`

**Round 18 design note:** R17 confirmed C-47 (`anchor-successor-role-named`) stable across
three structural contexts (V-03 isolates anchor naming with C-46 ablated; V-04 combines with
prospective role ordering; V-05 full eight-gate stack). V-05 R17 passes 37/39 criteria,
composite 99.49. C-38 FAIL in R17 is N/A (C-37 was not the novel criterion for R17; C-38 is
only relevant when C-37 is the current round's novel criterion). C-39 FAIL persists across all
17 rounds: no variation has yet placed a competitor inline at the Dual Auditor's
category-distribution verification step (Tier-Blind Categorizer pattern). R18 design goals:
(1) target C-39 directly via two lifecycle emphasis variations that introduce the TIER-BLIND
CATEGORIZER competitor at Audit Track 2 step 1; (2) probe C-48 candidate --
`audit-divergence-competitor-placed` -- by requiring the competitor to follow the canonical
competitor-block format (description of failure mode + derivation instruction); (3) confirm
C-47 stability under lifecycle emphasis and phrasing register axes not previously tested.

**C-48 candidate -- `audit-divergence-competitor-placed`:**

The ROLE: DUAL AUDITOR's Audit Track 2 category-distribution step is preceded by a named
competitor block -- TIER-BLIND CATEGORIZER -- that follows the canonical competitor block
format: description of the failure mode, what the standard approach does and does not do, and
a derivation instruction ending with "From the description above, derive what the divergence
check must verify before reading the check below." The block is placed inline, immediately
before the step that counts category assignments per tier -- not before the entire Dual Auditor
phase, not before Phase 4.5, not in any preamble zone. The block is criterion-local: it
governs exactly one audit check (the category-distribution divergence step).

**Distinction C-48 != C-39:** C-39 requires a competitor at the verification step (any form of
Tier-Blind Categorizer placement at the divergence check). C-48 -- if confirmed -- would
additionally require that competitor to follow the canonical competitor-block format with an
explicit derivation instruction, placed inline at the specific count-step (not at the phase
boundary). C-48 is only meaningful when C-39 is satisfied; a rubric that places a
TIER-BLIND CATEGORIZER competitor before the entire Dual Auditor phase satisfies C-39 but not
C-48. C-48 prerequisite: C-39 satisfied with inline placement at the category-count step.

**Distinction C-48 != C-42:** C-42 (PHASE-LOCALITY RULE) requires all competitor blocks to
avoid three prohibited zones (preamble zone, shared-operating-principles zone, multi-criterion
zone); C-48 requires a SPECIFIC competitor block to be placed at a SPECIFIC audit step. A rubric
satisfies C-42 (no competitors in prohibited zones) while failing C-48 if no competitor appears
at the divergence check step. A rubric satisfies C-48 (Tier-Blind Categorizer inline at
category-count step) while satisfying C-42 (the inline placement respects the PHASE-LOCALITY
RULE). C-42 is a global placement constraint; C-48 is a local presence requirement.

**Variation axes used in R18:**

| # | Axis | C-39 probe | C-47 | C-46 | C-48 candidate |
|---|------|-----------|------|------|----------------|
| V-01 | Lifecycle emphasis (Phase 4.5 split into ISOLATION AUDIT + DIVERGENCE CHECK) | Ablated -- subsection named but no competitor | Strong | Strong | Ablated |
| V-02 | Phrasing register (conversational -- no formal STOP/GATE/PREREQUISITE tokens) | Ablated | Strong | Strong | Ablated |
| V-03 | C-39 probe (TIER-BLIND CATEGORIZER inline at Dual Auditor category-count step) | Strong | Ablated | Ablated | Ablated |
| V-04 | C-39 + C-47 combined (Tier-Blind Categorizer at divergence check + anchor Consumer field) | Strong | Strong | Ablated | Ablated |
| V-05 | All axes + full stack (R17 V-05 stack + C-39 probe in canonical format) | Strong | Strong | Strong | Strong |

---

## Round 18 Variation Map

| Variation | Axis | C-39 probe | C-47 probe | C-46 probe | C-45 probe | C-44 probe | C-43 probe | C-41 probe | C-42 probe | C-48 probe | Notes |
|-----------|------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-------|
| V-01 | Lifecycle emphasis | Ablated -- DIVERGENCE CHECK subsection named, no competitor | Strong -- Consumer field in REFERENCE ANCHOR | Strong -- MECHANISM DEFINER GATE names BUILDER ASPIRATIONAL | Strong -- STOP at anchor block | Strong -- STOP inside DEFINER OUTPUT GATE | Strong -- DEFINER OUTPUT GATE with predicate | Strong -- Builder Aspirational quotes gates verbatim | Ablated | Ablated | Single-axis: Phase 4.5 split into ISOLATION AUDIT + DIVERGENCE CHECK; tests whether naming the divergence check as a distinct lifecycle step changes category distribution behavior; C-39 ablated to isolate the naming effect from the competitor effect |
| V-02 | Phrasing register | Ablated | Strong -- anchor Consumer clause present in conversational form | Strong -- gate successor named in conversational form | Strong -- "do not proceed" enforcement at anchor | Strong -- "this step is complete only when" form | Strong -- "before you write any criterion fields" form | Ablated -- standard precondition header, no verbatim gate quote | Ablated | Ablated | Single-axis: all formal tokens (STOP, GATE, PREREQUISITE) replaced with conversational equivalents; tests whether register affects mechanism satisfaction across C-43--C-47; primary risk is C-45 (STOP is a formal token with observable presence) and C-47 (Consumer field format may vary) |
| V-03 | C-39 probe | Strong -- TIER-BLIND CATEGORIZER competitor inline before category-count step | Ablated -- standard REFERENCE ANCHOR, no Consumer field | Ablated -- MECHANISM DEFINER GATE standard form | Strong -- STOP embedded inside anchor block | Strong -- STOP inside DEFINER OUTPUT GATE | Strong -- DEFINER OUTPUT GATE with predicate | Ablated -- standard Phase 5.5 header | Ablated | Ablated | Single-axis C-39 probe: TIER-BLIND CATEGORIZER placed immediately before Audit Track 2 step 1; C-47 and C-46 ablated to isolate C-39 signal; if C-39 is satisfied in V-03 without C-47 or C-46, C-39 is independently satisfiable |
| V-04 | C-39 + C-47 | Strong -- TIER-BLIND CATEGORIZER at divergence check | Strong -- Consumer field in REFERENCE ANCHOR | Ablated | Strong -- STOP in anchor block | Strong -- STOP in DEFINER OUTPUT GATE | Strong -- DEFINER OUTPUT GATE predicate | Ablated | Ablated | Ablated | Combined: tests whether C-39 and C-47 are jointly satisfiable without C-46; if V-04 passes both C-39 and C-47, the two signals are compatible without the full gate stack |
| V-05 | All axes + full stack | Strong -- TIER-BLIND CATEGORIZER inline in canonical competitor format | Strong -- Consumer field in REFERENCE ANCHOR | Strong -- MECHANISM DEFINER GATE names BUILDER ASPIRATIONAL | Strong | Strong -- embedded STOP | Strong -- predicate + exclusion terminal | Strong -- verbatim gate quote in Builder Aspirational entry | Strong -- PHASE-LOCALITY RULE with three prohibited zones | Strong -- canonical format competitor block at category-count step | Full ceiling: R17 V-05 structure + STATUS QUO COMPETITOR opening + Tier-Blind Categorizer at divergence check in canonical format; C-48 probe: competitor follows format (description + derivation instruction), placed inline at category-count step only |

---

## V-01 -- Lifecycle Emphasis

**Axis:** Lifecycle emphasis -- Phase 4.5 is restructured into two named subsections with
distinct entry requirements and STOP conditions. The first subsection, ISOLATION AUDIT, handles
per-criterion field checks (Text flags, Pass flags). The second subsection, DIVERGENCE CHECK,
handles cross-criterion category distribution and scope verification. Each subsection is a
named lifecycle boundary. DIVERGENCE CHECK has its own header, entry requirement (ISOLATION
AUDIT must be complete), and STOP condition.

All other R17 V-05 structures are preserved: DEFINER OUTPUT GATE with C-43+C-44, REFERENCE
ANCHOR with Consumer field (C-47), MECHANISM DEFINER GATE naming BUILDER ASPIRATIONAL (C-46),
BUILDER ASPIRATIONAL quoting both gates verbatim (C-41). No STATUS QUO COMPETITOR opening
block. C-39 ablated (DIVERGENCE CHECK has no companion competitor block -- naming the step
without a competitor establishes the ablation control for V-03).

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will show Phase 4.5 structured as two distinct subsections -- ISOLATION AUDIT (per-criterion) and DIVERGENCE CHECK (cross-criterion) -- each with its own header and STOP; any rubric where category distribution verification appears as a subpoint inside a single Phase 4.5 section (rather than as a named subsection boundary) falsifies the hypothesis; the falsification signal is a rubric where DIVERGENCE CHECK is not present as a named section header. | Naming the DIVERGENCE CHECK as a distinct lifecycle step makes category diversity a first-class structural requirement rather than a trailing audit subpoint; rubrics from V-01 may show more explicit tier-majority calculations in the Dual Auditor output because the builder was instructed to treat category distribution as a named phase boundary; the secondary test is whether the named DIVERGENCE CHECK subsection in Phase 4.5 causes the Dual Auditor to reproduce the subsection structure in its output. | V-03 is the primary extension: V-01 names the DIVERGENCE CHECK without a competitor; V-03 adds the TIER-BLIND CATEGORIZER competitor to the DIVERGENCE CHECK step. Comparing V-01 (named step, no competitor) and V-03 (named step, Tier-Blind Categorizer competitor) isolates whether the competitor placement -- not the step naming -- is the operative C-39 mechanism. |

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

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form -- in
any phrasing -- is any Text that locates causality in the wrong form's consequence: "X causes
failure," "failure occurs when X is present," "X leads to Z," and all semantic equivalents.
The Auditor check function tests causal structure, not pattern matching against canonical
examples.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

DEFINER OUTPUT GATE is satisfied when: Text template and Pass template are both present in
slot-fillable form, derived from the skill spec, with no additional content. Nothing else.
STOP if this role's output contains anything beyond the two required templates -- rewrite
before proceeding to Phase 3.

ROLES: PHASE 3 and PHASE 4 cannot begin until DEFINER OUTPUT GATE is satisfied.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied when:** Text template and Pass template are
both present in slot-fillable form, derived from the skill spec.

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

If introducing a competitor: place the competitor block immediately before this criterion's
definition. Do not group competitors in a shared preamble.

Each criterion requires five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: Apply CRITERION DEFINER Text template. "Without [Y], the artifact [fails] because
  [Z]. Not [X], but [Y]." with skill-specific values.
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass**: Apply CRITERION DEFINER Pass template. No "is clear" or "adequately covers" as
  sole observable.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied when:** Text template and Pass template are
both present in slot-fillable form.

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity --
not whether an element exists.

If introducing a competitor: place the competitor block immediately before the criterion.

Each criterion: same five fields as Phase 3. Required annotation:
**Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT

#### ISOLATION AUDIT

For each criterion from Phases 3 and 4, run the isolation audit. Read each field stripped of
surrounding context.

**Text field checks (3):**
1. **Direction**: does Text locate causality in Y's absence?
2. **Contrast**: does Text name the rejected form X alongside Y?
3. **Causal chain**: does Text name the downstream consequence Z?

**Pass field checks (3):**
4. **Location**: does Pass name an artifact location, field, or section?
5. **Observable**: does Pass name a specific count, token, or structural property?
6. **No qualitative-only**: does Pass avoid bare qualitative language without an anchor?

**Audit report format -- required; do not substitute a narrative log:**

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

STOP if any criterion fails one or more flags -- revise the failing field before proceeding
to DIVERGENCE CHECK.

#### DIVERGENCE CHECK

**PREREQUISITE: ISOLATION AUDIT must be complete (all criteria flagged, no FAIL remaining).**

Count category assignments per tier. For each tier, identify the majority category.

```
Essential tier:     [category] x[N], [category] x[N] ... -- majority: [category]
Recommended tier:   [category] x[N], [category] x[N] ... -- majority: [category]
Aspirational tier:  [category] x[N]                      -- majority: [category]
```

STOP if fewer than 2 of 3 tiers have distinct majority categories -- revise category
assignments before proceeding to PHASE 5.

---

### PHASE 5 -- REFERENCE ANCHOR

**Do not proceed to PHASE 5 until the DIVERGENCE CHECK is complete (all tier majorities
recorded, STOP condition cleared).**

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

STOP if this REFERENCE ANCHOR block is absent before ROLE: MECHANISM DEFINER begins, or if
the Falls-short field is blank, or if the Consumer field does not name ROLE: MECHANISM DEFINER
as the blocked consumer.

---

### PHASE 5.5 -- BUILDER ASPIRATIONAL PRECONDITION CHECK

Before ROLE: MECHANISM DEFINER begins, confirm:
1. DEFINER OUTPUT GATE satisfied (both templates present, no additional content).
2. REFERENCE ANCHOR complete (Falls-short populated; Consumer field names
   ROLE: MECHANISM DEFINER as the blocked consumer).

STOP if any prerequisite is unsatisfied.

---

### ROLE: MECHANISM DEFINER

**This role runs after Phase 4.5 and before ROLE: BUILDER ASPIRATIONAL.**

**PREREQUISITE:** REFERENCE ANCHOR is complete (Falls-short populated; Consumer field names
ROLE: MECHANISM DEFINER as the blocked consumer).

Read essential and recommended criteria. For each anticipated aspirational criterion, identify
the structural mechanism it would require. Produce an independence map.

**Independence map format:**

```
Mechanism        | Independence          | Affects criterion
[mechanism name] | Yes -- affects C-NN only | [TBD or criterion number]
```

Each row must be mutually exclusive. Removing any one mechanism leaves exactly one criterion
failing. No mechanism may carry dual responsibility for two gaps.

If any row is "No": stop, redesign, and restart this role.

**MECHANISM DEFINER GATE is satisfied when:** Independence map is complete with "Yes --
affects C-NN only" in every row, and every anticipated aspirational gap has a mechanism row.
Nothing else. STOP if this role's output contains anything beyond the independence map.

ROLE: BUILDER ASPIRATIONAL cannot begin until this gate is satisfied.

---

### ROLE: BUILDER ASPIRATIONAL

**Input required:**

- **CRITERION DEFINER GATE**: Text template and Pass template in slot-fillable form.
- **MECHANISM DEFINER GATE**: Independence Map with all C-NN citations populated.

**ROLE: BUILDER ASPIRATIONAL cannot begin unless both gate artifacts exist.**

Draft aspirational criteria that close the exact gap named in the REFERENCE ANCHOR Falls-short
field. One criterion per mechanism in the independence map.

**Aspirational tier count: 1-2 criteria.** STOP if you draft more than 2 aspirational
criteria. Rewrite to stay within range.

If introducing a competitor:

> **[COMPETITOR NAME]** -- [description of wrong implementation]. From the description above,
> derive the required implementation before reading the positive definition below.

Place each competitor block immediately before the criterion it governs -- not in a preamble,
not in a shared block, not governing more than one criterion.

Each criterion requires five fields: ID, Text (slot-filled), Weight: aspirational, Category,
Pass (slot-filled).

Required annotation: **Gap closed:** [independence map mechanism row citation, format:
"Yes -- affects C-NN only"].

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

   STOP if fewer than 2 of 3 tiers have distinct majority categories -- revise before Emit.

2. **Scoring section**: Confirm all present:
   - Composite formula (Essential weight + Recommended weight + Aspirational weight)
   - Denominator
   - Golden threshold (numeric)
   - PARTIAL handling: score value AND earn conditions

3. **Competitor coverage bijection**: For each novel aspirational criterion, confirm exactly
   one competitor block accompanies it. Count novel criteria. Count competitor blocks.
   Confirm counts match.

4. **Anchor chain**: Confirm REFERENCE ANCHOR has:
   - Falls-short field populated
   - Consumer field naming ROLE: MECHANISM DEFINER

5. **Gate chain**: Confirm:
   - DEFINER OUTPUT GATE ends with exclusion terminal and embedded STOP
   - MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL as blocked consumer

---

### EMIT

Produce the final rubric in this order:

1. Essential criteria (C-01 through C-NN)
2. Recommended criteria
3. Aspirational criteria
4. Scoring section

**Scoring section must include:**
- Composite formula
- Denominator (/NN)
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
| ISOLATION AUDIT complete (all criteria flagged) | |
| DIVERGENCE CHECK complete (tier majority table recorded, STOP cleared) | |
| Category diversity: >= 3 distinct categories across full rubric | |
| Aspirational tier count: 1-2 criteria | |
| PARTIAL handling stated with score value and earn conditions | |

---

## V-02 -- Phrasing Register

**Axis:** Phrasing register -- all formal structural tokens (STOP, GATE, PREREQUISITE, ROLE:)
are replaced with descriptive/conversational equivalents while preserving structural content.
"STOP if..." becomes "Do not proceed if...". "GATE is satisfied when:" becomes "This step is
complete when:". "PREREQUISITE:" becomes "Before continuing, confirm:". Named roles (ROLE:
CRITERION DEFINER) are replaced with named steps ("Step: Build Criterion Templates").
The structural sequence -- failure modes, templates, essential/recommended/aspirational
criteria, reference anchor, independence map, audit, emit -- is fully preserved.

All R17 V-05 structural mechanisms preserved in conversational form: anchor Consumer clause
(C-47), gate successor naming (C-46), anchor enforcement ("do not proceed" form of C-45),
gate exclusion terminal (C-43/C-44 in natural language). STATUS QUO COMPETITOR opening block
absent. C-39 ablated. C-41 ablated (standard precondition header without verbatim gate quote).
C-42 ablated (PHASE-LOCALITY RULE not explicitly stated; placement guidance embedded per step).

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will use conversational register throughout (no STOP/GATE/PREREQUISITE tokens); the structural sequence will be identical to R17 V-05 but expressed in natural language; the primary falsification signal is a rubric that contains any of the formal tokens STOP, GATE, or PREREQUISITE as section headers or structural keywords -- their presence would indicate the model defaulted to formal register despite the conversational framing; the secondary falsification signal is a rubric where the anchor Consumer clause or gate successor name is absent, suggesting conversational framing caused structural content loss. | Conversational register may reduce the rigidity of gate enforcement: a model following conversational instructions may interpret "do not proceed if..." as advisory rather than mandatory, producing a rubric where phases flow without explicit gate verification; this would manifest as missing ISOLATION AUDIT or DIVERGENCE CHECK outputs in the generated rubric body. | C-47 (anchor Consumer clause) is the primary stability test: the Consumer clause requires a specific named relationship in the anchor block; conversational framing may cause the model to describe this relationship in prose rather than as a named field, which would fail C-47's observable-field requirement. C-46 (gate successor named) is the secondary stability test. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### Step 1: Enumerate failure modes

Read the skill spec. For every way an output of this skill can fail, write down:

- What the skill output did (or omitted)
- What structural gap caused that behavior
- Whether the failure blocks use of the rubric, makes it suboptimal, or is cosmetic

Write at least 3 blocking failures and 2 suboptimal failures before moving to Step 2.

---

### Step 2: Build criterion templates

Do not write any criterion fields during this step.

Derive two templates from the skill spec -- one for criterion Text, one for Pass conditions.
You will use these templates to fill in each criterion later. No analysis, no criteria.

**Text template:**

A criterion Text field should follow this structure:
"Without [required property], the artifact [fails] because [downstream consequence].
Not [wrong approach], but [required property]."

Fill in skill-specific values for each slot. The causal arrow must point from the property's
absence to the failure: "without Y, Z fails" is correct; "X leads to failure" is not.

**Pass template:**

A criterion Pass field should follow this structure:
"In the [artifact field or section]: [specific count, token, or structural property] [must
be present / must equal / must exceed] [measurement or threshold]."

No Pass field should rely only on qualitative language like "is clear" or "well-structured"
without an observable anchor.

This step is complete when both templates are present in slot-fillable form with no
additional content. Do not begin Step 3 until this step is complete.

---

### Step 3: Essential criteria (3-5)

Before you begin, confirm: the Text template and Pass template from Step 2 are both present
in slot-fillable form.

Draft essential criteria from blocking failure modes. Apply your templates to each criterion.

If you want to introduce a comparison case, place it immediately before that specific criterion
-- not in a shared introduction block.

Each criterion needs five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: Fill in the Text template with skill-specific values.
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass**: Fill in the Pass template. Avoid "is clear" or "adequately covers" as the only
  observable.

---

### Step 4: Recommended criteria (2-3)

Before you begin, confirm: the Text template and Pass template from Step 2 are both present.

Draft recommended criteria from suboptimal failure modes. Pass conditions should test degree,
precision, or specificity -- not whether an element exists.

If you want to introduce a comparison case, place it immediately before that specific criterion.

Each criterion: same five fields as Step 3. Note which dimension the Pass condition tests:
**Dimension:** [degree | precision | specificity].

---

### Step 5: Check each criterion (isolation audit)

For each criterion from Steps 3 and 4, check these fields in isolation -- without reading
the surrounding criteria.

**For the Text field, ask:**
1. Does the Text locate the problem in the property's absence (not in a wrong form's presence)?
2. Does the Text name the wrong approach alongside the required one?
3. Does the Text name a downstream consequence?

**For the Pass field, ask:**
4. Does the Pass name a specific artifact location or field?
5. Does the Pass name a count, token, or structural property -- something measurable?
6. Does the Pass avoid qualitative-only language?

Write your answers in this format for each criterion:
`C-NN: Text [direction Y/N, contrast Y/N, chain Y/N]. Pass [location Y/N, observable Y/N, no-qualitative Y/N].`

Do not proceed if any criterion has a "N" answer -- revise the failing field first.

---

### Step 5a: Category divergence check

Before moving to Step 6, count how many criteria in each tier (essential, recommended,
aspirational) fall into each category (correctness, depth, format, coverage, behavior).
Identify the dominant category per tier.

Write down:
- Essential tier dominant category
- Recommended tier dominant category
- Aspirational tier dominant category (placeholder -- you will fill this after Step 7)

At least two of the three tiers must have different dominant categories. If the essential
and recommended tiers share the same dominant category, revise assignments before continuing.

---

### Step 6: Identify a reference case

Find a specific prior rubric or competing approach that passes your essential and recommended
criteria but falls short of a higher bar you have not yet defined. Record:

```
Reference case: [name or identifier]
Passes: [which criteria it satisfies -- at least C-01 through C-08]
Falls short of: [the specific dimension where it does not reach the aspirational level]
Blocked role: Step 7 (independence check) cannot begin until this reference case is
             complete with the "falls short" dimension populated.
```

Do not begin Step 7 if the reference case is missing or if "falls short of" is blank.

---

### Step 7: Independence check

Before you begin, confirm: the reference case from Step 6 is complete (both "passes" and
"falls short of" are populated, including the "blocked role" declaration).

Read your essential and recommended criteria. For each aspirational criterion you plan to
add, identify the structural mechanism it would require.

Write an independence map:

```
Mechanism     | Independent? | Will close
[name]        | Yes, closes C-NN only | [placeholder]
```

Each row must cover exactly one criterion gap. No two rows should cover the same gap; no
single row should cover two gaps.

Do not begin Step 8 if the map is incomplete or if any row covers multiple gaps.

Step 8 (aspirational criteria) cannot begin until this independence map is complete with
"Yes, closes C-NN only" in every row.

---

### Step 8: Aspirational criteria (1-2)

Before you begin, confirm: the independence map from Step 7 is complete and the reference
case falls-short dimension is populated.

Draft aspirational criteria that close the gap named in the reference case. One criterion per
row in the independence map.

Write 1 or 2 aspirational criteria. Do not write more than 2.

If you want to introduce a comparison case, place it immediately before that specific
criterion. End the comparison description with: "From the description above, work out what
the required approach must look like before reading the definition below."

Each criterion: same five fields as Step 3. Note which independence map row it closes:
**Closes:** [independence map row].

---

### Step 9: Final audit and emit

Run two verification passes.

**Pass 1 -- criterion quality (all criteria):**

```
| C-NN | Text: D/C/CC | Pass: L/O/Q | Status |
```

**Pass 2 -- structural verification:**

1. Category distribution per tier -- confirm at least 2 of 3 tiers have distinct dominant
   categories. Write down each tier's dominant category.

2. Scoring section -- confirm all of the following are stated: composite formula, denominator,
   golden threshold, and handling for partial credit (what score value + what earns it).

3. Reference case -- confirm it names a specific prior version, lists criteria it passes, and
   states a falls-short dimension.

4. Independence map closure -- confirm each aspirational criterion cites its independence map
   row and each map row is closed by exactly one criterion.

5. Gate declarations -- confirm: the template step (Step 2) names the constraint that blocks
   Steps 3 and 4; the independence-map step (Step 7) names the constraint that blocks Step 8;
   the reference case (Step 6) names the constraint that blocks Step 7; the reference case
   "blocked role" field names Step 7 as the consumer.

Emit the final rubric in order: essential -> recommended -> aspirational -> scoring section.

Before emitting, confirm: both templates present (Step 2); independence map complete (Step 7);
reference case falls-short populated and blocked role named; at least 3 distinct categories
across the rubric; partial credit handling stated with score value and earn conditions.

---

## V-03 -- C-39 Probe

**Axis:** C-39 probe -- the ROLE: DUAL AUDITOR's category-distribution verification step
(Audit Track 2, step 1) is preceded by a named TIER-BLIND CATEGORIZER competitor block.
The block describes the failure mode of assigning categories without tier-level majority
awareness. C-39 is the only new structural element introduced. C-46 ablated (MECHANISM
DEFINER GATE standard form, no successor named). C-47 ablated (REFERENCE ANCHOR standard
form, no Consumer field). C-41 ablated. STATUS QUO COMPETITOR opening block absent. C-42
ablated (PHASE-LOCALITY RULE not stated; competitor placement tested through presence only).

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain a TIER-BLIND CATEGORIZER competitor block immediately before the category-distribution count step in ROLE: DUAL AUDITOR; the competitor block will end with a derivation instruction requiring the model to derive the correct divergence-check procedure before reading the step; any rubric where the category-distribution step appears without a companion competitor block falsifies the hypothesis; the falsification signal is a rubric that completes Audit Track 2 step 1 without a preceding competitor. | The TIER-BLIND CATEGORIZER competitor changes how the model reads the category-distribution check: rather than reading the check as a positive verification procedure, the model reads the foil's failure mode and derives the procedure; this may produce more explicit tier-majority calculations in the audit output because the model derived the need for tier-awareness rather than executing a stated procedure. | V-04 is the primary extension: V-03 establishes C-39 in isolation; V-04 adds C-47 (anchor Consumer field) to test whether C-39 and C-47 are jointly satisfiable without C-46. If V-04 passes both C-39 and C-47, the two signals are structurally orthogonal. If V-04 fails C-39 but passes C-47, anchor consumer naming and divergence competitor placement interact. |

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

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form -- in
any phrasing -- is any Text that locates causality in the wrong form's consequence.
The Auditor check function tests causal structure, not pattern matching.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

DEFINER OUTPUT GATE is satisfied when: Text template and Pass template are both present in
slot-fillable form, derived from the skill spec. Nothing else. STOP if this role's output
contains anything beyond the two required templates -- rewrite before proceeding to Phase 3.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied when:** Text template and Pass template are
both present in slot-fillable form.

Draft from blocking failure modes. Apply Text template and Pass template to each criterion.

If introducing a competitor: place the competitor block immediately before this criterion's
definition. Do not group competitors in a shared preamble.

Each criterion: C-NN, Text (slot-filled), Weight: essential, Category, Pass (slot-filled).

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied when:** Text template and Pass template are
both present in slot-fillable form.

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

Each criterion: same five fields. **Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

For each criterion from Phases 3 and 4, run the isolation audit.

**Text field checks:** Direction / Contrast / Causal chain (Y/N each).
**Pass field checks:** Location / Observable / No-qualitative (Y/N each).

**Required format:**
```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

---

### PHASE 5 -- REFERENCE ANCHOR

Identify a specific competitor or prior-version rubric that passes essential and recommended
criteria. Record where it falls short of the aspirational bar.

```
REFERENCE ANCHOR:
  Reference:   [specific competitor or prior-version identifier]
  Passes:      [criteria it satisfies -- at minimum C-01 through C-08]
  Falls-short: [exact dimension on which it fails to meet the aspirational bar]
```

STOP if this REFERENCE ANCHOR block is absent before Phase 5.5 begins, or if the Falls-short
field is blank. Complete the anchor before proceeding.

---

### PHASE 5.5 -- MECHANISM DEFINER

Read the essential and recommended criteria from Phases 3 and 4. Identify which aspirational
criteria would require new independent mechanisms -- one mechanism per aspirational gap.

Produce an independence map:

```
Mechanism | Independence | Criterion slot
[name]    | Yes / No     | [TBD or C-NN]
```

If any row is "No" (two mechanisms jointly close one criterion, or one mechanism covers two
criteria), redesign before proceeding.

**MECHANISM DEFINER GATE is satisfied when:** Independence map is complete with "Yes" in
every row. Nothing else. STOP if this phase's output contains criteria drafts or anything
beyond the independence map.

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE:** MECHANISM DEFINER GATE must be satisfied. REFERENCE ANCHOR Falls-short
must be populated.

Draft aspirational criteria from the REFERENCE ANCHOR Falls-short dimension. 1-2 aspirational
criteria. Each criterion must correspond to one mechanism row in the independence map.

If introducing a competitor: place block immediately before the criterion, ending with:
"From the description above, derive the required implementation before reading the positive
definition below."

Five fields per criterion + **Gap closed:** [mechanism row citation].

---

### ROLE: DUAL AUDITOR

**Audit Track 1 -- Criterion quality:**

Per-criterion table: `C-NN | Text [D/C/CC] | Pass [L/O/Q] | Status`.

**Audit Track 2 -- Structural verification:**

> **TIER-BLIND CATEGORIZER** -- The standard category audit reads each criterion's Category
> field and confirms the field contains a valid category name. It may note that multiple
> categories appear in the rubric. It does not separate counts by tier (essential /
> recommended / aspirational), does not identify a majority category per tier, and does not
> check whether different tiers have different majority categories. A rubric where essential
> criteria are predominantly "correctness" and aspirational criteria are also predominantly
> "correctness" passes the standard audit: both tiers assign meaningful, present categories,
> and variation exists somewhere across the full rubric. The convergence -- both tiers sharing
> majority "correctness" -- is invisible to the standard check because the check is not
> tier-aware. The resulting rubric maps essential and aspirational criteria to the same quality
> dimension, collapsing what should be two distinct quality axes (severity vs sophistication)
> into one. From the description above, derive what the category-distribution divergence check
> must verify before reading the check below.

1. **Category distribution**: Count category assignments per tier. Identify majority category
   per tier. Record:
   ```
   Essential: [category] x[N] -- majority: [category]
   Recommended: [category] x[N] -- majority: [category]
   Aspirational: [category] x[N] -- majority: [category]
   ```
   STOP if fewer than 2 of 3 tiers have distinct majority categories -- revise before Emit.

2. **Scoring section**: formula + denominator + threshold + PARTIAL (score value + earn
   conditions).

3. **Competitor coverage**: one competitor per novel aspirational criterion.

---

### EMIT

Final rubric: essential -> recommended -> aspirational -> scoring.

Emit manifest: (a) DEFINER OUTPUT GATE satisfied; (b) MECHANISM DEFINER GATE satisfied;
(c) REFERENCE ANCHOR Falls-short populated; (d) >= 3 distinct categories;
(e) PARTIAL handling stated with score value and earn conditions;
(f) TIER-BLIND CATEGORIZER competitor present before category-distribution count step.

---

## V-04 -- C-39 + C-47 Combined

**Axis:** C-39 + C-47 -- V-03 form (TIER-BLIND CATEGORIZER inline at Dual Auditor
category-count step) combined with V-03/R17 form (REFERENCE ANCHOR Consumer field naming
ROLE: MECHANISM DEFINER as the blocked consumer). Tests whether C-39 and C-47 are jointly
satisfiable without the full gate stack. C-46 ablated (MECHANISM DEFINER GATE standard form,
no successor named). C-41 ablated. C-42 ablated. STATUS QUO COMPETITOR opening block absent.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain both the TIER-BLIND CATEGORIZER competitor block at the category-distribution step and the Consumer field in the REFERENCE ANCHOR naming ROLE: MECHANISM DEFINER; any rubric that has only one of these two structures falsifies the corresponding single-axis hypothesis carried into the combined context; the primary falsification signal is a rubric where adding the Consumer field (C-47) causes the TIER-BLIND CATEGORIZER to be dropped, or vice versa -- this would indicate the two signals compete for the same structural slot. | If V-04 passes both C-39 and C-47, and V-03 (C-39 only, C-47 ablated) also passes C-39, then the two signals are independently satisfiable and do not require each other. If V-04 passes C-39 but fails C-47, the Consumer field in the REFERENCE ANCHOR may interfere with how the model reads the anchor block, causing it to skip the divergence competitor. | V-05 is the primary full-stack test: V-04 establishes joint satisfiability of C-39 and C-47 without C-46; V-05 adds C-46 (gate successor named) and all other R17 structures to confirm joint satisfiability under the full gate stack. If V-05 passes C-39 while V-04 also passes C-39, the Tier-Blind Categorizer pattern is stable across stack completeness variations. |

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

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form -- in
any phrasing -- is any Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

DEFINER OUTPUT GATE is satisfied when: Text template and Pass template are both present in
slot-fillable form, derived from the skill spec. Nothing else. STOP if output exceeds the two
required templates.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE:** DEFINER OUTPUT GATE satisfied.

Draft from blocking failure modes. Apply Text template and Pass template to each criterion.

Inline competitors before each criterion if applicable. Five fields per criterion.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE:** DEFINER OUTPUT GATE satisfied.

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

Five fields + **Dimension:** annotation.

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

Isolation audit: Text flags (direction / contrast / causal chain) + Pass flags (location /
observable / no-qualitative).

Required format:
```
C-NN: Text flags: [D Y/N, C Y/N, CC Y/N]. Pass flags: [L Y/N, O Y/N, Q Y/N].
```

---

### PHASE 5 -- REFERENCE ANCHOR

Identify a specific competitor or prior-version rubric that passes C-01--C-08. Record where
it falls short of the aspirational bar.

```
REFERENCE ANCHOR:
  Reference:   [specific competitor or prior-version identifier]
  Passes:      [criteria satisfied -- minimum C-01 through C-08]
  Falls-short: [exact aspirational dimension where it fails]
  Consumer:    ROLE: MECHANISM DEFINER cannot begin until this anchor is complete.
               The Falls-short dimension defines the aspirational gap that the
               Mechanism Definer's independence map must cover.
```

STOP if this REFERENCE ANCHOR block is absent before Phase 5.5 begins, or if the Falls-short
field is blank, or if the Consumer field is blank.

---

### PHASE 5.5 -- BUILDER ASPIRATIONAL PRECONDITION CHECK

Before ROLE: BUILDER ASPIRATIONAL begins:
1. DEFINER OUTPUT GATE satisfied (both templates present).
2. REFERENCE ANCHOR complete (Falls-short and Consumer fields populated).

STOP if any prerequisite is unsatisfied.

---

### ROLE: MECHANISM DEFINER

Read essential and recommended criteria. Identify aspirational gaps requiring independent
mechanisms.

Independence map:
```
Mechanism | Independence | Affects criterion
[name]    | Yes -- affects C-NN only | [TBD or C-NN]
```

STOP if any row is "No". STOP if any row cites multiple criteria. Do not proceed until map
is complete.

**MECHANISM DEFINER GATE is satisfied when:** Independence map complete with "Yes --
affects C-NN only" in every row. Nothing else.

---

### ROLE: BUILDER ASPIRATIONAL

**PREREQUISITE:** MECHANISM DEFINER GATE satisfied. REFERENCE ANCHOR Falls-short and
Consumer fields populated.

Draft 1-2 aspirational criteria from the REFERENCE ANCHOR Falls-short dimension. Each
criterion corresponds to one row in the independence map.

Inline competitors: place before criterion, end with derivation instruction.

Five fields + **Gap closed:** [independence map row M-NN].

Aspirational count: 1-2. STOP if more than 2.

---

### ROLE: DUAL AUDITOR

**Audit Track 1:** Per-criterion table `C-NN | Text [D/C/CC] | Pass [L/O/Q] | Status`.

**Audit Track 2:**

> **TIER-BLIND CATEGORIZER** -- The standard category audit reads each criterion's Category
> field and confirms the field contains a valid category name. It may note that multiple
> categories appear in the rubric. It does not separate counts by tier (essential /
> recommended / aspirational), does not identify a majority category per tier, and does not
> check whether different tiers have different majority categories. A rubric where essential
> criteria are predominantly "correctness" and aspirational criteria are also predominantly
> "correctness" passes the standard audit: both tiers assign meaningful, present categories,
> and variation exists somewhere across the full rubric. The convergence -- both tiers sharing
> majority "correctness" -- is invisible to the standard check because the check is not
> tier-aware. The resulting rubric maps essential and aspirational criteria to the same quality
> dimension, collapsing what should be two distinct quality axes (severity vs sophistication)
> into one. From the description above, derive what the category-distribution divergence check
> must verify before reading the check below.

1. Category distribution per tier. STOP if < 2 tiers have distinct majority categories.
   ```
   Essential: [category] x[N] -- majority: [category]
   Recommended: [category] x[N] -- majority: [category]
   Aspirational: [category] x[N] -- majority: [category]
   ```
2. Scoring: formula + denominator + threshold + PARTIAL (score value + earn conditions).
3. Competitor coverage bijection.
4. Consumer field in REFERENCE ANCHOR populated with ROLE: MECHANISM DEFINER.

---

### EMIT

Final rubric: essential -> recommended -> aspirational -> scoring.

Manifest: (a) DEFINER OUTPUT GATE; (b) MECHANISM DEFINER GATE; (c) REFERENCE ANCHOR
(Falls-short + Consumer); (d) >= 3 categories; (e) PARTIAL handling;
(f) TIER-BLIND CATEGORIZER competitor present before category-distribution step.

---

## V-05 -- All Axes + Full Stack (Ceiling)

**Axis:** All axes + full nine-gate stack -- R17 V-05's eight-gate stack (STATUS QUO
COMPETITOR opening block; DEFINER OUTPUT GATE with C-40+C-43+C-44; REFERENCE ANCHOR with
Consumer field naming MECHANISM DEFINER: C-47; MECHANISM DEFINER GATE with C-43+C-44+C-46
naming BUILDER ASPIRATIONAL; BUILDER ASPIRATIONAL entry quoting both gates verbatim: C-41;
PHASE-LOCALITY RULE: C-42) plus C-39 probe: TIER-BLIND CATEGORIZER competitor inline at the
ROLE: DUAL AUDITOR category-distribution count step (Audit Track 2, step 1), in canonical
competitor-block format (description of failure mode + derivation instruction). C-48 candidate
is realized: the Tier-Blind Categorizer block follows the canonical format, is placed inline
at the count step only (not at phase boundary), and governs exactly one audit check.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain all nine structural elements: (1) STATUS QUO COMPETITOR opening block deriving Phase 1 from the foil's failures; (2) DEFINER OUTPUT GATE with satisfaction predicate + exclusion terminal + embedded STOP (C-40+C-43+C-44); (3) REFERENCE ANCHOR Consumer field naming ROLE: MECHANISM DEFINER (C-47); (4) MECHANISM DEFINER GATE with satisfaction predicate + exclusion terminal + embedded STOP naming ROLE: BUILDER ASPIRATIONAL as blocked consumer (C-43+C-44+C-46); (5) BUILDER ASPIRATIONAL entry quoting both CRITERION DEFINER GATE and MECHANISM DEFINER GATE verbatim (C-41); (6) PHASE-LOCALITY RULE with three prohibited zones (C-42); (7) TIER-BLIND CATEGORIZER competitor inline at Audit Track 2 step 1, category-count sub-step (C-39); (8) Tier-Blind Categorizer in canonical competitor-block format with derivation instruction (C-48 candidate); (9) REFERENCE ANCHOR STOP embedded before ROLE: MECHANISM DEFINER entry (C-45); any rubric missing any one of these nine structures is not V-05. | C-39 and C-47 together close cross-layer bidirectional traceability for a different dimension: C-47 makes the anchor -> Mechanism Definer dependency forward-visible from the anchor block; C-39 makes the category-diversity requirement derivable from a foil's failure at the point where diversity is verified. If V-05 passes both, the two independence signals (bidirectional anchor dependency and divergence-check competitor placement) are mutually compatible in the full stack. | V-04 is the primary partial-combination control for C-39+C-47 joint satisfiability; V-03 is the C-39 isolation control; comparing V-03 (C-39 only), V-04 (C-39+C-47), and V-05 (C-39+C-47+full stack) determines whether C-39 is stable across stack completeness levels and whether C-48 (canonical format) requires the full gate context to appear reliably. |

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
  "adequately covers," "is well-structured" as sole observables, not anchored to artifact
  locations or measurable tokens.
- Fails to name a specific reference anchor with a Falls-short dimension -- aspirational
  criteria address a hypothetical improvement rather than a specific identified gap.
- Fails to verify mechanism independence -- aspirational criteria accumulate without
  confirming each introduces exactly one new structural mechanism.
- Fails to make role dependencies bidirectionally traceable -- the gate enforces sequencing
  but does not name the specific role waiting on it; the anchor enforces completeness but
  does not name the role that consumes it.
- Fails to verify category diversity by tier -- category distribution is checked globally
  (variety exists somewhere) rather than per tier (each tier has a distinct majority), making
  tier convergence invisible.

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

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form -- in
any phrasing -- is any Text that locates causality in the wrong form's consequence: "X causes
failure," "failure occurs when X is present," "X leads to Z," and all semantic equivalents.
The Auditor check function tests causal structure, not pattern matching against canonical
examples.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

DEFINER OUTPUT GATE is satisfied when: Text template and Pass template are both present in
slot-fillable form, derived from the skill spec, with no additional content. Nothing else.
STOP if this role's output contains anything beyond the two required templates -- rewrite
before proceeding to Phase 3.

ROLES: PHASE 3 and PHASE 4 cannot begin until DEFINER OUTPUT GATE is satisfied.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied when:** Text template and Pass template are
both present in slot-fillable form, derived from the skill spec.

Draft from blocking failure modes. Apply Text template and Pass template to each criterion.

If introducing a competitor:

> **[COMPETITOR NAME]** -- [description of the wrong implementation: what it does, what
> surface form it has, why it fails to close the criterion gap]. This competitor IS the gap
> specification -- from the description above, derive the required implementation before
> reading the positive definition below.

Place the competitor block immediately before this criterion's definition. Do not group
competitors in a shared preamble.

Each criterion requires five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: Apply CRITERION DEFINER Text template. "Without [Y], the artifact [fails] because
  [Z]. Not [X], but [Y]." with skill-specific values.
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass**: Apply CRITERION DEFINER Pass template. No "is clear" or "adequately covers" as
  sole observable.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied when:** Text template and Pass template are
both present in slot-fillable form.

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: place block immediately before the criterion, with derivation
instruction at the end.

Each criterion: same five fields as Phase 3. Required annotation:
**Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

For each criterion from Phases 3 and 4, run the isolation audit. Read each field stripped
of surrounding context.

**Text field checks (3):**
1. **Direction**: does Text locate causality in Y's absence? (not X's presence)
2. **Contrast**: does Text name the rejected form X alongside Y?
3. **Causal chain**: does Text name the downstream consequence Z?

**Pass field checks (3):**
4. **Location**: does Pass name an artifact location, field, or section?
5. **Observable**: does Pass name a specific count, token, or structural property?
6. **No qualitative-only**: does Pass avoid bare qualitative language without an anchor?

**Audit report format -- required; do not substitute a narrative log:**

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

---

### PHASE 5 -- REFERENCE ANCHOR

**Do not proceed to PHASE 5 until the gap zone contains at least G-01.**

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

STOP if this REFERENCE ANCHOR block is absent before ROLE: MECHANISM DEFINER begins, or if
the Falls-short field is blank, or if the Consumer field does not name ROLE: MECHANISM DEFINER
as the blocked consumer.

---

### PHASE-LOCALITY RULE

The following placement zones are prohibited for all competitor blocks:

1. **Preamble zone**: any block appearing before any construction phase (Phases 3, 4, 6).
2. **Shared-operating-principles zone**: any block in an operating-principles or shared block
   preceding more than one construction step.
3. **Multi-criterion zone**: any combined block governing more than one criterion.

A competitor is correctly placed if and only if it does not appear in any of the three
enumerated prohibited zones. This rule is a required Emit manifest verification target.

---

### ROLE: MECHANISM DEFINER

**This role runs after Phase 4.5 and before ROLE: BUILDER ASPIRATIONAL.**

**PREREQUISITE:** REFERENCE ANCHOR is complete (Falls-short populated; Consumer field names
ROLE: MECHANISM DEFINER as the blocked consumer).

Read essential and recommended criteria. For each anticipated aspirational criterion, identify
the structural mechanism it would require. Produce an independence map.

**Independence map format:**

```
Mechanism        | Independence             | Affects criterion
[mechanism name] | Yes -- affects C-NN only | [TBD or criterion number]
```

Each row must be mutually exclusive. Removing any one mechanism leaves exactly one criterion
failing. No mechanism may carry dual responsibility for two gaps.

If any row is "No": stop, redesign, and restart this role.

**MECHANISM DEFINER GATE is satisfied when:** Independence map is complete with "Yes --
affects C-NN only" in every row, and every anticipated aspirational gap has a mechanism row.
Nothing else. STOP if this role's output contains anything beyond the independence map.

ROLE: BUILDER ASPIRATIONAL cannot begin until this gate is satisfied.

---

### ROLE: BUILDER ASPIRATIONAL

**Input required:**

- **CRITERION DEFINER GATE**: Text template and Pass template in slot-fillable form.
- **MECHANISM DEFINER GATE**: Independence Map with all C-NN citations populated.

**ROLE: BUILDER ASPIRATIONAL cannot begin unless both gate artifacts exist.**

Draft aspirational criteria that close the exact gap named in the REFERENCE ANCHOR Falls-short
field. One criterion per mechanism in the independence map.

**Aspirational tier count: 1-2 criteria.** STOP if you draft more than 2 aspirational
criteria. Rewrite to stay within range.

If introducing a competitor:

> **[COMPETITOR NAME]** -- [description of wrong implementation]. From the description above,
> derive the required implementation before reading the positive definition below.

Place each competitor block immediately before the criterion it governs -- not in a preamble,
not in a shared block, not governing more than one criterion. PHASE-LOCALITY RULE applies.

Each criterion requires five fields: ID, Text (slot-filled from CRITERION DEFINER templates),
Weight: aspirational, Category, Pass (slot-filled from CRITERION DEFINER templates).

Required annotation: **Gap closed:** [independence map mechanism row citation, format:
"Yes -- affects C-NN only"].

---

### ROLE: DUAL AUDITOR

Run two audit tracks sequentially.

**Audit Track 1 -- Criterion quality (all criteria):**

For each criterion, run the isolation audit.

Output as per-criterion table -- do not substitute a narrative log:

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
> names, variety exists in the rubric overall. The tier convergence -- two tiers sharing
> majority "correctness" -- is invisible to the standard check because the check is
> tier-agnostic. The resulting rubric maps essential severity and aspirational sophistication
> to the same quality axis, collapsing what should be two structurally distinct dimensions
> into one. An auditor using this approach cannot detect whether a rubric has structurally
> distinct tiers or merely distinct criteria within a single quality dimension. From the
> description above, derive what the category-distribution divergence check must verify
> before reading the check below.

1. **Category distribution**: Count category assignments per tier. Identify majority category
   per tier. Record:
   ```
   Essential: [category] x[N] -- majority: [category]
   Recommended: [category] x[N] -- majority: [category]
   Aspirational: [category] x[N] -- majority: [category]
   ```
   STOP if fewer than 2 of 3 tiers have distinct majority categories -- revise before Emit.

2. **Scoring section**: Confirm all present:
   - Composite formula (Essential weight + Recommended weight + Aspirational weight)
   - Denominator
   - Golden threshold (numeric)
   - PARTIAL handling: score value (e.g., 0.5) AND earn conditions

3. **Competitor coverage bijection**: For each novel aspirational criterion, confirm exactly
   one competitor block accompanies it. Count novel criteria. Count competitor blocks.
   Confirm counts match.

4. **Anchor chain**: Confirm REFERENCE ANCHOR has:
   - Falls-short field populated
   - Consumer field naming ROLE: MECHANISM DEFINER

5. **Gate chain**: Confirm:
   - DEFINER OUTPUT GATE ends with exclusion terminal and embedded STOP
   - MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL as blocked consumer
   - BUILDER ASPIRATIONAL entry quotes MECHANISM DEFINER GATE verbatim
   - PHASE-LOCALITY RULE: no competitor in any of the three prohibited zones
   - TIER-BLIND CATEGORIZER competitor: placed inline before category-distribution count
     step; ends with derivation instruction; governs exactly one audit check

---

### EMIT

Produce the final rubric in this order:

1. Essential criteria (C-01 through C-NN)
2. Recommended criteria
3. Aspirational criteria
4. Scoring section

**Scoring section must include:**
- Composite formula
- Denominator (/NN)
- Golden threshold (>= NN)
- PARTIAL: score value and earn conditions ("PARTIAL = 0.5: criterion is present but
  [specific condition for partial credit]")

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
| TIER-BLIND CATEGORIZER: inline at category-count step, canonical format, one check governed | |
| Category diversity: >= 3 distinct categories across full rubric | |
| Aspirational tier count: 1-2 criteria | |
| PARTIAL handling stated with score value and earn conditions | |
