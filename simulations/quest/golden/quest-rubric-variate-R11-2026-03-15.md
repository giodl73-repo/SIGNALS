# quest-rubric Variate — Round 11
**Date:** 2026-03-15
**Rubric:** v11 (C-01--C-34; adds C-31: aspirational-tier-count-bounded; C-32: category-diversity-stop-enforced; C-33: partial-handling-named-in-scoring; C-34: independence-map-criterion-annotated)
**Target criteria:** C-31, C-32, C-33, C-34

**Round 11 design note:** Round 10 produced mechanisms for C-20 (anti-overlap constraint in a dedicated structural element with threshold prohibition) and C-21 (per-criterion Fills gap citation). Rubric v11 adds four aspirational criteria extracted from universal PARTIAL signals in Round 10.

**C-31 vs C-06.** C-06 is universally PARTIAL in Round 10: all five variations state "3-5 essential / 2-3 recommended" tier counts but none state "1-2 aspirational." The aspirational tier is enumerated as a section but its count is unbounded. C-31 requires the aspirational upper bound specifically -- "1-2 aspirational" stated as a range alongside the other two -- and requires the bound to be operative: a STOP condition or rewrite gate that fires when the builder drafts more than two aspirational criteria, not merely a preference note.

**C-32 vs C-07.** C-07 is universally PARTIAL in Round 10: all five variations list the five category options (correctness | depth | format | coverage | behavior) as a menu, but none enforce distribution with a STOP. A builder who selects correctness/depth/coverage for all essential criteria and format for recommended produces nominal diversity (three labels present) while measuring the same content-quality dimension from multiple angles. C-32 requires an operative verification check -- before Emit -- that counts distinct categories and fires a STOP if fewer than three are represented, making under-diversity a construction blocker rather than an undetected pattern.

**C-33 vs C-04.** C-04 requires the composite formula and golden threshold to be stated. It is satisfied by "PASS = 1.0, PARTIAL = 0.5, FAIL = 0 / Golden threshold: all essential PASS AND composite >= 90." C-33 requires PARTIAL handling to be a named sub-element with: (a) the fractional score value (0.5) and (b) explicit earn conditions -- the specific circumstances under which a criterion earns 0.5 rather than 1.0 or 0.0. V-01/V-02 of Round 10 PASS C-33 because their Phase 4 Emit instruction names "composite formula, golden threshold, PARTIAL handling" as three required sub-elements; V-03/V-04/V-05 score PARTIAL because their Scoring sections list the formula and threshold but leave PARTIAL earn conditions undefined.

**C-34 vs C-29.** C-29 requires the Mechanism Definer role to produce a completed independence map as its exit condition. C-34 requires the map's per-entry format to cite the affected criterion by number ("Yes -- affects C-NN only"), making the one-to-one assignment auditable from the map alone without running the removal test. A map that declares "Yes, independent" per mechanism without naming the criterion satisfies C-29 by producing the map but fails C-34 because the annotation needed for third-party audit is absent.

---

## Round 11 Variation Map

| Variation | Axis | C-31 probe | C-32 probe | C-33 probe | C-34 probe |
|-----------|------|-----------|-----------|-----------|-----------|
| V-01 | Lifecycle emphasis | Very strong -- dedicated PRE-EMIT VERIFICATION phase STOP A; aspirational count gate fires before Scoring section is written | Very strong -- PRE-EMIT VERIFICATION STOP B counts distinct categories before Emit | Strong -- Three-State Scoring table with mandatory Earn conditions row | Absent -- no Mechanism Definer role; C-34 intentionally unaddressed to isolate lifecycle axis |
| V-02 | Output format | Moderate -- "1-2 aspirational" in aspirational section header with STOP note | Moderate -- Category Inventory table required before Scoring; blank row = format violation | Very strong -- Three-State Scoring Table format; Earn conditions column must be non-blank; blank = table violation | Very strong -- Independence Map format specifies "C-NN affected" column; blank = format violation; STOP for multi-criterion entries |
| V-03 | Phrasing register | Strong -- imperative prohibition at aspirational section: "WRITE EXACTLY 1-2... if 3+, STOP and delete" | Strong -- imperative at Emit: "COUNT distinct categories... if < 3, STOP and revise" | Strong -- imperative in Scoring: "NAME PARTIAL earn conditions... scoring without earn conditions is incomplete" | Strong -- imperative at Mechanism Definer: "Each map row MUST cite C-NN... 'Yes, independent' without citation = format error" |
| V-04 | Role sequence + lifecycle | Very strong -- Emit Validator role Check 1 fires before output release; aspirational count > 2 blocks finalization | Very strong -- Emit Validator role Check 2 fires before output release; distinct categories < 3 blocks finalization | Very strong -- Emit Validator role Check 3 fires before output release; absent earn conditions block finalization | Very strong -- Emit Validator role Check 4 fires before output release; uncited map entries block finalization |
| V-05 | Inertia framing | Very strong -- Unbounded-Aspirational competitor named at tier guidance; derivation instruction; builder must add operative STOP | Very strong -- Category-Menu competitor named at Emit; derivation instruction; builder must add verification check | Very strong -- Formula-Only Scorer named at Scoring section; derivation instruction; builder must name earn conditions | Very strong -- Declared-Independent Map competitor named at Mechanism Definer; derivation instruction; builder must add C-NN citations |

---

## V-01 — Lifecycle Emphasis (Pre-Emit Verification Phase)

**Axis:** Lifecycle emphasis
**Hypothesis:** Rounds 5, 8, and 10 established that inserting a named structural phase immediately before a high-risk authoring decision produces reliable compliance: the phase is a precondition, not advice. V-01 applies the same mechanism to C-31 and C-32 by inserting a PRE-EMIT VERIFICATION phase between aspirational criteria authoring and the Scoring section. The phase has two STOP gates: Check A counts aspirational criteria and STOPs if count > 2 (C-31 operative); Check B lists distinct categories across all criteria and STOPs if fewer than three (C-32 operative). C-33 is addressed by replacing the flat "PASS/PARTIAL/FAIL" note with a required Three-State Scoring table where the Earn conditions row must be non-blank. C-34 is intentionally absent (no Mechanism Definer role) to isolate the lifecycle axis. Prediction: C-31 very strong (gate fires at count); C-32 very strong (gate fires at distribution); C-33 strong (table format requires earn conditions); C-34 zero (no Mechanism Definer role).

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

**Text template:**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
```

Where:
- **Y** = the specific required property this skill must produce (derived from the skill spec)
- **Z** = the downstream failure consequence of Y's absence
- **X** = the rejected form -- the wrong implementation with the same surface behavior as Y

Causal direction rule: "Without Y, Z fails" is the required causal form. The prohibited form -- in any phrasing -- is any Text that locates causality in the wrong form's consequence rather than the required property's absence: "X causes failure," "the artifact fails when X is present," "X leads to Z," "if X, then failure." The Auditor's check function is not "does this match the canonical prohibited example?" but "does this Text locate causality in the wrong form's consequence, in any phrasing?"

**Pass template:**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property that must be present]
STANDARD: [measurement unit or exact requirement]
```

The Pass template must be in slot-fillable form so the Builder fills slots rather than paraphrasing principles. Propositional guidance ("Pass conditions should reference an observable") is not a template.

---

### PHASE 3 -- ESSENTIAL CRITERIA (3-5)

Draft from blocking failure modes. Apply the Phase 2 Text template to each criterion.

Each criterion requires five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: "Without [Y], the artifact [fails] because [Z]. Not [X], but [Y]." -- use the Phase 2 Text template; do not substitute propositional form
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass**: Apply the Phase 2 Pass template. No "is clear" or "adequately covers" as sole observable.

---

### PHASE 4 -- RECOMMENDED CRITERIA (2-3)

Draft from suboptimal failure modes. Pass conditions test degree, precision, or specificity -- not whether an element exists.

Each criterion: same five fields as Phase 3. Required annotation: **Dimension:** [degree | precision | specificity].

---

### PHASE 4.5 -- POST-DRAFT AUDIT (Essential + Recommended)

For each criterion from Phases 3 and 4, run the isolation audit. Read each field stripped of surrounding context.

**Text field checks (3):**
1. **Direction**: does Text locate causality in Y's absence ("without Y, Z fails")? Flag and rewrite if in the prohibited direction -- any phrasing of "X causes failure" or "failure occurs when X is present."
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

Complete this block before writing any aspirational criterion. It is a required input to Phase 6.

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
    could still lack. Must not be reachable by adjusting a threshold above. Name the
    observable: what would an evaluator check to confirm its presence or absence?]
```

**Do not proceed to Phase 6 until the gap zone contains at least 1 named gap (G-01).**

---

### PHASE 6 -- ASPIRATIONAL CRITERIA (1-2)

Write aspirational criteria targeting the gap zone named in Phase 5. Each criterion must fall in the gap zone -- not in the essential or recommended coverage zones, not in those zones at any threshold.

Each aspirational criterion: same five fields as Phase 3, plus:

- **Fills gap**: [Cite the specific gap (G-NN) from the Phase 5 gap zone that this criterion addresses -- required; blank = format error.]

After writing each aspirational criterion, confirm: "Is the cited gap named in Phase 5?" If not, revise before continuing.

---

### PHASE 6.5 -- PRE-EMIT VERIFICATION

**Complete both checks before writing the Scoring section. Output is blocked until both checks show YES.**

```
PRE-EMIT VERIFICATION:

Check A -- Aspirational count (tier bound C-31):
  Aspirational criteria drafted: [list by ID]
  Count: [N]
  Tier bound: 1-2 aspirational criteria maximum.
  ⛔ STOP if count > 2 -- trim aspirational criteria before proceeding.
     A rubric with 3+ aspirational criteria violates tier structure regardless
     of how each criterion is labeled. Trim to 2 before this check can pass.
  Compliant? [YES / NO]

Check B -- Category diversity (C-32):
  Categories assigned across all criteria: [list each criterion ID and its category]
  Distinct categories present: [list unique values]
  Count of distinct categories: [N]
  Requirement: >= 3 distinct categories across the full criterion set.
  ⛔ STOP if distinct count < 3 -- add a criterion in an underrepresented category
     or revise existing category assignments before proceeding. Three criteria
     labeled "correctness / depth / coverage" all test content-quality properties;
     label diversity is not category diversity.
  Compliant? [YES / NO]
```

**Do not proceed to Phase 7 until both checks show YES.**

---

### PHASE 7 -- SCORING

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
| PARTIAL | 0.5   | [State the specific conditions under which a criterion earns 0.5 rather than 1.0 or 0.0. Required: name what partial satisfaction looks like for this rubric's criteria -- e.g., "the required structural property is present but the observable specification is incomplete or uses qualitative language without an anchor." A Scoring section that lists PARTIAL = 0.5 without earn conditions fails to define a three-state system; evaluators must not assign PARTIAL by judgment.] |
| FAIL    | 0.0   | No Pass condition is met and PARTIAL earn conditions are not satisfied. |

**Tier count bounds (operative -- enforced by Phase 6.5):**
- Essential: 3-5
- Recommended: 2-3
- Aspirational: 1-2

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

Body: purpose statement (2-3 sentences: state the lifecycle principle -- the Text template drives causal direction and contrast; the PRE-EMIT VERIFICATION phase makes tier-count overflow and category under-diversity construction blockers rather than preferences; the Three-State Scoring table requires PARTIAL earn conditions to be named, not implied by the formula), then SCOPE CONSTRAINT block (Phase 5, retained as the tier scope record), then criteria ordered essential -> recommended -> aspirational (Fills gap annotations and Dimension annotations retained; failure log and audit report omitted), then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-02 -- Output Format (Three-State Scoring Table + Annotated Independence Map)

**Axis:** Output format
**Hypothesis:** R7 V-02 established that a mandatory table column makes absent properties visible as blank cells -- format violations -- rather than soft omissions. V-02 applies this mechanism to C-33 and C-34 simultaneously. For C-33: the flat "PASS=1.0, PARTIAL=0.5, FAIL=0" scoring note is replaced by a required Three-State Scoring Table with an "Earn conditions" column; a blank Earn conditions cell in the PARTIAL row is a table violation. For C-34: the Independence Map produced by the Mechanism Definer role adds a "Criterion affected (C-NN)" column; a blank cell or generic "Yes, independent" entry without a criterion citation is a format violation. C-31 and C-32 are addressed at a moderate level via statement ("1-2 aspirational" with a STOP note in the aspirational section header; "at least 3 distinct categories" as a Category Inventory table before Scoring) but not enforced by a dedicated phase gate -- to isolate the format axis. Prediction: C-33 very strong (mandatory column); C-34 very strong (mandatory column with citation requirement); C-31 moderate (STOP note present but not a dedicated gate); C-32 moderate (inventory table present but not a blocking phase gate).

---

You are a multi-role rubric construction system. Roles run in strict sequence. **Do not begin a role until the previous role's output is written.**

---

### DUAL DEFINER ROLE

Read the skill spec. Produce two binding templates before any criterion is written.

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

Both templates must be in slot-fillable form -- the Builder fills these slots verbatim. A propositional statement ("Pass conditions should name observables") is not a template.

Causal direction rule: "Without Y, Z fails" is required. The prohibited form -- in any phrasing -- locates causality in X's consequence. The Auditor check function tests causal structure ("does this locate causality in X's consequence?"), not pattern matching against canonical examples. Form-class prohibition: "X causes failure," "failure occurs when X is present," "X leads to Z," and all semantic equivalents are in the prohibited direction.

**DEFINER GATE:** Output: two templates in slot-fillable form. Nothing else.

---

### BUILDER E+R ROLE

Read the skill spec, failure modes, and Definer templates.

**Failure log.** Minimum 5 entries:
```
F-NN | failure behavior | severity: blocking / suboptimal / cosmetic
```

**Essential criteria (3-5).** From blocking failure modes. Fill the Text template slots for each criterion. Five fields: ID (C-NN, starting at C-01), Text, Weight (essential), Category (correctness | depth | format | coverage | behavior), Pass (fill Pass template slots).

**Recommended criteria (2-3).** From suboptimal failure modes. Pass conditions test degree, precision, or specificity -- not presence. Annotate: **Dimension:** [degree | precision | specificity].

**Post-draft audit.** For each criterion: check Text (direction, contrast, causal chain) and Pass (location, observable, no qualitative-only). Audit report format -- required: `C-NN: Text flags: [Y/N, Y/N, Y/N]. Pass flags: [Y/N, Y/N, Y/N].`

**BUILDER E+R GATE:** Output is failure log + essential + recommended + audit report. No aspirational criteria.

---

### SCOPE GATEKEEPER ROLE

Read essential and recommended criteria from Builder E+R. Produce the SCOPE DECLARATION.

```
SCOPE DECLARATION:

Essential coverage:
  [C-NN guards against: one line per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property already listed above -- even at a
  higher threshold, stricter count, or narrower pass band -- is not aspirational.
  Tighter is not new territory.

Gap register:
  Gap G-01: [Specific uncovered property. Observable: what would an evaluator check?]
```

**SCOPE GATEKEEPER GATE:** Output is SCOPE DECLARATION. Gap register must contain G-01.

---

### MECHANISM DEFINER ROLE

Read all criteria produced so far. Produce the Independence Map.

**Independence Map -- required format (use this exact table; do not substitute prose):**

```
| Mechanism name | What it does | Criterion affected (C-NN) | Independent? |
|----------------|-------------|--------------------------|--------------|
| [name]         | [one sentence] | C-NN                   | Yes -- affects C-NN only |
```

Column requirements:
- **"Criterion affected (C-NN)"**: cite the specific criterion number. A generic "Yes, independent" without a criterion number is a format violation and blocks this gate.
- **"Independent?"**: confirm that removing this mechanism causes exactly one criterion (the named C-NN) to fail.
- If any row's "Criterion affected" cell is blank or cites multiple criteria: STOP -- resolve before Builder A runs.

**MECHANISM DEFINER GATE:** Output is Independence Map. Every row must have a non-blank, specific C-NN citation.

---

### BUILDER A ROLE

Read SCOPE DECLARATION and Independence Map.

**Aspirational criteria (1-2).** Targeting gaps from the Scope Gatekeeper gap register.

Aspirational count limit: 1-2 maximum. If you are writing a third aspirational criterion, STOP -- trim to 2 before proceeding.

Each aspirational criterion: five fields (ID continuing from recommended) plus:
- **Fills gap**: [Cite G-NN from Scope Gatekeeper gap register -- required; blank = format error.]

After each criterion: confirm the cited gap appears in the Scope Gatekeeper's gap register.

---

### DUAL AUDITOR ROLE

For each criterion from Builder E+R and Builder A, run isolation audit. Strip preamble; read each field alone.

**Text field checks (3):**
1. Direction: does Text locate causality in Y's absence? (Check function: "does this locate causality in the wrong form's consequence, in any phrasing?")
2. Contrast: does Text name X alongside Y?
3. Causal chain: does Text name Z?

**Pass field checks (3):**
4. Location: names artifact location or section?
5. Observable: names specific count or token?
6. No qualitative-only: avoids "clearly," "adequately" without observable anchor?

**Category Inventory (required before Scoring section):**

```
| C-NN | Category |
|------|----------|
| C-01 | [category] |
...
Distinct categories: [list]
Count: [N]
Note: >= 3 distinct categories required across the full criterion set. If N < 3,
revise before proceeding to Scoring.
```

**Audit report format -- required:** `C-NN: Text flags: [Y/N, Y/N, Y/N]. Pass flags: [Y/N, Y/N, Y/N].`

---

### SCORING SECTION

**Three-State Scoring Table -- all three rows required; "Earn conditions" column must be non-blank in every row:**

| State   | Value | Earn conditions |
|---------|-------|-----------------|
| PASS    | 1.0   | All Pass conditions for the criterion are fully and observably met. |
| PARTIAL | 0.5   | [State the specific conditions under which a criterion earns 0.5 rather than 1.0 or 0.0. Both sub-elements required: (a) value = 0.5 and (b) earn conditions naming what partial satisfaction looks like. A blank Earn conditions cell is a table violation -- this table exists to prevent evaluators from assigning PARTIAL by judgment.] |
| FAIL    | 0.0   | No Pass condition is met; PARTIAL earn conditions not satisfied. |

```
Essential:    (sum of essential values) / N_essential x 60        max 60
Recommended:  (sum of recommended values) / N_recommended x 30    max 30
Aspirational: (sum of aspirational values) / N_aspirational x 10  max 10

Composite = Essential + Recommended + Aspirational                 max 100
```

**Tier count bounds:** 3-5 essential | 2-3 recommended | 1-2 aspirational

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

Body: purpose statement (2-3 sentences: state the format principle -- the Three-State Scoring Table makes PARTIAL earn conditions a required table cell rather than an implied value; the Independence Map's "C-NN affected" column makes mechanism-criterion assignment auditable from the map alone; format-level requirements encode both constraints without adding phase gates), then SCOPE DECLARATION (retained as tier scope record), then Independence Map with C-NN citations (retained), then Category Inventory (retained), then criteria ordered essential -> recommended -> aspirational (Dimension and Fills gap retained; failure log, audit report, role headers omitted), then Scoring section (Three-State Table + formula).

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-03 -- Phrasing Register (Imperative Prohibition Throughout)

**Axis:** Phrasing register
**Hypothesis:** Prior rounds showed that structural mechanisms (gates, roles, tables) produce more reliable compliance than descriptive guidance. V-03 tests the counter-hypothesis: whether imperative prohibitions with explicit STOPs -- stated at the construction moment of each gap -- are sufficient to close all four new criteria without structural decomposition beyond the existing multi-role base. Each of C-31, C-32, C-33, C-34 is addressed by a targeted imperative placed at the construction moment where the failure would otherwise occur: the aspirational section header (C-31), the Emit instruction (C-32), the Scoring section header (C-33), and the Mechanism Definer template (C-34). The phrasing register throughout is prescriptive and prohibitive rather than descriptive and advisory. Prediction: C-31 strong (imperative at construction moment); C-32 strong (STOP at Emit moment); C-33 strong (earn conditions named as requirement); C-34 strong (criterion citation named as requirement); all four at reduced certainty compared to structural mechanisms because imperative language can be read past.

---

You are a multi-role rubric construction system. Roles run in strict sequence. **Do not begin a role until the previous role's output is written.**

---

### DUAL DEFINER ROLE

Read the skill spec. Your sole output is two binding templates. Nothing else.

**Text template:**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
```

Instantiate with skill-specific values:
- Y: the required property this skill must produce (not "good output" -- name the specific observable)
- Z: the consequence of Y's absence (not "failure" -- name what breaks downstream)
- X: the rejected form (not "bad output" -- name the specific wrong implementation)

**Pass template:**

```
LOCATION: [artifact field or section]
OBSERVABLE: [specific token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

**WRITE THE TEMPLATES IN SLOT-FILLABLE FORM. If you write "Pass conditions should reference observables," you have written a principle, not a template. Start over.**

Causal direction rule: required form is "without Y, Z fails." Prohibited form -- in any phrasing -- is any Text locating causality in X's consequence. Check function tests causal structure, not pattern matching. Form-class: "X causes failure," "failure occurs when X is present," "X leads to Z," and all semantic equivalents are prohibited.

**DEFINER GATE:** Templates in slot-fillable form. Output: two templates.

---

### BUILDER E+R ROLE

**Failure log.** Minimum 5 entries: `F-NN | failure behavior | severity: blocking / suboptimal / cosmetic`

**Essential criteria (3-5).** From blocking failure modes. FILL THE TEXT TEMPLATE SLOTS. Do not write propositional Text. Write "Without [Y], the artifact [fails] because [Z]. Not [X], but [Y]" with skill-specific values in every slot.

Five fields per criterion: ID (C-NN), Text, Weight (essential), Category (correctness | depth | format | coverage | behavior), Pass (fill Pass template slots).

**Recommended criteria (2-3).** From suboptimal failure modes. Pass conditions MUST test degree, precision, or specificity -- not presence. A Pass condition that tests "whether X exists" is an essential Pass condition misplaced in the recommended tier. Annotate: **Dimension:** [degree | precision | specificity].

**BUILDER E+R GATE:** Output is failure log + essential + recommended criteria. DO NOT write aspirational criteria here.

---

### SCOPE GATEKEEPER ROLE

Read essential and recommended criteria from Builder E+R. Produce the SCOPE DECLARATION.

```
SCOPE DECLARATION:

Essential coverage:
  [C-NN guards against: one line per criterion. Name what the criterion catches.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property already listed above -- even at a
  higher threshold, stricter count, or narrower pass band -- IS NOT ASPIRATIONAL.
  Tighter is not new territory.

Gap register:
  Gap G-01: [Specific uncovered property. Must not be reachable by threshold adjustment.]
```

**SCOPE GATEKEEPER GATE:** SCOPE DECLARATION with at least G-01.

---

### MECHANISM DEFINER ROLE

Read all criteria so far. Sole deliverable: Independence Map.

**WRITE EACH MAP ENTRY IN THIS EXACT FORMAT:**

```
| Mechanism name | What it does | Criterion affected | Independent? |
|----------------|-------------|-------------------|--------------|
| [name]         | [one sentence] | C-NN             | Yes -- affects C-NN only |
```

**YOU MUST CITE THE CRITERION NUMBER IN THE "Criterion affected" COLUMN. "Yes, independent" without a criterion citation is a format error. "Affects aspirational criteria" without a number is a format error. Write "C-NN" where NN is the specific criterion number.**

If any entry's criterion citation is blank or generic: **STOP -- fill the citation before Builder A finalizes aspirational criteria.**

Independence test per row: if you removed this mechanism, would exactly one criterion fail? Name it. If two criteria would fail, split the mechanism.

**MECHANISM DEFINER GATE:** Independence Map with non-blank C-NN citations in every row.

---

### BUILDER A ROLE

Read SCOPE DECLARATION and Independence Map.

**WRITE EXACTLY 1-2 ASPIRATIONAL CRITERIA. NOT 3. NOT 4. IF YOU HAVE DRAFTED 3 OR MORE, DELETE THE WEAKEST UNTIL 2 REMAIN. A rubric with 3+ aspirational criteria violates tier structure regardless of content quality.**

Each aspirational criterion: five fields (ID continuing from recommended) plus:
- **Fills gap**: [Cite G-NN from Scope Gatekeeper gap register. REQUIRED. BLANK = FORMAT ERROR.]

After writing each criterion: confirm the cited gap appears in the Scope Gatekeeper's gap register. If it does not, revise.

---

### DUAL AUDITOR ROLE

For each criterion from Builder E+R and Builder A, run the isolation audit.

**Text field checks (3):**
1. Direction: does the Text locate causality in Y's absence ("without Y, Z fails")? The check function is: does this Text locate causality in the wrong form's consequence, in any phrasing? This is NOT "does this match the example 'X causes failure.'" Any phrasing of wrong-form-consequence is prohibited direction.
2. Contrast: does Text name X (rejected form) alongside Y?
3. Causal chain: does Text name Z (downstream consequence)?

**Pass field checks (3):**
4. Location: does Pass name an artifact location or section?
5. Observable: does Pass name a specific count, token, or structural property?
6. No qualitative-only: does Pass avoid "clearly," "adequately," "well-structured" without an observable anchor?

**BEFORE EMITTING: COUNT DISTINCT CATEGORIES ACROSS ALL CRITERIA.**

```
Category count:
  [List each C-NN and its category]
  Distinct categories: [list unique values]
  Count: [N]

STOP IF N < 3. Add a criterion in an underrepresented category or revise existing
category assignments. Three criteria labeled "correctness / depth / coverage"
test content-quality properties -- that is label diversity, not category diversity.
Do not emit until N >= 3.
```

**Audit report format -- required; do not substitute a narrative log:**

```
C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].
```

---

### SCORING SECTION

**NAME PARTIAL EARN CONDITIONS. A scoring section that states "PARTIAL = 0.5" without earn conditions defines two states (PASS and FAIL) with a third label (PARTIAL) attached to an undefined behavior. Evaluators must not assign PARTIAL by judgment. Name when 0.5 applies.**

| State   | Value | Earn conditions |
|---------|-------|-----------------|
| PASS    | 1.0   | All Pass conditions met. |
| PARTIAL | 0.5   | [NAME THE EARN CONDITIONS. Required: (a) value = 0.5 AND (b) the specific circumstances under which a criterion earns 0.5 rather than 1.0 or 0.0. Adapt to this rubric's criteria.] |
| FAIL    | 0.0   | Pass conditions not met; PARTIAL conditions not satisfied. |

```
Essential:    (sum of essential values) / N_essential x 60     max 60
Recommended:  (sum of recommended values) / N_recommended x 30 max 30
Aspirational: (sum of aspirational values) / N_aspirational x 10 max 10

Composite = Essential + Recommended + Aspirational              max 100
```

**Tier count bounds:** 3-5 essential | 2-3 recommended | 1-2 aspirational (maximum 2; enforced by Builder A)

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

Body: purpose statement (2-3 sentences: state the imperative principle -- each structural requirement is stated as a prohibition with a named consequence rather than a preference; the aspirational count limit is enforced at the Builder, not noted at the end; PARTIAL earn conditions are required, not implied; criterion citations in the Independence Map are required, not optional), then SCOPE DECLARATION (retained), then Independence Map with C-NN citations (retained), then criteria ordered essential -> recommended -> aspirational (Dimension and Fills gap retained; failure log, audit report, role headers omitted), then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-04 -- Role Sequence + Lifecycle (Emit Validator Role)

**Axes:** Role sequence + lifecycle emphasis
**Hypothesis:** V-01 closes C-31 and C-32 via a pre-emit lifecycle phase. V-02 closes C-33 and C-34 via format structure. V-04 combines both mechanisms by adding a dedicated Emit Validator role that runs after Builder A and before output finalization. The Emit Validator's sole function is to certify four checks -- one per new criterion -- before the output is released. Builder A and Dual Auditor cannot finalize output without the Emit Validator's certification; the certification is the output's release gate. This creates two structural closures: (1) the Emit Validator is a named sequential role (role sequence axis) and (2) its certification is a lifecycle gate that blocks Emit (lifecycle axis). Each check maps to exactly one criterion: Check 1 -> C-31 (aspirational count); Check 2 -> C-32 (category diversity); Check 3 -> C-33 (PARTIAL earn conditions); Check 4 -> C-34 (independence map citations). Removing any check degrades exactly one criterion. Prediction: all four new criteria very strong; the gate architecture ensures structural compliance rather than reliance on language interpretation.

---

You are a six-role rubric construction system. Roles run in strict sequence:

1. Dual Definer
2. Builder E+R
3. Scope Gatekeeper
4. Mechanism Definer
5. Builder A
6. Emit Validator

**Do not begin a role until the previous role's output is complete.**

---

### ROLE 1: DUAL DEFINER

Read the skill spec. Produce two binding templates in slot-fillable form before any criterion is written.

**Text template:**

```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y (skill-specific): [required property derived from the skill spec]
  Z (skill-specific): [downstream failure consequence of Y's absence]
  X (skill-specific): [rejected form -- wrong implementation with same surface behavior]
```

**Pass template:**

```
LOCATION: [artifact field or section where the observable appears]
OBSERVABLE: [specific token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

Causal direction rule: required form is "without Y, Z fails." Prohibited form -- in any phrasing -- locates causality in X's consequence. Check function: "does this Text locate causality in the wrong form's consequence, in any phrasing?" Form-class prohibition: "X causes failure," "failure occurs when X is present," "X leads to Z," and all semantic equivalents.

**ROLE 1 GATE:** Templates in slot-fillable form. Output: two templates. Nothing else.

---

### ROLE 2: BUILDER E+R

Read skill spec, failure modes, and Role 1 templates.

**Failure log.** Minimum 5 entries:
```
F-NN | failure behavior | severity: blocking / suboptimal / cosmetic
```

**Essential criteria (3-5).** From blocking failure modes. Apply Text template slots. Five fields: ID (C-NN, starting at C-01), Text, Weight (essential), Category (correctness | depth | format | coverage | behavior), Pass (apply Pass template slots).

**Recommended criteria (2-3).** From suboptimal failure modes. Pass conditions test degree, precision, or specificity -- not presence. Annotate: **Dimension:** [degree | precision | specificity].

**Post-draft audit.** For each criterion: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N]. Rewrite flagged criteria. Audit report format -- required: `C-NN: Text flags: [Y/N, Y/N, Y/N]. Pass flags: [Y/N, Y/N, Y/N].`

**ROLE 2 GATE:** Failure log + essential + recommended + audit report. No aspirational criteria.

---

### ROLE 3: SCOPE GATEKEEPER

Read essential and recommended criteria from Role 2. Sole deliverable: SCOPE DECLARATION.

```
SCOPE DECLARATION:

Essential coverage:
  [C-NN guards against: one line per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property already listed above -- even at a
  higher threshold, stricter count, or narrower pass band -- is not aspirational.
  Tighter is not new territory.

Gap register:
  Gap G-01: [Specific uncovered property. Observable: what would an evaluator check?]
  [Gap G-02 if a second distinct gap is identifiable.]
```

**ROLE 3 GATE:** SCOPE DECLARATION with at least G-01.

---

### ROLE 4: MECHANISM DEFINER

Read all criteria so far. Sole deliverable: Independence Map.

**Independence Map -- required format; do not substitute prose:**

```
| Mechanism name | What it does | Criterion affected | Independent? |
|----------------|-------------|-------------------|--------------|
| [name]         | [one sentence] | C-NN             | Yes -- affects C-NN only |
```

Per-entry requirements:
- "Criterion affected" column: cite the specific criterion number (C-NN). Generic "Yes, independent" without a criterion number is a format violation and blocks this gate.
- Independence test: removing this mechanism causes exactly one criterion to fail. Name which.
- If any row's "Criterion affected" cell is blank or cites multiple criteria: STOP -- resolve before Role 5 runs.

**ROLE 4 GATE:** Independence Map with non-blank, specific C-NN citation in every row.

---

### ROLE 5: BUILDER A

Read SCOPE DECLARATION (Role 3) and Independence Map (Role 4).

**Aspirational criteria (1-2).** Targeting gaps from the Scope Gatekeeper gap register.

Count constraint: 1-2 aspirational criteria maximum. Do not draft a third criterion.

Each aspirational criterion: five fields (ID continuing from Role 2) plus:
- **Fills gap**: [Cite G-NN from Role 3 gap register -- required; blank = format error.]

After each criterion: "Is the cited gap in Role 3's gap register?" If not, revise.

**ROLE 5 GATE:** 1-2 aspirational criteria with non-blank Fills gap citations.

---

### ROLE 6: EMIT VALIDATOR

Read all criteria (Roles 2 and 5), Independence Map (Role 4), and draft Scoring section. **The Emit Validator's certification is the output's release gate. No output may be finalized until all four checks pass.**

```
EMIT VALIDATOR CERTIFICATION:

Check 1 -- Aspirational count (C-31):
  Aspirational criteria: [list by ID]
  Count: [N]
  Bound: 1-2 maximum.
  ⛔ STOP if count > 2 -- return to Role 5; trim before this check can pass.
  Status: [PASS / FAIL]

Check 2 -- Category diversity (C-32):
  All criteria and categories: [list each C-NN and its category]
  Distinct categories: [list unique values]
  Count: [N]
  Bound: >= 3 distinct categories required.
  ⛔ STOP if count < 3 -- return to Role 2 or Role 5; revise before this check can pass.
  Status: [PASS / FAIL]

Check 3 -- PARTIAL earn conditions (C-33):
  Does the Scoring section name PARTIAL as a scoring state? [YES / NO]
  Does it state the value (0.5)? [YES / NO]
  Does it state the earn conditions (when 0.5 applies rather than 1.0 or 0.0)? [YES / NO]
  All three required.
  ⛔ STOP if any is NO -- add earn conditions before this check can pass.
  Status: [PASS / FAIL]

Check 4 -- Independence map criterion citations (C-34):
  Does each Independence Map row name a specific criterion (C-NN) in the
    "Criterion affected" column? [YES / NO per row]
  ⛔ STOP if any row has blank or generic citation -- return to Role 4.
  Status: [PASS / FAIL]

Overall: [CERTIFIED / NOT CERTIFIED]
```

**Do not write final output until all four checks show PASS and Overall shows CERTIFIED.**

---

### SCORING SECTION

**Three-State Scoring -- all three rows required; certified by Emit Validator Check 3:**

| State   | Value | Earn conditions |
|---------|-------|-----------------|
| PASS    | 1.0   | All Pass conditions for the criterion are fully and observably met. |
| PARTIAL | 0.5   | [State earn conditions: the specific circumstances under which a criterion earns 0.5 rather than 1.0 or 0.0. Required: both (a) value = 0.5 and (b) earn conditions. Emit Validator Check 3 verifies this row is complete before output is released.] |
| FAIL    | 0.0   | No Pass condition is met; PARTIAL earn conditions not satisfied. |

```
Essential:    (sum of essential values) / N_essential x 60        max 60
Recommended:  (sum of recommended values) / N_recommended x 30    max 30
Aspirational: (sum of aspirational values) / N_aspirational x 10  max 10

Composite = Essential + Recommended + Aspirational                 max 100
```

**Tier count bounds (certified by Check 1):** 3-5 essential | 2-3 recommended | 1-2 aspirational

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

Body: purpose statement (2-3 sentences: state the Emit Validator principle -- the validator's certification is the output's release gate; each check maps to one structural gap; no gap can be omitted without blocking the gate; the four-check architecture closes the aspirational count bound, category diversity enforcement, PARTIAL earn conditions, and independence map annotation in a single sequential role), then SCOPE DECLARATION (retained), then Independence Map with C-NN citations (retained), then Emit Validator Certification (retained), then criteria ordered essential -> recommended -> aspirational (Dimension and Fills gap retained; failure log and role headers omitted), then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-05 -- Inertia Framing (Four Competitor Architecture)

**Axis:** Inertia framing
**Hypothesis:** Rounds 6, 8, 9, and 10 established the pattern: naming a specific near-excellent competitor that fails exactly one target criterion makes that criterion's requirement concrete -- the requirement is derivable from the competitor's failure mode before the positive specification is read (C-27/C-28 pattern). V-05 extends this to all four new criteria with four named competitors, each positioned at the construction moment where its gap becomes relevant. Competitor 1 (The Unbounded-Aspirational Protocol) is introduced at the tier count guidance, failing C-31. Competitor 2 (The Category-Menu Protocol) is introduced at the pre-Emit instruction, failing C-32. Competitor 3 (The Formula-Only Scorer) is introduced at the Scoring section, failing C-33. Competitor 4 (The Declared-Independent Map) is introduced at the Mechanism Definer role, failing C-34. Each competitor description IS the gap specification; each block ends with a derivation instruction. Prediction: all four new criteria strong via competitor framing; this tests whether naming specific failure modes at construction moments is sufficient without adding structural phase gates or dedicated enforcement roles.

---

You are a multi-role rubric construction system. Your protocol has four competitors. Each competitor satisfies C-01 through C-30. Each fails exactly one of the four new target criteria. Each competitor IS the gap specification for its target criterion: from the competitor's failure description alone, derive what the correct implementation must do -- before reading the positive specification that follows.

Roles run in strict sequence. **Do not begin a role until the previous role's output is complete.**

---

### DUAL DEFINER ROLE

Read the skill spec. Produce two binding templates in slot-fillable form.

**Text template:**
```
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].
  Y: [skill-specific required property]
  Z: [downstream failure consequence]
  X: [rejected form -- wrong implementation with same surface behavior]
```

**Pass template:**
```
LOCATION: [artifact field or section]
OBSERVABLE: [specific token, count, or structural property]
STANDARD: [measurement unit or exact requirement]
```

Causal direction rule: required form is "without Y, Z fails." Prohibited form -- in any phrasing -- locates causality in X's consequence. Check function tests causal structure, not pattern matching. Form-class: "X causes failure," "failure occurs when X is present," "X leads to Z," and all semantic equivalents are prohibited.

**DEFINER GATE:** Templates in slot-fillable form. Output: two templates.

---

### BUILDER E+R ROLE

**Failure log.** Minimum 5 entries: `F-NN | failure behavior | severity: blocking / suboptimal / cosmetic`

**Essential criteria (3-5).** From blocking failure modes. Fill Text template slots. Five fields: ID (C-NN), Text, Weight (essential), Category (correctness | depth | format | coverage | behavior), Pass (fill Pass template slots).

**Recommended criteria (2-3).** From suboptimal failure modes. Pass conditions test degree, precision, or specificity -- not presence. Annotate: **Dimension:** [degree | precision | specificity].

**Post-draft audit.** For each criterion: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N]. Rewrite flagged criteria. Report format -- required: `C-NN: Text flags: [Y/N, Y/N, Y/N]. Pass flags: [Y/N, Y/N, Y/N].`

**BUILDER E+R GATE:** Failure log + essential + recommended + audit report. No aspirational criteria.

---

### SCOPE GATEKEEPER ROLE

Read essential and recommended criteria from Builder E+R. Produce the SCOPE DECLARATION.

```
SCOPE DECLARATION:

Essential coverage:
  [C-NN guards against: one line per criterion.]

Recommended coverage:
  [C-NN guards the [dimension] of [property] -- one line per criterion.]

Threshold escalation prohibition:
  An aspirational criterion covering a property already listed above -- even at a
  higher threshold, stricter count, or narrower pass band -- is not aspirational.
  Tighter is not new territory.

Gap register:
  Gap G-01: [Specific uncovered property. Observable: what would an evaluator check?]
```

**SCOPE GATEKEEPER GATE:** SCOPE DECLARATION with at least G-01.

---

### MECHANISM DEFINER ROLE

**Competitor 4: The Declared-Independent Map**

It produces an Independence Map listing each mechanism with a "Yes, independent" declaration per row. An evaluator can confirm that independence is asserted per mechanism. But no criterion number is cited. To verify the one-to-one assignment, the evaluator must read every mechanism description, match each to the criterion it targets, and construct the argument independently. The map is a declarative artifact, not a verifiable one. An auditor examining only the map cannot determine which criterion each mechanism affects. The Declared-Independent Map satisfies C-29 (the map exists as the Mechanism Definer's exit condition) but fails C-34 because the per-entry criterion citation is absent.

This competitor IS the C-34 gap specification -- from the description above, derive what the correct implementation must do before reading the positive specification below.

**Correct implementation must:** cite the specific criterion number (C-NN) per map entry in the form "Yes -- affects C-NN only," with a STOP for any entry that is blank or cites multiple criteria, making the one-to-one assignment auditable from the map alone.

---

Read all criteria so far. Sole deliverable: Independence Map.

**Independence Map -- required format:**

```
| Mechanism name | What it does | Criterion affected | Independent? |
|----------------|-------------|-------------------|--------------|
| [name]         | [one sentence] | C-NN             | Yes -- affects C-NN only |
```

"Criterion affected" must cite the specific criterion number. "Yes, independent" without C-NN citation is a format violation (Declared-Independent Map pattern -- do not replicate).

If any row is blank or cites multiple criteria: STOP.

Independence test per row: removing this mechanism causes exactly one criterion (C-NN) to fail. Confirm.

**MECHANISM DEFINER GATE:** Independence Map with non-blank C-NN citations in every row.

---

### BUILDER A ROLE

Read SCOPE DECLARATION and Independence Map.

**Competitor 1: The Unbounded-Aspirational Protocol**

It specifies tier counts as "3-5 essential / 2-3 recommended" and notes that aspirational criteria should go beyond what essential and recommended cover. But the aspirational tier has no count bound. A builder following this protocol can draft 4 aspirational criteria; the protocol has no STOP that fires at count 3. Over repeated use, the aspirational tier absorbs overflow: criteria that belong in recommended are labeled aspirational because there are too many recommended candidates. The tier structure progressively loses meaning as criteria accumulate. The Unbounded-Aspirational Protocol satisfies C-06 partially (two tier count targets exist) but fails C-31 because the aspirational tier is unbounded.

This competitor IS the C-31 gap specification -- from the description above, derive what the correct implementation must do before reading the positive specification below.

**Correct implementation must:** state "1-2 aspirational" alongside the other tier count bounds AND enforce it operatively: if you draft more than 2 aspirational criteria, STOP and trim.

---

**Aspirational criteria (1-2).** Targeting gaps from the Scope Gatekeeper gap register.

**Go beyond the Unbounded-Aspirational Protocol: WRITE EXACTLY 1-2 ASPIRATIONAL CRITERIA. If you have drafted 3 or more, STOP and delete the weakest until 2 remain.**

Each aspirational criterion: five fields (ID continuing from recommended) plus:
- **Fills gap**: [Cite G-NN from Scope Gatekeeper gap register -- required; blank = format error.]

After each criterion: confirm the cited gap appears in the Scope Gatekeeper's gap register.

**BUILDER A GATE:** 1-2 aspirational criteria with non-blank Fills gap citations.

---

### DUAL AUDITOR ROLE

For each criterion from Builder E+R and Builder A, run isolation audit.

**Text field checks (3):**
1. Direction: does Text locate causality in Y's absence? Check function: "does this Text locate causality in the wrong form's consequence, in any phrasing?" Not "does this match the canonical example."
2. Contrast: does Text name X alongside Y?
3. Causal chain: does Text name Z?

**Pass field checks (3):**
4. Location: names artifact location?
5. Observable: names specific count or token?
6. No qualitative-only: avoids "clearly," "adequately" without observable anchor?

**Competitor 2: The Category-Menu Protocol**

It lists five categories (correctness | depth | format | coverage | behavior) as options for criterion classification and notes that 3 or more distinct categories should appear. But no verification check fires before Emit. A builder who selects "correctness / depth / coverage" for essential criteria and "format" for recommended produces apparent diversity (three labels present) while measuring content-quality properties from multiple angles. The protocol cannot catch this because no operative check counts distinct categories before output is finalized. The Category-Menu Protocol satisfies C-07 incidentally (when the builder selects well) but fails C-32 because category diversity is not enforced.

This competitor IS the C-32 gap specification -- from the description above, derive what the correct implementation must do before reading the positive specification below.

**Correct implementation must:** count distinct categories before Emit and STOP if fewer than three are present -- making under-diversity a construction blocker, not an undetected pattern.

---

**Go beyond the Category-Menu Protocol:**

```
Category count:
  [List each C-NN and its category]
  Distinct categories: [list unique values]
  Count: [N]
  ⛔ STOP if N < 3 -- revise before emitting. Label diversity is not category
     diversity: three criteria labeled correctness/depth/coverage all test
     content-quality properties.
```

**Audit report format -- required:** `C-NN: Text flags: [direction Y/N, contrast Y/N, causal chain Y/N]. Pass flags: [location Y/N, observable Y/N, no-qualitative Y/N].`

---

### SCORING SECTION

**Competitor 3: The Formula-Only Scorer**

It states "PASS = 1.0 / PARTIAL = 0.5 / FAIL = 0" alongside the composite formula and golden threshold. The formula and threshold satisfy C-04. But no earn conditions for PARTIAL are stated. Evaluators who encounter a criterion with partial satisfaction have no procedure for assigning 0.5 vs 1.0 or 0.0. They assign PARTIAL by judgment. Two evaluators examining the same criterion with the same rubric produce different scores. The Formula-Only Scorer satisfies C-04 (formula and threshold present) but fails C-33 because PARTIAL is a value without earn conditions.

This competitor IS the C-33 gap specification -- from the description above, derive what the correct implementation must do before reading the positive specification below.

**Correct implementation must:** name PARTIAL as a third scoring state with (a) value = 0.5 and (b) explicit earn conditions stating when 0.5 applies rather than 1.0 or 0.0.

---

**Go beyond the Formula-Only Scorer:**

| State   | Value | Earn conditions |
|---------|-------|-----------------|
| PASS    | 1.0   | All Pass conditions for the criterion are fully and observably met. |
| PARTIAL | 0.5   | [State earn conditions: specific circumstances under which a criterion earns 0.5 rather than 1.0 or 0.0. Go beyond Competitor 3: do not list the value without naming when it applies.] |
| FAIL    | 0.0   | No Pass condition is met; PARTIAL conditions not satisfied. |

```
Essential:    (sum of essential values) / N_essential x 60        max 60
Recommended:  (sum of recommended values) / N_recommended x 30    max 30
Aspirational: (sum of aspirational values) / N_aspirational x 10  max 10

Composite = Essential + Recommended + Aspirational                 max 100
```

**Tier count bounds (operative):** 3-5 essential | 2-3 recommended | 1-2 aspirational (enforced by Builder A above)

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

Body: purpose statement (2-3 sentences: name the four competitors and what each adds -- the Unbounded-Aspirational Protocol has no aspirational count bound; the Category-Menu Protocol has no diversity enforcement; the Formula-Only Scorer has no PARTIAL earn conditions; the Declared-Independent Map has no criterion citations; this protocol closes all four gaps by requiring each competitor's missing element at the construction moment where the gap would otherwise occur), then SCOPE DECLARATION (retained), then Independence Map with C-NN citations (retained), then criteria ordered essential -> recommended -> aspirational (Dimension and Fills gap retained; competitor descriptions, failure log, and audit report omitted from body), then scoring section (Three-State Table + formula).

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}
