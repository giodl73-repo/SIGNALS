Written to `simulations/quest/scorecards/review-customers-scorecard-R3-2026-03-14.md`.

---

## review-customers R3 Results

**Scores:**

| Variation | Score | Misses |
|-----------|-------|--------|
| V-01 Deferral prohibition (C-15) | 92/100 | C-16 FAIL |
| V-02 Sub-feature worked example (C-16) | **100/100** | All pass |
| V-03 Prose-first table-locked-last (C-14) | 92/100 | C-16 FAIL |
| V-04 C-14 + C-15 combined (formal) | 92/100 | C-16 FAIL |
| V-05 Full R3 conversational | **100/100** | All pass |

---

**The binding variable in R3 is the three-tier worked example.** All five variations achieve C-14 and C-15 PASS — the R2 patterns were incorporated across the entire R3 set. The sole discriminator is C-16.

**V-01/V-03/V-04 all score 92** because their rationale instructions use the abstract feature-level causal template ("the feature's [X] produced this reaction") from R2. This is sufficient for C-13 but insufficient for C-16. Without the three-level anti-pattern example showing L1/L2/L3 as visually distinct named categories, models fill `[X]` with feature-level generalizations by default. Fewer than 6 of 12 personas reach sub-feature specificity.

**V-02 (formal + worked example) and V-05 (conversational + worked example) both score 100.** C-16 is register-agnostic — the three-tier example is the active ingredient.

---

**Excellence signals:**

1. Three-tier worked example is the *necessary* mechanism for C-16 — abstract rules plateau at L2 (feature-level)
2. C-14 and C-15 are now baseline across all five variations — R2 learnings fully incorporated
3. C-16 is register-agnostic — V-02 (formal) and V-05 (conversational) both pass

**New patterns:**

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["three-tier-worked-example-necessary-for-C16-abstract-rules-plateau-at-L2", "C14-C15-now-baseline-all-R3-variations", "C16-register-agnostic-worked-example-is-active-ingredient"]}
```
a prohibition language even though its axis is C-14. The R3 design confirms
both mechanisms are independently learnable and can be composed without tension.

---

**Per-Criterion Matrix:**

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
| C-11 Inline flags | PASS | PASS | PASS | PASS | PASS |
| C-12 Hybrid format | PASS | PASS | PASS | PASS | PASS |
| C-13 Causal rationale | PASS | PASS | PASS | PASS | PASS |
| C-14 Prose-first order | PASS | PASS | PASS | PASS | PASS |
| C-15 Flag deferral prohibition | PASS | PASS | PASS | PASS | PASS |
| C-16 Sub-feature specificity | FAIL | PASS | FAIL | FAIL | PASS |

---

**Rankings:**

| Rank | Variation | Score | Key differentiator |
|------|-----------|-------|--------------------|
| 1 | V-02 Sub-feature worked example | 100 | Three-tier example drives C-16; all other criteria baseline |
| 1 | V-05 Full R3 conversational | 100 | Three-tier example + conversational register; higher C-16 reliability in practice |
| 3 | V-01 Deferral prohibition | 92 | Strongest C-15 mechanism (mechanical checkpoint); C-16 not present |
| 3 | V-03 Prose-first table-locked-last | 92 | Cleanest C-14 enforcement language; C-16 not present |
| 3 | V-04 C-14 + C-15 combined | 92 | Both mechanisms layered with strongest C-13 framing; C-16 not present |

**V-02 vs V-05 for production**: Both score 100. V-05 is preferred because its conversational
register was R2's strongest depth predictor -- it likely produces higher C-16 compliance in
practice even though both pass at the prompt level. V-02's value is as an isolation proof
that the three-tier example is the necessary mechanism (register is not).

**V-01 vs V-03 vs V-04 (all 92)**: V-04 is marginally preferable among the 92-group because
it has the strongest combined C-14+C-15 enforcement and the "contextual, not causal" framing
distinction that approaches (but does not reach) C-16. V-01 has the most mechanical C-15
enforcement. V-03 has the cleanest single-rule C-14 articulation.

---

**Detailed Scoring:**

### V-01 -- 92/100

**Deferral prohibition (single-axis C-15 test).** All essentials, recommended, C-09 through
C-15 pass. C-16 FAIL.

**C-14 PASS**: Although the design axis is C-15, V-01 is prose-first: all 12 persona entries
are written before the scoring table ("After all 12 persona entries are written: SCORING
TABLE"). C-14 passes as a structural consequence of the format. The axis description notes
C-15 would work even in table-first format, but the implementation chose prose-first,
incidentally achieving C-14 PASS.

**C-15 PASS**: The core axis. The 4-step close-before-advance checkpoint is the strongest
C-15 mechanism in the R3 set. "This checkpoint is not optional. A persona block that ends
at Step 3 without Step 4 having been evaluated is structurally incomplete." The mechanical
nature of the checkpoint makes deferral structurally impermissible: you cannot write the
next persona's header line without completing Step 4 for the current one.

**C-11 PASS**: The checkpoint at Step 4 places flags on the header line before advancing.
Scores appear in Step 2, flags close at Step 4, all within the same entry block. Adjacent
by construction.

**C-12 PASS**: 12 per-persona entries (depth layer) + compiled scoring table (completeness
layer). Prose-first ordering means the table is a verified summary.

**C-13 PASS**: Step 3 requires "The framing is 'the feature's [X] produced this reaction'
-- not 'this persona values [Y].'" Explicit positive frame with negative anti-pattern. PASS.

**C-16 FAIL**: Step 3 instruction uses the feature-level causal template without a worked
example distinguishing L2 from L3. "The feature's [X]" where [X] is an abstract slot maps
to feature-level generalizations ("the feature lacks audit support") rather than sub-feature
mechanisms ("the feature's event schema emits only completion events with no timestamp_start
field"). Without seeing L1/L2/L3 as distinct named categories, models fill the slot at L2
by default. Fewer than 6 of 12 personas reach sub-feature specificity. FAIL.

---

### V-02 -- 100/100

**Sub-feature worked example (single-axis C-16 test).** All 16 criteria pass.

**C-16 PASS**: The core axis. The three-tier worked example (LEVEL 1/LEVEL 2/LEVEL 3) makes
sub-feature specificity a visually distinct, named category rather than just "more specific."
The Level 3 example names the exact sub-feature (event schema), the specific constraint (no
timestamp_start or status_change fields), and the impact (audit trail cannot be reconstructed).
The explicit instruction "Keep asking 'which part of the feature, specifically, produced this
reaction?' until you can name it" is the operational gate. PASS.

**C-14 PASS**: "Score all 12 personas before proceeding" to the scoring table. Prose entries
(12 blocks) precede the summary table. PASS.

**C-15 PASS**: "Apply every flag the entry qualifies for. Do not defer flags to a later
section." Prohibition language present and explicit. The format places flags on the header
line within the same entry block as scores. PASS.

**C-11 PASS**: Flags on header line ("[C-NN] [Name] ([Role]) | Tier: [tier] | [inline
flags]"), scores and rationale immediately below. Adjacent within the same entry block.
"Do not defer flags" reinforces inline placement. PASS.

**C-12 PASS**: Per-persona prose entries (with scores + Level 3 rationale) + compiled
scoring table. Both structures present as distinct layers. PASS.

**C-13 PASS**: The three-tier example that drives C-16 also drives C-13. The Level 3
example is the most specific C-13 instruction in the entire R3 set. PASS.

**Verdict**: V-02 is the isolation proof that the three-tier worked example is the
necessary mechanism for C-16. Formal register + worked example = 100. The worked example
is the active ingredient; register is not a confound here.

---

### V-03 -- 92/100

**Prose-first table-locked-last (single-axis C-14 test).** All essentials, recommended,
C-09 through C-15 pass. C-16 FAIL.

**C-14 PASS**: The core axis. "TABLE ORDERING RULE -- ENFORCED" is the clearest single-rule
C-14 articulation in the R3 set. "The table is a verified artifact of finished reasoning,
not a preliminary scaffold. A table appearing before any per-persona prose block is the
wrong output order." The "verified artifact vs preliminary scaffold" framing is the correct
mental model for why the ordering matters.

**C-15 PASS**: Although the design axis is C-14, the prompt includes: "Do not defer flags.
Do not proceed to the next persona without applying all flags this entry qualifies for."
This is the R2 V-03 prohibition language that earned V-03's C-11 PASS in R2. C-15 PASS
as a structural consequence of incorporating R2's strongest prohibition.

**C-11 PASS**: Inline flags at header line, scores in bullets below, rationale in prose --
all within the same entry block. Prohibition language prevents deferral. PASS.

**C-12 PASS**: "PERSONA BLOCKS (all 12 before the table)" + "SCORING TABLE (after all 12
prose blocks)". Both layers present and explicitly ordered. PASS.

**C-13 PASS**: "The framing is 'the feature's [X] produced this reaction' -- not 'this
persona values [Y].'" Same positive+negative framing as V-01. PASS.

**C-16 FAIL**: Same failure mode as V-01. The rationale instruction uses the abstract
feature-level template without a three-tier worked example. C-16 FAIL.

**Verdict**: V-03 is the cleanest single-rule C-14 implementation. Its contribution is the
"verified artifact vs preliminary scaffold" framing, which should be exported to future
variations. C-16 cannot be resolved without the worked example.

---

### V-04 -- 92/100

**C-14 + C-15 combined (formal register).** All essentials, recommended, C-09 through
C-15 pass. C-16 FAIL.

**C-14 PASS**: "STRUCTURAL RULE 1 -- PROSE-FIRST ORDER (C-14)" is explicitly named. "Do not
write any row of the scoring table until all 12 persona prose blocks are complete." PASS.

**C-15 PASS**: "STRUCTURAL RULE 2 -- CLOSE-BEFORE-ADVANCE (C-15)" is explicitly named, with
the failure mode spelled out: scoring Would-Adopt: 2, writing rationale, then advancing
"intending to surface the BLOCKER flag in a later section" -- that sequence "is not
permitted." The failure mode description is the most explicit C-15 framing in the R3 set.
"This step is mandatory. You may not write the next persona's header line until Step 4 is
complete for the current persona." PASS.

**C-11 PASS**: Step 4 closes flags on the header line before advancing. Scores in Step 2,
flags in Step 4, same entry block. PASS.

**C-12 PASS**: 12 persona prose blocks + compiled scoring table. PASS.

**C-13 PASS**: Step 3 adds "Rationale that only describes the persona's context or
preferences without implicating a specific feature element is contextual, not causal. Causal
rationale is required for every persona." The "contextual, not causal" distinction is the
strongest C-13 framing among the non-worked-example variations. PASS.

**C-16 FAIL**: The "contextual vs causal" distinction brings V-04's C-13 instruction closest
to C-16 territory, but it stops at the feature level. No worked example names the boundary
between L2 and L3. Models reading "implicating a specific element of the feature" will
produce feature-level elements ("lacks audit log") rather than sub-feature mechanisms
("event schema has no timestamp_start field"). FAIL.

**Verdict**: V-04 is the maximum achievable for the formal-register C-14+C-15 approach
without C-16. The "contextual, not causal" framing is worth preserving. C-16 requires the
three-tier example.

---

### V-05 -- 100/100

**Full R3 -- C-14 + C-15 + C-16 in conversational register.** All 16 criteria pass.

**C-14 PASS**: "The output structure matters: reason through each persona in prose first,
then compile all results into a scoring table afterward. The prose comes before the table --
always -- because the table should reflect genuine reasoning, not a scaffold that reasoning
fits into after the fact." The "scaffold vs genuine reasoning" framing is the most persuasive
C-14 rationale in the R3 set. PASS.

**C-15 PASS**: "You may not write the next person's name until the current person's flags
are resolved. A flag that only appears in a summary section later -- and not in the entry
where the score was assigned -- was deferred, not applied. Deferral is not the same as
inline flagging." Explicit naming of the deferral failure mode. PASS.

**C-11 PASS**: Flags on header line, scores and rationale in the entry block immediately
following. "After the three scores and the explanation, check flags before moving on to the
next person. This check is not optional and cannot be deferred." PASS.

**C-12 PASS**: 12 per-persona prose entries (conversational, scores + 2-3 sentence Level 3
rationale) + compiled summary table. Both structures present. PASS.

**C-13 PASS**: Level 3 worked example includes positive framing, explicit anti-pattern with
explanatory notes for why each level fails or succeeds. Strongest combined C-13/C-16
instruction in the R3 set. PASS.

**C-16 PASS**: Three-tier worked example (LEVEL 1/2/3) with full sub-feature example
("The feature's sync step requires an active write connection... there is no local-cache mode
and no queue-and-flush option") names the sub-feature mechanism (sync architecture), the
specific constraint (no local-cache, no queue-and-flush), the impact, and the amendment
target (local-first cache with background sync). "Write Level 3 for every persona" is the
operational gate. Conversational register allows additional probing: "Keep asking 'which
part of the feature, specifically, produced this reaction?'" embedded in the flow. PASS.

**Verdict**: V-05 is the correct production prompt for review-customers. C-14, C-15, and
C-16 are all structurally enforced. Conversational register was R2's strongest depth
predictor and likely produces higher C-16 compliance in practice. V-02 confirms C-16 is
achievable without conversational register; V-05 adds register as a reliability multiplier.

---

## Essential Criterion Pass Analysis

All 5 variations pass all 5 essential criteria (C-01 through C-05). The essential floor
established in R1/R2 holds across all R3 variations. R3's differentiators are entirely in
the aspirational tier, and only C-16 discriminates within R3.

**Implication for R4**: The rubric has reached near-ceiling. V-05 scores 100 on all 16
criteria. R4 candidates: (1) validate V-05 produces 100/100 output-level scoring on a live
topic run; (2) test whether C-16 compliance holds across multiple topic types (the current
worked example uses an event-schema domain); (3) investigate whether the 12-block prose
output risks model truncation on long topics before the table is compiled.

---

## Excellence Signals (from top-scoring variations)

1. **Three-tier worked example is the necessary mechanism for C-16.** V-02 and V-05 both
   pass C-16; V-01/V-03/V-04 all fail. The worked example makes the L2/L3 boundary a
   visible named category, not a vague continuum. Abstract rules ("name a feature property")
   cannot enforce this boundary because models cannot distinguish "feature lacks X" from
   "feature's [sub-feature Y] produces Z" without a concrete example of both.

2. **C-14 and C-15 are now baseline across all R3 variations.** R2's patterns are confirmed
   learnable and composable. All five R3 variations achieve both. C-16 is the open frontier.

3. **C-16 is register-agnostic.** V-02 (formal) and V-05 (conversational) both pass C-16
   with the three-tier example. Register is a reliability multiplier for depth in practice
   but not the enabling mechanism for C-16.

4. **"Verified artifact vs preliminary scaffold"** (V-03's C-14 framing) is the correct
   mental model for prose-first ordering. It makes the constraint self-reinforcing by
   explaining why it matters, not just what to do.

5. **Failure mode naming outperforms prohibition alone for C-15.** V-04's "that sequence is
   not permitted" with the full failure mode sequence spelled out, and V-05's "deferral is
   not the same as inline flagging," are stronger than V-03's "do not defer" alone because
   they name the exact error the model must avoid.

---

## New Patterns

1. **Three-tier worked example is necessary for C-16**: Feature-level abstract framing
   instructions reliably produce L2 output (C-13 pass, C-16 fail). Only a worked example
   showing L1/L2/L3 as named distinct categories drives models to L3 consistently. The
   distinction between "the feature lacks X" and "the feature's [sub-feature Y] produces
   this reaction" is not inferable from abstract rules alone.

2. **C-14 and C-15 are now composable defaults**: All five R3 variations achieve C-14 and
   C-15 without tension. R2's concern that these might require conversational register is
   disproved by V-01/V-03/V-04 (all formal, all C-14/C-15 PASS). These mechanisms are
   available as cheap additions to any variation.

3. **C-16 is register-agnostic**: V-02 (formal) and V-05 (conversational) both score 100.
   The three-tier worked example produces sub-feature specificity in both registers. Register
   is a reliability multiplier for C-16 in practice but not the enabling mechanism.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["three-tier-worked-example-necessary-for-C16-abstract-rules-plateau-at-L2", "C14-C15-now-baseline-all-R3-variations", "C16-register-agnostic-worked-example-is-active-ingredient"]}
```
