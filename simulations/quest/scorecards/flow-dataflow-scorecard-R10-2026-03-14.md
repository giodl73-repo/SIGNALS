# flow-dataflow — Round 10 Scorecard

## Scoring Framework

| Tier | Weight | Criteria | Pts each |
|------|--------|----------|----------|
| Essential | 60 pts | C-01..C-04 | 15.00 |
| Recommended | 30 pts | C-05..C-07 | 10.00 |
| Aspirational | 10 pts | C-08..C-35 (28 total) | 0.357 |

PASS = full | PARTIAL = half | FAIL = 0

---

## Per-Variation Rubric Evaluation

### V-01 — Lifecycle emphasis (Finance → Operations → Commerce, natural order)

| ID | Criterion | V-01 | Evidence |
|----|-----------|------|----------|
| C-01 | Data lineage chain | PASS | Stage traces [A-03][A-06][A-09] cover source→stage→destination for all entities |
| C-02 | Boundary error handling | PASS | `Error Handling` column required; `no handling — see [A-12]` or named mechanism; silence fails |
| C-03 | Data loss point identification | PASS | `Data Loss Flag` column required in all boundary blocks and stage tables; generic language fails |
| C-04 | Schema state at each stage | PASS | SC-7 requires `Schema In | Schema Out` in stage tables; `Schema Delta` column in boundary blocks |
| C-05 | Latency characterization | PASS | SC-7 requires explicit `Stage Latency` column; SC-3 requires cumulative `Elapsed (cumul.)` |
| C-06 | Stale data windows | PASS | [A-11] STALE ANALYSIS mandated with normal-operation and failure-mode rows |
| C-07 | Domain framing | PASS | `Entity` column requires named entity from [A-01]; entity vocab in DOMAIN CONTEXT |
| C-08 | Recovery prescriptions | PASS | [A-12] requires named recovery per loss point and `no handling` flag; formula enforced |
| C-09 | Pattern trade-off analysis | PASS | SC-8: [A-14] required named section, ≥1 alternative, ≥2 dimensions |
| C-10 | Pre-trace domain context gate | PASS | [A-01] DOMAIN CONTEXT written before Stage 1; entity terms reappear in boundary Entity columns |
| C-11 | Interleaved boundary gates | PASS | SC-2: Stage N+1 blocked until boundary block complete; one block per stage pair per role |
| C-12 | Domain entity exposure per boundary | PASS | `Entity` column: named entity from [A-01]; "data" or "records" alone fails |
| C-13 | Pre-declared staleness contract | PASS | SC-5: Finance appends immutability statement to [A-01]; SLA declared as integer with unit before Stage 1 |
| C-14 | Additive elapsed time calculation | PASS | SC-3: `Elapsed (cumul.)` computed inside each block; [A-11] uses final cumulative value |
| C-15 | Incumbent or manual-process baseline | PASS | [A-02] names ≥3 steps with durations; SC-8 requires [A-14] to cite [A-02]; [A-12] formula cites [A-02] |
| C-16 | Cross-role reference chain | PASS | SC-1: Operations cites [A-01][A-02][A-04]; Commerce cites [A-01][A-02][A-04][A-07] by token |
| C-17 | Immutability declaration | PASS | SC-5: verbatim "This threshold is fixed. No subsequent role may revise it after Stage 1 is written." |
| C-18 | Incremental boundary elapsed | PASS | SC-3: elapsed computed inside each block; deferred totals fail |
| C-19 | Machine-verifiable citation convention | PASS | `[A-xx]` convention declared in ARTIFACT REGISTRY; uniform throughout; no ad-hoc labels |
| C-20 | Stage-write progression gate | PASS | SC-2: explicit write-order prohibition by name; gate condition stated |
| C-21 | Binary freshness verdict per boundary | PASS | SC-4: `Verdict` = FRESH or STALE from [A-01] threshold; required at every block |
| C-22 | Formal pre-declared registry table | PASS | ARTIFACT REGISTRY table: all 14 artifacts with token, owner, description before any role |
| C-23 | Phase gate self-verification checklists | PASS | [A-05][A-08] are tick checklists with named criterion identifiers; SC-9 explicitly checked |
| C-24 | Upfront constraint section with inline callbacks | PASS | SC-1..SC-10 upfront; "[Apply SC-x]" callbacks at every enforcement point |
| C-25 | Phase gate artifacts as first-class registry rows | PASS | [A-05] and [A-08] appear as named rows in ARTIFACT REGISTRY with token, owner, description |
| C-26 | Non-natural role ordering | **FAIL** | Finance → Operations → Commerce is the natural upstream-to-downstream order; citation laziness is not detectable |
| C-27 | Named recovery formula anchoring incumbent baseline | PASS | `Fall back to [A-02] if [condition]` as required formula in [A-12] role instructions |
| C-28 | Named-column boundary block schema | PASS | BOUNDARY BLOCK SCHEMA section: 7 named columns declared as table |
| C-29 | Trade-off as prompt-required section | PASS | SC-8 explicitly mandates [A-14] as "structurally required named section" with [A-02] token |
| C-30 | Output register declaration with field-compliance markers | PASS | REGISTER DECLARATION: tabular register named; per-field compliance markers table present |
| C-31 | Pre-declared boundary block schema section | PASS | BOUNDARY BLOCK SCHEMA is a standalone section before roles; all columns listed |
| C-32 | Register-specific compliance marker mapping | PASS | REGISTER DECLARATION maps each field to exact column header and disqualifying forms |
| C-33 | Register-invariant declaration | PASS | Exempt (tabular-only variation) |
| C-34 | Per-boundary incumbent equivalent column | PASS | BOUNDARY BLOCK SCHEMA col 7: `Incumbent Equiv.`, cell form `[A-02]: [step + duration]`; SC-9 enforces; bare duration fails |
| C-35 | INCUMBENT TOTAL as pre-trade-off artifact | PASS | [A-13] in registry; SC-10 requires before [A-14]; role-breakdown table template; SC-8 requires [A-14] to cite [A-13] |

**V-01 Score: 60 + 30 + (27/28 × 10) = 99.6**

---

### V-02 — Output format (REGISTER DECLARATION as primary C-34/C-35 vehicle, natural order)

Differs from V-01 only in how C-34/C-35 compliance is specified — via REGISTER DECLARATION Part A/Part B as the authoritative source, with SC-9/SC-10 as callbacks rather than primary declarations. Role order unchanged (Finance → Operations → Commerce).

| ID | Criterion | V-02 | Evidence |
|----|-----------|------|----------|
| C-01..C-25 | (All structural criteria) | All PASS | Same pattern as V-01; REGISTER DECLARATION strengthens per-field specificity without changing pass conditions |
| C-26 | Non-natural role ordering | **FAIL** | Natural Finance → Operations → Commerce; same fail as V-01 |
| C-27..C-33 | (All remaining) | All PASS | — |
| C-34 | Per-boundary incumbent equivalent | PASS | Part A: `Incumbent equivalent` row with cell form `[A-02]: [named step + duration]`; disqualifying form explicit; BOUNDARY BLOCK SCHEMA col header must match Part A spellings exactly. Single-location authoritative reference. |
| C-35 | INCUMBENT TOTAL as pre-trade-off artifact | PASS | Part B: `### [A-13] INCUMBENT TOTAL` with table schema, role rows, Grand Total, all-numeric requirement. Trade-off section: must include all three tokens. SC-10 callbacks to Part B. Evaluator can verify C-35 from Part B alone. |

**V-02 Score: 60 + 30 + (27/28 × 10) = 99.6**

*V-02's Part B is the strongest single-location verification structure for C-35 across all R10 variations — but no higher score because C-35 is binary and V-01 also passes.*

---

### V-03 — Inertia framing (Operations → Finance → Commerce; baseline first)

| ID | Criterion | V-03 | Evidence |
|----|-----------|------|----------|
| C-01..C-04 | Essential | All PASS | Stage traces for three roles, schema columns, loss flags, error handling |
| C-05..C-07 | Recommended | All PASS | Stage Latency, STALE ANALYSIS, domain entity vocabulary |
| C-08 | Recovery prescriptions | PASS | [A-12] formula: `Fall back to [A-01] if [condition]`; [A-01] is INCUMBENT BASELINE |
| C-09 | Trade-off analysis | PASS | SC-8 and [A-14] registry row |
| C-10 | Pre-trace domain context gate | PASS | [A-02] DOMAIN CONTEXT written before Stage 1 (after [A-01]); "reuse ≥2 entity names from [A-01]"; entity column enforces reuse |
| C-11..C-14 | Boundary gates, elapsed | PASS | Same structural enforcement as V-01 |
| C-15 | Incumbent baseline | PASS | [A-01] INCUMBENT BASELINE produced first; cited in [A-12] formula and SC-8 requires [A-14] cites [A-01] |
| C-16 | Cross-role reference chain | PASS | SC-1: Finance cites [A-01][A-02][A-04]; Commerce cites [A-01][A-02][A-04][A-07]; all named by token |
| C-17..C-25 | (Remaining structural) | All PASS | SC-5 immutability, registry, phase gates, SC-x callbacks |
| C-26 | Non-natural role ordering | PASS | Operations → Finance → Commerce is non-natural; Commerce must cite [A-04] (Operations, Role 1) — two roles prior, not immediate predecessor Finance. SC-1 explicitly requires [A-04] in Commerce's Citing line |
| C-27 | Named recovery formula | PASS | `Fall back to [A-01] if [condition]` required structure |
| C-28..C-33 | Format and register | All PASS | BOUNDARY BLOCK SCHEMA standalone; REGISTER DECLARATION with field mapping; tabular-only exempt from C-33 |
| C-34 | Per-boundary incumbent equivalent | PASS | BOUNDARY BLOCK SCHEMA col 7: `Incumbent Equiv.` = `[A-01]: [named step + duration]`; SC-9 enforces; baseline [A-01] is the first artifact produced — no forward-citation required |
| C-35 | INCUMBENT TOTAL | PASS | [A-13] registered; SC-10 + role instruction; table template with Operations/Finance/Commerce/Grand Total rows; [A-14] cites [A-13] per SC-8 |

**V-03 Score: 60 + 30 + 10 = 100.0**

*Differentiator: C-34 is maximally simple — [A-01] is visible since line 1, so every Incumbent Equiv. cell cites a fully-produced artifact. No forward-citation complexity.*

---

### V-04 — Commerce → Operations → Finance (maximum non-natural + forward-citation stress)

| ID | Criterion | V-04 | Evidence |
|----|-----------|------|----------|
| C-01..C-04 | Essential | All PASS | Stages 1–7 across three roles; schema, loss, error handling enforced |
| C-05..C-07 | Recommended | All PASS | Stage Latency, STALE ANALYSIS, domain vocabulary |
| C-08 | Recovery prescriptions | PASS | [A-12] formula: `Fall back to [A-02] if [condition]`; Finance produces [A-12] after writing [A-02] — no ambiguity |
| C-09..C-14 | (Standard structural) | All PASS | SC-2 through SC-4; SC-7; [A-11] stale analysis |
| C-15 | Incumbent baseline | PASS | [A-02] produced by Finance (last); cited in [A-12] and SC-8 requires [A-14] cites [A-02] |
| C-16 | Cross-role reference chain | PASS | SC-1: Operations cites [A-01][A-04]; Finance must cite [A-01][A-04][A-07] — all three required. Finance citing [A-01] (Commerce, two roles prior) is explicitly mandated |
| C-17..C-25 | (Remaining structural) | All PASS | SC-5 (Commerce appends immutability to [A-01]); phase gates; SC-x callbacks |
| C-26 | Non-natural role ordering | PASS | Commerce → Operations → Finance is the maximally non-natural order. Finance must cite [A-01][A-04] from Commerce (two roles prior). SC-1 makes this a named-token requirement, not an inference |
| C-27..C-33 | Format and register | All PASS | Same BOUNDARY BLOCK SCHEMA, REGISTER DECLARATION, tabular-only C-33 exempt |
| C-34 | Per-boundary incumbent equivalent | PASS | BOUNDARY BLOCK SCHEMA col 7 explicitly names the forward-citation protocol: "Commerce and Operations: cite [A-02] as a forward reference; use domain knowledge of the manual retail process." SC-9: "`[A-02]` token required regardless of whether Finance has produced [A-02] yet." Bare duration is protocol violation. This is the strongest C-34 stress test. |
| C-35 | INCUMBENT TOTAL | PASS | [A-13] registered (Finance owner); SC-10: Finance aggregates from [A-04][A-07][A-10]; role-breakdown table with Commerce/Operations/Finance rows; SC-10 optionally notes forward-citation consistency. [A-14] cites [A-13] per SC-8. |

**V-04 Score: 60 + 30 + 10 = 100.0**

*Differentiator: Forward-citation makes C-34 laziness structurally detectable — a missing `[A-02]` token in a Commerce or Operations boundary cell is a definitively flagged protocol violation, not a prose gap. Finance's backward-consistency check adds a verification pass not present in any prior variation.*

---

### V-05 — Finance → Commerce → Operations (dual-register; REGISTER TRANSLATION TABLE)

| ID | Criterion | V-05 | Evidence |
|----|-----------|------|----------|
| C-01..C-04 | Essential | All PASS | Finance (tabular), Commerce (conversational), Operations (tabular); all structural requirements active in both registers |
| C-05..C-07 | Recommended | All PASS | `Stage Latency` column (tabular) and `**Stage latency:**` opener (conversational); [A-11] STALE ANALYSIS |
| C-08..C-14 | (Standard criteria) | All PASS | Register-specific enforcement via REGISTER TRANSLATION TABLE; SC-3 covers both `Elapsed (cumul.)` column and `**Elapsed:**` marker |
| C-15 | Incumbent baseline | PASS | [A-01] INCUMBENT BASELINE produced first by Finance; cited in [A-12] formula `Fall back to [A-01] if [condition]` and SC-8 requires [A-14] cites [A-01] |
| C-16 | Cross-role reference chain | PASS | SC-1: Commerce cites [A-01][A-02][A-04]; Operations cites [A-01][A-02][A-04][A-07]. Operations citing [A-04] (Finance, two roles prior) is explicitly required |
| C-17 | Immutability | PASS | SC-5: Finance appends immutability statement to [A-02]; "SLA = [A-01] total + [headroom]" anchoring |
| C-18..C-22 | (Structural) | All PASS | Per-register enforcement in REGISTER TRANSLATION TABLE |
| C-23 | Phase gate checklists | PASS | [A-05] tabular checklist; [A-08] conversational with sentence-format compliance items referencing SC-x identifiers |
| C-24 | Upfront constraint section | PASS | SC-1..SC-10 upfront; "[Apply SC-x]" callbacks in role instructions; register-aware callbacks (e.g., "tabular: column; conversational: `**Elapsed:**` marker") |
| C-25 | Phase gate artifacts as registry rows | PASS | [A-05] and [A-08] appear with token, owner, register, description in ARTIFACT REGISTRY |
| C-26 | Non-natural role ordering | PASS | Finance → Commerce → Operations. Operations must cite [A-04] (Finance, two roles prior). SC-1 requires it explicitly; Commerce is the immediate predecessor but Finance's boundaries ([A-04]) must still be named |
| C-27 | Named recovery formula | PASS | `Fall back to [A-01] if [condition]` as required formula |
| C-28 | Named-column boundary block schema | PASS | REGISTER TRANSLATION TABLE tabular section: 8 named columns (including `Incumbent Equiv.`). Conversational section: 8 named bold markers. Covers both registers |
| C-29 | Trade-off as required named section | PASS | SC-8 mandates [A-14]; cites [A-01][A-02][A-13] required |
| C-30 | Output register declaration | PASS | REGISTER TRANSLATION TABLE explicitly names tabular and conversational registers; per-field compliance markers for each |
| C-31 | Pre-declared boundary block schema section | PASS | REGISTER TRANSLATION TABLE serves as the pre-role boundary schema declaration (explicitly stated: "simultaneously declares the boundary block schema (per C-31)") |
| C-32 | Register-specific compliance marker mapping | PASS | Tabular: column headers. Conversational: bold markers. Both mapped in same table. Criterion requires "enumerated as a table or list" — present |
| C-33 | Register-invariant declaration | PASS | REGISTER INVARIANTS section explicitly present; 5 criteria mapped with tabular check + conversational equivalent. C-34 listed: `**Incumbent equivalent:**` marker = column existence equivalent |
| C-34 | Per-boundary incumbent equivalent | PASS | Tabular: `Incumbent Equiv.` column, form `[A-01]: [step + duration]`. Conversational: `**Incumbent equivalent:**` bold marker, form `[A-01]: [step + duration]`. Both in REGISTER TRANSLATION TABLE. SC-9 covers both: "Token required in both registers; bare durations are protocol violations." REGISTER INVARIANTS confirms C-34 survives register switch |
| C-35 | INCUMBENT TOTAL | PASS | [A-13] registered; REGISTER TRANSLATION TABLE INCUMBENT TOTAL section format row specifies markdown table with role rows including Finance, Commerce (conversational), Operations, Grand Total. [A-13] template in role instructions correctly specifies "sum of [A-07] **Incumbent equivalent:** values." SC-10 covers aggregation from mixed registers. *(Minor: SC-10's parenthetical says `**Elapsed:**` entries rather than `**Incumbent equivalent:**` — an internal inconsistency, but [A-13] role instruction and REGISTER TRANSLATION TABLE are authoritative and correct.)* |

**V-05 Score: 60 + 30 + 10 = 100.0**

*Differentiator: C-33 explicitly included in REGISTER INVARIANTS (row 4: C-34 conversational check). INCUMBENT TOTAL aggregation is cross-register with per-row extraction method. Most architecturally sophisticated variation.*

---

## Composite Scores

| Var | Essential (60) | Recommended (30) | Aspirational (10) | **Total** | C-26 |
|-----|---------------|-----------------|------------------|-----------|------|
| V-01 | 60 | 30 | 9.64 | **99.6** | FAIL |
| V-02 | 60 | 30 | 9.64 | **99.6** | FAIL |
| V-03 | 60 | 30 | 10.00 | **100.0** | PASS |
| V-04 | 60 | 30 | 10.00 | **100.0** | PASS |
| V-05 | 60 | 30 | 10.00 | **100.0** | PASS |

---

## Ranking

| Rank | Variation | Score | Axis |
|------|-----------|-------|------|
| **1** | V-03 | 100.0 | Inertia-first + non-natural ordering (O→F→C) |
| **1** | V-04 | 100.0 | Forward-citation stress + Finance-last verification (C→O→F) |
| **1** | V-05 | 100.0 | Dual-register + REGISTER TRANSLATION TABLE (F→C→O) |
| 4 | V-01 | 99.6 | Lifecycle emphasis (F→O→C) |
| 4 | V-02 | 99.6 | REGISTER DECLARATION primary vehicle (F→O→C) |

---

## Excellence Signals

**From V-03 — Inertia-first baseline eliminates forward-citation ambiguity:**
When INCUMBENT BASELINE is the first artifact in the entire output, every `Incumbent Equiv.` cell at every boundary cites a fully-produced artifact. No forward-citation risk. The SLA anchoring formula ("SLA = [A-01] total + [headroom]") also creates a bidirectional dependency: DOMAIN CONTEXT threshold is mathematically derivable from the INCUMBENT TOTAL, making C-13 and C-35 numerically cross-checkable.

**From V-04 — Finance-last backward-consistency verification pass:**
The combination of forward-citation protocol (Commerce and Operations cite [A-02] before Finance produces it) with an explicit consistency audit (Finance notes discrepancies between forward-cited steps and actual [A-02] step names) is a genuinely new verification architecture. C-34 compliance is now testable in two directions: structural (token present?) and semantic (does the step name match?). No prior variation had a backward-verification pass.

**From V-05 — REGISTER TRANSLATION TABLE as unified compliance surface for C-34/C-35:**
The REGISTER TRANSLATION TABLE simultaneously serves C-31 (boundary schema), C-32 (per-field markers), and C-33 (invariants). Adding the INCUMBENT TOTAL section format to this table makes C-35 verification format-aware: an evaluator confirms C-35 by checking the REGISTER TRANSLATION TABLE's section row, not by reading role instructions. Cross-register INCUMBENT TOTAL aggregation with per-role extraction method (explicitly specifying scanning [A-07] for `**Incumbent equivalent:**` markers) is a new structural pattern for multi-register pipelines.

**From V-04 — Phase gate self-verification with SC-9 validation item:**
Every Phase Gate in R10 includes an explicit checklist item confirming that Incumbent Equiv. cell form was followed (e.g., "Every `Incumbent Equiv.` cell uses form `[A-02]: [named step + duration]` (SC-9)"). This creates a mandatory intermediate checkpoint for C-34 compliance at role transitions — a verification gate between C-34 production and the next role's consumption.

---

## New Patterns for R11 Rubric

**Pattern 1 — Backward-citation consistency audit (V-04 Finance-last):**
When INCUMBENT BASELINE is produced last (after roles have forward-cited it), the baseline-producing role should be required to explicitly verify that each forward-cited step name corresponds to an actual step in the baseline — not just note discrepancies optionally. A mandatory consistency audit converts C-34 from a structural token-presence check into a semantic content check.

**Pattern 2 — SLA anchoring formula creating bidirectional C-13/C-35 constraint (V-03/V-05):**
When DOMAIN CONTEXT declares the staleness SLA as `SLA = [A-01] total + [headroom]`, the threshold is mathematically derivable from the INCUMBENT TOTAL Grand Total. This creates a verifiable relationship: if [A-13] Grand Total ≠ ([A-01] threshold − headroom), either the threshold or the INCUMBENT TOTAL is wrong. This bidirectional constraint could become a new criterion requiring the declared SLA derivation formula to be checkable against the [A-13] Grand Total.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["backward-citation consistency audit: the baseline-producing role explicitly verifies that forward-cited step names match actual baseline steps — converting C-34 from token-presence to semantic correctness", "SLA anchoring formula creates bidirectional C-13/C-35 constraint: threshold declared as baseline-total + headroom makes C-13 threshold numerically derivable from C-35 INCUMBENT TOTAL Grand Total"]}
```
