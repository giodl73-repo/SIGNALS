Five complete variations written to `simulations/quest/variations/discover-competitors-alt-variations-R1-2026-03-17.md`.

**R1 setup:** R6 achieved 160/160 under v6 rubric. v7/v8 added C-23–C-26 (20 pts, max 180). Under v8, the R6 baseline scores **165** (C-25 vacuous pass gives +5; C-23/C-24/C-26 all fail).

| # | Axis | Hypothesis | Expected |
|---|------|------------|----------|
| V-01 | Phrasing register | DO NOT/DO in instructions + "bilateral enforcement pair present?" in loop satisfies C-23 FULL PASS | **170** |
| V-02 | Role sequence | SR-block-free + opening assertion + phase-embedded declarations satisfies C-24 without breaking C-14/C-17/C-18–C-22 | **170** |
| V-03 | Phrasing register (boundary) | DO NOT/DO in instructions + FAILS/PASS in loop yields C-23 PARTIAL (2.5) — confirms loop language is the full/partial determinant | **167.5** |
| V-04 | Lifecycle emphasis | Pre-generation prompt-completeness loop + post-generation output-completeness loop satisfies C-26 | **170** |
| V-05 | Combined | All four new criteria: C-23 + C-24 + C-25 (real, not vacuous) + C-26 | **180** |

**Four open questions R1 will resolve:**
1. Is DO NOT/DO + label-agnostic loop truly C-23 PASS (5) vs PARTIAL (2.5)?
2. Does SR-block removal (V-02) preserve all 7 criteria from C-18–C-24 that depend on the preamble structure?
3. Does C-23 split precisely at loop language — confirming PARTIAL when instructions are label-agnostic but loop is FAILS/PASS?
4. Does the pre-generation loop's "prompt subject" vs post-generation loop's "output subject" satisfy C-26's non-competing requirement?
ithout any degradation?
3. Is the C-23 PARTIAL path (label-agnostic instructions / label-specific loop) confirmed to be PARTIAL, not FAIL?
4. Does the pre-generation loop check prompt completeness (not output correctness) in a way that satisfies C-26's "different subjects" requirement?

---

## V-01 — Label-Agnostic Bilateral Pairs (C-23 PASS)

**Axis:** Phrasing register
**Hypothesis:** Using DO NOT/DO bilateral pairs in all three phase-level structural constraint
instructions, AND using "bilateral enforcement pair present (rejection example + acceptance
example)?" in the verification loop, satisfies C-23 fully. SR block retained for C-14/C-17.
Expected: C-23 PASS (+5), C-24 FAIL (0), C-25 PASS vacuous (+5 unchanged), C-26 FAIL (0) = **170**.

---

```
SETUP: Detect the product domain from README, CLAUDE.md, package.json, or any
Glob-discoverable project file. Do not ask the user to name the domain or competitors.
Infer everything from context.

STRUCTURAL REQUIREMENTS

SR1 (C-11): Pre-map table required when focus dimension is provided. Apparatus: table schema.
An absent table or absent row fails. Row labels must appear verbatim downstream.

SR2 (C-13): Inertia mechanism table required. Three rows: WORKAROUND SATISFACTION, SWITCHING
COST, HABIT LOCK-IN. Apparatus: table schema. An absent table or empty row fails.

SR4 (C-12): Whitespace table required. Two rows: Competitive gap, Focus gap. Apparatus: table
schema. An absent table or single-row table fails.

All three primary structural requirements (SR1, SR2, SR4) enforce via table schema. An absent
table or empty row/cell is an observable format failure.

Enforcement symmetry: SR1, SR2, and SR4 each carry an identical three-component enforcement
apparatus — a named format artifact (table schema), a format-failure declaration, and a
bilateral enforcement pair (rejection example + acceptance example) at phase instruction level.

---

PHASE 1 — COMPETITIVE LANDSCAPE MAP

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

The most dangerous competitor in almost every product market is not a named vendor — it is the
team's existing way of doing things. Assess inertia first.

Competitor 0: None / status quo. Threat level: HIGH. State explicitly.

INERTIA MECHANISMS (SR2 structural constraint; mechanism table required)

DO NOT: Omit the mechanism table. Leave any mechanism row empty. Write mechanism descriptions
  so generic they would apply equally to a social network, a payroll tool, or a scheduling app.
DO: Fill all three mechanism rows with content so domain-specific that substituting it into a
  different product category would be obviously wrong. Run the portability test on every row.

| Mechanism | Description | Portability test |
|-----------|-------------|-----------------|
| WORKAROUND SATISFACTION | | |
| SWITCHING COST | | |
| HABIT LOCK-IN | | |

PORTABILITY TEST: Each mechanism must fail if substituted into a different product category.
Exact fail condition: If a mechanism description reads as true for a social network (or
equivalent dissimilar category), it fails.

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

DO NOT: Produce a single-row whitespace table. Leave either row without Phase 1 grounding or
  Map Position label reference. Omit the combined paragraph. Produce a Focus gap row that
  could exist without the focus dimension input.
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

For SR1 (C-11): (1) Format artifact present? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
For SR2 (C-13): (1) Format artifact present? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
For SR4 (C-12): (1) Format artifact present? (2) Format-failure declared?
  (3) Bilateral enforcement pair present (rejection example + acceptance example)?
```

---

## V-02 — SR-Block-Free Architecture (C-24 PASS)

**Axis:** Role sequence (SR block placement / existence)
**Hypothesis:** Removing the numbered SR preamble block entirely and satisfying C-14/C-17
via (a) a two-sentence opening symmetry assertion naming all three constraints and the
apparatus type, and (b) phase-embedded "C-XX structural constraint. Apparatus: table schema."
declarations at each constraint phase, preserves all of C-14, C-17, C-18, C-19, C-20, C-21,
C-22 and additionally satisfies C-24. Uses standard FAILS/PASS throughout (C-23 FAIL).
Expected: C-23 FAIL (0), C-24 PASS (+5), C-25 PASS vacuous (+5 unchanged), C-26 FAIL (0) = **170**.

---

```
All three structural constraints (C-11 pre-map, C-13 inertia mechanisms, C-12 whitespace)
enforce via table schema. An absent table or empty row/cell is an observable format failure.

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

FAILS: Pre-map table absent; fewer than 3 named rows; row labels paraphrased downstream.
PASS: Pre-map table present with >= 3 named rows; labels appear verbatim in downstream
  Map Position column.

| Dimension | [columns per focus] |
|-----------|---------------------|

---

PHASE 2 — INERTIA COMPETITOR

The most dangerous competitor in almost every product market is not a named vendor — it is the
team's existing way of doing things. Assess inertia first.

Competitor 0: None / status quo. Threat level: HIGH. State explicitly.

C-13 structural constraint. Apparatus: table schema. An absent table or empty mechanism row fails.

FAILS: Mechanism table absent; any mechanism row empty; row content passes the portability
  test for a different product category.
PASS: All three mechanism rows present; each row is domain-exclusive; portability test confirms.

| Mechanism | Description | Portability test |
|-----------|-------------|-----------------|
| WORKAROUND SATISFACTION | | |
| SWITCHING COST | | |
| HABIT LOCK-IN | | |

PORTABILITY TEST: Each mechanism must fail if substituted into a different product category.
Exact fail condition: If a mechanism description reads as true for a social network (or
equivalent dissimilar category), it fails.

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

FAILS: Whitespace table absent; single-row table; either row lacks Phase 1 grounding or Map
  Position label reference; combined paragraph absent.
PASS: Both rows present; each row names a Phase 1 entry or Map Position label; Focus gap row
  requires both Phase 1 data and the focus dimension; combined paragraph synthesizes across both.

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

For C-11 (pre-map): (1) Format artifact present? (2) Format-failure declared?
  (3) FAILS/PASS pair present?
For C-13 (mechanism table): (1) Format artifact present? (2) Format-failure declared?
  (3) FAILS/PASS pair present?
For C-12 (whitespace): (1) Format artifact present? (2) Format-failure declared?
  (3) FAILS/PASS pair present?
```

---

## V-03 — C-23 Partial Boundary Test (DO NOT/DO instructions + FAILS/PASS loop)

**Axis:** Phrasing register (C-23 partial path)
**Hypothesis:** Using DO NOT/DO bilateral pairs in phase instructions (satisfying the
instruction-level half of C-23) while retaining "FAILS/PASS pair present?" in the verification
loop (the label-specific loop fails the loop-level half of C-23) yields C-23 PARTIAL (2.5),
not C-23 FULL PASS (5). Confirms the C-23 partial/full boundary is loop language, not
instruction language. SR block retained. Single loop only.
Expected: C-23 PARTIAL (+2.5), C-24 FAIL (0), C-25 PASS vacuous (+5 unchanged), C-26 FAIL (0) = **167.5**.

---

```
SETUP: Detect the product domain from README, CLAUDE.md, package.json, or any
Glob-discoverable project file. Do not ask the user to name the domain or competitors.
Infer everything from context.

STRUCTURAL REQUIREMENTS

SR1 (C-11): Pre-map table required when focus dimension is provided. Apparatus: table schema.
An absent table or absent row fails. Row labels must appear verbatim downstream.

SR2 (C-13): Inertia mechanism table required. Three rows: WORKAROUND SATISFACTION, SWITCHING
COST, HABIT LOCK-IN. Apparatus: table schema. An absent table or empty row fails.

SR4 (C-12): Whitespace table required. Two rows: Competitive gap, Focus gap. Apparatus: table
schema. An absent table or single-row table fails.

All three primary structural requirements (SR1, SR2, SR4) enforce via table schema. An absent
table or empty row/cell is an observable format failure.

Enforcement symmetry: SR1, SR2, and SR4 each carry an identical three-component enforcement
apparatus — a named format artifact (table schema), a format-failure declaration, and a
rejection example + acceptance example pair at phase instruction level.

---

PHASE 1 — COMPETITIVE LANDSCAPE MAP

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

The most dangerous competitor in almost every product market is not a named vendor — it is the
team's existing way of doing things. Assess inertia first.

Competitor 0: None / status quo. Threat level: HIGH. State explicitly.

INERTIA MECHANISMS (SR2 structural constraint; mechanism table required)

DO NOT: Omit the mechanism table. Leave any mechanism row empty. Write mechanism descriptions
  generic enough to describe a social network, a payroll tool, or a scheduling app equally.
DO: Fill all three mechanism rows with content so domain-specific that substituting it into a
  different product category would be obviously wrong. Run the portability test on every row.

| Mechanism | Description | Portability test |
|-----------|-------------|-----------------|
| WORKAROUND SATISFACTION | | |
| SWITCHING COST | | |
| HABIT LOCK-IN | | |

PORTABILITY TEST: Each mechanism must fail if substituted into a different product category.
Exact fail condition: If a mechanism description reads as true for a social network (or
equivalent dissimilar category), it fails.

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

DO NOT: Produce a single-row whitespace table. Leave either row without Phase 1 grounding or
  Map Position label reference. Omit the combined paragraph. Produce a Focus gap row that
  does not require the focus dimension input to exist.
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

For SR1 (C-11): (1) Format artifact present? (2) Format-failure declared?
  (3) FAILS/PASS pair present?
For SR2 (C-13): (1) Format artifact present? (2) Format-failure declared?
  (3) FAILS/PASS pair present?
For SR4 (C-12): (1) Format artifact present? (2) Format-failure declared?
  (3) FAILS/PASS pair present?
```

---

## V-04 — Dual-Loop Verification Architecture (C-26 PASS)

**Axis:** Lifecycle emphasis (verification loop placement and subject)
**Hypothesis:** Adding a PRE-GENERATION INTEGRITY CHECK at the prompt opening that asks
per-constraint prompt-completeness questions (format artifact declared in prompt?
format-failure declared in prompt? bilateral enforcement pair present in prompt?) — covering
all three structural constraints — while retaining the standard post-generation
PRE-SUBMISSION VERIFICATION loop (output completeness) satisfies C-26. The two loops check
different subjects (prompt vs. output) and are non-competing. C-20 is satisfied by the
closing loop; C-26 is satisfied by both loops together. Uses standard FAILS/PASS throughout.
Expected: C-23 FAIL (0), C-24 FAIL (0), C-25 PASS vacuous (+5 unchanged), C-26 PASS (+5) = **170**.

---

```
PRE-GENERATION INTEGRITY CHECK

Before generating any phase output, verify the prompt contains the following elements:
For C-11 (pre-map table):
  (1) Format artifact declared in prompt? (2) Format-failure declared in prompt?
  (3) Bilateral enforcement pair present in prompt?
For C-13 (mechanism table):
  (1) Format artifact declared in prompt? (2) Format-failure declared in prompt?
  (3) Bilateral enforcement pair present in prompt?
For C-12 (whitespace table):
  (1) Format artifact declared in prompt? (2) Format-failure declared in prompt?
  (3) Bilateral enforcement pair present in prompt?
If any check fails, halt and report the missing element before proceeding.

---

SETUP: Detect the product domain from README, CLAUDE.md, package.json, or any
Glob-discoverable project file. Do not ask the user to name the domain or competitors.
Infer everything from context.

STRUCTURAL REQUIREMENTS

SR1 (C-11): Pre-map table required when focus dimension is provided. Apparatus: table schema.
An absent table or absent row fails. Row labels must appear verbatim downstream.

SR2 (C-13): Inertia mechanism table required. Three rows: WORKAROUND SATISFACTION, SWITCHING
COST, HABIT LOCK-IN. Apparatus: table schema. An absent table or empty row fails.

SR4 (C-12): Whitespace table required. Two rows: Competitive gap, Focus gap. Apparatus: table
schema. An absent table or single-row table fails.

All three primary structural requirements (SR1, SR2, SR4) enforce via table schema. An absent
table or empty row/cell is an observable format failure.

Enforcement symmetry: SR1, SR2, and SR4 each carry an identical three-component enforcement
apparatus — a named format artifact (table schema), a format-failure declaration, and a
FAILS/PASS rejection example pair at phase instruction level.

---

PHASE 1 — COMPETITIVE LANDSCAPE MAP

IF focus = market sizing:
  Build a market-dimension table: segments, size indicators, growth signals. Minimum 3 named rows.

IF focus = positioning framework:
  Build a positioning-dimension table: axes, poles, current occupation. Minimum 3 named rows.

FAILS: Pre-map table absent; fewer than 3 named rows; row labels paraphrased downstream.
PASS: Pre-map table present with >= 3 named rows; labels appear verbatim in downstream
  Map Position column.

| Dimension | [columns per focus] |
|-----------|---------------------|

---

PHASE 2 — INERTIA COMPETITOR

The most dangerous competitor in almost every product market is not a named vendor — it is the
team's existing way of doing things. Assess inertia first.

Competitor 0: None / status quo. Threat level: HIGH. State explicitly.

INERTIA MECHANISMS (SR2 structural constraint; mechanism table required)

FAILS: Mechanism table absent; any mechanism row empty; row content passes the portability
  test for a different product category.
PASS: All three mechanism rows present; each row is domain-exclusive; portability test confirms.

| Mechanism | Description | Portability test |
|-----------|-------------|-----------------|
| WORKAROUND SATISFACTION | | |
| SWITCHING COST | | |
| HABIT LOCK-IN | | |

PORTABILITY TEST: Each mechanism must fail if substituted into a different product category.
Exact fail condition: If a mechanism description reads as true for a social network (or
equivalent dissimilar category), it fails.

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

FAILS: Whitespace table absent; single-row table; either row lacks Phase 1 grounding or Map
  Position label reference; combined paragraph absent.
PASS: Both rows present; each row names a Phase 1 entry or Map Position label; Focus gap row
  requires both Phase 1 data and the focus dimension simultaneously; combined paragraph
  synthesizes across both rows.

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

For SR1 (C-11): (1) Format artifact present in output? (2) Format-failure declared?
  (3) FAILS/PASS pair present?
For SR2 (C-13): (1) Format artifact present in output? (2) Format-failure declared?
  (3) FAILS/PASS pair present?
For SR4 (C-12): (1) Format artifact present in output? (2) Format-failure declared?
  (3) FAILS/PASS pair present?
```

---

## V-05 — Full Synthesis (C-23 + C-24 + C-25 + C-26)

**Axis:** Combined — all four new criteria simultaneously
**Hypothesis:** Combining SR-block-free architecture (C-24), label-agnostic bilateral pairs
in phase instructions AND in the verification loop (C-23), intentional multi-table Phase 2
with explicit constraint designation tokens and companion non-substitutability declarations
(C-25), and dual-loop verification with different subjects (C-26) achieves 180/180.
Expected: C-23 PASS (+5), C-24 PASS (+5), C-25 PASS real (+5, unchanged), C-26 PASS (+5) = **180**.

Phase 2 produces two tables: (1) the mechanism table — the C-13 structural constraint —
and (2) a portability summary table — additional framing only, not a structural constraint.
This makes C-25 non-vacuous and tests real disambiguation.

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

## Variation Summary

| # | C-23 | C-24 | C-25 | C-26 | Expected |
|---|------|------|------|------|----------|
| V-01 | PASS (5) | FAIL (0) | PASS vacuous (5) | FAIL (0) | 170 |
| V-02 | FAIL (0) | PASS (5) | PASS vacuous (5) | FAIL (0) | 170 |
| V-03 | PARTIAL (2.5) | FAIL (0) | PASS vacuous (5) | FAIL (0) | 167.5 |
| V-04 | FAIL (0) | FAIL (0) | PASS vacuous (5) | PASS (5) | 170 |
| V-05 | PASS (5) | PASS (5) | PASS real (5) | PASS (5) | 180 |

*Baseline under v8 rubric: 165 (C-01–C-22: 160, C-25 vacuous: 5, C-23/C-24/C-26: 0)*

**Key discriminators:**
- V-01 vs. V-03 isolates whether loop language is the determinant for C-23 full/partial split
- V-02 confirms SR-block removal doesn't break any of C-14, C-17, C-18, C-19, C-20, C-21, C-22
- V-04 confirms the pre-generation / post-generation dual-loop satisfies C-26's "different subjects" requirement
- V-05 synthesizes all four new axes and tests the 180 ceiling
