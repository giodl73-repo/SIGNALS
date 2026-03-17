Round 7 variations written. Here's the summary:

---

**R7 gap closed:** V-04/R6 scored ~99.7 on the v6 rubric — not 100.0. C-24 was PARTIAL: the pre-artifact audit had TOKEN RECALL items for Phases 3, 4, 5, 7 (4/5) but the C-16 index declares 5 register-sensitive phases {3, 4, 5, 7, **10**}. The missing item is a Phase 10 AMEND TOKEN RECALL structural check.

**Five variations:**

| V | Label | Axis | Key change |
|---|-------|------|------------|
| V-01 | audit-recall-parity | Lifecycle emphasis | Single new audit item: Phase 10 AMEND TOKEN RECALL structural check (14-item checklist) |
| V-02 | count-assertion-header | Format | V-01 + RECALL COVERAGE COUNT block at audit header; C-24 verifiable in one line |
| V-03 | recall-sequence-labels | Phrasing register | Numbered `(n/5)` TOKEN RECALL labels throughout + Phase 1 sequence index + count-match audit item |
| V-04 | r7-canonical | Combination | All three: numbered labels + count header + AMEND structural check (15-item audit) |
| V-05 | lean-c24-aware | Lean form | V-05/R6 lean + C-21 PARTIAL→PASS (missing audit item added) + C-23 PARTIAL→PASS (independence constraint explicit) |

**Predicted scores (v6 rubric / 16 denominator):** V-01–V-04 all **100.0**. V-05 **~95.9**.

**Architecture note on Phase 10:** AMEND runs after Phase 9 (artifact). The pre-artifact audit at Phase 8 can only verify Phase 10 TOKEN RECALL as a **structural commitment** — it checks that Phase 10 as written opens with TOKEN RECALL before any AMEND TYPE label — not a runtime check. This is the only viable form for a pre-artifact audit checking a post-artifact phase, and satisfies C-24's count requirement.
5.9** (lean form; C-21 PASS from PARTIAL; C-23 PASS from PARTIAL; C-24 N/A; 9.5/16 aspirational)

**Phase 10 AMEND TOKEN RECALL audit item — architectural note:**
The pre-artifact audit (Phase 8) fires before Phase 9 (artifact write) and before Phase 10 (AMEND), which runs only when the user invokes AMEND after the base output. The Phase 10 audit item is therefore a **structural commitment check**: it verifies that Phase 10 as written opens with TOKEN RECALL before any sub-type runs — verified from the prompt text above, not from runtime execution. Runtime compliance is verified at AMEND invocation. This is the only viable architectural form for a pre-artifact audit checking a post-artifact phase, and satisfies C-24's count requirement (5/5 declared phases have corresponding audit items).

---

## V-01: audit-recall-parity (lifecycle emphasis axis)

Axis: Lifecycle emphasis -- V-04/R6 with one addition: Phase 8 audit gains a 14th item
verifying Phase 10 AMEND TOKEN RECALL as a structural commitment. This closes C-24: the
C-16 phase index declares 5 register-sensitive phases {3, 4, 5, 7, 10}; the audit now
carries 5 TOKEN RECALL verification items, one per declared phase.

Hypothesis: V-04/R6 on v6 rubric scores C-24 PARTIAL (4/5 recall items vs 5 declared
phases). Adding the Phase 10 structural check achieves count parity (5/5). C-22 PASS and
C-23 PASS already hold from V-04/R6. No other criteria regress. Predicted 100.0.

```
You are running /discover-compare for topic: {topic}.
Comparing: Option A -- {option_a} vs Option B -- {option_b}.
Audience: {audience}  (exec | engineering | general -- default: general)

=== PHASE 0: STATUS QUO ANCHOR (Option 0) ===

Before any analysis, name the behavior teams fall back on today if neither option is built.

ANCHOR[0A] := {what teams do today instead of building Option A}
ANCHOR[0B] := {what teams do today instead of building Option B}

Binding rule: all inertia analysis, competitive analysis, gate logic, and recommendation
phases must reference ANCHOR[0A] and ANCHOR[0B] by token name -- not by prose paraphrase.
Any reference to "the status quo," "current approach," or "doing nothing" without the
token name violates this binding.

Print: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. Binding committed."

=== PHASE 1: AUDIENCE REGISTER ===

Read the audience parameter. This register governs the following phases and dimensions:

  Phase 3 (dimension analysis):
    - Risk sub-section: failure mode framing language
    - Competitive sub-section: differentiation vector framing language
  Phase 4 (three-column matrix): cell content emphasis and vocabulary
  Phase 5 (two-column summary): cell content emphasis and vocabulary
  Phase 7 (recommendation): lead structure and level of detail
  Phase 10 (AMEND handler): revised recommendation framing

exec: business signal leads all register-sensitive phases and dimensions;
  implementation detail omitted; language is investment/risk/market.
  Phase 3 risk: frame as business impact (revenue, partner dependency, market timing).
  Phase 3 competitive: frame as market differentiation, cost-of-delay, switching cost.
  Phase 4/5 cells: lead with business signal. Omit build-level detail.
  Phase 7: recommendation leads; business risk of not acting second; trade-off third.
  Phase 10: same as Phase 7 structure.

engineering: implementation signal leads all register-sensitive phases and dimensions;
  technical risk detail present; language is build/integrate/operate.
  Phase 3 risk: frame as technical failure mode (race condition, schema drift, dependency brittleness).
  Phase 3 competitive: frame as build cost, latency advantage, dependency graph.
  Phase 4/5 cells: lead with technical signal. Include dependency or correctness risk.
  Phase 7: feasibility delta and technical risk lead; recommendation second; trade-off third.
  Phase 10: same as Phase 7 structure.

general (default): neutral -- no routing applied.

Print: "Register: {exec|engineering|general}. Contract: Phase 3 [risk, competitive],
  Phase 4 [cell emphasis], Phase 5 [cell emphasis], Phase 7 [lead structure], Phase 10 [framing]."

=== PHASE 2: CONTEXT ===

Read existing discover artifacts for this topic:
- Glob: simulations/discover/**/{topic}-*-*.md

Print inventory: | skill | date | path | for each file found.
If prior artifacts exist, note any signals that refine the ANCHOR[0A] or ANCHOR[0B]
characterization committed in Phase 0. Do not change committed tokens -- note refinements only.
If none found: "No prior discover artifacts -- proceeding from inputs."

=== PHASE 3: DIMENSION ANALYSIS ===

TOKEN RECALL: ANCHOR[0A] = {reproduce committed value from Phase 0}.
              ANCHOR[0B] = {reproduce committed value from Phase 0}.

Run each dimension across both options before moving to the next.
ANCHOR[0A] is the reference for all Option A inertia and competitive analysis.
ANCHOR[0B] is the reference for all Option B inertia and competitive analysis.

--- Feasibility ---
Option A: High / Medium / Low. One reason (skill, tooling, timeline).
Option B: High / Medium / Low. One reason.

--- Inertia ---
INERTIA RULE: Inertia is checked for BOTH options independently.
The question for A: would teams keep using ANCHOR[0A] INSTEAD OF building Option A?
  Name the specific mechanism that makes ANCHOR[0A] a viable substitute.
  Threat rating: High / Medium / Low.
The question for B: would teams keep using ANCHOR[0B] INSTEAD OF building Option B?
  Name the specific mechanism that makes ANCHOR[0B] a viable substitute.
  Threat rating: High / Medium / Low.

--- Risk ---
Option A: Primary failure mode. Rating: High / Medium / Low.
Option B: Same.
Register: {applies from Phase 1 -- risk framing dimension}
If register = exec: frame as business impact (revenue impact, partner dependency).
If register = engineering: frame as technical failure mode (race condition, schema drift).
If register = general: standard format.
Option 0 continuation risk: What is the long-term cost of staying with ANCHOR[0A] and ANCHOR[0B]
  rather than building either option? One sentence -- enters the 3-column matrix.

--- Competitive Position ---
ANTI-PATTERN GUARD: Generic competitive analysis uses phrases such as "more competitive,"
"better positioned," or "stronger in the market" without specifying the mechanism.
Such phrasing is insufficient and will fail this criterion. Name the concrete vector:
  Speed: throughput, latency, or iteration rate advantage
  Cost: build, operating, or switching cost difference
  Ecosystem: integration depth, lock-in reduction, or partner leverage
  Capability: what ANCHOR[0A] / ANCHOR[0B] cannot do that this option enables

Option A: At least one concrete vector vs ANCHOR[0A].
Register: {applies from Phase 1 -- competitive framing dimension}
If register = exec: frame in market/investment terms.
If register = engineering: frame in build/operate/latency terms.
Option B: Same requirement and same register instruction, vs ANCHOR[0B].
Option 0 competitive position: What do ANCHOR[0A] and ANCHOR[0B] offer today
  that Option A and Option B do not yet match?

=== TABLE GUIDE ===

Which question are you answering?
  Does either option beat doing nothing (ANCHOR[0A] / ANCHOR[0B])? -> TABLE 1 (Phase 4)
  Which option should we build?                                      -> TABLE 2 (Phase 5)

TABLE 1 (Phase 4) -- Status-Quo Context View: A and B alongside ANCHOR[0A] / ANCHOR[0B].
  Use to assess whether either build option beats the status quo.
  [ -> See Table 2 (Phase 5) for the A-vs-B decision summary. ]

TABLE 2 (Phase 5) -- A-vs-B Decision Summary: A vs B only, Option 0 excluded.
  Use to reach the recommendation.
  [ <- Source: Table 1 (Phase 4), Option 0 column excluded. ]

=== PHASE 4: THREE-COLUMN MATRIX (Table 1 of 2 -- status-quo context view) ===
[ -> See Table 2 (Phase 5) for A-vs-B decision summary ]

TOKEN RECALL: ANCHOR[0A] = {reproduce committed value from Phase 0}.
              ANCHOR[0B] = {reproduce committed value from Phase 0}.

Register: {applies from Phase 1 -- cell emphasis dimension}
If register = exec: lead each non-N/A cell with business impact signal.
  Format: Rating + one-phrase business signal. Omit implementation-level detail.
If register = engineering: lead each non-N/A cell with implementation signal.
  Format: Rating + one-phrase technical signal. Include dependency or correctness risk.
If register = general: balanced. Format: Rating + one-phrase signal.

N/A cells for Option 0 are by design and must be labeled explicitly.
Option 0 column header must use ANCHOR[0A] and ANCHOR[0B] token names from Phase 0.

| Dimension              | Option A: {option_a} | Option B: {option_b} | Option 0: ANCHOR[0A] / ANCHOR[0B] |
|------------------------|----------------------|----------------------|-----------------------------------|
| Feasibility            |                      |                      | N/A (no build required)           |
| Inertia threat         | [vs ANCHOR[0A]]      | [vs ANCHOR[0B]]      | N/A (this IS the anchor)          |
| Risk                   |                      |                      | Continuation risk: ...            |
| Competitive position   |                      |                      | ANCHOR advantage: ...             |

Fill all non-N/A cells using the register-appropriate format.

=== PHASE 5: TWO-COLUMN COMPARISON SUMMARY (Table 2 of 2 -- A-vs-B decision view) ===
[ <- Source: Table 1 (Phase 4); Option 0 column excluded. Use this table to reach the recommendation. ]

TOKEN RECALL: ANCHOR[0A] = {reproduce committed value from Phase 0}.
              ANCHOR[0B] = {reproduce committed value from Phase 0}.

Extract A-vs-B signal from Phase 4 into a scannable 2-column view.
A reader should reach the recommendation from this table without re-reading Phase 3 or 4.

Register: {applies from Phase 1 -- cell emphasis dimension}
If register = exec: business impact signal leads each cell.
If register = engineering: implementation signal leads each cell.
If register = general: balanced content.

| Dimension              | Option A | Option B |
|------------------------|----------|----------|
| Feasibility            |          |          |
| Inertia threat         |          |          |
| Risk                   |          |          |
| Competitive position   |          |          |

Format: Rating + one-phrase signal. No empty cells.

=== PHASE 6: OPTION 0 VERDICT AND GATE ===

TOKEN RECALL: ANCHOR[0A] = {reproduce committed value from Phase 0}.
              ANCHOR[0B] = {reproduce committed value from Phase 0}.

Step 1 -- Issue bilateral verdicts (each independently grounded, one sentence each):

VERDICT A: Teams would [keep using ANCHOR[0A] / build Option A] rather than [build Option A /
  keep using ANCHOR[0A]] because {specific mechanism from Phase 3 inertia analysis}.
  Inertia threat: High / Medium / Low.

VERDICT B: Teams would [keep using ANCHOR[0B] / build Option B] rather than [build Option B /
  keep using ANCHOR[0B]] because {specific mechanism from Phase 3 inertia analysis}.
  Inertia threat: High / Medium / Low.

These verdicts are independent. VERDICT A does not reference Option B. VERDICT B does not
reference Option A. Each verdict stands alone against its own ANCHOR baseline.

Step 2 -- Fire gate based on verdicts:

If VERDICT A = High AND VERDICT B = High:
  "INERTIA GATE: ANCHOR[0A] beats Option A (see VERDICT A). ANCHOR[0B] beats Option B
  (see VERDICT B). Teams will not build either option without a forcing function. 'Build
  neither' is the leading recommendation. If proceeding, name the forcing function explicitly."
  The recommendation in Phase 7 must address this gate.

If exactly one verdict = High:
  "INERTIA NOTE: ANCHOR[{0A|0B}] beats Option {A|B} (see VERDICT {A|B}), but Option {A|B}
  clears the do-nothing bar (see VERDICT {A|B}). Asymmetry may outweigh other dimension signals."

If neither verdict = High:
  "Inertia check passed -- both Options A and B beat their ANCHOR baselines
  (VERDICT A: {A-rating}, VERDICT B: {B-rating})."

=== PHASE 7: RECOMMENDATION ===

TOKEN RECALL: ANCHOR[0A] = {reproduce committed value from Phase 0}.
              ANCHOR[0B] = {reproduce committed value from Phase 0}.

State: choose Option A / choose Option B / build neither / defer.

Register: {applies from Phase 1 -- lead structure dimension}
If register = exec:
  Lead with: recommendation and business risk of not taking it. One sentence each.
  Then: trade-off (what is given up by not choosing the other option).
  Omit implementation detail.
If register = engineering:
  Lead with: feasibility delta and primary technical risk.
  Then: recommendation.
  Then: trade-off (what is given up technically).
If register = general:
  Recommendation, primary reason, trade-off in one paragraph.

All registers:
- If GATE A fired (both verdicts High): either "build neither" OR name the forcing function
  that overrides the inertia evidence. Reference ANCHOR[0A] and ANCHOR[0B] in the gate language.
- Recommendation traceable to Table 2 (Phase 5) -- do not assert a winner that
  contradicts the matrix signals without explicit justification. If the recommendation
  diverges from the matrix plurality, state the reason explicitly.

=== PHASE 8: STRUCTURAL AUDIT (pre-artifact gate) ===

Before writing the artifact in Phase 9, self-verify each item below.
If any item fails, correct the affected section NOW -- before proceeding to Phase 9.
The artifact must reflect the corrected state, not the raw output.

AUDIT CHECKLIST:
[ ] Phase 0: ANCHOR[0A] and ANCHOR[0B] committed before Phase 1?
    Evidence: "Binding committed." line printed.
[ ] Phase 1: register contract printed with dimension-level phase index?
    Expected pattern: "Phase 3 [risk, competitive], Phase 4 [cell emphasis],
    Phase 5 [cell emphasis], Phase 7 [lead structure], Phase 10 [framing]."
[ ] Phase 3 TOKEN RECALL: token values reproduced at top of Phase 3?
[ ] Phase 3 inertia: both A and B independently checked vs ANCHOR[0A] and ANCHOR[0B]?
    Failure pattern: checking which build option teams prefer instead of vs anchor.
[ ] Phase 4 TOKEN RECALL: token values reproduced at top of Phase 4?
[ ] TABLE GUIDE present before Phase 4? Question-keyed routing to TABLE 1 and TABLE 2?
[ ] Phase 4 header carries "[ -> See Table 2 (Phase 5)... ]"?
[ ] Phase 5 TOKEN RECALL: token values reproduced at top of Phase 5?
[ ] Phase 5 header carries "[ <- Source: Table 1 (Phase 4)... ]"?
[ ] Phase 6 VERDICT A and VERDICT B both present and independently grounded?
    Failure pattern: either verdict references the other option or their anchor.
    Independence constraint: VERDICT A does not name Option B; VERDICT B does not name Option A.
[ ] Phase 6 TOKEN RECALL reproduced correctly? Gate language uses ANCHOR token names?
[ ] Phase 7 TOKEN RECALL reproduced correctly? Recommendation traceable to Table 2?
    If recommendation diverges from matrix plurality: reason stated explicitly?
[ ] If GATE A fired in Phase 6: "build neither" named OR forcing function named in Phase 7?
[ ] Phase 10 AMEND TOKEN RECALL: Phase 10 AMEND handler opens with TOKEN RECALL before
    any sub-type runs. [Structural commitment -- verify from Phase 10 text above: opening
    TOKEN RECALL block present before first AMEND TYPE label. Runtime verified at invocation.]

Print: "PRE-ARTIFACT AUDIT -- {N}/14 checks passed. Proceeding to artifact write."
If any check failed: print which item failed and the correction applied, THEN proceed to Phase 9.

=== PHASE 9: ARTIFACT ===

Write to simulations/discover/compare/{topic}-compare-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  option_a: {option_a}
  option_b: {option_b}
  anchor_0a: {ANCHOR[0A] committed in Phase 0}
  anchor_0b: {ANCHOR[0B] committed in Phase 0}
  audience: {exec|engineering|general}
  feasibility_a: High|Medium|Low
  feasibility_b: High|Medium|Low
  inertia_a: High|Medium|Low
  inertia_b: High|Medium|Low
  risk_a: High|Medium|Low
  risk_b: High|Medium|Low
  inertia_gate: passed|note|warning
  recommendation: A|B|neither|defer
  neither_path_surfaced: true|false
  option_0_matrix: true
  verdict_a: build|inertia
  verdict_b: build|inertia
  amended: false

=== PHASE 10: AMEND HANDLER ===

Activates when the user says AMEND after the base output.

TOKEN RECALL: ANCHOR[0A] = {reproduce committed value from Phase 0}.
              ANCHOR[0B] = {reproduce committed value from Phase 0}.

Three types -- execute the matching protocol:

AMEND TYPE 1 -- Add Option C: {option_c}

1. Define ANCHOR[0C] := {what teams do today instead of building C}.
   Print: "ANCHOR[0C] = {value}. Binding extended."
   TOKEN RECALL at each Option C analysis sub-section:
   "ANCHOR[0C] = {reproduce committed value}."
2. Run Option C through all four dimensions vs ANCHOR[0C]:
   - Feasibility: High / Medium / Low + one reason.
     Register: apply Phase 1 contract [cell emphasis dimension].
   - Inertia (INERTIA RULE): Would teams keep using ANCHOR[0C] instead of building C?
     Name the specific mechanism. Rate: High / Medium / Low.
   - Risk: Primary failure mode. High / Medium / Low.
     Register: apply Phase 1 contract [risk framing dimension].
   - Competitive position: At least one concrete vector vs ANCHOR[0C]. Anti-pattern guard applies.
     Register: apply Phase 1 contract [competitive framing dimension].
   - Issue VERDICT C: same bilateral verdict structure as Phase 6.
3. Expand Table 1 (Phase 4) to four columns: add Option C column.
   Update header: "Table 1 of 2 -- Status-Quo Context View (A / B / C / Option 0)"
   Update cross-reference: "[ -> See Table 2 (Phase 5) for A-vs-B-vs-C decision summary ]"
   Option 0 column header: "Option 0: ANCHOR[0A] / ANCHOR[0B] / ANCHOR[0C]"
   Register: apply Phase 1 contract to new Option C cells.
4. Update Table 2 (Phase 5) to three columns A/B/C.
   Update header: "Table 2 of 2 -- A-vs-B-vs-C Decision Summary"
   Update cross-reference: "[ <- Source: Table 1 (Phase 4); Option 0 column excluded. ]"
   Register: apply Phase 1 contract to new Option C cells.
   Verify: Option C ratings in Table 1 and Table 2 match.
5. Re-run Phase 6 verdict-and-gate for all three options.
   TOKEN RECALL: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. ANCHOR[0C] = {value}."
6. Revise recommendation: A / B / C / build neither / defer.
   TOKEN RECALL: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. ANCHOR[0C] = {value}."
   If changed, name what changed and why. Anti-contradiction applies to updated Table 2.
   Register: apply Phase 1 contract [lead structure dimension] to revised recommendation.
7. Update artifact: add anchor_0c, option_c, verdict_c, update recommendation, amended: true.

AMEND TYPE 2 -- Weight dimension: {dimension} x{weight}

1. Apply weight multiplier to named dimension across Table 2 (Phase 5).
   Valid: feasibility, inertia, risk, competitive. Weight: x2 or x0.5.
2. Mark weighted dimension: "Feasibility [x2]".
3. Determine aggregate winner under new weighting.
4. Revise recommendation if weighting changes plurality.
   Name the delta explicitly.
   Register: apply Phase 1 contract [lead structure dimension] to revised recommendation.
5. Update artifact: weight_{dimension}: {weight}, amended: true.

AMEND TYPE 3 -- Shift audience: {exec|engineering}

1. Re-render Table 1 (Phase 4), Table 2 (Phase 5), and Phase 7 (recommendation)
   for the specified register per Phase 1 contract.
   exec: business impact cell framing; recommendation leads; omit implementation detail.
   engineering: implementation signal cell framing; feasibility leads; full technical framing.
2. Underlying evidence unchanged. ANCHOR[0A] and ANCHOR[0B] token references maintained.
   Presentation layer only.
3. Note: "Audience amendment: {exec|engineering} -- re-rendered for register."
4. Do not update the artifact file.
```

---

## V-02: count-assertion-header (format axis)

Axis: Format -- V-01 base (Phase 10 AMEND TOKEN RECALL item added) + a RECALL COVERAGE
COUNT block at the opening of the Phase 8 audit. The count block explicitly names each
required recall item by number, making C-24 verifiable at-a-glance from the audit header
without manually counting checklist items.

Hypothesis: V-01 closes C-24 by adding the 14th item. V-02 makes the closure observable:
a reader (or evaluator) can see "Required: 5. Present: items 3, 5, 8, 12, 14 (5/5)" at
the top of the audit without re-reading every phase. The count assertion pairs the C-16
forward index (which declares which phases require recall) with the audit (which verifies
them) into a closed contract. No criteria regress vs V-01. Predicted 100.0.

```
You are running /discover-compare for topic: {topic}.
Comparing: Option A -- {option_a} vs Option B -- {option_b}.
Audience: {audience}  (exec | engineering | general -- default: general)

=== PHASE 0: STATUS QUO ANCHOR (Option 0) ===

Before any analysis, name the behavior teams fall back on today if neither option is built.

ANCHOR[0A] := {what teams do today instead of building Option A}
ANCHOR[0B] := {what teams do today instead of building Option B}

Binding rule: all inertia analysis, competitive analysis, gate logic, and recommendation
phases must reference ANCHOR[0A] and ANCHOR[0B] by token name -- not by prose paraphrase.
Any reference to "the status quo," "current approach," or "doing nothing" without the
token name violates this binding.

Print: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. Binding committed."

=== PHASE 1: AUDIENCE REGISTER ===

Read the audience parameter. This register governs the following phases and dimensions:

  Phase 3 (dimension analysis):
    - Risk sub-section: failure mode framing language
    - Competitive sub-section: differentiation vector framing language
  Phase 4 (three-column matrix): cell content emphasis and vocabulary
  Phase 5 (two-column summary): cell content emphasis and vocabulary
  Phase 7 (recommendation): lead structure and level of detail
  Phase 10 (AMEND handler): revised recommendation framing

exec: business signal leads all register-sensitive phases and dimensions;
  implementation detail omitted; language is investment/risk/market.
  Phase 3 risk: frame as business impact (revenue, partner dependency, market timing).
  Phase 3 competitive: frame as market differentiation, cost-of-delay, switching cost.
  Phase 4/5 cells: lead with business signal. Omit build-level detail.
  Phase 7: recommendation leads; business risk of not acting second; trade-off third.
  Phase 10: same as Phase 7 structure.

engineering: implementation signal leads all register-sensitive phases and dimensions;
  technical risk detail present; language is build/integrate/operate.
  Phase 3 risk: frame as technical failure mode (race condition, schema drift, dependency brittleness).
  Phase 3 competitive: frame as build cost, latency advantage, dependency graph.
  Phase 4/5 cells: lead with technical signal. Include dependency or correctness risk.
  Phase 7: feasibility delta and technical risk lead; recommendation second; trade-off third.
  Phase 10: same as Phase 7 structure.

general (default): neutral -- no routing applied.

Print: "Register: {exec|engineering|general}. Contract: Phase 3 [risk, competitive],
  Phase 4 [cell emphasis], Phase 5 [cell emphasis], Phase 7 [lead structure], Phase 10 [framing]."

=== PHASE 2: CONTEXT ===

Read existing discover artifacts for this topic:
- Glob: simulations/discover/**/{topic}-*-*.md

Print inventory: | skill | date | path | for each file found.
If prior artifacts exist, note any signals that refine the ANCHOR[0A] or ANCHOR[0B]
characterization committed in Phase 0. Do not change committed tokens -- note refinements only.
If none found: "No prior discover artifacts -- proceeding from inputs."

=== PHASE 3: DIMENSION ANALYSIS ===

TOKEN RECALL: ANCHOR[0A] = {reproduce committed value from Phase 0}.
              ANCHOR[0B] = {reproduce committed value from Phase 0}.

Run each dimension across both options before moving to the next.
ANCHOR[0A] is the reference for all Option A inertia and competitive analysis.
ANCHOR[0B] is the reference for all Option B inertia and competitive analysis.

--- Feasibility ---
Option A: High / Medium / Low. One reason (skill, tooling, timeline).
Option B: High / Medium / Low. One reason.

--- Inertia ---
INERTIA RULE: Inertia is checked for BOTH options independently.
The question for A: would teams keep using ANCHOR[0A] INSTEAD OF building Option A?
  Name the specific mechanism that makes ANCHOR[0A] a viable substitute.
  Threat rating: High / Medium / Low.
The question for B: would teams keep using ANCHOR[0B] INSTEAD OF building Option B?
  Name the specific mechanism that makes ANCHOR[0B] a viable substitute.
  Threat rating: High / Medium / Low.

--- Risk ---
Option A: Primary failure mode. Rating: High / Medium / Low.
Option B: Same.
Register: {applies from Phase 1 -- risk framing dimension}
If register = exec: frame as business impact (revenue impact, partner dependency).
If register = engineering: frame as technical failure mode (race condition, schema drift).
If register = general: standard format.
Option 0 continuation risk: What is the long-term cost of staying with ANCHOR[0A] and ANCHOR[0B]
  rather than building either option? One sentence -- enters the 3-column matrix.

--- Competitive Position ---
ANTI-PATTERN GUARD: Generic competitive analysis uses phrases such as "more competitive,"
"better positioned," or "stronger in the market" without specifying the mechanism.
Such phrasing is insufficient and will fail this criterion. Name the concrete vector:
  Speed: throughput, latency, or iteration rate advantage
  Cost: build, operating, or switching cost difference
  Ecosystem: integration depth, lock-in reduction, or partner leverage
  Capability: what ANCHOR[0A] / ANCHOR[0B] cannot do that this option enables

Option A: At least one concrete vector vs ANCHOR[0A].
Register: {applies from Phase 1 -- competitive framing dimension}
If register = exec: frame in market/investment terms.
If register = engineering: frame in build/operate/latency terms.
Option B: Same requirement and same register instruction, vs ANCHOR[0B].
Option 0 competitive position: What do ANCHOR[0A] and ANCHOR[0B] offer today
  that Option A and Option B do not yet match?

=== TABLE GUIDE ===

Which question are you answering?
  Does either option beat doing nothing (ANCHOR[0A] / ANCHOR[0B])? -> TABLE 1 (Phase 4)
  Which option should we build?                                      -> TABLE 2 (Phase 5)

TABLE 1 (Phase 4) -- Status-Quo Context View: A and B alongside ANCHOR[0A] / ANCHOR[0B].
  Use to assess whether either build option beats the status quo.
  [ -> See Table 2 (Phase 5) for the A-vs-B decision summary. ]

TABLE 2 (Phase 5) -- A-vs-B Decision Summary: A vs B only, Option 0 excluded.
  Use to reach the recommendation.
  [ <- Source: Table 1 (Phase 4), Option 0 column excluded. ]

=== PHASE 4: THREE-COLUMN MATRIX (Table 1 of 2 -- status-quo context view) ===
[ -> See Table 2 (Phase 5) for A-vs-B decision summary ]

TOKEN RECALL: ANCHOR[0A] = {reproduce committed value from Phase 0}.
              ANCHOR[0B] = {reproduce committed value from Phase 0}.

Register: {applies from Phase 1 -- cell emphasis dimension}
If register = exec: lead each non-N/A cell with business impact signal.
  Format: Rating + one-phrase business signal. Omit implementation-level detail.
If register = engineering: lead each non-N/A cell with implementation signal.
  Format: Rating + one-phrase technical signal. Include dependency or correctness risk.
If register = general: balanced. Format: Rating + one-phrase signal.

N/A cells for Option 0 are by design and must be labeled explicitly.
Option 0 column header must use ANCHOR[0A] and ANCHOR[0B] token names from Phase 0.

| Dimension              | Option A: {option_a} | Option B: {option_b} | Option 0: ANCHOR[0A] / ANCHOR[0B] |
|------------------------|----------------------|----------------------|-----------------------------------|
| Feasibility            |                      |                      | N/A (no build required)           |
| Inertia threat         | [vs ANCHOR[0A]]      | [vs ANCHOR[0B]]      | N/A (this IS the anchor)          |
| Risk                   |                      |                      | Continuation risk: ...            |
| Competitive position   |                      |                      | ANCHOR advantage: ...             |

Fill all non-N/A cells using the register-appropriate format.

=== PHASE 5: TWO-COLUMN COMPARISON SUMMARY (Table 2 of 2 -- A-vs-B decision view) ===
[ <- Source: Table 1 (Phase 4); Option 0 column excluded. Use this table to reach the recommendation. ]

TOKEN RECALL: ANCHOR[0A] = {reproduce committed value from Phase 0}.
              ANCHOR[0B] = {reproduce committed value from Phase 0}.

Extract A-vs-B signal from Phase 4 into a scannable 2-column view.
A reader should reach the recommendation from this table without re-reading Phase 3 or 4.

Register: {applies from Phase 1 -- cell emphasis dimension}
If register = exec: business impact signal leads each cell.
If register = engineering: implementation signal leads each cell.
If register = general: balanced content.

| Dimension              | Option A | Option B |
|------------------------|----------|----------|
| Feasibility            |          |          |
| Inertia threat         |          |          |
| Risk                   |          |          |
| Competitive position   |          |          |

Format: Rating + one-phrase signal. No empty cells.

=== PHASE 6: OPTION 0 VERDICT AND GATE ===

TOKEN RECALL: ANCHOR[0A] = {reproduce committed value from Phase 0}.
              ANCHOR[0B] = {reproduce committed value from Phase 0}.

Step 1 -- Issue bilateral verdicts (each independently grounded, one sentence each):

VERDICT A: Teams would [keep using ANCHOR[0A] / build Option A] rather than [build Option A /
  keep using ANCHOR[0A]] because {specific mechanism from Phase 3 inertia analysis}.
  Inertia threat: High / Medium / Low.

VERDICT B: Teams would [keep using ANCHOR[0B] / build Option B] rather than [build Option B /
  keep using ANCHOR[0B]] because {specific mechanism from Phase 3 inertia analysis}.
  Inertia threat: High / Medium / Low.

These verdicts are independent. VERDICT A does not reference Option B. VERDICT B does not
reference Option A. Each verdict stands alone against its own ANCHOR baseline.

Step 2 -- Fire gate based on verdicts:

If VERDICT A = High AND VERDICT B = High:
  "INERTIA GATE: ANCHOR[0A] beats Option A (see VERDICT A). ANCHOR[0B] beats Option B
  (see VERDICT B). Teams will not build either option without a forcing function. 'Build
  neither' is the leading recommendation. If proceeding, name the forcing function explicitly."
  The recommendation in Phase 7 must address this gate.

If exactly one verdict = High:
  "INERTIA NOTE: ANCHOR[{0A|0B}] beats Option {A|B} (see VERDICT {A|B}), but Option {A|B}
  clears the do-nothing bar (see VERDICT {A|B}). Asymmetry may outweigh other dimension signals."

If neither verdict = High:
  "Inertia check passed -- both Options A and B beat their ANCHOR baselines
  (VERDICT A: {A-rating}, VERDICT B: {B-rating})."

=== PHASE 7: RECOMMENDATION ===

TOKEN RECALL: ANCHOR[0A] = {reproduce committed value from Phase 0}.
              ANCHOR[0B] = {reproduce committed value from Phase 0}.

State: choose Option A / choose Option B / build neither / defer.

Register: {applies from Phase 1 -- lead structure dimension}
If register = exec:
  Lead with: recommendation and business risk of not taking it. One sentence each.
  Then: trade-off (what is given up by not choosing the other option).
  Omit implementation detail.
If register = engineering:
  Lead with: feasibility delta and primary technical risk.
  Then: recommendation.
  Then: trade-off (what is given up technically).
If register = general:
  Recommendation, primary reason, trade-off in one paragraph.

All registers:
- If GATE A fired (both verdicts High): either "build neither" OR name the forcing function
  that overrides the inertia evidence. Reference ANCHOR[0A] and ANCHOR[0B] in the gate language.
- Recommendation traceable to Table 2 (Phase 5) -- do not assert a winner that
  contradicts the matrix signals without explicit justification. If the recommendation
  diverges from the matrix plurality, state the reason explicitly.

=== PHASE 8: STRUCTURAL AUDIT (pre-artifact gate) ===

Before writing the artifact in Phase 9, self-verify each item below.
If any item fails, correct the affected section NOW -- before proceeding to Phase 9.
The artifact must reflect the corrected state, not the raw output.

RECALL COVERAGE COUNT: C-16 declared 5 register-sensitive phases {3, 4, 5, 7, 10}.
Required TOKEN RECALL audit items: 5.
These items appear as: item 3 (Phase 3), item 5 (Phase 4), item 8 (Phase 5),
  item 12 (Phase 7), item 14 (Phase 10 AMEND).
Verify count: {count items matching the above} == 5 before proceeding.

AUDIT CHECKLIST:
[ ] Phase 0: ANCHOR[0A] and ANCHOR[0B] committed before Phase 1?
    Evidence: "Binding committed." line printed.
[ ] Phase 1: register contract printed with dimension-level phase index?
    Expected pattern: "Phase 3 [risk, competitive], Phase 4 [cell emphasis],
    Phase 5 [cell emphasis], Phase 7 [lead structure], Phase 10 [framing]."
[ ] Phase 3 TOKEN RECALL: token values reproduced at top of Phase 3?
[ ] Phase 3 inertia: both A and B independently checked vs ANCHOR[0A] and ANCHOR[0B]?
    Failure pattern: checking which build option teams prefer instead of vs anchor.
[ ] Phase 4 TOKEN RECALL: token values reproduced at top of Phase 4?
[ ] TABLE GUIDE present before Phase 4? Question-keyed routing to TABLE 1 and TABLE 2?
[ ] Phase 4 header carries "[ -> See Table 2 (Phase 5)... ]"?
[ ] Phase 5 TOKEN RECALL: token values reproduced at top of Phase 5?
[ ] Phase 5 header carries "[ <- Source: Table 1 (Phase 4)... ]"?
[ ] Phase 6 VERDICT A and VERDICT B both present and independently grounded?
    Failure pattern: either verdict references the other option or their anchor.
    Independence constraint: VERDICT A does not name Option B; VERDICT B does not name Option A.
[ ] Phase 6 TOKEN RECALL reproduced correctly? Gate language uses ANCHOR token names?
[ ] Phase 7 TOKEN RECALL reproduced correctly? Recommendation traceable to Table 2?
    If recommendation diverges from matrix plurality: reason stated explicitly?
[ ] If GATE A fired in Phase 6: "build neither" named OR forcing function named in Phase 7?
[ ] Phase 10 AMEND TOKEN RECALL: Phase 10 AMEND handler opens with TOKEN RECALL before
    any sub-type runs. [Structural commitment -- verify from Phase 10 text above: opening
    TOKEN RECALL block present before first AMEND TYPE label. Runtime verified at invocation.]

Print: "PRE-ARTIFACT AUDIT -- {N}/14 checks passed. RECALL COVERAGE: {count}/5. Proceeding to artifact write."
If any check failed: print which item failed and the correction applied, THEN proceed to Phase 9.

=== PHASE 9: ARTIFACT ===

Write to simulations/discover/compare/{topic}-compare-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  option_a: {option_a}
  option_b: {option_b}
  anchor_0a: {ANCHOR[0A] committed in Phase 0}
  anchor_0b: {ANCHOR[0B] committed in Phase 0}
  audience: {exec|engineering|general}
  feasibility_a: High|Medium|Low
  feasibility_b: High|Medium|Low
  inertia_a: High|Medium|Low
  inertia_b: High|Medium|Low
  risk_a: High|Medium|Low
  risk_b: High|Medium|Low
  inertia_gate: passed|note|warning
  recommendation: A|B|neither|defer
  neither_path_surfaced: true|false
  option_0_matrix: true
  verdict_a: build|inertia
  verdict_b: build|inertia
  amended: false

=== PHASE 10: AMEND HANDLER ===

Activates when the user says AMEND after the base output.

TOKEN RECALL: ANCHOR[0A] = {reproduce committed value from Phase 0}.
              ANCHOR[0B] = {reproduce committed value from Phase 0}.

Three types -- execute the matching protocol:

AMEND TYPE 1 -- Add Option C: {option_c}

1. Define ANCHOR[0C] := {what teams do today instead of building C}.
   Print: "ANCHOR[0C] = {value}. Binding extended."
   TOKEN RECALL at each Option C analysis sub-section:
   "ANCHOR[0C] = {reproduce committed value}."
2. Run Option C through all four dimensions vs ANCHOR[0C]:
   - Feasibility: High / Medium / Low + one reason.
     Register: apply Phase 1 contract [cell emphasis dimension].
   - Inertia (INERTIA RULE): Would teams keep using ANCHOR[0C] instead of building C?
     Name the specific mechanism. Rate: High / Medium / Low.
   - Risk: Primary failure mode. High / Medium / Low.
     Register: apply Phase 1 contract [risk framing dimension].
   - Competitive position: At least one concrete vector vs ANCHOR[0C]. Anti-pattern guard applies.
     Register: apply Phase 1 contract [competitive framing dimension].
   - Issue VERDICT C: same bilateral verdict structure as Phase 6.
3. Expand Table 1 (Phase 4) to four columns: add Option C column.
   Update header: "Table 1 of 2 -- Status-Quo Context View (A / B / C / Option 0)"
   Update cross-reference: "[ -> See Table 2 (Phase 5) for A-vs-B-vs-C decision summary ]"
   Option 0 column header: "Option 0: ANCHOR[0A] / ANCHOR[0B] / ANCHOR[0C]"
   Register: apply Phase 1 contract to new Option C cells.
4. Update Table 2 (Phase 5) to three columns A/B/C.
   Update header: "Table 2 of 2 -- A-vs-B-vs-C Decision Summary"
   Update cross-reference: "[ <- Source: Table 1 (Phase 4); Option 0 column excluded. ]"
   Register: apply Phase 1 contract to new Option C cells.
   Verify: Option C ratings in Table 1 and Table 2 match.
5. Re-run Phase 6 verdict-and-gate for all three options.
   TOKEN RECALL: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. ANCHOR[0C] = {value}."
6. Revise recommendation: A / B / C / build neither / defer.
   TOKEN RECALL: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. ANCHOR[0C] = {value}."
   If changed, name what changed and why. Anti-contradiction applies to updated Table 2.
   Register: apply Phase 1 contract [lead structure dimension] to revised recommendation.
7. Update artifact: add anchor_0c, option_c, verdict_c, update recommendation, amended: true.

AMEND TYPE 2 -- Weight dimension: {dimension} x{weight}

1. Apply weight multiplier to named dimension across Table 2 (Phase 5).
   Valid: feasibility, inertia, risk, competitive. Weight: x2 or x0.5.
2. Mark weighted dimension: "Feasibility [x2]".
3. Determine aggregate winner under new weighting.
4. Revise recommendation if weighting changes plurality.
   Name the delta explicitly.
   Register: apply Phase 1 contract [lead structure dimension] to revised recommendation.
5. Update artifact: weight_{dimension}: {weight}, amended: true.

AMEND TYPE 3 -- Shift audience: {exec|engineering}

1. Re-render Table 1 (Phase 4), Table 2 (Phase 5), and Phase 7 (recommendation)
   for the specified register per Phase 1 contract.
   exec: business impact cell framing; recommendation leads; omit implementation detail.
   engineering: implementation signal cell framing; feasibility leads; full technical framing.
2. Underlying evidence unchanged. ANCHOR[0A] and ANCHOR[0B] token references maintained.
   Presentation layer only.
3. Note: "Audience amendment: {exec|engineering} -- re-rendered for register."
4. Do not update the artifact file.
```

---

## V-03: recall-sequence-labels (phrasing register axis)

Axis: Phrasing register (formal/technical) -- V-04/R6 base with TOKEN RECALL blocks
numbered as "(n/5 register-sensitive)" at each of the 5 register-sensitive phases. The
C-16 declaration adds an explicit count ("5 register-sensitive phases total"). The Phase 8
audit gains a count-match item and the Phase 10 AMEND TOKEN RECALL structural check.
The numbered sequence makes the recall chain traceable: an evaluator can verify 5 labeled
blocks exist and which phases they cover without counting unlabeled occurrences.

Hypothesis: Numbered recall labels don't change what TOKEN RECALL does -- they make the
coverage footprint visible in the output. An evaluator checking C-20 can scan for labels
"(1/5)" through "(5/5)" instead of hunting for TOKEN RECALL blocks by phase number. The
count-match audit item closes C-24 from the same structural commitment angle as V-01 but
also verifies label completeness explicitly. Predicted 100.0.

```
You are running /discover-compare for topic: {topic}.
Comparing: Option A -- {option_a} vs Option B -- {option_b}.
Audience: {audience}  (exec | engineering | general -- default: general)

=== PHASE 0: STATUS QUO ANCHOR (Option 0) ===

Before any analysis, name the behavior teams fall back on today if neither option is built.

ANCHOR[0A] := {what teams do today instead of building Option A}
ANCHOR[0B] := {what teams do today instead of building Option B}

Binding rule: all inertia analysis, competitive analysis, gate logic, and recommendation
phases must reference ANCHOR[0A] and ANCHOR[0B] by token name -- not by prose paraphrase.
Any reference to "the status quo," "current approach," or "doing nothing" without the
token name violates this binding.

Print: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. Binding committed."

=== PHASE 1: AUDIENCE REGISTER ===

Read the audience parameter. This register governs the following phases and dimensions:

  Phase 3 (dimension analysis):
    - Risk sub-section: failure mode framing language
    - Competitive sub-section: differentiation vector framing language
  Phase 4 (three-column matrix): cell content emphasis and vocabulary
  Phase 5 (two-column summary): cell content emphasis and vocabulary
  Phase 7 (recommendation): lead structure and level of detail
  Phase 10 (AMEND handler): revised recommendation framing

5 register-sensitive phases total: {3, 4, 5, 7, 10}.
Each will carry a numbered TOKEN RECALL block: (1/5) through (5/5).

exec: business signal leads all register-sensitive phases and dimensions;
  implementation detail omitted; language is investment/risk/market.
  Phase 3 risk: frame as business impact (revenue, partner dependency, market timing).
  Phase 3 competitive: frame as market differentiation, cost-of-delay, switching cost.
  Phase 4/5 cells: lead with business signal. Omit build-level detail.
  Phase 7: recommendation leads; business risk of not acting second; trade-off third.
  Phase 10: same as Phase 7 structure.

engineering: implementation signal leads all register-sensitive phases and dimensions;
  technical risk detail present; language is build/integrate/operate.
  Phase 3 risk: frame as technical failure mode (race condition, schema drift, dependency brittleness).
  Phase 3 competitive: frame as build cost, latency advantage, dependency graph.
  Phase 4/5 cells: lead with technical signal. Include dependency or correctness risk.
  Phase 7: feasibility delta and technical risk lead; recommendation second; trade-off third.
  Phase 10: same as Phase 7 structure.

general (default): neutral -- no routing applied.

Print: "Register: {exec|engineering|general}. Contract: Phase 3 [risk, competitive],
  Phase 4 [cell emphasis], Phase 5 [cell emphasis], Phase 7 [lead structure], Phase 10 [framing].
  TOKEN RECALL sequence: (1/5) at Phase 3, (2/5) at Phase 4, (3/5) at Phase 5,
  (4/5) at Phase 7, (5/5) at Phase 10."

=== PHASE 2: CONTEXT ===

Read existing discover artifacts for this topic:
- Glob: simulations/discover/**/{topic}-*-*.md

Print inventory: | skill | date | path | for each file found.
If prior artifacts exist, note any signals that refine the ANCHOR[0A] or ANCHOR[0B]
characterization committed in Phase 0. Do not change committed tokens -- note refinements only.
If none found: "No prior discover artifacts -- proceeding from inputs."

=== PHASE 3: DIMENSION ANALYSIS ===

TOKEN RECALL (1/5 register-sensitive): ANCHOR[0A] = {reproduce committed value from Phase 0}.
                                       ANCHOR[0B] = {reproduce committed value from Phase 0}.

Run each dimension across both options before moving to the next.
ANCHOR[0A] is the reference for all Option A inertia and competitive analysis.
ANCHOR[0B] is the reference for all Option B inertia and competitive analysis.

--- Feasibility ---
Option A: High / Medium / Low. One reason (skill, tooling, timeline).
Option B: High / Medium / Low. One reason.

--- Inertia ---
INERTIA RULE: Inertia is checked for BOTH options independently.
The question for A: would teams keep using ANCHOR[0A] INSTEAD OF building Option A?
  Name the specific mechanism that makes ANCHOR[0A] a viable substitute.
  Threat rating: High / Medium / Low.
The question for B: would teams keep using ANCHOR[0B] INSTEAD OF building Option B?
  Name the specific mechanism that makes ANCHOR[0B] a viable substitute.
  Threat rating: High / Medium / Low.

--- Risk ---
Option A: Primary failure mode. Rating: High / Medium / Low.
Option B: Same.
Register: {applies from Phase 1 -- risk framing dimension}
If register = exec: frame as business impact (revenue impact, partner dependency).
If register = engineering: frame as technical failure mode (race condition, schema drift).
If register = general: standard format.
Option 0 continuation risk: What is the long-term cost of staying with ANCHOR[0A] and ANCHOR[0B]
  rather than building either option? One sentence -- enters the 3-column matrix.

--- Competitive Position ---
ANTI-PATTERN GUARD: Generic competitive analysis uses phrases such as "more competitive,"
"better positioned," or "stronger in the market" without specifying the mechanism.
Such phrasing is insufficient and will fail this criterion. Name the concrete vector:
  Speed: throughput, latency, or iteration rate advantage
  Cost: build, operating, or switching cost difference
  Ecosystem: integration depth, lock-in reduction, or partner leverage
  Capability: what ANCHOR[0A] / ANCHOR[0B] cannot do that this option enables

Option A: At least one concrete vector vs ANCHOR[0A].
Register: {applies from Phase 1 -- competitive framing dimension}
If register = exec: frame in market/investment terms.
If register = engineering: frame in build/operate/latency terms.
Option B: Same requirement and same register instruction, vs ANCHOR[0B].
Option 0 competitive position: What do ANCHOR[0A] and ANCHOR[0B] offer today
  that Option A and Option B do not yet match?

=== TABLE GUIDE ===

Which question are you answering?
  Does either option beat doing nothing (ANCHOR[0A] / ANCHOR[0B])? -> TABLE 1 (Phase 4)
  Which option should we build?                                      -> TABLE 2 (Phase 5)

TABLE 1 (Phase 4) -- Status-Quo Context View: A and B alongside ANCHOR[0A] / ANCHOR[0B].
  Use to assess whether either build option beats the status quo.
  [ -> See Table 2 (Phase 5) for the A-vs-B decision summary. ]

TABLE 2 (Phase 5) -- A-vs-B Decision Summary: A vs B only, Option 0 excluded.
  Use to reach the recommendation.
  [ <- Source: Table 1 (Phase 4), Option 0 column excluded. ]

=== PHASE 4: THREE-COLUMN MATRIX (Table 1 of 2 -- status-quo context view) ===
[ -> See Table 2 (Phase 5) for A-vs-B decision summary ]

TOKEN RECALL (2/5 register-sensitive): ANCHOR[0A] = {reproduce committed value from Phase 0}.
                                       ANCHOR[0B] = {reproduce committed value from Phase 0}.

Register: {applies from Phase 1 -- cell emphasis dimension}
If register = exec: lead each non-N/A cell with business impact signal.
  Format: Rating + one-phrase business signal. Omit implementation-level detail.
If register = engineering: lead each non-N/A cell with implementation signal.
  Format: Rating + one-phrase technical signal. Include dependency or correctness risk.
If register = general: balanced. Format: Rating + one-phrase signal.

N/A cells for Option 0 are by design and must be labeled explicitly.
Option 0 column header must use ANCHOR[0A] and ANCHOR[0B] token names from Phase 0.

| Dimension              | Option A: {option_a} | Option B: {option_b} | Option 0: ANCHOR[0A] / ANCHOR[0B] |
|------------------------|----------------------|----------------------|-----------------------------------|
| Feasibility            |                      |                      | N/A (no build required)           |
| Inertia threat         | [vs ANCHOR[0A]]      | [vs ANCHOR[0B]]      | N/A (this IS the anchor)          |
| Risk                   |                      |                      | Continuation risk: ...            |
| Competitive position   |                      |                      | ANCHOR advantage: ...             |

Fill all non-N/A cells using the register-appropriate format.

=== PHASE 5: TWO-COLUMN COMPARISON SUMMARY (Table 2 of 2 -- A-vs-B decision view) ===
[ <- Source: Table 1 (Phase 4); Option 0 column excluded. Use this table to reach the recommendation. ]

TOKEN RECALL (3/5 register-sensitive): ANCHOR[0A] = {reproduce committed value from Phase 0}.
                                       ANCHOR[0B] = {reproduce committed value from Phase 0}.

Extract A-vs-B signal from Phase 4 into a scannable 2-column view.
A reader should reach the recommendation from this table without re-reading Phase 3 or 4.

Register: {applies from Phase 1 -- cell emphasis dimension}
If register = exec: business impact signal leads each cell.
If register = engineering: implementation signal leads each cell.
If register = general: balanced content.

| Dimension              | Option A | Option B |
|------------------------|----------|----------|
| Feasibility            |          |          |
| Inertia threat         |          |          |
| Risk                   |          |          |
| Competitive position   |          |          |

Format: Rating + one-phrase signal. No empty cells.

=== PHASE 6: OPTION 0 VERDICT AND GATE ===

TOKEN RECALL (anchor-sensitive): ANCHOR[0A] = {reproduce committed value from Phase 0}.
                                  ANCHOR[0B] = {reproduce committed value from Phase 0}.

Step 1 -- Issue bilateral verdicts (each independently grounded, one sentence each):

VERDICT A: Teams would [keep using ANCHOR[0A] / build Option A] rather than [build Option A /
  keep using ANCHOR[0A]] because {specific mechanism from Phase 3 inertia analysis}.
  Inertia threat: High / Medium / Low.

VERDICT B: Teams would [keep using ANCHOR[0B] / build Option B] rather than [build Option B /
  keep using ANCHOR[0B]] because {specific mechanism from Phase 3 inertia analysis}.
  Inertia threat: High / Medium / Low.

These verdicts are independent. VERDICT A does not reference Option B. VERDICT B does not
reference Option A. Each verdict stands alone against its own ANCHOR baseline.

Step 2 -- Fire gate based on verdicts:

If VERDICT A = High AND VERDICT B = High:
  "INERTIA GATE: ANCHOR[0A] beats Option A (see VERDICT A). ANCHOR[0B] beats Option B
  (see VERDICT B). Teams will not build either option without a forcing function. 'Build
  neither' is the leading recommendation. If proceeding, name the forcing function explicitly."
  The recommendation in Phase 7 must address this gate.

If exactly one verdict = High:
  "INERTIA NOTE: ANCHOR[{0A|0B}] beats Option {A|B} (see VERDICT {A|B}), but Option {A|B}
  clears the do-nothing bar (see VERDICT {A|B}). Asymmetry may outweigh other dimension signals."

If neither verdict = High:
  "Inertia check passed -- both Options A and B beat their ANCHOR baselines
  (VERDICT A: {A-rating}, VERDICT B: {B-rating})."

=== PHASE 7: RECOMMENDATION ===

TOKEN RECALL (4/5 register-sensitive): ANCHOR[0A] = {reproduce committed value from Phase 0}.
                                       ANCHOR[0B] = {reproduce committed value from Phase 0}.

State: choose Option A / choose Option B / build neither / defer.

Register: {applies from Phase 1 -- lead structure dimension}
If register = exec:
  Lead with: recommendation and business risk of not taking it. One sentence each.
  Then: trade-off (what is given up by not choosing the other option).
  Omit implementation detail.
If register = engineering:
  Lead with: feasibility delta and primary technical risk.
  Then: recommendation.
  Then: trade-off (what is given up technically).
If register = general:
  Recommendation, primary reason, trade-off in one paragraph.

All registers:
- If GATE A fired (both verdicts High): either "build neither" OR name the forcing function
  that overrides the inertia evidence. Reference ANCHOR[0A] and ANCHOR[0B] in the gate language.
- Recommendation traceable to Table 2 (Phase 5) -- do not assert a winner that
  contradicts the matrix signals without explicit justification. If the recommendation
  diverges from the matrix plurality, state the reason explicitly.

=== PHASE 8: STRUCTURAL AUDIT (pre-artifact gate) ===

Before writing the artifact in Phase 9, self-verify each item below.
If any item fails, correct the affected section NOW -- before proceeding to Phase 9.
The artifact must reflect the corrected state, not the raw output.

AUDIT CHECKLIST:
[ ] Phase 0: ANCHOR[0A] and ANCHOR[0B] committed before Phase 1?
    Evidence: "Binding committed." line printed.
[ ] Phase 1: register contract printed with TOKEN RECALL sequence index
    ("(1/5) at Phase 3, (2/5) at Phase 4, (3/5) at Phase 5, (4/5) at Phase 7, (5/5) at Phase 10")?
[ ] Phase 3 TOKEN RECALL (1/5): labeled block present at top of Phase 3?
[ ] Phase 3 inertia: both A and B independently checked vs ANCHOR[0A] and ANCHOR[0B]?
    Failure pattern: checking which build option teams prefer instead of vs anchor.
[ ] Phase 4 TOKEN RECALL (2/5): labeled block present at top of Phase 4?
[ ] TABLE GUIDE present before Phase 4? Question-keyed routing to TABLE 1 and TABLE 2?
[ ] Phase 4 header carries "[ -> See Table 2 (Phase 5)... ]"?
[ ] Phase 5 TOKEN RECALL (3/5): labeled block present at top of Phase 5?
[ ] Phase 5 header carries "[ <- Source: Table 1 (Phase 4)... ]"?
[ ] Phase 6 VERDICT A and VERDICT B both present and independently grounded?
    Failure pattern: either verdict references the other option or their anchor.
    Independence constraint: VERDICT A does not name Option B; VERDICT B does not name Option A.
[ ] Phase 6 TOKEN RECALL (anchor-sensitive): labeled block present?
[ ] Phase 7 TOKEN RECALL (4/5): labeled block present? Recommendation traceable to Table 2?
    If recommendation diverges from matrix plurality: reason stated explicitly?
[ ] If GATE A fired in Phase 6: "build neither" named OR forcing function named in Phase 7?
[ ] Phase 10 TOKEN RECALL (5/5): AMEND handler opens with TOKEN RECALL (5/5) before any
    sub-type runs. [Structural commitment -- verify label "(5/5 register-sensitive)" present
    at top of Phase 10 text block above. Runtime verified at invocation.]
[ ] TOKEN RECALL sequence count: labels (1/5) through (5/5) all present = 5/5 register-sensitive
    phases covered. Count from Phase 1 sequence index.

Print: "PRE-ARTIFACT AUDIT -- {N}/15 checks passed. TOKEN RECALL sequence: {count}/5. Proceeding to artifact write."
If any check failed: print which item failed and the correction applied, THEN proceed to Phase 9.

=== PHASE 9: ARTIFACT ===

Write to simulations/discover/compare/{topic}-compare-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  option_a: {option_a}
  option_b: {option_b}
  anchor_0a: {ANCHOR[0A] committed in Phase 0}
  anchor_0b: {ANCHOR[0B] committed in Phase 0}
  audience: {exec|engineering|general}
  feasibility_a: High|Medium|Low
  feasibility_b: High|Medium|Low
  inertia_a: High|Medium|Low
  inertia_b: High|Medium|Low
  risk_a: High|Medium|Low
  risk_b: High|Medium|Low
  inertia_gate: passed|note|warning
  recommendation: A|B|neither|defer
  neither_path_surfaced: true|false
  option_0_matrix: true
  verdict_a: build|inertia
  verdict_b: build|inertia
  amended: false

=== PHASE 10: AMEND HANDLER ===

Activates when the user says AMEND after the base output.

TOKEN RECALL (5/5 register-sensitive): ANCHOR[0A] = {reproduce committed value from Phase 0}.
                                       ANCHOR[0B] = {reproduce committed value from Phase 0}.

Three types -- execute the matching protocol:

AMEND TYPE 1 -- Add Option C: {option_c}

1. Define ANCHOR[0C] := {what teams do today instead of building C}.
   Print: "ANCHOR[0C] = {value}. Binding extended."
   TOKEN RECALL at each Option C analysis sub-section:
   "ANCHOR[0C] = {reproduce committed value}."
2. Run Option C through all four dimensions vs ANCHOR[0C]:
   - Feasibility: High / Medium / Low + one reason.
     Register: apply Phase 1 contract [cell emphasis dimension].
   - Inertia (INERTIA RULE): Would teams keep using ANCHOR[0C] instead of building C?
     Name the specific mechanism. Rate: High / Medium / Low.
   - Risk: Primary failure mode. High / Medium / Low.
     Register: apply Phase 1 contract [risk framing dimension].
   - Competitive position: At least one concrete vector vs ANCHOR[0C]. Anti-pattern guard applies.
     Register: apply Phase 1 contract [competitive framing dimension].
   - Issue VERDICT C: same bilateral verdict structure as Phase 6.
3. Expand Table 1 (Phase 4) to four columns: add Option C column.
   Update header: "Table 1 of 2 -- Status-Quo Context View (A / B / C / Option 0)"
   Update cross-reference: "[ -> See Table 2 (Phase 5) for A-vs-B-vs-C decision summary ]"
   Option 0 column header: "Option 0: ANCHOR[0A] / ANCHOR[0B] / ANCHOR[0C]"
   Register: apply Phase 1 contract to new Option C cells.
4. Update Table 2 (Phase 5) to three columns A/B/C.
   Update header: "Table 2 of 2 -- A-vs-B-vs-C Decision Summary"
   Update cross-reference: "[ <- Source: Table 1 (Phase 4); Option 0 column excluded. ]"
   Register: apply Phase 1 contract to new Option C cells.
   Verify: Option C ratings in Table 1 and Table 2 match.
5. Re-run Phase 6 verdict-and-gate for all three options.
   TOKEN RECALL: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. ANCHOR[0C] = {value}."
6. Revise recommendation: A / B / C / build neither / defer.
   TOKEN RECALL: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. ANCHOR[0C] = {value}."
   If changed, name what changed and why. Anti-contradiction applies to updated Table 2.
   Register: apply Phase 1 contract [lead structure dimension] to revised recommendation.
7. Update artifact: add anchor_0c, option_c, verdict_c, update recommendation, amended: true.

AMEND TYPE 2 -- Weight dimension: {dimension} x{weight}

1. Apply weight multiplier to named dimension across Table 2 (Phase 5).
   Valid: feasibility, inertia, risk, competitive. Weight: x2 or x0.5.
2. Mark weighted dimension: "Feasibility [x2]".
3. Determine aggregate winner under new weighting.
4. Revise recommendation if weighting changes plurality.
   Name the delta explicitly.
   Register: apply Phase 1 contract [lead structure dimension] to revised recommendation.
5. Update artifact: weight_{dimension}: {weight}, amended: true.

AMEND TYPE 3 -- Shift audience: {exec|engineering}

1. Re-render Table 1 (Phase 4), Table 2 (Phase 5), and Phase 7 (recommendation)
   for the specified register per Phase 1 contract.
   exec: business impact cell framing; recommendation leads; omit implementation detail.
   engineering: implementation signal cell framing; feasibility leads; full technical framing.
2. Underlying evidence unchanged. ANCHOR[0A] and ANCHOR[0B] token references maintained.
   Presentation layer only.
3. Note: "Audience amendment: {exec|engineering} -- re-rendered for register."
4. Do not update the artifact file.
```

---

## V-04: r7-canonical (combination axis)

Axis: Combination -- V-01 (Phase 10 AMEND TOKEN RECALL structural check in audit) +
V-02 (RECALL COVERAGE COUNT block in audit header) + V-03 (numbered TOKEN RECALL blocks
as n/5 throughout phases + sequence index in C-16 declaration). Phase 8 audit: 15 items
(14 from V-01/V-02 + V-03's count-match item). Three-layer C-24 contract: declare count
in C-16 sequence index (V-03) -> label each recall block (V-03) -> assert count in audit
header (V-02) -> verify Phase 10 structural commitment (V-01).

Hypothesis: All three R7 mechanisms close C-24 independently; combining them creates
the strongest verifiable form. The sequence label "(n/5)" makes TOKEN RECALL blocks
scannable by position. The count assertion header makes coverage verifiable without
counting items. The Phase 10 structural check closes the count gap (5/5). A reader can
verify C-24 compliance in three steps: (1) check Phase 1 sequence index lists 5 phases;
(2) scan for labels (1/5)-(5/5); (3) check audit RECALL COVERAGE COUNT = 5/5. Predicted 100.0.

```
You are running /discover-compare for topic: {topic}.
Comparing: Option A -- {option_a} vs Option B -- {option_b}.
Audience: {audience}  (exec | engineering | general -- default: general)

=== PHASE 0: STATUS QUO ANCHOR (Option 0) ===

Before any analysis, name the behavior teams fall back on today if neither option is built.

ANCHOR[0A] := {what teams do today instead of building Option A}
ANCHOR[0B] := {what teams do today instead of building Option B}

Binding rule: all inertia analysis, competitive analysis, gate logic, and recommendation
phases must reference ANCHOR[0A] and ANCHOR[0B] by token name -- not by prose paraphrase.
Any reference to "the status quo," "current approach," or "doing nothing" without the
token name violates this binding.

Print: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. Binding committed."

=== PHASE 1: AUDIENCE REGISTER ===

Read the audience parameter. This register governs the following phases and dimensions:

  Phase 3 (dimension analysis):
    - Risk sub-section: failure mode framing language
    - Competitive sub-section: differentiation vector framing language
  Phase 4 (three-column matrix): cell content emphasis and vocabulary
  Phase 5 (two-column summary): cell content emphasis and vocabulary
  Phase 7 (recommendation): lead structure and level of detail
  Phase 10 (AMEND handler): revised recommendation framing

5 register-sensitive phases total: {3, 4, 5, 7, 10}.
Each will carry a numbered TOKEN RECALL block: (1/5) through (5/5).

exec: business signal leads all register-sensitive phases and dimensions;
  implementation detail omitted; language is investment/risk/market.
  Phase 3 risk: frame as business impact (revenue, partner dependency, market timing).
  Phase 3 competitive: frame as market differentiation, cost-of-delay, switching cost.
  Phase 4/5 cells: lead with business signal. Omit build-level detail.
  Phase 7: recommendation leads; business risk of not acting second; trade-off third.
  Phase 10: same as Phase 7 structure.

engineering: implementation signal leads all register-sensitive phases and dimensions;
  technical risk detail present; language is build/integrate/operate.
  Phase 3 risk: frame as technical failure mode (race condition, schema drift, dependency brittleness).
  Phase 3 competitive: frame as build cost, latency advantage, dependency graph.
  Phase 4/5 cells: lead with technical signal. Include dependency or correctness risk.
  Phase 7: feasibility delta and technical risk lead; recommendation second; trade-off third.
  Phase 10: same as Phase 7 structure.

general (default): neutral -- no routing applied.

Print: "Register: {exec|engineering|general}. Contract: Phase 3 [risk, competitive],
  Phase 4 [cell emphasis], Phase 5 [cell emphasis], Phase 7 [lead structure], Phase 10 [framing].
  TOKEN RECALL sequence: (1/5) at Phase 3, (2/5) at Phase 4, (3/5) at Phase 5,
  (4/5) at Phase 7, (5/5) at Phase 10."

=== PHASE 2: CONTEXT ===

Read existing discover artifacts for this topic:
- Glob: simulations/discover/**/{topic}-*-*.md

Print inventory: | skill | date | path | for each file found.
If prior artifacts exist, note any signals that refine the ANCHOR[0A] or ANCHOR[0B]
characterization committed in Phase 0. Do not change committed tokens -- note refinements only.
If none found: "No prior discover artifacts -- proceeding from inputs."

=== PHASE 3: DIMENSION ANALYSIS ===

TOKEN RECALL (1/5 register-sensitive): ANCHOR[0A] = {reproduce committed value from Phase 0}.
                                       ANCHOR[0B] = {reproduce committed value from Phase 0}.

Run each dimension across both options before moving to the next.
ANCHOR[0A] is the reference for all Option A inertia and competitive analysis.
ANCHOR[0B] is the reference for all Option B inertia and competitive analysis.

--- Feasibility ---
Option A: High / Medium / Low. One reason (skill, tooling, timeline).
Option B: High / Medium / Low. One reason.

--- Inertia ---
INERTIA RULE: Inertia is checked for BOTH options independently.
The question for A: would teams keep using ANCHOR[0A] INSTEAD OF building Option A?
  Name the specific mechanism that makes ANCHOR[0A] a viable substitute.
  Threat rating: High / Medium / Low.
The question for B: would teams keep using ANCHOR[0B] INSTEAD OF building Option B?
  Name the specific mechanism that makes ANCHOR[0B] a viable substitute.
  Threat rating: High / Medium / Low.

--- Risk ---
Option A: Primary failure mode. Rating: High / Medium / Low.
Option B: Same.
Register: {applies from Phase 1 -- risk framing dimension}
If register = exec: frame as business impact (revenue impact, partner dependency).
If register = engineering: frame as technical failure mode (race condition, schema drift).
If register = general: standard format.
Option 0 continuation risk: What is the long-term cost of staying with ANCHOR[0A] and ANCHOR[0B]
  rather than building either option? One sentence -- enters the 3-column matrix.

--- Competitive Position ---
ANTI-PATTERN GUARD: Generic competitive analysis uses phrases such as "more competitive,"
"better positioned," or "stronger in the market" without specifying the mechanism.
Such phrasing is insufficient and will fail this criterion. Name the concrete vector:
  Speed: throughput, latency, or iteration rate advantage
  Cost: build, operating, or switching cost difference
  Ecosystem: integration depth, lock-in reduction, or partner leverage
  Capability: what ANCHOR[0A] / ANCHOR[0B] cannot do that this option enables

Option A: At least one concrete vector vs ANCHOR[0A].
Register: {applies from Phase 1 -- competitive framing dimension}
If register = exec: frame in market/investment terms.
If register = engineering: frame in build/operate/latency terms.
Option B: Same requirement and same register instruction, vs ANCHOR[0B].
Option 0 competitive position: What do ANCHOR[0A] and ANCHOR[0B] offer today
  that Option A and Option B do not yet match?

=== TABLE GUIDE ===

Which question are you answering?
  Does either option beat doing nothing (ANCHOR[0A] / ANCHOR[0B])? -> TABLE 1 (Phase 4)
  Which option should we build?                                      -> TABLE 2 (Phase 5)

TABLE 1 (Phase 4) -- Status-Quo Context View: A and B alongside ANCHOR[0A] / ANCHOR[0B].
  Use to assess whether either build option beats the status quo.
  [ -> See Table 2 (Phase 5) for the A-vs-B decision summary. ]

TABLE 2 (Phase 5) -- A-vs-B Decision Summary: A vs B only, Option 0 excluded.
  Use to reach the recommendation.
  [ <- Source: Table 1 (Phase 4), Option 0 column excluded. ]

=== PHASE 4: THREE-COLUMN MATRIX (Table 1 of 2 -- status-quo context view) ===
[ -> See Table 2 (Phase 5) for A-vs-B decision summary ]

TOKEN RECALL (2/5 register-sensitive): ANCHOR[0A] = {reproduce committed value from Phase 0}.
                                       ANCHOR[0B] = {reproduce committed value from Phase 0}.

Register: {applies from Phase 1 -- cell emphasis dimension}
If register = exec: lead each non-N/A cell with business impact signal.
  Format: Rating + one-phrase business signal. Omit implementation-level detail.
If register = engineering: lead each non-N/A cell with implementation signal.
  Format: Rating + one-phrase technical signal. Include dependency or correctness risk.
If register = general: balanced. Format: Rating + one-phrase signal.

N/A cells for Option 0 are by design and must be labeled explicitly.
Option 0 column header must use ANCHOR[0A] and ANCHOR[0B] token names from Phase 0.

| Dimension              | Option A: {option_a} | Option B: {option_b} | Option 0: ANCHOR[0A] / ANCHOR[0B] |
|------------------------|----------------------|----------------------|-----------------------------------|
| Feasibility            |                      |                      | N/A (no build required)           |
| Inertia threat         | [vs ANCHOR[0A]]      | [vs ANCHOR[0B]]      | N/A (this IS the anchor)          |
| Risk                   |                      |                      | Continuation risk: ...            |
| Competitive position   |                      |                      | ANCHOR advantage: ...             |

Fill all non-N/A cells using the register-appropriate format.

=== PHASE 5: TWO-COLUMN COMPARISON SUMMARY (Table 2 of 2 -- A-vs-B decision view) ===
[ <- Source: Table 1 (Phase 4); Option 0 column excluded. Use this table to reach the recommendation. ]

TOKEN RECALL (3/5 register-sensitive): ANCHOR[0A] = {reproduce committed value from Phase 0}.
                                       ANCHOR[0B] = {reproduce committed value from Phase 0}.

Extract A-vs-B signal from Phase 4 into a scannable 2-column view.
A reader should reach the recommendation from this table without re-reading Phase 3 or 4.

Register: {applies from Phase 1 -- cell emphasis dimension}
If register = exec: business impact signal leads each cell.
If register = engineering: implementation signal leads each cell.
If register = general: balanced content.

| Dimension              | Option A | Option B |
|------------------------|----------|----------|
| Feasibility            |          |          |
| Inertia threat         |          |          |
| Risk                   |          |          |
| Competitive position   |          |          |

Format: Rating + one-phrase signal. No empty cells.

=== PHASE 6: OPTION 0 VERDICT AND GATE ===

TOKEN RECALL (anchor-sensitive): ANCHOR[0A] = {reproduce committed value from Phase 0}.
                                  ANCHOR[0B] = {reproduce committed value from Phase 0}.

Step 1 -- Issue bilateral verdicts (each independently grounded, one sentence each):

VERDICT A: Teams would [keep using ANCHOR[0A] / build Option A] rather than [build Option A /
  keep using ANCHOR[0A]] because {specific mechanism from Phase 3 inertia analysis}.
  Inertia threat: High / Medium / Low.

VERDICT B: Teams would [keep using ANCHOR[0B] / build Option B] rather than [build Option B /
  keep using ANCHOR[0B]] because {specific mechanism from Phase 3 inertia analysis}.
  Inertia threat: High / Medium / Low.

These verdicts are independent. VERDICT A does not reference Option B. VERDICT B does not
reference Option A. Each verdict stands alone against its own ANCHOR baseline.

Step 2 -- Fire gate based on verdicts:

If VERDICT A = High AND VERDICT B = High:
  "INERTIA GATE: ANCHOR[0A] beats Option A (see VERDICT A). ANCHOR[0B] beats Option B
  (see VERDICT B). Teams will not build either option without a forcing function. 'Build
  neither' is the leading recommendation. If proceeding, name the forcing function explicitly."
  The recommendation in Phase 7 must address this gate.

If exactly one verdict = High:
  "INERTIA NOTE: ANCHOR[{0A|0B}] beats Option {A|B} (see VERDICT {A|B}), but Option {A|B}
  clears the do-nothing bar (see VERDICT {A|B}). Asymmetry may outweigh other dimension signals."

If neither verdict = High:
  "Inertia check passed -- both Options A and B beat their ANCHOR baselines
  (VERDICT A: {A-rating}, VERDICT B: {B-rating})."

=== PHASE 7: RECOMMENDATION ===

TOKEN RECALL (4/5 register-sensitive): ANCHOR[0A] = {reproduce committed value from Phase 0}.
                                       ANCHOR[0B] = {reproduce committed value from Phase 0}.

State: choose Option A / choose Option B / build neither / defer.

Register: {applies from Phase 1 -- lead structure dimension}
If register = exec:
  Lead with: recommendation and business risk of not taking it. One sentence each.
  Then: trade-off (what is given up by not choosing the other option).
  Omit implementation detail.
If register = engineering:
  Lead with: feasibility delta and primary technical risk.
  Then: recommendation.
  Then: trade-off (what is given up technically).
If register = general:
  Recommendation, primary reason, trade-off in one paragraph.

All registers:
- If GATE A fired (both verdicts High): either "build neither" OR name the forcing function
  that overrides the inertia evidence. Reference ANCHOR[0A] and ANCHOR[0B] in the gate language.
- Recommendation traceable to Table 2 (Phase 5) -- do not assert a winner that
  contradicts the matrix signals without explicit justification. If the recommendation
  diverges from the matrix plurality, state the reason explicitly.

=== PHASE 8: STRUCTURAL AUDIT (pre-artifact gate) ===

Before writing the artifact in Phase 9, self-verify each item below.
If any item fails, correct the affected section NOW -- before proceeding to Phase 9.
The artifact must reflect the corrected state, not the raw output.

RECALL COVERAGE COUNT: C-16 declared 5 register-sensitive phases {3, 4, 5, 7, 10}.
Required TOKEN RECALL audit items: 5.
These items appear as: item 3 (Phase 3 -- 1/5), item 5 (Phase 4 -- 2/5),
  item 8 (Phase 5 -- 3/5), item 12 (Phase 7 -- 4/5), item 15 (Phase 10 AMEND -- 5/5).
Verify count before proceeding: {count labeled recall items in output} == 5.

AUDIT CHECKLIST:
[ ] Phase 0: ANCHOR[0A] and ANCHOR[0B] committed before Phase 1?
    Evidence: "Binding committed." line printed.
[ ] Phase 1: register contract printed with TOKEN RECALL sequence index
    ("(1/5) at Phase 3, (2/5) at Phase 4, (3/5) at Phase 5, (4/5) at Phase 7, (5/5) at Phase 10")?
[ ] Phase 3 TOKEN RECALL (1/5): labeled block present at top of Phase 3?
[ ] Phase 3 inertia: both A and B independently checked vs ANCHOR[0A] and ANCHOR[0B]?
    Failure pattern: checking which build option teams prefer instead of vs anchor.
[ ] Phase 4 TOKEN RECALL (2/5): labeled block present at top of Phase 4?
[ ] TABLE GUIDE present before Phase 4? Question-keyed routing to TABLE 1 and TABLE 2?
[ ] Phase 4 header carries "[ -> See Table 2 (Phase 5)... ]"?
[ ] Phase 5 TOKEN RECALL (3/5): labeled block present at top of Phase 5?
[ ] Phase 5 header carries "[ <- Source: Table 1 (Phase 4)... ]"?
[ ] Phase 6 VERDICT A and VERDICT B both present and independently grounded?
    Failure pattern: either verdict references the other option or their anchor.
    Independence constraint: VERDICT A does not name Option B; VERDICT B does not name Option A.
[ ] Phase 6 TOKEN RECALL (anchor-sensitive): labeled block present?
[ ] Phase 7 TOKEN RECALL (4/5): labeled block present? Recommendation traceable to Table 2?
    If recommendation diverges from matrix plurality: reason stated explicitly?
[ ] If GATE A fired in Phase 6: "build neither" named OR forcing function named in Phase 7?
[ ] RECALL COVERAGE COUNT match: count of labeled "(n/5)" blocks in output equals 5?
    Expected: labels (1/5) through (5/5) each appear exactly once.
[ ] Phase 10 AMEND TOKEN RECALL (5/5): AMEND handler opens with TOKEN RECALL (5/5) before
    any sub-type runs. [Structural commitment -- verify label "(5/5 register-sensitive)"
    present at top of Phase 10 text above. Runtime verified at invocation.]

Print: "PRE-ARTIFACT AUDIT -- {N}/15 checks passed. RECALL COVERAGE: {count}/5. Proceeding to artifact write."
If any check failed: print which item failed and the correction applied, THEN proceed to Phase 9.

=== PHASE 9: ARTIFACT ===

Write to simulations/discover/compare/{topic}-compare-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  option_a: {option_a}
  option_b: {option_b}
  anchor_0a: {ANCHOR[0A] committed in Phase 0}
  anchor_0b: {ANCHOR[0B] committed in Phase 0}
  audience: {exec|engineering|general}
  feasibility_a: High|Medium|Low
  feasibility_b: High|Medium|Low
  inertia_a: High|Medium|Low
  inertia_b: High|Medium|Low
  risk_a: High|Medium|Low
  risk_b: High|Medium|Low
  inertia_gate: passed|note|warning
  recommendation: A|B|neither|defer
  neither_path_surfaced: true|false
  option_0_matrix: true
  verdict_a: build|inertia
  verdict_b: build|inertia
  amended: false

=== PHASE 10: AMEND HANDLER ===

Activates when the user says AMEND after the base output.

TOKEN RECALL (5/5 register-sensitive): ANCHOR[0A] = {reproduce committed value from Phase 0}.
                                       ANCHOR[0B] = {reproduce committed value from Phase 0}.

Three types -- execute the matching protocol:

AMEND TYPE 1 -- Add Option C: {option_c}

1. Define ANCHOR[0C] := {what teams do today instead of building C}.
   Print: "ANCHOR[0C] = {value}. Binding extended."
   TOKEN RECALL at each Option C analysis sub-section:
   "ANCHOR[0C] = {reproduce committed value}."
2. Run Option C through all four dimensions vs ANCHOR[0C]:
   - Feasibility: High / Medium / Low + one reason.
     Register: apply Phase 1 contract [cell emphasis dimension].
   - Inertia (INERTIA RULE): Would teams keep using ANCHOR[0C] instead of building C?
     Name the specific mechanism. Rate: High / Medium / Low.
   - Risk: Primary failure mode. High / Medium / Low.
     Register: apply Phase 1 contract [risk framing dimension].
   - Competitive position: At least one concrete vector vs ANCHOR[0C]. Anti-pattern guard applies.
     Register: apply Phase 1 contract [competitive framing dimension].
   - Issue VERDICT C: same bilateral verdict structure as Phase 6.
3. Expand Table 1 (Phase 4) to four columns: add Option C column.
   Update header: "Table 1 of 2 -- Status-Quo Context View (A / B / C / Option 0)"
   Update cross-reference: "[ -> See Table 2 (Phase 5) for A-vs-B-vs-C decision summary ]"
   Option 0 column header: "Option 0: ANCHOR[0A] / ANCHOR[0B] / ANCHOR[0C]"
   Register: apply Phase 1 contract to new Option C cells.
4. Update Table 2 (Phase 5) to three columns A/B/C.
   Update header: "Table 2 of 2 -- A-vs-B-vs-C Decision Summary"
   Update cross-reference: "[ <- Source: Table 1 (Phase 4); Option 0 column excluded. ]"
   Register: apply Phase 1 contract to new Option C cells.
   Verify: Option C ratings in Table 1 and Table 2 match.
5. Re-run Phase 6 verdict-and-gate for all three options.
   TOKEN RECALL: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. ANCHOR[0C] = {value}."
6. Revise recommendation: A / B / C / build neither / defer.
   TOKEN RECALL: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. ANCHOR[0C] = {value}."
   If changed, name what changed and why. Anti-contradiction applies to updated Table 2.
   Register: apply Phase 1 contract [lead structure dimension] to revised recommendation.
7. Update artifact: add anchor_0c, option_c, verdict_c, update recommendation, amended: true.

AMEND TYPE 2 -- Weight dimension: {dimension} x{weight}

1. Apply weight multiplier to named dimension across Table 2 (Phase 5).
   Valid: feasibility, inertia, risk, competitive. Weight: x2 or x0.5.
2. Mark weighted dimension: "Feasibility [x2]".
3. Determine aggregate winner under new weighting.
4. Revise recommendation if weighting changes plurality.
   Name the delta explicitly.
   Register: apply Phase 1 contract [lead structure dimension] to revised recommendation.
5. Update artifact: weight_{dimension}: {weight}, amended: true.

AMEND TYPE 3 -- Shift audience: {exec|engineering}

1. Re-render Table 1 (Phase 4), Table 2 (Phase 5), and Phase 7 (recommendation)
   for the specified register per Phase 1 contract.
   exec: business impact cell framing; recommendation leads; omit implementation detail.
   engineering: implementation signal cell framing; feasibility leads; full technical framing.
2. Underlying evidence unchanged. ANCHOR[0A] and ANCHOR[0B] token references maintained.
   Presentation layer only.
3. Note: "Audience amendment: {exec|engineering} -- re-rendered for register."
4. Do not update the artifact file.
```

---

## V-05: lean-c24-aware (lifecycle emphasis lean axis)

Axis: Lifecycle emphasis (lean) -- V-05/R6 lean with two fixes:
(1) Phase 5 audit gains item 6 "recommendation traceable to Table 2" (promotes C-21 from
PARTIAL to PASS -- was missing one of the 6 minimum required audit items).
(2) Phase 5 audit item 4 gains explicit independence constraint language for C-23
("VERDICT A does not reference Option B; VERDICT B does not reference Option A").
C-24 remains N/A: the lean form has no audience register (C-15/C-16 fail), so C-20 is
PARTIAL, and C-24 requires C-20 to be implemented (scores N/A = 0 when C-20 is absent).

Hypothesis: V-05/R6 scored C-21 PARTIAL (5/6 minimum items; missing "recommendation
traceable") and C-23 PARTIAL (independence implied but audit item said "independently
grounded" not "does not reference the other option"). Adding the missing C-21 item and
sharpening the C-23 language achieves C-21 PASS and C-23 PASS. Predicted ~95.9 on v6
rubric (up from ~95.3).

```
You are running /discover-compare for topic: {topic}.
Comparing: Option A -- {option_a} vs Option B -- {option_b}.

=== PHASE 0: STATUS QUO ANCHOR (Option 0) ===

Before any analysis, name the behavior teams fall back on today if neither option is built.

ANCHOR[0A] := {what teams do today instead of building Option A}
ANCHOR[0B] := {what teams do today instead of building Option B}

Binding rule: all inertia analysis, competitive analysis, gate logic, and recommendation
must reference ANCHOR[0A] and ANCHOR[0B] by token name -- not by prose paraphrase.
Any reference to "the status quo," "current approach," or "doing nothing" without the
token name violates this binding.

Print: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. Binding committed."

=== PHASE 1: CONTEXT ===

Read existing discover artifacts for this topic:
- Glob: simulations/discover/**/{topic}-*-*.md

Print inventory: | skill | date | path | for each file found.
If prior artifacts exist, note any signals that refine the ANCHOR[0A] or ANCHOR[0B]
characterization committed in Phase 0. Do not change committed tokens.
If none found: "No prior discover artifacts -- proceeding from inputs."

=== PHASE 2: DIMENSION ANALYSIS ===

Run each dimension across both options before moving to the next.

--- Feasibility ---
Option A: High / Medium / Low. One reason (skill, tooling, timeline).
Option B: High / Medium / Low. One reason.

--- Inertia ---
TOKEN RECALL: ANCHOR[0A] = {reproduce committed value from Phase 0}.
              ANCHOR[0B] = {reproduce committed value from Phase 0}.

INERTIA RULE: Inertia is checked for BOTH options independently.
The question for A: would teams keep using ANCHOR[0A] INSTEAD OF building Option A?
  Name the specific mechanism that makes ANCHOR[0A] a viable substitute.
  Threat rating: High / Medium / Low.
The question for B: would teams keep using ANCHOR[0B] INSTEAD OF building Option B?
  Name the specific mechanism that makes ANCHOR[0B] a viable substitute.
  Threat rating: High / Medium / Low.

--- Risk ---
Option A: Primary failure mode. Rating: High / Medium / Low.
Option B: Same.
Option 0 continuation risk: What is the long-term cost of staying with ANCHOR[0A] and ANCHOR[0B]
  rather than building either option? One sentence -- enters the 3-column matrix.

--- Competitive Position ---
ANTI-PATTERN GUARD: Generic competitive analysis uses phrases such as "more competitive,"
"better positioned," or "stronger in the market" without specifying the mechanism.
Such phrasing is insufficient. Name the concrete vector:
  Speed: throughput, latency, or iteration rate advantage
  Cost: build, operating, or switching cost difference
  Ecosystem: integration depth, lock-in reduction, or partner leverage
  Capability: what ANCHOR[0A] / ANCHOR[0B] cannot do that this option enables

Option A: At least one concrete vector vs ANCHOR[0A].
Option B: Same requirement, vs ANCHOR[0B].
Option 0 competitive position: What do ANCHOR[0A] and ANCHOR[0B] offer today
  that Option A and Option B do not yet match?

=== PHASE 3: MATRICES ===

Which question are you answering?
  Does either option beat doing nothing (ANCHOR[0A] / ANCHOR[0B])? -> TABLE 1 below
  Which option should we build?                                      -> TABLE 2 below

TABLE 1 of 2 -- Status-Quo Context View (A and B alongside Option 0)
[ -> See Table 2 below for A-vs-B decision summary. ]

| Dimension              | Option A: {option_a} | Option B: {option_b} | Option 0: ANCHOR[0A] / ANCHOR[0B] |
|------------------------|----------------------|----------------------|-----------------------------------|
| Feasibility            |                      |                      | N/A (no build required)           |
| Inertia threat         | [vs ANCHOR[0A]]      | [vs ANCHOR[0B]]      | N/A (this IS the anchor)          |
| Risk                   |                      |                      | Continuation risk: ...            |
| Competitive position   |                      |                      | ANCHOR advantage: ...             |

TABLE 2 of 2 -- A-vs-B Decision Summary (Option 0 excluded)
[ <- Source: Table 1 above; Option 0 column excluded. Use this table to reach the recommendation. ]

| Dimension              | Option A | Option B |
|------------------------|----------|----------|
| Feasibility            |          |          |
| Inertia threat         |          |          |
| Risk                   |          |          |
| Competitive position   |          |          |

Format: Rating + one-phrase signal. No empty cells.

=== PHASE 4: OPTION 0 VERDICT AND GATE ===

TOKEN RECALL: ANCHOR[0A] = {reproduce committed value from Phase 0}.
              ANCHOR[0B] = {reproduce committed value from Phase 0}.

Issue bilateral verdicts (each independently grounded, one sentence each):

VERDICT A: Teams would [keep using ANCHOR[0A] / build Option A] rather than [build Option A /
  keep using ANCHOR[0A]] because {specific mechanism from Phase 2 inertia analysis}.
  Inertia threat: High / Medium / Low.

VERDICT B: Teams would [keep using ANCHOR[0B] / build Option B] rather than [build Option B /
  keep using ANCHOR[0B]] because {specific mechanism from Phase 2 inertia analysis}.
  Inertia threat: High / Medium / Low.

Independence constraint: VERDICT A does not reference Option B or ANCHOR[0B].
VERDICT B does not reference Option A or ANCHOR[0A].
Each verdict stands alone against its own ANCHOR baseline only.

If VERDICT A = High AND VERDICT B = High:
  "INERTIA GATE: ANCHOR[0A] beats Option A. ANCHOR[0B] beats Option B.
  'Build neither' is the leading recommendation."

If exactly one verdict = High:
  "INERTIA NOTE: ANCHOR[{0A|0B}] beats Option {A|B}. Asymmetry may outweigh other signals."

If neither verdict = High:
  "Inertia check passed -- both options beat their ANCHOR baselines."

=== PHASE 5: STRUCTURAL AUDIT (pre-recommendation and pre-artifact gate) ===

Before writing the recommendation (Phase 6) and the artifact (Phase 7), self-verify each
item below. If any item fails, correct the affected section NOW -- before proceeding to
Phase 6. The artifact must reflect the corrected state.

AUDIT CHECKLIST:
[ ] Phase 0: ANCHOR[0A] and ANCHOR[0B] committed before Phase 1?
    Evidence: "Binding committed." line printed.
[ ] Phase 2 inertia: both A and B independently checked vs ANCHOR[0A] and ANCHOR[0B]?
    Failure pattern: checking which option teams prefer instead of each vs its anchor.
[ ] Table 1 and Table 2 present? Table 1 has Option 0 column with N/A labels?
    Table 2 excludes Option 0? Cross-reference arrows present on both table headers?
[ ] Phase 4 VERDICT A and VERDICT B both present and independently grounded?
    Independence constraint verified: VERDICT A does not reference Option B or ANCHOR[0B];
    VERDICT B does not reference Option A or ANCHOR[0A].
    Phase 4 TOKEN RECALL reproduced? Gate language uses ANCHOR token names?
[ ] If GATE fired (both verdicts High): "build neither" will be named in Phase 6 recommendation?
[ ] Recommendation will be traceable to Table 2 (Phase 3) -- Phase 6 will state the choice
    explicitly and trace it to the matrix; if diverging from plurality, reason will be explicit.

Print: "PRE-RECOMMENDATION AUDIT -- {N}/6 checks passed."
If any check failed: print which item failed and the correction applied, THEN proceed to Phase 6.

=== PHASE 6: RECOMMENDATION ===

State: choose Option A / choose Option B / build neither / defer.

Recommendation, primary reason, trade-off (what is given up by not choosing the other option)
in one paragraph.

If GATE fired in Phase 4: either "build neither" OR name the forcing function that overrides
the inertia evidence. Reference ANCHOR[0A] and ANCHOR[0B] in the gate language.

Recommendation traceable to Table 2 (Phase 3) -- do not assert a winner that contradicts
the matrix signals without explicit justification. If the recommendation diverges from the
matrix plurality, state the reason explicitly.

=== PHASE 7: ARTIFACT ===

Write to simulations/discover/compare/{topic}-compare-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  option_a: {option_a}
  option_b: {option_b}
  anchor_0a: {ANCHOR[0A] committed in Phase 0}
  anchor_0b: {ANCHOR[0B] committed in Phase 0}
  feasibility_a: High|Medium|Low
  feasibility_b: High|Medium|Low
  inertia_a: High|Medium|Low
  inertia_b: High|Medium|Low
  risk_a: High|Medium|Low
  risk_b: High|Medium|Low
  inertia_gate: passed|note|warning
  recommendation: A|B|neither|defer
  neither_path_surfaced: true|false
  option_0_matrix: true
  verdict_a: build|inertia
  verdict_b: build|inertia
  amended: false
```

---

## Predicted Scores (v6 rubric, denominator 16)

| Variation | C-22 | C-23 | C-24 | Aspirational | Total | Golden? |
|-----------|------|------|------|--------------|-------|---------|
| V-01 audit-recall-parity | PASS | PASS | PASS | 16/16 = 10.0 | 100.0 | YES |
| V-02 count-assertion-header | PASS | PASS | PASS | 16/16 = 10.0 | 100.0 | YES |
| V-03 recall-sequence-labels | PASS | PASS | PASS | 16/16 = 10.0 | 100.0 | YES |
| V-04 r7-canonical | PASS | PASS | PASS | 16/16 = 10.0 | 100.0 | YES |
| V-05 lean-c24-aware | PASS | PASS | N/A=0 | 9.5/16 = 5.94 | 95.9 | YES |

**V-01 vs V-02 vs V-03 sub-distinctions (all predict 100.0):**
- V-01: Minimum viable C-24 close. One structural check item added. No other changes.
  Audit does not announce the count explicitly; evaluator must count recall items manually.
- V-02: Makes C-24 visible at-a-glance. RECALL COVERAGE COUNT in audit header with item
  numbers. An evaluator verifying C-24 reads one line, not 14. Strongest format form.
- V-03: Makes C-24 traceable by position. Numbered "(n/5)" labels make each recall block
  identifiable in the output. Phase 1 sequence index + count-match audit item close both
  the count (C-24) and visibility (C-02) in one mechanism. Strongest phrasing-register form.
- V-04: All three. Dual verifiability: count-by-header (V-02) AND count-by-label (V-03).

**V-05 lean path to 100:**
Not achievable without audience register (C-09/C-10/C-15/C-16 will remain FAIL/0). The lean
form is structurally capped by the absence of register machinery. V-05 R7 target: 95.9 (up
from ~95.3 in R6 on v6 rubric via C-21 PARTIAL->PASS and C-23 PARTIAL->PASS).

**New R7 pattern candidates (v8 rubric):**
1. **RECALL COVERAGE COUNT header** -- audit declares required recall count at top with item
   numbers; evaluator can verify C-24 in one line without re-reading phases.
2. **Numbered TOKEN RECALL sequence labels** -- "(n/N)" labels at each recall block create
   a traceable chain; Phase 1 sequence index maps label position to phase number.
3. **C-24 verified by count assertion** -- audit header count + Phase 1 forward index + labeled
   blocks form a three-layer C-24 contract (declare -> label -> assert) analogous to the
   three-layer C-19/C-20/C-21 drift-defense contract established in earlier rounds.
