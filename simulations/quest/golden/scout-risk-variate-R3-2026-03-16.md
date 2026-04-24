---
skill: quest-variate
skill_target: scout-risk
round: 3
date: 2026-03-16
rubric: simulations/quest/rubrics/scout-risk-rubric-v3-2026-03-16.md
axes_explored: [lifecycle-emphasis (>=3 pairs), output-format (IF-THEN schema template), phrasing-register (structural obligation sub-fields), lifecycle+output-format, full-integration]
---

# scout-risk — Prompt Variations R3

Five complete, runnable skill body prompts. Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

**R3 context**: Round 2 produced five GOLDEN variations (V-05 at 99 under v2 rubric). The v3 rubric adds three new aspirational criteria — C-14 (IF-THEN syntactic form on every likelihood), C-15 (mitigation type declared with structural obligation), C-16 (interdependency section names ≥3 named pairs). Analysis of R2 V-05 under v3 rubric reveals C-14 and C-15 already pass (R2 V-05 had both mechanisms), but C-16 fails — R2 V-05 only required ≥2 pairs. R3 primary target: C-16. Each single-axis variation isolates one mechanism from R3's gap profile.

---

## V-01 — Axis: Lifecycle Emphasis (interdependency count upgrade to >=3)

**Hypothesis**: Changing the minimum from 2 to 3 in the Phase 3 interdependency section, and upgrading the smell-test from "if you find only 1" to "if you find fewer than 3 after reviewing all rows, your risks are not specific enough — revise Phase 2," creates backward pressure on the entire risk register. A register generic enough to yield only 2 pairings cannot satisfy the count; the model must produce more specific risks to generate the third. Built on R2 V-03's lifecycle-phase structure (proven path to C-09/C-13 PASS). Expected new criterion unlocked: C-16 (dedicated section, ≥3 named pairs). C-14 and C-15 remain at PARTIAL/FAIL baseline — this variation isolates C-16 alone.

---

```
Auto-detect the topic from repo context. Do not ask.

Build a risk register organized in three phases. Complete each phase before starting the next.

**Phase 1: Write the inertia risk (mandatory, first).**

The inertia risk is always the first entry. It is the risk that the status quo was good enough and this feature is the wrong thing to build. Do not skip it. Do not move it.

Give it:
- Severity: HIGH, MEDIUM, or LOW — nothing else
- Likelihood: name the specific condition that would make status quo win
- Mitigation: name what the team should do to test whether inertia applies before building

**Phase 2: Write the dimensional risks.**

List at least one risk each from 3 or more of these dimensions: Technical, Market, Compliance, Dependency, Timeline.

For each risk, provide:
- Name: a short label (5-10 words)
- Dimension: which of the five it belongs to
- Severity: HIGH, MEDIUM, or LOW — nothing else
- Likelihood: what specific condition or scenario triggers this risk — not just "possible"
- Mitigation: a concrete action — not "monitor the situation", not "be careful", not "consider alternatives"

Read back every mitigation. If two or more are generic non-actions, replace them.

Sort dimensional risks from highest to lowest severity.

**Phase 3: Write the Risk Interdependencies section (mandatory).**

After the risk register entries, write a section with this exact heading:

## Risk Interdependencies

This section must contain at least 3 named compound-risk pairings. Use this format for each:

> If [Risk A: name it explicitly] materializes, [Risk B: name it explicitly] escalates to [HIGH / MEDIUM / LOW] because [one-clause reason].

Enforcement rules:
- Do not scatter interdependencies as footnotes inside individual risk entries. They belong here only.
- At least 3 pairings are required. If you find fewer than 3 after reviewing all rows, your risks are not specific enough — go back to Phase 2 and make them more concrete before returning here.
- "If technical risks compound" is not a valid pairing — both risks must be named explicitly by title.
- A pairing must state a severity direction (escalates to HIGH, escalates to MEDIUM, etc.).

**Phase 4 (only if AMEND is in the prompt):**

AMEND: focus on [dimension] — keep inertia and the ## Risk Interdependencies section, drop all dimensional risks outside that dimension.
AMEND: adjust severity threshold to [level] — keep inertia and the ## Risk Interdependencies section, drop risks below that level.

**Write the artifact to:** simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-02 — Axis: Output Format (IF-THEN as embedded table schema template)

**Hypothesis**: Placing the IF-THEN structure directly in the column header of the likelihood table column — so the header reads `IF [condition], THEN risk activates` — makes the constraint a schema template the model fills in, rather than a rule the model follows. The model sees an incomplete template cell and completes it; it cannot produce "high" or "possible" where the header demonstrates the required form. This is syntactic completion rather than rule obedience. Built on R2 V-01's single-axis IF-THEN foundation. Expected: C-14 PASS via schema template rather than instruction. Compares to R2 V-01's rule-based enforcement to test which mechanism is structurally stronger.

---

```
Auto-detect the topic from repo context. Do not ask.

Build a risk register. Follow this sequence.

**Step 1: Write the inertia risk (mandatory, first).**

The inertia risk is always the first entry — the risk that the status quo was good enough and this feature is the wrong thing to build. Do not skip it. Do not move it.

Format:
- Dimension: Inertia
- Severity: HIGH, MEDIUM, or LOW — nothing else
- IF [specific condition that makes status quo win], THEN this risk activates.
- Mitigation: one concrete action to test whether inertia applies before building

**Step 2: Write the dimensional risks (table format).**

Cover at least 3 of: Technical, Market, Compliance, Dependency, Timeline.

Output as a markdown table with these column headers exactly:

| # | Dimension | Risk | Severity | IF [condition], THEN risk activates | Mitigation Type | Mitigation |
|---|-----------|------|----------|-------------------------------------|-----------------|------------|

Column definitions:
- #: row number starting at 1 (inertia is row 0, written separately above)
- Dimension: Technical / Market / Compliance / Dependency / Timeline
- Risk: a short label (5-10 words)
- Severity: HIGH / MEDIUM / LOW — no other values
- IF [condition], THEN risk activates: complete the template — every cell in this column starts with "IF" and ends with a concrete triggering scenario. Do not write "high", "possible", "~30%", or any bare label in this column.
- Mitigation Type: one of — Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation: one sentence naming exactly what to do

**Mitigation type definitions:**
- Spike: time-boxed experiment to reduce a named technical unknown
- Validate: user/stakeholder test that confirms or kills an assumption
- Gate: go/no-go checkpoint before the next phase
- Contract: formal agreement with a named party (SLA, API contract, compliance sign-off)
- Cut: remove the risky element from scope entirely
- Instrument: add observability producing a named metric (not passive monitoring)

**Forbidden mitigation words — replace before proceeding:**
"monitor closely", "keep an eye on", "revisit later", "consider alternatives", "be careful", "evaluate options".

Sort rows by severity descending.

**Step 3: Note at least one interdependency.**

After the table, note any risks that compound each other:
"If [Risk A] materializes, [Risk B] escalates to [severity]."

**Step 4 (only if AMEND is in the prompt):**

AMEND: focus on [dimension] — keep inertia (row 0), drop all other dimensions.
AMEND: adjust severity threshold to [level] — keep inertia (row 0), drop risks below that level.

**Write the artifact to:** simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-03 — Axis: Phrasing Register (mitigation type with structural obligation sub-fields)

**Hypothesis**: Requiring each mitigation to declare its type AND fulfill that type's structural contract — by naming the specific sub-field the type requires (Spike: named unknown + time-box; Gate: named criterion; Validate: named assumption + method; Contract: named party + commitment; Cut: named element + scope effect; Instrument: named metric + alert threshold) — raises C-15 from "type label present" to "type contract fulfilled." The sub-fields function as required named fields: a model cannot complete a Spike without naming the unknown and the time-box, making "monitor closely" incompatible with any type by structural necessity. Built on R2 V-02's taxonomy-focused foundation. Expected: C-15 PASS with structural obligation enforcement rather than definition-based prevention.

---

```
Auto-detect the topic from repo context. Do not ask.

Build a risk register. Follow this sequence.

**Step 1: Write the inertia risk (mandatory, first).**

The inertia risk is always the first entry — the risk that the status quo was good enough and this feature is the wrong thing to build. Do not skip it. Do not move it.

Give it:
- Severity: HIGH, MEDIUM, or LOW — nothing else
- Likelihood: name the specific condition that would make status quo win
- Mitigation type: one of — Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation (fulfill the type contract):
  - If Spike: Unknown: [what is being resolved] / Time-box: [duration]
  - If Validate: Assumption: [what is being tested] / Method: [interviews / prototype / survey]
  - If Gate: Criterion: [what must be true to pass]
  - If Contract: Party: [who] / Commitment: [what is owed]
  - If Cut: Element: [what is removed] / Scope effect: [impact on v1 delivery]
  - If Instrument: Metric: [name] / Alert threshold: [value or condition]

**Step 2: Write the dimensional risks.**

List at least one risk each from 3 or more of these dimensions: Technical, Market, Compliance, Dependency, Timeline.

For each risk, provide:
- Name: a short label (5-10 words)
- Dimension: which of the five it belongs to
- Severity: HIGH, MEDIUM, or LOW — nothing else
- Likelihood: what specific condition or scenario triggers this risk — not just "possible"
- Mitigation type: one of — Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation (fulfill the type contract using the sub-fields above for whichever type you selected)

**Type contract rules:**
Every mitigation must fulfill its type's contract. The sub-fields are required named outputs:
- Spike without a named unknown and time-box is incomplete.
- Gate without a named criterion is incomplete.
- Validate without a named assumption and method is incomplete.
- Contract without a named party and commitment is incomplete.
- Cut without a named element and scope effect is incomplete.
- Instrument without a named metric and alert threshold is incomplete.

Generic hedges ("monitor closely", "keep an eye on", "revisit later", "consider alternatives") are incompatible with all six types — no type contract can be fulfilled by a generic phrase.

Sort dimensional risks from highest to lowest severity.

**Step 3: Check your type contracts.**

Read back every mitigation. Verify each fulfills its type contract (named sub-fields filled in). Replace any that fail this check.

**Step 4: Note at least one interdependency.**

If any two risks compound each other:
"If [Risk A] materializes, [Risk B] escalates to [severity]."

**Step 5 (only if AMEND is in the prompt):**

AMEND: focus on [dimension] — keep inertia, drop all dimensional risks outside that dimension.
AMEND: adjust severity threshold to [level] — keep inertia, drop risks below that level.

**Write the artifact to:** simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-04 — Axes: Lifecycle Emphasis + Output Format (>=3 pairs + IF-THEN schema template)

**Hypothesis**: V-01's interdependency section upgrade (≥3 pairs with backward pressure on register specificity) and V-02's schema-embedded IF-THEN (column header as template) are orthogonal mechanisms — the first targets the interdependency phase, the second targets the likelihood field in the dimensional risk table. Combining them should produce C-14 PASS (via schema template) and C-16 PASS (via ≥3 pairs requirement) simultaneously. Built on R2 V-04's dual-axis foundation (IF-THEN + taxonomy), upgrading the interdependency requirement from "at least one mention" to "dedicated section with ≥3 named pairs." Expected: C-14 + C-16 PASS at ~103.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal artifacts). Do not prompt unless context is absent.

Build a risk register. Every risk entry must pass two non-negotiable quality gates before you proceed: the likelihood column must complete the IF-THEN template, and the mitigation must be typed from a named vocabulary.

**Step 1: Write the inertia risk (mandatory, first).**

The inertia risk is always the first entry — the risk that the status quo was good enough and this feature is the wrong thing to build. Do not skip it. Do not move it.

Format:
- Dimension: Inertia
- Severity: HIGH, MEDIUM, or LOW — nothing else
- IF [specific condition that makes status quo win], THEN this risk activates.
- Mitigation type: one of — Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation: one sentence naming exactly what to do

**Step 2: Write the dimensional risks (table format).**

Cover at least 3 of: Technical, Market, Compliance, Dependency, Timeline.

Output as a markdown table with these exact column headers:

| # | Dimension | Risk | Severity | IF [condition], THEN risk activates | Mitigation Type | Mitigation |
|---|-----------|------|----------|-------------------------------------|-----------------|------------|

Column rules:
- Severity: only HIGH, MEDIUM, or LOW — no numbers, percentages, or invented labels
- IF [condition], THEN risk activates: complete the template — every cell begins with "IF". A bare probability label ("high", "~30%", "possible") cannot satisfy the column header's template format.
- Mitigation Type: one of — Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation: one sentence naming exactly what to do

**Mitigation type definitions:**
- Spike: time-boxed experiment to reduce a named technical unknown
- Validate: user/stakeholder test that confirms or kills an assumption
- Gate: go/no-go checkpoint before the next phase
- Contract: formal agreement with a named party (SLA, API contract, compliance sign-off)
- Cut: remove the risky element from scope entirely
- Instrument: add observability producing a named metric (not passive monitoring)

**Forbidden mitigation words — replace on sight:**
"monitor closely", "keep an eye on", "revisit later", "consider alternatives", "be careful", "evaluate options". Selecting a type first eliminates these: a Spike has a question to answer; a Gate has a criterion to pass.

Sort rows by severity descending.

**Step 3: Write the Risk Interdependencies section (mandatory, >=3 pairs).**

After the table, write this section with the exact heading:

## Risk Interdependencies

This section must contain at least 3 named compound-risk pairings. Format each as:

- If [Risk A: name it by title] materializes, [Risk B: name it by title] escalates to [HIGH / MEDIUM / LOW] because [one-clause reason].

Enforcement rules:
- Do not embed interdependency notes inside table rows — this section is the only location.
- At least 3 named pairs are required. If you find fewer than 3 after reviewing all rows, your risks are not specific enough — revise Phase 2 to make them more concrete, then return here.
- Both risks must be named by their exact title from the table. "If technical risks compound other risks" fails the naming requirement.
- Each pairing must declare a severity direction.

**Step 4: Self-check.**

Before writing the artifact, verify each item:
- [ ] Inertia is row 0, before all Technical/Market/Compliance/Dependency/Timeline risks
- [ ] Every severity is only HIGH, MEDIUM, or LOW
- [ ] At least 3 dimensions covered
- [ ] Every likelihood cell in the table starts with "IF" — scan every row
- [ ] Every row has a named Mitigation Type from the approved list
- [ ] No forbidden mitigation words in any entry
- [ ] Rows sorted high-to-low after inertia
- [ ] ## Risk Interdependencies section exists with at least 3 explicitly named compound-risk pairs

Fix any violation before proceeding.

**Step 5 (only if AMEND is in the prompt):**

AMEND: focus on [dimension] — keep inertia (row 0) and ## Risk Interdependencies section, drop all rows not matching [dimension]. Re-sort.
AMEND: adjust severity threshold to [level] — keep inertia (row 0) and ## Risk Interdependencies section, drop rows below [level]. Re-sort.

**Write artifact to:** simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-05 — Full Integration (R2 V-05 base + >=3 pairs + structural type obligations + schema template)

**Hypothesis**: R2 V-05 already passes C-11, C-12, C-13, C-14, and C-15 under the v3 rubric — its mechanisms were the evidence basis for those criteria. The only v3 gap is C-16 (requires ≥3 pairs; R2 V-05 only enforced ≥2). This variation makes three targeted changes to R2 V-05: (1) upgrades STEP 3 interdependency count from ≥2 to ≥3 and updates the smell-test accordingly, (2) embeds the IF-THEN form in the table column header (structural template rather than rule), (3) expands the mitigation type definitions to include each type's structural sub-field obligation. The STEP 4 self-check is updated to verify ≥3 pairs. Expected score: 105/106 — C-10 PARTIAL is the ceiling on all base prompts.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal artifacts). Do not prompt unless context is absent.

Build a risk register. Follow these steps in order. Do not skip any step.

---

**STEP 1 — INERTIA RISK (mandatory, always first)**

Write the inertia risk before anything else. The inertia risk is: the risk that the status quo is good enough and this feature is the wrong thing to build.

Run the Skeptic lens: given what this topic does and who it is for, what does the team or user do instead? How sticky is that alternative? What does building this cost relative to the value it delivers?

Output the inertia risk in this exact format:

**0. Inertia — [one-line risk title]**
- Dimension: Inertia
- Severity: HIGH / MEDIUM / LOW
- IF [specific condition that makes inertia win], THEN this risk activates.
- Mitigation type: [Spike / Validate / Gate / Contract / Cut / Instrument]
- Mitigation (fulfill the type contract below): [1 sentence]

---

**STEP 2 — DIMENSIONAL RISKS (3 roles, table output)**

Run three analyst roles. Each contributes risks from their lens. Then merge all into a single table.

Roles:
- **Skeptic** (Market, Compliance): why will this fail to deliver value?
- **Realist** (Technical, Dependency): what will break during build?
- **Scheduler** (Timeline, cross-check Dependency): what will slip the date?

Cover at least 3 of the 5 dimensions: Technical, Market, Compliance, Dependency, Timeline.

Merge all role contributions into this table, sorted by severity descending after inertia:

| # | Dimension | Risk | Severity | IF [condition], THEN risk activates | Mitigation Type | Mitigation |
|---|-----------|------|----------|-------------------------------------|-----------------|------------|

**Likelihood rule — column header is the template:** Every cell in the `IF [condition], THEN risk activates` column must complete the template — start with "IF", name the triggering scenario, end with a concrete consequence. Bare probability labels ("high", "~30%", "possible", "likely when") cannot satisfy a column that begins with "IF". If you draft a cell without "IF", rewrite it before adding the row.

**Mitigation type rule:** Every mitigation must carry a named type. Select the type first, then write the mitigation sentence by fulfilling the type's structural contract:
- Spike: Unknown: [what is being resolved] / Time-box: [duration] — then one action sentence
- Validate: Assumption: [what is being tested] / Method: [interviews/prototype/survey] — then one action sentence
- Gate: Criterion: [what must be true to pass] — then one action sentence
- Contract: Party: [who] / Commitment: [what is owed] — then one action sentence
- Cut: Element: [what is removed] / Scope effect: [impact on delivery] — then one action sentence
- Instrument: Metric: [name] / Alert threshold: [value or condition] — then one action sentence

**Type contract rule:** A mitigation is only complete when its named sub-fields are filled in. A Spike without a named unknown and time-box is incomplete. A Gate without a criterion is incomplete. Fulfilling the sub-fields makes generic hedges structurally impossible — "monitor closely" cannot satisfy any type contract.

**Forbidden mitigation text — replace on sight:** "monitor closely", "keep an eye on", "revisit later", "consider alternatives", "be careful", "evaluate options". These name no action and fulfill no type contract. If you draft one, replace it with a typed mitigation before continuing.

---

**STEP 3 — RISK INTERDEPENDENCIES (mandatory section, >=3 pairs)**

Write this section with the exact heading:

## Risk Interdependencies

List at least 3 compound-risk pairings. Each pairing must name both risks explicitly and give a one-clause reason. Format:

- If [Risk A: name it by title] materializes, [Risk B: name it by title] escalates to [HIGH / MEDIUM / LOW] because [one-clause reason].

Enforcement rules:
- Do not put interdependency notes inside individual table rows. This section is the only place they appear.
- Minimum 3 named pairs. If you find fewer than 3 after reviewing all rows, your risks are too generic — revise STEP 2 to make them more specific before returning here. A register with fewer than 3 natural pairings has not reached sufficient specificity.
- "If technical risks compound other risks" is not a valid pairing. Both risks must be named by their exact title from the table.
- Each pairing must declare a severity direction.

---

**STEP 4 — SELF-CHECK**

Before writing the artifact, verify every item:
- [ ] Inertia is row 0, before any Technical/Market/Compliance/Dependency/Timeline risk
- [ ] Severity values are only HIGH, MEDIUM, or LOW — no numbers, percentages, or invented labels
- [ ] At least 3 dimensions covered in the table
- [ ] Every likelihood cell starts with "IF" — scan every row; no bare probability labels
- [ ] Every row has a named Mitigation Type from the approved list
- [ ] Every mitigation fulfills its type contract (named sub-fields present)
- [ ] Zero instances of forbidden mitigation text anywhere in the register
- [ ] Rows after inertia sorted high-to-low severity
- [ ] ## Risk Interdependencies section exists with at least 3 explicitly named compound-risk pairs

Fix any violation before proceeding.

---

**STEP 5 — AMEND (if present in prompt)**

AMEND: focus on [dimension] — keep inertia (row 0) and the ## Risk Interdependencies section, remove all rows not matching [dimension]. Re-sort.
AMEND: adjust severity threshold to [level] — keep inertia (row 0) and the ## Risk Interdependencies section, remove rows below [level]. Re-sort.

---

Write artifact to: simulations/scout/risk/{topic}-risk-{date}.md
```

---

## Variation Summary (v3 rubric projection)

The v3 rubric adds 3 aspirational criteria (C-14/C-15/C-16) each worth 2 points. Max composite rises to 106. R2 V-05 under v3 rubric scores 103 — it already passes C-14 and C-15 but fails C-16 (only ≥2 pairs). R3 targets C-16.

| ID | Axes | New Mechanism | C-14 | C-15 | C-16 | vs R2 V-05 | Score | Golden |
|----|------|---------------|------|------|------|------------|-------|--------|
| V-01 | Lifecycle | >=3 pairs (R2 V-03 base) | FAIL | FAIL | **PASS** | Isolated C-16 | ~99 | YES |
| V-02 | Output format | IF-THEN schema template (R2 V-01 base) | **PASS** | FAIL | FAIL | Structural vs rule C-14 | ~96 | YES |
| V-03 | Phrasing register | Type contract sub-fields (R2 V-02 base) | FAIL | **PASS** | FAIL | Structural vs definition C-15 | ~96 | YES |
| V-04 | Lifecycle + Output format | >=3 pairs + IF-THEN schema (R2 V-04 base) | **PASS** | **PASS** | **PASS** | C-14+C-15+C-16 | ~103 | YES |
| V-05 | Full integration | R2 V-05 + all v3 upgrades | **PASS** | **PASS** | **PASS** | Max attainable | **~105** | YES |

### Score calculations (v3 rubric, max 106)

- **Essential** (C-01–C-05): 60 pts, 5/5 pass on all R3 variations
- **Recommended** (C-06–C-08): 30 pts, 3/3 pass on all R3 variations
- **Aspirational** (C-09–C-16): 16 pts max, 2 pts each; C-10 always PARTIAL (1 pt)

| ID | Essential | Recommended | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | Composite |
|----|-----------|-------------|------|------|------|------|------|------|------|------|-----------|
| V-01 | 60 | 30 | 2 | 1 | 1 | 1 | 2 | 0 | 0 | **2** | **99** |
| V-02 | 60 | 30 | 0 | 1 | 2 | **2** | 0 | **2** | 0 | 0 | **95** |
| V-03 | 60 | 30 | 0 | 1 | **2** | 1 | 0 | 0 | **2** | 0 | **96** |
| V-04 | 60 | 30 | 2 | 1 | 2 | **2** | 2 | **2** | **2** | **2** | **105** |
| V-05 | 60 | 30 | 2 | 1 | 2 | **2** | 2 | **2** | **2** | **2** | **105** |

### Rankings

1. **V-04 and V-05 — 105 (tie)** — Both reach the base-prompt ceiling. C-10 PARTIAL (1 pt) is unreachable without a live AMEND directive. V-04 is the minimal combination path; V-05 is the structurally richer full-integration with role decomposition and the extended type contract sub-fields.
2. **V-01 — 99** — Cleanest C-16 proof. Isolates the ≥3 pairs mechanism on R2 V-03 baseline. IF-THEN and taxonomy absent so C-14/C-15 fail — deliberate single-axis isolation.
3. **V-03 — 96** — C-15 structural obligation proof. Type contract sub-fields on R2 V-02 baseline. No interdependency section so C-13/C-16 fail. C-14 fails (no IF-THEN).
4. **V-02 — 95** — C-14 schema template proof. Schema header enforcement on R2 V-01 baseline. No interdependency section so C-13/C-16 fail. C-15 fails (no taxonomy in this base).

### R3 Design Notes

**Why V-04 and V-05 tie**: Both include all three v3 mechanisms (schema IF-THEN, type contracts, ≥3 pairs). V-04 is a cleaner combination of R2 V-04 + interdependency upgrade — compact prompt. V-05 adds the three-role decomposition, richer type contract sub-fields, and the extended 9-item self-check from R2 V-05. Both reach 105. For production use, V-05 is preferred — the role decomposition produces better dimensional coverage and the sub-field obligations are more explicit, reducing edge-case failures on unusual topics.

**C-16 backward pressure**: The ≥3 pairs count is not arbitrary. A register with generic risks ("technical implementation may be complex") cannot produce 3 distinct named pairings. The minimum forces the model to have generated 3 pairs' worth of specific risk entries before the interdependency phase can close. This is why V-03 (Phase 3) smell-test in R2 said "if only 1 pairing, your risks are too generic" — same logic applied at a higher threshold in R3.

**Schema template vs. rule for C-14**: V-02 tests whether a column header reading `IF [condition], THEN risk activates` is a stronger structural enforcer than R2 V-01's explicit rule "every likelihood must begin with IF." The table cell is a blank to fill in; the column header models the required text. Both should pass C-14, but the schema approach may produce more consistent IF-THEN phrasing because the model is completing a template rather than following a constraint.

**Structural obligation sub-fields for C-15**: V-03 goes beyond R2 V-02's type selection (pick from Spike/Validate/Gate/Contract/Cut/Instrument) by requiring named sub-fields per type. C-15 requires "positively typed" mitigations where each type carries a structural obligation. The sub-fields make the obligation explicit and verifiable: a Spike cell containing only "run a spike on performance" fails the contract; a Spike cell containing "Unknown: SDK rate-limit behavior under concurrent load / Time-box: 2 days" fulfills it. V-05 integrates this approach.

**C-10 ceiling unchanged**: AMEND behavior requires a live AMEND directive and cannot be demonstrated in a base prompt. PARTIAL (1 pt) remains the ceiling for C-10 on all five variations. Score ceiling without C-10 is 105.

```json
{"top_score": 105, "all_essential_pass": true, "gap_closed": "C-16 (>=3 interdependency pairs)", "mechanisms_tested": [">=3 pairs with backward pressure smell-test (V-01)", "IF-THEN as table schema template — completion vs rule-following (V-02)", "type contract sub-fields — named structural obligation per type (V-03)", "schema-IF-THEN + >=3 pairs combination (V-04)", "full integration with role decomposition + type contracts + >=3 pairs + 9-item self-check (V-05)"], "ceiling_note": "C-10 PARTIAL (1pt) is irreducible on all base prompts — live AMEND directive required to demonstrate PASS"}
```
