## review-customers R2 Results

**Scores:**

| Variation | Score | Misses |
|-----------|-------|--------|
| V-01 Hybrid format | 94/100 | C-11 PARTIAL |
| V-02 Causal rationale | 76/100 | C-11 FAIL, C-12 FAIL |
| V-03 Inline flags isolated | 82/100 | C-12 FAIL, C-13 PARTIAL |
| V-04 Full C-11+C-12+C-13 | 94/100 | C-11 PARTIAL |
| V-05 Causal conversational + hybrid | **100/100** | All pass |

---

**The binding variable in R2 is C-11 adjacency.** The question isn't whether inline flags are present -- V-01/V-03/V-04/V-05 all have them. The question is whether the flag lands adjacent to the offending score or in a separate structure.

**V-05 wins (100)** because prose-first ordering makes scores and flags colocate in the same per-persona block. The flag is on the header; the scores are in the bullets immediately below. The table is then compiled from already-flagged reasoning -- a verified summary, not a preliminary structure.

**V-01 and V-04 both earn 94 (C-11 PARTIAL)**: Both are table-first hybrids. The scores live in Phase 2; the flags land in Phase 3 prose headers. A blocker in the table row isn't marked until a different section of the output. The phase gates in V-04 reduce omission risk but don't fix the structural adjacency gap.

**V-03 earns 82**: C-11 PASS confirmed -- the inline mechanism works without 7 phases. But the combined per-entry format sacrifices C-12 (no separate table layer), and the causal framing instruction is weaker than the others (C-13 PARTIAL).

**V-02 earns 76**: Contains the strongest C-13 instruction in the set (worked anti-pattern example with specific domain language). But pure conversational format has no table (C-12 FAIL) and no inline flag mechanism (C-11 FAIL).

---

**New patterns for R3:**
1. Prose-first ordering resolves the C-11 adjacency gap structurally
2. V-02's worked anti-pattern C-13 example is more precise than abstract framing rules -- should be merged into V-05
3. V-03's "Do not defer flags" prohibition is the strongest C-11 enforcement language -- should also be imported into V-05

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["prose-first-ordering-resolves-C11-adjacency-gap", "worked-antipattern-examples-outperform-abstract-framing-rules", "table-first-hybrid-creates-score-flag-phase-gap"]}
```
-outperform-abstract-framing-rules", "table-first-hybrid-creates-score-flag-phase-gap"]}
```

---

## Per-Criterion Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 All 12 personas | PASS | PASS | PASS | PASS | PASS |
| C-02 Weighted aggregate | PASS | PASS | PASS | PASS | PASS |
| C-03 Adoption blockers | PASS | PASS | PASS | PASS | PASS |
| C-04 Positioning leaks | PASS | PASS | PASS | PASS | PASS |
| C-05 Tier assignment | PASS | PASS | PASS | PASS | PASS |
| C-06 Delight signals | PASS | PASS | PASS | PASS | PASS |
| C-07 Amendment order | PASS | PASS | PASS | PASS | PASS |
| C-08 Per-persona rationale | PASS | PASS | PASS | PASS | PASS |
| C-09 Cross-persona pattern | PASS | PASS | PASS | PASS | PASS |
| C-10 Amend-to-score projection | PASS | PASS | PASS | PASS | PASS |
| C-11 Inline flags (aspirational) | PARTIAL | FAIL | PASS | PARTIAL | PASS |
| C-12 Hybrid format (aspirational) | PASS | FAIL | FAIL | PASS | PASS |
| C-13 Causal rationale (aspirational) | PASS | PASS | PARTIAL | PASS | PASS |

---

## Detailed Scoring

### V-01 -- 94/100

**Hybrid format (single-axis C-12 test).** All essentials and recommended pass. Among aspirational:
C-12 and C-13 pass; C-11 earns PARTIAL.

**C-11 PARTIAL**: The inline flag instruction exists ("Apply inline flags to the persona header
line before the prose, based on Phase 2 table") but the flags land in Phase 3 headers while the
offending scores live in the Phase 2 table. The rubric requires inline markers "adjacent to the
offending score." A blocker in the table row is not marked until Phase 3's prose header -- a
different section of the output. The structural gap is real: a model following V-01 could score
a primary persona Would-Adopt: 2 in the table, then omit the [BLOCKER] flag in Phase 3, with no
mechanism to prevent it. This earns PARTIAL, not FAIL, because the flag mechanism is present and
the Phase 4 DETECT section would catch any omission -- the reliability is lower than PASS but the
system is not blind to blockers.

**C-12 PASS**: V-01's core axis. Phase 2 mandates the complete 12-row scoring table (completeness
layer). Phase 3 mandates 2-3 sentence prose blocks per persona (rationale layer). "Both layers
are required." The trade-off from R1 V-02 (table-only, rationale depth capped) is structurally
resolved.

**C-13 PASS**: Phase 3 requires "The rationale must implicate the feature, not just describe the
persona's role or preferences. 'The feature's [X] produced this reaction' -- not 'This persona
values [Y].'" The explicit causal contrast passes the C-13 instruction bar.

**Verdict**: Strong hybrid implementation. C-11 PARTIAL is the sole gap. The fix is structural:
move flags into the Phase 2 table row (or use prose-first ordering as in V-05).

---

### V-02 -- 76/100

**Causal rationale isolated (single-axis C-13 test).** All essentials, recommended, C-09, and
C-10 pass. C-11 and C-12 both FAIL.

**C-11 FAIL**: No inline flag mechanism anywhere in V-02. The prompt has post-hoc sections
("IS ADOPTION BLOCKED?", "IS THE POSITIONING LEAKING?") but no [BLOCKER]/[LEAK] markers are
applied during scoring. Blockers and leaks are identified reactively, not at the point of
discovery. Two or more personas would qualify as blockers/leaks in a typical run without any
inline marker. FAIL confirmed.

**C-12 FAIL**: V-02 is pure conversational prose with no summary table. The tier declaration
("Write it out for all twelve: 'C-01 Maria Chen -- primary'") creates a list but not a scoring
structure. C-12 requires both a structured summary (table) with all 12 personas and three
numeric scores, AND prose rationale blocks. V-02 has only prose. FAIL confirmed.

**C-13 PASS**: V-02 contains the strongest C-13 instruction of all five variations. The framing
provides both the positive rule ("name the specific feature property, design gap, or workflow
fit/mismatch as the driver") and a worked anti-pattern with specificity: "Not 'This persona
values [thing]' -- but 'the feature requires [X], which this persona's workflow does not support
yet.'" The explicit worked example anchors the model's behavior more concretely than a framing
rule alone. Strongest C-13 instruction in the set.

**Verdict**: V-02 is the C-13 isolation proof: the causal framing instruction works at full
strength. But the conversational format structurally eliminates both C-11 and C-12. V-02's
C-13 instruction should be merged into V-05 for R3 as the richest available causal framing.

---

### V-03 -- 82/100

**Inline flags isolated (single-axis C-11 test).** All essentials, recommended, C-09, C-10,
and C-11 pass. C-12 FAIL and C-13 PARTIAL.

**C-11 PASS**: V-03's core axis. The per-entry format places the flag rules on the scoring
header with the scores immediately below:

  [C-NN] [Name] ([Role]) | Tier: [tier] | [inline flags]
  - Usefulness [1-5]: [score]
  - Clarity [1-5]: [score]
  - Would-Adopt [1-5]: [score]

The flag and the offending score are in the same entry block. "Flags go on the header line --
not in the rationale block. Do not defer flags to the findings sections -- they must appear
here, adjacent to the scores that triggered them." The explicit "Do not defer" prohibition is
the strongest C-11 language in the set. PASS.

**C-12 FAIL**: V-03 uses a combined per-entry format (header + score bullets + rationale) with
no separate summary table. The TIER ASSIGNMENT list before scoring creates a tier register but
not a scored summary structure with numeric values for all 12 personas in one place. C-12
requires both a summary structure AND prose blocks as distinct layers. V-03 merges both into
one entry format, satisfying neither as a distinct layer. FAIL.

**C-13 PARTIAL**: V-03 has "Identify the specific feature property, design gap, or workflow
fit/mismatch that produced these scores -- not just what this persona values in general." This
is directional causal instruction. It names the target (feature property/gap) and adds the
negative constraint ("not just what this persona values"). But it lacks the explicit framing
contrast -- "The feature's [X] produced this reaction" -- that appears in V-01/V-02/V-04/V-05.
The instruction will produce causal rationale in some runs but is less reliable than the
positive framing model. PARTIAL: likely 6-8 of 12 personas qualify rather than a consistent
8+.

**Verdict**: C-11 mechanism confirmed as orthogonal to phase complexity. V-03 achieves full
C-11 PASS without 7 phases. The C-11 mechanism CAN be backported cheaply. But V-03 shows the
cost: the combined per-entry format that enables C-11 adjacency sacrifices C-12's hybrid
structure guarantee, and the weaker C-13 instruction leaves causal depth unreliable.

---

### V-04 -- 94/100

**Full C-11 + C-12 + C-13 combined (all three new criteria).** All essentials, recommended,
C-09, C-10, C-12, and C-13 pass. C-11 PARTIAL.

**C-11 PARTIAL**: V-04 inherits V-01's phase architecture: scores in Phase 2 table, flags in
Phase 3 prose headers. The instruction is explicit ("Apply inline flags to the persona header
line, based on Phase 2 table scores") but the structural gap remains. A blocker in Phase 2
table row is not flagged until Phase 3 header -- a different output section. Same PARTIAL
reasoning as V-01. V-04's explicit "Do not proceed" phase gates make omission less likely than
V-01 (the model must enter Phase 3 and write all 12 prose blocks), but the adjacency gap is
still present by design.

**C-12 PASS**: Phase 2 = scoring table (completeness layer). Phase 3 = causal prose blocks
(rationale layer). "Two rules: 1. Do not restate the scores. 2. Name the specific feature
property, design gap, or workflow fit/mismatch that drove the scores." Both required.

**C-13 PASS**: Phase 3 rule 2 is the most explicit C-13 instruction among table-first
variations: "Rationale that only describes the persona's context or preferences without
implicating a specific element of the feature is contextual, not causal. Causal rationale is
required for every persona." The "contextual, not causal" framing distinction directly maps to
C-13's pass criteria. Stronger than V-01's C-13 instruction.

**V-04 vs V-01**: Same score (94). V-04 has stronger C-13 instruction and explicit phase
gates. V-01 is simpler. Neither resolves the C-11 PARTIAL because both are table-first hybrids
with the score-flag phase gap. The phase gates in V-04 reduce omission risk but do not fix the
structural adjacency issue.

**Verdict**: V-04 is the maximum achievable for table-first hybrid format. The C-11 PARTIAL
is structural, not fixable by instruction improvement without changing the ordering model.

---

### V-05 -- 100/100

**Prose-first hybrid (C-12 + C-13 in conversational register).** All 13 criteria pass.

**C-11 PASS**: V-05's prose-first ordering is what makes C-11 work cleanly. The per-persona
block contains:

  [C-NN] Name | tier | [BLOCKER] / [LEAK] / [DELIGHT: dimension]
  - Usefulness: [1-5]
  - Clarity: [1-5]
  - Would-Adopt: [1-5]
  [2-3 sentence causal explanation]

The inline flags appear on the header line; the offending scores appear in the bullet points
immediately below. They are adjacent within the same per-persona block. After reasoning through
all 12, the table is compiled as a summary. The table inherits verified flag-adjacent scores;
it is a verified output, not a preliminary structure that the model must later annotate.
Compare to V-01/V-04: the Phase 2 table is built first with no flags, creating a gap that
Phase 3 must retroactively close by applying flags to prose headers. V-05 eliminates this gap
by keeping scores and flags colocated.

**C-12 PASS**: Prose-first hybrid satisfies C-12 in a different ordering than V-01/V-04: per-
persona prose blocks (with inline scores and 2-3 sentence rationale) serve as the depth layer;
the compiled table at the end is the completeness/auditability layer. "All 12 rows and all
tier labels are required. The table is a summary of the reasoning above -- not a scoring step."
Both structures are present and serve their distinct purposes.

**C-13 PASS**: V-05 contains the second-strongest C-13 instruction. The positive framing
("The feature's lack of [X] means this persona cannot integrate it into [specific workflow
step], which is why would-adopt lags usefulness"), the explicit negative anti-pattern ("Not
'this persona values reliability'"), and the summary rule ("The explanation must implicate the
feature, not just describe the person") produce reliable C-13 output. The worked example is
specific enough to anchor model behavior on the causal framing.

**Additional strengths retained from V-05 R1**: Adoption blockers are declared during scoring
(inline) rather than discovered post-hoc. The C-10 projection formula ("likely lifts primary
W-Adopt by ~[delta], moving weighted composite from [current] to approximately [current +
effect]") is present. The C-09 cross-persona pattern instruction explicitly requires naming
a feature mechanism ("Generic observations ('scores vary') do not qualify").

**Verdict**: V-05 is the correct working prompt for R3. The prose-first ordering is not just
a format choice -- it resolves the structural tension between C-11 adjacency (needs scores and
flags colocated) and C-12 hybrid (needs both table and prose). Prose-first achieves both by
making the table a compiled summary of already-flagged reasoning.

---

## Rankings

| Rank | Variation | Score | Key differentiator |
|------|-----------|-------|--------------------|
| 1 | V-05 Causal conversational + hybrid | 100 | Prose-first: scores and flags colocated; all 13 criteria pass |
| 2 | V-01 Hybrid format | 94 | C-12 PASS (core axis); C-11 PARTIAL from score-flag phase gap |
| 2 | V-04 Full C-11+C-12+C-13 | 94 | Strongest C-13 instruction; same C-11 PARTIAL as V-01 |
| 4 | V-03 Inline flags isolated | 82 | C-11 PASS confirmed; C-12 structural sacrifice; C-13 PARTIAL |
| 5 | V-02 Causal rationale | 76 | Strongest C-13 instruction; no table = C-12 FAIL; no flags = C-11 FAIL |

**Tie-breaking V-01 vs V-04**: Both earn 94. V-04 has stronger C-13 framing ("contextual,
not causal" distinction) and phase gates that reduce omission risk. V-01 is structurally
simpler. For production use, V-04 is marginally preferable if table-first hybrid is required
for integration reasons. But the correct direction is V-05.

---

## Essential Criterion Pass Analysis

All 5 variations pass all 5 essential criteria (C-01 through C-05). The essential floor
established in R1 holds. R2's differentiators are entirely in the aspirational tier (C-11
through C-13).

**Implication for R3**: The rubric has been stabilized. All 13 criteria have strong prompting
solutions. R3 should test V-05 on a live topic run to validate that the 100/100 prompt-level
score produces 100/100 output-level scoring. The new patterns below are the primary candidates
for investigation:

1. Does V-02's worked anti-pattern C-13 instruction, merged into V-05's prose-first structure,
   produce stronger C-13 output than V-05 alone?
2. Does the prose-first ordering constraint in V-05 require any adjustment for longer topics
   where 12 prose blocks before the table may cause model truncation?
3. Is C-11 PASS in V-03 (combined-format inline) sufficient for production reliability, or
   does the prose-first table compilation in V-05 provide meaningfully higher reliability
   on actual runs?

---

## Excellence Signals (from top-scoring variation)

1. **Prose-first ordering** resolves the C-11 adjacency requirement without sacrificing C-12.
   The table becomes a verified summary of flagged reasoning rather than an unflagged structure
   that flags must be retroactively applied to.

2. **Worked anti-pattern specificity** in C-13 instruction ("Not 'this persona values
   reliability' -- but 'the feature's lack of [X] means this persona cannot integrate it into
   [specific workflow step]'") is more actionable than a framing rule because it shows the
   model exactly what the wrong output looks like alongside the right output.

3. **Score-anchored C-10 projection** ("from [current] to approximately [current + effect]")
   is present in V-05 and makes the projection auditable against actual composite scores.

4. **"The table is a summary of the reasoning above -- not a scoring step"** is the right
   mental model for prose-first hybrid. It prevents the model from treating the table as the
   scoring authority and the prose as secondary commentary.

5. **V-03's "Do not defer flags" prohibition** is the strongest C-11 enforcement language
   even though V-03 sacrifices C-12. This language should be imported into V-05 for R3.

---

## New Patterns

1. **Prose-first ordering resolves C-11 adjacency**: Scores written in prose, flags on
   the prose header line -- they are adjacent by construction. Table compiled after reasoning
   inherits the flag-labeled results. Table-first formats cannot achieve C-11 adjacency
   without restructuring the scoring entry format.

2. **Worked anti-pattern examples outperform abstract framing rules for C-13**: V-02's
   "Not 'this persona values reliability' -- but 'the feature's lack of [X] means...'" is
   more precise than V-01's "'The feature's [X] produced this reaction' -- not 'This persona
   values [Y].'" Both are causal-framing instructions, but the worked example with a specific
   domain ("workflow step," "would-adopt lags usefulness") anchors model behavior more
   concretely than a generic slot-fill template.

3. **Table-first hybrid creates a score-flag phase gap**: The hybrid ordering (table Phase 2 +
   prose Phase 3) structurally separates scores from flags. This is remediable only by either
   (a) adding flags to the table rows themselves (breaking the "completeness layer only"
   discipline) or (b) inverting to prose-first ordering.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["prose-first-ordering-resolves-C11-adjacency-gap", "worked-antipattern-examples-outperform-abstract-framing-rules", "table-first-hybrid-creates-score-flag-phase-gap"]}
```
