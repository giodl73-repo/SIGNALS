Written to `simulations/quest/variations/discover-competitors-alt-variations-R2-2026-03-17.md`.

---

## R2 Variations — discover-competitors-alt

**Starting point:** R1 V-05 (180/180). All R2 variations use the proven architecture as their base.

**Three single-axis variations:**

| # | Axis | Change | Expected |
|---|------|--------|---------|
| V-01 | Lifecycle emphasis | Single-sentence opening assertion (two clauses joined by em-dash) | **180** or **170** |
| V-02 | Role sequence | Inertia as Phase 1, pre-map as Phase 2; downstream phase references updated | **180** |
| V-03 | Phrasing register | DO NOT/DO replaced with WRONG:/RIGHT: in all three structural constraint phases | **180** or **177.5** |

**Two combined variations:**

| # | Axes | Change | Expected |
|---|------|--------|---------|
| V-04 | Lifecycle + role sequence | Compressed opening + phase inversion | **180** or **170** |
| V-05 | Role sequence + phrasing + inertia framing | Phase inversion + WRONG/RIGHT + inertia manifesto preamble before SETUP | **180** or **177.5** |

**Four open questions R2 will resolve:**

1. Is a single em-dash sentence sufficient for C-14/C-17, or does C-14 require two distinct sentences?
2. Does C-11 ("Phase 1 pre-map table") require the table to be in phase-labeled "Phase 1", or is the label descriptive of the construct?
3. Is WRONG/RIGHT "equivalent structural framing" per C-23 (FULL PASS), or label-specific (PARTIAL = 2.5)?
4. Do phase inversion + compressed opening stack cleanly, or does the combination expose a gap (e.g., C-10/C-09 referencing "Phase 1 map entry" when the map is now Phase 2)?

The degenerate case is V-01 failing C-14/C-17 and V-03 getting PARTIAL on C-23 — still Breakthrough territory at 167.5–177.5.
S, 180 | **180** |
| V-04 | Combined: lifecycle + role sequence | Compressed opening + phase inversion → 180 | **180** |
| V-05 | Combined: role sequence + phrasing + inertia framing | Phase inversion + WRONG/RIGHT + manifesto → 180 | **180** |

---

## V-01 — Single-Sentence Meta-Declaration (Lifecycle Compression)

**Axis:** Lifecycle emphasis
**Hypothesis:** Compressing the two-line opening assertion into a single sentence joined by
em-dash still satisfies C-14 and C-17 in the SR-block-free architecture. C-14's pass condition
requires naming all three constraints and the apparatus type — the "two-sentence" example in the
definition is illustrative, not prescriptive. C-17 requires asserting symmetry, not a specific
sentence count. Expected: **180**. If the single sentence is judged insufficient for C-14 or C-17,
expected: **170** (−5 each, or **175** if only one fails).

---

```
All three structural constraints (C-11 pre-map, C-13 inertia mechanisms, C-12 whitespace) enforce via table schema — an absent table or empty row/cell is an observable format failure.

PRE-GENERATION INTEGRITY CHECK

Before generating any phase output, verify the prompt contains the following elements:
For C-11 (pre-map): (1) Format artifact declared in prompt? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
For C-13 (mechanism table): (1) Format artifact declared in prompt? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
For C-12 (whitespace): (1) Format artifact declared in prompt? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
If any check fails, halt and report the missing element before proceeding.

---

SETUP: Detect the product domain from README, CLAUDE.md, package.json, or any
Glob-discoverable project file. Do not ask the user to name the domain or competitors.
Infer everything from context.

---

PHASE 1 — COMPETITIVE LANDSCAPE MAP

C-11 structural constraint. Apparatus: table schema.

IF focus = market sizing:
  Build a market-dimension table: segments, size indicators, growth signals. Minimum 3 named rows.

IF focus = positioning framework:
  Build a positioning-dimension table: axes, poles, current occupation. Minimum 3 named rows.

DO NOT: Omit the pre-map table. Use fewer than 3 named rows. Paraphrase row labels in any
  downstream column.
DO: Produce a named pre-map table with >= 3 rows. Carry row labels verbatim into the Map
  Position column in Phase 3.

| Dimension | [columns per focus] |
|-----------|---------------------|

---

PHASE 2 — INERTIA COMPETITOR

The most dangerous competitor in almost every product market is not a named vendor — it is
the team's existing way of doing things. Assess inertia first.

Competitor 0: None / status quo. Threat level: HIGH. State explicitly.

Phase 2 produces two tables. Table 1 below is the C-13 structural constraint (mechanism
table). Table 2 below is a portability summary — additional framing only; it does not
substitute for the mechanism table for C-13 apparatus uniformity or C-19 purposes.

C-13 structural constraint. Apparatus: table schema. An absent mechanism table or empty
mechanism row fails.

DO NOT: Omit the mechanism table. Leave any mechanism row empty. Write mechanism descriptions
  generic enough to apply to a social network, a payroll tool, or a scheduling app without
  modification.
DO: Fill all three mechanism rows with content so domain-specific that substituting it into a
  different product category would be obviously wrong.

| Mechanism | Description | Domain-exclusive? |
|-----------|-------------|------------------|
| WORKAROUND SATISFACTION | | |
| SWITCHING COST | | |
| HABIT LOCK-IN | | |

PORTABILITY TEST: Each mechanism must fail if substituted into a different product category.
Exact fail condition: If a mechanism description reads as true for a social network (or
equivalent dissimilar category), it fails.

Portability summary (additional framing only; does not substitute for the mechanism table
above for C-13 or C-19 apparatus uniformity purposes):

| Mechanism | Fails portability test for: | Result |
|-----------|----------------------------|--------|
| WORKAROUND SATISFACTION | | |
| SWITCHING COST | | |
| HABIT LOCK-IN | | |

Run WebSearch to verify domain-specific claims if needed.

---

PHASE 3 — NAMED COMPETITORS

For each named competitor:
1. Run WebSearch. Cite the source inline (URL or publication).
2. Assign threat level: HIGH / MEDIUM / LOW.
3. Fill Map Position from Phase 1 row label verbatim. An empty or paraphrased cell fails.

| Competitor | Threat | Map Position | [focus columns] | Notes |
|------------|--------|-------------|-----------------|-------|

---

PHASE 4 — WHITESPACE ANALYSIS

C-12 structural constraint. Apparatus: table schema. An absent table or single-row table fails.

DO NOT: Produce a single-row whitespace table. Leave either row without Phase 1 grounding or
  Map Position label reference. Omit the combined paragraph. Write a Focus gap that does not
  require the focus dimension input.
DO: Fill both whitespace rows with findings that require both Phase 1 data and the focus
  dimension simultaneously. Write a combined paragraph (2-3 sentences) naming at least one
  Phase 3 competitor and one Phase 1 row label.

| Gap type | Description | Phase 1 grounding |
|----------|-------------|------------------|
| Competitive gap | | |
| Focus gap | | |

Write a combined paragraph synthesizing both whitespace rows into a single narrative.

---

PHASE 5 — KEY FINDINGS

List 4-6 findings. Each finding must reference at least one named Phase 1 row or Phase 3
competitor by label. No finding may be free-floating.

---

AMEND

Exactly 3 items. Each names: (1) what input changes, (2) what changes in the output.
1. Shift focus dimension (market <-> positioning) — pre-map table restructures; whitespace
   rows shift; combined paragraph changes axis.
2. Add a named competitor — Phase 3 gains a row; findings update if the new competitor
   contests a whitespace gap.
3. Narrow domain to a submarket — pre-map rows focus; inertia mechanisms become more
   specific; portability test becomes more stringent.

---

PRE-SUBMISSION VERIFICATION

For C-11 (pre-map): (1) Format artifact present in output? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
For C-13 (mechanism table): (1) Format artifact present in output — mechanism table, not
  portability summary? (2) Format-failure declared? (3) Bilateral enforcement pair present
  (rejection example + acceptance example)?
For C-12 (whitespace): (1) Format artifact present in output? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
```

---

## V-02 — Phase Inversion: Inertia as Phase 1

**Axis:** Role sequence
**Hypothesis:** Moving the inertia assessment to Phase 1 (before the competitive landscape map)
and the pre-map table to Phase 2 simultaneously satisfies C-01 (inertia is assessed first —
now the literal first phase) and C-11 (pre-map table structure is present with verbatim rule,
bilateral pair, and phase-embedded designation token, regardless of phase label). Phase 3 Map
Position and Phase 4/5 grounding references update to Phase 2 row labels. C-25 real-pass is
preserved — Phase 1 now carries the two inertia tables with explicit non-substitutability.
Expected: **180**. Open question Q2: does the rubric's C-11 label "Phase 1 pre-map table"
require the table to be in a phase numbered "1"?

---

```
All three structural constraints (C-11 pre-map, C-13 inertia mechanisms, C-12 whitespace)
enforce via table schema. An absent table or empty row/cell is an observable format failure.

PRE-GENERATION INTEGRITY CHECK

Before generating any phase output, verify the prompt contains the following elements:
For C-11 (pre-map): (1) Format artifact declared in prompt? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
For C-13 (mechanism table): (1) Format artifact declared in prompt? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
For C-12 (whitespace): (1) Format artifact declared in prompt? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
If any check fails, halt and report the missing element before proceeding.

---

SETUP: Detect the product domain from README, CLAUDE.md, package.json, or any
Glob-discoverable project file. Do not ask the user to name the domain or competitors.
Infer everything from context.

---

PHASE 1 — INERTIA COMPETITOR

The most dangerous competitor in every product market is not a named vendor — it is the
team's existing way of doing things. Assess inertia before all named competitors.

Competitor 0: None / status quo. Threat level: HIGH. State explicitly.

Phase 1 produces two tables. Table 1 below is the C-13 structural constraint (mechanism
table). Table 2 below is a portability summary — additional framing only; it does not
substitute for the mechanism table for C-13 apparatus uniformity or C-19 purposes.

C-13 structural constraint. Apparatus: table schema. An absent mechanism table or empty
mechanism row fails.

DO NOT: Omit the mechanism table. Leave any mechanism row empty. Write mechanism descriptions
  generic enough to apply to a social network, a payroll tool, or a scheduling app without
  modification.
DO: Fill all three mechanism rows with content so domain-specific that substituting it into a
  different product category would be obviously wrong.

| Mechanism | Description | Domain-exclusive? |
|-----------|-------------|------------------|
| WORKAROUND SATISFACTION | | |
| SWITCHING COST | | |
| HABIT LOCK-IN | | |

PORTABILITY TEST: Each mechanism must fail if substituted into a different product category.
Exact fail condition: If a mechanism description reads as true for a social network (or
equivalent dissimilar category), it fails.

Portability summary (additional framing only; does not substitute for the mechanism table
above for C-13 or C-19 apparatus uniformity purposes):

| Mechanism | Fails portability test for: | Result |
|-----------|----------------------------|--------|
| WORKAROUND SATISFACTION | | |
| SWITCHING COST | | |
| HABIT LOCK-IN | | |

Run WebSearch to verify domain-specific claims if needed.

---

PHASE 2 — COMPETITIVE LANDSCAPE MAP

C-11 structural constraint. Apparatus: table schema.

IF focus = market sizing:
  Build a market-dimension table: segments, size indicators, growth signals. Minimum 3 named rows.

IF focus = positioning framework:
  Build a positioning-dimension table: axes, poles, current occupation. Minimum 3 named rows.

DO NOT: Omit the pre-map table. Use fewer than 3 named rows. Paraphrase row labels in any
  downstream column.
DO: Produce a named pre-map table with >= 3 rows. Carry row labels verbatim into the Map
  Position column in Phase 3.

| Dimension | [columns per focus] |
|-----------|---------------------|

---

PHASE 3 — NAMED COMPETITORS

For each named competitor:
1. Run WebSearch. Cite the source inline (URL or publication).
2. Assign threat level: HIGH / MEDIUM / LOW.
3. Fill Map Position from Phase 2 row label verbatim. An empty or paraphrased cell fails.

| Competitor | Threat | Map Position | [focus columns] | Notes |
|------------|--------|-------------|-----------------|-------|

---

PHASE 4 — WHITESPACE ANALYSIS

C-12 structural constraint. Apparatus: table schema. An absent table or single-row table fails.

DO NOT: Produce a single-row whitespace table. Leave either row without Phase 2 grounding or
  Map Position label reference. Omit the combined paragraph. Write a Focus gap that does not
  require the focus dimension input.
DO: Fill both whitespace rows with findings that require both Phase 2 data and the focus
  dimension simultaneously. Write a combined paragraph (2-3 sentences) naming at least one
  Phase 3 competitor and one Phase 2 row label.

| Gap type | Description | Phase 2 grounding |
|----------|-------------|------------------|
| Competitive gap | | |
| Focus gap | | |

Write a combined paragraph synthesizing both whitespace rows into a single narrative.

---

PHASE 5 — KEY FINDINGS

List 4-6 findings. Each finding must reference at least one named Phase 2 row or Phase 3
competitor by label. No finding may be free-floating.

---

AMEND

Exactly 3 items. Each names: (1) what input changes, (2) what changes in the output.
1. Shift focus dimension (market <-> positioning) — pre-map table restructures; whitespace
   rows shift; combined paragraph changes axis.
2. Add a named competitor — Phase 3 gains a row; findings update if the new competitor
   contests a whitespace gap.
3. Narrow domain to a submarket — pre-map rows focus; inertia mechanisms become more
   specific; portability test becomes more stringent.

---

PRE-SUBMISSION VERIFICATION

For C-11 (pre-map): (1) Format artifact present in output? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
For C-13 (mechanism table): (1) Format artifact present in output — mechanism table, not
  portability summary? (2) Format-failure declared? (3) Bilateral enforcement pair present
  (rejection example + acceptance example)?
For C-12 (whitespace): (1) Format artifact present in output? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
```

---

## V-03 — WRONG/RIGHT Bilateral Labels

**Axis:** Phrasing register
**Hypothesis:** Replacing DO NOT/DO with WRONG:/RIGHT: in all three phase-level structural
constraint instructions — while keeping both loops label-agnostic ("bilateral enforcement pair
present (rejection example + acceptance example)?") — satisfies C-23 fully. Per C-23's
definition, the invariant is the bilateral structure (rejection example + acceptance example),
and "the label format is surface." WRONG/RIGHT maintains the bilateral structure: WRONG
provides the rejection example; RIGHT provides the acceptance example. Expected: **180**
(C-23 FULL PASS). If WRONG/RIGHT is treated as label-specific, expected: **C-23 PARTIAL = 177.5**.

---

```
All three structural constraints (C-11 pre-map, C-13 inertia mechanisms, C-12 whitespace)
enforce via table schema. An absent table or empty row/cell is an observable format failure.

PRE-GENERATION INTEGRITY CHECK

Before generating any phase output, verify the prompt contains the following elements:
For C-11 (pre-map): (1) Format artifact declared in prompt? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
For C-13 (mechanism table): (1) Format artifact declared in prompt? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
For C-12 (whitespace): (1) Format artifact declared in prompt? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
If any check fails, halt and report the missing element before proceeding.

---

SETUP: Detect the product domain from README, CLAUDE.md, package.json, or any
Glob-discoverable project file. Do not ask the user to name the domain or competitors.
Infer everything from context.

---

PHASE 1 — COMPETITIVE LANDSCAPE MAP

C-11 structural constraint. Apparatus: table schema.

IF focus = market sizing:
  Build a market-dimension table: segments, size indicators, growth signals. Minimum 3 named rows.

IF focus = positioning framework:
  Build a positioning-dimension table: axes, poles, current occupation. Minimum 3 named rows.

WRONG: Pre-map table absent; fewer than 3 named rows; row labels paraphrased in any downstream
  column.
RIGHT: Pre-map table present with >= 3 named rows; row labels appear verbatim in the Map
  Position column in Phase 3.

| Dimension | [columns per focus] |
|-----------|---------------------|

---

PHASE 2 — INERTIA COMPETITOR

The most dangerous competitor in almost every product market is not a named vendor — it is
the team's existing way of doing things. Assess inertia first.

Competitor 0: None / status quo. Threat level: HIGH. State explicitly.

Phase 2 produces two tables. Table 1 below is the C-13 structural constraint (mechanism
table). Table 2 below is a portability summary — additional framing only; it does not
substitute for the mechanism table for C-13 apparatus uniformity or C-19 purposes.

C-13 structural constraint. Apparatus: table schema. An absent mechanism table or empty
mechanism row fails.

WRONG: Mechanism table absent; any mechanism row empty; mechanism descriptions generic enough
  to apply equally to a social network, a payroll tool, or a scheduling app.
RIGHT: All three mechanism rows present with domain-specific content; substituting any row
  into a different product category would be obviously wrong.

| Mechanism | Description | Domain-exclusive? |
|-----------|-------------|------------------|
| WORKAROUND SATISFACTION | | |
| SWITCHING COST | | |
| HABIT LOCK-IN | | |

PORTABILITY TEST: Each mechanism must fail if substituted into a different product category.
Exact fail condition: If a mechanism description reads as true for a social network (or
equivalent dissimilar category), it fails.

Portability summary (additional framing only; does not substitute for the mechanism table
above for C-13 or C-19 apparatus uniformity purposes):

| Mechanism | Fails portability test for: | Result |
|-----------|----------------------------|--------|
| WORKAROUND SATISFACTION | | |
| SWITCHING COST | | |
| HABIT LOCK-IN | | |

Run WebSearch to verify domain-specific claims if needed.

---

PHASE 3 — NAMED COMPETITORS

For each named competitor:
1. Run WebSearch. Cite the source inline (URL or publication).
2. Assign threat level: HIGH / MEDIUM / LOW.
3. Fill Map Position from Phase 1 row label verbatim. An empty or paraphrased cell fails.

| Competitor | Threat | Map Position | [focus columns] | Notes |
|------------|--------|-------------|-----------------|-------|

---

PHASE 4 — WHITESPACE ANALYSIS

C-12 structural constraint. Apparatus: table schema. An absent table or single-row table fails.

WRONG: Single-row whitespace table; either row lacks Phase 1 grounding or Map Position label
  reference; combined paragraph absent; Focus gap row that does not require the focus
  dimension input to exist.
RIGHT: Both rows present; each row grounded in a Phase 1 entry or Map Position label; Focus
  gap requires both Phase 1 data and the focus dimension simultaneously; combined paragraph
  synthesizes across both rows naming at least one Phase 3 competitor and one Phase 1 label.

| Gap type | Description | Phase 1 grounding |
|----------|-------------|------------------|
| Competitive gap | | |
| Focus gap | | |

Write a combined paragraph synthesizing both whitespace rows into a single narrative.

---

PHASE 5 — KEY FINDINGS

List 4-6 findings. Each finding must reference at least one named Phase 1 row or Phase 3
competitor by label. No finding may be free-floating.

---

AMEND

Exactly 3 items. Each names: (1) what input changes, (2) what changes in the output.
1. Shift focus dimension (market <-> positioning) — pre-map table restructures; whitespace
   rows shift; combined paragraph changes axis.
2. Add a named competitor — Phase 3 gains a row; findings update if the new competitor
   contests a whitespace gap.
3. Narrow domain to a submarket — pre-map rows focus; inertia mechanisms become more
   specific; portability test becomes more stringent.

---

PRE-SUBMISSION VERIFICATION

For C-11 (pre-map): (1) Format artifact present in output? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
For C-13 (mechanism table): (1) Format artifact present in output — mechanism table, not
  portability summary? (2) Format-failure declared? (3) Bilateral enforcement pair present
  (rejection example + acceptance example)?
For C-12 (whitespace): (1) Format artifact present in output? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
```

---

## V-04 — Combined: Phase Inversion + Compressed Meta-Declaration

**Axes:** Role sequence + lifecycle emphasis
**Hypothesis:** Phase inversion (V-02) and single-sentence opening assertion (V-01) combine
without unexpected criterion interaction. Single-sentence covers C-14/C-17 for C-24 PASS;
Phase 1 inertia covers C-01; Phase 2 pre-map covers C-11; phase-embedded C-XX declarations
are consistent with the new phase numbering. Expected: **180**. If the single sentence fails
C-14/C-17, expected: **170**.

---

```
All three structural constraints (C-11 pre-map, C-13 inertia mechanisms, C-12 whitespace) enforce via table schema — an absent table or empty row/cell is an observable format failure.

PRE-GENERATION INTEGRITY CHECK

Before generating any phase output, verify the prompt contains the following elements:
For C-11 (pre-map): (1) Format artifact declared in prompt? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
For C-13 (mechanism table): (1) Format artifact declared in prompt? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
For C-12 (whitespace): (1) Format artifact declared in prompt? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
If any check fails, halt and report the missing element before proceeding.

---

SETUP: Detect the product domain from README, CLAUDE.md, package.json, or any
Glob-discoverable project file. Do not ask the user to name the domain or competitors.
Infer everything from context.

---

PHASE 1 — INERTIA COMPETITOR

The most dangerous competitor in every product market is not a named vendor — it is the
team's existing way of doing things. Assess inertia before all named competitors.

Competitor 0: None / status quo. Threat level: HIGH. State explicitly.

Phase 1 produces two tables. Table 1 below is the C-13 structural constraint (mechanism
table). Table 2 below is a portability summary — additional framing only; it does not
substitute for the mechanism table for C-13 apparatus uniformity or C-19 purposes.

C-13 structural constraint. Apparatus: table schema. An absent mechanism table or empty
mechanism row fails.

DO NOT: Omit the mechanism table. Leave any mechanism row empty. Write mechanism descriptions
  generic enough to apply to a social network, a payroll tool, or a scheduling app without
  modification.
DO: Fill all three mechanism rows with content so domain-specific that substituting it into a
  different product category would be obviously wrong.

| Mechanism | Description | Domain-exclusive? |
|-----------|-------------|------------------|
| WORKAROUND SATISFACTION | | |
| SWITCHING COST | | |
| HABIT LOCK-IN | | |

PORTABILITY TEST: Each mechanism must fail if substituted into a different product category.
Exact fail condition: If a mechanism description reads as true for a social network (or
equivalent dissimilar category), it fails.

Portability summary (additional framing only; does not substitute for the mechanism table
above for C-13 or C-19 apparatus uniformity purposes):

| Mechanism | Fails portability test for: | Result |
|-----------|----------------------------|--------|
| WORKAROUND SATISFACTION | | |
| SWITCHING COST | | |
| HABIT LOCK-IN | | |

Run WebSearch to verify domain-specific claims if needed.

---

PHASE 2 — COMPETITIVE LANDSCAPE MAP

C-11 structural constraint. Apparatus: table schema.

IF focus = market sizing:
  Build a market-dimension table: segments, size indicators, growth signals. Minimum 3 named rows.

IF focus = positioning framework:
  Build a positioning-dimension table: axes, poles, current occupation. Minimum 3 named rows.

DO NOT: Omit the pre-map table. Use fewer than 3 named rows. Paraphrase row labels in any
  downstream column.
DO: Produce a named pre-map table with >= 3 rows. Carry row labels verbatim into the Map
  Position column in Phase 3.

| Dimension | [columns per focus] |
|-----------|---------------------|

---

PHASE 3 — NAMED COMPETITORS

For each named competitor:
1. Run WebSearch. Cite the source inline (URL or publication).
2. Assign threat level: HIGH / MEDIUM / LOW.
3. Fill Map Position from Phase 2 row label verbatim. An empty or paraphrased cell fails.

| Competitor | Threat | Map Position | [focus columns] | Notes |
|------------|--------|-------------|-----------------|-------|

---

PHASE 4 — WHITESPACE ANALYSIS

C-12 structural constraint. Apparatus: table schema. An absent table or single-row table fails.

DO NOT: Produce a single-row whitespace table. Leave either row without Phase 2 grounding or
  Map Position label reference. Omit the combined paragraph. Write a Focus gap that does not
  require the focus dimension input.
DO: Fill both whitespace rows with findings that require both Phase 2 data and the focus
  dimension simultaneously. Write a combined paragraph (2-3 sentences) naming at least one
  Phase 3 competitor and one Phase 2 row label.

| Gap type | Description | Phase 2 grounding |
|----------|-------------|------------------|
| Competitive gap | | |
| Focus gap | | |

Write a combined paragraph synthesizing both whitespace rows into a single narrative.

---

PHASE 5 — KEY FINDINGS

List 4-6 findings. Each finding must reference at least one named Phase 2 row or Phase 3
competitor by label. No finding may be free-floating.

---

AMEND

Exactly 3 items. Each names: (1) what input changes, (2) what changes in the output.
1. Shift focus dimension (market <-> positioning) — pre-map table restructures; whitespace
   rows shift; combined paragraph changes axis.
2. Add a named competitor — Phase 3 gains a row; findings update if the new competitor
   contests a whitespace gap.
3. Narrow domain to a submarket — pre-map rows focus; inertia mechanisms become more
   specific; portability test becomes more stringent.

---

PRE-SUBMISSION VERIFICATION

For C-11 (pre-map): (1) Format artifact present in output? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
For C-13 (mechanism table): (1) Format artifact present in output — mechanism table, not
  portability summary? (2) Format-failure declared? (3) Bilateral enforcement pair present
  (rejection example + acceptance example)?
For C-12 (whitespace): (1) Format artifact present in output? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
```

---

## V-05 — Combined: Phase Inversion + WRONG/RIGHT + Inertia Manifesto

**Axes:** Role sequence + phrasing register + inertia framing
**Hypothesis:** Phase inversion (V-02) + WRONG/RIGHT labels (V-03) + an inertia manifesto
preamble (new axis) combine cleanly at 180. The manifesto is a contextual frame before SETUP —
it motivates the C-01 and C-06 requirements narratively without replacing any structural element.
Two-sentence opening assertion is retained (not compressed) to isolate V-01's question from
this combination. WRONG/RIGHT labels carry through all three structural constraint phases.
The manifesto adds depth to C-06 (stickiness reasoning pre-motivated) and C-01 (inertia-first
established as principle, not just rule). Expected: **180**.

---

```
All three structural constraints (C-11 pre-map, C-13 inertia mechanisms, C-12 whitespace)
enforce via table schema. An absent table or empty row/cell is an observable format failure.

PRE-GENERATION INTEGRITY CHECK

Before generating any phase output, verify the prompt contains the following elements:
For C-11 (pre-map): (1) Format artifact declared in prompt? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
For C-13 (mechanism table): (1) Format artifact declared in prompt? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
For C-12 (whitespace): (1) Format artifact declared in prompt? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
If any check fails, halt and report the missing element before proceeding.

---

INERTIA FRAME

Before any named vendor enters the analysis, understand this: inertia — the team's current
workflow, spreadsheets, scripts, and informal coordination — is the competitor that wins by
default. It requires no sales motion, no onboarding, and no budget approval. It wins because
it is already in place. Every switching cost, every habit reinforcing the current workflow,
and every workaround that has become good enough is a force multiplier for inertia. A
competitive analysis that treats inertia as one competitor among equals has already
miscalibrated. Assess inertia in full — three mechanism slots — before any named competitor
receives a row.

---

SETUP: Detect the product domain from README, CLAUDE.md, package.json, or any
Glob-discoverable project file. Do not ask the user to name the domain or competitors.
Infer everything from context.

---

PHASE 1 — INERTIA COMPETITOR

Competitor 0: None / status quo. Threat level: HIGH. State explicitly.

Phase 1 produces two tables. Table 1 below is the C-13 structural constraint (mechanism
table). Table 2 below is a portability summary — additional framing only; it does not
substitute for the mechanism table for C-13 apparatus uniformity or C-19 purposes.

C-13 structural constraint. Apparatus: table schema. An absent mechanism table or empty
mechanism row fails.

WRONG: Mechanism table absent; any mechanism row empty; mechanism descriptions generic enough
  to apply equally to a social network, a payroll tool, or a scheduling app.
RIGHT: All three mechanism rows present with domain-specific content; substituting any row
  into a different product category would be obviously wrong.

| Mechanism | Description | Domain-exclusive? |
|-----------|-------------|------------------|
| WORKAROUND SATISFACTION | | |
| SWITCHING COST | | |
| HABIT LOCK-IN | | |

PORTABILITY TEST: Each mechanism must fail if substituted into a different product category.
Exact fail condition: If a mechanism description reads as true for a social network (or
equivalent dissimilar category), it fails.

Portability summary (additional framing only; does not substitute for the mechanism table
above for C-13 or C-19 apparatus uniformity purposes):

| Mechanism | Fails portability test for: | Result |
|-----------|----------------------------|--------|
| WORKAROUND SATISFACTION | | |
| SWITCHING COST | | |
| HABIT LOCK-IN | | |

Run WebSearch to verify domain-specific claims if needed.

---

PHASE 2 — COMPETITIVE LANDSCAPE MAP

C-11 structural constraint. Apparatus: table schema.

IF focus = market sizing:
  Build a market-dimension table: segments, size indicators, growth signals. Minimum 3 named rows.

IF focus = positioning framework:
  Build a positioning-dimension table: axes, poles, current occupation. Minimum 3 named rows.

WRONG: Pre-map table absent; fewer than 3 named rows; row labels paraphrased in any downstream
  column.
RIGHT: Pre-map table present with >= 3 named rows; row labels carried verbatim into the Map
  Position column in Phase 3.

| Dimension | [columns per focus] |
|-----------|---------------------|

---

PHASE 3 — NAMED COMPETITORS

For each named competitor:
1. Run WebSearch. Cite the source inline (URL or publication).
2. Assign threat level: HIGH / MEDIUM / LOW.
3. Fill Map Position from Phase 2 row label verbatim. An empty or paraphrased cell fails.

| Competitor | Threat | Map Position | [focus columns] | Notes |
|------------|--------|-------------|-----------------|-------|

---

PHASE 4 — WHITESPACE ANALYSIS

C-12 structural constraint. Apparatus: table schema. An absent table or single-row table fails.

WRONG: Single-row whitespace table; either row lacks Phase 2 grounding or Map Position label
  reference; combined paragraph absent; Focus gap independent of the focus dimension input.
RIGHT: Both rows present; each grounded in a Phase 2 entry or Map Position label; Focus gap
  requires both Phase 2 data and the focus dimension simultaneously; combined paragraph
  synthesizes across both rows naming at least one Phase 3 competitor and one Phase 2 label.

| Gap type | Description | Phase 2 grounding |
|----------|-------------|------------------|
| Competitive gap | | |
| Focus gap | | |

Write a combined paragraph synthesizing both whitespace rows into a single narrative.

---

PHASE 5 — KEY FINDINGS

List 4-6 findings. Each finding must reference at least one named Phase 2 row or Phase 3
competitor by label. No finding may be free-floating.

---

AMEND

Exactly 3 items. Each names: (1) what input changes, (2) what changes in the output.
1. Shift focus dimension (market <-> positioning) — pre-map table restructures; whitespace
   rows shift; combined paragraph changes axis.
2. Add a named competitor — Phase 3 gains a row; findings update if the new competitor
   contests a whitespace gap.
3. Narrow domain to a submarket — pre-map rows focus; inertia mechanisms become more
   specific; portability test becomes more stringent.

---

PRE-SUBMISSION VERIFICATION

For C-11 (pre-map): (1) Format artifact present in output? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
For C-13 (mechanism table): (1) Format artifact present in output — mechanism table, not
  portability summary? (2) Format-failure declared? (3) Bilateral enforcement pair present
  (rejection example + acceptance example)?
For C-12 (whitespace): (1) Format artifact present in output? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
```

---

## Variation Summary

| # | Axes | C-23 | C-24 | C-25 | C-26 | Expected |
|---|------|------|------|------|------|---------|
| V-01 | Lifecycle (1-sentence opening) | PASS (5) | PASS? (5) | PASS real (5) | PASS (5) | **180** or **170** |
| V-02 | Role sequence (phase inversion) | PASS (5) | PASS (5) | PASS real (5) | PASS (5) | **180** |
| V-03 | Phrasing register (WRONG/RIGHT) | PASS? (5) | PASS (5) | PASS real (5) | PASS (5) | **180** or **177.5** |
| V-04 | Lifecycle + role sequence | PASS (5) | PASS? (5) | PASS real (5) | PASS (5) | **180** or **170** |
| V-05 | Role seq + phrasing + inertia framing | PASS? (5) | PASS (5) | PASS real (5) | PASS (5) | **180** or **177.5** |

*Baseline: R1 V-05 = 180. All five R2 variations expect 180; deviations reveal rubric sensitivity.*

**Key discriminators:**
- V-01 isolates whether a single em-dash sentence is sufficient for C-14/C-17 under C-24
- V-02 isolates whether C-11 is phase-label sensitive ("Phase 1" literal) or phase-concept sensitive (pre-map table, wherever it appears)
- V-03 isolates whether WRONG/RIGHT is "equivalent structural framing" for C-23 (FULL PASS) or label-specific (PARTIAL)
- V-04 stacks V-01 + V-02 to detect unexpected criterion interactions
- V-05 stacks V-02 + V-03 + inertia manifesto to test the full combined robustness ceiling
