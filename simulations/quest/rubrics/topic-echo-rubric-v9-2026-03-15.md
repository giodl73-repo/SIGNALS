Reading the scorecard to extract Round 8 excellence signals before writing the rubric.

The two excellence signals come from the V-01/V-02 delta on C-15 and C-21:

**Signal → C-26**: C-15 PASS in V-01, PARTIAL in V-02. V-01 evidence: *"If 'Defeated Belief' cannot be stated → candidate failed Stage 2 → **return to gate**."* V-02 evidence: *"a check, not a structural admission gate. Counterfactual is validated after generation, not required for admission."* The excellence: gate-back-to-prior-stage semantics vs post-hoc validity flag.

**Signal → C-27**: C-21 PASS in V-01, PARTIAL in V-02. V-01 evidence: *"named stage with clear input (SURPRISE candidates) and output (completed table rows)."* V-02 evidence: *"no named phases with explicit inputs/outputs and word budgets. Pipeline implicit rather than declared."* The excellence: stage contracts visible to the reader as explicit I/O declarations.

---

## Rubric: `topic-echo` — v9

**Skill**: `topic:echo`
**Version**: v9
**Date**: 2026-03-16
**Criteria count**: 27 (4 essential / 3 recommended / **20** aspirational)

**Formula**: `(essential_pass/4 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/20 × 10)`

Each full aspirational pass ≈ **0.50 pts** (down from 0.56 in v8, denominator grew 18 → 20).

---

### Essential (4) — 60 pts total

| # | Criterion | Category |
|---|-----------|----------|
| C-01 | Minimum Entry Count | structure |
| C-02 | Signal Attribution | structure |
| C-03 | Surprise Framing | structure |
| C-04 | Actionability | structure |

**Pass condition**: All 4 required. Failure on any essential → score capped at 59 regardless of other criteria.

---

### Recommended (3) — 30 pts total

| # | Criterion | Category |
|---|-----------|----------|
| C-05 | Namespace Diversity Enforcement | enforcement |
| C-06 | Correction Register | schema |
| C-07 | Impact Double-Enforcement | enforcement |

---

### Aspirational (20) — 10 pts total

| # | Criterion | Category |
|---|-----------|----------|
| C-08 | Cross-Signal Synthesis | synthesis |
| C-09 | Counterfactual Awareness | epistemic |
| C-10 | Epistemic Delta Tracing | epistemic |
| C-11 | Non-Derivability Verification | epistemic |
| C-12 | Root-Cause Grouping | synthesis |
| C-13 | Signal Coverage Assessment | meta |
| C-14 | Redundancy Elimination | enforcement |
| C-15 | Structural Counterfactual Induction | schema |
| C-16 | Misunderstanding-Category Synthesis | synthesis |
| C-17 | Correction-Register Schema Design | schema |
| C-18 | Verification Audit Layer | enforcement |
| C-19 | Synthesis-Section Independence | meta |
| C-20 | Audit Scope Differentiation | enforcement |
| C-21 | Enforcement Pipeline Staging | enforcement |
| C-22 | Synthesis Verdict Commitment | meta |
| C-23 | Pre-Investigation Belief Inventory | epistemic |
| C-24 | Confidence-Weighted Triage | triage |
| C-25 | Surviving Belief Handover | synthesis |
| C-26 | Admission Gate Return Semantics | enforcement |
| C-27 | Stage I/O Contract Declaration | schema |

---

### Criteria — Essential

**C-01 | Minimum Entry Count** (essential, structure)

Pass condition: ≥3 distinct surprise entries present. Failure → floor-miss noted, score capped at 59.

---

**C-02 | Signal Attribution** (essential, structure)

Pass condition: Every entry carries ≥2 cross-signal citations. Entry format: `[CROSS: {artifact-A} × {artifact-B}]`. Single-artifact entries are discarded before the entry gate.

---

**C-03 | Surprise Framing** (essential, structure)

Pass condition: Every entry contains a falsifiable "We believed: {specific assumption}" field. Vague fills ("we hadn't considered") → FAIL.

---

**C-04 | Actionability** (essential, structure)

Pass condition: Every entry contains "If the next team carries the old assumption: {specific concrete mis-design}." Abstract consequences → FAIL.

---

### Criteria — Recommended

**C-05 | Namespace Diversity Enforcement** (recommended, enforcement)

Pass condition: ≥3 distinct namespaces covered; explicit floor stated in the prompt; entry sourcing is verified against the namespace list.

---

**C-06 | Correction Register** (recommended, schema)

Pass condition: Step 9 correction register present with T-1..T-4 slots; each slot has a citable source requirement; empty/abstract fills flagged.

---

**C-07 | Impact Double-Enforcement** (recommended, enforcement)

Pass condition: Full impact triage occurs before any entry expansion (not after); a traceability check at the end confirms tier labels in entries match declaration-table tiers.

---

### Criteria — Aspirational

**C-08 | Cross-Signal Synthesis** (aspirational, synthesis)

Pass condition: Synthesis section ≤120 words; names ≥2 surprise entries by label; asserts a pattern explicitly unreachable from any single entry alone. PARTIAL if pattern is stated but not attributed to specific entries. FAIL if synthesis merely summarizes individual entries.

---

**C-09 | Counterfactual Awareness** (aspirational, epistemic)

Pass condition: Every entry states the specific wrong action a future team would take if the surprise is not surfaced. PARTIAL if some entries carry the field but others do not.

---

**C-10 | Epistemic Delta Tracing** (aspirational, epistemic)

Pass condition: A non-empty discard log exists; each discarded candidate records route type, reason, and downstream destination (e.g., moved to trace, dropped entirely). FAIL if discard log is empty or absent.

---

**C-11 | Non-Derivability Verification** (aspirational, epistemic)

Pass condition: Each surprise is tested against the fixed Competitor Belief set (CB-IDs from C-23); a new team reading only the spec could not have derived the surprise from the declared belief set alone. PARTIAL if the test is present but runs against an implicit prior rather than the CB-set. FAIL if no non-derivability check exists.

Cross-reference: C-11 PASS requires C-23 PASS (CB-IDs must exist to test against).

---

**C-12 | Root-Cause Grouping** (aspirational, synthesis)

Pass condition: Surprises are grouped by the CB-ID they defeat (not by topic or domain); group headers name the defeated belief; at least 2 distinct CB-IDs anchor at least one group each. PARTIAL if entries are grouped by topic with belief labels added post-hoc. FAIL if no grouping exists or grouping is not anchored to pre-declared CB-IDs.

Cross-reference: C-12 PASS requires C-23 PASS.

---

**C-13 | Signal Coverage Assessment** (aspirational, meta)

Pass condition: Namespace coverage is recorded before entry expansion; a gap is noted if fewer than 3 namespaces are represented; the coverage record is visible in the output.

---

**C-14 | Redundancy Elimination** (aspirational, enforcement)

Pass condition: An explicit cross-entry redundancy check is run after the declaration table is complete; two entries defeating the same CB-ID are structurally flagged as redundancy candidates regardless of surface content. PARTIAL if single-artifact entries are cut (stage 3 gate) but no cross-entry redundancy check is performed. FAIL if no redundancy check of any kind exists.

Cross-reference: C-14 PASS strengthened by C-23 PASS (CB-ID anchor makes structural redundancy testable).

---

**C-15 | Structural Counterfactual Induction** (aspirational, schema)

Pass condition: Belief framing is enforced as a structural admission gate — a candidate that cannot state a falsifiable "Defeated Belief" fails Stage 2 and returns to the prior gate, rather than being flagged invalid post-generation. The gate is stated as a conditional return, not a validation check. PARTIAL if belief framing is validated after entry generation (post-hoc) rather than required for admission. FAIL if no structural enforcement of belief framing exists.

---

**C-16 | Misunderstanding-Category Synthesis** (aspirational, synthesis)

Pass condition: The synthesis section names the category of misunderstanding shared across entries (e.g., capability underestimation, integration surface blindness, pricing-model conflation), not merely the topic pattern. Categories are declarative, not implicit. PARTIAL if the synthesis names a pattern but does not classify by misunderstanding type.

---

**C-17 | Correction-Register Schema Design** (aspirational, schema)

Pass condition: The T-1..T-4 correction register is fully specified — each slot has a named register, a list of required fields, and a source-citation requirement. The schema is visible in the prompt, not implicit in prose instructions.

---

**C-18 | Verification Audit Layer** (aspirational, enforcement)

Pass condition: A formal verification pass exists with per-field confirmation (each required field in each entry is explicitly checked); the audit is a named step, not embedded prose. PARTIAL if enforcement instructions are present ("fill the slot") but no per-field audit step exists.

---

**C-19 | Synthesis-Section Independence** (aspirational, meta)

Pass condition: The synthesis section states its own independence constraint — the pattern it asserts must be "unreachable from any single entry alone"; this constraint is part of the section's acceptance criteria, not a narrator aside.

---

**C-20 | Audit Scope Differentiation** (aspirational, enforcement)

Pass condition: The pipeline contains ≥2 named phases with explicit scope contracts (what each phase may and may not touch); phases are not merely sequential steps but have bounded scopes that prevent scope-bleed between, e.g., triage and expansion. PARTIAL if steps are sequential but no scope contracts are declared.

---

**C-21 | Enforcement Pipeline Staging** (aspirational, enforcement)

Pass condition: The pipeline contains ≥2 named stages with explicit I/O declarations (see C-27); each stage has a declared input type and output type; the pipeline order is not merely implied by step numbering but stated as a dependency chain. PARTIAL if stages exist but I/O contracts are absent or implicit.

Cross-reference: C-21 PASS strengthened by C-27 PASS.

---

**C-22 | Synthesis Verdict Commitment** (aspirational, meta)

Pass condition: The synthesis section commits to a specific cross-entry pattern that is falsifiable and above any individual entry; it does not hedge with "may suggest" or "seems to indicate." PARTIAL if the verdict is stated but qualified with hedging language.

---

**C-23 | Pre-Investigation Belief Inventory** (aspirational, epistemic)

Encodes the R7 V-05 finding that C-12 (Root-Cause Grouping) had never been passed in seven rounds because triage ordering is not failure-mode categorization. V-05 solved it structurally by requiring a Belief Inventory before the investigation gate: a fixed set of falsifiable Competitor Beliefs, each with source and confidence level (HIGH/MEDIUM/LOW). Once beliefs are declared pre-gate, every surprise becomes the defeat of a named knowledge gap, and grouping by defeated belief is grouping by root-cause — no separate categorization step is required.

Pass condition: ≥3 Competitor Beliefs declared before the entry gate in falsifiable form; each belief carries an explicit source and a confidence level (HIGH/MEDIUM/LOW); every surprise entry references the defeated belief by ID (e.g., `defeats: CB-{n}`). PARTIAL if beliefs are declared but confidence levels are absent or entries do not reference belief IDs. FAIL if no pre-gate belief inventory exists, or if beliefs are declared after entry collection begins.

Cross-reference: **C-23 PASS is the structural prerequisite for C-12 PASS** and **C-11 PASS**. C-23 PASS → C-14 strengthened (same-CB-ID entries are structurally redundant).

---

**C-24 | Confidence-Weighted Triage** (aspirational, triage)

Pass condition: HIGH-confidence beliefs receive first-priority surprise slots in the triage order; triage rank is a function of confidence level (HIGH before MEDIUM before LOW), not entry order or surface salience. PARTIAL if confidence levels are declared but triage ordering does not reflect them. FAIL if no confidence-weighted triage step exists.

Cross-reference: C-24 requires C-23 (confidence levels must exist on the belief inventory to weight triage).

---

**C-25 | Surviving Belief Handover** (aspirational, synthesis)

Pass condition: A surviving-belief register exists at output — beliefs that were not defeated by any surprise (i.e., survived the investigation intact) are listed by CB-ID with a note that they require future round confirmation; the register is non-empty unless all beliefs were defeated. PARTIAL if surviving beliefs are mentioned in prose but not registered with CB-IDs. FAIL if no surviving-belief output exists.

---

**C-26 | Admission Gate Return Semantics** (aspirational, enforcement)

Encodes the R8 V-01/V-02 delta on C-15. V-01 PASSED C-15 because belief framing carried explicit return semantics: "If 'Defeated Belief' cannot be stated → candidate failed Stage 2 → **return to gate**." V-02 only reached PARTIAL because it used a post-generation validity check ("VALID / INVALID") rather than a gate that blocks forward progress and routes the candidate back. The distinction: a gate with return semantics prevents a malformed candidate from ever appearing in the output; a validity check merely annotates it.

Pass condition: ≥1 enforcement gate in the pipeline carries explicit return semantics — stated as "→ return to {prior stage}" or equivalent, not as "INVALID" annotation or a post-hoc flag. The return path is a conditional in the prompt flow, not a narrator aside. PARTIAL if the gate condition is stated but the return destination is unspecified (i.e., "this candidate fails" without routing). FAIL if all enforcement is post-hoc validation with no return-routing.

Cross-reference: C-26 PASS strengthens C-15 (structural admission gate becomes testably distinct from validation check) and C-21 (pipeline staging gains directional enforcement, not just ordering).

---

**C-27 | Stage I/O Contract Declaration** (aspirational, schema)

Encodes the R8 V-01/V-02 delta on C-21. V-01 PASSED C-21 because the declaration table stage carried explicit I/O contracts visible to the reader: input type ("SURPRISE candidates"), output type ("completed table rows"). V-02 only reached PARTIAL because its pipeline was implicit — steps were sequenced but no stage had a declared input type, output type, or word budget. A reader of V-02 cannot determine what a stage consumes or produces without inferring it from context.

Pass condition: ≥2 named pipeline stages carry explicit I/O declarations in the prompt text — each stage states its input type (what it consumes), its output type (what it produces), and optionally a word or entry budget. The declarations are visible in the stage header or opening line, not embedded in step prose. PARTIAL if stages are named but input/output types are implicit (inferable but not stated). FAIL if the pipeline is implicit — stages are not named or I/O contracts are entirely absent.

Cross-reference: C-27 PASS strengthens C-21 (pipeline staging gains verifiable contracts) and C-20 (scope differentiation becomes testable when I/O types are declared).
