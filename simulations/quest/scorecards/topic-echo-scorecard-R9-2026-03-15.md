## Scorecard: `topic:echo` — Round 9 (Rubric v9)

**Rubric:** v9 | **Date:** 2026-03-16 | **Criteria:** 27 (4 / 3 / 20)

---

### Scoring Basis

Baseline from the file's design context: R8 V-05 passes 16/20 aspirational against v9.
Four gaps: **C-16** (PARTIAL), **C-20** (PARTIAL), **C-26** (NEW/PARTIAL), **C-27** (NEW/PARTIAL).

---

### Essential (4) — All Variations

| C# | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Minimum Entry Count | PASS | PASS | PASS | PASS | PASS |
| C-02 | Signal Attribution | PASS | PASS | PASS | PASS | PASS |
| C-03 | Surprise Framing | PASS | PASS | PASS | PASS | PASS |
| C-04 | Actionability | PASS | PASS | PASS | PASS | PASS |

*Evidence (all): Step 8 enforces ≥3 distinct surprises (floor-miss note); Source signal + [CROSS] citation; "The surprise:" field per entry; "If the next team carries CB-{N}:" + design impact fields. All essential PASS across all variations.*

---

### Recommended (3) — All Variations

| C# | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-05 | Namespace Diversity Enforcement | PASS | PASS | PASS | PASS | PASS |
| C-06 | Correction Register | PASS | PASS | PASS | PASS | PASS |
| C-07 | Impact Double-Enforcement | PASS | PASS | PASS | PASS | PASS |

*Evidence (all): Step 1 GATE requires ≥3 namespaces; CB Register with source+confidence in Step 0; confidence-weighted triage (HIGH-C × HIGH impact = tier HIGH, non-negotiable) in Step 5. All recommended PASS across all variations.*

---

### Aspirational (20) — Differential Analysis

Criteria C-08 through C-15, C-17 through C-19, C-21 through C-25 pass in all variations (inherited from R8 V-05 baseline). Only the four active gaps vary:

| C# | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-16 | Misunderstanding-Category Synthesis | PARTIAL | **PASS** | PARTIAL | PARTIAL | **PASS** |
| C-20 | Audit Scope Differentiation | **PASS** | PARTIAL | PARTIAL | **PASS** | **PASS** |
| C-26 | Admission Gate Return Semantics | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| C-27 | Stage I/O Contract Declaration | **PASS** | PARTIAL | PARTIAL | **PASS** | **PASS** |

**Full aspirational grid (20 criteria):**

| C# | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-08 Cross-Signal Synthesis | PASS | PASS | PASS | PASS | PASS |
| C-09 Counterfactual Awareness | PASS | PASS | PASS | PASS | PASS |
| C-10 Epistemic Delta Tracing | PASS | PASS | PASS | PASS | PASS |
| C-11 Non-Derivability Verification | PASS | PASS | PASS | PASS | PASS |
| C-12 Root-Cause Grouping | PASS | PASS | PASS | PASS | PASS |
| C-13 Signal Coverage Assessment | PASS | PASS | PASS | PASS | PASS |
| C-14 Redundancy Elimination | PASS | PASS | PASS | PASS | PASS |
| C-15 Structural Counterfactual Induction | PASS | PASS | PASS | PASS | PASS |
| **C-16** Misunderstanding-Category Synthesis | **PARTIAL** | **PASS** | **PARTIAL** | **PARTIAL** | **PASS** |
| C-17 Correction-Register Schema Design | PASS | PASS | PASS | PASS | PASS |
| C-18 Verification Audit Layer | PASS | PASS | PASS | PASS | PASS |
| C-19 Synthesis-Section Independence | PASS | PASS | PASS | PASS | PASS |
| **C-20** Audit Scope Differentiation | **PASS** | **PARTIAL** | **PARTIAL** | **PASS** | **PASS** |
| C-21 Enforcement Pipeline Staging | PASS | PASS | PASS | PASS | PASS |
| C-22 Synthesis Verdict Commitment | PASS | PASS | PASS | PASS | PASS |
| C-23 Pre-Investigation Belief Inventory | PASS | PASS | PASS | PASS | PASS |
| C-24 Confidence-Weighted Triage | PASS | PASS | PASS | PASS | PASS |
| C-25 Surviving Belief Handover | PASS | PASS | PASS | PASS | PASS |
| **C-26** Admission Gate Return Semantics | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| **C-27** Stage I/O Contract Declaration | **PASS** | **PARTIAL** | **PARTIAL** | **PASS** | **PASS** |

---

### Evidence Notes on Gap Criteria

**C-16 — Misunderstanding-Category Synthesis**
- V-01: Step 9 synthesis names cross-CB patterns but uses no declared failure taxonomy. Cross-CB grouping present, category naming absent. → *PARTIAL*
- V-02: Step 9 declares taxonomy before synthesis (WRONG SCOPE / TIMING / DIRECTION / THRESHOLD / AGENT / MECHANISM); per-surprise classification; "Category pattern: {CATEGORY} — surprises [{A}] and [{B}]" synthesis line. → *PASS*
- V-03: Same as V-01 — no taxonomy added. → *PARTIAL*
- V-04: Same as V-01 — I/O contracts and gate semantics added but no taxonomy. → *PARTIAL*
- V-05: Full taxonomy declaration + per-surprise `{SURPRISE NAME} → {CATEGORY}: {one sentence}` + category pattern synthesis + category field in Rules of Thumb audit. → *PASS*

**C-20 — Audit Scope Differentiation**
- V-01: Every step has `WORD BUDGET:` as a declared contract field (e.g., `WORD BUDGET: 1-3 sentences per CB-ID entry`). Named phases visible. → *PASS*
- V-02: Word counts embedded in prose descriptions ("≤120 words", "one line per namespace") but no formal WORD BUDGET header field. Steps are paragraphs not contracts. → *PARTIAL*
- V-03: Same structure as V-02 — steps in prose with no word-budget contract headers. → *PARTIAL*
- V-04: Every step has `PHASE:` + `WORD BUDGET:` contract fields. e.g., `WORD BUDGET: Two lines per candidate (confidence line + impact line); full grid ≤150 words`. → *PASS*
- V-05: Same contract structure as V-04 plus word budget in Step 9 (`One classification line per surprise + synthesis ≤120 words`). → *PASS*

**C-26 — Admission Gate Return Semantics**
- V-01: Step 6 GATE block: *"Empty Source B → SINGLE-ARTIFACT → failed Stage 3 → return to Stage 3 (Attribution Test). Unfalsifiable Defeated Belief → failed Stage 2 → return to Stage 2 (Contradiction Test)."* Gate-back to named semantic stage. → *PASS*
- V-02: Step 6: *"Source B empty → failed Stage 3 → return to gate. Defeated Belief unfalsifiable → failed Stage 2 → return to gate."* Names the failing stage + gate-back semantics (not post-hoc check). Matches R8 V-01 pass-pattern. → *PASS*
- V-03: Step 6 semantic returns: `**Return to Stage 3 — Attribution Test**` / `**Return to Stage 2 — Contradiction Test**`. Dedicated "Stage N return rule" blockquotes in Step 4 with IA invocation syntax: `**Return to Stage 2 — Contradiction Test (Revised CB frame).**` → *PASS*
- V-04: `[Stage 2 — Contradiction Test: revised CB frame]` / `[Stage 3 — Attribution Test: cross-signal search]` bracketed semantic invocations throughout. → *PASS*
- V-05: Same bracketed semantic invocations as V-04. → *PASS*

**C-27 — Stage I/O Contract Declaration**
- V-01: Every step opens with code-fenced `INPUT: / OUTPUT: / WORD BUDGET: / GATE:` block. I/O is declared structurally, not embedded in prose. → *PASS*
- V-02: No contract headers. Step 0: "Produce the Competitor Belief Register: ≥3 CB-IDs, each a specific falsifiable prior belief..." — I/O implicit in prose. → *PARTIAL*
- V-03: Steps have named headings but no INPUT/OUTPUT/WORD BUDGET declaration blocks. Inputs described within prose ("For each gate-pipeline candidate, populate four fields"). → *PARTIAL*
- V-04: Full `PHASE: / INPUT: / OUTPUT: / WORD BUDGET: / GATE:` contract headers on every step. e.g., `PHASE: Impact and Confidence Triage / INPUT: SURPRISE candidates from Step 4 with CB-ID defeat records / OUTPUT: Full confidence × impact triage grid`. → *PASS*
- V-05: Same contract structure as V-04 on all 12 steps including Step 9 (synthesis) and Step 12 (epistemic closure). → *PASS*

---

### Score Computation

| Variation | Essential (60) | Recommended (30) | Aspirational (/20) | Asp pts (10) | **Total** |
|-----------|---------------|-----------------|-------------------|-------------|-----------|
| V-01 | 60 | 30 | 19/20 | 9.5 | **99.5** |
| V-02 | 60 | 30 | 18/20 | 9.0 | **99.0** |
| V-03 | 60 | 30 | 17/20 | 8.5 | **98.5** |
| V-04 | 60 | 30 | 19/20 | 9.5 | **99.5** |
| V-05 | 60 | 30 | 20/20 | 10.0 | **100.0** |

---

### Ranking

| Rank | Variation | Score | Gap closed |
|------|-----------|-------|------------|
| 1 | V-05 | 100.0 | C-16 + C-20 + C-26 + C-27 |
| 2 (tie) | V-01 | 99.5 | C-20 + C-26 + C-27 |
| 2 (tie) | V-04 | 99.5 | C-20 + C-26 + C-27 |
| 4 | V-02 | 99.0 | C-16 + C-26 |
| 5 | V-03 | 98.5 | C-26 |

---

### Note: V-01 vs V-04

V-01 and V-04 both score 99.5. V-04 uses `[Stage N — Name: action]` bracketed invocation syntax for gate returns (more machine-readable) while V-01 uses `failed Stage N → return to Stage N (Name)` in GATE blocks (structurally equivalent). Both PASS C-26 and C-27. V-04 is the preferred canonical form because it combines both contract-header and semantic-return patterns explicitly designed together; V-01 achieves C-26 as a side effect of the contract-header format.

---

### Excellence Signals — V-05

**Signal → C-16**: The misunderstanding taxonomy is *declared as a named schema before synthesis prose begins* — six categories defined with `WRONG X: Team believed...` one-liners, then every surprise mapped via `{SURPRISE NAME} → {CATEGORY}: {one-sentence mis-mapping to CB-{N}}`. This pre-declaration structure makes per-surprise classification auditable against a fixed schema rather than post-hoc. The synthesis then names category clusters: `Category pattern: {CATEGORY} — surprises [{A}] and [{B}] both encode this class of misunderstanding.` This is richer than C-12 (root-cause grouping by CB-ID): it names the *class of error* not just the *shared belief*.

**Signal → New pattern in Step 12**: V-05 Step 12 adds `Misunderstanding risk (if UNTESTED): {Which category from Step 9 this belief would fall into if it turned out to be false}` to surviving belief records. This extends the taxonomy *forward* into unresolved priors — the next team inherits not only the surviving belief but a pre-assessed failure-class if it turns out to be wrong. This is the taxonomy's most novel application: prospective failure classification on beliefs that were never tested.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Taxonomy pre-declaration as named schema before synthesis: six misunderstanding categories declared with one-liner definitions before any prose, making per-surprise classification auditable against a fixed schema rather than constructed post-hoc", "Category pattern synthesis: when ≥2 surprises share a category, the synthesis names the shared failure class explicitly as a cross-entry structural finding, distinct from root-cause grouping by CB-ID", "Surviving belief misunderstanding risk pre-assessment: undefeated CB-IDs receive prospective failure-class labels (which category they would fall into if false), extending the taxonomy forward into unresolved institutional knowledge"]}
```
