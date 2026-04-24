---
skill: quest-variate
skill_target: scout-risk
round: 6
date: 2026-03-16
rubric: simulations/quest/rubrics/scout-risk-rubric-v6-2026-03-16.md
axes_explored: [lifecycle-emphasis (C-21: standalone downstream diversity audit), output-format (C-22: vocabulary-constrained typed columns), phrasing-register (C-21: explicit Repair Loop labels), lifecycle+output-format (C-21+C-22+C-15), full-integration]
---

# scout-risk — Prompt Variations R6

Five complete, runnable skill body prompts. Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

**R6 context**: R4 V-05 under v6 rubric scores 113/118. The v6 rubric adds C-21 (repair-loop count equals minimum-count gate count) and C-22 (severity-transition columns type-constrained at cell level). Analysis of R4 V-05 under v6 rubric finds two gaps: (1) C-21 FAIL — R4 V-05 has two minimum-count gates (type diversity + pair count) but only one downstream repair loop with an explicit back-reference to STEP 2; the diversity gate is embedded within STEP 2 as a generation-time rule, not a downstream check. (2) C-22 FAIL — R4 V-05's interdependency format is prose ("escalates from [CURRENT] to [NEW]"), not a typed table where From and To columns carry vocabulary constraints naming {HIGH, MEDIUM, LOW} as the complete allowed value set. Max composite rises from 110 (v4) to 118 (v6). Golden threshold stays >= 80.

---

## V-01 — Axis: Lifecycle Emphasis (C-21: standalone Phase 2b extracts diversity audit into a downstream step with explicit back-reference)

**Hypothesis**: R4 V-01's type diversity mechanism was embedded within STEP 2 as a generation-time rule — the model is instructed to diversify types while generating, not after. A downstream repair loop requires the model to (1) complete generation, (2) audit the result, (3) detect failure, and (4) revise the upstream step by name. This variation extracts the diversity gate into a standalone Phase 2b that runs after Phase 2 is complete, explicitly names "return to Phase 2," and mirrors the pair-count repair loop in Phase 3. The result is two count gates (Phase 2b: type diversity; Phase 3: pair count) and two downstream repair loops, each naming Phase 2. C-21 PASS via this mechanism. C-22 remains FAIL — prose FROM/TO format is preserved, isolating C-21 alone. C-15 is absent (simpler R4 V-01 base, no type sub-field contracts).

---

```
Auto-detect the topic from repo context. Do not ask.

Build a risk register organized in phases. Complete each phase before starting the next.

---

**Phase 1: Write the inertia risk (mandatory, first).**

The inertia risk is always the first entry. It is the risk that the status quo was good enough and this feature is the wrong thing to build. Do not skip it. Do not move it.

Give it:
- Severity: HIGH, MEDIUM, or LOW — nothing else
- Likelihood: IF [specific condition that would make status quo win], THEN this risk activates.
- Mitigation type: one of — Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation: name what the team should do to test whether inertia applies before building.
  Forbidden phrases: "monitor closely", "keep an eye on", "revisit later", "consider alternatives", "be careful", "evaluate options". Any of these renders a mitigation invalid — replace on sight.

---

**Phase 2: Write the dimensional risks.**

List at least one risk each from 3 or more of these dimensions: Technical, Market, Compliance, Dependency, Timeline.

For each risk, provide:
- Name: a short label (5-10 words)
- Dimension: which of the five it belongs to
- Severity: HIGH, MEDIUM, or LOW — nothing else
- Likelihood: IF [specific condition or scenario that triggers this risk], THEN this risk activates. No bare probability labels ("high", "possible", "~30%").
- Mitigation type: one of — Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation: a concrete action. Forbidden phrases — "monitor closely", "keep an eye on", "revisit later", "consider alternatives", "be careful", "evaluate options" — replace on sight.

Sort dimensional risks from highest to lowest severity.

---

**Phase 2b: Type Diversity Audit (mandatory — run after Phase 2 is complete).**

Scan all mitigation type labels across Phase 1 and Phase 2 entries. List each distinct type class name found. Count distinct types.

If fewer than 3 distinct type class names appear, return to Phase 2 and revise mitigation type assignments until at least 3 distinct types are represented. Repeat this audit after each revision pass. Do not proceed to Phase 3 until the count reaches 3 or more.

Available type classes: Spike, Validate, Gate, Contract, Cut, Instrument.

---

**Phase 3: Write the Risk Interdependencies section (mandatory).**

After the risk register entries, write a section with this exact heading:

## Risk Interdependencies

This section must contain at least 3 named compound-risk pairings. Use this format for each:

> If [Risk A: name it explicitly by Phase 2 label] materializes, [Risk B: name it explicitly by Phase 2 label] escalates from [CURRENT SEVERITY of Risk B] to [NEW SEVERITY] because [one-clause reason].

Enforcement rules:
- Do not scatter interdependencies inside individual risk entries. This section is the only location.
- At least 3 pairings are required. If you find fewer than 3 after reviewing all rows, your risks are not specific enough — return to Phase 2 and make them more concrete, then return here.
- Both risks must be named by their exact title.
- Every pairing must state both the FROM severity (Risk B's current severity) and the TO severity (Risk B's new severity). A pairing stating only "escalates to HIGH" without the origin severity is incomplete.

---

**Phase 4 (only if AMEND is in the prompt):**

AMEND: focus on [dimension] — keep inertia and the ## Risk Interdependencies section, drop all dimensional risks outside that dimension. Re-sort.
AMEND: adjust severity threshold to [level] — keep inertia and the ## Risk Interdependencies section, drop risks below that level. Re-sort.

---

Write the artifact to: simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-02 — Axis: Output Format (C-22: vocabulary-constrained typed columns on From/To in interdependency table)

**Hypothesis**: R4 V-03 used a 5-column interdependency table with separate From Severity and To Severity columns — a structural advance over prose. But the columns carried no vocabulary constraint: the model could write "MEDIUM → HIGH" or "escalates to HIGH" in the cell without violating any stated rule. C-22 requires that From and To are defined as vocabulary-constrained fields where {HIGH, MEDIUM, LOW} is named as the complete allowed value set, making any other cell value a detectable violation. This variation adds that explicit cell-level vocabulary rule to both columns. Built on R4 V-03's type sub-field contract base (C-15 PASS). No type diversity gate, so C-18 FAIL — this isolates C-22 alone. C-21 passes trivially (1 count gate: pair count; 1 repair loop: return to Step 2 — count matches).

---

```
Auto-detect the topic from repo context. Do not ask.

Build a risk register. Follow this sequence.

---

**Step 1: Write the inertia risk (mandatory, first).**

The inertia risk is always the first entry — the risk that the status quo was good enough and this feature is the wrong thing to build. Do not skip it. Do not move it.

Give it:
- Severity: HIGH, MEDIUM, or LOW — nothing else
- Likelihood: IF [specific condition that makes status quo win], THEN this risk activates.
- Mitigation type: one of — Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation (fulfill the type contract):
  - If Spike: Unknown: [what is being resolved] / Time-box: [duration]
  - If Validate: Assumption: [what is being tested] / Method: [interviews / prototype / survey]
  - If Gate: Criterion: [what must be true to pass]
  - If Contract: Party: [who] / Commitment: [what is owed]
  - If Cut: Element: [what is removed] / Scope effect: [impact on v1 delivery]
  - If Instrument: Metric: [name] / Alert threshold: [value or condition]

---

**Step 2: Write the dimensional risks.**

List at least one risk each from 3 or more of these dimensions: Technical, Market, Compliance, Dependency, Timeline.

For each risk, provide:
- Name: a short label (5-10 words)
- Dimension: which of the five it belongs to
- Severity: HIGH, MEDIUM, or LOW — nothing else
- Likelihood: IF [specific condition or scenario], THEN this risk activates.
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

Forbidden phrases — "monitor closely", "keep an eye on", "revisit later", "consider alternatives", "be careful", "evaluate options" — are incompatible with all six types. Replace on sight.

Sort dimensional risks from highest to lowest severity.

---

**Step 3: Check your type contracts.**

Read back every mitigation. Verify each fulfills its type contract (named sub-fields filled in). Replace any that fail this check.

---

**Step 4: Write the Risk Interdependencies section (mandatory).**

After the dimensional risks, write a section with this exact heading:

## Risk Interdependencies

This section must contain at least 3 compound-risk pairings. Output as a markdown table with these exact column headers:

| Trigger Risk | Activated Risk | From Severity | To Severity | Condition |
|-------------|----------------|---------------|-------------|-----------|

Column definitions:
- Trigger Risk: name the risk that materializes (use the exact name from Step 2)
- Activated Risk: name the risk whose severity changes (use the exact name from Step 2)
- From Severity: the current severity of Activated Risk before activation. **Vocabulary: must contain exactly one of {HIGH, MEDIUM, LOW}. These are the only permitted values. No other text is valid in this column.**
- To Severity: the new severity after Trigger Risk materializes. **Vocabulary: must contain exactly one of {HIGH, MEDIUM, LOW}. These are the only permitted values. No other text is valid in this column.**
- Condition: one clause explaining why activation occurs

Enforcement rules:
- Both risks must be named by their exact title from the register.
- From Severity and To Severity are separate required fields. Each cell must contain exactly one of {HIGH, MEDIUM, LOW} and nothing else. A cell containing "MEDIUM → HIGH", "escalates to HIGH", or any prose violates the vocabulary constraint.
- If you cannot find any compound pairs, your risks are too generic — return to Step 2 and revise.
- Minimum 3 rows required. If fewer than 3 pairs are present, return to Step 2 and add or refine risk entries until 3 pairs can be named.

---

**Step 5 (only if AMEND is in the prompt):**

AMEND: focus on [dimension] — keep inertia, drop all dimensional risks outside that dimension.
AMEND: adjust severity threshold to [level] — keep inertia, drop risks below that level.

---

Write the artifact to: simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-03 — Axis: Phrasing Register (C-21: explicit "Repair Loop A / Repair Loop B" labels make the two-loop structure auditable by name)

**Hypothesis**: V-01 achieves two downstream repair loops by extracting Phase 2b as a new phase. V-03 tests an alternative structural mechanism: using named repair loop sections ("Repair Loop A" and "Repair Loop B") as labeled steps, each with an explicit back-reference to Step 2. The labeling convention makes it visually and structurally unambiguous that two independent loops exist — a reader or LLM scanning the prompt can count them. This tests whether explicit naming produces equivalent C-21 enforcement to the phase-extraction approach in V-01. Built on a simpler base (no type sub-field contracts) to isolate the phrasing-register axis. C-22 remains FAIL — prose FROM/TO format — and C-15 remains absent, isolating C-21 via structural labeling alone.

---

```
Auto-detect the topic from repo context. Do not ask.

Build a risk register. Follow this sequence. The quality protocol includes two named repair loops — Repair Loop A runs after risk generation, Repair Loop B runs after interdependency generation.

---

**Step 1: Write the inertia risk (mandatory, first).**

The inertia risk is always the first entry — the risk that the status quo was good enough and this feature is the wrong thing to build. Do not skip it. Do not move it.

Format:
- Dimension: Inertia
- Severity: HIGH, MEDIUM, or LOW — nothing else
- IF [specific condition that makes status quo win], THEN this risk activates.
- Mitigation type: one of — Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation: one concrete action to test whether inertia applies. Forbidden phrases: "monitor closely", "keep an eye on", "revisit later", "consider alternatives", "be careful", "evaluate options".

---

**Step 2: Write the dimensional risks.**

Cover at least 3 of: Technical, Market, Compliance, Dependency, Timeline.

For each entry:
- Dimension: [Technical / Market / Compliance / Dependency / Timeline]
- Risk: a short label (5-10 words)
- Severity: HIGH, MEDIUM, or LOW — nothing else
- IF [specific triggering condition], THEN this risk activates. No bare probability labels.
- Mitigation type: one of — Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation: a concrete action. Forbidden phrases — "monitor closely", "keep an eye on", "revisit later", "consider alternatives", "be careful", "evaluate options" — replace on sight.

Sort entries from highest to lowest severity.

---

**Repair Loop A — Type Diversity (run after Step 2 is complete):**

Scan all mitigation type labels across Steps 1 and 2. List the distinct type class names found. Count them.

Minimum required: 3 distinct type class names. If fewer than 3 appear, return to Step 2 and revise mitigation type assignments — replace or reassign entries to introduce additional type classes — until the count reaches 3. Re-run this audit after each revision.

---

**Step 3: Write the Risk Interdependencies section (mandatory).**

Write a section with this exact heading:

## Risk Interdependencies

List at least 3 compound-risk pairings. Format each as:

> If [Risk A: name by exact Step 2 label] materializes, [Risk B: name by exact Step 2 label] escalates from [CURRENT SEVERITY of Risk B] to [NEW SEVERITY] because [one-clause reason].

Every pairing must state both FROM severity (Risk B's current severity) and TO severity (Risk B's new severity). Stating only the destination ("escalates to HIGH") without the origin is incomplete.

---

**Repair Loop B — Interdependency Count (run after Step 3 is complete):**

Count the named compound-risk pairs in the ## Risk Interdependencies section.

Minimum required: 3 named pairs. If fewer than 3 are present, return to Step 2 and add or refine risk entries to generate additional compound pairs, then regenerate the ## Risk Interdependencies section.

---

**Step 4 (only if AMEND is in the prompt):**

AMEND: focus on [dimension] — keep inertia and the ## Risk Interdependencies section, drop all entries not matching [dimension]. Re-sort.
AMEND: adjust severity threshold to [level] — keep inertia and the ## Risk Interdependencies section, drop entries below [level]. Re-sort.

---

Write the artifact to: simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-04 — Axes: Lifecycle + Output Format (C-21: standalone diversity audit step + C-22: vocabulary-constrained typed columns + C-15: type sub-field contracts)

**Hypothesis**: V-01 isolates C-21 via Phase 2b extraction; V-02 isolates C-22 via typed column vocabulary. Combining them on top of R4 V-03's type sub-field base (C-15 PASS) closes both gaps simultaneously. The prompt introduces two explicitly downstream audit steps: Step 2b verifies type contract fulfillment (existing from R4 V-03), Step 2c audits type diversity and names "return to Step 2," and Step 3 uses a vocabulary-constrained typed table for interdependencies. Result: 2 count gates (Step 2c: diversity; Step 3: pair count) × 2 repair loops, both naming Step 2. C-21 PASS + C-22 PASS. Expected: all criteria except C-10 PARTIAL.

---

```
Auto-detect the topic from repo context. Do not ask.

Build a risk register. Follow this sequence. Two repair loops run downstream of generation — one for type diversity, one for interdependency count.

---

**Step 1: Write the inertia risk (mandatory, first).**

The inertia risk is always the first entry — the risk that the status quo was good enough and this feature is the wrong thing to build. Do not skip it. Do not move it.

Format:
- Dimension: Inertia
- Severity: HIGH, MEDIUM, or LOW — nothing else
- IF [specific condition that makes status quo win], THEN this risk activates.
- Mitigation type: one of — Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation (fulfill the type contract):
  - If Spike: Unknown: [what is being resolved] / Time-box: [duration]
  - If Validate: Assumption: [what is being tested] / Method: [interviews / prototype / survey]
  - If Gate: Criterion: [what must be true to pass]
  - If Contract: Party: [who] / Commitment: [what is owed]
  - If Cut: Element: [what is removed] / Scope effect: [impact on v1 delivery]
  - If Instrument: Metric: [name] / Alert threshold: [value or condition]

---

**Step 2: Write the dimensional risks.**

Cover at least 3 of: Technical, Market, Compliance, Dependency, Timeline.

For each entry:
- Dimension: [Technical / Market / Compliance / Dependency / Timeline]
- Risk: a short label (5-10 words)
- Severity: HIGH, MEDIUM, or LOW — nothing else
- IF [specific triggering condition], THEN this risk activates.
- Mitigation type: one of — Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation (fulfill the type contract using the sub-fields above)

**Type contract rules:**
- Spike without a named unknown and time-box is incomplete.
- Gate without a named criterion is incomplete.
- Validate without a named assumption and method is incomplete.
- Contract without a named party and commitment is incomplete.
- Cut without a named element and scope effect is incomplete.
- Instrument without a named metric and alert threshold is incomplete.

Forbidden phrases — "monitor closely", "keep an eye on", "revisit later", "consider alternatives", "be careful", "evaluate options" — replace on sight.

Sort entries from highest to lowest severity.

---

**Step 2b: Type Contract Verification.**

Read back every mitigation. Verify each fulfills its type contract (named sub-fields filled in). Replace any that fail.

---

**Step 2c: Type Diversity Audit (mandatory — run after Step 2b).**

Scan all mitigation type labels across Steps 1 and 2. List the distinct type class names found. Count them.

Minimum required: 3 distinct type class names. If fewer than 3 appear, return to Step 2 and revise mitigation type assignments until at least 3 distinct classes are represented. Repeat this audit after revision. Do not proceed to Step 3 until the count is 3 or more.

---

**Step 3: Write the Risk Interdependencies section (mandatory).**

Write a section with this exact heading:

## Risk Interdependencies

This section must contain at least 3 compound-risk pairings. Output as a markdown table:

| Trigger Risk | Activated Risk | From Severity | To Severity | Condition |
|-------------|----------------|---------------|-------------|-----------|

Column definitions:
- Trigger Risk: name the risk that materializes (exact name from Step 2)
- Activated Risk: name the risk whose severity changes (exact name from Step 2)
- From Severity: the current severity of Activated Risk. **Vocabulary: must contain exactly one of {HIGH, MEDIUM, LOW}. No other values are permitted.**
- To Severity: the new severity after Trigger Risk materializes. **Vocabulary: must contain exactly one of {HIGH, MEDIUM, LOW}. No other values are permitted.**
- Condition: one clause explaining why activation occurs

Enforcement rules:
- Both risks must be named by their exact title from the register.
- From Severity and To Severity are separate required fields — each cell must contain exactly one of {HIGH, MEDIUM, LOW}. A prose entry ("escalates to HIGH", "MEDIUM → HIGH") violates the vocabulary constraint.
- Minimum 3 rows required. If fewer than 3 pairs are present, return to Step 2 and add or refine risk entries until 3 pairs can be named.

---

**Step 4 (only if AMEND is in the prompt):**

AMEND: focus on [dimension] — keep inertia and the ## Risk Interdependencies section, drop all entries not matching [dimension]. Re-sort.
AMEND: adjust severity threshold to [level] — keep inertia and the ## Risk Interdependencies section, drop entries below [level]. Re-sort.

---

Write the artifact to: simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-05 — Full Integration (R4 V-05 base + STEP 2b standalone diversity audit + typed-column interdependency table)

**Hypothesis**: R4 V-05 is the definitive integration — three-role decomposition (Skeptic/Realist/Scheduler), IF-THEN column header as schema template, type sub-field contracts, 11-item self-check. Under v6 rubric it scores 113/118. Two targeted changes close the remaining gap: (1) move the embedded diversity rule out of STEP 2 into a standalone STEP 2b that post-processes the table and explicitly says "return to STEP 2" — creating a second downstream repair loop with a named back-reference (C-21 PASS); (2) replace the prose interdependency format with a typed-column table where From Severity and To Severity are vocabulary-constrained to {HIGH, MEDIUM, LOW} as the complete allowed value set (C-22 PASS). The STEP 4 self-check gains two new items. Everything else in R4 V-05 is preserved intact. Expected: C-21 PASS (+2), C-22 PASS (+2) → 117/118.

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

**STEP 2b — TYPE DIVERSITY AUDIT (mandatory — run after STEP 2 table is complete)**

Scan every row in the STEP 2 table. List each distinct Mitigation Type class name found. Count distinct types.

Minimum required: 3 distinct type class names. If fewer than 3 appear, return to STEP 2 and revise mitigation type assignments — select different type classes appropriate to each risk's nature and fulfill each type's sub-field contract — until at least 3 distinct class names are present. Re-run this audit after revision.

Do not proceed to STEP 3 until the audit passes.

---

**STEP 3 — RISK INTERDEPENDENCIES (mandatory section, >= 3 pairs)**

Write this section with the exact heading:

## Risk Interdependencies

List at least 3 compound-risk pairings. Output as a markdown table with these exact column headers:

| Trigger Risk | Activated Risk | From Severity | To Severity | Condition |
|-------------|----------------|---------------|-------------|-----------|

Column definitions:
- Trigger Risk: name the risk that materializes (exact title from STEP 2 table)
- Activated Risk: name the risk whose severity changes (exact title from STEP 2 table)
- From Severity: the current severity of Activated Risk before activation. **Vocabulary constraint: must contain exactly one of {HIGH, MEDIUM, LOW}. These are the only permitted values in this column. No other text is valid.**
- To Severity: the new severity after Trigger Risk materializes. **Vocabulary constraint: must contain exactly one of {HIGH, MEDIUM, LOW}. These are the only permitted values in this column. No other text is valid.**
- Condition: one clause explaining why activation occurs

Enforcement rules:
- Do not put interdependency notes inside individual rows of the STEP 2 table. This section is the only place they appear.
- Both risks must be named by their exact title from the STEP 2 table. "Technical risks compound other risks" is not valid.
- From Severity and To Severity are separate required fields — each cell must contain exactly one of {HIGH, MEDIUM, LOW}. A cell containing prose ("escalates to HIGH", "MEDIUM → HIGH", "from medium to high") fails the vocabulary constraint.
- Minimum 3 rows required. If fewer than 3 pairs can be identified, return to STEP 2 and add or refine risk entries to generate additional compound pairs. Regenerate this table after revision.

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
- [ ] Type diversity audit complete: at least 3 distinct Mitigation Type class names used
- [ ] ## Risk Interdependencies table exists with at least 3 rows
- [ ] From Severity column: every cell contains exactly one of {HIGH, MEDIUM, LOW}
- [ ] To Severity column: every cell contains exactly one of {HIGH, MEDIUM, LOW}

Fix any violation before proceeding.

---

**STEP 5 — AMEND (if present in prompt)**

AMEND: focus on [dimension] — keep inertia (row 0) and the ## Risk Interdependencies section, remove all rows not matching [dimension]. Re-sort.
AMEND: adjust severity threshold to [level] — keep inertia (row 0) and the ## Risk Interdependencies section, remove rows below [level]. Re-sort.

---

Write artifact to: simulations/scout/risk/{topic}-risk-{date}.md
```

---

## Variation Summary (v6 rubric projection)

The v6 rubric adds C-21 (repair-loop count equals gate count, 2 pts) and C-22 (cell-level vocabulary constraint on severity-transition columns, 2 pts). Max composite rises to 118. R4 V-05 under v6 scores 113 — it passes C-19 and C-20 (already present in R4) but fails C-21 (embedded diversity rule is not a downstream repair loop) and C-22 (prose FROM/TO).

| ID | Axes | C-21 mechanism | C-22 | vs R4 V-05 (v6:113) | Score | Golden |
|----|------|----------------|------|----------------------|-------|--------|
| V-01 | Lifecycle | Phase 2b standalone audit, 2 loops for 2 gates | FAIL | +C-18+C-21, no C-15/C-22 | **115** | YES |
| V-02 | Output format | Trivially PASS (1 gate = 1 loop) | **PASS** | +C-15+C-22, no C-18 | **117** | YES |
| V-03 | Phrasing register | Named Repair Loop A/B, 2 loops for 2 gates | FAIL | +C-18+C-21, no C-15/C-22 | **115** | YES |
| V-04 | Lifecycle + Output format | Step 2c standalone, 2 loops for 2 gates | **PASS** | +C-15+C-18+C-21+C-22 | **117** | YES |
| V-05 | Full integration | STEP 2b standalone, 2 loops for 2 gates | **PASS** | +C-18+C-21+C-22 | **117** | YES |

### Score calculations (v6 rubric, max 118)

- **Essential** (C-01–C-05): 60 pts, 5/5 pass on all R6 variations
- **Recommended** (C-06–C-08): 30 pts, 3/3 pass on all R6 variations
- **Aspirational** (C-09–C-22): 28 pts max, 2 pts PASS / 1 pt PARTIAL / 0 pts FAIL; C-10 always PARTIAL (1 pt)

| ID | Ess | Rec | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | C-21 | C-22 | Composite |
|----|-----|-----|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| V-01 | 60 | 30 | 2 | 1 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 2 | 2 | **2** | 0 | **115** |
| V-02 | 60 | 30 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | **2** | **2** | **117** |
| V-03 | 60 | 30 | 2 | 1 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 2 | 2 | **2** | 0 | **115** |
| V-04 | 60 | 30 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **2** | **2** | **117** |
| V-05 | 60 | 30 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **2** | **2** | **117** |

### Rankings

1. **V-02, V-04, V-05 — 117 (three-way tie)** — 117 is the theoretical ceiling for a base prompt. C-10 PARTIAL (1 pt vs 2 pt) is irreducible without a live AMEND directive. V-02 achieves 117 by isolating C-22 alone — it passes C-21 trivially (1 gate = 1 loop) and gains C-15 from R4 V-03's base, but gives up C-18 (no diversity gate). V-04 is the minimal combination path (C-21 + C-22 + C-15). V-05 is the structurally richest — role decomposition, schema-template IF-THEN, sub-field contracts, standalone STEP 2b, typed table, 12-item self-check.
2. **V-01 — 115** — C-21 PASS via Phase 2b extraction mechanism. Cleanest isolation of C-21 mechanism A (standalone downstream step) on R4 V-01 baseline. C-15 absent (simpler base), C-22 absent (prose FROM/TO) — deliberate single-axis. Confirms Phase 2b extraction is sufficient for C-21.
3. **V-03 — 115** — C-21 PASS via Repair Loop labeling mechanism. Same score as V-01 but different structural mechanism: named "Repair Loop A / Repair Loop B" sections rather than a new phase. C-22 absent, C-15 absent — deliberate single-axis. Mechanism comparison with V-01: phase extraction vs. explicit loop labels. Both achieve C-21 at same score; empirical scoring will reveal whether one mechanism is more reliable.

### R6 Design Notes

**C-21: two mechanisms compared (V-01 vs V-03)**

Both V-01 and V-03 achieve C-21 PASS, but via structurally distinct approaches:
- V-01 uses a **phase extraction** mechanism: the diversity audit becomes a numbered phase (Phase 2b) that runs after Phase 2 and explicitly says "return to Phase 2." The audit is a sequential step in the workflow — the model completes Phase 2, then executes Phase 2b as a distinct action.
- V-03 uses a **labeled loop** mechanism: the repair logic is formatted as named sections ("Repair Loop A", "Repair Loop B") bracketing the generation steps. The labels make the count auditable without changing the phase structure.

Phase extraction (V-01) integrates naturally with R4 V-05's multi-step architecture. Labeled loops (V-03) may produce more consistent two-loop behavior because the repair sections are visually distinct from generation steps — a model is less likely to conflate "Repair Loop A" with STEP 2 generation than to collapse a Phase 2b into Phase 2.

**C-22: typed column vocabulary vs. prose template**

R4 V-03/V-04 had a 5-column interdependency table where "From Severity" and "To Severity" were separate column headers — a structural advance over prose FROM/TO. But the columns lacked cell-level vocabulary rules. V-02 and V-05 add: "Must contain exactly one of {HIGH, MEDIUM, LOW}. No other values are permitted." This is the constraint that makes violations mechanically detectable. The cell rule is stronger than a prose instruction ("state the FROM severity") because the model cannot write "escalates to HIGH" inside a cell defined as accepting only {HIGH, MEDIUM, LOW}.

**V-02 scoring paradox: C-18 FAIL but 117**

V-02 deliberately omits the type diversity gate (C-18 FAIL, -2 pts) to isolate C-22. Yet it still scores 117 because C-22 PASS (+2 pts) and C-15 PASS (inherited from R4 V-03 base, +2 pts vs V-01's simpler base) offset the C-18 loss. V-02 is the demonstration that C-22 alone, on the right base, reaches the score ceiling.

**C-21 trivial pass in V-02**

V-02 has exactly one minimum-count gate (pair count >= 3) and one repair instruction (return to Step 2). C-21 requires repair-loop count equals gate count: 1 = 1 → PASS. The criterion is not "maximum number of repair loops" but "no gate without a loop." V-02's single gate satisfies this with a single loop. V-04 and V-05 have two gates (diversity + pair count) and two loops — a richer demonstration of C-21.

**C-10 ceiling unchanged at PARTIAL**

All five variations handle AMEND via a dedicated step retaining inertia and the interdependency table under any scope narrowing. No live AMEND directive exists in a base prompt — PARTIAL (1 pt) remains the ceiling for C-10 on all base-prompt evaluations. Theoretical max with C-10 PASS is 118.

```json
{"top_score": 117, "all_essential_pass": true, "gap_closed": ["C-21 (repair-loop count equals minimum-count gate count)", "C-22 (From/To severity columns vocabulary-constrained to {HIGH, MEDIUM, LOW} at cell level)"], "mechanisms_tested": ["Phase 2b extraction: standalone downstream diversity audit naming Phase 2 (V-01)", "Vocabulary-constrained typed columns: {HIGH, MEDIUM, LOW} as complete allowed value set (V-02)", "Named Repair Loop labels: Repair Loop A / Repair Loop B sections with explicit back-references (V-03)", "Phase 2b + typed columns + type sub-fields combined (V-04)", "Full integration: R4 V-05 base + STEP 2b + typed column table + 12-item self-check (V-05)"], "ceiling_note": "C-10 PARTIAL (1pt) is irreducible on all base prompts. Theoretical max with live AMEND directive is 118."}
```
