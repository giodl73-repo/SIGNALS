Written to `simulations/quest/variations/discover-competitors-alt-variations-R3-2026-03-17.md`.

---

## discover-competitors-alt — Variations R3

Five complete prompt bodies. Baseline is R2 V-05. All R2 excellence patterns preserved in every variation.

### Variation axes

| Variation | Axis | R3 criteria targeted |
|-----------|------|----------------------|
| **V-01** | Gate failure naming + AMEND proof rerun prescription | C-14, C-16 |
| **V-02** | Inline anchor tag before proof block (SOURCE: slot) | C-15 |
| **V-03** | WHITESPACE grounded by attribute absence + NOT ACCEPTABLE anchoring example | C-17, C-18 |
| **V-04** | Combined: C-14 + C-15 + C-16 | C-14, C-15, C-16 |
| **V-05** | Combined: All 5 new R3 criteria | C-14, C-15, C-16, C-17, C-18 |

### Key structural decisions

**C-14 load-bearing condition:** AMEND item 1 must name `proof rerun failure` and explicitly prohibit "update the finding" as insufficient. R2 V-05 said "rerun both proofs" but never named the failure state or the forbidden shortcut.

**C-15 load-bearing condition:** A `SOURCE:` slot as the *first element* of the CROSS-DIMENSIONAL block, before REDUCTION-1/2. R2 V-05 named evidence incidentally inside argument text — evidence was discovered during the proof, not declared before it.

**C-16 load-bearing condition:** Every gate instruction names its failure state explicitly — `citation gate failure`, `anchor gate failure`, `proof structure failure`. R2 V-05 used positive framing only ("do not proceed").

**C-17 load-bearing condition:** WHITESPACE gets a dedicated attribute-absence template (Row C{N} — {column}: {absent value}) plus NOT ACCEPTABLE bare-assertion examples. R2 V-05 said "reference attributes" but still allowed the assertion form.

**C-18 load-bearing condition:** NOT ACCEPTABLE example must name the exact inadequate pattern — "Competitor X reveals that..." The R2 baseline already had this in the anchoring block; V-03/V-05 strengthen the WHITESPACE variant.

### Projected composites

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| Essential (60) | 60 | 60 | 60 | 60 | 60 |
| Recommended (30) | 30 | 30 | 30 | 30 | 30 |
| Aspirational (50) | ~35 | ~35 | ~35 | ~42.5 | ~50 |
| **Composite** | ~**125** | ~**125** | ~**125** | ~**132** | ~**140** |

### Rubric coverage

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 AMEND proof validator | **PASS** | PARTIAL | PARTIAL | **PASS** | **PASS** |
| C-15 anchor tag before proof | PARTIAL | **PASS** | PARTIAL | **PASS** | **PASS** |
| C-16 gate failure naming | **PASS** | PARTIAL | PARTIAL | **PASS** | **PASS** |
| C-17 WHITESPACE by attribute absence | PARTIAL | PARTIAL | **PASS** | PARTIAL | **PASS** |
| C-18 NOT ACCEPTABLE anchoring | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |

Key interactions to watch:
- **V-01 vs V-02 on C-15** — isolates whether C-15 needs structural proof template change vs instructional amendment
- **V-03 vs V-04 on C-17** — isolates whether C-17 propagates from claim-level anchoring rules or needs its own WHITESPACE template
- **V-04 vs V-05 on C-17** — confirms whether dedicated attribute-absence template is required even with full C-14/C-15/C-16 coverage
r all gate instructions + AMEND prescribes full reduction rerun on focus shift
**Hypothesis:** Adding explicit failure state names ("citation gate failure", "anchor gate failure", "proof rerun failure") to all gate instructions, and requiring AMEND item 1 to prescribe re-execution of both reduction arguments (not just "update the finding"), produces C-14 and C-16 without requiring structural changes to the proof block format. Tests whether C-14 and C-16 can be satisfied through instructional amendments to existing R2 V-05 structure.

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

**Per-row citation gate:** Before writing any external competitor row (row 1 or higher), run WebSearch for that competitor. Paste the citation URL in the Citation column of that row. Do not write the row without it. An empty Citation cell is a **citation gate failure** -- do not proceed to Phase 4 until all Citation cells are filled. Placing citations in a footnote or trailing references section is a **citation gate failure**: inline placement is required.

| Competitor | Core offering | Threat | Mechanism | {Focus if active} | Citation |
|---|---|---|---|---|---|
| **0. {C0 name}** | {current user behavior} | {level} | {mechanism from Phase 2} | {focus note if active} | -- |
| **1. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL -- required] |
| **2. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL -- required] |
| *(add rows as needed)* | | | | | |

Rules:
- Every external row must have a URL in Citation. Do not proceed to the next row without filling Citation. Do not proceed to Phase 4 with any empty Citation cells.
- Threat must be HIGH, MEDIUM, or LOW for every row. No other values.
- If FOCUS is active, populate the focus column for every row including Row 0. Do not add a trailing section for focus content.

Print: `Phase 3 complete. Competitors: {count}. All citations present: {yes/no}.`

---

**[PHASE 4 -- SYNTHESIS]**

Write 3-5 findings.

**Claim-level anchoring rule -- applies to every finding:**

Each finding must reference a specific attribute from a named competitor row. Qualifying attributes:
- A specific threat level -- e.g., "Competitor 2's HIGH threat rating"
- A specific mechanism phrase -- e.g., "Competitor 0's habit lock-in: [exact phrase from mechanism column]"
- A specific differentiation claim -- e.g., "Competitor 1's core offering: [phrase from offering column]"
- A specific focus-column value -- e.g., "Competitor 3's [focus dimension]: [value from focus column]"

ACCEPTABLE: "Competitor 2's HIGH threat rating combined with its [focus-column value of X] reveals..."
ACCEPTABLE: "The MEDIUM threat of Competitor 1 (mechanism: [phrase from mechanism cell]) implies the gap at..."
NOT ACCEPTABLE: "Competitor 2 reveals that..." -- name-only anchor; no specific attribute cited
NOT ACCEPTABLE: "As shown by Competitor 1..." -- name-only anchor

A finding anchored only by competitor name is an **anchor gate failure**. Free-floating findings and name-only-anchored findings are both prohibited.

Required findings:

**WHITESPACE: {gap label}** -- Name the uncontested space no competitor row owns. One sentence on the gap. One sentence on actionability. Reference which specific attributes from competitor rows confirm no ownership.

If FOCUS is active: produce a **CROSS-DIMENSIONAL** finding using this proof structure exactly:

```
CROSS-DIMENSIONAL: {gap statement}

Single-dimension reduction:
-> Competitive map alone (focus dimension removed): {What does the table show without the focus column? Does this gap appear?} -- NO. {Explain specifically what information from the focus dimension is required -- what is lost when focus is removed.}
-> Focus dimension alone (competitive map removed): {What does the focus analysis show without the competitor rows? Does this gap appear?} -- NO. {Explain specifically what information from the competitor map is required -- what is lost when the map is removed.}

Both reductions fail -> this gap requires both inputs simultaneously. Neither alone is sufficient.
```

If either reduction answer cannot honestly be NO, find a different gap. Do not assert cross-dimensionality without completing both reductions.

---

**[PHASE 5 -- AMEND]**

Exactly 3 adjustments:

1. **Shift focus** -- Change the FOCUS token. Add or replace the focus column in Phase 3 MAP for all rows. Rerun the full CROSS-DIMENSIONAL proof: replace both single-dimension reduction arguments for the new focus dimension -- do not carry over reduction arguments from the previous proof. A standalone instruction to "update the finding" is a **proof rerun failure**: both reduction arguments must be explicitly re-executed, not just the conclusion replaced. State which rows and findings changed.
2. **Add competitor** -- Name the competitor. Add a Phase 3 row with all required fields. Run WebSearch and add the citation inline. State whether WHITESPACE survives, narrows, or closes.
3. **Adjust depth** -- Specify `expand: HIGH` or `expand: {competitor number}`. For matching rows, add a sub-row: (a) the specific feature or behavior driving the threat rating, (b) the one move that would shift the rating down one level.

---

---

## V-02 -- Inline Anchor Tag Before Proof Block

**Axis:** Structural proof format -- SOURCE: slot declared as the first element inside the CROSS-DIMENSIONAL block, before reduction arguments
**Hypothesis:** R2 V-05's two-step reduction proof names the evidentiary basis incidentally inside the argument text -- evidence is discovered during the proof, not declared before it. Adding a mandatory SOURCE: slot as the first line of the proof block forces the model to identify the evidentiary basis before constructing the proof, preventing circular construction where the conclusion implicitly selects its own evidence. Tests whether C-15 can be satisfied by a structural addition to the proof template alone.

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

**Per-row citation gate:** Before writing any external competitor row (row 1 or higher), run WebSearch for that competitor. Paste the citation URL in the Citation column of that row. Do not write the row without it. Do not proceed to Phase 4 with any empty Citation cells. Citations must appear inline in each row -- not in a footnote or trailing references section.

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

Write 3-5 findings.

**Claim-level anchoring rule -- applies to every finding:**

Each finding must reference a specific attribute from a named competitor row. Qualifying attributes:
- A specific threat level -- e.g., "Competitor 2's HIGH threat rating"
- A specific mechanism phrase -- e.g., "Competitor 0's habit lock-in: [exact phrase from mechanism column]"
- A specific differentiation claim -- e.g., "Competitor 1's core offering: [phrase from offering column]"
- A specific focus-column value -- e.g., "Competitor 3's [focus dimension]: [value from focus column]"

ACCEPTABLE: "Competitor 2's HIGH threat rating combined with its [focus-column value of X] reveals..."
ACCEPTABLE: "The MEDIUM threat of Competitor 1 (mechanism: [phrase from mechanism cell]) implies the gap at..."
NOT ACCEPTABLE: "Competitor 2 reveals that..." -- name-only anchor; no specific attribute cited
NOT ACCEPTABLE: "As shown by Competitor 1..." -- name-only anchor

Free-floating findings and name-only-anchored findings are both prohibited.

Required findings:

**WHITESPACE: {gap label}** -- Name the uncontested space no competitor row owns. One sentence on the gap. One sentence on actionability. Reference which specific attributes from competitor rows confirm no ownership.

If FOCUS is active: produce a **CROSS-DIMENSIONAL** finding using this proof structure exactly:

```
CROSS-DIMENSIONAL: {gap statement}

SOURCE: {identify the specific competitor row(s) by number and the exact attribute(s) -- threat level,
mechanism phrase, or focus-column value -- that anchor this finding. Name the evidence before
constructing the proof. Do not proceed to REDUCTION-1 until this slot is filled.}

REDUCTION-1: Without competitive map alone (focus dimension removed): {What does the table show
without the focus column? Does this gap appear?} -- NO. {Explain specifically what information from
the focus dimension is required -- what is lost when focus is removed.}
REDUCTION-2: Without focus dimension alone (competitive map removed): {What does the focus analysis
show without the competitor rows? Does this gap appear?} -- NO. {Explain specifically what information
from the competitor map is required -- what is lost when the map is removed.}

THEREFORE: This gap requires both inputs simultaneously. Neither alone is sufficient.
```

Rule: The SOURCE slot must be filled before writing REDUCTION-1 or REDUCTION-2. Constructing either reduction before naming the evidentiary source is a structural violation -- the evidentiary basis is identified first, the proof follows.

If either reduction answer cannot honestly be NO, find a different gap. Do not assert cross-dimensionality without completing both reductions.

---

**[PHASE 5 -- AMEND]**

Exactly 3 adjustments:

1. **Shift focus** -- Change the FOCUS token. Add or replace the focus column in Phase 3 MAP for all rows. Update the CROSS-DIMENSIONAL finding: first replace the SOURCE slot with the updated evidentiary basis for the new focus dimension, then rerun both REDUCTION-1 and REDUCTION-2. State which rows and findings changed.
2. **Add competitor** -- Name the competitor. Add a Phase 3 row with all required fields. Run WebSearch and add the citation inline. State whether WHITESPACE survives, narrows, or closes.
3. **Adjust depth** -- Specify `expand: HIGH` or `expand: {competitor number}`. For matching rows, add a sub-row: (a) the specific feature or behavior driving the threat rating, (b) the one move that would shift the rating down one level.

---

---

## V-03 -- WHITESPACE Attribute Absence + NOT ACCEPTABLE Anchoring Example

**Axes:** WHITESPACE finding requires attribute-level absence evidence (C-17) + NOT ACCEPTABLE example names the failure pattern directly (C-18)
**Hypothesis:** R2 V-05's WHITESPACE instruction says "reference which specific attributes from competitor rows confirm no ownership" -- this allows the model to name attributes in the positive without naming absent values across rows. V-03 rewrites the WHITESPACE instruction to require naming which attributes are absent or show None/uncontested across named rows, paired with a NOT ACCEPTABLE/ACCEPTABLE example pair demonstrating the bare-assertion failure. Tests whether C-17 and C-18 require only an instructional reframe or a structural template change.

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

**Per-row citation gate:** Before writing any external competitor row (row 1 or higher), run WebSearch for that competitor. Paste the citation URL in the Citation column of that row. Do not write the row without it. Do not proceed to Phase 4 with any empty Citation cells. Citations must appear inline in each row -- not in a footnote or trailing references section.

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

Write 3-5 findings.

**Claim-level anchoring rule -- applies to every finding:**

Each finding must reference a specific attribute from a named competitor row. Qualifying attributes:
- A specific threat level -- e.g., "Competitor 2's HIGH threat rating"
- A specific mechanism phrase -- e.g., "Competitor 0's habit lock-in: [exact phrase from mechanism column]"
- A specific differentiation claim -- e.g., "Competitor 1's core offering: [phrase from offering column]"
- A specific focus-column value -- e.g., "Competitor 3's [focus dimension]: [value from focus column]"

ACCEPTABLE: "Competitor 2's HIGH threat rating combined with its [focus-column value of X] reveals..."
NOT ACCEPTABLE: "Competitor 2 reveals that..." -- this is name-only anchoring. Naming the competitor without citing a specific attribute from that row does not satisfy -- the reader cannot verify the inference without re-reading the full row. Every NOT ACCEPTABLE instance must be caught and rewritten before Phase 5.

Free-floating findings and name-only-anchored findings are both prohibited.

Required findings:

**WHITESPACE: {gap label}**

Ground the gap by naming which specific attributes across which competitor rows are absent or uncontested -- do not assert the gap without attribute-level evidence.

Template:
```
WHITESPACE: {gap label}
Absence evidence: Row C{N} -- {attribute column}: {absent or "None" / "N/A" / uncontested value}.
                  Row C{N} -- {attribute column}: {absent or uncontested value}.
                  [repeat for each relevant row]
Gap confirmed: No row provides a non-absent value for [{attribute column(s)}] -- this space is attribute-level uncontested, not asserted.
Actionability: {one sentence}
```

NOT ACCEPTABLE: "No competitor owns the [X] space." -- bare assertion; no attributes named, no rows cited.
NOT ACCEPTABLE: "None of the competitors address [X]." -- assertion without attribute-level evidence.
ACCEPTABLE: "Row C0 (Mechanism: 'email fragmentation' -- no async-hybrid value), Row C1 (Focus-column: 'N/A'), Row C2 (Mechanism: 'sync-only' -- no hybrid value): all three rows show absent or incompatible values in the [async-hybrid] column. Gap confirmed by attribute-level absence across rows, not asserted."

If FOCUS is active: produce a **CROSS-DIMENSIONAL** finding using this proof structure exactly:

```
CROSS-DIMENSIONAL: {gap statement}

Single-dimension reduction:
-> Competitive map alone (focus dimension removed): {What does the table show without the focus column? Does this gap appear?} -- NO. {Explain specifically what information from the focus dimension is required -- what is lost when focus is removed.}
-> Focus dimension alone (competitive map removed): {What does the focus analysis show without the competitor rows? Does this gap appear?} -- NO. {Explain specifically what information from the competitor map is required -- what is lost when the map is removed.}

Both reductions fail -> this gap requires both inputs simultaneously. Neither alone is sufficient.
```

If either reduction answer cannot honestly be NO, find a different gap.

---

**[PHASE 5 -- AMEND]**

Exactly 3 adjustments:

1. **Shift focus** -- Change the FOCUS token. Add or replace the focus column in Phase 3 MAP for all rows. Update the CROSS-DIMENSIONAL finding and rerun both reduction proofs. State which rows and findings changed.
2. **Add competitor** -- Name the competitor. Add a Phase 3 row with all required fields. Run WebSearch and add the citation inline. Re-evaluate the WHITESPACE absence evidence: does the new row introduce a non-absent value for any attribute column supporting the gap? State whether WHITESPACE survives, narrows, or closes.
3. **Adjust depth** -- Specify `expand: HIGH` or `expand: {competitor number}`. For matching rows, add a sub-row: (a) the specific feature or behavior driving the threat rating, (b) the one move that would shift the rating down one level.

---

---

## V-04 -- Combined: Gate Failure Naming + Source-Before-Proof + AMEND Proof Rerun

**Axes:** C-14 (AMEND prescribes full reduction rerun) + C-15 (SOURCE: slot before proof) + C-16 (named failure states for all gates)
**Hypothesis:** The three format/behavior criteria (C-14, C-15, C-16) can be encoded simultaneously in R2 V-05 without conflicting with existing R2 criteria. The citation gate acquires a named failure state; the proof block gains a SOURCE: slot before reductions; AMEND item 1 names the failure and requires re-execution. Tests whether combining C-14 + C-15 + C-16 produces a clean triple addition or whether any two instructions create tension.

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

**Per-row citation gate:** Before writing any external competitor row (row 1 or higher), run WebSearch for that competitor. Paste the citation URL in the Citation column of that row. Do not write the row without it. An empty Citation cell is a **citation gate failure** -- do not proceed to Phase 4 until all Citation cells are filled. Placing citations in a footnote or trailing references section instead of inline is a **citation gate failure**.

| Competitor | Core offering | Threat | Mechanism | {Focus if active} | Citation |
|---|---|---|---|---|---|
| **0. {C0 name}** | {current user behavior} | {level} | {mechanism from Phase 2} | {focus note if active} | -- |
| **1. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL -- required] |
| **2. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL -- required] |
| *(add rows as needed)* | | | | | |

Rules:
- Every external row must have a URL in Citation. Do not proceed to the next row without filling Citation. Do not proceed to Phase 4 with any empty Citation cells.
- Threat must be HIGH, MEDIUM, or LOW for every row. No other values.
- If FOCUS is active, populate the focus column for every row including Row 0. Do not add a trailing section for focus content.

Print: `Phase 3 complete. Competitors: {count}. All citations present: {yes/no}.`

---

**[PHASE 4 -- SYNTHESIS]**

Write 3-5 findings.

**Claim-level anchoring rule -- applies to every finding:**

Each finding must reference a specific attribute from a named competitor row. Qualifying attributes:
- A specific threat level -- e.g., "Competitor 2's HIGH threat rating"
- A specific mechanism phrase -- e.g., "Competitor 0's habit lock-in: [exact phrase from mechanism column]"
- A specific differentiation claim -- e.g., "Competitor 1's core offering: [phrase from offering column]"
- A specific focus-column value -- e.g., "Competitor 3's [focus dimension]: [value from focus column]"

ACCEPTABLE: "Competitor 2's HIGH threat rating combined with its [focus-column value of X] reveals..."
ACCEPTABLE: "The MEDIUM threat of Competitor 1 (mechanism: [phrase from mechanism cell]) implies the gap at..."
NOT ACCEPTABLE: "Competitor 2 reveals that..." -- name-only anchor; no specific attribute cited
NOT ACCEPTABLE: "As shown by Competitor 1..." -- name-only anchor

A finding anchored only by competitor name is an **anchor gate failure**. Free-floating findings and name-only-anchored findings are both prohibited.

Required findings:

**WHITESPACE: {gap label}** -- Name the uncontested space no competitor row owns. One sentence on the gap. One sentence on actionability. Reference which specific attributes from competitor rows confirm no ownership.

If FOCUS is active: produce a **CROSS-DIMENSIONAL** finding using this proof structure exactly:

```
CROSS-DIMENSIONAL: {gap statement}

SOURCE: {identify the specific competitor row(s) by number and the exact attribute(s) -- threat
level, mechanism phrase, or focus-column value -- that anchor this finding. Declare the evidentiary
basis before writing any reduction argument.}

REDUCTION-1: Without competitive map alone (focus dimension removed): {What does the table show
without the focus column? Does this gap appear?} -- NO. {Explain specifically what information from
the focus dimension is required -- what is lost when focus is removed.}
REDUCTION-2: Without focus dimension alone (competitive map removed): {What does the focus analysis
show without the competitor rows? Does this gap appear?} -- NO. {Explain specifically what information
from the competitor map is required -- what is lost when the map is removed.}

THEREFORE: This gap requires both inputs simultaneously. Neither alone is sufficient.
```

Rule: The SOURCE slot must be filled before writing REDUCTION-1 or REDUCTION-2. Constructing either reduction before naming the evidentiary source is a **proof structure failure**.

If either reduction answer cannot honestly be NO, find a different gap.

---

**[PHASE 5 -- AMEND]**

Exactly 3 adjustments:

1. **Shift focus** -- Change the FOCUS token. Add or replace the focus column in Phase 3 MAP for all rows. Rerun the full CROSS-DIMENSIONAL proof: first replace the SOURCE slot with the updated evidentiary basis for the new focus dimension, then rewrite REDUCTION-1 and REDUCTION-2 from scratch -- do not carry over reduction arguments from the previous proof. A standalone instruction to "update the finding" is a **proof rerun failure**: both reduction arguments must be explicitly re-executed. State which rows and findings changed.
2. **Add competitor** -- Name the competitor. Add a Phase 3 row with all required fields. Run WebSearch and add the citation inline. State whether WHITESPACE survives, narrows, or closes.
3. **Adjust depth** -- Specify `expand: HIGH` or `expand: {competitor number}`. For matching rows, add a sub-row: (a) the specific feature or behavior driving the threat rating, (b) the one move that would shift the rating down one level.

---

---

## V-05 -- Combined: All 5 New R3 Criteria

**Axes:** C-14 + C-15 + C-16 + C-17 + C-18 simultaneously, on top of full R2 V-05 baseline
**Hypothesis:** All 10 aspirational criteria (C-09 through C-18) can be satisfied simultaneously when each criterion's load-bearing condition is explicitly encoded: per-row citation gate for C-11; SOURCE-before-REDUCTION template for C-15; named failure states for C-16; two-step reduction proof for C-12; ACCEPTABLE/NOT ACCEPTABLE anchor examples for C-13/C-18; attribute-absence template for WHITESPACE for C-17; AMEND rerun prescription naming the failure for C-14; cross-dimensional exclusion test for C-09; claim-level grounding prohibition for C-10. This is the maximum-coverage variation targeting 140/140.

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
- Every external row must have a URL in Citation. Do not proceed to the next row without filling Citation. Do not proceed to Phase 4 with any empty Citation cells.
- Threat must be HIGH, MEDIUM, or LOW for every row. No other values.
- If FOCUS is active, populate the focus column for every row including Row 0. Do not add a trailing section for focus content.

Print: `Phase 3 complete. Competitors: {count}. All citations present: {yes/no}.`

---

**[PHASE 4 -- SYNTHESIS]**

Write 3-5 findings.

**Claim-level anchoring rule -- applies to every finding:**

Each finding must reference a specific attribute from a named competitor row. Qualifying attributes:
- A specific threat level -- e.g., "Competitor 2's HIGH threat rating"
- A specific mechanism phrase -- e.g., "Competitor 0's habit lock-in: [exact phrase from mechanism column]"
- A specific differentiation claim -- e.g., "Competitor 1's core offering: [phrase from offering column]"
- A specific focus-column value -- e.g., "Competitor 3's [focus dimension]: [value from focus column]"

ACCEPTABLE: "Competitor 2's HIGH threat rating combined with its [focus-column value of X] reveals..."
ACCEPTABLE: "The MEDIUM threat of Competitor 1 (mechanism: [phrase from mechanism cell]) implies the gap at..."
NOT ACCEPTABLE: "Competitor 2 reveals that..." -- this is name-only anchoring. The competitor name appears but no specific attribute from that row is cited. This is the most common anchor failure -- naming the competitor alone does not satisfy the anchoring requirement.
NOT ACCEPTABLE: "As Competitor 1 demonstrates..." -- name-only anchor; same failure.

A finding anchored only by competitor name is an **anchor gate failure**. Free-floating findings and name-only-anchored findings are both prohibited.

Required findings:

**WHITESPACE: {gap label}**

Ground the gap by naming which specific attributes across which competitor rows are absent or uncontested -- do not assert the gap without attribute-level evidence.

Template:
```
WHITESPACE: {gap label}
Absence evidence: Row C{N} -- {attribute column}: {absent or "None" / "N/A" / uncontested value}.
                  Row C{N} -- {attribute column}: {absent or uncontested value}.
                  [repeat for each relevant row]
Gap confirmed: No row provides a non-absent value for [{attribute column(s)}] -- this space is attribute-level uncontested.
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

REDUCTION-1: Without competitive map alone (focus dimension removed): {What does the table show
without the focus column? Does this gap appear?} -- NO. {Explain specifically what information from
the focus dimension is required -- what is lost when focus is removed.}
REDUCTION-2: Without focus dimension alone (competitive map removed): {What does the focus analysis
show without the competitor rows? Does this gap appear?} -- NO. {Explain specifically what
information from the competitor map is required -- what is lost when the map is removed.}

THEREFORE: This gap requires both inputs simultaneously. Neither alone is sufficient.
```

Rules:
- The SOURCE slot must be filled before writing REDUCTION-1 or REDUCTION-2. Constructing either reduction before declaring the evidentiary source is a **proof structure failure**.
- If either reduction answer cannot honestly be NO, find a different gap. Do not assert cross-dimensionality without completing both reductions.

---

**[PHASE 5 -- AMEND]**

Exactly 3 adjustments:

1. **Shift focus** -- Change the FOCUS token. Add or replace the focus column in Phase 3 MAP for all rows. Rerun the full CROSS-DIMENSIONAL proof: first replace the SOURCE slot with the updated evidentiary basis for the new focus dimension, then rewrite REDUCTION-1 and REDUCTION-2 from scratch for the updated focus -- do not carry over reduction arguments from the previous proof. A standalone instruction to "update the finding" or to "update the CROSS-DIMENSIONAL conclusion" is a **proof rerun failure**: the explicit reconstruction of both single-dimension reduction arguments is required. State which rows and findings changed.
2. **Add competitor** -- Name the competitor. Add a Phase 3 row with all required fields. Run WebSearch and add the citation inline. Re-evaluate the WHITESPACE absence evidence: does the new row introduce a non-absent value for any attribute column supporting the gap? State whether WHITESPACE survives, narrows, or closes.
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
| C-14 AMEND as proof validator | PASS | PARTIAL | PARTIAL | PASS | PASS |
| C-15 inline anchor tag before proof | PARTIAL | PASS | PARTIAL | PASS | PASS |
| C-16 gate failure naming | PASS | PARTIAL | PARTIAL | PASS | PASS |
| C-17 WHITESPACE by attribute absence | PARTIAL | PARTIAL | PASS | PARTIAL | PASS |
| C-18 NOT ACCEPTABLE anchoring example | PASS | PASS | PASS | PASS | PASS |

Notes on partials:
- V-01 C-15: two-step reduction proof present but no SOURCE: slot before arguments; evidence named inside REDUCTION-1 text rather than declared before it -- PARTIAL
- V-01 C-17: WHITESPACE says "reference which specific attributes confirm no ownership" -- close but no attribute-absence template or NOT ACCEPTABLE assertion example -- PARTIAL
- V-02 C-14: AMEND item 1 says "rerun both REDUCTION-1 and REDUCTION-2" but does not name "proof rerun failure" or prohibit "update the finding" explicitly -- PARTIAL
- V-02 C-16: citation gate uses positive framing ("do not proceed") but does not name the failure state -- PARTIAL
- V-02 C-17: same as V-01 C-17; no attribute-absence template -- PARTIAL
- V-03 C-14: AMEND says "rerun both reduction proofs" but does not name failure state -- PARTIAL
- V-03 C-15: no SOURCE: slot before reduction arguments -- PARTIAL
- V-03 C-16: citation gate uses positive framing; no named failure state -- PARTIAL
- V-04 C-17: WHITESPACE instruction retained from R2 ("reference which specific attributes confirm no ownership") -- close but permits assertion form without row-by-row attribute-absence evidence -- PARTIAL
- V-04 C-18: NOT ACCEPTABLE examples from R2 baseline name "Competitor 2 reveals that..." -- PASS

Key interactions to watch in scoring:
- V-01 vs V-02 on C-15: gate naming + AMEND rerun vs SOURCE:-before-proof -- isolates whether C-15 requires structural proof template changes or instructional amendments are sufficient
- V-03 vs V-04 on C-17: attribute-absence WHITESPACE template (V-03) vs C-14+C-15+C-16 without WHITESPACE template (V-04) -- isolates whether C-17 requires its own dedicated template or propagates from claim-level anchoring rules
- V-04 vs V-05 on C-17: confirms whether C-17 needs the dedicated attribute-absence template even when all other R3 criteria are already encoded
- V-01 vs V-05 on C-14: named failure state + AMEND rerun prescription alone vs full stack -- confirms whether C-14 is stable under full five-criterion load
