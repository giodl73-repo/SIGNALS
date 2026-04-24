Written to `simulations/quest/variations/discover-competitors-alt-variations-R2-2026-03-17.md`.

---

## discover-competitors-alt — Variations R2

Five complete prompt bodies generated. Baseline is R1 V-05 (scored 100) — all R1 excellence patterns preserved in every variation.

### Variation axes

| Variation | Axis | New R2 criteria targeted |
|-----------|------|--------------------------|
| **V-01** | Citation completeness — per-row WebSearch gate on every external row | C-11 |
| **V-02** | Self-negating proof — two-step reduction template (→ map alone: NO / → focus alone: NO) | C-12 |
| **V-03** | Claim-level anchoring — ACCEPTABLE/NOT ACCEPTABLE examples + named attribute list | C-13 |
| **V-04** | Combined — citation gate + reduction proof | C-11, C-12 |
| **V-05** | Combined — all R2 criteria simultaneously | C-11, C-12, C-13 |

### Key design decisions

**C-11 (fully-cited table):** The R1 V-05 instruction "verify at least one external competitor" left other rows uncited. V-01 replaces it with a structural per-row gate: "do not write row N without running WebSearch for competitor N first; do not proceed to Phase 4 with any empty Citation cells." The gate makes an uncited row a visible failure rather than a permitted omission.

**C-12 (self-negating proof):** R1 V-05's "cannot be produced by dropping the focus input" asserts the exclusion but doesn't show the reduction. V-02 adds a mandatory two-step template with labeled `→ Competitive map alone: … — NO` and `→ Focus dimension alone: … — NO` slots. The model must construct both arguments, not just assert the conclusion.

**C-13 (claim-level anchors):** The R1 prohibition ("free-floating findings prohibited") established row-citation but allowed name-only anchors like "Competitor 2 reveals...". V-03 adds a named qualifying-attribute list (threat rating, mechanism phrase, differentiation claim, focus-column value) and explicit ACCEPTABLE/NOT ACCEPTABLE examples to force cell-value granularity.

### Projected composites

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| Essential (60) | 60 | 60 | 60 | 60 | 60 |
| Recommended (30) | 30 | 30 | 30 | 30 | 30 |
| Aspirational (25) | ~12.5 | ~12.5 | ~12.5 | ~17.5 | ~25 |
| **Composite** | ~**93** | ~**93** | ~**93** | ~**100** | ~**115** |
**V-01 vs R1 V-05 on C-11**: per-row gate ("do not write row without citation") vs "at least one" — tests whether gate scope is the load-bearing condition for a fully-cited table
- **V-02 vs R1 V-05 on C-12**: two-step reduction template ("→ competitive map alone: does gap appear? NO") vs exclusion assertion ("cannot be produced by dropping focus") — tests whether structured proof is required for self-negating finding
- **V-03 vs R1 V-05 on C-13**: ACCEPTABLE/NOT ACCEPTABLE examples + attribute list vs general prohibition — tests whether example-level instruction is required for claim-level anchoring
- **V-04 vs V-05 on C-13**: combined C-11 + C-12 without claim-level examples vs with — isolates whether C-13 requires dedicated instruction even when two other R2 criteria are already encoded

---

## V-01 — Citation Completeness

**Axis:** Citation scope — per-row WebSearch gate applied to every external competitor row, not just one
**Hypothesis:** Changing "verify at least one external competitor" to a per-row gate ("run WebSearch before writing each row; paste citation inline; do not write the row without it") produces C-11 (fully-cited table) without degrading any R1 criteria. The gate is structural — a row cannot appear without the citation being present — rather than an instruction that may or may not be honored at scale.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If the user supplied `focus: market-sizing` or `focus: positioning-framework`, the focus dimension is active. If not, no focus column is added and focus-related criteria pass by vacuous satisfaction.

---

**[PHASE 1 — CONTEXT]**

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer the topic. Do not ask.

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

**[PHASE 2 — INERTIA ASSESSMENT]**

Assess the status quo before any external competitor.

```
Token: C0: {specific name of status quo behavior or tool — not "status quo" or "inertia"}
```

- **Threat:** HIGH / MEDIUM / LOW
- **Mechanism:** one sentence — name the specific switching cost, habit lock-in, or workaround satisfaction that explains this threat level. Not just "inertia is high."

If FOCUS is active: apply the focus dimension to Competitor 0 here, integrated with the assessment above — not deferred to a later section.

```
Token: C0-ASSESS: Threat={level}, Mechanism={sentence}, Focus={note or N/A}
```

Print: `Phase 2 complete. C0: {name}. Threat: {level}.`

---

**[PHASE 3 — EXTERNAL COMPETITORS]**

Build the competitive map. Competitor 0 from Phase 2 is the first row.

**Per-row citation gate:** Before writing any external competitor row (row 1 or higher), run WebSearch for that competitor. Paste the citation URL in the Citation column of that row. Do not write the row without a citation. Do not consolidate citations into a footnote or trailing references block — every external row gets its own inline citation.

| Competitor | Core offering | Threat | Mechanism | {Focus if active} | Citation |
|---|---|---|---|---|---|
| **0. {C0 name}** | {current user behavior} | {level} | {mechanism from Phase 2} | {focus note if active} | — |
| **1. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL — required] |
| **2. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL — required] |
| *(add rows as needed)* | | | | | |

Rules:
- Every external row must have a URL in Citation. An empty Citation cell is a gate failure — do not proceed to Phase 4 until all Citation cells are filled.
- Threat must be HIGH, MEDIUM, or LOW for every row. No other values.
- If FOCUS is active, populate the focus column for every row including Row 0. Do not add a trailing section for focus content.

Print: `Phase 3 complete. Competitors: {count}. All citations present: {yes/no}.`

---

**[PHASE 4 — SYNTHESIS]**

Write 3–5 findings. Every finding must name at least one competitor by number (e.g., "Competitor 0," "Competitor 2"). Free-floating findings that do not cite a table row are prohibited.

Required:

**WHITESPACE: {gap label}** — Name the uncontested space no competitor row owns. One sentence. One sentence on actionability.

If FOCUS is active: include one finding labeled **CROSS-DIMENSIONAL:** that names a gap uncontested across both the competitive dimension and the focus dimension simultaneously. This finding must cite at least one competitor row and at least one focus column entry. It cannot be produced by dropping the focus input.

---

**[PHASE 5 — AMEND]**

Exactly 3 adjustments:

1. **Shift focus** — Change the FOCUS token. Add or replace the focus column in Phase 3 MAP for all rows. Update or replace the CROSS-DIMENSIONAL finding. State which rows and findings changed.
2. **Add competitor** — Name the competitor. Add a Phase 3 row with all required fields. Run WebSearch and add the citation inline. State whether the WHITESPACE finding survives, narrows, or closes.
3. **Adjust depth** — Specify `expand: HIGH` or `expand: {competitor number}`. For matching rows, add a sub-row: (a) the specific feature or behavior driving the threat rating, (b) the one move that would shift the rating down one level.

---

---

## V-02 — Self-Negating Proof

**Axis:** Cross-dimensional proof format — two-step structured reduction template replaces single exclusion assertion
**Hypothesis:** R1 V-05 scored PASS on C-09 via "cannot be produced by dropping focus input" but C-12 (new in R2) requires the output to show the single-dimension reduction explicitly — not just assert the exclusion. A templated two-step proof forces the model to construct the argument for both removals rather than asserting the conclusion, satisfying C-12's requirement that the output "implies the single-dimension reduction for each — showing what is lost when either dimension is removed."

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If the user supplied `focus: market-sizing` or `focus: positioning-framework`, the focus dimension is active. If not, no focus column is added and focus-related criteria pass by vacuous satisfaction.

---

**[PHASE 1 — CONTEXT]**

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer the topic. Do not ask.

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

**[PHASE 2 — INERTIA ASSESSMENT]**

Assess the status quo before any external competitor.

```
Token: C0: {specific name of status quo behavior or tool}
```

- **Threat:** HIGH / MEDIUM / LOW
- **Mechanism:** one sentence — name the specific switching cost, habit lock-in, or workaround satisfaction. Not just "inertia is high."

If FOCUS is active: apply the focus dimension to Competitor 0 here, integrated with the assessment above.

```
Token: C0-ASSESS: Threat={level}, Mechanism={sentence}, Focus={note or N/A}
```

Print: `Phase 2 complete. C0: {name}. Threat: {level}.`

---

**[PHASE 3 — EXTERNAL COMPETITORS]**

Build the competitive map. Competitor 0 from Phase 2 is the first row.

| Competitor | Core offering | Threat | Mechanism | {Focus if active} |
|---|---|---|---|---|
| **0. {C0 name}** | {current user behavior} | {level} | {mechanism from Phase 2} | {focus note if active} |
| **1. {name}** | | H / M / L | one sentence | {if FOCUS active} |
| **2. {name}** | | H / M / L | one sentence | {if FOCUS active} |
| *(add rows as needed)* | | | | |

Rules:
- Every row must have a threat level. No row appears without H, M, or L.
- The mechanism column is required for every row.
- If FOCUS is active, populate the focus column for every row. Do not add a trailing section for focus content.
- Use WebSearch to verify at least one external competitor characterization. Inline the citation in the relevant row.

Print: `Phase 3 complete. Competitors: {count}. Web-verified: {name of verified competitor}.`

---

**[PHASE 4 — SYNTHESIS]**

Write 3–5 findings. Every finding must cite at least one competitor by number. Free-floating findings that do not cite a table row are prohibited.

Required:

**WHITESPACE: {gap label}** — Name the uncontested space no competitor row owns. One sentence. One sentence on actionability.

If FOCUS is active, produce a **CROSS-DIMENSIONAL** finding using the following proof structure exactly:

```
CROSS-DIMENSIONAL: {gap statement}

Single-dimension reduction proof:
→ Competitive map alone (focus dimension removed): {Describe what the competitor table shows without the focus column. Does this gap appear in the table without focus?} — NO. {Explain specifically what information from the focus dimension is required to see this gap — what is lost when focus is removed.}
→ Focus dimension alone (competitive map removed): {Describe what the focus analysis shows without the competitor rows. Does this gap appear from focus analysis alone?} — NO. {Explain specifically what information from the competitor map is required to see this gap — what is lost when the map is removed.}

Conclusion: This gap requires both the competitor map AND the {focus dimension} simultaneously. Neither alone is sufficient.
```

If either reduction answer cannot honestly be NO, find a different gap. Do not assert cross-dimensionality without completing both reductions.

---

**[PHASE 5 — AMEND]**

Exactly 3 adjustments:

1. **Shift focus** — Change the FOCUS token. Add or replace the focus column in Phase 3 MAP for all rows. Update the CROSS-DIMENSIONAL finding and rerun both reduction proofs. State which rows and findings changed.
2. **Add competitor** — Name the competitor. Add a Phase 3 MAP row with all required fields. Verify with WebSearch. State whether WHITESPACE survives, narrows, or closes.
3. **Adjust depth** — Specify `expand: HIGH` or `expand: {competitor number}`. For matching rows, add a sub-row: (a) the specific feature or behavior driving the threat rating, (b) the one move that would shift the rating down one level.

---

---

## V-03 — Claim-Level Anchoring

**Axis:** Finding anchor depth — ACCEPTABLE/NOT ACCEPTABLE examples paired with a named qualifying-attribute list replaces general prohibition alone
**Hypothesis:** R1 V-05 produced reliable C-10 (findings cite a table row) via "free-floating findings prohibited" but R2 adds C-13 (findings cite a specific cell value or row-level attribute, not just competitor name). The prohibition alone does not specify what attribute granularity is required. Adding explicit examples ("ACCEPTABLE: Competitor 2's HIGH threat rating combined with...") and a named attribute list trains the model to distinguish between name-only anchors (prohibited) and specific-value anchors (required), producing C-13.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If the user supplied `focus: market-sizing` or `focus: positioning-framework`, the focus dimension is active. If not, no focus column is added and focus-related criteria pass by vacuous satisfaction.

---

**[PHASE 1 — CONTEXT]**

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer the topic. Do not ask.

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

**[PHASE 2 — INERTIA ASSESSMENT]**

Assess the status quo before any external competitor.

```
Token: C0: {specific name of status quo behavior or tool}
```

- **Threat:** HIGH / MEDIUM / LOW
- **Mechanism:** one sentence — name the specific switching cost, habit lock-in, or workaround satisfaction. Not just "inertia is high."

If FOCUS is active: apply the focus dimension to Competitor 0 here, integrated with the assessment above.

```
Token: C0-ASSESS: Threat={level}, Mechanism={sentence}, Focus={note or N/A}
```

Print: `Phase 2 complete. C0: {name}. Threat: {level}.`

---

**[PHASE 3 — EXTERNAL COMPETITORS]**

Build the competitive map. Competitor 0 from Phase 2 is the first row.

| Competitor | Core offering | Threat | Mechanism | {Focus if active} |
|---|---|---|---|---|
| **0. {C0 name}** | {current user behavior} | {level} | {mechanism from Phase 2} | {focus note if active} |
| **1. {name}** | | H / M / L | one sentence | {if FOCUS active} |
| **2. {name}** | | H / M / L | one sentence | {if FOCUS active} |
| *(add rows as needed)* | | | | |

Rules:
- Every row must have a threat level. No row appears without H, M, or L.
- The mechanism column is required for every row.
- If FOCUS is active, populate the focus column for every row. Do not add a trailing section for focus content.
- Use WebSearch to verify at least one external competitor characterization. Inline the citation in the relevant row.

Print: `Phase 3 complete. Competitors: {count}. Web-verified: {name}.`

---

**[PHASE 4 — SYNTHESIS]**

Write 3–5 findings.

**Claim-level anchoring rule — applies to every finding:**

Each finding must reference a specific attribute from a named competitor row. Qualifying attributes:
- A specific threat level — e.g., "Competitor 2's HIGH threat rating"
- A specific mechanism phrase — e.g., "Competitor 0's habit lock-in: [exact phrase from mechanism column]"
- A specific differentiation claim — e.g., "Competitor 1's core offering: [phrase from offering column]"
- A specific focus-column value — e.g., "Competitor 3's [focus dimension]: [value from focus column]"

ACCEPTABLE: "Competitor 2's HIGH threat rating, combined with its [focus-column value], reveals that..."
ACCEPTABLE: "The MEDIUM threat of Competitor 1 (mechanism: [phrase from mechanism cell]) implies the gap at..."
NOT ACCEPTABLE: "Competitor 2 reveals that..." — name-only anchor; no specific attribute from the row cited
NOT ACCEPTABLE: "As Competitor 1 demonstrates..." — name-only anchor

Free-floating findings and name-only-anchored findings are both prohibited.

Required findings:

**WHITESPACE: {gap label}** — Name the uncontested space no competitor row owns. One sentence on the gap. One sentence on actionability. Reference which specific attributes from competitor rows confirm no ownership.

If FOCUS is active: include one finding labeled **CROSS-DIMENSIONAL:** that names a gap uncontested across both the competitive dimension and the focus dimension simultaneously. Anchor it to a specific attribute from a competitor row AND a specific value from the focus column. This finding cannot be produced by dropping the focus input.

---

**[PHASE 5 — AMEND]**

Exactly 3 adjustments:

1. **Shift focus** — Change the FOCUS token. Add or replace the focus column in Phase 3 MAP for all rows. Update or replace the CROSS-DIMENSIONAL finding. State which rows and findings changed.
2. **Add competitor** — Name the competitor. Add a Phase 3 MAP row with all required fields. Verify with WebSearch. State whether WHITESPACE survives, narrows, or closes.
3. **Adjust depth** — Specify `expand: HIGH` or `expand: {competitor number}`. For matching rows, add a sub-row: (a) the specific feature or behavior driving the threat rating, (b) the one move that would shift the rating down one level.

---

---

## V-04 — Combined: Citation Completeness + Self-Negating Proof

**Axes:** V-01 per-row citation gate + V-02 two-step reduction proof
**Hypothesis:** C-11 (all-external citations) and C-12 (self-negating proof) can be achieved simultaneously without sacrificing any R1 criteria. The per-row citation gate is structural — each row requires a citation before the next row can be written — and the two-step reduction proof is templated with forced NO answers, so neither instruction conflicts with the other or with existing R1 enforcement machinery. This tests whether the R1 V-05 baseline cleanly absorbs two new enforcement mechanisms.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If the user supplied `focus: market-sizing` or `focus: positioning-framework`, the focus dimension is active. If not, no focus column is added and focus-related criteria pass by vacuous satisfaction.

---

**[PHASE 1 — CONTEXT]**

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer the topic. Do not ask.

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

**[PHASE 2 — INERTIA ASSESSMENT]**

Assess the status quo before any external competitor.

```
Token: C0: {specific name of status quo behavior or tool}
```

- **Threat:** HIGH / MEDIUM / LOW
- **Mechanism:** one sentence — name the specific switching cost, habit lock-in, or workaround satisfaction. Not just "inertia is high."

If FOCUS is active: apply the focus dimension to Competitor 0 here, integrated with the assessment above — not deferred to a later section.

```
Token: C0-ASSESS: Threat={level}, Mechanism={sentence}, Focus={note or N/A}
```

Print: `Phase 2 complete. C0: {name}. Threat: {level}.`

---

**[PHASE 3 — EXTERNAL COMPETITORS]**

Build the competitive map. Competitor 0 from Phase 2 is the first row.

**Per-row citation gate:** Before writing any external competitor row, run WebSearch for that competitor. Paste the citation URL in the Citation column of that row. Do not write the row without it. Citations go inline in the row — not in a footnote or trailing references section.

| Competitor | Core offering | Threat | Mechanism | {Focus if active} | Citation |
|---|---|---|---|---|---|
| **0. {C0 name}** | {current user behavior} | {level} | {mechanism from Phase 2} | {focus note if active} | — |
| **1. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL — required] |
| **2. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL — required] |
| *(add rows as needed)* | | | | | |

Rules:
- Every external row must have a URL in Citation. Do not proceed to the next row until the Citation cell is filled. Do not proceed to Phase 4 with any empty Citation cells.
- Threat must be HIGH, MEDIUM, or LOW for every row.
- If FOCUS is active, populate the focus column for every row including Row 0. Do not add a trailing section for focus content.

Print: `Phase 3 complete. Competitors: {count}. All citations present: {yes/no}.`

---

**[PHASE 4 — SYNTHESIS]**

Write 3–5 findings. Every finding must name at least one competitor by number. Free-floating findings that do not cite a table row are prohibited.

Required:

**WHITESPACE: {gap label}** — Name the uncontested space no competitor row owns. One sentence. One sentence on actionability.

If FOCUS is active, produce a **CROSS-DIMENSIONAL** finding using this proof structure exactly:

```
CROSS-DIMENSIONAL: {gap statement}

Single-dimension reduction:
→ Competitive map alone (focus dimension removed): {What does the table show without the focus column? Does this gap appear?} — NO. {Explain what information from the focus dimension is required to see this gap.}
→ Focus dimension alone (competitive map removed): {What does the focus analysis show without the competitor rows? Does this gap appear?} — NO. {Explain what information from the competitor map is required to see this gap.}

Both reductions fail → this gap requires both inputs simultaneously.
```

If either reduction answer cannot honestly be NO, find a different gap.

---

**[PHASE 5 — AMEND]**

Exactly 3 adjustments:

1. **Shift focus** — Change the FOCUS token. Add or replace the focus column in Phase 3 MAP for all rows. Update the CROSS-DIMENSIONAL finding and rerun both reduction proofs. State which rows and findings changed.
2. **Add competitor** — Name the competitor. Add a Phase 3 MAP row with all required fields. Run WebSearch and add the citation inline. State whether WHITESPACE survives, narrows, or closes.
3. **Adjust depth** — Specify `expand: HIGH` or `expand: {competitor number}`. For matching rows, add a sub-row: (a) the specific feature or behavior driving the threat rating, (b) the one move that would shift the rating down one level.

---

---

## V-05 — Combined: All R2 Criteria

**Axes:** V-01 per-row citation gate + V-02 two-step reduction proof + V-03 claim-level anchoring examples + R1 V-05 baseline (layered enforcement, prohibition framing, token anchors)
**Hypothesis:** All five aspirational criteria (C-09 through C-13) can be achieved simultaneously when each criterion's load-bearing condition is explicitly encoded: per-row citation gate for C-11; templated two-step reduction proof for C-12; ACCEPTABLE/NOT ACCEPTABLE examples with named attribute list for C-13; cross-dimensional exclusion test for C-09; prohibition framing + claim-level examples together for C-10. The R1 V-05 baseline handles all essential and recommended criteria. The three R2 additions integrate into the same phase structure without conflict.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If the user supplied `focus: market-sizing` or `focus: positioning-framework`, the focus dimension is active. If not, no focus column is added and focus-related criteria pass by vacuous satisfaction.

---

**[PHASE 1 — CONTEXT]**

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer the topic. Do not ask.

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

**[PHASE 2 — INERTIA ASSESSMENT]**

Assess the status quo before any external competitor.

```
Token: C0: {specific name of status quo behavior or tool — not "status quo" or "inertia"}
```

- **Threat:** HIGH / MEDIUM / LOW
- **Mechanism:** one sentence — name the specific switching cost, habit lock-in, or workaround satisfaction that explains this threat level. Not just "inertia is high."

If FOCUS is active: apply the focus dimension to Competitor 0 here, integrated with the assessment above — not deferred to a later section.

```
Token: C0-ASSESS: Threat={level}, Mechanism={sentence}, Focus={note or N/A}
```

Print: `Phase 2 complete. C0: {name}. Threat: {level}.`

---

**[PHASE 3 — EXTERNAL COMPETITORS]**

Build the competitive map. Competitor 0 from Phase 2 is the first row.

**Per-row citation gate:** Before writing any external competitor row (row 1 or higher), run WebSearch for that competitor. Paste the citation URL in the Citation column of that row. Do not write the row without it. Citations must appear inline in each row — not in a footnote, not in a trailing references section. Consolidating citations elsewhere is a gate failure.

| Competitor | Core offering | Threat | Mechanism | {Focus if active} | Citation |
|---|---|---|---|---|---|
| **0. {C0 name}** | {current user behavior} | {level} | {mechanism from Phase 2} | {focus note if active} | — |
| **1. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL — required] |
| **2. {name}** | | H / M / L | one sentence | {if FOCUS active} | [URL — required] |
| *(add rows as needed)* | | | | | |

Rules:
- Every external row must have a URL in Citation. Do not proceed to the next row without filling Citation. Do not proceed to Phase 4 with any empty Citation cells.
- Threat must be HIGH, MEDIUM, or LOW for every row. No other values.
- If FOCUS is active, populate the focus column for every row including Row 0. Do not add a trailing section for focus content.

Print: `Phase 3 complete. Competitors: {count}. All citations present: {yes/no}.`

---

**[PHASE 4 — SYNTHESIS]**

Write 3–5 findings.

**Claim-level anchoring rule — applies to every finding:**

Each finding must reference a specific attribute from a named competitor row. Qualifying attributes:
- A specific threat level — e.g., "Competitor 2's HIGH threat rating"
- A specific mechanism phrase — e.g., "Competitor 0's habit lock-in: [exact phrase from mechanism column]"
- A specific differentiation claim — e.g., "Competitor 1's core offering: [phrase from offering column]"
- A specific focus-column value — e.g., "Competitor 3's [focus dimension]: [value from focus column]"

ACCEPTABLE: "Competitor 2's HIGH threat rating combined with its [focus-column value of X] reveals..."
ACCEPTABLE: "The MEDIUM threat of Competitor 1 (mechanism: [phrase from mechanism cell]) implies the gap at..."
NOT ACCEPTABLE: "Competitor 2 reveals that..." — name-only anchor; no specific attribute cited
NOT ACCEPTABLE: "As shown by Competitor 1..." — name-only anchor

Free-floating findings and name-only-anchored findings are both prohibited.

Required findings:

**WHITESPACE: {gap label}** — Name the uncontested space no competitor row owns. One sentence on the gap. One sentence on actionability. Reference which specific attributes from competitor rows confirm no ownership.

If FOCUS is active: produce a **CROSS-DIMENSIONAL** finding using this proof structure exactly:

```
CROSS-DIMENSIONAL: {gap statement}
[Anchor: {specific competitor attribute} + {specific focus-column value} that produce this finding]

Single-dimension reduction:
→ Competitive map alone (focus dimension removed): {What does the table show without the focus column? Does this gap appear?} — NO. {Explain specifically what information from the focus dimension is required — what is lost when focus is removed.}
→ Focus dimension alone (competitive map removed): {What does the focus analysis show without the competitor rows? Does this gap appear?} — NO. {Explain specifically what information from the competitor map is required — what is lost when the map is removed.}

Both reductions fail → this gap requires both dimensions simultaneously. Neither alone is sufficient.
```

If either reduction answer cannot honestly be NO, find a different gap. Do not assert cross-dimensionality without completing both reductions.

---

**[PHASE 5 — AMEND]**

Exactly 3 adjustments:

1. **Shift focus** — Change the FOCUS token. Add or replace the focus column in Phase 3 MAP for all rows. Update the CROSS-DIMENSIONAL finding and rerun both reduction proofs. State which rows and findings changed.
2. **Add competitor** — Name the competitor. Add a Phase 3 MAP row with all required fields. Run WebSearch and add the citation inline. State whether WHITESPACE survives, narrows, or closes.
3. **Adjust depth** — Specify `expand: HIGH` or `expand: {competitor number}`. For matching rows, add a sub-row: (a) the specific feature or behavior driving the threat rating, (b) the one move that would shift the rating down one level.

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
| C-11 fully-cited competitor table | PASS | FAIL | FAIL | PASS | PASS |
| C-12 self-negating cross-dimensional | PARTIAL | PASS | PARTIAL | PASS | PASS |
| C-13 claim-level finding anchors | PARTIAL | PARTIAL | PASS | PARTIAL | PASS |

Notes on partials and fails:
- V-01 C-12: exclusion assertion present from R1 V-05 but no two-step reduction template — model may assert "cannot be produced by dropping focus" without showing either single-dimension reduction explicitly; PARTIAL
- V-01 C-13: prohibition framing present from R1 V-05 but no qualifying-attribute list or ACCEPTABLE examples — model may anchor to competitor name + vague description rather than a specific cell value; PARTIAL
- V-02 C-11: two-step reduction proof present but citation gate is "at least one" from R1 V-05 — external rows without citations remain possible; FAIL
- V-02 C-13: prohibition framing only; no claim-level examples or named attribute list; PARTIAL
- V-03 C-11: claim-level anchoring examples present but citation gate is "at least one" from R1 V-05; FAIL
- V-03 C-12: exclusion assertion present from R1 V-05 but no two-step reduction template; PARTIAL
- V-04 C-13: per-row citation gate + two-step reduction proof both present but no ACCEPTABLE/NOT ACCEPTABLE examples or qualifying-attribute list; PARTIAL

Key interactions to watch in scoring:
- V-01 vs R1 V-05 on C-11: per-row gate vs "at least one" — confirms whether gate scope is the load-bearing condition for a fully-cited table
- V-02 vs V-01 on C-12: two-step reduction template vs single exclusion assertion — confirms whether structured proof or assertion is required for C-12
- V-03 vs V-01 on C-13: ACCEPTABLE/NOT ACCEPTABLE examples + attribute list vs prohibition alone — confirms whether example-level instruction is required for C-13
- V-04 vs V-05 on C-13: C-11 + C-12 enforcement without claim-level examples vs with — isolates whether C-13 requires dedicated instruction even when two other R2 criteria are already encoded
