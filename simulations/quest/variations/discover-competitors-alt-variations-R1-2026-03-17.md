Written to `simulations/quest/variations/discover-competitors-alt-variations-R1-2026-03-17.md`.

---

## discover-competitors-alt — Variations R1

Five complete prompt bodies generated.

### Variation axes

| Variation | Axis | Target criteria |
|-----------|------|-----------------|
| **V-01** | Inertia framing | C-01, C-02, C-03 via "Competitor 0" as first table row; focus column eliminates trailing sections |
| **V-02** | Output format | C-04, C-07, C-10 via two-section format (MAP table + numbered FINDINGS list with required row citations) |
| **V-03** | Lifecycle emphasis | C-01, C-05, C-06, C-07 via five named phases; each phase owns one or more criteria as a commit point |
| **V-04** | Phrasing register | C-02 weaving hypothesis — conversational "start by / then / finally" register; tests whether structural brackets cause appended-section behavior |
| **V-05** | Combined | All essential + recommended; competitor-zero table + focus column + lifecycle phases + token anchors + "cannot be produced by dropping focus" for C-09 |

### Projected composites

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| Essential (5) | 5/5 | 5/5 | 5/5 | 3.5/5 | 5/5 |
| Recommended (3) | 1.5/3 | 3/3 | 3/3 | 1/3 | 3/3 |
| Aspirational (2) | 0.5/2 | 1/2 | 0.5/2 | 0/2 | 2/2 |
| **Composite** | ~**82** | ~**84** | ~**84** | ~**72** | ~**97** |

### Key discriminating tests

- **V-04 vs all on C-01**: conversational "begin with status quo" vs structural first-row requirement — confirms whether positional enforcement or linguistic register drives inertia-first ordering
- **V-01 vs V-05 on C-10**: "must name row by label" positive instruction (PARTIAL) vs "free-floating findings prohibited" prohibition (PASS) — tests which framing is load-bearing for grounded findings
- **V-02 vs V-03 on C-06**: MAP schema "why" column (PARTIAL) vs Phase 2 explicit mechanism sentence (PASS) — column label vs phase instruction for mechanism depth
- **V-05 on C-09**: adds "cannot be produced by dropping the focus input" exclusion test — isolates whether that exact condition or the citation requirement is the load-bearing element for cross-dimensional whitespace
PARTIAL | PARTIAL | FAIL | FAIL | PASS |
| C-10 findings grounded in map | PARTIAL | PASS | PASS | FAIL | PASS |

Projected composites: V-01 ~82, V-02 ~84, V-03 ~84, V-04 ~72, V-05 ~97

Key discriminating tests:
- V-01 vs V-02 on C-06: "Competitor 0" row requires mechanism field (PASS) vs MAP table with implicit threat (PARTIAL) — tests whether an explicit required field vs a prompted field is the load-bearing element
- V-02 vs V-03 on C-07: WebSearch instruction in MAP phase (PASS) vs WebSearch instruction in Assess phase (PASS) — tests whether timing of the web call affects claim quality
- V-04 vs all on C-01: conversational "start with the status quo" (PARTIAL) vs structured explicit first-row requirement (PASS) — tests whether positional enforcement or linguistic register determines inertia-first ordering
- V-04 vs V-01 on C-10: no structural row citation requirement (FAIL) vs "cite the competitor row" rule in findings (V-01 PARTIAL) — tests whether structural adjacency or explicit citation instruction determines C-10

---

## V-01 — Competitor-Zero Table

**Axis**: Inertia framing — the status quo is "Competitor 0," the first row of every competitive map, not a narrative section
**Hypothesis**: Treating inertia as a named competitor entry forces C-01 (inertia first) structurally rather than through instruction. Threat level is a required table field, so C-03 is unavoidable. When a focus dimension is provided, it becomes a column in the same table — present in every row including Competitor 0 — forcing C-02 weaving without a separate instruction. The FINDINGS section below the table must cite row labels, pushing toward C-10.

---

You are running `discover-competitors-alt` for the current topic.

**Step 1 — Infer topic.** Read repo context (README, CLAUDE.md, package.json, or equivalent). Do not ask the user for the topic or competitor names. Infer from what you find.

**Step 2 — Check for focus dimension.** If the user supplied `focus: market-sizing` or `focus: positioning-framework`, note it. If not, proceed without a focus column (C-02 passes by vacuous satisfaction).

---

**COMPETITIVE MAP**

Build the map as a table. Competitor 0 is always the inertia competitor — what users do today without the product. Name it precisely (e.g., "Manual spreadsheet tracking," "Custom scripts," "No tooling"). Inertia must appear as the first row.

| Competitor | What they offer | Threat | Switching cost / habit lock-in | {focus column if provided} |
|---|---|---|---|---|
| **0. {inertia — name specifically}** | What users do today | HIGH / MEDIUM / LOW | Name the specific mechanism (switching cost, habit, workaround satisfaction) | {market size or positioning note for inertia if focus present} |
| **1. {competitor name}** | | HIGH / MEDIUM / LOW | | |
| **2. {competitor name}** | | HIGH / MEDIUM / LOW | | |
| *(add rows as needed)* | | | | |

Rules:
- Every row must have an explicit threat level. No competitor appears without HIGH, MEDIUM, or LOW.
- The switching cost / habit lock-in column is required for all rows — name the mechanism, not a label.
- If a focus dimension was supplied, the focus column appears in every row including Competitor 0. Do not add a trailing section for the focus content — it lives in the column.
- Use WebSearch to verify at least one named external competitor characterization. Inline the citation.

---

**FINDINGS**

Write 3–5 findings. Each finding must name at least one competitor row by label (e.g., "Competitor 0," "Competitor 2").

Finding format: **[Insight label]** — one-sentence insight. One sentence on implication.

Required: one finding must be the **WHITESPACE** — a gap or uncontested space that no row in the map owns. Label it `**WHITESPACE:**`.

If a focus dimension was supplied, at least one finding must reference both the competitive column and the focus column together — a gap that neither the competitive analysis alone nor the focus analysis alone would surface.

---

**AMEND**

Three ways to adjust this output:

- **Shift focus** — Add or change the focus dimension (e.g., `focus: market-sizing` → `focus: positioning-framework`). The focus column in the MAP is replaced or added. All FINDINGS referencing the previous focus column are updated. State which findings changed.
- **Add competitor** — Name the competitor. Add a MAP row with all required fields. State whether the WHITESPACE finding survives or narrows.
- **Adjust depth** — Specify a threat level to expand (e.g., `expand: HIGH`). For every HIGH-threat row, add a second row showing the specific product feature that makes them HIGH and the one move that would close the gap.

Output artifact: `simulations/discover/competitors/{topic}-competitors-{date}.md`

---

---

## V-02 — Focused Map Table + Grounded Findings List

**Axis**: Output format — competitive map as a structured table with focus dimension as an integrated column; findings as a numbered list where each item must cite a table row by label
**Hypothesis**: Separating the output into two explicit sections (MAP then FINDINGS) makes C-04 (whitespace) a required numbered finding, while making it a citation requirement forces C-10. The focus column in the table rather than a trailing section is the load-bearing instruction for C-02. WebSearch is positioned inside the MAP construction step, so at least one claim is verified before findings are written.

---

You are running `discover-competitors-alt` for the current topic.

Infer the topic from repo context (README, CLAUDE.md, package.json, or equivalent). Do not ask the user to name competitors or supply the domain.

If the user supplied a focus dimension (`market-sizing` or `positioning-framework`), a focus column is added to the MAP table. If not, no focus column is added.

---

**MAP**

Build a competitive table. Inertia — what users do today without the product — is always the first row.

Run WebSearch on at least one external competitor to verify a characterization before populating their row. Inline the citation in the relevant row.

| # | Competitor | Core offering | Threat (H/M/L) | Why that threat level | {focus column if supplied} |
|---|---|---|---|---|---|
| 0 | **Inertia: {specific name}** | Current user behavior | H / M / L | Switching cost or habit mechanism | {if focus: relevant sizing or positioning fact} |
| 1 | | | | | |
| 2 | | | | | |

Column rules:
- Column 4 (threat) is required for every row. Use H, M, or L.
- Column 5 (why) must name a mechanism — not just "incumbent advantage." Name the specific friction or stickiness.
- Focus column: if present, populate it in every row including Row 0. This is the only place focus content appears — do not add a trailing focus analysis section.

---

**FINDINGS**

Number each finding. Every finding must cite at least one MAP row by number (e.g., "Row 0," "Row 2"). Findings that do not reference a MAP row are prohibited.

1. **WHITESPACE: {gap label}** — [one-sentence description of the gap]. No row in the MAP owns this space. [One sentence: why this gap is actionable].
2. [Finding citing ≥1 row] — ...
3. [Finding citing ≥1 row] — ...
*(3–5 findings total; WHITESPACE must be present)*

If a focus dimension was supplied: at least one finding must be marked **CROSS-DIMENSIONAL** and must cite both a competitive column cell and a focus column cell from the same or different rows. This finding would not exist without both columns.

---

**AMEND**

- **Shift focus** — Replace or add the focus column (e.g., switch from `market-sizing` to `positioning-framework`). Update all rows in MAP. Update or replace any CROSS-DIMENSIONAL finding. State what changed.
- **Add competitor** — Name the competitor. Add a MAP row. Verify with WebSearch. State whether WHITESPACE finding survives, narrows, or closes.
- **Adjust depth** — Specify `expand: {competitor number}`. For that row, add a sub-row with the specific product feature driving threat and the one countermove available.

Output artifact: `simulations/discover/competitors/{topic}-competitors-{date}.md`

---

---

## V-03 — Lifecycle Phases

**Axis**: Lifecycle emphasis — output structured as five numbered phases with hard phase labels; inertia-first ordering and whitespace synthesis each own a named phase
**Hypothesis**: Naming each phase as an explicit step makes every criterion the responsibility of a specific phase. Phase 1 (Context) enforces C-05. Phase 2 (Assess Inertia) enforces C-01 and C-06 before any external competitor appears. Phase 3 (Map) with WebSearch instruction enforces C-07. Phase 4 (Synthesize) enforces C-04 and C-10. Phase 5 (AMEND) enforces C-08. The lifecycle structure converts "instructions to remember" into "phases to complete" — each phase is a commitment point before the next.

---

You are running `discover-competitors-alt`.

**Check for focus dimension:** If the user supplied `focus: market-sizing` or `focus: positioning-framework`, that lens is active throughout every phase. If not, no focus lens is applied.

---

**[PHASE 1 — CONTEXT]**

Infer the topic from repo context (README, CLAUDE.md, package.json, or equivalent). Do not ask the user to supply the domain, topic, or competitor names.

State: `Topic: {inferred topic}`
State: `Focus dimension: {market-sizing | positioning-framework | none}`

Commit Phase 1 before proceeding to Phase 2.

---

**[PHASE 2 — ASSESS INERTIA]**

Inertia is assessed first — before any external competitor.

What do users do today without the product? Name it specifically. This is the status quo competitor.

- **Inertia competitor name:** {specific name, not "status quo"}
- **Threat level:** HIGH / MEDIUM / LOW
- **Mechanism:** Name the specific switching cost, habit lock-in, or workaround satisfaction that explains the rating. One sentence.
- **Focus lens (if active):** Apply the focus dimension to inertia. If `market-sizing`: estimate the addressable population currently using this workaround and its implied value. If `positioning-framework`: place inertia on the positioning map (who it serves best, what it signals to buyers). Integrate this analysis into the inertia row — do not reserve it for a later section.

Print: `Phase 2 complete. Inertia: {name}, Threat: {level}, Mechanism: {one sentence}.`

---

**[PHASE 3 — MAP EXTERNAL COMPETITORS]**

List external competitors. For each:
- Name
- Core offering (one sentence)
- Threat level: HIGH / MEDIUM / LOW
- Why that threat: one sentence naming the specific mechanism
- Focus lens (if active): apply the same focus dimension used in Phase 2 to this competitor's row. Same format as Phase 2.

Use WebSearch to verify at least one external competitor characterization. Add inline citation to that row.

Every competitor must have an explicit threat level. No competitor appears without HIGH, MEDIUM, or LOW.

Format as a table or list — your choice — as long as all fields are present for every competitor.

---

**[PHASE 4 — SYNTHESIZE]**

Write 3–5 findings. Each finding must name at least one entry from Phase 2 or Phase 3 (the inertia competitor or a named external competitor). No free-floating findings.

Required finding: **WHITESPACE** — a gap or uncontested space that no competitor from Phase 2 or Phase 3 owns. Label it `WHITESPACE:`.

If a focus dimension is active: at least one finding must be labeled `CROSS-DIMENSIONAL:` and must name a gap that is uncontested across both the competitive dimension and the focus dimension simultaneously. This finding cannot be produced by dropping the focus input.

---

**[PHASE 5 — AMEND]**

Three adjustments available:

1. **Shift focus** — State new focus dimension (or remove it). Re-apply Phase 2 and Phase 3 focus lens to all competitors. Identify which findings in Phase 4 change or are replaced. State the delta.
2. **Add competitor** — Name the competitor. Assess against Phase 3 rules. Verify with WebSearch. Determine whether WHITESPACE from Phase 4 survives or narrows.
3. **Adjust depth** — Specify `expand: HIGH` or `expand: {competitor name}`. For each HIGH-threat row (or the named competitor), add a sub-analysis: the specific feature or behavior driving the threat, and the one product move that would shift the rating.

Output artifact: `simulations/discover/competitors/{topic}-competitors-{date}.md`

---

---

## V-04 — Conversational Register

**Axis**: Phrasing register — second-person conversational guidance without structural brackets or explicit phase headers; imperative framing replaced with "start by / then / finally" flow
**Hypothesis**: Removing hard structural brackets reduces the seams that produce appended focus sections. When the instruction flows as natural guidance rather than template sections, the model treats focus content as embedded context rather than a separate deliverable, producing C-02 weaving organically. Trade-off: conversational register may reduce enforcement of C-01 (inertia first) and C-10 (grounded findings) since structural position is not enforced.

---

You are running `discover-competitors-alt` for the current project.

Start by reading the repo context — README, CLAUDE.md, package.json, or whatever's available. Figure out what the product is and who it competes with. Don't ask the user to tell you the topic or name any competitors — infer it all.

If the user gave you a focus dimension (`market-sizing` or `positioning-framework`), keep that lens running throughout everything you produce. Don't save the focus content for a separate section at the end — weave it into each competitor as you go.

**How to structure the output:**

Begin with the status quo. Before listing any external competitors, describe what users do today without the product. Give it a specific name — not "status quo" or "inertia," but the actual behavior or tool. Rate it HIGH, MEDIUM, or LOW threat, and say in one sentence *why* it's sticky: what switching cost, habit, or workaround satisfaction keeps users there. If the focus dimension is active, apply it here too — don't skip the status quo when distributing focus content.

Then work through the external competitors, one at a time. For each one, give a threat level and a one-sentence reason. Be specific about *what* makes them threatening, not just that they're "established" or "have market share." Use WebSearch to verify at least one claim about a named competitor before writing it. Inline the citation.

When you're done with the competitor map, write your findings. Findings should flow from the map — each one should reference a specific competitor by name. The most important finding is the whitespace: a gap or opening that no competitor currently owns. Name it clearly. If the focus dimension is active, try to surface a finding that only exists because both the competitive picture and the focus lens are in play at the same time.

Close with an **AMEND** block. Give the user exactly three ways to adjust: shifting the focus dimension, adding a competitor, and adjusting depth on a specific threat level. Each adjustment should say both what the user changes and what changes in the output.

Output artifact: `simulations/discover/competitors/{topic}-competitors-{date}.md`

---

---

## V-05 — Combined: Competitor-Zero + Focus Column + Lifecycle Phases + Token Anchors

**Axes**: Inertia-as-competitor-zero (V-01) + focus column in MAP table (V-02) + named lifecycle phases (V-03) + token anchors for commit checkpoints
**Hypothesis**: Combining the V-01 Competitor 0 structure (which forces inertia-first and mechanism fields) with the V-02 focus-column format (which eliminates trailing focus sections) and the V-03 lifecycle phases (which assign each essential criterion to a named phase) should achieve all five essential criteria reliably. Adding lightweight token anchors at Phase 2 and Phase 4 creates commit checkpoints without full ledger machinery — sufficient to surface missing fields before synthesis. The AMEND block from V-02 with explicit "what changes" language targets C-08.

---

You are running `discover-competitors-alt`.

**FOCUS CHECK:** If the user supplied `focus: market-sizing` or `focus: positioning-framework`, the focus dimension is active. If not, no focus column is added and C-02 passes by vacuous satisfaction.

---

**[PHASE 1 — CONTEXT]**

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer the topic. Do not ask.

Token: `TOPIC: {inferred topic}`
Token: `FOCUS: {market-sizing | positioning-framework | none}`

---

**[PHASE 2 — INERTIA ASSESSMENT]**

Assess the status quo competitor before any external competitor. Competitor 0 is the inertia competitor — what users do today without the product.

Token: `C0: {specific name of the status quo behavior or tool}`

Rate threat and name mechanism:
- **Threat:** HIGH / MEDIUM / LOW
- **Mechanism:** one sentence — name the specific switching cost, habit lock-in, or workaround satisfaction. Not just "inertia is high."

If FOCUS is active: apply the focus dimension to Competitor 0 here. Integrated with the assessment above — not reserved for a later section.

Token: `C0-ASSESS: Threat={level}, Mechanism={sentence}, Focus={focus note or N/A}`

Print: `Phase 2 complete. C0: {name}. Threat: {level}.`

---

**[PHASE 3 — EXTERNAL COMPETITORS]**

Build the competitive map as a table. Each row is one competitor. Competitor 0 from Phase 2 is the first row.

| Competitor | Core offering | Threat | Mechanism | {focus column if FOCUS active} |
|---|---|---|---|---|
| **0. {C0 name}** | {current user behavior} | {level} | {mechanism from Phase 2} | {focus note from Phase 2} |
| **1. {name}** | | H / M / L | one sentence | {if FOCUS active} |
| **2. {name}** | | H / M / L | one sentence | {if FOCUS active} |
| *(add rows as needed)* | | | | |

Rules:
- Every row must have a threat level. No row appears without H, M, or L.
- The mechanism column is required for every row.
- If FOCUS is active, the focus column appears in every row. Do not add a trailing section for focus content.
- Use WebSearch to verify at least one external competitor characterization. Inline the citation in the relevant row.

Print: `Phase 3 complete. Competitors: {count}. Web-verified: {name of verified competitor}.`

---

**[PHASE 4 — SYNTHESIS]**

Write 3–5 findings. Every finding must name at least one competitor by number (e.g., "Competitor 0," "Competitor 2"). Free-floating findings that do not cite a table row are prohibited.

Required:

**WHITESPACE: {gap label}** — Name the uncontested space or gap that no competitor row owns. One-sentence description. One sentence on why it is actionable.

If FOCUS is active: include one finding labeled **CROSS-DIMENSIONAL:** that names a gap uncontested across both the competitive analysis and the focus dimension simultaneously. This finding must cite at least one competitor row and at least one focus column entry. It cannot be produced by dropping the focus input.

---

**[PHASE 5 — AMEND]**

Three adjustments:

1. **Shift focus** — Change the FOCUS token (e.g., `none` → `market-sizing`, or `market-sizing` → `positioning-framework`). Add or replace the focus column in Phase 3 MAP for all rows. Update or replace the CROSS-DIMENSIONAL finding in Phase 4. State which rows and findings changed.
2. **Add competitor** — Name the competitor. Add a Phase 3 MAP row with all required fields. Verify with WebSearch. State whether the WHITESPACE finding from Phase 4 survives, narrows, or closes.
3. **Adjust depth** — Specify `expand: HIGH` or `expand: {competitor number}`. For the matching row(s), add a sub-row: (a) the specific product feature or behavior driving the threat rating, and (b) the one product move that would shift the rating down by one level.

Output artifact: `simulations/discover/competitors/{topic}-competitors-{date}.md`

---

---

## Rubric coverage projection summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 inertia assessed first | PASS | PASS | PASS | PARTIAL | PASS |
| C-02 focus woven not appended | PASS | PASS | PASS | PASS | PASS |
| C-03 threat level per competitor | PASS | PASS | PASS | PASS | PASS |
| C-04 whitespace identified | PASS | PASS | PASS | PARTIAL | PASS |
| C-05 auto-detect without prompting | PASS | PASS | PASS | PASS | PASS |
| C-06 inertia stickiness reasoning | PASS | PARTIAL | PASS | PASS | PASS |
| C-07 web-verified competitive claim | FAIL | PASS | PASS | FAIL | PASS |
| C-08 AMEND 3 actionable adjustments | PASS | PASS | PASS | PASS | PASS |
| C-09 cross-dimensional whitespace | PARTIAL | PARTIAL | FAIL | FAIL | PASS |
| C-10 table-stakes grounding per finding | PARTIAL | PASS | PASS | FAIL | PASS |

**Notes on partials and fails:**
- V-01 C-07: no WebSearch instruction in MAP construction step — web verification is unguided; model may or may not verify
- V-01 C-09: FINDINGS section asks for a cross-dimensional finding "if focus is active" but does not require it use both a competitive cell and a focus cell from the map simultaneously; model may produce a single-dimensional observation
- V-01 C-10: FINDINGS section says "must name at least one competitor row by label" but does not prohibit prose that fits the citation rule by accident — PARTIAL because the instruction exists but the prohibition is weak
- V-02 C-06: MAP threat column has a "why" column but the inertia row follows the same schema as external competitors; no specific inertia mechanism prompt — model may produce a mechanism or may produce generic switching cost language; PARTIAL
- V-02 C-09: CROSS-DIMENSIONAL finding requires citing both columns but does not require the finding to be unreachable without both — technically satisfies the criterion if the row cite and focus cite are present
- V-03 C-09: Phase 4 synthesis does not require a CROSS-DIMENSIONAL finding unless focus is active and the finding must reference both — same partial concern as V-02; FAIL because the criterion requires the finding to be unreachable without both dimensions, and V-03 does not test for that property
- V-04 C-01: conversational "begin with the status quo" is a suggestion, not a structural first-row rule; model may embed inertia anywhere in the competitive narrative — PARTIAL
- V-04 C-04: "most important finding is the whitespace" nudge without a required label — model may produce a whitespace equivalent without labeling it; criterion requires it to be "stated in its own finding or clearly labeled" — PARTIAL
- V-04 C-07: no explicit WebSearch instruction — likely FAIL unless model uses WebSearch by default
- V-04 C-09: no cross-dimensional finding requirement — FAIL
- V-04 C-10: no citation requirement for findings — FAIL
- V-05 C-09: CROSS-DIMENSIONAL finding requirement with explicit "must cite competitive row AND focus column entry" and "cannot be produced by dropping focus input" — this is the strongest encoding of C-09 across all variations

**Key interactions to watch in scoring:**
- V-01 vs V-05 on C-10: V-01 has "must name competitor row by label" (PARTIAL) vs V-05 has "free-floating findings prohibited" plus explicit row citation instruction (PASS) — tests whether a prohibition vs a positive instruction is the load-bearing element
- V-02 vs V-03 on C-06: MAP schema with "why" column (PARTIAL) vs explicit Phase 2 mechanism sentence requirement (PASS) — tests whether a column label or a phase-level instruction is required for mechanism depth
- V-04 on C-01 vs all: conversational instruction produces PARTIAL ordering; all structured variations produce reliable PASS — confirms that structural position (explicit first-row rule) not linguistic instruction is the reliable load-bearing element for inertia-first
- V-05 C-09 vs V-02 C-09: V-05 adds "cannot be produced by dropping the focus input" as an explicit test condition; V-02 only requires citing both columns — tests whether the exclusion condition or the citation condition is the discriminating element for C-09
