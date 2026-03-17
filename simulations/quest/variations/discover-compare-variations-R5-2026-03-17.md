Done. `discover-compare-variations-R5-2026-03-17.md` written.

---

## Round 5 — 5 Variations

| # | Label | Axis | Key change from V-04/R4 |
|---|-------|------|------------------------|
| V-01 | token-bind | Inertia framing | V-04/R4 + ANCHOR[0A]/ANCHOR[0B] tokens + binding rule; all downstream phases use token name, not prose |
| V-02 | self-verify | Role sequence | V-01 + Phase 10 structural audit: 9-item self-check before returning output |
| V-03 | inline-token-check | Phrasing register | V-01 + TOKEN RECALL header at Phases 3, 6, 7 -- model reproduces token values at point-of-use |
| V-04 | full-integration | Combination | V-01 + V-02 + V-03: all three R5 mechanisms; predicted R5 canonical |
| V-05 | lean-anchor | Lifecycle emphasis | V-05/R4 lean (no AMEND/register) + ANCHOR tokens throughout |

**Predicted scores (v4 rubric):** V-01/V-02/V-03/V-04 all 100.0; V-05 = 95.0 Golden.

**What's being tested:** R4's identified gap was V-03/R4's ANCHOR token mechanism -- the only thing not carried into V-04/R4. Each single-axis variation targets a different point in the drift lifecycle: token binding prevents silent prose substitution at declaration; inline recall catches it at point-of-use; terminal audit catches structural omissions above the token level. V-04 combines all three. V-05 tests whether token grounding alone raises the lean form's real-world robustness without changing its 95.0 score.
4/R4 uses prose "Option 0 named in Phase 0" in downstream phases -- any paraphrase is invisible. ANCHOR[0A]/ANCHOR[0B] token syntax requires literal reproduction; drift is detectable. R5 tests whether merging that token mechanism into V-04's established structure raises practical robustness without changing v4 rubric scores, and whether a self-verification audit (V-02) and inline recall (V-03) provide additional drift guards at different points in the output lifecycle.

**V-01** tests the merger: V-04 dimension contract + question-keyed TABLE GUIDE + token binding throughout. The minimal addition that closes the V-04 gap.

**V-02** tests closed-loop audit: does a terminal self-check phase that verifies 9 structural criteria before output is returned catch remaining drift that token binding alone might miss?

**V-03** tests inline recall: does reproducing the token value at point-of-use in each sensitive phase add guard beyond Phase 0 commitment alone?

**V-04** is the definitive combination: all three mechanisms simultaneously. Expected R5 canonical.

**V-05** is the lean floor with tokens: V-05/R4 without AMEND/register but with ANCHOR binding. Same score (95.0), stronger real-world behavior.

---

## V-01: token-bind (inertia framing axis)

Axis: Inertia framing -- Phase 0 commits ANCHOR[0A]/ANCHOR[0B] tokens with a binding rule.
All downstream phases that reference Option 0 must use the token name, not prose. This
is the direct merger of V-04/R4's full structure with V-03/R4's unique token mechanism.

Hypothesis: V-04/R4 passes all 18 criteria at 100.0, but its downstream inertia, gate, and
recommendation phases use prose ("Option 0 named in Phase 0"). If a model paraphrases the
anchor mid-run, the drift is invisible. ANCHOR token syntax requires literal reproduction --
any downstream phase that writes "the current approach" instead of "ANCHOR[0A]" is visibly
wrong. The merger adds the strongest C-18 form (V-03) without changing any other criterion
behavior. Predicted 100.0; no criteria regress.

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
token name violates this binding and weakens the inertia contract.

Print: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. Binding committed."

=== PHASE 1: AUDIENCE REGISTER ===

Read the audience parameter. This register governs the following phases and dimensions:

  Phase 3 (dimension analysis):
    - Risk sub-section: failure mode framing language
    - Competitive sub-section: differentiation vector framing language
  Phase 4 (three-column matrix): cell content emphasis and vocabulary
  Phase 5 (two-column summary): cell content emphasis and vocabulary
  Phase 7 (recommendation): lead structure and level of detail
  Phase 9 (AMEND handler): revised recommendation framing

exec: business signal leads all register-sensitive phases and dimensions;
  implementation detail omitted; language is investment/risk/market.
  Phase 3 risk: frame as business impact (revenue, partner dependency, market timing).
  Phase 3 competitive: frame as market differentiation, cost-of-delay, switching cost.
  Phase 4/5 cells: lead with business signal. Omit build-level detail.
  Phase 7: recommendation leads; business risk of not acting second; trade-off third.
  Phase 9: same as Phase 7 structure.

engineering: implementation signal leads all register-sensitive phases and dimensions;
  technical risk detail present; language is build/integrate/operate.
  Phase 3 risk: frame as technical failure mode (race condition, schema drift, dependency brittleness).
  Phase 3 competitive: frame as build cost, latency advantage, dependency graph.
  Phase 4/5 cells: lead with technical signal. Include dependency or correctness risk.
  Phase 7: feasibility delta and technical risk lead; recommendation second; trade-off third.
  Phase 9: same as Phase 7 structure.

general (default): neutral -- no routing applied.

Print: "Register: {exec|engineering|general}. Contract: Phase 3 [risk, competitive],
  Phase 4 [cell emphasis], Phase 5 [cell emphasis], Phase 7 [lead structure], Phase 9 [framing]."

=== PHASE 2: CONTEXT ===

Read existing discover artifacts for this topic:
- Glob: simulations/discover/**/{topic}-*-*.md

Print inventory: | skill | date | path | for each file found.
If prior artifacts exist, note any signals that refine the ANCHOR[0A] or ANCHOR[0B]
characterization committed in Phase 0. Do not change committed tokens -- note refinements only.
If none found: "No prior discover artifacts -- proceeding from inputs."

=== PHASE 3: DIMENSION ANALYSIS ===

Run each dimension across both options before moving to the next.
ANCHOR[0A] (Phase 0) is the reference for all Option A inertia and competitive analysis.
ANCHOR[0B] (Phase 0) is the reference for all Option B inertia and competitive analysis.

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

=== PHASE 6: INERTIA GATE ===

Read the Inertia threat cells from Table 2 (Phase 5).

GATE A -- Both High: "INERTIA GATE: ANCHOR[0A] beats Option A and ANCHOR[0B] beats Option B.
  Teams will not build either option without a forcing function. 'Build neither' is the
  leading recommendation. If proceeding, name the forcing function explicitly."
  The recommendation in Phase 7 must address this gate.

GATE B -- One High: "INERTIA NOTE: ANCHOR[{0A|0B}] beats Option {A|B} but Option {A|B}
  clears the do-nothing bar. Asymmetry may outweigh other dimension signals."

GATE C -- Neither High: "Inertia check passed -- both options beat their ANCHOR baseline."

=== PHASE 7: RECOMMENDATION ===

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
- If GATE A fired: either "build neither" OR name the forcing function that overrides
  the inertia evidence. Reference ANCHOR[0A] and ANCHOR[0B] in the gate language.
- Recommendation traceable to Table 2 (Phase 5) -- do not assert a winner that
  contradicts the matrix signals without explicit justification. If the recommendation
  diverges from the matrix plurality, state the reason explicitly.

=== PHASE 8: ARTIFACT ===

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
  amended: false

=== PHASE 9: AMEND HANDLER ===

Activates when the user says AMEND after the base output.
Three types -- execute the matching protocol:

AMEND TYPE 1 -- Add Option C: {option_c}

1. Define ANCHOR[0C] := {what teams do today instead of building C}.
   Print: "ANCHOR[0C] = {value}. Binding extended."
   Binding rule: all Option C dimensional analysis must reference ANCHOR[0C] by token name.
2. Run Option C through all four dimensions vs ANCHOR[0C]:
   - Feasibility: High / Medium / Low + one reason.
     Register: apply Phase 1 contract [cell emphasis dimension].
   - Inertia (INERTIA RULE): Would teams keep using ANCHOR[0C] instead of building C?
     Name the specific mechanism. Rate: High / Medium / Low.
   - Risk: Primary failure mode. High / Medium / Low.
     Register: apply Phase 1 contract [risk framing dimension].
   - Competitive position: At least one concrete vector vs ANCHOR[0C]. Anti-pattern guard applies.
     Register: apply Phase 1 contract [competitive framing dimension].
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
5. Re-run the INERTIA GATE using ANCHOR token language across all three build options.
6. Revise recommendation: A / B / C / build neither / defer.
   If changed, name what changed and why. Anti-contradiction applies to updated Table 2.
   Register: apply Phase 1 contract [lead structure dimension] to revised recommendation.
7. Update artifact: add anchor_0c, option_c, update recommendation, amended: true.

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

## V-02: self-verify (role sequence axis)

Axis: Role sequence -- V-01 base + Phase 10 structural audit appended after Phase 9. The
model self-checks 9 structural criteria before returning output to the user. Any failed
check triggers a correction before the output is returned.

Hypothesis: Token binding (V-01) prevents Option 0 drift by requiring literal token names.
A self-verification gate catches structural failures that token syntax cannot prevent:
missing TABLE GUIDE, one-sided inertia check, recommendation not traceable to Table 2,
or GATE A firing without "build neither" being named. The terminal audit creates a
closed-loop contract: declare (Phase 0) → use (Phases 3-9) → verify (Phase 10). For
models that follow the prompt structure but skip a structural requirement, the audit
adds a correction opportunity before the artifact is written.

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
  Phase 9 (AMEND handler): revised recommendation framing

exec: business signal leads all register-sensitive phases and dimensions;
  implementation detail omitted; language is investment/risk/market.
  Phase 3 risk: frame as business impact (revenue, partner dependency, market timing).
  Phase 3 competitive: frame as market differentiation, cost-of-delay, switching cost.
  Phase 4/5 cells: lead with business signal. Omit build-level detail.
  Phase 7: recommendation leads; business risk of not acting second; trade-off third.
  Phase 9: same as Phase 7 structure.

engineering: implementation signal leads all register-sensitive phases and dimensions;
  technical risk detail present; language is build/integrate/operate.
  Phase 3 risk: frame as technical failure mode (race condition, schema drift, dependency brittleness).
  Phase 3 competitive: frame as build cost, latency advantage, dependency graph.
  Phase 4/5 cells: lead with technical signal. Include dependency or correctness risk.
  Phase 7: feasibility delta and technical risk lead; recommendation second; trade-off third.
  Phase 9: same as Phase 7 structure.

general (default): neutral -- no routing applied.

Print: "Register: {exec|engineering|general}. Contract: Phase 3 [risk, competitive],
  Phase 4 [cell emphasis], Phase 5 [cell emphasis], Phase 7 [lead structure], Phase 9 [framing]."

=== PHASE 2: CONTEXT ===

Read existing discover artifacts for this topic:
- Glob: simulations/discover/**/{topic}-*-*.md

Print inventory: | skill | date | path | for each file found.
If prior artifacts exist, note any signals that refine the ANCHOR[0A] or ANCHOR[0B]
characterization committed in Phase 0. Do not change committed tokens -- note refinements only.
If none found: "No prior discover artifacts -- proceeding from inputs."

=== PHASE 3: DIMENSION ANALYSIS ===

Run each dimension across both options before moving to the next.
ANCHOR[0A] (Phase 0) is the reference for all Option A inertia and competitive analysis.
ANCHOR[0B] (Phase 0) is the reference for all Option B inertia and competitive analysis.

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

=== PHASE 6: INERTIA GATE ===

Read the Inertia threat cells from Table 2 (Phase 5).

GATE A -- Both High: "INERTIA GATE: ANCHOR[0A] beats Option A and ANCHOR[0B] beats Option B.
  Teams will not build either option without a forcing function. 'Build neither' is the
  leading recommendation. If proceeding, name the forcing function explicitly."
  The recommendation in Phase 7 must address this gate.

GATE B -- One High: "INERTIA NOTE: ANCHOR[{0A|0B}] beats Option {A|B} but Option {A|B}
  clears the do-nothing bar. Asymmetry may outweigh other dimension signals."

GATE C -- Neither High: "Inertia check passed -- both options beat their ANCHOR baseline."

=== PHASE 7: RECOMMENDATION ===

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
- If GATE A fired: either "build neither" OR name the forcing function that overrides
  the inertia evidence. Reference ANCHOR[0A] and ANCHOR[0B] in the gate language.
- Recommendation traceable to Table 2 (Phase 5) -- do not assert a winner that
  contradicts the matrix signals without explicit justification. If the recommendation
  diverges from the matrix plurality, state the reason explicitly.

=== PHASE 8: ARTIFACT ===

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
  amended: false

=== PHASE 9: AMEND HANDLER ===

Activates when the user says AMEND after the base output.
Three types -- execute the matching protocol:

AMEND TYPE 1 -- Add Option C: {option_c}

1. Define ANCHOR[0C] := {what teams do today instead of building C}.
   Print: "ANCHOR[0C] = {value}. Binding extended."
   Binding rule: all Option C dimensional analysis must reference ANCHOR[0C] by token name.
2. Run Option C through all four dimensions vs ANCHOR[0C]:
   - Feasibility: High / Medium / Low + one reason.
     Register: apply Phase 1 contract [cell emphasis dimension].
   - Inertia (INERTIA RULE): Would teams keep using ANCHOR[0C] instead of building C?
     Name the specific mechanism. Rate: High / Medium / Low.
   - Risk: Primary failure mode. High / Medium / Low.
     Register: apply Phase 1 contract [risk framing dimension].
   - Competitive position: At least one concrete vector vs ANCHOR[0C]. Anti-pattern guard applies.
     Register: apply Phase 1 contract [competitive framing dimension].
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
5. Re-run the INERTIA GATE using ANCHOR token language across all three build options.
6. Revise recommendation: A / B / C / build neither / defer.
   If changed, name what changed and why. Anti-contradiction applies to updated Table 2.
   Register: apply Phase 1 contract [lead structure dimension] to revised recommendation.
7. Update artifact: add anchor_0c, option_c, update recommendation, amended: true.

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

=== PHASE 10: STRUCTURAL AUDIT ===

Before returning the output, self-verify each item below.
If any item fails, correct the affected section first, then return the full corrected output.

AUDIT CHECKLIST:
[ ] Phase 0: ANCHOR[0A] and ANCHOR[0B] committed before Phase 1?
    Evidence: "Binding committed." line printed.
[ ] Phase 1: register contract printed with dimension-level phase index?
    Expected pattern: "Phase 3 [risk, competitive], Phase 4 [cell emphasis],
    Phase 5 [cell emphasis], Phase 7 [lead structure], Phase 9 [framing]."
[ ] Phase 3 inertia: both A and B independently checked vs ANCHOR[0A] and ANCHOR[0B]?
    Failure pattern: checking which build option teams prefer instead of vs anchor.
[ ] TABLE GUIDE present before Phase 4? Question-keyed routing to TABLE 1 and TABLE 2?
[ ] Phase 4 header carries "[ -> See Table 2 (Phase 5)... ]"?
[ ] Phase 5 header carries "[ <- Source: Table 1 (Phase 4)... ]"?
[ ] Phase 6 gate: ANCHOR token names used in gate language (not prose "status quo")?
[ ] Phase 7 recommendation: traceable to Table 2 (Phase 5)?
    If recommendation diverges from matrix plurality: reason stated explicitly?
[ ] If GATE A fired in Phase 6: "build neither" named OR forcing function named in Phase 7?

Print: "AUDIT COMPLETE -- {N}/9 checks passed."
If any check failed: print which item failed and the correction applied before the full output.
```

---

## V-03: inline-token-check (phrasing register axis)

Axis: Phrasing register -- V-01 base + TOKEN RECALL header in each phase that uses ANCHOR
tokens (Phases 3, 6, 7). Before producing register-sensitive or anchor-sensitive output,
the model reproduces the committed ANCHOR token values inline. This makes drift detectable
at point-of-use without requiring a terminal audit.

Hypothesis: Token binding (V-01) commits values in Phase 0 and requires downstream literal
reproduction. A model that paraphrases mid-prompt loses the audit trail for that specific
phase. Inline TOKEN RECALL forces the model to write "ANCHOR[0A] = {value}" at the top of
each sensitive phase, which acts as a self-correction opportunity: if the value reproduced
in Phase 3 differs from Phase 6, the drift is visible in the output itself. This is a
different guard than V-02's terminal audit -- inline recall catches drift at the moment of
use, not after all phases have run. For the competitive and inertia dimensions, reproducing
the anchor values in-situ also prevents the model from substituting a generic "current
approach" without triggering an observable token mismatch.

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

Print: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. Binding committed."

=== PHASE 1: AUDIENCE REGISTER ===

Read the audience parameter. This register governs the following phases and dimensions:

  Phase 3 (dimension analysis):
    - Risk sub-section: failure mode framing language
    - Competitive sub-section: differentiation vector framing language
  Phase 4 (three-column matrix): cell content emphasis and vocabulary
  Phase 5 (two-column summary): cell content emphasis and vocabulary
  Phase 7 (recommendation): lead structure and level of detail
  Phase 9 (AMEND handler): revised recommendation framing

exec: business signal leads all register-sensitive phases and dimensions;
  implementation detail omitted; language is investment/risk/market.
  Phase 3 risk: frame as business impact (revenue, partner dependency, market timing).
  Phase 3 competitive: frame as market differentiation, cost-of-delay, switching cost.
  Phase 4/5 cells: lead with business signal. Omit build-level detail.
  Phase 7: recommendation leads; business risk of not acting second; trade-off third.
  Phase 9: same as Phase 7 structure.

engineering: implementation signal leads all register-sensitive phases and dimensions;
  technical risk detail present; language is build/integrate/operate.
  Phase 3 risk: frame as technical failure mode (race condition, schema drift, dependency brittleness).
  Phase 3 competitive: frame as build cost, latency advantage, dependency graph.
  Phase 4/5 cells: lead with technical signal. Include dependency or correctness risk.
  Phase 7: feasibility delta and technical risk lead; recommendation second; trade-off third.
  Phase 9: same as Phase 7 structure.

general (default): neutral -- no routing applied.

Print: "Register: {exec|engineering|general}. Contract: Phase 3 [risk, competitive],
  Phase 4 [cell emphasis], Phase 5 [cell emphasis], Phase 7 [lead structure], Phase 9 [framing]."

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

=== PHASE 6: INERTIA GATE ===

TOKEN RECALL: ANCHOR[0A] = {reproduce committed value from Phase 0}.
              ANCHOR[0B] = {reproduce committed value from Phase 0}.

Read the Inertia threat cells from Table 2 (Phase 5).

GATE A -- Both High: "INERTIA GATE: ANCHOR[0A] beats Option A and ANCHOR[0B] beats Option B.
  Teams will not build either option without a forcing function. 'Build neither' is the
  leading recommendation. If proceeding, name the forcing function explicitly."
  The recommendation in Phase 7 must address this gate.

GATE B -- One High: "INERTIA NOTE: ANCHOR[{0A|0B}] beats Option {A|B} but Option {A|B}
  clears the do-nothing bar. Asymmetry may outweigh other dimension signals."

GATE C -- Neither High: "Inertia check passed -- both options beat their ANCHOR baseline."

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
- If GATE A fired: either "build neither" OR name the forcing function that overrides
  the inertia evidence. Reference ANCHOR[0A] and ANCHOR[0B] in the gate language.
- Recommendation traceable to Table 2 (Phase 5) -- do not assert a winner that
  contradicts the matrix signals without explicit justification. If the recommendation
  diverges from the matrix plurality, state the reason explicitly.

=== PHASE 8: ARTIFACT ===

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
  amended: false

=== PHASE 9: AMEND HANDLER ===

Activates when the user says AMEND after the base output.
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
5. Re-run the INERTIA GATE.
   TOKEN RECALL before gate: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. ANCHOR[0C] = {value}."
   Use ANCHOR token language across all three build options.
6. Revise recommendation: A / B / C / build neither / defer.
   TOKEN RECALL: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. ANCHOR[0C] = {value}."
   If changed, name what changed and why. Anti-contradiction applies to updated Table 2.
   Register: apply Phase 1 contract [lead structure dimension] to revised recommendation.
7. Update artifact: add anchor_0c, option_c, update recommendation, amended: true.

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

## V-04: full-integration (combination axis)

Axis: Combination -- V-01 (token binding) + V-02 (terminal audit) + V-03 (inline recall).
All three R5 mechanisms active simultaneously. Predicted definitive R5 canonical at 100.0.

The combination question: does inline TOKEN RECALL (V-03) and terminal STRUCTURAL AUDIT
(V-02) add independent guard value on top of token binding (V-01)? Or do they produce
redundant overhead? Under the v4 rubric all three mechanisms target drift prevention, not
new criteria. The combination is the safest production form for the discover-compare skill.

Hypothesis: Each mechanism guards a different failure mode. Token binding prevents silent
prose substitution. Inline recall catches drift at point-of-use and forces value
reproduction before the output of each sensitive phase. Terminal audit catches structural
omissions (missing TABLE GUIDE, one-sided inertia, un-named forcing function) that happen
above the token level. Together they form three non-overlapping guards across the full
lifecycle. 100.0 on v4 rubric; stronger real-world behavior than V-04/R4.

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
  Phase 9 (AMEND handler): revised recommendation framing

exec: business signal leads all register-sensitive phases and dimensions;
  implementation detail omitted; language is investment/risk/market.
  Phase 3 risk: frame as business impact (revenue, partner dependency, market timing).
  Phase 3 competitive: frame as market differentiation, cost-of-delay, switching cost.
  Phase 4/5 cells: lead with business signal. Omit build-level detail.
  Phase 7: recommendation leads; business risk of not acting second; trade-off third.
  Phase 9: same as Phase 7 structure.

engineering: implementation signal leads all register-sensitive phases and dimensions;
  technical risk detail present; language is build/integrate/operate.
  Phase 3 risk: frame as technical failure mode (race condition, schema drift, dependency brittleness).
  Phase 3 competitive: frame as build cost, latency advantage, dependency graph.
  Phase 4/5 cells: lead with technical signal. Include dependency or correctness risk.
  Phase 7: feasibility delta and technical risk lead; recommendation second; trade-off third.
  Phase 9: same as Phase 7 structure.

general (default): neutral -- no routing applied.

Print: "Register: {exec|engineering|general}. Contract: Phase 3 [risk, competitive],
  Phase 4 [cell emphasis], Phase 5 [cell emphasis], Phase 7 [lead structure], Phase 9 [framing]."

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

=== PHASE 6: INERTIA GATE ===

TOKEN RECALL: ANCHOR[0A] = {reproduce committed value from Phase 0}.
              ANCHOR[0B] = {reproduce committed value from Phase 0}.

Read the Inertia threat cells from Table 2 (Phase 5).

GATE A -- Both High: "INERTIA GATE: ANCHOR[0A] beats Option A and ANCHOR[0B] beats Option B.
  Teams will not build either option without a forcing function. 'Build neither' is the
  leading recommendation. If proceeding, name the forcing function explicitly."
  The recommendation in Phase 7 must address this gate.

GATE B -- One High: "INERTIA NOTE: ANCHOR[{0A|0B}] beats Option {A|B} but Option {A|B}
  clears the do-nothing bar. Asymmetry may outweigh other dimension signals."

GATE C -- Neither High: "Inertia check passed -- both options beat their ANCHOR baseline."

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
- If GATE A fired: either "build neither" OR name the forcing function that overrides
  the inertia evidence. Reference ANCHOR[0A] and ANCHOR[0B] in the gate language.
- Recommendation traceable to Table 2 (Phase 5) -- do not assert a winner that
  contradicts the matrix signals without explicit justification. If the recommendation
  diverges from the matrix plurality, state the reason explicitly.

=== PHASE 8: ARTIFACT ===

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
  amended: false

=== PHASE 9: AMEND HANDLER ===

Activates when the user says AMEND after the base output.
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
5. Re-run the INERTIA GATE.
   TOKEN RECALL: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. ANCHOR[0C] = {value}."
   Use ANCHOR token language across all three build options.
6. Revise recommendation: A / B / C / build neither / defer.
   TOKEN RECALL: "ANCHOR[0A] = {value}. ANCHOR[0B] = {value}. ANCHOR[0C] = {value}."
   If changed, name what changed and why. Anti-contradiction applies to updated Table 2.
   Register: apply Phase 1 contract [lead structure dimension] to revised recommendation.
7. Update artifact: add anchor_0c, option_c, update recommendation, amended: true.

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

=== PHASE 10: STRUCTURAL AUDIT ===

Before returning the output, self-verify each item below.
If any item fails, correct the affected section first, then return the full corrected output.

AUDIT CHECKLIST:
[ ] Phase 0: ANCHOR[0A] and ANCHOR[0B] committed before Phase 1?
    Evidence: "Binding committed." line printed.
[ ] Phase 1: register contract printed with dimension-level phase index?
    Expected pattern: "Phase 3 [risk, competitive], Phase 4 [cell emphasis],
    Phase 5 [cell emphasis], Phase 7 [lead structure], Phase 9 [framing]."
[ ] Phase 3 TOKEN RECALL: token values reproduced at top of Phase 3?
[ ] Phase 3 inertia: both A and B independently checked vs ANCHOR[0A] and ANCHOR[0B]?
    Failure pattern: checking which build option teams prefer instead of vs anchor.
[ ] TABLE GUIDE present before Phase 4? Question-keyed routing to TABLE 1 and TABLE 2?
[ ] Phase 4 header carries "[ -> See Table 2 (Phase 5)... ]"?
[ ] Phase 5 header carries "[ <- Source: Table 1 (Phase 4)... ]"?
[ ] Phase 6 TOKEN RECALL reproduced correctly? Gate language uses ANCHOR token names?
[ ] Phase 7 TOKEN RECALL reproduced correctly? Recommendation traceable to Table 2?
    If recommendation diverges from matrix plurality: reason stated explicitly?
[ ] If GATE A fired in Phase 6: "build neither" named OR forcing function named in Phase 7?

Print: "AUDIT COMPLETE -- {N}/10 checks passed."
If any check failed: print which item failed and the correction applied before the full output.
```

---

## V-05: lean-anchor (lifecycle emphasis axis)

Axis: Lifecycle emphasis -- V-05/R4 (6-phase lean, no AMEND/register) with ANCHOR[0A]/
ANCHOR[0B] token binding added. Tests token grounding in the minimal form. Score stays
at 95.0 (C-09/C-10/C-14/C-15/C-16 remain 0 by design); drift resistance is hardened.

Hypothesis: V-05/R4 passes C-18 (dedicated Phase 0 anchor) but uses prose downstream.
Any model run on the lean form that paraphrases "the current approach" in the inertia
or gate phase loses the inertia contract silently. ANCHOR tokens added to the lean form
make drift detectable without adding AMEND or audience register complexity. The lean
floor stays at 95.0 under v4 rubric; a v6 criterion testing token presence in 3+
downstream phases would differentiate lean-anchor from lean-prose.

```
You are running /discover-compare for topic: {topic}.
Comparing: Option A -- {option_a} vs Option B -- {option_b}.

=== PHASE 0: STATUS QUO ANCHOR (Option 0) ===

Before any analysis, name the behavior teams fall back on today if neither option is built.

ANCHOR[0A] := {what teams do today instead of building Option A}
ANCHOR[0B] := {what teams do today instead of building Option B}

Binding rule: all inertia analysis, competitive analysis, gate logic, and recommendation
must reference ANCHOR[0A] and ANCHOR[0B] by token name -- not by prose paraphrase.

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
ANCHOR[0A] is the reference for all Option A inertia and competitive analysis.
ANCHOR[0B] is the reference for all Option B inertia and competitive analysis.

--- Feasibility ---
Option A: High / Medium / Low. One reason.
Option B: High / Medium / Low. One reason.

--- Inertia ---
INERTIA RULE: Inertia is checked for BOTH options independently.
The question for each option: would teams keep using the ANCHOR token INSTEAD OF building it?
Option A: would teams keep using ANCHOR[0A] instead of building Option A?
  Name the specific mechanism. Threat rating: High / Medium / Low.
Option B: would teams keep using ANCHOR[0B] instead of building Option B?
  Name the specific mechanism. Threat rating: High / Medium / Low.

--- Risk ---
Option A: Primary failure mode. Rating: High / Medium / Low.
Option B: Same.
Option 0 continuation risk: What is the long-term cost of staying with ANCHOR[0A] and ANCHOR[0B]?
  One sentence -- enters the 3-column matrix.

--- Competitive Position ---
ANTI-PATTERN GUARD: Generic competitive analysis uses phrases such as "more competitive,"
"better positioned," or "stronger in the market" without specifying the mechanism.
Such phrasing is insufficient and will fail this criterion. Name the concrete vector:
  Speed: throughput, latency, or iteration rate advantage
  Cost: build, operating, or switching cost difference
  Ecosystem: integration depth, lock-in reduction, or partner leverage
  Capability: what ANCHOR[0A] / ANCHOR[0B] cannot do that this option enables

Option A: At least one concrete vector vs ANCHOR[0A].
Option B: Same requirement vs ANCHOR[0B].
Option 0 competitive position: What do ANCHOR[0A] and ANCHOR[0B] offer today
  that Option A and Option B do not yet match?

=== PHASE 3: MATRICES ===

Which question are you answering?
  Does either option beat doing nothing (ANCHOR[0A] / ANCHOR[0B])? -> TABLE 1 (below)
  Which option should we build?                                      -> TABLE 2 (below)

--- Table 1 of 2: Status-Quo Context View ---
[ -> See Table 2 below for A-vs-B decision summary. ]

| Dimension              | Option A: {option_a} | Option B: {option_b} | Option 0: ANCHOR[0A] / ANCHOR[0B] |
|------------------------|----------------------|----------------------|-----------------------------------|
| Feasibility            |                      |                      | N/A (no build required)           |
| Inertia threat         | [vs ANCHOR[0A]]      | [vs ANCHOR[0B]]      | N/A (this IS the anchor)          |
| Risk                   |                      |                      | Continuation risk: ...            |
| Competitive position   |                      |                      | ANCHOR advantage: ...             |

--- Table 2 of 2: A-vs-B Decision Summary ---
[ <- Source: Table 1 above; Option 0 column excluded. Use this table to reach the recommendation. ]

A reader should reach the recommendation from Table 2 without re-reading Phase 2.

| Dimension              | Option A | Option B |
|------------------------|----------|----------|
| Feasibility            |          |          |
| Inertia threat         |          |          |
| Risk                   |          |          |
| Competitive position   |          |          |

Format: Rating + one-phrase signal. No empty cells.

=== PHASE 4: INERTIA GATE ===

Read the Inertia threat cells from Table 2.

GATE A -- Both High: "INERTIA GATE: ANCHOR[0A] beats Option A and ANCHOR[0B] beats Option B.
  Teams will not build either option without a forcing function. 'Build neither' is the
  leading recommendation. If proceeding, name the forcing function explicitly."

GATE B -- One High: "INERTIA NOTE: ANCHOR[{0A|0B}] beats Option {A|B} but Option {A|B}
  clears the do-nothing bar. Asymmetry may outweigh other dimension signals."

GATE C -- Neither High: "Inertia check passed -- both options beat their ANCHOR baseline."

=== PHASE 5: RECOMMENDATION ===

State: choose Option A / choose Option B / build neither / defer.

Recommendation, primary reason, trade-off (what is given up by not choosing the other
option) in one paragraph.

- If GATE A fired: either "build neither" OR name the forcing function that overrides
  the inertia evidence. Reference ANCHOR[0A] and ANCHOR[0B] in the gate language.
- Recommendation traceable to Table 2 -- do not assert a winner that contradicts the
  matrix signals without explicit justification. If the recommendation diverges from
  the matrix plurality, state the reason explicitly.

=== PHASE 6: ARTIFACT ===

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
  amended: false
```
