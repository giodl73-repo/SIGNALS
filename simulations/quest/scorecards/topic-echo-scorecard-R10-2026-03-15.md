## Scorecard: `topic:echo` — Round 10 (Rubric v10)

---

### Scoring Method

**Formula**: `(essential_pass/4 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/22 × 10)`

PARTIAL = 0.5, PASS = 1.0, FAIL = 0. Cap at 59 if any essential fails.

---

### Common Baseline — All Variations (Built on R9 V-05)

Before scoring by variation, the following criteria apply identically to all five:

| Criterion | All Variations | Evidence |
|-----------|---------------|----------|
| C-01 Minimum Entry Count | PASS | Template enforces ≥3 SURPRISE entries via floor-miss rule |
| C-02 Signal Attribution | PASS | `[CROSS: A × B]` annotation in every entry template |
| C-03 Surprise Framing | PASS | `We believed: {falsifiable assumption}` field required in entry schema |
| C-04 Actionability | PASS | `If the next team carries the old assumption: {specific concrete mis-design}` |
| C-05 Namespace Diversity | PASS | Step 1 records ≥3 floor before expansion; gap explicitly flagged |
| C-06 Correction Register | PASS | T-1..T-4 register in Step 9 with named slots and source-citation requirement |
| C-07 Impact Double-Enforcement | PASS | Step 4 triage before expansion; TRACE-CHECK-VERDICT confirms tier match at Step 10 |
| C-08 Cross-Signal Synthesis | PASS | Synthesis ≤120 words, ≥2 named entries, pattern independence constraint stated |
| C-09 Counterfactual Awareness | PASS | Every entry template includes `If next team carries…` field |
| C-10 Epistemic Delta Tracing | PASS | Non-empty discard log with route type, reason, destination per item |
| C-11 Non-Derivability Verification | **FAIL** | No `defeats: CB-{n}` in entry template; C-23 prerequisite not met |
| C-12 Root-Cause Grouping | **FAIL** | No CB-IDs; C-23 prerequisite not met |
| C-13 Signal Coverage Assessment | PASS | Namespace coverage recorded in Step 1 before entry expansion |
| C-14 Redundancy Elimination | **PARTIAL** | Stage 3 cuts single-artifact entries; no cross-entry CB-ID structural redundancy check |
| C-15 Structural Counterfactual Induction | PASS | Stage 2 INVALID → return to discard log (gate, not annotation); Step 6 return to Step 5 |
| C-17 Correction-Register Schema Design | PASS | T-1..T-4 fully specified with slot templates and source-citation requirement in Step 9 |
| C-18 Verification Audit Layer | PASS | TRACE-CHECK-VERDICT named step with per-field confirmation, forward-reader protocol |
| C-19 Synthesis-Section Independence | PASS | "Unreachable from any single entry alone" stated as acceptance criterion in all Step 8 variants |
| C-22 Synthesis Verdict Commitment | PASS | Independence constraint explicit; no hedging language in synthesis instructions |
| C-23 Pre-Investigation Belief Inventory | **FAIL** | No CB-IDs, confidence levels, or `defeats: CB-{n}` field in any variation |
| C-24 Confidence-Weighted Triage | **FAIL** | Requires C-23 PASS; no confidence-weighted mechanism |
| C-25 Surviving Belief Handover | **FAIL** | Requires C-23 content; no surviving-belief register |
| C-26 Admission Gate Return Semantics | PASS | Stage 2 INVALID → return semantics explicit; Step 6 "return to Step 5" |

**Stable aspirational tally (all variations):**
- PASS: C-08, C-09, C-10, C-13, C-15, C-17, C-18, C-19, C-22, C-26 = **10**
- PARTIAL: C-14 = **0.5**
- FAIL: C-11, C-12, C-23, C-24, C-25 = **0**

Baseline aspirational score = **10.5** (with variation-specific criteria C-16, C-20, C-21, C-27, C-28, C-29 still to be scored per variation).

---

### Variation-Specific Criteria

#### C-16 | Misunderstanding-Category Synthesis

| Variation | Score | Evidence |
|-----------|-------|---------|
| V-01 | **PASS** | Step 8 has explicit `CATEGORY DECLARATION:` block with per-surprise typed labels before synthesis paragraph |
| V-02 | **PARTIAL** | Step 8 instructs "Name the category of shared misunderstanding (C-16)" in prose only; no declarative block; categories implied, not structurally declared |
| V-03 | **PARTIAL** | Same as V-02; taxonomy instruction present in PHASE block body but no CATEGORY DECLARATION structure |
| V-04 | **PASS** | CATEGORY DECLARATION block present, categories typed by misunderstanding class |
| V-05 | **PASS** | Full CATEGORY DECLARATION block with vocabulary list (capability-underestimation, integration-surface-blindness, etc.) |

#### C-20 | Audit Scope Differentiation

| Variation | Score | Evidence |
|-----------|-------|---------|
| V-01 | **PARTIAL** | No formal PHASE+SCOPE blocks at step headers; scope constraints embedded in role descriptions and gate prose only |
| V-02 | **PARTIAL** | Step 8 has PHASE+SCOPE block (1 stage); criterion requires ≥2 named phases with scope contracts |
| V-03 | **PASS** | Every pipeline step (Steps 1–12) opens with explicit `PHASE:` + `SCOPE:` block; prevents scope-bleed across all phases |
| V-04 | **PARTIAL** | Step 8 has PHASE+SCOPE block; no formal scope contracts at other step headers |
| V-05 | **PASS** | PHASE+SCOPE+optional WORD BUDGET+INPUT+OUTPUT at every named step; complete phase-contract coverage |

#### C-21 | Enforcement Pipeline Staging

| Variation | Score | Evidence |
|-----------|-------|---------|
| V-01 | **PARTIAL** | Dependency chain stated in Step 12 chain trace with produces/consumed-by; I/O not at execution-time step headers — C-27 not met |
| V-02 | **PASS** | Step 8 PHASE block has INPUT/OUTPUT declared at header; Step 12 chain trace names all NODE I/O; ≥2 stages with explicit declarations |
| V-03 | **PASS** | Same as V-02 + PHASE blocks on all steps |
| V-04 | **PASS** | Step 8 PHASE block with INPUT/OUTPUT; Step 12 chain trace; dependency chain explicitly closed |
| V-05 | **PASS** | Steps 7 and 8 both carry full INPUT/OUTPUT declarations in PHASE blocks; chain trace complete |

#### C-27 | Stage I/O Contract Declaration

| Variation | Score | Evidence |
|-----------|-------|---------|
| V-01 | **PARTIAL** | I/O contracts visible only in Step 12 terminal chain trace; not at execution-time step headers |
| V-02 | **PASS** | Step 8 header declares INPUT/OUTPUT; chain trace enumerates all nodes; ≥2 stages verifiable at point of execution |
| V-03 | **PASS** | Step 8 PHASE block has INPUT/OUTPUT; chain trace; all steps have phase labels |
| V-04 | **PASS** | Step 8 PHASE block explicitly lists INPUT and OUTPUT types; chain trace closed with 7 enumerated loops |
| V-05 | **PASS** | Steps 7 and 8 both carry I/O in step headers; chain trace closes all loops; full pipeline verifiable |

#### C-28 | Category-Field Audit Propagation

| Variation | Score | Evidence |
|-----------|-------|---------|
| V-01 | **PASS** | CATEGORY DECLARATION in Step 8 → Step 10 schema explicitly `(encodes: {NAME} → {CATEGORY}: {label})`. Return gate at Step 10: "absent label → return to Step 8." Propagation is structural. |
| V-02 | **FAIL** | C-16 PARTIAL (no taxonomy block) → Step 10 uses `(encodes: {SURPRISE NAME})` only; no `{CATEGORY}:` field in audit rows |
| V-03 | **FAIL** | No CATEGORY DECLARATION block in Step 8; Step 10 audit rows standard format without `{CATEGORY}:` |
| V-04 | **PASS** | CATEGORY DECLARATION → Step 10 schema includes `{CATEGORY}: {taxonomy-label}` field; Step 10 check #4 verifies each `{CATEGORY}:` references declared label |
| V-05 | **PASS** | Full CATEGORY DECLARATION block; Step 10 PHASE block with `{CATEGORY}:` propagation; TRACE-CHECK-VERDICT certifies C-28 propagation; chain trace names NODE 3b → NODE 7 as explicit dependency |

#### C-29 | Synthesis-Step Budget Contract

| Variation | Score | Evidence |
|-----------|-------|---------|
| V-01 | **PARTIAL** | Step 8 synthesis paragraph instructions contain prose "<=120 words" but no `WORD BUDGET:` contract header as named field |
| V-02 | **PASS** | Step 8 PHASE block carries `WORD BUDGET: <=120 words (synthesis paragraph only)` as named contract field; scoped to Step 8 specifically; Dependency Closure confirms as standalone C-29 anchor |
| V-03 | **PASS** | Step 8 PHASE block includes `WORD BUDGET: <=120 words (synthesis paragraph)` as named field; rubric pass condition met (named contract field, not prose instruction) |
| V-04 | **PASS** | `WORD BUDGET: <=120 words (synthesis paragraph; taxonomy declaration lines not counted)` as named field in Step 8 PHASE block; chain trace notes "WORD BUDGET: standalone contract field at step header (C-29)" |
| V-05 | **PASS** | Same as V-04; chain trace explicitly names NODE 5 budget contract (C-29); Dependency Closure Enumeration identifies as a distinct anchor |

---

### Full Aspirational Matrix

| # | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|-----------|------|------|------|------|------|
| C-08 | Cross-Signal Synthesis | P | P | P | P | P |
| C-09 | Counterfactual Awareness | P | P | P | P | P |
| C-10 | Epistemic Delta Tracing | P | P | P | P | P |
| C-11 | Non-Derivability Verification | F | F | F | F | F |
| C-12 | Root-Cause Grouping | F | F | F | F | F |
| C-13 | Signal Coverage Assessment | P | P | P | P | P |
| C-14 | Redundancy Elimination | ½ | ½ | ½ | ½ | ½ |
| C-15 | Structural Counterfactual Induction | P | P | P | P | P |
| C-16 | Misunderstanding-Category Synthesis | P | ½ | ½ | P | P |
| C-17 | Correction-Register Schema Design | P | P | P | P | P |
| C-18 | Verification Audit Layer | P | P | P | P | P |
| C-19 | Synthesis-Section Independence | P | P | P | P | P |
| C-20 | Audit Scope Differentiation | ½ | ½ | P | ½ | P |
| C-21 | Enforcement Pipeline Staging | ½ | P | P | P | P |
| C-22 | Synthesis Verdict Commitment | P | P | P | P | P |
| C-23 | Pre-Investigation Belief Inventory | F | F | F | F | F |
| C-24 | Confidence-Weighted Triage | F | F | F | F | F |
| C-25 | Surviving Belief Handover | F | F | F | F | F |
| C-26 | Admission Gate Return Semantics | P | P | P | P | P |
| C-27 | Stage I/O Contract Declaration | ½ | P | P | P | P |
| C-28 | Category-Field Audit Propagation | P | F | F | P | P |
| C-29 | Synthesis-Step Budget Contract | ½ | P | P | P | P |
| **Sum / 22** | | **14.5** | **14.5** | **15.0** | **16.0** | **16.5** |
| **Pts (×10/22)** | | **6.59** | **6.59** | **6.82** | **7.27** | **7.50** |

*P = PASS (1.0), ½ = PARTIAL (0.5), F = FAIL (0)*

---

### Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | **Total** |
|-----------|---------------|-----------------|-------------------|----------|
| V-01 | 60 | 30 | 6.59 | **96.59** |
| V-02 | 60 | 30 | 6.59 | **96.59** |
| V-03 | 60 | 30 | 6.82 | **96.82** |
| V-04 | 60 | 30 | 7.27 | **97.27** |
| **V-05** | **60** | **30** | **7.50** | **97.50** |

**Ranking: V-05 > V-04 > V-03 > V-01 = V-02**

---

### Differential Analysis

**V-01 vs V-02 (tied at 96.59):**
V-01 wins C-16 (PASS vs PARTIAL) and C-28 (PASS vs FAIL), gaining +1.5 in aspirational points. V-02 wins C-21 (PASS vs PARTIAL), C-27 (PASS vs PARTIAL), and C-29 (PASS vs PARTIAL), gaining +1.5. The net cancels exactly — confirming the design intent that C-28 and C-29 are comparably weighted structural gaps.

**V-03 vs V-01/V-02 (+0.23):**
Formal phase blocks throughout deliver C-20 PASS (vs PARTIAL), C-27 PASS, and C-29 PASS — but C-28 FAIL eliminates the taxonomy gains from V-01. Net: +0.5 aspirational unit over V-01.

**V-04 vs V-03 (+0.45):**
C-28 PASS on top of V-03's gains, at cost of C-20 PARTIAL (no full-pipeline phase contracts). Net: +1.0 aspirational unit.

**V-05 vs V-04 (+0.23):**
Uniform PHASE+SCOPE contracts throughout — the only gain is C-20 PASS (vs PARTIAL). Single +0.5 unit delta confirms the phrasing register axis is real but marginal.

---

### Excellence Signals from V-05

**Pattern 1: Taxonomy as schema constraint, not rhetorical category**
The CATEGORY DECLARATION block in Step 8 forces the model to type every surprise by misunderstanding class *before* writing synthesis. By making Step 10's audit row schema a structural consumer of that declaration (`{CATEGORY}: {label}` with return gate "absent label → return to Step 8"), the taxonomy becomes non-optional. Without it, audit rows cannot be written. This is distinct from C-16's "name the category in prose" — it makes the category a typed dependency that propagates forward.

**Pattern 2: Full-pipeline phase scope contracts prevent scope-bleed at execution time**
V-05 is the only variation where every step opens with a PHASE+SCOPE block, not just the synthesis step. The `SCOPE:` field on Step 3 says "rejection testing only — no triage, no expansion, no naming." On Step 4: "tier assignment only — no entry generation." On Step 6: "gate only — no expansion until both VALID." This makes scope violations detectable by a reader at each step, not just inferable from the pipeline sequence.

**Pattern 3: Closed dependency graph with typed upstream/downstream links**
V-05's Dependency Closure Enumeration explicitly names the NODE 3b → NODE 5 and NODE 3b → NODE 7 links, with the C-28 label on each. A reviewer checking whether C-28 propagation occurred has a single named artifact to locate (TRACE-CHECK-VERDICT, check #4) without reading the full chain.

---

### Ceiling Analysis

The aspirational ceiling for v10 without C-23 (no Competitor Belief inventory) is **16.5/22 aspirational units = 97.50**. The five failing criteria (C-11, C-12, C-23, C-24, C-25) all depend on CB-IDs; C-14 is structurally PARTIAL without them. Adding C-23 in v11 would unlock +3.5 aspirational points at minimum (C-23 PASS, C-11 PASS, C-12 PASS possible), pushing the ceiling toward 99+.

---

```json
{"top_score": 97.5, "all_essential_pass": true, "new_patterns": ["taxonomy-as-schema-constraint: CATEGORY DECLARATION in Step 8 propagates as typed {CATEGORY}: field into Step 10 audit rows, making taxonomy structurally non-optional via return gate", "full-pipeline phase scope contracts: PHASE+SCOPE blocks at every step make scope-bleed violations detectable at execution time, not inferred from sequence"]}
```
