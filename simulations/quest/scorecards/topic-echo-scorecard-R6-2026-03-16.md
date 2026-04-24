# Round 6 Scorecard — `topic:echo`

**Rubric:** v6 | **Max:** 155 | **Date:** 2026-03-16

---

## Criterion-by-criterion evaluation

### Essential (C-01 – C-05) — All variations

All five variations inherit R5 V-05's structural enforcement of every essential criterion:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-01 Named surprises | PASS | PASS | PASS | PASS | PASS | CORRECTION RECORD requires departure framing; STILL-LIVE FILTER enforces surprise/expected partition |
| C-02 Signal tracing | PASS | PASS | PASS | PASS | PASS | `Source: namespace:skill:artifact` field — prose attribution prohibited |
| C-03 Design impact | PASS | PASS | PASS | PASS | PASS | "What the next team would build wrong" field — specific component/flow required |
| C-04 Synthesis not summary | PASS | PASS | PASS | PASS | PASS | STILL-LIVE FILTER + correction-register framing blocks summary content |
| C-05 Surprise specificity | PASS | PASS | PASS | PASS | PASS | PBI-Ref + Source artifact linkage requires investigation-specific derivation |

**Essential subtotal: 60/60 for all five.**

---

### Recommended (C-06 – C-08) — All variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-06 Counterfactual | PASS | PASS | PASS | PASS | PASS | PBI + "What today's materials imply" / "What signals showed instead" fields enforce expected-vs-actual structure |
| C-07 Institutional framing | PASS | PASS | PASS | PASS | PASS | Future-team framing throughout; CORRECTION FORWARD STATEMENT closes with "Before you build…" register |
| C-08 Cross-signal pattern | PASS | PASS | PASS | PASS | PASS | CROSS-SIGNAL REQUIREMENT mandates at least one multi-signal entry with named convergence gap; PATTERN OF INHERITED ERRORS section explicitly required |

**Recommended subtotal: 30/30 for all five.**

---

### Aspirational (C-09 – C-21) — criterion detail

#### C-09 through C-18 — shared baseline (all variations)

All six variations inherit R5 V-05's structure for C-09 through C-18 without degradation:

| Criterion | All five | Evidence |
|-----------|----------|----------|
| C-09 Surprise hierarchy | PASS | PHASE 4 required; numbered list with argued rationale; "assertion without argument fails" |
| C-10 Riskiest surprise | PASS | PHASE 4 top-ranked entry: "names the design decision at risk and what must be redesigned before other work can proceed"; BLIND SPOT MAP synthesis provides structural identification |
| C-11 PBI | PASS | PB-[NN] identifiers required; freeze before PHASE 1 |
| C-12 Named handles | PASS | HL-[NN] labels required in Handle Ledger, cited by Name field in entries |
| C-13 Dual phase-locked integrity | PASS | PBI uses belief language; Handle Ledger uses finding language; independence test stated explicitly |
| C-14 Audit trail completeness | PASS | All three pointers in every entry: Handle Ledger cite (Name), PBI-Ref, Source artifact |
| C-15 Mechanism declaration | PASS | STRUCTURAL PROVENANCE declared (in PBI preamble for V-01/V-02/V-04; in ENFORCEMENT MECHANISM section for V-03/V-05) |
| C-16 Production-time attestation | PASS | Verified field required; "actual text of both, sufficient to confirm cited identifiers point to the right content" |
| C-17 Mechanism classification | PASS | Tier (STRUCTURAL), distinguishing property (role-scope exclusion vs phase sequencing), reviewer implication (C-13 confirmatory not probative) — present in all five |
| C-18 Per-entry attestation with quotation | PASS | Verified field: "Quote the actual text of PB-[NN] and the key sentence from the source artifact" — identifier-only fails |

**C-09 through C-18 subtotal: 50/50 for all five.**

---

#### C-19 — Post-production chain integrity audit with visible tokens

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Explicit PHASE 3B: CHAIN INTEGRITY AUDIT added. Structurally distinct from ENTRY GATE (gate = register quality; audit = chain consistency). Four-element verification per entry: [1] PBI-Ref alignment, [2] Handle match, [3] Source artifact existence, [4] Verified quotation accuracy. Emits `CHAIN-COMPLETE` or `CHAIN-FLAG` per entry. CHAIN-FLAG blocks progression. |
| V-02 | **PASS** | PHASE 3B retained from V-01, same token emission mechanism |
| V-03 | **PASS** | PHASE 3B retained from V-01/V-02 baseline |
| V-04 | **PASS** | Explicit PHASE 3B, same specification as V-01 |
| V-05 | **PASS** | PHASE 3B retained; CHAIN-COMPLETE tokens visible in artifact structure item 6 |

---

#### C-20 — Impact-anchored distillation layer with traceability verification

The v6 rubric requires **both**: (1) a Rules of Thumb section with tier annotations ([HIGH]/[MEDIUM], LOW excluded), and (2) a named `RULES-ANCHORED` traceability check confirming tier alignment. The CORRECTION FORWARD STATEMENT (1-3 narrative sentences) cannot satisfy this requirement — it lacks tier annotations and a named check.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **FAIL** | No PHASE 4B. Artifact structure has CORRECTION FORWARD STATEMENT (PHASE 7) but no Rules of Thumb table, no tier annotations, no RULES-ANCHORED check. Narrative distillation does not satisfy the structured table + named traceability check requirement. |
| V-02 | **PASS** | PHASE 4B: RULES OF THUMB added. Table with `Rule`, `Tier`, `Entry`, `Statement (<=20 words)` columns. RULES-ANCHORED block follows: "R-01: tier [HIGH] confirmed against entry [Name] Severity: [HIGH] — ALIGNED." Blocking condition: "Do not proceed to Phase 5 until all rules show ALIGNED." Artifact structure item 7: "Rules of Thumb (table + RULES-ANCHORED)." |
| V-03 | **PASS** | PHASE 4B retained from V-02 baseline. Artifact structure item 8: "Rules of Thumb (table + RULES-ANCHORED)." |
| V-04 | **PASS** | Explicit PHASE 4B, same specification as V-02 |
| V-05 | **PASS** | PHASE 4B retained; RULES-ANCHORED present; artifact structure item 8 |

---

#### C-21 — Enforcement mechanism declaration in independently navigable section

The v6 rubric test: *can a reviewer jump directly to the enforcement mechanism claim using section headings or table titles alone?*

The structural provenance declaration in V-01/V-02/V-04 is located in the **PBI preamble** — embedded within the `== PRE-COMMITTED BELIEF INVENTORY (PBI) ==` section. A reviewer navigating by section header finds "PRE-COMMITTED BELIEF INVENTORY" — a title that signals *entry production*, not *enforcement mechanism classification*. The C-17 content is present but is not independently navigable.

Note: this is structurally weaker than R5 V-05, which had the structural provenance declaration in CORRECTION ENFORCEMENT Rule 1 — at least navigable via the "CORRECTION ENFORCEMENT" header. V-01/V-02/V-04 moved the declaration into the PBI section, which is less targeted for a reviewer seeking provenance classification.

V-03 and V-05 place a dedicated `== ENFORCEMENT MECHANISM ==` section **first** in the artifact, before PBI, before any entries. The section title unambiguously signals enforcement mechanism classification. Reviewer using section headers jumps directly to it.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **FAIL** | Structural provenance declaration in PBI preamble ("This artifact uses STRUCTURAL PROVENANCE: the PBI-writing role operates under role-scope exclusion…"). Section title "PRE-COMMITTED BELIEF INVENTORY (PBI)" does not signal enforcement mechanism. Not independently navigable. CORRECTION ENFORCEMENT section contains only Rules 1-3 (framing, voice, completeness) — no provenance classification. |
| V-02 | **FAIL** | Same structure as V-01 for C-21. Declaration in PBI preamble. "CORRECTION ENFORCEMENT" section has Rules 1-3 without structural provenance claim. |
| V-03 | **PASS** | Dedicated `== ENFORCEMENT MECHANISM ==` section, position 1 of artifact. Contains: Tier (STRUCTURAL), distinguishing property (role-scope exclusion vs phase sequencing — architectural not behavioral), reviewer implication (C-13 confirmatory rather than probative). Reviewer navigates directly from header "ENFORCEMENT MECHANISM" to the classification claim without reading entry content. |
| V-04 | **FAIL** | Same as V-01/V-02. PHASE 3B and PHASE 4B added; C-21 unchanged. Structural provenance in PBI preamble, not in independently navigable section. |
| V-05 | **PASS** | Dedicated `== ENFORCEMENT MECHANISM ==` section, position 1 (before PBI). All three C-17 elements present. Reviewer can navigate to classification via section header alone. Identical navigability to V-03. |

---

## Composite Scores

| Variation | Essential | Recommended | Asp (C-09–C-18) | C-19 | C-20 | C-21 | Asp Total | Composite | Golden |
|-----------|-----------|-------------|-----------------|------|------|------|-----------|-----------|--------|
| V-01 | 60 | 30 | 50 | 5 | 0 | 0 | 55 | **145** | YES |
| V-02 | 60 | 30 | 50 | 5 | 5 | 0 | 60 | **150** | YES |
| V-03 | 60 | 30 | 50 | 5 | 5 | 5 | 65 | **155** | YES |
| V-04 | 60 | 30 | 50 | 5 | 5 | 0 | 60 | **150** | YES |
| V-05 | 60 | 30 | 50 | 5 | 5 | 5 | 65 | **155** | YES |

---

## Ranking

1. **V-03** — 155/155 (single axis: role sequence achieves full ceiling because it builds on V-02 baseline which already had PHASE 3B + PHASE 4B)
1. **V-05** — 155/155 (all-axes combined; structurally identical to V-03 in final form)
3. **V-02** — 150/155 (C-21 miss: declaration in PBI preamble, not independently navigable)
3. **V-04** — 150/155 (same C-21 gap as V-02)
5. **V-01** — 145/155 (C-20 miss: no Rules of Thumb table; C-21 miss: declaration in PBI preamble)

---

## Excellence Signals from V-03 / V-05

**Signal 1 — Section title must name the reviewer's target, not the producer's action.**

"ENFORCEMENT MECHANISM" navigates a reviewer directly to the provenance classification. "PRE-COMMITTED BELIEF INVENTORY" is a producer-action title — it names what's being produced, not what a reviewer seeks. C-21 navigability is a section-title design problem, not a content problem: V-01 has all three C-17 elements but they are invisible from headers.

**Signal 2 — First-position enforcement declaration prevents post-hoc classification bias.**

Placing ENFORCEMENT MECHANISM before the PBI means the provenance claim is committed before any signal content is processed. This is the architectural equivalent of the PBI's own temporal separation: provenance cannot be retrospectively tuned to match content discovered during writing.

**Signal 3 — The three-phase explicit mechanism set is additive and non-interfering.**

ENFORCEMENT MECHANISM (pre-entry), CHAIN INTEGRITY AUDIT (post-gate), RULES OF THUMB (post-hierarchy) fire at lifecycle positions with no shared state. V-04 proves that two of three (PHASE 3B + PHASE 4B) produce 150; V-03 proves that adding the first-position enforcement section achieves 155. The phases compose cleanly.

**Signal 4 — V-03 and V-05 converge: single-axis-against-cumulative-baseline = full-combination.**

V-03 was designed as "single axis: role sequence against V-02 baseline." Because V-02's baseline already contained PHASE 3B (C-19) and PHASE 4B (C-20), V-03's axis addition produced the complete three-mechanism set. V-05, designed as the explicit full combination, is structurally identical to V-03. When variations are built against cumulative baselines, single-axis additions can achieve the full score.

---

## Key R6 Departure from Design Predictions

The design predicted V-01 at 155 ("C-20 PASS at R5 level, C-21 PASS at R5 level"). The actual prompt body for V-01 places the structural provenance declaration in the PBI preamble and omits the Rules of Thumb table entirely. This is structurally weaker for C-21 than R5 V-05 (which had the declaration in CORRECTION ENFORCEMENT Rule 1) and fails C-20 entirely (no table, no RULES-ANCHORED). V-01 scores 145, not 155. This reveals a design assumption error: "no other changes from R5 V-05 structure" was not upheld — the structural provenance preamble was repositioned from CORRECTION ENFORCEMENT into the PBI instructions.

---

```json
{"top_score": 155, "all_essential_pass": true, "new_patterns": ["section-title-navigability: the enforcement mechanism declaration must be in a section whose TITLE signals 'enforcement mechanism classification', not 'entry production' — PRE-COMMITTED BELIEF INVENTORY buries the C-17 content because the header signals producer action, not reviewer target; ENFORCEMENT MECHANISM surfaces it directly from the section list", "first-position-commitment: placing the ENFORCEMENT MECHANISM section before PBI commits the provenance claim before any signal content is processed, preventing retrospective classification bias — the same temporal separation logic that justifies the PBI applies to the provenance declaration itself"]}
```
