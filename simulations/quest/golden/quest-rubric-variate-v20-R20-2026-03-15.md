# quest-rubric Variate -- Round 20 (Against rubric v19)
**Date:** 2026-03-15
**Rubric:** v19 (C-01--C-51; denominator /43; adds C-50: scoring-section-named-tier-table,
C-51: gate-scope-note-structural-equivalence-basis)
**Target criteria:** C-38 (persistent fail since R1 -- class-recognition-app-note);
C-50, C-51 (stability confirmation under new axes); C-52 candidate:
`phase-1-severity-taxonomy-feeds-tier`

**Round 20 design note:** R19 confirmed C-50 (`scoring-section-named-tier-table`) and C-51
(`gate-scope-note-structural-equivalence-basis`), raising the ceiling to 42/43 = 99.77.
C-38 (`class-recognition-app-note`) is the sole blocking criterion. No variation across
R1--R19 has produced a scoring-model-applicable class-recognition note that passes C-38.
R20 design goals:
(1) target C-38 with the strongest combined probe to date -- V-03 simultaneously deploys
three mechanisms (foil names class-recognition failure + EMIT note with structural-equivalence
basis + DEFINER OUTPUT GATE scope-closure grounded in class-recognition terms), never tried
together;
(2) probe C-52 candidate `phase-1-severity-taxonomy-feeds-tier` via lifecycle-emphasis
variation (V-02);
(3) test phrasing-register variation (V-01) to determine whether declarative prose preserves
gate/anchor structural compliance under new rubric version;
(4) test role-sequence + output-format combined variation (V-04: CRITERION DEFINER twice +
GOLD/SILVER/BRONZE supplementing composite formula) to confirm C-50 stability under sequence
change;
(5) full-stack ceiling attempt in V-05 (all 43 criteria + C-38 triple probe + C-52 Phase 1
taxonomy + C-50 tier table supplementing formula + C-51 structural-equivalence basis).

**C-52 candidate -- `phase-1-severity-taxonomy-feeds-tier`:**

V-02 R20 probe -- Phase 1's failure mode log includes a mandatory SEVERITY-TO-TIER
DERIVATION step: after logging all failure modes (blocking / suboptimal / cosmetic), the
prompt requires an explicit mapping table linking each failure mode to its target criterion
tier (essential / recommended / aspirational / no criterion). Blocking failures map to
essential criteria; suboptimal failures map to recommended; cosmetic failures map to
aspirational or no criterion. A rubric output satisfying C-52 shows this derivation table
in Phase 1 output, making weight assignment traceable to failure severity. A rubric output
failing C-52 has a failure log without a derivation table -- the severity taxonomy is present
as a label convention but is not structurally functional: weights in Phases 3 and 4 are
asserted editorially rather than derived from the taxonomy.

**Key distinction C-52 != C-01--C-51:** C-52 governs Phase 1 output format (derivation table
present, mapping every logged failure to a criterion tier), not criterion field format, not
gate structure, not scoring section. A rubric satisfying all 51 existing criteria while
lacking Phase 1 derivation table fails C-52 without failing any existing criterion. The
derivation table does not appear in the emitted rubric artifact -- it is a production-stage
intermediate that is verified by looking at the Phase 1 section of the prompt output.

---

**Variation axes used in R20:**

| # | Axis | C-38 probe | C-50 | C-51 | C-52 | Notes |
|---|------|-----------|------|------|------|-------|
| V-01 | Phrasing register (declarative) | Ablated | Ablated | Ablated -- declarative gate, no structural-equivalence basis | Ablated | Single-axis: all instructions rewritten in declarative/descriptive register; STOP -> "output is not complete if"; tests whether register change breaks gate/anchor structural compliance |
| V-02 | Lifecycle emphasis (Phase 1 taxonomy) | Ablated | Ablated | Ablated | Strong -- derivation table required in Phase 1 | Single-axis: Phase 1 expanded with severity-to-tier derivation table + explicit mapping step; rest standard; isolates C-52 signal |
| V-03 | Inertia framing (C-38 maximum probe) | Strong -- triple mechanism | Ablated | Strong -- gate scope-closure grounded in class-recognition terms | Ablated | Single-axis: foil names class-recognition failure (8th item) + EMIT CLASS RECOGNITION APPLICATION NOTE with structural-equivalence basis + DEFINER OUTPUT GATE scope-closure with structural-equivalence basis; most aggressive C-38 probe to date |
| V-04 | Role sequence + output format | Ablated | Strong -- GOLD/SILVER/BRONZE supplementing formula | Ablated | Ablated | Two-axis: CRITERION DEFINER runs twice (Phase 0.5 initial + Phase 2.5 review); scoring section adds named-tier table supplementing formula; tests C-50 stability under sequence change |
| V-05 | Full stack R20 | Strong -- triple mechanism | Strong -- tier table supplementing formula | Strong -- gate structural-equivalence basis | Strong -- Phase 1 derivation table | Ceiling attempt: all R19 V-05 + C-38 triple + C-52 Phase 1 taxonomy; STATUS QUO COMPETITOR extended to 9 foil items |

---

## Round 20 Variation Map

| Variation | Axis | C-38 | C-49 | C-50 | C-51 | C-52 | C-43 | C-44 | C-45 | C-46 | C-47 | C-41 | C-42 | C-39 | C-48 | Notes |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|
| V-01 | Phrasing register | Ablated | Strong -- foil names tier-diversity failure | Ablated | Ablated -- gate closure in declarative form, no structural-equivalence basis | Ablated | Strong -- predicate present in declarative form | Strong -- completion condition present in declarative form | Strong -- anchor "does not begin until" in declarative form | Strong -- gate names BUILDER ASPIRATIONAL | Strong -- Consumer field present | Strong -- Builder entry quotes both gates verbatim | Strong -- PHASE-LOCALITY RULE present in declarative form | Strong -- TIER-BLIND CATEGORIZER canonical inline | Strong -- canonical format preserved | Single-axis: phrasing only; tests whether declarative register breaks C-43 (predicate form), C-44 (embedded STOP), C-45 (anchor STOP) |
| V-02 | Lifecycle emphasis | Ablated | Strong -- foil names tier-diversity failure | Ablated | Ablated | Strong -- derivation table in Phase 1 | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Single-axis: Phase 1 expanded; tests whether severity taxonomy expansion produces C-52 observable without disrupting standard mechanisms |
| V-03 | Inertia framing | Strong -- foil + EMIT + gate basis | Strong -- foil names tier-diversity failure | Ablated | Strong -- gate basis grounded in class-recognition terms | Ablated | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Single-axis C-38 maximum; STATUS QUO COMPETITOR foil has 8 items; EMIT has full CLASS RECOGNITION APPLICATION NOTE with structural-equivalence basis; DEFINER OUTPUT GATE scope-closure has structural-equivalence basis connecting class-recognition |
| V-04 | Role sequence + output format | Ablated | Strong -- foil names tier-diversity failure | Strong -- GOLD/SILVER/BRONZE supplementing formula | Ablated | Ablated | Strong | Strong | Strong | Strong | Strong | Strong -- Builder quotes both gates including Phase 2.5 templates | Strong | Strong | Strong | Two-axis: CRITERION DEFINER runs twice; scoring section adds tier table; tests C-50 stability under sequence + format change |
| V-05 | Full stack R20 | Strong -- foil + EMIT + gate basis | Strong -- foil names tier-diversity failure (item 7) | Strong -- tier table supplementing formula | Strong -- gate structural-equivalence basis | Strong -- Phase 1 derivation table | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Ceiling attempt: all R19 V-05 mechanisms + C-52 probe; STATUS QUO COMPETITOR foil has 9 items (adds severity-taxonomy gap); path to 100 requires C-38 pass |

---

## V-01 -- Phrasing Register

**Axis:** Phrasing register -- all instructions rewritten in declarative/descriptive prose.
Imperative forms ("Do not begin X until Y", "STOP if...") are replaced by declarative
equivalents ("X begins after Y is produced", "The output is not complete if..."). Role names
are retained but all directives use descriptive framing. STOP conditions become completion
criteria: "This role's output is complete when X" rather than "STOP if not X."

All R18/R19 structural mechanisms preserved: STATUS QUO COMPETITOR opening block with
tier-diversity failure item (C-49); DEFINER OUTPUT GATE predicate in declarative form (C-43)
with embedded completion condition (C-44); MECHANISM DEFINER GATE naming ROLE: BUILDER
ASPIRATIONAL (C-46); REFERENCE ANCHOR Consumer field naming ROLE: MECHANISM DEFINER (C-47)
with declarative STOP at Mechanism Definer entry (C-45); BUILDER ASPIRATIONAL quotes both
gates verbatim (C-41); PHASE-LOCALITY RULE (C-42); TIER-BLIND CATEGORIZER in canonical
derivation format inline at category-count step (C-39, C-48); composite formula + denominator
+ golden threshold + PARTIAL (C-02).

Ablated: C-38 (no CLASS RECOGNITION APPLICATION NOTE); C-50 (standard formula scoring, no
named-tier table); C-51 (DEFINER OUTPUT GATE scope-closure note present in declarative form
but no structural-equivalence basis -- to isolate phrasing effect); C-52 (no Phase 1
derivation table).

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will preserve gate/anchor structure (DEFINER OUTPUT GATE, MECHANISM DEFINER GATE, REFERENCE ANCHOR) under declarative phrasing; the primary falsification signal is a rubric where ROLE: CRITERION DEFINER outputs criterion fields during the template-generation phase, violating the template-only constraint -- if the declarative register reduces the constraint's salience, the model may produce criteria before passing the gate; the secondary falsification signal is a rubric where the declarative completion condition ("not complete if it contains anything beyond the two required templates") is ignored because it lacks the literal word "STOP." | The DEFINER OUTPUT GATE's declarative rewrite affects C-43 and C-44 differently: C-43 requires a satisfaction predicate ("satisfied when X"); the declarative form "this role's output is complete when X" has the same logical structure but different surface form; if C-43's pass condition tests for the word "satisfied" it will fail, but if it tests for logical predicate structure it may pass. C-44 requires an embedded STOP; the declarative form "the output is not complete if it contains anything beyond..." is a conditional non-completion statement, not a literal STOP; whether C-44's pass condition is form-sensitive or semantics-sensitive determines the result. | C-43 and C-44 are the primary risk criteria: both are satisfied in imperative form across R1--R19; the declarative rewrite for the first time tests whether their pass conditions are form-sensitive or structure-sensitive. C-45 (anchor STOP at Mechanism Definer entry) is the secondary risk: the declarative equivalent "ROLE: MECHANISM DEFINER does not begin until this anchor is complete" functions as a STOP without the literal token. |

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

**From the description above, derive what the required rubric-building procedure must supply --
before reading Phase 1. State your derivation, then proceed.**

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Phase 1 produces a failure mode log. The log records every way an output of this skill can
fail. Each entry uses the format:

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

The log is complete when it contains at least 3 blocking entries and 2 suboptimal entries.
ROLE: CRITERION DEFINER receives the completed failure log as input. ROLE: CRITERION DEFINER
begins only after the failure log is complete.

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

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form, in
any phrasing, is any Text that locates causality in the wrong form's consequence.

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

**DEFINER OUTPUT GATE:** This role's output is complete when both templates are present in
slot-fillable form, derived from the skill spec, with no additional content. The output is
not complete if it contains criterion fields (ID, Text, Weight, Category, Pass), narrative
commentary, or anything other than the two required templates. Nothing else belongs in this
role's output. PHASE 3 and PHASE 4 begin only after DEFINER OUTPUT GATE is satisfied.

**Scope note:** A rubric-building output satisfying this gate contains exactly two templates
in slot-fillable form. A failing output either omits a template, provides it in
non-slot-fillable form, or adds content beyond the two templates. These two outputs are
structurally distinct.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**Input:** DEFINER OUTPUT GATE is satisfied -- both templates are present.

Phase 3 drafts from blocking failure modes. Each criterion applies the Text template and
Pass template from ROLE: CRITERION DEFINER.

Each criterion has five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: Slot-filled Text template.
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass**: Slot-filled Pass template. "is clear" or "adequately covers" as sole observable
  is not a valid Pass condition.

A competitor block, if present, appears immediately before the criterion it governs, ending
with a derivation instruction.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**Input:** DEFINER OUTPUT GATE is satisfied.

Phase 4 drafts from suboptimal failure modes. Pass conditions test degree, precision, or
specificity.

Each criterion has the same five fields as Phase 3. Each criterion includes:
**Dimension:** [degree | precision | specificity].

A competitor block, if present, appears immediately before the criterion it governs.

---

### PHASE-LOCALITY RULE

The following placement zones are prohibited for all competitor blocks:

1. **Preamble zone**: any block appearing before any construction phase.
2. **Shared-operating-principles zone**: any block preceding more than one construction step.
3. **Multi-criterion zone**: any combined block governing more than one criterion.

A competitor is correctly placed only when it does not appear in any of the three prohibited
zones. PHASE-LOCALITY RULE is a required Emit manifest verification target.

---

### PHASE 4.5 -- POST-DRAFT AUDIT

#### ISOLATION AUDIT

Phase 4.5 audits all criteria from Phases 3 and 4. Each criterion is read stripped of
surrounding context.

**Text field checks (3):**
1. **Direction**: does Text locate causality in Y's absence?
2. **Contrast**: does Text name the rejected form X alongside Y?
3. **Causal chain**: does Text name the downstream consequence Z?

**Pass field checks (3):**
4. **Location**: does Pass name an artifact location, field, or section?
5. **Observable**: does Pass name a specific count, token, or structural property?
6. **No qualitative-only**: does Pass avoid bare qualitative language without an anchor?

**Audit report format -- required:**

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

The audit is not complete if any criterion shows one or more N flags. Any criterion with a
failing flag is revised before DIVERGENCE CHECK proceeds.

#### DIVERGENCE CHECK

**Input:** ISOLATION AUDIT is complete (all criteria flagged, no failing flags remaining).

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

Count category assignments per tier. For each tier, identify the majority category. Record:

```
Essential tier:    [category] x[N] ... -- majority: [category]
Recommended tier:  [category] x[N] ... -- majority: [category]
Aspirational tier: [category] x[N]     -- majority: [category]
```

The divergence check is not complete if fewer than 2 of 3 tiers have distinct majority
categories. Category assignments are revised before proceeding to PHASE 5.

---

### PHASE 5 -- REFERENCE ANCHOR

**Input:** Phase 4.5 is complete.

Phase 5 identifies a specific competitor or prior-version rubric that passes essential and
recommended criteria. It records where it falls short of the aspirational bar.

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

Before ROLE: BUILDER ASPIRATIONAL begins, the following are confirmed:
1. DEFINER OUTPUT GATE satisfied (both templates present, no additional content).
2. MECHANISM DEFINER GATE satisfied (independence map complete, all rows "Yes").
3. REFERENCE ANCHOR complete (Falls-short populated; Consumer field names
   ROLE: MECHANISM DEFINER).

ROLE: BUILDER ASPIRATIONAL begins only after all three are confirmed.

---

### ROLE: MECHANISM DEFINER

**Input:** REFERENCE ANCHOR is complete (Falls-short populated; Consumer field names
ROLE: MECHANISM DEFINER as the blocked consumer).

This role reads essential and recommended criteria and produces an independence map for
anticipated aspirational gaps.

**Independence map format:**

```
Mechanism        | Independence             | Affects criterion
[mechanism name] | Yes -- affects C-NN only | [TBD or C-NN]
```

Each row must be mutually exclusive. Removing any one mechanism leaves exactly one criterion
failing. No mechanism carries dual responsibility for two gaps.

**MECHANISM DEFINER GATE:** This role's output is complete when the independence map contains
at least one row, every row shows "Yes -- affects C-NN only," and every anticipated
aspirational gap has a mechanism row. The output is not complete if it contains anything
beyond the independence map. ROLE: BUILDER ASPIRATIONAL begins only after MECHANISM DEFINER
GATE is satisfied.

---

### ROLE: BUILDER ASPIRATIONAL

**Input required:**

- **CRITERION DEFINER GATE**: Text template and Pass template in slot-fillable form.
- **MECHANISM DEFINER GATE**: Independence Map with all C-NN citations populated.

ROLE: BUILDER ASPIRATIONAL begins only when both gate artifacts exist.

This role drafts aspirational criteria that close the exact gap named in the REFERENCE ANCHOR
Falls-short field. One criterion per mechanism in the independence map.

**Aspirational tier count: 1-2 criteria.** If more than 2 aspirational criteria are drafted,
reduce to 2 before proceeding.

If introducing a competitor:

> **[COMPETITOR NAME]** -- [description of wrong implementation]. From the description above,
> derive the required implementation before reading the positive definition below.

Each competitor block appears immediately before the criterion it governs -- not in a
preamble, not in a shared block, not governing more than one criterion. PHASE-LOCALITY RULE
applies.

Each criterion: five fields (ID, Text slot-filled, Weight: aspirational, Category, Pass
slot-filled). Required annotation: **Gap closed:** [independence map mechanism row citation].

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
> multiple category names appear across the rubric. It does not separate assignments by tier,
> does not compute a majority category per tier, and does not check whether different tiers
> have different majority categories. A rubric where essential and aspirational criteria are
> both dominated by "correctness" passes the standard audit. The tier convergence is invisible.
> From the description above, derive what the category-distribution divergence check must
> verify before reading the check below.

1. **Category distribution per tier:**
   ```
   Essential:    [category] x[N] -- majority: [category]
   Recommended:  [category] x[N] -- majority: [category]
   Aspirational: [category] x[N] -- majority: [category]
   ```
   The distribution check is not complete if fewer than 2 of 3 tiers have distinct majority
   categories. Revise category assignments before proceeding to Emit.

2. **Scoring section**: Confirm all present:
   - Composite formula (Essential weight + Recommended weight + Aspirational weight)
   - Denominator (/NN)
   - Golden threshold (numeric)
   - PARTIAL handling: score value AND earn conditions

3. **Competitor coverage bijection**: For each novel aspirational criterion, confirm exactly
   one competitor block accompanies it.

4. **Anchor chain**: Confirm REFERENCE ANCHOR has Falls-short populated and Consumer field
   naming ROLE: MECHANISM DEFINER.

5. **Gate chain**: Confirm:
   - DEFINER OUTPUT GATE: completion condition present (both templates, no additional content)
     with embedded non-completion condition
   - MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL as blocked consumer
   - BUILDER ASPIRATIONAL entry quotes both gate artifacts verbatim
   - PHASE-LOCALITY RULE: no competitor in any of the three prohibited zones
   - TIER-BLIND CATEGORIZER competitor: placed inline before category-distribution count step;
     ends with derivation instruction; governs exactly one audit check

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

---

## V-02 -- Lifecycle Emphasis

**Axis:** Lifecycle emphasis -- Phase 1 is expanded with a mandatory SEVERITY-TO-TIER
DERIVATION step. After logging all failure modes, the prompt requires an explicit mapping
table linking each failure mode to its target criterion tier. Blocking failures must map to
essential; suboptimal failures must map to recommended; cosmetic failures must map to
aspirational or "no criterion." Phase 3 and Phase 4 must cite the derivation table when
assigning weights, making weight assignment traceable rather than editorial.

All R18/R19 structural mechanisms preserved: STATUS QUO COMPETITOR opening block with
tier-diversity failure item (C-49); DEFINER OUTPUT GATE with predicate + exclusion terminal
+ embedded STOP (C-43, C-44); MECHANISM DEFINER GATE naming ROLE: BUILDER ASPIRATIONAL
(C-46); REFERENCE ANCHOR Consumer field (C-47) + anchor STOP (C-45); BUILDER ASPIRATIONAL
quotes both gates verbatim (C-41); PHASE-LOCALITY RULE (C-42); TIER-BLIND CATEGORIZER
canonical (C-39, C-48); composite formula + denominator + threshold + PARTIAL (C-02).

Ablated: C-38 (no CLASS RECOGNITION APPLICATION NOTE, to isolate C-52 signal); C-50 (no
named-tier table); C-51 (no structural-equivalence basis in DEFINER OUTPUT GATE scope-closure
note).

C-52 probe (strong): Phase 1 includes severity-to-tier derivation table; Phases 3 and 4
require Derivation annotation referencing Phase 1 rows.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will include a severity-to-tier derivation table in Phase 1, with blocking failures mapped to essential and suboptimal failures mapped to recommended; the primary falsification signal is a rubric where Phase 1 logs failure modes with severity labels but produces no derivation table -- confirming the C-52 structural gap; the secondary falsification signal is a rubric where the derivation table appears but Phases 3 and 4 do not carry Derivation annotations, breaking the traceability chain. | The severity-to-tier derivation may create a count tension: if Phase 1 logs more than 5 blocking failures, the derivation table maps more blocking entries than the Phase 3 essential tier count range (3-5) allows; the model must either consolidate failures into shared criteria (multiple F-NN rows -> one criterion) or exceed the 3-5 range; this tension is a secondary structural signal distinct from C-52 itself. | C-52's pass condition tests derivation table presence (Phase 1 output), not bijection (one criterion per failure mode); the presence/bijection distinction is a secondary structural axis that may yield a C-53 candidate if a rubric satisfies C-52 (table present) while failing bijection (multiple failures mapped to one criterion without consolidation notation). |

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

**After logging all failure modes, produce a SEVERITY-TO-TIER DERIVATION TABLE:**

```
| F-NN | Severity    | Target tier  | Rationale                                    |
|------|-------------|--------------|----------------------------------------------|
| F-01 | blocking    | essential    | [why absence blocks core function]           |
| F-02 | suboptimal  | recommended  | [why absence degrades quality not function]  |
| F-03 | cosmetic    | aspirational | [why absence reduces excellence, not quality]|
| F-04 | cosmetic    | no criterion | [why this failure does not warrant a criterion]|
```

Rules for the derivation table:
- Every logged failure mode must appear as a row.
- Blocking -> essential; suboptimal -> recommended; cosmetic -> aspirational or no criterion.
- If two failures share the same structural gap, consolidate them into one row and note:
  "consolidated with F-NN."

**Do not begin ROLE: CRITERION DEFINER until the derivation table is complete.**

When drafting criteria in Phases 3 and 4, reference the derivation table for weight
assignment. Each criterion must carry a **Derivation:** annotation citing the Phase 1 row(s)
that justify its weight.

---

### ROLE: CRITERION DEFINER

**This role runs after Phase 1 (failure log + derivation table complete). Do not write any
criterion fields during this role.**

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

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied. Derivation table is complete.**

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

If introducing a competitor: place the competitor block immediately before this criterion's
definition. Do not group competitors in a shared preamble.

Each criterion requires five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: Apply CRITERION DEFINER Text template.
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass**: Apply CRITERION DEFINER Pass template. No "is clear" or "adequately covers" as
  sole observable.
- **Derivation:** [F-NN row(s) from Phase 1 derivation table that justify this weight
  assignment]

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied. Derivation table is complete.**

Draft from suboptimal failure modes. Apply Text template and Pass template. Pass conditions
test degree, precision, or specificity -- not whether an element exists.

If introducing a competitor: place immediately before the criterion.

Each criterion: same five fields as Phase 3. Required annotations:
**Dimension:** [degree | precision | specificity].
**Derivation:** [F-NN row(s) from Phase 1 derivation table].

After drafting recommended criteria: review the independence map from ROLE: MECHANISM
DEFINER. If any recommended criterion opens a new aspirational gap not covered by an existing
map row, add a new row. The gate is not re-satisfied until the map is updated.

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

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

For each criterion from Phases 3 and 4, run the isolation audit. Read each field stripped
of surrounding context.

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

**Do not proceed to PHASE 5 until the DIVERGENCE CHECK is complete.**

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
the Falls-short field is blank, or if the Consumer field does not name ROLE: MECHANISM
DEFINER as the blocked consumer.

---

### PHASE 5.5 -- BUILDER ASPIRATIONAL PRECONDITION CHECK

Before ROLE: BUILDER ASPIRATIONAL begins, confirm:
1. DEFINER OUTPUT GATE satisfied (both templates present, no additional content).
2. MECHANISM DEFINER GATE satisfied (independence map complete, all rows "Yes").
3. REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE: MECHANISM DEFINER).

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

Place each competitor block immediately before the criterion it governs. PHASE-LOCALITY RULE
applies.

Each criterion: five fields (ID, Text slot-filled, Weight: aspirational, Category, Pass
slot-filled). Required annotations:
**Gap closed:** [independence map mechanism row citation].
**Derivation:** [F-NN row(s) from Phase 1 derivation table, if applicable].

---

### ROLE: DUAL AUDITOR

Run two audit tracks sequentially.

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
   - PARTIAL handling: score value AND earn conditions

3. **Competitor coverage bijection**: For each novel aspirational criterion, confirm exactly
   one competitor block accompanies it.

4. **Anchor chain**: Confirm REFERENCE ANCHOR has Falls-short populated and Consumer field
   naming ROLE: MECHANISM DEFINER.

5. **Gate chain**: Confirm:
   - DEFINER OUTPUT GATE ends with exclusion terminal and embedded STOP
   - MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL as blocked consumer
   - BUILDER ASPIRATIONAL entry quotes MECHANISM DEFINER GATE verbatim
   - PHASE-LOCALITY RULE: no competitor in any of the three prohibited zones
   - TIER-BLIND CATEGORIZER competitor: placed inline before category-distribution count
     step; ends with derivation instruction; governs exactly one audit check

6. **Phase 1 derivation table**: Confirm Phase 1 output contains a severity-to-tier
   derivation table with at least one row per severity class present in the failure log.
   Confirm all Phase 3, 4, and 6 criteria carry Derivation annotations referencing Phase 1
   rows.

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
| BUILDER ASPIRATIONAL entry quotes MECHANISM DEFINER GATE verbatim | |
| PHASE-LOCALITY RULE: no competitor in any of the three prohibited zones | |
| TIER-BLIND CATEGORIZER: inline at category-count step, canonical format, one check governed | |
| ISOLATION AUDIT complete (all criteria flagged, no FAIL remaining) | |
| Category diversity: >= 3 distinct categories across full rubric | |
| Aspirational tier count: 1-2 criteria | |
| PARTIAL handling stated with score value and earn conditions | |
| Phase 1 severity-to-tier derivation table present (one row per logged failure mode) | |
| All Phase 3 and 4 criteria carry Derivation annotation referencing Phase 1 rows | |

---

## V-03 -- Inertia Framing (C-38 Maximum Probe)

**Axis:** Inertia framing -- triple-mechanism C-38 probe. Three simultaneous structural
elements target C-38, none of which have been combined in any prior round:

(1) STATUS QUO COMPETITOR opening block is extended to 8 failure items. The 8th item
explicitly names class-recognition application note absence as a foil failure: "Fails to
include a class-recognition application note -- outputs are scored criterion-by-criterion
without first identifying whether the rubric belongs to the inertia class."

(2) CLASS RECOGNITION APPLICATION NOTE is included in EMIT with the full inertia-pattern
definition and structural-equivalence basis (same depth as R19 V-05).

(3) DEFINER OUTPUT GATE scope-closure note includes an explicit structural-equivalence basis
grounded in class-recognition terms: the note explains why gate satisfaction and inertia
class membership are structurally linked, making C-51 explicit while connecting it to C-38.

All R18/R19 structural mechanisms preserved: C-49 (STATUS QUO COMPETITOR with 8 items);
DEFINER OUTPUT GATE predicate + exclusion terminal + embedded STOP (C-43, C-44); C-51
(structural-equivalence basis in gate, class-recognition grounded); MECHANISM DEFINER GATE
naming BUILDER ASPIRATIONAL (C-46); REFERENCE ANCHOR Consumer field (C-47) + anchor STOP
(C-45); BUILDER ASPIRATIONAL quotes both gates verbatim (C-41); PHASE-LOCALITY RULE (C-42);
TIER-BLIND CATEGORIZER canonical (C-39, C-48); composite formula + denominator + threshold +
PARTIAL (C-02).

Ablated: C-50 (no named-tier table in scoring section, to isolate C-38 triple-mechanism
signal); C-52 (no Phase 1 derivation table).

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain all three C-38 mechanisms: the opening foil's 8th failure item naming class-recognition note absence; the CLASS RECOGNITION APPLICATION NOTE in EMIT with inertia-pattern definition and FAIL declaration; the DEFINER OUTPUT GATE scope-closure note with structural-equivalence basis grounded in class-recognition terms; the primary falsification signal is a rubric that contains the foil item (item 8) and the gate structural-equivalence basis while omitting the EMIT note -- which would indicate that the foil and gate mechanisms compete with EMIT attention; the secondary falsification signal is a rubric that contains the EMIT note without the foil item, indicating the 8-item foil competes with the 7-item foil in terms of C-49 stability. | If V-03 passes C-38 after R1--R19 failures, the combination of all three mechanisms is sufficient; the next question is which mechanisms are necessary -- V-04 (no C-38) and V-05 (all three) provide the comparison points. If V-03 passes C-38 but C-38 fails in rounds that used only one or two mechanisms, the triple-mechanism combination is necessary (no single mechanism suffices). If V-03 still fails C-38, the mechanism count is not the limiting factor and the pass condition for C-38 may require a different structural approach. | C-49 stability is the primary secondary test: V-03 extends the foil from 7 to 8 items; if C-49 passes (foil names tier-diversity failure) under 8 items, the foil extension does not displace C-49's required item; if C-49 fails despite item 7 being present, the extension to 8 items competes for the scoring model's foil-coverage attention. |

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
- Fails to include a class-recognition application note -- outputs are scored
  criterion-by-criterion without first identifying whether the rubric belongs to the inertia
  class, making rubrics that satisfy all surface criteria while failing structural equivalence
  invisible to the scoring process.

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

**Scope note:** A rubric-building output satisfying this gate differs structurally from one
that fails it in terms of class identifiability at the scoring stage. The satisfying output
contains exactly two templates in slot-fillable form: a Text template with causal-direction
slots (Y, X, Z) and a Pass template with observability slots (LOCATION, OBSERVABLE,
STANDARD). The failing output lacks one or both templates, provides them in non-slot-fillable
form, or adds content beyond them. Criteria produced from a satisfying output show
causal-direction Text fields and location-anchored Pass conditions -- neither signal of the
inertia pattern. Criteria produced from a failing output show descriptive Text fields or
qualitative-only Pass conditions -- both signals of the inertia pattern. A scoring model
applying the CLASS RECOGNITION APPLICATION NOTE correctly classifies rubrics built from
satisfying outputs (not inertia class) and rubrics built from failing outputs (inertia class).
Gate satisfaction is the production-stage control that determines inertia-class membership at
the scoring stage. A rubric-satisfying instance and a rubric-failing instance are structurally
non-equivalent at this gate because the downstream class membership they produce is different.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied when:** Text template and Pass template are
both present in slot-fillable form, derived from the skill spec.

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

If introducing a competitor: place immediately before this criterion's definition.

Each criterion requires five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: Apply CRITERION DEFINER Text template.
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass**: Apply CRITERION DEFINER Pass template. No "is clear" or "adequately covers" as
  sole observable.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied when:** Text template and Pass template are
both present in slot-fillable form.

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

If introducing a competitor: place immediately before the criterion.

Each criterion: same five fields. **Dimension:** [degree | precision | specificity].

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

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

For each criterion from Phases 3 and 4, run the isolation audit. Read each field stripped
of surrounding context.

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

**Do not proceed to PHASE 5 until the DIVERGENCE CHECK is complete.**

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
the Falls-short field is blank, or if the Consumer field does not name ROLE: MECHANISM
DEFINER as the blocked consumer.

---

### PHASE 5.5 -- BUILDER ASPIRATIONAL PRECONDITION CHECK

Before ROLE: BUILDER ASPIRATIONAL begins, confirm:
1. DEFINER OUTPUT GATE satisfied (both templates present, no additional content).
2. MECHANISM DEFINER GATE satisfied (independence map complete, all rows "Yes").
3. REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE: MECHANISM DEFINER).

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
Mechanism        | Independence             | Affects criterion
[mechanism name] | Yes -- affects C-NN only | [TBD or criterion number]
```

Each row must be mutually exclusive. Removing any one mechanism leaves exactly one criterion
failing. No mechanism may carry dual responsibility for two gaps.

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

Place each competitor block immediately before the criterion it governs. PHASE-LOCALITY RULE
applies.

Each criterion: five fields (ID, Text slot-filled, Weight: aspirational, Category, Pass
slot-filled). Required annotation: **Gap closed:** [independence map mechanism row citation].

---

### ROLE: DUAL AUDITOR

Run two audit tracks sequentially.

**Audit Track 1 -- Criterion quality (all criteria):**

```
| C-NN | Text: D/C/CC | Pass: L/O/Q | Status |
```

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
   - PARTIAL handling: score value AND earn conditions
   - CLASS RECOGNITION APPLICATION NOTE: present, names inertia pattern as FAIL,
     structural-equivalence basis present

3. **Competitor coverage bijection**: For each novel aspirational criterion, confirm exactly
   one competitor block accompanies it.

4. **Anchor chain**: Confirm REFERENCE ANCHOR has Falls-short populated and Consumer field
   naming ROLE: MECHANISM DEFINER.

5. **Gate chain**: Confirm:
   - DEFINER OUTPUT GATE ends with exclusion terminal and embedded STOP
   - DEFINER OUTPUT GATE scope-closure note: structural-equivalence basis present and
     grounded in class-recognition terms
   - MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL as blocked consumer
   - BUILDER ASPIRATIONAL entry quotes both gate artifacts verbatim
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
- PARTIAL: score value and earn conditions

**CLASS RECOGNITION APPLICATION NOTE** (include in scoring section, before the composite
formula):

```
CLASS RECOGNITION APPLICATION NOTE:
Before scoring individual criteria, identify the output class of the rubric under evaluation.

INERTIA PATTERN: A rubric where (a) criteria Text fields describe what good output contains
  rather than what absence of the required property causes, (b) Pass conditions use only
  qualitative language ("is clear," "is complete," "adequately covers") without an artifact
  location or measurable token, or (c) weights (essential / recommended / aspirational) are
  assigned without evidence of a failure-mode analysis. Any one of these three signals
  identifies the inertia pattern.

STRUCTURAL EQUIVALENCE: A rubric that passes the inertia-pattern check (all three signals
  absent) but where two or more criteria test the same observable -- same artifact location,
  same token, same structural property, only paraphrased -- fails the structural-equivalence
  check. Structurally equivalent criteria are not independent: removing either leaves the
  rubric measuring the same thing. A rubric with N structurally equivalent criteria is
  functionally a rubric with N-1 criteria. The structural-equivalence check is not satisfied
  by confirming all criteria have different ID numbers or different Text phrasings -- it
  requires confirming that each criterion's Pass observable is not achievable by the same
  artifact property that satisfies any other criterion's Pass observable.

If the rubric belongs to the inertia class OR fails the structural-equivalence check:
  score = FAIL. Do not apply the composite formula. Do not partial-score individual criteria.

If the rubric passes both checks: apply the composite formula below.
```

**Emit manifest check** -- do not emit until all verified:

| Check | Status |
|-------|--------|
| DEFINER OUTPUT GATE satisfied (both templates, no additional content) | |
| DEFINER OUTPUT GATE scope-closure note: structural-equivalence basis present, grounded in class-recognition terms | |
| MECHANISM DEFINER GATE satisfied (independence map complete, all C-NN cited) | |
| REFERENCE ANCHOR Falls-short populated | |
| REFERENCE ANCHOR Consumer names ROLE: MECHANISM DEFINER | |
| MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL | |
| BUILDER ASPIRATIONAL entry quotes both gate artifacts verbatim | |
| PHASE-LOCALITY RULE: no competitor in any of the three prohibited zones | |
| TIER-BLIND CATEGORIZER: inline at category-count step, canonical format, one check governed | |
| STATUS QUO COMPETITOR failure list: names tier-diversity verification failure explicitly (item 7) | |
| STATUS QUO COMPETITOR failure list: names class-recognition note absence explicitly (item 8) | |
| CLASS RECOGNITION APPLICATION NOTE present: names inertia pattern as FAIL | |
| CLASS RECOGNITION APPLICATION NOTE: structural-equivalence basis present, closes PARTIAL bypass path | |
| ISOLATION AUDIT complete (all criteria flagged, no FAIL remaining) | |
| Category diversity: >= 3 distinct categories across full rubric | |
| Aspirational tier count: 1-2 criteria | |
| PARTIAL handling stated with score value and earn conditions | |

---

## V-04 -- Role Sequence + Output Format

**Axis:** Two-axis variation: (1) ROLE: CRITERION DEFINER runs twice -- an initial pass
(Phase 0.5) derives templates from the skill spec before any failure modes are known; a
review pass (Phase 2.5) refines templates using failure-mode evidence from Phase 1; the
DEFINER OUTPUT GATE uses the Phase 2.5 final templates, not the Phase 0.5 initial templates;
(2) the scoring section adds a GOLD/SILVER/BRONZE named-tier table supplementing the
composite formula (C-50 carry).

Phase 0.5 produces initial templates. Phase 1 produces the failure log. Phase 2.5 reviews
initial templates against failure evidence and may revise Z (downstream consequence) or X
(rejected form) but not Y (required property -- changing Y changes criterion meaning). The
DEFINER OUTPUT GATE is re-satisfied after Phase 2.5 using the refined templates.

All R18/R19 structural mechanisms preserved: STATUS QUO COMPETITOR opening block with
tier-diversity failure item (C-49); DEFINER OUTPUT GATE predicate + exclusion terminal +
embedded STOP (C-43, C-44); MECHANISM DEFINER GATE naming ROLE: BUILDER ASPIRATIONAL (C-46);
REFERENCE ANCHOR Consumer field (C-47) + anchor STOP (C-45); BUILDER ASPIRATIONAL quotes
both gates verbatim -- CRITERION DEFINER GATE quoted is the Phase 2.5 final output (C-41);
PHASE-LOCALITY RULE (C-42); TIER-BLIND CATEGORIZER canonical (C-39, C-48); composite formula
+ denominator + threshold + PARTIAL (C-02). C-50 carry: GOLD/SILVER/BRONZE tier table
supplementing composite formula.

Ablated: C-38 (no CLASS RECOGNITION APPLICATION NOTE, to isolate role-sequence + C-50
joint signal); C-51 (no structural-equivalence basis in DEFINER OUTPUT GATE scope-closure
note); C-52 (no Phase 1 derivation table).

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will show two CRITERION DEFINER passes: Phase 0.5 producing initial templates from spec-only evidence, and Phase 2.5 producing refined templates after seeing failure modes; the primary falsification signal is a rubric where Phase 2.5 revises Y (the required property) rather than only X or Z -- changing Y would indicate the model does not respect the Y-revision prohibition and treats the second pass as a wholesale template rewrite rather than a targeted refinement. | The GOLD/SILVER/BRONZE tier table supplementing the composite formula tests C-50 stability under the role-sequence change: R19 V-02 confirmed C-50 under a format-only axis; V-04 R20 tests whether C-50 holds when the sequence change is introduced simultaneously; the secondary falsification signal is a rubric where the tier table replaces the composite formula (failing C-02) rather than supplementing it. C-41 is the secondary structural test: BUILDER ASPIRATIONAL must quote the CRITERION DEFINER GATE verbatim; under V-04, the gate was satisfied twice (Phase 0.5 and Phase 2.5); the model must quote the Phase 2.5 final templates, not the Phase 0.5 initial templates. | C-41 (Builder Aspirational quotes gate verbatim) is the primary structural risk: in prior rounds C-41 tests whether the Builder quotes the single CRITERION DEFINER GATE; under V-04, the gate was satisfied twice and the Builder must identify the correct (Phase 2.5) version; if the Builder quotes Phase 0.5 templates, C-41 may fail; if it quotes Phase 2.5, C-41 passes. C-02 (denominator present) is the secondary risk: the tier table must supplement not replace the formula. |

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
before reading Phase 0.5. State your derivation, then proceed.**

---

### PHASE 0.5 -- CRITERION DEFINER INITIAL

**This phase runs before Phase 1. It produces initial templates from the skill spec alone,
without failure-mode evidence. Do not write any criterion fields during this phase.**

Generate skill-specific templates from the skill spec.

**Text template (slot-fillable):**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y = [skill-specific required property derived from the spec]
  Z = [downstream failure consequence of Y's absence]
  X = [rejected form -- wrong implementation with same surface behavior as Y]
```

**Pass template (slot-fillable):**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

These are initial templates. They will be reviewed and may be refined in Phase 2.5 after
the failure log is complete. Do not use these templates directly for criterion drafting --
wait for Phase 2.5 final templates.

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Read the skill spec. For every way an output of this skill can fail, record:

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. **Do not begin PHASE 2.5 until the
failure log contains at least 5 entries.**

---

### PHASE 2.5 -- CRITERION DEFINER REVIEW

**This phase runs after Phase 1. It reviews the initial templates from Phase 0.5 against
failure-mode evidence. Do not write any criterion fields during this phase.**

Read the initial templates from Phase 0.5 and the failure log from Phase 1.

For each template, assess whether the failure-mode evidence reveals:
- A more specific downstream consequence Z (revise Z if yes).
- A more specific rejected form X (revise X if yes).
- A change to the required property Y (do NOT revise Y -- if Y needs changing, draft a new
  template and note: "New template: Y revised, previous template retired").

Produce final templates incorporating any revisions. If no revisions are needed, carry
Phase 0.5 templates forward unchanged and note: "No revisions -- Phase 0.5 templates final."

Causal direction rule: "Without Y, Z fails" is the required form. The prohibited form -- in
any phrasing -- is any Text that locates causality in the wrong form's consequence.

**DEFINER OUTPUT GATE is satisfied when:** Final Text template and final Pass template are
both present in slot-fillable form, with Phase 2.5 revision notes where applicable, and no
criterion fields. Nothing else. STOP if this role's output contains anything beyond the
final templates and revision notes -- rewrite before proceeding to Phase 3.

ROLES: PHASE 3 and PHASE 4 cannot begin until DEFINER OUTPUT GATE is satisfied using the
Phase 2.5 final templates.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied when:** Phase 2.5 final Text template and
Pass template are both present in slot-fillable form.

Draft from blocking failure modes. Apply the Phase 2.5 final templates to each criterion.

If introducing a competitor: place immediately before this criterion's definition.

Each criterion requires five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: Apply Phase 2.5 final Text template.
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass**: Apply Phase 2.5 final Pass template. No "is clear" or "adequately covers" as
  sole observable.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied.**

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity.

Each criterion: same five fields. **Dimension:** [degree | precision | specificity].

---

### PHASE-LOCALITY RULE

The following placement zones are prohibited for all competitor blocks:

1. **Preamble zone**: any block appearing before any construction phase (Phases 3, 4, 6).
2. **Shared-operating-principles zone**: any block preceding more than one construction step.
3. **Multi-criterion zone**: any combined block governing more than one criterion.

A competitor is correctly placed if and only if it does not appear in any of the three
enumerated prohibited zones. This rule is a required Emit manifest verification target.

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

For each criterion from Phases 3 and 4, run the isolation audit.

**Text field checks (3):**
1. **Direction**: does Text locate causality in Y's absence?
2. **Contrast**: does Text name the rejected form X alongside Y?
3. **Causal chain**: does Text name the downstream consequence Z?

**Pass field checks (3):**
4. **Location**: does Pass name an artifact location, field, or section?
5. **Observable**: does Pass name a specific count, token, or structural property?
6. **No qualitative-only**: does Pass avoid bare qualitative language without an anchor?

**Audit report format:**

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

STOP if any criterion fails one or more flags. Revise before DIVERGENCE CHECK.

#### DIVERGENCE CHECK

Count category assignments per tier. For each tier, identify the majority category.

```
Essential tier:     [category] x[N] ... -- majority: [category]
Recommended tier:   [category] x[N] ... -- majority: [category]
Aspirational tier:  [category] x[N]     -- majority: [category]
```

STOP if fewer than 2 of 3 tiers have distinct majority categories.

---

### PHASE 5 -- REFERENCE ANCHOR

Identify a specific competitor or prior-version rubric that passes essential and recommended
criteria. Record where it falls short.

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

### PHASE 5.5 -- BUILDER ASPIRATIONAL PRECONDITION CHECK

Before ROLE: BUILDER ASPIRATIONAL begins, confirm:
1. DEFINER OUTPUT GATE satisfied (Phase 2.5 final templates present, no additional content).
2. MECHANISM DEFINER GATE satisfied (independence map complete, all rows "Yes").
3. REFERENCE ANCHOR complete (Falls-short populated; Consumer names ROLE: MECHANISM DEFINER).

STOP if any prerequisite is unsatisfied.

---

### ROLE: MECHANISM DEFINER

**PREREQUISITE:** REFERENCE ANCHOR is complete (Falls-short populated; Consumer field names
ROLE: MECHANISM DEFINER as the blocked consumer).

Produce an independence map for anticipated aspirational gaps.

```
Mechanism        | Independence             | Affects criterion
[mechanism name] | Yes -- affects C-NN only | [TBD or C-NN]
```

Each row mutually exclusive. No mechanism carries dual responsibility.

**MECHANISM DEFINER GATE is satisfied when:** Map complete, all rows "Yes -- affects C-NN
only." Nothing else. STOP beyond independence map.

ROLE: BUILDER ASPIRATIONAL cannot begin until this gate is satisfied.

---

### ROLE: BUILDER ASPIRATIONAL

**Input required:**

- **CRITERION DEFINER GATE** (Phase 2.5 final templates): Text template and Pass template
  in slot-fillable form.
- **MECHANISM DEFINER GATE**: Independence Map with all C-NN citations populated.

**ROLE: BUILDER ASPIRATIONAL cannot begin unless both gate artifacts exist.**

Quote both gate artifacts verbatim at entry to this role before drafting any criterion.

Draft 1-2 aspirational criteria from the Falls-short dimension. STOP if more than 2.

If introducing a competitor:

> **[COMPETITOR NAME]** -- [description of wrong implementation]. From the description above,
> derive the required implementation before reading the positive definition below.

Place each competitor block immediately before the criterion it governs. PHASE-LOCALITY RULE
applies.

Each criterion: five fields (ID, Text slot-filled from Phase 2.5 templates, Weight:
aspirational, Category, Pass slot-filled). **Gap closed:** [independence map row].

---

### ROLE: DUAL AUDITOR

**Audit Track 1:** `| C-NN | Text: D/C/CC | Pass: L/O/Q | Status |`

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

1. **Category distribution per tier:**
   ```
   Essential:    [category] x[N] -- majority: [category]
   Recommended:  [category] x[N] -- majority: [category]
   Aspirational: [category] x[N] -- majority: [category]
   ```
   STOP if < 2 tiers have distinct majority categories.

2. **Scoring section**: Confirm all present:
   - Composite formula
   - Denominator (/NN)
   - Golden threshold (numeric)
   - PARTIAL handling: score value AND earn conditions
   - GOLD/SILVER/BRONZE named-tier table supplementing (not replacing) the composite formula

3. **Competitor coverage bijection.**

4. **Anchor chain:** Falls-short + Consumer (ROLE: MECHANISM DEFINER).

5. **Gate chain:** Confirm:
   - DEFINER OUTPUT GATE (Phase 2.5 final templates) ends with exclusion terminal and
     embedded STOP
   - MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL
   - BUILDER ASPIRATIONAL entry quotes Phase 2.5 CRITERION DEFINER GATE verbatim
   - BUILDER ASPIRATIONAL entry quotes MECHANISM DEFINER GATE verbatim
   - PHASE-LOCALITY RULE: no competitor in any of the three prohibited zones
   - TIER-BLIND CATEGORIZER: inline at category-count step, canonical format, one check

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

**Named-tier table (supplementing the composite formula -- do not replace the formula):**

```
GOLD:   All essential criteria pass AND all recommended criteria pass AND all aspirational
        criteria pass (or PARTIAL >= 0.5 each). Composite score >= [N].
SILVER: All essential criteria pass AND at least [N/2 rounded up] recommended criteria pass
        AND at least 1 aspirational criterion passes. Composite score >= [M].
BRONZE: All essential criteria pass. Recommended and aspirational may be partial or absent.
PARTIAL = 0.5: criterion is present but Pass condition is met only in part (e.g., location
  named but observable absent; observable present but standard not met). PARTIAL counts as
  0.5 toward both composite score and tier threshold counts.
```

**Emit manifest check** -- do not emit until all verified:

| Check | Status |
|-------|--------|
| Phase 0.5 initial templates produced before Phase 1 | |
| Phase 2.5 review pass complete; revision notes present (or "no revisions" noted) | |
| DEFINER OUTPUT GATE satisfied using Phase 2.5 final templates (no additional content) | |
| MECHANISM DEFINER GATE satisfied (independence map complete, all C-NN cited) | |
| REFERENCE ANCHOR Falls-short populated | |
| REFERENCE ANCHOR Consumer names ROLE: MECHANISM DEFINER | |
| MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL | |
| BUILDER ASPIRATIONAL entry quotes Phase 2.5 CRITERION DEFINER GATE verbatim | |
| BUILDER ASPIRATIONAL entry quotes MECHANISM DEFINER GATE verbatim | |
| PHASE-LOCALITY RULE: no competitor in any of the three prohibited zones | |
| TIER-BLIND CATEGORIZER: inline at category-count step, canonical format, one check governed | |
| ISOLATION AUDIT complete (all criteria flagged, no FAIL remaining) | |
| Category diversity: >= 3 distinct categories across full rubric | |
| Aspirational tier count: 1-2 criteria | |
| PARTIAL handling stated with score value and earn conditions | |
| GOLD/SILVER/BRONZE named-tier table present; composite formula also present (tier table supplementary) | |

---

## V-05 -- Full Stack R20

**Axis:** All axes -- R19 V-05 full stack plus two R20 additions: (1) Phase 1
severity-to-tier derivation table (C-52 probe); (2) STATUS QUO COMPETITOR extended to 9
foil items (item 9 names severity-taxonomy gap). All R19 V-05 mechanisms preserved unchanged:
STATUS QUO COMPETITOR with tier-diversity failure (item 7) and class-recognition note absence
(item 8); DEFINER OUTPUT GATE with predicate + exclusion terminal + embedded STOP (C-43,
C-44) + structural-equivalence basis grounded in class-recognition terms (C-51); MECHANISM
DEFINER GATE naming BUILDER ASPIRATIONAL (C-46); REFERENCE ANCHOR Consumer field (C-47) +
anchor STOP (C-45); BUILDER ASPIRATIONAL quotes both gates verbatim (C-41); PHASE-LOCALITY
RULE (C-42); TIER-BLIND CATEGORIZER canonical (C-39, C-48); CLASS RECOGNITION APPLICATION
NOTE with structural-equivalence basis in EMIT (C-38); GOLD/SILVER/BRONZE named-tier table
supplementing composite formula in EMIT (C-50); composite formula + denominator + threshold +
PARTIAL (C-02).

**Ceiling attempt under v19:** If V-05 R20 passes C-38, C-50, C-51, and C-52 alongside all
carried criteria (C-01--C-51 minus C-38 persistent fail), composite = 43/43 x 10 = 10.0,
composite 100. V-05 R19 passed 42/43 (C-38 alone failed). V-05 R20 adds C-52 probe to the
Phase 1 section; if C-52 is confirmed and C-38 finally passes, the new ceiling is 44/44 x 10
(C-52 would become v20 C-52 after round scoring).

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain all fourteen structural elements: 9-item STATUS QUO COMPETITOR foil (C-49 + class-recognition item + severity-taxonomy item); Phase 1 severity-to-tier derivation table (C-52); DEFINER OUTPUT GATE structural-equivalence basis grounded in class-recognition terms (C-51); CLASS RECOGNITION APPLICATION NOTE with structural-equivalence basis in EMIT (C-38); GOLD/SILVER/BRONZE tier table supplementing composite formula (C-50); all carried gate/anchor/role mechanisms (C-39--C-48, C-41--C-47); the primary falsification signal is a rubric that satisfies 13 of 14 elements while failing C-38 for the 20th consecutive round, which would confirm that C-38 requires a structural approach not yet attempted and close this round's probe. | The 9-item foil extends V-03 R20's 8-item foil by one item (severity-taxonomy gap absence). If V-05 passes C-49 under 9 items while V-03 passes C-49 under 8 items, the foil extension to 9 items does not displace C-49's required item. If V-05 fails C-49 while V-03 passes it, the 9th item competes with item 7 for scoring-model coverage. | C-38 is the primary test for this round as it has been for all prior rounds. V-05 R20 deploys the identical C-38 triple-mechanism from V-03 R20 plus Phase 1 derivation table framing the failure-mode log. If V-05 passes C-38 and V-03 fails it, the Phase 1 taxonomy addition is what enables C-38 satisfaction. If both V-03 and V-05 fail C-38, triple-mechanism + taxonomy is still insufficient and the R20 ablation design leaves C-52 as the confirmed new criterion (V-02 scorecard) with C-38 unresolved for R21. |

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
- Fails to include a class-recognition application note -- outputs are scored
  criterion-by-criterion without first identifying whether the rubric belongs to the inertia
  class, making rubrics that satisfy all surface criteria while failing structural equivalence
  invisible to the scoring process.
- Fails to derive criterion weight from failure severity -- failure modes are logged with
  blocking/suboptimal/cosmetic labels, but those labels do not drive weight assignment;
  essential / recommended / aspirational weights are assigned by editorial judgment rather
  than derived from the severity taxonomy, making weight assignment unverifiable.

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

**After logging all failure modes, produce a SEVERITY-TO-TIER DERIVATION TABLE:**

```
| F-NN | Severity    | Target tier  | Rationale                                      |
|------|-------------|--------------|------------------------------------------------|
| F-01 | blocking    | essential    | [why absence blocks core function]             |
| F-02 | suboptimal  | recommended  | [why absence degrades quality, not function]   |
| F-03 | cosmetic    | aspirational | [why absence reduces excellence, not quality]  |
| F-04 | cosmetic    | no criterion | [why this failure does not warrant a criterion]|
```

Rules for the derivation table:
- Every logged failure mode must appear as a row.
- Blocking -> essential; suboptimal -> recommended; cosmetic -> aspirational or no criterion.
- Consolidate failures sharing the same structural gap into one row; note: "consolidated
  with F-NN."

**Do not begin ROLE: CRITERION DEFINER until the derivation table is complete.**

When drafting criteria in Phases 3, 4, and 6, reference the derivation table for weight
assignment. Each criterion must carry a **Derivation:** annotation citing the Phase 1 row(s)
that justify its weight.

---

### ROLE: CRITERION DEFINER

**This role runs after Phase 1 (failure log + derivation table complete). Do not write any
criterion fields during this role.**

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

**Scope note:** A rubric-building output satisfying this gate differs structurally from one
that fails it in terms of class identifiability at the scoring stage. The satisfying output
contains exactly two templates in slot-fillable form: a Text template with causal-direction
slots (Y, X, Z) and a Pass template with observability slots (LOCATION, OBSERVABLE,
STANDARD). The failing output lacks one or both templates, provides them in non-slot-fillable
form, or adds content beyond them. Criteria produced from a satisfying output show
causal-direction Text fields and location-anchored Pass conditions -- neither signal of the
inertia pattern. Criteria produced from a failing output show descriptive Text fields or
qualitative-only Pass conditions -- both signals of the inertia pattern. A scoring model
applying the CLASS RECOGNITION APPLICATION NOTE correctly classifies rubrics built from
satisfying outputs (not inertia class) and rubrics built from failing outputs (inertia class).
Gate satisfaction is the production-stage control that determines inertia-class membership at
the scoring stage. A rubric-satisfying instance and a rubric-failing instance are structurally
non-equivalent at this gate because the downstream class membership they produce is different.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied when:** Text template and Pass template are
both present in slot-fillable form, derived from the skill spec. Derivation table complete.

Draft from blocking failure modes. Apply the Text template and Pass template from ROLE:
CRITERION DEFINER to each criterion.

If introducing a competitor:

> **[COMPETITOR NAME]** -- [description of the wrong implementation: what it does, what
> surface form it has, why it fails to close the criterion gap]. This competitor IS the gap
> specification -- from the description above, derive the required implementation before
> reading the positive definition below.

Place the competitor block immediately before this criterion's definition. Do not group
competitors in a shared preamble.

Each criterion requires five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: Apply CRITERION DEFINER Text template.
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass**: Apply CRITERION DEFINER Pass template. No "is clear" or "adequately covers" as
  sole observable.
- **Derivation:** [F-NN row(s) from Phase 1 derivation table]

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

**PREREQUISITE: DEFINER OUTPUT GATE is satisfied when:** Text template and Pass template are
both present in slot-fillable form.

Draft from suboptimal failure modes. Apply Text template and Pass template. Pass conditions
test degree, precision, or specificity -- not whether an element exists.

If introducing a competitor: place immediately before the criterion, ending with a derivation
instruction.

Each criterion: same five fields as Phase 3. Required annotations:
**Dimension:** [degree | precision | specificity].
**Derivation:** [F-NN row(s) from Phase 1 derivation table].

After drafting recommended criteria: review the independence map from ROLE: MECHANISM
DEFINER. If any recommended criterion opens a new aspirational gap not covered by an existing
map row, add a new row now.

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

### PHASE 4.5 -- POST-DRAFT AUDIT

For each criterion from Phases 3 and 4, run the isolation audit. Read each field stripped
of surrounding context.

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
the Falls-short field is blank, or if the Consumer field does not name ROLE: MECHANISM
DEFINER as the blocked consumer.

---

### PHASE 5.5 -- BUILDER ASPIRATIONAL PRECONDITION CHECK

Before ROLE: BUILDER ASPIRATIONAL begins, confirm:
1. DEFINER OUTPUT GATE satisfied (both templates present, no additional content).
2. MECHANISM DEFINER GATE satisfied (independence map complete, all rows "Yes").
3. REFERENCE ANCHOR complete (Falls-short populated; Consumer field names
   ROLE: MECHANISM DEFINER).

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

Quote both gate artifacts verbatim at entry to this role before drafting any criterion.

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

Required annotations:
**Gap closed:** [independence map mechanism row citation, format: "Yes -- affects C-NN only"].
**Derivation:** [F-NN row(s) from Phase 1 derivation table, if applicable].

---

### ROLE: DUAL AUDITOR

Run two audit tracks sequentially.

**Audit Track 1 -- Criterion quality (all criteria):**

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
   - CLASS RECOGNITION APPLICATION NOTE: present, names inertia pattern as FAIL,
     structural-equivalence basis present (closing the PARTIAL bypass path)
   - GOLD/SILVER/BRONZE named-tier table: present and supplementing (not replacing) the
     composite formula

3. **Competitor coverage bijection**: For each novel aspirational criterion, confirm exactly
   one competitor block accompanies it. Count novel criteria. Count competitor blocks.
   Confirm counts match.

4. **Anchor chain**: Confirm REFERENCE ANCHOR has:
   - Falls-short field populated
   - Consumer field naming ROLE: MECHANISM DEFINER

5. **Gate chain**: Confirm:
   - DEFINER OUTPUT GATE ends with exclusion terminal and embedded STOP
   - DEFINER OUTPUT GATE scope-closure note: structural-equivalence basis present, grounded
     in class-recognition terms (not merely a restatement of the gate predicate)
   - MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL as blocked consumer
   - BUILDER ASPIRATIONAL entry quotes CRITERION DEFINER GATE verbatim
   - BUILDER ASPIRATIONAL entry quotes MECHANISM DEFINER GATE verbatim
   - PHASE-LOCALITY RULE: no competitor in any of the three prohibited zones
   - TIER-BLIND CATEGORIZER competitor: placed inline before category-distribution count
     step; ends with derivation instruction; governs exactly one audit check

6. **Phase 1 derivation table**: Confirm Phase 1 output contains a severity-to-tier
   derivation table with at least one row per severity class present in the failure log.
   Confirm all Phase 3, 4, and aspirational criteria carry Derivation annotations.

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

**CLASS RECOGNITION APPLICATION NOTE** (include in scoring section, before the composite
formula):

```
CLASS RECOGNITION APPLICATION NOTE:
Before scoring individual criteria, identify the output class of the rubric under evaluation.

INERTIA PATTERN: A rubric where (a) criteria Text fields describe what good output contains
  rather than what absence of the required property causes, (b) Pass conditions use only
  qualitative language ("is clear," "is complete," "adequately covers") without an artifact
  location or measurable token, or (c) weights (essential / recommended / aspirational) are
  assigned without evidence of a failure-mode analysis. Any one of these three signals
  identifies the inertia pattern.

STRUCTURAL EQUIVALENCE: A rubric that passes the inertia-pattern check (all three signals
  absent) but where two or more criteria test the same observable -- same artifact location,
  same token, same structural property, only paraphrased -- fails the structural-equivalence
  check. Structurally equivalent criteria are not independent: removing either leaves the
  rubric measuring the same thing. A rubric with N structurally equivalent criteria is
  functionally a rubric with N-1 criteria. The structural-equivalence check is not satisfied
  by confirming all criteria have different ID numbers or different Text phrasings -- it
  requires confirming that each criterion's Pass observable is not achievable by the same
  artifact property that satisfies any other criterion's Pass observable.

If the rubric belongs to the inertia class OR fails the structural-equivalence check:
  score = FAIL. Do not apply the composite formula. Do not partial-score individual criteria.

If the rubric passes both checks: apply the composite formula below.
```

**Named-tier table (supplementing the composite formula -- do not replace the formula):**

```
GOLD:   All essential criteria pass AND all recommended criteria pass AND all aspirational
        criteria pass (or PARTIAL >= 0.5 each). Composite score >= [N].
SILVER: All essential criteria pass AND at least [N/2 rounded up] recommended criteria pass
        AND at least 1 aspirational criterion passes. Composite score >= [M].
BRONZE: All essential criteria pass. Recommended and aspirational may be partial or absent.
PARTIAL = 0.5: criterion is present but Pass condition is met only in part (e.g., location
  named but observable absent; observable present but standard not met). PARTIAL counts as
  0.5 toward both composite score and tier threshold counts.
```

**Emit manifest check** -- do not emit until all verified:

| Check | Status |
|-------|--------|
| DEFINER OUTPUT GATE satisfied (both templates, no additional content) | |
| DEFINER OUTPUT GATE scope-closure note: structural-equivalence basis present, grounded in class-recognition terms | |
| MECHANISM DEFINER GATE satisfied (independence map complete, all C-NN cited) | |
| REFERENCE ANCHOR Falls-short populated | |
| REFERENCE ANCHOR Consumer names ROLE: MECHANISM DEFINER | |
| MECHANISM DEFINER GATE names ROLE: BUILDER ASPIRATIONAL | |
| BUILDER ASPIRATIONAL entry quotes CRITERION DEFINER GATE verbatim | |
| BUILDER ASPIRATIONAL entry quotes MECHANISM DEFINER GATE verbatim | |
| PHASE-LOCALITY RULE: no competitor in any of the three prohibited zones | |
| TIER-BLIND CATEGORIZER: inline at category-count step, canonical format with derivation instruction, governs exactly one check | |
| STATUS QUO COMPETITOR failure list: names tier-diversity verification failure explicitly (item 7) | |
| STATUS QUO COMPETITOR failure list: names class-recognition note absence explicitly (item 8) | |
| STATUS QUO COMPETITOR failure list: names severity-taxonomy weight-derivation gap explicitly (item 9) | |
| CLASS RECOGNITION APPLICATION NOTE: present, names inertia pattern as FAIL | |
| CLASS RECOGNITION APPLICATION NOTE: structural-equivalence basis present, closes PARTIAL bypass path | |
| GOLD/SILVER/BRONZE named-tier table present; composite formula also present (tier table supplementary) | |
| Phase 1 severity-to-tier derivation table present (one row per logged failure mode) | |
| All Phase 3, 4, and aspirational criteria carry Derivation annotation referencing Phase 1 rows | |
| ISOLATION AUDIT complete (all criteria flagged, no FAIL remaining) | |
| Category diversity: >= 3 distinct categories across full rubric | |
| Aspirational tier count: 1-2 criteria | |
| PARTIAL handling stated with score value and earn conditions | |
