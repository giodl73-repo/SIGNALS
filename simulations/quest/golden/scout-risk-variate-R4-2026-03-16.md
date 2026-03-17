---
skill: quest-variate
skill_target: scout-risk
round: 4
date: 2026-03-16
rubric: simulations/quest/rubrics/scout-risk-rubric-v4-2026-03-16.md
axes_explored: [lifecycle-emphasis (C-17 FROM/TO prose template), output-format (C-18 diversity gate), phrasing-register (C-17 tabular FROM/TO columns), lifecycle+output-format (C-17+C-18+C-15 fix), full-integration]
---

# scout-risk — Prompt Variations R4

Five complete, runnable skill body prompts. Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

**R4 context**: Round 3 produced five GOLDEN variations (V-05 at 105/106 under v3 rubric). The v4 rubric adds two new aspirational criteria — C-17 (interdependency pairs carry severity-transition labels, FROM/TO) and C-18 (mitigation type portfolio covers ≥3 distinct classes). Analysis of R3 V-05 under v4 rubric confirms both fail: C-17 fails because R3 V-05's pairing format "escalates to [HIGH]" names only the destination, not the origin severity; C-18 fails because V-05 enforces type presence and sub-field fulfillment but never tests for diversity across the type vocabulary. Max composite rises from 106 to 110; golden threshold stays ≥80. R4 primary targets: C-17 and C-18. C-17 and C-18 are independent failures — each requires a distinct mechanism.

---

## V-01 — Axis: Lifecycle Emphasis (C-17: FROM/TO severity-transition labels in Phase 3)

**Hypothesis**: The pairing format in R3 V-01's Phase 3 reads "escalates to [HIGH/MEDIUM/LOW]" — a one-directional pointer that names the destination but not the origin. The origin severity is present in every risk entry in Phase 2; the gap is that the Phase 3 template doesn't require the model to carry it forward. Upgrading the template to "escalates from [CURRENT SEVERITY] to [NEW SEVERITY]" adds one named slot. The backward-pressure smell-test from R3 V-01 is preserved. Expected: C-17 PASS (+2). C-18 remains FAIL — no diversity gate in this variation, isolating C-17 alone.

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

> If [Risk A: name it explicitly] materializes, [Risk B: name it explicitly] escalates from [CURRENT SEVERITY of Risk B] to [NEW SEVERITY] because [one-clause reason].

Enforcement rules:
- Do not scatter interdependencies as footnotes inside individual risk entries. They belong here only.
- At least 3 pairings are required. If you find fewer than 3 after reviewing all rows, your risks are not specific enough — go back to Phase 2 and make them more concrete before returning here.
- "If technical risks compound" is not a valid pairing — both risks must be named explicitly by title.
- Every pairing must name the severity the risk escalates FROM and the severity it escalates TO. A pairing that says only "escalates to HIGH" without stating the origin severity is incomplete.

**Phase 4 (only if AMEND is in the prompt):**

AMEND: focus on [dimension] — keep inertia and the ## Risk Interdependencies section, drop all dimensional risks outside that dimension.
AMEND: adjust severity threshold to [level] — keep inertia and the ## Risk Interdependencies section, drop risks below that level.

**Write the artifact to:** simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-02 — Axis: Output Format (C-18: type diversity gate in table schema)

**Hypothesis**: R3 V-02 passes C-15 FAIL — it has a Mitigation Type column but no sub-field obligations, so labels are present but not positively typed. For R4, V-02's target is C-18 alone: after the table is complete, a diversity gate forces the model to count distinct type classes and replace entries if fewer than 3 distinct classes are present. The gate is a structural read-back analogous to the forbidden-words gate — it operates post-generation, creating repair pressure. The same table schema and IF-THEN column header from R3 V-02 are preserved. Expected: C-18 PASS (+2). C-17 remains FAIL — the interdependency note in Step 3 is optional and has no FROM/TO requirement, isolating C-18 alone.

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
- Mitigation type: one of — Spike / Validate / Gate / Contract / Cut / Instrument
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

**Step 2b: Type diversity gate (mandatory).**

After completing all rows, scan the Mitigation Type column. Count how many distinct type class names appear.

- If fewer than 3 distinct type classes appear, the register has type-monoculture: the taxonomy is labeling, not classifying. A register where every entry uses "Spike" has not applied the taxonomy — it has applied a single label. Replace entries with different type classes until at least 3 distinct type names are present in the column.
- The six available classes are: Spike, Validate, Gate, Contract, Cut, Instrument. Three is the minimum for meaningful coverage across a 5-7 entry register.

**Step 3: Note at least one interdependency.**

After the table, note any risks that compound each other:
"If [Risk A] materializes, [Risk B] escalates to [severity]."

**Step 4 (only if AMEND is in the prompt):**

AMEND: focus on [dimension] — keep inertia (row 0), drop all other dimensions.
AMEND: adjust severity threshold to [level] — keep inertia (row 0), drop risks below that level.

**Write the artifact to:** simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-03 — Axis: Phrasing Register (C-17: severity-transition table makes FROM/TO explicit columns)

**Hypothesis**: V-01 achieves C-17 by upgrading the prose template's single "escalates to" slot into a two-part "escalates from [X] to [Y]" pattern — the model still writes one prose sentence, and the FROM half could be omitted if the model collapses the template. V-03 tests a structurally stronger mechanism: replacing the prose pairing format with a 5-column markdown table where "From Severity" and "To Severity" are separate named columns. A table cell cannot be left blank without the omission being visible; the model completes the table by filling in cells, not by writing sentences. Built on R3 V-03's phrasing-register base (type contract sub-fields, C-15 PASS). Expected: C-17 PASS (+2) via column structure rather than prose template. C-18 remains FAIL — no diversity gate in this variation, isolating C-17's mechanism comparison with V-01.

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

**Step 4: Write the Risk Interdependencies section (mandatory).**

After the dimensional risks, write a section with this exact heading:

## Risk Interdependencies

This section must contain at least one compound-risk pairing. Output as a markdown table with these exact column headers:

| Trigger Risk | Activated Risk | From Severity | To Severity | Condition |
|-------------|----------------|---------------|-------------|-----------|

Column definitions:
- Trigger Risk: name the risk that materializes (use the exact name from Step 2)
- Activated Risk: name the risk whose severity changes (use the exact name from Step 2)
- From Severity: the current severity of Activated Risk (HIGH / MEDIUM / LOW)
- To Severity: the new severity after Trigger Risk materializes (HIGH / MEDIUM / LOW)
- Condition: one clause explaining why activation occurs

Enforcement rules:
- Both risks must be named by their exact title from the register.
- From Severity and To Severity are separate required fields — a row without both is incomplete.
- If you cannot find any compound pairs, your risks are too generic — revise Step 2 to make them more concrete.

**Step 5 (only if AMEND is in the prompt):**

AMEND: focus on [dimension] — keep inertia, drop all dimensional risks outside that dimension.
AMEND: adjust severity threshold to [level] — keep inertia, drop risks below that level.

**Write the artifact to:** simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-04 — Axes: Lifecycle + Output Format (C-17 + C-18 + C-15 fix)

**Hypothesis**: R3 V-04 combined IF-THEN schema template and ≥3 pairs but left C-15 at PARTIAL (sub-fields described but not required as named outputs) and lacked C-17 (no FROM/TO) and C-18 (no diversity gate). This variation makes three targeted changes to R3 V-04: (1) upgrades the interdependency pairing format to require FROM/TO severity transitions (C-17), (2) adds a type diversity gate after the table requiring ≥3 distinct classes (C-18), and (3) promotes the type sub-field definitions to required named outputs per V-05's mechanism (C-15 PARTIAL → PASS). The self-check gains two items: one for FROM/TO pairs and one for type diversity count. Expected: C-15 PASS (+1 over R3 V-04), C-17 PASS (+2), C-18 PASS (+2) → score 109.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal artifacts). Do not prompt unless context is absent.

Build a risk register. Every risk entry must pass two non-negotiable quality gates before you proceed: the likelihood column must complete the IF-THEN template, and the mitigation must be typed and fulfill its type's structural contract.

**Step 1: Write the inertia risk (mandatory, first).**

The inertia risk is always the first entry — the risk that the status quo was good enough and this feature is the wrong thing to build. Do not skip it. Do not move it.

Format:
- Dimension: Inertia
- Severity: HIGH, MEDIUM, or LOW — nothing else
- IF [specific condition that makes status quo win], THEN this risk activates.
- Mitigation type: one of — Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation (fulfill the type contract — required sub-fields below): one sentence

**Step 2: Write the dimensional risks (table format).**

Cover at least 3 of: Technical, Market, Compliance, Dependency, Timeline.

Output as a markdown table with these exact column headers:

| # | Dimension | Risk | Severity | IF [condition], THEN risk activates | Mitigation Type | Mitigation |
|---|-----------|------|----------|-------------------------------------|-----------------|------------|

Column rules:
- Severity: only HIGH, MEDIUM, or LOW — no numbers, percentages, or invented labels
- IF [condition], THEN risk activates: complete the template — every cell begins with "IF". A bare probability label ("high", "~30%", "possible") cannot satisfy the column header's template format.
- Mitigation Type: one of — Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation: one sentence — but only after fulfilling the type's required sub-fields (see below)

**Mitigation type contracts — required named outputs (not optional descriptions):**
- Spike — Unknown: [what is being resolved] / Time-box: [duration] — then write the action sentence
- Validate — Assumption: [what is being tested] / Method: [interviews / prototype / survey] — then write the action sentence
- Gate — Criterion: [what must be true to pass] — then write the action sentence
- Contract — Party: [who] / Commitment: [what is owed] — then write the action sentence
- Cut — Element: [what is removed] / Scope effect: [impact on delivery] — then write the action sentence
- Instrument — Metric: [name] / Alert threshold: [value or condition] — then write the action sentence

**Type contract rule:** A mitigation is only complete when its type's named sub-fields are filled in. A Spike without a named unknown and time-box is incomplete. A Gate without a named criterion is incomplete. No generic hedge ("monitor closely", "keep an eye on", "revisit later", "consider alternatives", "be careful", "evaluate options") can fulfill any type contract — replace on sight.

**Forbidden mitigation words — replace on sight:** "monitor closely", "keep an eye on", "revisit later", "consider alternatives", "be careful", "evaluate options".

Sort rows by severity descending.

**Step 2b: Type diversity gate (mandatory).**

After completing all rows, scan the Mitigation Type column and count distinct type class names.

- If fewer than 3 distinct type classes appear, the register has type-monoculture. The taxonomy exists to classify mitigation strategies — a register dominated by a single type is not classifying, it is labeling. Replace entries with different types until at least 3 distinct classes are represented.
- Replacing an entry means choosing a different type appropriate to that risk's nature, then fulfilling that type's sub-field contract.

**Step 3: Write the Risk Interdependencies section (mandatory, ≥3 pairs with FROM/TO labels).**

After the table, write this section with the exact heading:

## Risk Interdependencies

This section must contain at least 3 named compound-risk pairings. Format each as:

- If [Risk A: name it by title] materializes, [Risk B: name it by title] escalates from [CURRENT SEVERITY of Risk B] to [NEW SEVERITY] because [one-clause reason].

Enforcement rules:
- Do not embed interdependency notes inside table rows — this section is the only location.
- At least 3 named pairs are required. If you find fewer than 3 after reviewing all rows, your risks are not specific enough — revise Step 2 to make them more concrete, then return here.
- Both risks must be named by their exact title from the table. "If technical risks compound other risks" fails the naming requirement.
- Every pairing must state both the FROM severity (what Risk B is currently rated) and the TO severity (what it becomes). A pairing that says only "escalates to HIGH" without naming the current severity is incomplete.

**Step 4: Self-check.**

Before writing the artifact, verify each item:
- [ ] Inertia is row 0, before all Technical/Market/Compliance/Dependency/Timeline risks
- [ ] Every severity is only HIGH, MEDIUM, or LOW
- [ ] At least 3 dimensions covered
- [ ] Every likelihood cell in the table starts with "IF" — scan every row
- [ ] Every row has a named Mitigation Type from the approved list
- [ ] Every mitigation fulfills its type contract (named sub-fields filled in)
- [ ] No forbidden mitigation words in any entry
- [ ] Rows sorted high-to-low after inertia
- [ ] Mitigation Type column contains at least 3 distinct type class names
- [ ] ## Risk Interdependencies section exists with at least 3 explicitly named pairs
- [ ] Every interdependency pair states both FROM severity and TO severity

Fix any violation before proceeding.

**Step 5 (only if AMEND is in the prompt):**

AMEND: focus on [dimension] — keep inertia (row 0) and ## Risk Interdependencies section, drop all rows not matching [dimension]. Re-sort.
AMEND: adjust severity threshold to [level] — keep inertia (row 0) and ## Risk Interdependencies section, drop rows below [level]. Re-sort.

**Write artifact to:** simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-05 — Full Integration (R3 V-05 base + C-17 FROM/TO + C-18 diversity gate)

**Hypothesis**: R3 V-05 is the definitive integration — three-role decomposition, IF-THEN column header, type sub-field contracts, ≥3 interdependency pairs, 9-item self-check. Under v4 rubric it scores 105/110. Two targeted additions close the remaining gap: (1) upgrade STEP 3 pairing format from "escalates to [NEW]" to "escalates from [CURRENT] to [NEW]" with explicit enforcement that the origin severity is required (C-17 PASS); (2) add a type diversity check to STEP 2 requiring ≥3 distinct type classes appear across the full register, with repair instructions if the count falls short (C-18 PASS). The STEP 4 self-check gains two new items. Everything else in R3 V-05 is preserved intact. Expected: C-17 PASS (+2), C-18 PASS (+2) → score 109/110.

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

**Type diversity rule:** After completing all rows, scan the Mitigation Type column. Count distinct type class names. If fewer than 3 distinct classes appear, the register has type-monoculture — the taxonomy is labeling rather than classifying. Replace entries with different types appropriate to each risk's nature until at least 3 distinct type class names are present. Replacing means selecting a different type and fulfilling its sub-field contract.

**Forbidden mitigation text — replace on sight:** "monitor closely", "keep an eye on", "revisit later", "consider alternatives", "be careful", "evaluate options". These name no action and fulfill no type contract. If you draft one, replace it with a typed mitigation before continuing.

---

**STEP 3 — RISK INTERDEPENDENCIES (mandatory section, ≥3 pairs with FROM/TO labels)**

Write this section with the exact heading:

## Risk Interdependencies

List at least 3 compound-risk pairings. Each pairing must name both risks explicitly, state the full severity transition, and give a one-clause reason. Format:

- If [Risk A: name it by title] materializes, [Risk B: name it by title] escalates from [CURRENT SEVERITY of Risk B] to [NEW SEVERITY] because [one-clause reason].

Enforcement rules:
- Do not put interdependency notes inside individual table rows. This section is the only place they appear.
- Minimum 3 named pairs. If you find fewer than 3 after reviewing all rows, your risks are too generic — revise STEP 2 to make them more specific before returning here.
- "If technical risks compound other risks" is not a valid pairing. Both risks must be named by their exact title from the table.
- Every pairing must declare both the FROM severity (what Risk B is currently) and the TO severity (what it becomes). A pairing stating only "escalates to HIGH" without naming the origin severity is incomplete — the reader cannot assess the magnitude of the escalation without knowing where it starts.

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
- [ ] Mitigation Type column contains at least 3 distinct type class names
- [ ] ## Risk Interdependencies section exists with at least 3 explicitly named compound-risk pairs
- [ ] Every interdependency pair states both FROM severity and TO severity for the activated risk

Fix any violation before proceeding.

---

**STEP 5 — AMEND (if present in prompt)**

AMEND: focus on [dimension] — keep inertia (row 0) and the ## Risk Interdependencies section, remove all rows not matching [dimension]. Re-sort.
AMEND: adjust severity threshold to [level] — keep inertia (row 0) and the ## Risk Interdependencies section, remove rows below [level]. Re-sort.

---

Write artifact to: simulations/scout/risk/{topic}-risk-{date}.md
```

---

## Variation Summary (v4 rubric projection)

The v4 rubric adds 2 aspirational criteria (C-17/C-18) each worth 2 points. Max composite rises to 110. R3 V-05 under v4 rubric scores 105 — it passes C-09 through C-16 but fails C-17 (no FROM/TO) and C-18 (no diversity). R4 targets close both gaps.

| ID | Axes | New Mechanism | C-17 | C-18 | vs R3 V-05 | Score | Golden |
|----|------|---------------|------|------|------------|-------|--------|
| V-01 | Lifecycle | FROM/TO prose template (R3 V-01 base) | **PASS** | FAIL | +C-17 only | ~101 | YES |
| V-02 | Output format | Diversity gate after table (R3 V-02 base) | FAIL | **PASS** | +C-18 only | ~98 | YES |
| V-03 | Phrasing register | FROM/TO as table columns (R3 V-03 base) | **PASS** | FAIL | Structural vs prose C-17 | ~98 | YES |
| V-04 | Lifecycle + Output format | FROM/TO + diversity gate + C-15 fix (R3 V-04 base) | **PASS** | **PASS** | +C-17+C-18+C-15 | ~109 | YES |
| V-05 | Full integration | R3 V-05 + FROM/TO + diversity gate | **PASS** | **PASS** | Max attainable | **~109** | YES |

### Score calculations (v4 rubric, max 110)

- **Essential** (C-01–C-05): 60 pts, 5/5 pass on all R4 variations
- **Recommended** (C-06–C-08): 30 pts, 3/3 pass on all R4 variations
- **Aspirational** (C-09–C-18): 20 pts max, 2 pts each; C-10 always PARTIAL (1 pt)

| ID | Essential | Recommended | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | Composite |
|----|-----------|-------------|------|------|------|------|------|------|------|------|------|------|-----------|
| V-01 | 60 | 30 | 2 | 1 | 1 | 1 | 2 | 0 | 0 | 2 | **2** | 0 | **101** |
| V-02 | 60 | 30 | 0 | 1 | 1 | 2 | 0 | 2 | 0 | 0 | 0 | **2** | **98** |
| V-03 | 60 | 30 | 0 | 1 | 2 | 1 | 0 | 0 | 2 | 0 | **2** | 0 | **98** |
| V-04 | 60 | 30 | 2 | 1 | 2 | 2 | 2 | 2 | **2** | 2 | **2** | **2** | **109** |
| V-05 | 60 | 30 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | **2** | **2** | **109** |

### Rankings

1. **V-04 and V-05 — 109 (tie)** — Both reach the base-prompt ceiling under v4. C-10 PARTIAL (1 pt) remains irreducible without a live AMEND directive. V-04 is the minimal combination path (R3 V-04 + three targeted additions); V-05 is the structurally richer full-integration with role decomposition and inline type contract sub-fields. Both score 109.
2. **V-01 — 101** — Cleanest C-17 proof. Isolates FROM/TO prose template on R3 V-01 baseline. C-14/C-15/C-18 absent — deliberate single-axis isolation. 4 pts ahead of R3 V-01 (99).
3. **V-02 — 98** — C-18 type diversity gate proof. No interdependency section so C-13/C-16/C-17 fail. C-15 fails (type definitions present but not sub-field obligations in this base). 2 pts ahead of R3 V-02 (96).
4. **V-03 — 98** — C-17 via tabular notation proof. Separate From/To columns make both severity fields structurally explicit. No diversity gate so C-18 fails. C-14 absent (no IF-THEN template). Mechanism comparison with V-01: table columns vs prose template for FROM/TO enforcement.

### R4 Design Notes

**C-17: prose template vs. table columns (V-01 vs V-03)**
Two distinct mechanisms for enforcing the FROM/TO severity pair:
- V-01 adds the origin slot to the prose pairing template: "escalates from [CURRENT] to [NEW]." The model writes one prose sentence with two slots. Risk: the FROM slot could be collapsed ("escalates from MEDIUM to HIGH" → "escalates to HIGH" if the model pattern-matches to its prior training on this output style).
- V-03 uses a 5-column markdown table where "From Severity" and "To Severity" are separate columns. The model completes a table cell for each. Empty cells in a table are structurally visible — the model is more likely to fill each column than to fulfill a prose template slot it might elide.
The tabular approach (V-03) is the stronger structural enforcer of FROM/TO by the same logic that a table schema template (C-14) is stronger than a prose IF-THEN rule. R4 scoring will reveal whether this holds empirically.

**C-18: post-table repair gate mechanism**
V-02 and V-04/V-05 add a diversity gate after the table is complete. The gate is structural detection-and-repair: generate first, count, replace if short. This is analogous to C-11's read-back gate for generic mitigations in V-01/V-03's lineage. The gate does not prevent type-monoculture from being generated; it catches and repairs it. The threshold of 3 distinct classes is calibrated to a typical 5-7 entry register: 3 distinct types across 5-7 entries means the model must have applied taxonomy reasoning (not all unknowns get Spike, not all decisions get Gate).

**V-04 C-15 fix vs R3 V-04**
R3 V-04 left C-15 at PARTIAL because type definitions were provided but sub-fields were not declared as required named outputs. V-04 promotes the sub-field definitions to required outputs using the same wording as R3 V-05 that produced C-15 PASS: "A Spike without a named unknown and time-box is incomplete." This single promotion moves C-15 from PARTIAL (1) to PASS (2), contributing +1 to the composite (104 → 105 baseline before C-17/C-18 additions).

**C-10 ceiling unchanged at PARTIAL**
All five variations handle AMEND correctly via an AMEND step that retains inertia and the interdependencies section. No live AMEND directive exists in a base prompt — PARTIAL (1 pt) is the theoretical ceiling for C-10 on all base-prompt evaluations. Score ceiling without C-10 PASS remains 109 under v4 rubric.

```json
{"top_score": 109, "all_essential_pass": true, "gap_closed": ["C-17 (FROM/TO severity-transition labels on every interdependency pair)", "C-18 (>=3 distinct mitigation type classes in use)"], "mechanisms_tested": ["FROM/TO prose template upgrade in interdependency format (V-01)", "Post-table diversity gate: count distinct type classes, repair if <3 (V-02)", "FROM/TO as separate table columns in interdependency section (V-03)", "FROM/TO + diversity gate + C-15 sub-field promotion combined (V-04)", "Full integration: R3 V-05 base + FROM/TO + diversity gate (V-05)"], "ceiling_note": "C-10 PARTIAL (1pt) is irreducible on all base prompts — live AMEND directive required to demonstrate PASS. Theoretical max with C-10 PASS is 110."}
```
