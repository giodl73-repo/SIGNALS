All 5 variations written to `simulations/quest/variations/discover-competitors-alt-variations-R4-2026-03-17.md` (53KB, 112 structural element hits).

---

## discover-competitors-alt -- Variations R4

**Baseline:** R3 V-05 (140/140). All 18 criteria preserved in every variation.

**R4 question:** R3 V-05 satisfies all criteria through one specific structural arrangement. Do different structural arrangements satisfy the same criteria — or do some criteria couple tightly to their R3 form?

| Variation | Axis | Projected composite | Key test |
|-----------|------|--------------------:|----------|
| **V-01** | Role sequence (synthesis-first) | ~140 | Does pre-declaring synthesis contracts before Phase 3 tighten C-10/C-13/C-17 compliance? |
| **V-02** | Output format (tabular findings) | ~137.5 | Does a structured Anchor column with `Row C{N} + attribute: value` structurally prevent name-only anchoring without instructional prohibition? |
| **V-03** | Inertia framing (inertia as gravitational center) | ~137.5 | Does an INERTIA-REF token + per-finding inertia comparison clause deepen C-06 mechanism reasoning or produce formulaic additions? |
| **V-04** | Combined: role sequence + gate-first lifecycle | ~140 | Do standalone GATE sections with PASS/FAIL tables produce cleaner C-16 failure state naming than inline gate rules? |
| **V-05** | Combined: tabular findings + inertia + conversational register | ~135 | Can bolded failure state names embedded in conversational prose satisfy C-15/C-16, or does formal gate architecture matter? |

**Key structural choices by variation:**

- **V-01:** `[SYNTHESIS REQUIREMENTS]` block appears *before* Phase 2 — output contracts visible at data-gathering time. Phase 4 executes rather than re-specifies.
- **V-02:** Phase 4 is a findings table with `Anchor (Row C{N} + attribute: value)` as a structural column. Name-only entries fail the column shape itself.
- **V-03:** Mandatory `INERTIA BENCHMARK` step after Phase 3 produces `INERTIA-REF` token. Every finding closes with an inertia comparison clause citing the specific threat level and mechanism phrase.
- **V-04:** Three `GATE` sections between phases, each a PASS/FAIL table with named failure states (`citation gate failure`, `proof structure failure`, `anchor gate failure`, `whitespace gate failure`). Gates as isolated checkpoints rather than embedded rules.
- **V-05:** Steps 1–5 (conversational) replace Phases 1–5. All four failure state names appear bolded within natural-language instructions. Tests the register boundary for C-15/C-16.

**Sharpest interaction to score:** V-04 vs V-05 on C-16 — gate table vs conversational bold. If C-16 requires isolated gate architecture, V-05 scores PARTIAL. If inline bold naming satisfies "names the error condition explicitly," V-05 scores PASS.
ch gate carries: what passes, what the failure is named, and what to fix. Tests whether gate-as-section produces cleaner C-16 coverage than inline gate rules in phase bodies.

**V-05 load-bearing condition:** Conversational register throughout. Failure state names (citation gate failure, anchor gate failure, proof rerun failure, proof structure failure) appear in bold within natural-language instructions rather than in isolated gate declarations. Tests whether conversational embedding of failure states satisfies C-15/C-16 or whether the formal gate architecture is required.

### Projected composites

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| Essential (60) | 60 | 60 | 60 | 60 | 60 |
| Recommended (30) | 30 | 30 | 30 | 30 | 30 |
| Aspirational (50) | ~50 | ~47.5 | ~47.5 | ~50 | ~45 |
| **Composite** | ~**140** | ~**137.5** | ~**137.5** | ~**140** | ~**135** |

### Rubric coverage

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 AMEND proof validator | PASS | PASS | PASS | PASS | PASS |
| C-15 anchor tag before proof | PASS | PASS | PASS | PASS | PARTIAL? |
| C-16 gate failure naming | PASS | PASS | PASS | PASS | PARTIAL? |
| C-17 WHITESPACE by attribute absence | PASS | PASS | PASS | PASS | PASS |
| C-18 NOT ACCEPTABLE anchoring | PASS | PASS | PASS | PASS | PASS |

Key interactions to watch:
- **V-01 vs R3 V-05 on C-10** -- synthesis-first vs synthesis-last: does pre-declaring output contracts change finding groundedness?
- **V-02 vs V-03 on C-10** -- tabular anchoring (column-enforced) vs inertia-clause anchoring (rule-enforced): which produces more reliable compliance?
- **V-04 vs V-01 on C-16** -- gate-as-section table vs embedded gate rules: does isolated gate architecture produce cleaner failure state naming?
- **V-05 C-15/C-16** -- conversational register stress test: do failure state names embedded in natural language satisfy named-slot and gate-failure-naming requirements?


## test


---

## V-01 -- Role Sequence (Synthesis-First)

**Axis:** Synthesis output requirements declared after Phase 1, before data gathering. Phase 4 executes pre-declared contracts rather than re-specifying them inline.
**Hypothesis:** Declaring the WHITESPACE template, CROSS-DIMENSIONAL proof structure, and anchoring rules before Phase 3 forces the competitive map to collect the attributes each output needs. Tests whether requirements-first architecture tightens C-10 (table-stakes grounding), C-13 (claim-level anchors), and C-17 (attribute absence evidence) by making output contracts visible at data-gathering time.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If the user supplied `focus: market-sizing` or `focus: positioning-framework`, the focus dimension is active. If not, no focus column is added and focus-related criteria pass by vacuous satisfaction.

---

**[PHASE 1 -- CONTEXT]**

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer the topic. Do not ask.

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

**[SYNTHESIS REQUIREMENTS -- READ BEFORE BUILDING THE COMPETITIVE MAP]**

Phase 4 will produce three output types. Read these requirements now so Phase 3 collects the attributes each output needs.

**Output A -- WHITESPACE finding (required in every run)**

Template:
```
WHITESPACE: {gap label}
Absence evidence: Row C{N} -- {attribute column}: {absent or "None" / "N/A" / uncontested value}.
                  Row C{N} -- {attribute column}: {absent or uncontested value}.
                  [repeat for each relevant row]
Gap confirmed: No row provides a non-absent value for [{attribute column(s)}] -- attribute-level uncontested.
Actionability: {one sentence}
```

NOT ACCEPTABLE: "No competitor owns the [X] space." -- bare assertion; no attributes named, no rows cited.
NOT ACCEPTABLE: "None of the competitors address [X]." -- assertion without attribute-level evidence.

When building Phase 3: note which Mechanism and Focus-column cells are absent or show no relevant value. These become the absence evidence entries.

**Output B -- CROSS-DIMENSIONAL finding (required if FOCUS is active)**

```
CROSS-DIMENSIONAL: {gap statement}

SOURCE: {identify the specific competitor row(s) by number and the exact attribute(s) -- threat
level, mechanism phrase, or focus-column value -- that anchor this finding. Name the evidence
before constructing the proof. Do not proceed to REDUCTION-1 until this slot is filled.}

REDUCTION-1: Competitive map alone (focus dimension removed): {What does the table show without
the focus column? Does this gap appear?} -- NO. {What is lost when focus is removed.}
REDUCTION-2: Focus dimension alone (competitive map removed): {What does the focus analysis show
without the competitor rows? Does this gap appear?} -- NO. {What is lost when the map is removed.}

THEREFORE: This gap requires both inputs simultaneously. Neither alone is sufficient.
```

SOURCE must be filled before writing REDUCTION-1 or REDUCTION-2. Constructing either reduction before declaring the evidentiary source is a **proof structure failure**.

If either reduction answer cannot honestly be NO, find a different gap.

**Output C -- Claim-level anchoring for all findings**

Every finding must reference a specific attribute from a named competitor row:
- A specific threat level -- e.g., "Competitor 2's HIGH threat rating"
- A specific mechanism phrase -- e.g., "Competitor 0's mechanism: [exact phrase from mechanism column]"
- A specific offering claim -- e.g., "Competitor 1's core offering: [phrase from offering column]"
- A specific focus-column value -- e.g., "Competitor 3's [focus dimension]: [value from focus column]"

ACCEPTABLE: "Competitor 2's HIGH threat rating combined with its [focus-column value of X] reveals..."
NOT ACCEPTABLE: "Competitor 2 reveals that..." -- name-only anchoring; no specific attribute cited. This is the most common anchor failure.
NOT ACCEPTABLE: "As Competitor 1 demonstrates..." -- name-only anchor; same failure.

A finding anchored only by competitor name is an **anchor gate failure**. Free-floating and name-only-anchored findings are both prohibited.

---

**[PHASE 2 -- INERTIA ASSESSMENT]**

Assess the status quo before any external competitor.

```
Token: C0: {specific name of status quo behavior or tool -- not "status quo" or "inertia"}
```

- **Threat:** HIGH / MEDIUM / LOW
- **Mechanism:** one sentence -- name the specific switching cost, habit lock-in, or workaround satisfaction that explains this threat level. Not just "inertia is high."

If FOCUS is active: apply the focus dimension to Competitor 0 here, integrated with the assessment above -- not deferred to a later section.

```
Token: C0-ASSESS: Threat={level}, Mechanism={sentence}, Focus={note or N/A}
```

Print: `Phase 2 complete. C0: {name}. Threat: {level}.`

---

**[PHASE 3 -- EXTERNAL COMPETITORS]**

Build the competitive map. Competitor 0 from Phase 2 is the first row.

**Per-row citation gate:** Before writing any external competitor row (row 1 or higher), run WebSearch for that competitor. Paste the citation URL in the Citation column of that row. Do not write the row without it. An empty Citation cell is a **citation gate failure** -- do not proceed to Phase 4 until all Citation cells are filled. Placing citations in a footnote, endnote, or trailing references section is a **citation gate failure**: inline placement is required.

| Competitor | Core offering | Threat | Mechanism | {Focus if active} | Citation |
|---|---|---|---|---|---|
| **0. {C0 name}** | {current user behavior} | {level} | {mechanism from Phase 2} | {focus note if active} | -- |
| **1. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL -- required] |
| **2. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL -- required] |
| *(add rows as needed)* | | | | | |

Rules:
- Every external row must have a URL in Citation. Do not proceed to Phase 4 with any empty Citation cells.
- Threat must be HIGH, MEDIUM, or LOW for every row. No other values.
- If FOCUS is active, populate the focus column for every row including Row 0. Do not add a trailing section for focus content.
- Collect Mechanism and Focus-column values with Output A in mind: note which cells are absent or uncontested. These become the absence evidence for WHITESPACE.

Print: `Phase 3 complete. Competitors: {count}. All citations present: {yes/no}.`

---

**[PHASE 4 -- SYNTHESIS]**

Execute the three output types declared in the Synthesis Requirements above.

Write 3-5 findings total. Apply claim-level anchoring (Output C) to every finding. An **anchor gate failure** occurs when a finding is anchored only by competitor name -- catch and rewrite before proceeding.

**WHITESPACE finding:** Use the template from Output A. Fill the absence evidence block row by row using the absent values identified in Phase 3. Do not assert the gap.

If FOCUS is active: **CROSS-DIMENSIONAL finding:** Use the structure from Output B. Fill SOURCE before writing any reduction. Both reductions must answer NO with specific explanation of what each dimension loses without the other.

---

**[PHASE 5 -- AMEND]**

Exactly 3 adjustments:

1. **Shift focus** -- Change the FOCUS token. Add or replace the focus column in Phase 3 MAP for all rows. Rerun the full CROSS-DIMENSIONAL proof: first replace the SOURCE slot with the updated evidentiary basis for the new focus dimension, then rewrite REDUCTION-1 and REDUCTION-2 from scratch -- do not carry over reduction arguments from the previous proof. A standalone instruction to "update the finding" or to "update the CROSS-DIMENSIONAL conclusion" is a **proof rerun failure**: the explicit reconstruction of both single-dimension reduction arguments is required. State which rows and findings changed.
2. **Add competitor** -- Name the competitor. Add a Phase 3 row with all required fields. Run WebSearch and add the citation inline. Re-evaluate the WHITESPACE absence evidence: does the new row introduce a non-absent value for any attribute column supporting the gap? State whether WHITESPACE survives, narrows, or closes.
3. **Adjust depth** -- Specify `expand: HIGH` or `expand: {competitor number}`. For matching rows, add a sub-row: (a) the specific feature or behavior driving the threat rating, (b) the one move that would shift the rating down one level.

---

---

## V-02 -- Output Format (Tabular Findings)

**Axis:** Phase 4 findings rendered as a structured table with explicit Anchor and Evidence columns, extended by finding-specific blocks for WHITESPACE and CROSS-DIMENSIONAL.
**Hypothesis:** A findings table that structurally requires Row C{N} + attribute value in the Anchor column prevents name-only anchoring by architectural coercion rather than instructional prohibition. The column header "Anchor (Row C{N} + attribute: value)" makes a competitor name alone structurally incomplete -- the template shape rejects name-only entries without requiring the model to evaluate them. Tests whether format coercion eliminates anchor gate failures (C-13) and whether the structured absence column provides attribute-level evidence for C-17 without a separate instructional template.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If the user supplied `focus: market-sizing` or `focus: positioning-framework`, the focus dimension is active. If not, no focus column is added and focus-related criteria pass by vacuous satisfaction.

---

**[PHASE 1 -- CONTEXT]**

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer the topic. Do not ask.

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

**[PHASE 2 -- INERTIA ASSESSMENT]**

Assess the status quo before any external competitor.

```
Token: C0: {specific name of status quo behavior or tool -- not "status quo" or "inertia"}
```

- **Threat:** HIGH / MEDIUM / LOW
- **Mechanism:** one sentence -- name the specific switching cost, habit lock-in, or workaround satisfaction that explains this threat level. Not just "inertia is high."

If FOCUS is active: apply the focus dimension to Competitor 0 here, integrated with the assessment above -- not deferred to a later section.

```
Token: C0-ASSESS: Threat={level}, Mechanism={sentence}, Focus={note or N/A}
```

Print: `Phase 2 complete. C0: {name}. Threat: {level}.`

---

**[PHASE 3 -- EXTERNAL COMPETITORS]**

Build the competitive map. Competitor 0 from Phase 2 is the first row.

**Per-row citation gate:** Before writing any external competitor row (row 1 or higher), run WebSearch for that competitor. Paste the citation URL in the Citation column of that row. Do not write the row without it. An empty Citation cell is a **citation gate failure** -- do not proceed to Phase 4 until all Citation cells are filled. Placing citations in a footnote, endnote, or trailing references section is a **citation gate failure**: inline placement is required.

| Competitor | Core offering | Threat | Mechanism | {Focus if active} | Citation |
|---|---|---|---|---|---|
| **0. {C0 name}** | {current user behavior} | {level} | {mechanism from Phase 2} | {focus note if active} | -- |
| **1. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL -- required] |
| **2. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL -- required] |
| *(add rows as needed)* | | | | | |

Rules:
- Every external row must have a URL in Citation. Do not proceed to Phase 4 with any empty Citation cells.
- Threat must be HIGH, MEDIUM, or LOW for every row. No other values.
- If FOCUS is active, populate the focus column for every row including Row 0. Do not add a trailing section for focus content.

Print: `Phase 3 complete. Competitors: {count}. All citations present: {yes/no}.`

---

**[PHASE 4 -- SYNTHESIS]**

Write 3-5 findings using the findings table format below.

**Findings table column rules:**

- **Anchor** column: must contain `Row C{N}, {attribute name}: "{attribute value}"`. A competitor name alone is NOT ACCEPTABLE -- it is an **anchor gate failure**. NOT ACCEPTABLE: "Competitor 2" -- name-only; no attribute cited. NOT ACCEPTABLE: "Competitor 2 reveals that..." -- name-only anchor; the competitor name appears but no specific attribute is cited. ACCEPTABLE: "Row C2, Threat: HIGH" or "Row C0, Mechanism: [exact phrase from mechanism column]".
- **Evidence** column: quote the specific cell content that drives the finding -- the exact phrase from the mechanism column, the exact focus-column value, or the threat rating plus its row context.
- **Finding** column: the claim that follows from the named anchor and evidence.

| # | Type | Anchor (Row C{N} + attribute: value) | Evidence (quoted cell content) | Finding |
|---|------|--------------------------------------|-------------------------------|---------|
| F1 | GENERAL | Row C{N}, {attribute}: "{value}" | {quoted phrase from that cell} | {claim} |
| F2 | GENERAL | Row C{N}, {attribute}: "{value}" | {quoted phrase from that cell} | {claim} |
| ... | | | | |
| WS | WHITESPACE | [see absence block below] | [see absence block below] | {gap label} |
| XD | CROSS-DIMENSIONAL | [see proof block below] | [see proof block below] | {gap statement} |

*(Omit XD row if FOCUS is not active.)*

**WHITESPACE absence block** (follows the WS table row):

```
WHITESPACE: {gap label}
Absence evidence: Row C{N} -- {attribute column}: {absent or "None" / "N/A" / uncontested value}.
                  Row C{N} -- {attribute column}: {absent or uncontested value}.
                  [repeat for each relevant row]
Gap confirmed: No row provides a non-absent value for [{attribute column(s)}] -- attribute-level uncontested.
Actionability: {one sentence}
```

NOT ACCEPTABLE: "No competitor owns the [X] space." -- bare assertion; no attributes named, no rows cited.
NOT ACCEPTABLE: "None of the competitors address [X]." -- assertion without attribute-level evidence.
ACCEPTABLE: "Row C0 (Mechanism: 'email fragmentation'), Row C1 (Focus-column: 'N/A'), Row C2 (Mechanism: 'batch-only'): all three rows show absent or incompatible values in the [real-time collaborative] column. Gap confirmed by attribute-level absence, not asserted."

**CROSS-DIMENSIONAL proof block** (if FOCUS is active, follows the XD table row):

```
CROSS-DIMENSIONAL: {gap statement}

SOURCE: {identify the specific competitor row(s) by number and the exact attribute(s) -- threat
level, mechanism phrase, or focus-column value -- that anchor this finding. Name the evidence
before constructing the proof. Do not proceed to REDUCTION-1 until this slot is filled.}

REDUCTION-1: Competitive map alone (focus dimension removed): {What does the table show without
the focus column? Does this gap appear?} -- NO. {What is lost when focus is removed.}
REDUCTION-2: Focus dimension alone (competitive map removed): {What does the focus analysis show
without the competitor rows? Does this gap appear?} -- NO. {What is lost when the map is removed.}

THEREFORE: This gap requires both inputs simultaneously. Neither alone is sufficient.
```

Rule: SOURCE must be filled before REDUCTION-1 or REDUCTION-2. Constructing either reduction before declaring the evidentiary source is a **proof structure failure**.

If either reduction cannot honestly answer NO, find a different gap.

---

**[PHASE 5 -- AMEND]**

Exactly 3 adjustments:

1. **Shift focus** -- Change the FOCUS token. Add or replace the focus column in Phase 3 MAP for all rows. Rerun the full CROSS-DIMENSIONAL proof: first replace the SOURCE slot with the updated evidentiary basis for the new focus dimension, then rewrite REDUCTION-1 and REDUCTION-2 from scratch -- do not carry over reduction arguments from the previous proof. A standalone instruction to "update the finding" or to "update the CROSS-DIMENSIONAL conclusion" is a **proof rerun failure**: the explicit reconstruction of both single-dimension reduction arguments is required. State which rows and findings changed.
2. **Add competitor** -- Name the competitor. Add a Phase 3 row with all required fields. Run WebSearch and add the citation inline. Re-evaluate the WHITESPACE absence evidence: does the new row introduce a non-absent value for any attribute column supporting the gap? State whether WHITESPACE survives, narrows, or closes.
3. **Adjust depth** -- Specify `expand: HIGH` or `expand: {competitor number}`. For matching rows, add a sub-row: (a) the specific feature or behavior driving the threat rating, (b) the one move that would shift the rating down one level.

---

---

## V-03 -- Inertia Framing (Inertia as Gravitational Center)

**Axis:** Every finding benchmarks explicitly against C0's threat level and mechanism. Inertia is the reference frame for all synthesis, not just a first row in the table.
**Hypothesis:** R3 V-05 treats C0 as the first row of a symmetric competitive map. This variation makes C0 asymmetric: after Phase 3, a mandatory INERTIA BENCHMARK step extracts a reference sentence used by all findings. Every finding must include an inertia comparison clause ("this finding reinforces / challenges / contextualizes C0's [level] threat via [mechanism phrase]"). Tests whether inertia-anchored synthesis deepens C-06 mechanism reasoning, and whether the added inertia clause can satisfy C-12/C-15 cross-dimensional proof requirements without weakening them.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If the user supplied `focus: market-sizing` or `focus: positioning-framework`, the focus dimension is active. If not, no focus column is added and focus-related criteria pass by vacuous satisfaction.

---

**[PHASE 1 -- CONTEXT]**

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer the topic. Do not ask.

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

**[PHASE 2 -- INERTIA ASSESSMENT]**

Assess the status quo before any external competitor. The C0 assessment produced here is the gravitational center of the entire analysis -- every synthesis finding will reference it.

```
Token: C0: {specific name of status quo behavior or tool -- not "status quo" or "inertia"}
```

- **Threat:** HIGH / MEDIUM / LOW
- **Mechanism:** one sentence -- name the specific switching cost, habit lock-in, or workaround satisfaction that explains this threat level. Not just "inertia is high." The mechanism sentence must name the specific behavior or product feature causing the lock-in -- not a category label applied generically.

If FOCUS is active: apply the focus dimension to Competitor 0 here, integrated with the assessment above -- not deferred to a later section.

```
Token: C0-ASSESS: Threat={level}, Mechanism={sentence}, Focus={note or N/A}
```

Print: `Phase 2 complete. C0: {name}. Threat: {level}.`

---

**[PHASE 3 -- EXTERNAL COMPETITORS]**

Build the competitive map. Competitor 0 from Phase 2 is the first row.

**Per-row citation gate:** Before writing any external competitor row (row 1 or higher), run WebSearch for that competitor. Paste the citation URL in the Citation column of that row. Do not write the row without it. An empty Citation cell is a **citation gate failure** -- do not proceed to Phase 4 until all Citation cells are filled. Placing citations in a footnote, endnote, or trailing references section is a **citation gate failure**: inline placement is required.

| Competitor | Core offering | Threat | Mechanism | {Focus if active} | Citation |
|---|---|---|---|---|---|
| **0. {C0 name}** | {current user behavior} | {level} | {mechanism from Phase 2} | {focus note if active} | -- |
| **1. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL -- required] |
| **2. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL -- required] |
| *(add rows as needed)* | | | | | |

Rules:
- Every external row must have a URL in Citation. Do not proceed to Phase 4 with any empty Citation cells.
- Threat must be HIGH, MEDIUM, or LOW for every row. No other values.
- If FOCUS is active, populate the focus column for every row including Row 0. Do not add a trailing section for focus content.

Print: `Phase 3 complete. Competitors: {count}. All citations present: {yes/no}.`

---

**[INERTIA BENCHMARK]**

Before writing findings, produce the inertia reference sentence:

```
Token: INERTIA-REF: C0 ({name}) holds {threat level} threat via {mechanism phrase from Phase 2}. This is the reference baseline for all findings.
```

Every finding in Phase 4 must include an inertia comparison clause: one sentence stating whether this finding reinforces, challenges, or contextualizes C0's threat level or mechanism. The comparison must name the specific threat level and mechanism phrase from INERTIA-REF -- a generic reference to "inertia" without these specifics does not satisfy.

---

**[PHASE 4 -- SYNTHESIS]**

Write 3-5 findings.

**Claim-level anchoring rule -- applies to every finding:**

Each finding must reference a specific attribute from a named competitor row. Qualifying attributes:
- A specific threat level -- e.g., "Competitor 2's HIGH threat rating"
- A specific mechanism phrase -- e.g., "Competitor 0's mechanism: [exact phrase from mechanism column]"
- A specific offering claim -- e.g., "Competitor 1's core offering: [phrase from offering column]"
- A specific focus-column value -- e.g., "Competitor 3's [focus dimension]: [value from focus column]"

ACCEPTABLE: "Competitor 2's HIGH threat rating combined with its [focus-column value of X] reveals..."
ACCEPTABLE: "The MEDIUM threat of Competitor 1 (mechanism: [phrase from mechanism cell]) implies the gap at..."
NOT ACCEPTABLE: "Competitor 2 reveals that..." -- this is name-only anchoring. The competitor name appears but no specific attribute from that row is cited. This is the most common anchor failure.
NOT ACCEPTABLE: "As Competitor 1 demonstrates..." -- name-only anchor; same failure.

A finding anchored only by competitor name is an **anchor gate failure**. Free-floating findings and name-only-anchored findings are both prohibited.

After each finding, add the inertia comparison clause: "Inertia relation: [this finding reinforces / challenges / contextualizes] C0's [{level}] threat via [{mechanism phrase from INERTIA-REF}]." A generic reference to "inertia" without the specific threat level and mechanism phrase does not satisfy.

Required findings:

**WHITESPACE: {gap label}**

Ground the gap by naming which specific attributes across which competitor rows are absent or uncontested -- do not assert the gap without attribute-level evidence.

Template:
```
WHITESPACE: {gap label}
Absence evidence: Row C{N} -- {attribute column}: {absent or "None" / "N/A" / uncontested value}.
                  Row C{N} -- {attribute column}: {absent or uncontested value}.
                  [repeat for each relevant row, including C0]
Gap confirmed: No row provides a non-absent value for [{attribute column(s)}] -- attribute-level uncontested.
C0 position: C0 ({name}) {occupies / partially occupies / does not occupy} this space -- {cite the C0 Mechanism or Focus-column value that determines this}.
Actionability: {one sentence}
```

NOT ACCEPTABLE: "No competitor owns the [X] space." -- bare assertion; no attributes named, no rows cited.
NOT ACCEPTABLE: "None of the competitors address [X]." -- assertion without attribute-level evidence.
ACCEPTABLE: "Row C0 (Mechanism: 'email fragmentation'), Row C1 (Focus-column: 'N/A'), Row C2 (Mechanism: 'batch-only'): all three rows show absent or incompatible values in the [real-time collaborative] column. Gap confirmed by attribute-level absence, not asserted."

If FOCUS is active: produce a **CROSS-DIMENSIONAL** finding using this proof structure exactly:

```
CROSS-DIMENSIONAL: {gap statement}

SOURCE: {identify the specific competitor row(s) by number and the exact attribute(s) -- threat
level, mechanism phrase, or focus-column value -- that anchor this finding. Name the evidence
before constructing the proof. Do not proceed to REDUCTION-1 until this slot is filled.}

REDUCTION-1: Competitive map alone (focus dimension removed): {What does the table show without
the focus column? Does this gap appear?} -- NO. {What is lost when focus is removed.}
REDUCTION-2: Focus dimension alone (competitive map removed): {What does the focus analysis show
without the competitor rows? Does this gap appear?} -- NO. {What is lost when the map is removed.}

THEREFORE: This gap requires both inputs simultaneously. Neither alone is sufficient.
Inertia relation: [this finding reinforces / challenges / contextualizes] C0's [{level}] threat via [{mechanism phrase from INERTIA-REF}].
```

Rule: SOURCE must be filled before REDUCTION-1 or REDUCTION-2. Constructing either reduction before declaring the evidentiary source is a **proof structure failure**.

If either reduction answer cannot honestly be NO, find a different gap.

---

**[PHASE 5 -- AMEND]**

Exactly 3 adjustments:

1. **Shift focus** -- Change the FOCUS token. Add or replace the focus column in Phase 3 MAP for all rows. Rerun the full CROSS-DIMENSIONAL proof: first replace the SOURCE slot with the updated evidentiary basis for the new focus dimension, then rewrite REDUCTION-1 and REDUCTION-2 from scratch -- do not carry over reduction arguments from the previous proof. A standalone instruction to "update the finding" or to "update the CROSS-DIMENSIONAL conclusion" is a **proof rerun failure**: the explicit reconstruction of both single-dimension reduction arguments is required. Update the inertia comparison clause for the new focus. State which rows and findings changed.
2. **Add competitor** -- Name the competitor. Add a Phase 3 row with all required fields. Run WebSearch and add the citation inline. Re-evaluate the WHITESPACE absence evidence: does the new row introduce a non-absent value for any attribute column supporting the gap? Update the C0 position sentence if the gap narrows toward or away from C0. State whether WHITESPACE survives, narrows, or closes.
3. **Adjust depth** -- Specify `expand: HIGH` or `expand: {competitor number}`. For matching rows, add a sub-row: (a) the specific feature or behavior driving the threat rating, (b) the one move that would shift the rating down one level.

---

---

## V-04 -- Combined: Role Sequence + Gate-First Lifecycle Emphasis

**Axes:** Synthesis declared before Phase 3 (role sequence) + gates elevated to standalone GATE sections with explicit PASS/FAIL tables between phases (lifecycle emphasis).
**Hypothesis:** Combining synthesis-first contracts with gate-as-section architecture produces two complementary improvements: front-loaded requirements tighten data collection, and standalone gate sections make failure states maximally visible as checkpoints. Tests whether gate-as-section architecture produces cleaner C-16 coverage (failure state naming) than inline gate rules embedded in phase bodies, and whether the two structural changes compound cleanly or create redundancy.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If the user supplied `focus: market-sizing` or `focus: positioning-framework`, the focus dimension is active. If not, no focus column is added and focus-related criteria pass by vacuous satisfaction.

---

**[PHASE 1 -- CONTEXT]**

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer the topic. Do not ask.

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

**[SYNTHESIS REQUIREMENTS -- READ BEFORE BUILDING THE COMPETITIVE MAP]**

Phase 4 will require these output types. Read them now so Phase 3 collects the needed attributes.

**Output A -- WHITESPACE finding**

```
WHITESPACE: {gap label}
Absence evidence: Row C{N} -- {attribute column}: {absent or "None" / "N/A" / uncontested value}.
                  Row C{N} -- {attribute column}: {absent or uncontested value}.
                  [repeat for each relevant row]
Gap confirmed: No row provides a non-absent value for [{attribute column(s)}] -- attribute-level uncontested.
Actionability: {one sentence}
```

NOT ACCEPTABLE: "No competitor owns the [X] space." -- bare assertion; no attributes or rows cited.
NOT ACCEPTABLE: "None of the competitors address [X]." -- assertion without attribute-level evidence.

**Output B -- CROSS-DIMENSIONAL finding (if FOCUS active)**

```
CROSS-DIMENSIONAL: {gap statement}

SOURCE: {specific row(s) by number and exact attribute(s) -- declare before any reduction.
Do not proceed to REDUCTION-1 until this slot is filled.}

REDUCTION-1: Competitive map alone (focus removed): {gap present?} -- NO. {What focus information is lost.}
REDUCTION-2: Focus alone (map removed): {gap present?} -- NO. {What map information is lost.}

THEREFORE: Both inputs required. Neither alone sufficient.
```

SOURCE declared before REDUCTION-1/2. Constructing a reduction before naming its evidentiary source is a **proof structure failure**.

**Output C -- Claim-level anchoring**

Every finding anchors on a specific row attribute (threat level, mechanism phrase, offering, focus-column value).

NOT ACCEPTABLE: "Competitor 2 reveals that..." -- name-only anchoring; no specific attribute cited. This is the most common anchor failure.
NOT ACCEPTABLE: "As Competitor 1 demonstrates..." -- name-only anchor; same failure.

A finding anchored only by competitor name is an **anchor gate failure**.

---

**[PHASE 2 -- INERTIA ASSESSMENT]**

Assess the status quo before any external competitor.

```
Token: C0: {specific name of status quo behavior or tool -- not "status quo" or "inertia"}
```

- **Threat:** HIGH / MEDIUM / LOW
- **Mechanism:** one sentence -- name the specific switching cost, habit lock-in, or workaround satisfaction. Not just "inertia is high."

If FOCUS is active: apply focus to Competitor 0 here, integrated with the assessment above.

```
Token: C0-ASSESS: Threat={level}, Mechanism={sentence}, Focus={note or N/A}
```

Print: `Phase 2 complete. C0: {name}. Threat: {level}.`

---

**[GATE 1 -- INERTIA GATE]**

Before proceeding to Phase 3:

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 name specificity | C0 names a specific behavior or tool (not "status quo" or "inertia") | **inertia naming failure** -- revise C0 token |
| Threat level declared | Threat is exactly HIGH, MEDIUM, or LOW | **inertia threat failure** -- add threat level |
| Mechanism specificity | Mechanism names a specific cost, lock-in type, or workaround -- not a category label | **inertia mechanism failure** -- rewrite mechanism |

Do not proceed to Phase 3 if any check shows a failure state.

Print: `Gate 1 passed. Proceeding to Phase 3.`

---

**[PHASE 3 -- EXTERNAL COMPETITORS]**

Build the competitive map. Competitor 0 from Phase 2 is the first row.

Run WebSearch for each external competitor before writing its row. Paste the citation URL inline in the Citation column.

| Competitor | Core offering | Threat | Mechanism | {Focus if active} | Citation |
|---|---|---|---|---|---|
| **0. {C0 name}** | {current user behavior} | {level} | {mechanism from Phase 2} | {focus note if active} | -- |
| **1. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL -- required] |
| **2. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL -- required] |
| *(add rows as needed)* | | | | | |

Rules:
- Threat must be HIGH, MEDIUM, or LOW for every row. No other values.
- If FOCUS is active, populate the focus column for every row including Row 0. Do not add a trailing section for focus content.
- Collect Mechanism and Focus-column cells with Output A in mind: note which cells are absent or uncontested. These become the absence evidence for WHITESPACE.

Print: `Phase 3 complete. Competitors: {count}. All citations present: {yes/no}.`

---

**[GATE 2 -- CITATION GATE]**

Before proceeding to Phase 4:

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| All Citation cells filled | Every external row (row 1+) has a URL in Citation | **citation gate failure** -- run WebSearch and fill missing cells |
| Citations inline | All URLs appear within the row, not in footnotes or trailing sections | **citation gate failure** -- move citations inline |
| All Threat levels present | Every row has HIGH, MEDIUM, or LOW | **threat gate failure** -- add missing threat levels |

Do not proceed to Phase 4 if any check shows a failure state.

Print: `Gate 2 passed. Proceeding to Phase 4.`

---

**[PHASE 4 -- SYNTHESIS]**

Execute the three output types from the Synthesis Requirements block. Write 3-5 findings total.

Apply claim-level anchoring (Output C) to every finding. Catch any **anchor gate failure** (name-only anchor) and rewrite before Phase 5.

**WHITESPACE finding:** Use Output A template. Fill absence evidence row by row using absent values identified in Phase 3. Do not assert the gap.

If FOCUS is active: **CROSS-DIMENSIONAL finding:** Use Output B structure. Fill SOURCE before any reduction. Both reductions must answer NO with specific explanation.

Print: `Phase 4 complete. Findings: {count}. WHITESPACE present: yes. CROSS-DIMENSIONAL present: {yes/no}.`

---

**[GATE 3 -- SYNTHESIS GATE]**

Before proceeding to Phase 5:

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| No free-floating findings | Every finding references a named competitor row by attribute | **anchor gate failure** -- rewrite unanchored findings |
| No name-only anchors | No finding uses only a competitor name as its evidential basis | **anchor gate failure** -- add specific attribute citation |
| WHITESPACE has absence evidence | WHITESPACE block contains Row C{N} absence entries, not bare assertion | **whitespace gate failure** -- add row-by-row absence evidence |
| SOURCE declared before reductions | CROSS-DIMENSIONAL proof begins with SOURCE slot before REDUCTION-1 | **proof structure failure** -- move SOURCE before reductions |
| Both reductions answer NO | REDUCTION-1 and REDUCTION-2 both resolve to NO with explanation | **proof structure failure** -- find a different gap or complete the reduction |

Do not proceed to Phase 5 if any check shows a failure state.

Print: `Gate 3 passed. Proceeding to Phase 5.`

---

**[PHASE 5 -- AMEND]**

Exactly 3 adjustments:

1. **Shift focus** -- Change the FOCUS token. Add or replace the focus column in Phase 3 MAP for all rows. Rerun the full CROSS-DIMENSIONAL proof: first replace the SOURCE slot with the updated evidentiary basis for the new focus dimension, then rewrite REDUCTION-1 and REDUCTION-2 from scratch -- do not carry over reduction arguments from the previous proof. A standalone instruction to "update the finding" or to "update the CROSS-DIMENSIONAL conclusion" is a **proof rerun failure**: the explicit reconstruction of both single-dimension reduction arguments is required. State which rows and findings changed.
2. **Add competitor** -- Name the competitor. Add a Phase 3 row with all required fields. Run WebSearch and add the citation inline. Re-evaluate the WHITESPACE absence evidence: does the new row introduce a non-absent value for any attribute column supporting the gap? State whether WHITESPACE survives, narrows, or closes.
3. **Adjust depth** -- Specify `expand: HIGH` or `expand: {competitor number}`. For matching rows, add a sub-row: (a) the specific feature or behavior driving the threat rating, (b) the one move that would shift the rating down one level.

---

---

## V-05 -- Combined: Tabular Findings + Inertia Framing + Conversational Register

**Axes:** Tabular findings format (V-02) + inertia as gravitational center (V-03) + conversational phrasing register throughout.
**Hypothesis:** A conversational register ("when you write each finding...") can maintain structural precision while being more natural to execute. The register shift is the risk: failure state names (anchor gate failure, proof structure failure, citation gate failure, proof rerun failure) may lose their precision signal when embedded in conversational prose rather than declared in isolated gate instructions. If C-15/C-16 score PARTIAL, the conversational register cannot substitute for formal gate naming -- the failure state must be explicitly labeled, not just described.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If the user supplied `focus: market-sizing` or `focus: positioning-framework`, the focus dimension is active. If not, no focus column is added and focus-related criteria pass by vacuous satisfaction.

---

**Start by reading the repo context** -- README, CLAUDE.md, package.json, or whatever describes this project. Infer the topic from what you find. Don't ask the user to name it.

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

**Step 1 -- Assess the status quo first**

Before you look at any external tool or competitor, name and assess the current user behavior -- what the user is already doing today.

Give it a real name (not "status quo" or "inertia" -- those are category labels, not names). Assign a threat level: HIGH, MEDIUM, or LOW. Then write one sentence on the mechanism: what specific habit, switching cost, or workaround satisfaction keeps the user here? Don't write "inertia is high" -- name the specific feature or behavior that produces the stickiness.

```
Token: C0: {specific name}
Token: C0-ASSESS: Threat={level}, Mechanism={sentence}, Focus={note or N/A}
```

If FOCUS is active, fold the focus dimension into this assessment inline -- don't defer it.

When you're done: `Step 1 complete. C0: {name}. Threat: {level}.`

---

**Step 2 -- Build the competitive map**

Add external competitors after C0. Before writing any external row, run a WebSearch for that competitor and paste the result URL directly in the Citation cell. If you don't have a URL, don't write the row -- an empty Citation cell is a **citation gate failure** and the table isn't ready for synthesis until every cell is filled. URLs go in the row itself, not in a footnote or trailing references section -- placing them there is also a **citation gate failure**.

| Competitor | Core offering | Threat | Mechanism | {Focus if active} | Citation |
|---|---|---|---|---|---|
| **0. {C0 name}** | {current behavior} | {level} | {mechanism from Step 1} | {focus note if active} | -- |
| **1. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL -- required] |
| **2. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL -- required] |
| *(add rows as needed)* | | | | | |

Give every row a threat level (HIGH, MEDIUM, or LOW -- no other values). If FOCUS is active, fill the focus column for every row including C0.

Before you move to synthesis: `Step 2 complete. Competitors: {count}. All citations present: {yes/no}.`

---

**Step 3 -- Produce an inertia reference sentence**

Extract one sentence from Step 1 that will anchor all findings:

```
Token: INERTIA-REF: C0 ({name}) holds {threat level} threat via {mechanism phrase from Step 1}.
```

Every finding you write in Step 4 should say something concrete about how it relates to this sentence -- whether it reinforces the inertia case, challenges it, or puts a boundary around it. Use the specific threat level and mechanism phrase -- a generic reference to "inertia" doesn't count.

---

**Step 4 -- Write findings**

Write 3-5 findings using the table below, then expand WHITESPACE and CROSS-DIMENSIONAL with their structured blocks.

When you write each finding, start from a specific cell in the competitive map -- a threat rating, a mechanism phrase, an offering description, or a focus-column value from a named row. That cell is your anchor. Don't write "Competitor 2 reveals that..." -- that's name-only anchoring and it's an **anchor gate failure**: you've named the competitor but haven't cited which attribute from that row supports your claim. Cite the specific attribute: "Competitor 2's HIGH threat rating" or "Competitor 2's mechanism: [exact phrase]". "As Competitor 1 demonstrates..." is the same failure -- name-only anchor.

| # | Type | Anchor (Row C{N} + attribute: value) | Evidence (quoted cell content) | Finding |
|---|------|--------------------------------------|-------------------------------|---------|
| F1 | GENERAL | Row C{N}, {attribute}: "{value}" | {exact phrase from that cell} | {claim that follows} |
| F2 | GENERAL | Row C{N}, {attribute}: "{value}" | {exact phrase from that cell} | {claim that follows} |
| ... | | | | |
| WS | WHITESPACE | [absence block below] | [absence block below] | {gap label} |
| XD | CROSS-DIMENSIONAL | [proof block below] | [proof block below] | {gap statement} |

*(Omit XD row if FOCUS is not active.)*

After each finding, add an inertia comparison clause: one sentence on whether this finding reinforces, challenges, or contextualizes C0's threat level or mechanism. Use the specific threat level and mechanism phrase from INERTIA-REF.

**WHITESPACE absence block:**

```
WHITESPACE: {gap label}
Absence evidence: Row C{N} -- {attribute column}: {absent or "None" / "N/A" / uncontested value}.
                  Row C{N} -- {attribute column}: {absent or uncontested value}.
                  [repeat for each relevant row]
Gap confirmed: No row provides a non-absent value for [{attribute column(s)}] -- attribute-level uncontested.
C0 position: C0 ({name}) {occupies / partially occupies / does not occupy} this space -- {cite the C0 Mechanism or Focus-column value that determines this}.
Actionability: {one sentence}
```

Don't just say "no competitor owns this space" -- that's a bare assertion and it's not verifiable from the table. Show which attributes are absent or uncontested across which rows. NOT ACCEPTABLE: "No competitor owns the [X] space." -- bare assertion; no attributes or rows cited. NOT ACCEPTABLE: "None of the competitors address [X]." -- same failure. ACCEPTABLE: "Row C0 (Mechanism: 'email fragmentation'), Row C1 (Focus-column: 'N/A'), Row C2 (Mechanism: 'batch-only'): all three rows show absent or incompatible values in the [real-time collaborative] column. Gap confirmed by attribute-level absence."

**CROSS-DIMENSIONAL proof block** (if FOCUS is active):

```
CROSS-DIMENSIONAL: {gap statement}

SOURCE: {name the specific row(s) and the exact attribute(s) -- threat level, mechanism phrase, or
focus-column value -- that this finding depends on. Write this before you write anything else in
this block. If you cannot name a specific attribute here, you do not have a cross-dimensional
finding yet. Do not proceed to REDUCTION-1 until SOURCE is filled -- constructing a reduction
before naming its evidence is a proof structure failure.}

REDUCTION-1: Competitive map alone (focus removed): {What does the table show without the focus
column? Does this gap appear?} -- NO. {What information from the focus dimension is required --
what is lost when focus is removed.}
REDUCTION-2: Focus alone (map removed): {What does the focus analysis show without the competitor
rows? Does this gap appear?} -- NO. {What information from the competitive map is required --
what is lost when the map is removed.}

THEREFORE: This gap requires both inputs. Neither alone is sufficient.
Inertia relation: [reinforces / challenges / contextualizes] C0's {level} threat via {mechanism phrase from INERTIA-REF}.
```

If you cannot get REDUCTION-1 and REDUCTION-2 to honestly answer NO, find a different gap. Don't claim cross-dimensionality before running both reductions.

---

**Step 5 -- AMEND**

Exactly 3 adjustments:

1. **Shift focus** -- Change the FOCUS token. Update the focus column in the competitive map for all rows. Rerun the CROSS-DIMENSIONAL proof from scratch: replace the SOURCE slot first, then rewrite both REDUCTION-1 and REDUCTION-2 for the new focus dimension. Don't carry over the old reduction arguments -- that is a **proof rerun failure**. Saying "update the finding" without rewriting both reductions is also a **proof rerun failure**: the reconstruction of both single-dimension reduction arguments is what makes the proof valid, not just a new conclusion. Update the inertia comparison clause. State which rows and findings changed.
2. **Add competitor** -- Name the competitor. Add a competitive map row with all fields. Run WebSearch and add the citation inline. Check whether the new row adds a non-absent value to any attribute column the WHITESPACE finding depends on. Update C0 position if the gap changes. State whether WHITESPACE survives, narrows, or closes.
3. **Adjust depth** -- Specify `expand: HIGH` or `expand: {competitor number}`. For matching rows, add a sub-row: (a) the specific feature or behavior driving the threat rating, (b) the one move that would shift the rating down one level.

---

---

## Rubric Coverage Projection

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 inertia assessed first | PASS | PASS | PASS | PASS | PASS |
| C-02 focus woven not appended | PASS | PASS | PASS | PASS | PASS |
| C-03 threat level per competitor | PASS | PASS | PASS | PASS | PASS |
| C-04 whitespace identified | PASS | PASS | PASS | PASS | PASS |
| C-05 auto-detect without prompting | PASS | PASS | PASS | PASS | PASS |
| C-06 inertia stickiness reasoning | PASS | PASS | PASS | PASS | PASS |
| C-07 web-verified competitive claim | PASS | PASS | PASS | PASS | PASS |
| C-08 AMEND 3 actionable adjustments | PASS | PASS | PASS | PASS | PASS |
| C-09 cross-dimensional whitespace | PASS | PASS | PASS | PASS | PASS |
| C-10 table-stakes grounding per finding | PASS | PASS | PASS | PASS | PASS |
| C-11 fully-cited competitor table | PASS | PASS | PASS | PASS | PASS |
| C-12 self-negating cross-dimensional | PASS | PASS | PASS | PASS | PASS |
| C-13 claim-level finding anchors | PASS | PASS | PASS | PASS | PASS |
| C-14 AMEND proof validator | PASS | PASS | PASS | PASS | PASS |
| C-15 anchor tag before proof | PASS | PASS | PASS | PASS | PARTIAL? |
| C-16 gate failure naming | PASS | PASS | PASS | PASS | PARTIAL? |
| C-17 WHITESPACE by attribute absence | PASS | PASS | PASS | PASS | PASS |
| C-18 NOT ACCEPTABLE anchoring example | PASS | PASS | PASS | PASS | PASS |

Notes on V-05 PARTIAL projections:
- V-05 C-15: The SOURCE: slot is present and labeled before REDUCTION-1/2. The conversational instruction ("Write this before you write anything else in this block...Do not proceed to REDUCTION-1 until SOURCE is filled") names the slot. However, the failure state ("proof structure failure") appears embedded in conversational parenthetical rather than as an isolated gate rule. The named slot requirement should PASS; the failure-state-in-natural-language may yield PARTIAL on C-16 spillover.
- V-05 C-16: All four failure states are present and bolded (citation gate failure, anchor gate failure, proof rerun failure, proof structure failure) within conversational instructions. The rubric requires naming the error state -- these are named, but embedded in prose rather than in gate declarations. If C-16 requires isolated gate architecture (failure state named as a labeled block), V-05 scores PARTIAL. If inline bold naming satisfies, V-05 scores PASS.

Key interactions to watch in scoring:
- **V-01 vs R3 V-05 on C-10** -- synthesis-first vs synthesis-last: does pre-declaring output contracts change finding groundedness or is C-10 invariant to instruction placement?
- **V-02 vs V-03 on C-10** -- tabular column-enforced anchoring vs inertia-clause rule-enforced anchoring: which produces more reliable compliance under adversarial completion?
- **V-04 vs V-01 on C-16** -- gate-as-section table (V-04) vs embedded gate rules in phase bodies (V-01): does isolated gate architecture produce cleaner failure state naming?
- **V-04 vs R3 V-05 on C-16** -- does the gate table format strengthen C-16 coverage compared to R3 V-05's inline gate rules, given that R3 V-05 already scored PASS on C-16?
- **V-05 register shift on C-14/C-15/C-16** -- conversational failure state naming: does bolded inline naming satisfy the rubric's "names the error condition explicitly" requirement, or does the formal gate declaration architecture matter?
- **V-03 inertia clause on C-06** -- does requiring a specific "inertia comparison clause" per finding deepen mechanism reasoning or produce formulaic additions?
