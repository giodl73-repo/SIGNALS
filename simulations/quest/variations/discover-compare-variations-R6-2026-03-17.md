Written to `simulations/quest/variations/discover-compare-variations-R6-2026-03-17.md`.

---

## Round 6 — 5 Variations

| # | Label | Axis | Key change from V-04/R5 |
|---|-------|------|------------------------|
| V-01 | **recall-full-coverage** | Lifecycle emphasis | TOKEN RECALL added at Phase 4 + Phase 5 (missing register-sensitive phases); Phase 10 audit bumps to 12 items |
| V-02 | **pre-artifact-gate** | Role sequence | Audit promoted to Phase 8 (between recommendation and artifact write); artifact is Phase 9; AMEND is Phase 10 |
| V-03 | **bilateral-verdict** | Inertia framing | Phase 6 becomes "OPTION 0 VERDICT AND GATE" — explicit VERDICT A / VERDICT B before gate fires; V-01 recall coverage included |
| V-04 | **r6-canonical** | Combination | V-01 + V-02 + V-03: full recall + pre-artifact gate + bilateral verdict; 13-item pre-artifact audit |
| V-05 | **lean-c20c21** | Lifecycle emphasis (lean) | V-05/R5 lean + TOKEN RECALL at anchor phases (2, 4) + pre-recommendation 5-item audit |

**The R6 gap being closed:** C-20 requires TOKEN RECALL "at every phase scored under C-15 (all register-sensitive phases)" = Phases 3, 4, 5, 7, 9. V-04/R5 covers Phases 3 and 7 (register-sensitive) plus Phase 6 (anchor-sensitive but not register-sensitive). Phases 4, 5, and 9 were missing. V-01 adds them.

**Predicted scores (v5 rubric):**
- V-01/V-02/V-03/V-04: **100.0** (C-19 PASS, C-20 PASS, C-21 PASS → 13/13 aspirational)
- V-05: **~95.0** (C-20 PARTIAL — TOKEN RECALL at anchor phases but no register-sensitive phases; 6.5/13 aspirational)

**Key architectural differences:**
- V-02's pre-artifact gate is the strongest C-21 form: corrections happen before the file exists, not after it's already written
- V-03's bilateral verdict makes C-02 compliance an observable output trace, not just a structural guarantee
- V-04 combines all three — the R6 canonical
se 7 and Phase 8, gating the artifact write. If Phase 10 in V-04/R5 fires "before the artifact is returned to the user" (valid for C-21), then Phase 8 in V-02 fires "before the artifact is written to disk" — architecturally stronger and eliminates the need to rewrite the artifact on correction.

**V-03** tests inertia-framing depth: separating bilateral verdicts (VERDICT A / VERDICT B) from gate logic creates an observable anchor-grounded trace for each option independently. The gate reads from the verdicts, not from raw inertia ratings.

**V-04** is the definitive combination: full recall + pre-artifact gate + bilateral verdict. Three-layer drift defense preserved; architecturally stronger than V-04/R5 on C-20 and C-21.

**V-05** tests lean ceiling under v5: C-20 is PARTIAL (TOKEN RECALL at anchor phases but C-15 not achievable without register), C-21 PASS (audit fires pre-recommendation), C-19 PASS. Predicts ~95.4 (aspirational ≈ 6.5/13).

---

## V-01: recall-full-coverage (lifecycle emphasis axis)

Axis: Lifecycle emphasis -- V-04/R5 + TOKEN RECALL at Phase 4 (THREE-COLUMN MATRIX) and
Phase 5 (TWO-COLUMN SUMMARY) -- the two register-sensitive phases V-04/R5 missed. Phase 9
(AMEND handler) also gets a top-level TOKEN RECALL before any AMEND sub-type runs. Phase 10
audit gains two new items for Phase 4 and Phase 5 TOKEN RECALL verification (N=12).

Hypothesis: V-04/R5 has TOKEN RECALL at Phases 3, 6, 7. C-20 pass condition requires TOKEN
RECALL "at every phase scored under C-15 (all register-sensitive phases)" = Phases 3, 4, 5, 7,
9. V-04/R5 covers 3 and 7 (register-sensitive) and 6 (anchor-sensitive but not register-
sensitive). Missing: Phase 4, Phase 5, Phase 9. Adding those three phases achieves full C-20
coverage (5/5 register-sensitive phases). No other criteria regress. Predicted 100.0.

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
[ ] Phase 4 TOKEN RECALL: token values reproduced at top of Phase 4 (NEW)?
[ ] TABLE GUIDE present before Phase 4? Question-keyed routing to TABLE 1 and TABLE 2?
[ ] Phase 4 header carries "[ -> See Table 2 (Phase 5)... ]"?
[ ] Phase 5 TOKEN RECALL: token values reproduced at top of Phase 5 (NEW)?
[ ] Phase 5 header carries "[ <- Source: Table 1 (Phase 4)... ]"?
[ ] Phase 6 TOKEN RECALL reproduced correctly? Gate language uses ANCHOR token names?
[ ] Phase 7 TOKEN RECALL reproduced correctly? Recommendation traceable to Table 2?
    If recommendation diverges from matrix plurality: reason stated explicitly?
[ ] If GATE A fired in Phase 6: "build neither" named OR forcing function named in Phase 7?

Print: "AUDIT COMPLETE -- {N}/12 checks passed."
If any check failed: print which item failed and the correction applied before the full output.
```

---

## V-02: pre-artifact-gate (role sequence axis)

Axis: Role sequence -- structural audit promoted from Phase 10 to Phase 8, placing it between
the recommendation (Phase 7) and the artifact write (Phase 9). The audit becomes a pre-write
gate: if any item fails, the correction happens before the artifact file is created. AMEND
moves to Phase 10. TOKEN RECALL coverage matches V-04/R5 (Phases 3, 6, 7 only) to isolate the
position-change effect cleanly. The 10-item checklist is unchanged from V-04/R5.

Hypothesis: C-21 pass condition says "before the final artifact is returned." V-04/R5 interprets
this as "before the full output is returned to the user" (Phase 10 fires in the same output
batch). V-02 interprets it as "before the artifact is written to disk" (Phase 8 fires before
Phase 9 writes the file). The architectural difference: in V-04/R5, a correction in Phase 10
must also rewrite the already-completed artifact frontmatter. In V-02, no file exists yet when
the audit runs -- corrections are cleaner and the artifact always reflects the corrected state.
No criteria regress. Predicted 100.0.

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
[ ] TABLE GUIDE present before Phase 4? Question-keyed routing to TABLE 1 and TABLE 2?
[ ] Phase 4 header carries "[ -> See Table 2 (Phase 5)... ]"?
[ ] Phase 5 header carries "[ <- Source: Table 1 (Phase 4)... ]"?
[ ] Phase 6 TOKEN RECALL reproduced correctly? Gate language uses ANCHOR token names?
[ ] Phase 7 TOKEN RECALL reproduced correctly? Recommendation traceable to Table 2?
    If recommendation diverges from matrix plurality: reason stated explicitly?
[ ] If GATE A fired in Phase 6: "build neither" named OR forcing function named in Phase 7?

Print: "PRE-ARTIFACT AUDIT -- {N}/10 checks passed. Proceeding to artifact write."
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
  amended: false

=== PHASE 10: AMEND HANDLER ===

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
```

---

## V-03: bilateral-verdict (inertia framing axis)

Axis: Inertia framing -- Phase 6 becomes "OPTION 0 VERDICT AND GATE." Instead of reading
inertia threat cells from Table 2 and firing a gate, the phase first issues two explicit
per-option verdicts grounded by ANCHOR token names, then derives the gate from those verdicts.
Also includes V-01's full TOKEN RECALL coverage (Phases 3, 4, 5, 7, 9). The verdict structure
forces bilateral independence to be observable in the output itself.

Hypothesis: V-04/R5 passes C-02 (bilateral inertia check) via the INERTIA RULE in Phase 3 and
gate language in Phase 6 that uses both ANCHOR tokens. But the bilateral check in Phase 6 is
implicit -- the gate fires on both-high, one-high, or neither, reading composite ratings from
Table 2 rather than issuing independent verdicts. The bilateral-verdict framing requires the
model to produce two separate verdict sentences before the gate fires: "VERDICT A: teams would
[not] build Option A over ANCHOR[0A] because..." and "VERDICT B: same for B." This makes the
bilateral independence explicit in the output trace. The gate then reads from verdicts, not from
raw ratings. Strongest observable form of C-02. Predicted 100.0.

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
  "INERTIA GATE: ANCHOR[0A] beats Option A. ANCHOR[0B] beats Option B. Teams will not build
  either option without a forcing function. 'Build neither' is the leading recommendation.
  If proceeding, name the forcing function explicitly."
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
  verdict_a: build|inertia
  verdict_b: build|inertia
  amended: false

=== PHASE 9: AMEND HANDLER ===

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
[ ] Phase 4 TOKEN RECALL: token values reproduced at top of Phase 4?
[ ] TABLE GUIDE present before Phase 4? Question-keyed routing to TABLE 1 and TABLE 2?
[ ] Phase 4 header carries "[ -> See Table 2 (Phase 5)... ]"?
[ ] Phase 5 TOKEN RECALL: token values reproduced at top of Phase 5?
[ ] Phase 5 header carries "[ <- Source: Table 1 (Phase 4)... ]"?
[ ] Phase 6 VERDICT A and VERDICT B both present and independently grounded?
    Failure pattern: VERDICT A references Option B or VERDICT B references Option A.
[ ] Phase 6 TOKEN RECALL reproduced correctly? Gate language uses ANCHOR token names?
[ ] Phase 7 TOKEN RECALL reproduced correctly? Recommendation traceable to Table 2?
    If recommendation diverges from matrix plurality: reason stated explicitly?
[ ] If GATE A fired in Phase 6: "build neither" named OR forcing function named in Phase 7?

Print: "AUDIT COMPLETE -- {N}/13 checks passed."
If any check failed: print which item failed and the correction applied before the full output.
```

---

## V-04: r6-canonical (combination axis)

Axis: Combination -- V-01 (full TOKEN RECALL coverage at all 5 register-sensitive phases) +
V-02 (pre-artifact gate at Phase 8) + V-03 (bilateral verdict structure in Phase 6). Phase 10
becomes AMEND handler. Audit fires as Phase 8 (pre-artifact gate) with 12 items: the 10 from
V-04/R5 + Phase 4 TOKEN RECALL + Phase 5 TOKEN RECALL. Verdict A / Verdict B structure in
Phase 6 replaces the direct GATE read.

Hypothesis: Three R6 mechanisms are independent and non-overlapping. Full recall (V-01) closes
the C-20 gap. Pre-artifact gate (V-02) creates the strongest architecturally clean C-21 form.
Bilateral verdict (V-03) creates the strongest observable C-02 trace. All three together: C-20
PASS (5/5 recall phases), C-21 PASS (pre-write gate with correction), C-02 PASS (explicit per-
option verdicts). Three-layer drift defense from V-04/R5 preserved: token binding + inline recall
+ terminal audit. No criteria regress. Predicted 100.0 at 13/13 aspirational.

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
[ ] Phase 6 TOKEN RECALL reproduced correctly? Gate language uses ANCHOR token names?
[ ] Phase 7 TOKEN RECALL reproduced correctly? Recommendation traceable to Table 2?
    If recommendation diverges from matrix plurality: reason stated explicitly?
[ ] If GATE A fired in Phase 6: "build neither" named OR forcing function named in Phase 7?

Print: "PRE-ARTIFACT AUDIT -- {N}/13 checks passed. Proceeding to artifact write."
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

## V-05: lean-c20c21 (lifecycle emphasis lean axis)

Axis: Lifecycle emphasis (lean) -- V-05/R5 lean (no AMEND/register) + TOKEN RECALL at the two
anchor-sensitive lean phases (Phase 2 inertia sub-section, Phase 4 verdict-and-gate) + new Phase
5 pre-recommendation audit (5-item lean checklist). Tests whether the lean form can add C-21
(terminal audit) without adding register contract (C-15/C-16). C-20 is PARTIAL by design: TOKEN
RECALL appears at anchor-sensitive phases (2 and 4) but C-15 is not achievable without register.

Hypothesis: V-05/R5 scores C-19 PASS (binding rule in Phase 0). Adding TOKEN RECALL at Phases 2
and 4 adds visible anchor grounding at the lean form's two most drift-prone phases (inertia
analysis and gate/verdict). C-20 scores PARTIAL (TOKEN RECALL at anchor-sensitive phases, but
no register-sensitive phases exist to satisfy the C-15 scope). Adding Phase 5 pre-recommendation
audit scores C-21 PASS (5-item checklist fires before recommendation and artifact). Net change
vs V-05/R5: aspirational goes from 5/13 to approximately 6.5/13 (adding C-20=0.5, C-21=1).
Predicted: 60 + 30 + (6.5/13)*10 = 95.0. Lean floor stable.

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

These verdicts are independent. VERDICT A does not reference Option B. VERDICT B does not
reference Option A.

If VERDICT A = High AND VERDICT B = High:
  "INERTIA GATE: ANCHOR[0A] beats Option A. ANCHOR[0B] beats Option B.
  'Build neither' is the leading recommendation."

If exactly one verdict = High:
  "INERTIA NOTE: ANCHOR[{0A|0B}] beats Option {A|B}. Asymmetry may outweigh other signals."

If neither verdict = High:
  "Inertia check passed -- both options beat their ANCHOR baselines."

=== PHASE 5: STRUCTURAL AUDIT (pre-recommendation gate) ===

Before writing the recommendation and artifact, self-verify each item below.
If any item fails, correct the affected section NOW before proceeding to Phase 6.

AUDIT CHECKLIST:
[ ] Phase 0: ANCHOR[0A] and ANCHOR[0B] committed before Phase 1?
    Evidence: "Binding committed." line printed.
[ ] Phase 2 inertia: both A and B independently checked vs ANCHOR[0A] and ANCHOR[0B]?
    Failure pattern: checking which option teams prefer instead of each vs its anchor.
[ ] Table 1 and Table 2 present? Table 1 has Option 0 column? Table 2 excludes Option 0?
    Cross-reference arrows present on both table headers?
[ ] Phase 4 VERDICT A and VERDICT B both present and independently grounded?
    Phase 4 TOKEN RECALL reproduced? Gate language uses ANCHOR token names?
[ ] If GATE fired (both verdicts High): "build neither" named in Phase 6 recommendation?

Print: "PRE-RECOMMENDATION AUDIT -- {N}/5 checks passed."
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
