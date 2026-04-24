## listen-support Quest Score — Round 6

### Scoring Basis

All five variations inherit R5 V-05 in full. Under rubric v6, R5 V-05 maps to **150 pts** (all 20 criteria C-01 through C-20 pass). C-21 and C-22 are the two new aspirational criteria at 5 pts each, max delta = 10 pts.

---

### Essential Criteria Scan (C-01 through C-05) — All Variations

All five variations carry the complete R5 V-05 mechanism set. The fixed-changes table confirms every essential mechanism is retained unchanged.

| Criterion | All Variations | Evidence |
|-----------|---------------|---------|
| C-01 — Title field on card | PASS (12) | Card template has `Title: [descriptive subject line]` as discrete field in all five |
| C-02 — Controlled vocabulary declared and enforced | PASS (12) | VOCABULARY DECLARATION step present; allowed values table appears in all five |
| C-03 — First-person voice | PASS (12) | "Write as me — first person throughout. No role titles in body text." in STEP 7 of all five |
| C-04 — Gap analysis with three named sections | PASS (12) | GAP ANALYSIS TABLE with minimum 1 Doc, 1 Design, 1 Operational row in all five |
| C-05 — TABLE CHECK gate with halt instruction | PASS (12) | TABLE CHECK block present in STEP 3 of all five; "Do not proceed to STEP 4 until TABLE CHECK shows all items PASS" names the blocked step; Total >= 7 structural |

**all_essential_pass = TRUE for all variations.**

---

### Recommended Criteria (C-06 through C-08)

All five carry the R5 V-05 baseline, which passed recommended criteria. Score contribution: **30 pts** across all variations.

---

### Aspirational Criteria (C-09 through C-20) — Baseline

R5 V-05 established the ceiling for C-09 through C-20. All 12 aspirational criteria below C-21 pass. Score contribution: **60 pts** across all variations.

---

### C-21 — Evidence-to-gap traceability with orphan-gap check

| Variation | Mechanism | Score |
|-----------|-----------|-------|
| V-01 | Gap ID column in Step 9 table; dedicated GAP-TICKET TRACEABILITY TABLE in Step 9B; ORPHAN-GAP CHECK block with explicit halt ("Do not finalize the output if..."). Full two-lookup chain. | **PASS (5)** |
| V-02 | No Gap ID column. No traceability table. No orphan check. Consequence fields added but traceability chain absent. | **FAIL (0)** |
| V-03 | Inline `Supporting ticket(s)` column in gap table; orphan count integrated into GAP COVERAGE + TRACEABILITY CHECK block. No dedicated traceability table — one-lookup only. | **PARTIAL (2)** |
| V-04 | Gap ID column in Step 9; dedicated traceability table in Step 9C; ORPHAN-GAP CHECK with halt. Identical to V-01 mechanism for C-21. | **PASS (5)** |
| V-05 | Gap ID column + inline Supporting ticket(s) column in Step 9 (two inline anchors); dedicated traceability table Step 9C with cross-reference instruction ("Populate Supporting ticket(s) from the STEP 9 table — same values"); ORPHAN-GAP CHECK with halt; FINAL VERIFICATION sub-checks name C-21 explicitly with four YES/NO items. Belt-and-suspenders: inline + dedicated table. | **PASS (5)** |

---

### C-22 — Prohibited sentinel language on consequence fields

| Variation | Mechanism | Score |
|-----------|-----------|-------|
| V-01 | No consequence fields. No sentinel. No SENTINEL COMPLIANCE CHECK. | **FAIL (0)** |
| V-02 | Step 9B: "Prohibited on 'Consequence if unresolved'" block with named disallowed phrases; per-gap narrative fields; SENTINEL COMPLIANCE CHECK with verbatim-quote audit (YES/NO on persona specificity + Day-90 failure + prohibited register); halt if any FAIL. Two-gate structure. | **PASS (5)** |
| V-03 | Inline Prohibited note in gap table column header; orphan/sentinel summary integrated into GAP COVERAGE + TRACEABILITY CHECK block. No dedicated sentinel compliance check block — coverage block carries "Consequence fills using prohibited language: [N] (required: 0)". Single gate, lighter weight. | **PARTIAL (2)** |
| V-04 | Step 9B with Prohibited sentinel + SENTINEL COMPLIANCE CHECK — identical to V-02 mechanism for C-22. | **PASS (5)** |
| V-05 | Inline Prohibited annotation on consequence column in Step 9 header (blocks at generation); Step 9B dedicated consequence fields with full Prohibited list + SENTINEL COMPLIANCE CHECK with verbatim-quote audit; FINAL VERIFICATION sub-checks name C-22 explicitly with four YES/NO items. Two layers: inline prevents, step audits, verification confirms. | **PASS (5)** |

---

### Composite Scores

| Variation | Base (C-01–C-20) | C-21 | C-22 | Composite | all_essential_pass |
|-----------|-----------------|------|------|-----------|-------------------|
| V-01 | 150 | 5 | 0 | **155** | TRUE |
| V-02 | 150 | 0 | 5 | **155** | TRUE |
| V-03 | 150 | 2 | 2 | **154** | TRUE |
| V-04 | 150 | 5 | 5 | **160** | TRUE |
| V-05 | 150 | 5 | 5 | **160** | TRUE |

---

### Ranking

1. **V-05 = 160** — Full synthesis: belt-and-suspenders on both C-21 (inline + dedicated table) and C-22 (inline column prohibition + dedicated Step 9B + sentinel compliance check), plus FINAL VERIFICATION spine naming both criteria by ID. Highest robustness to model compression.
1. **V-04 = 160** — Combined V-01 + V-02: dedicated traceability table (C-21) and dedicated sentinel consequence step (C-22). Clean separation. Slightly lower compression-resistance than V-05 (no inline fallback layer, no FINAL VERIFICATION spine).
3. **V-01 = 155** — C-21 PASS (dedicated traceability), C-22 absent. Single-axis ceiling.
3. **V-02 = 155** — C-22 PASS (sentinel + compliance check), C-21 absent. Single-axis ceiling.
5. **V-03 = 154** — Both PARTIAL. Lightest weight but insufficient for either criterion under strict scoring.

---

### Excellence Signals from V-05

**Pattern 1 — Belt-and-suspenders criterion satisfaction:** For criteria requiring structural verification, embed both an inline column (point-of-generation block) and a dedicated verification step (post-generation audit). If the model drops the dedicated step, the inline column survives and vice versa.

**Pattern 2 — Materialized-view traceability instruction:** Instruct the model to populate the traceability table from the gap table ("same values") rather than re-deriving it. This converts a second-pass generation task into a transcription task, dramatically reducing divergence risk between the two tables.

**Pattern 3 — Criterion-ID-named final verification spine:** A FINAL VERIFICATION block at the end that names every criterion by ID (C-01 through C-22) with explicit YES/NO sub-questions converts the entire prompt into a self-auditing artifact — a scorer can verify criterion satisfaction by reading one block.

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["Belt-and-suspenders criterion satisfaction: embed inline column (generation-time block) plus dedicated verification step (post-generation audit) — two independent paths to same criterion; model compression drops one, the other survives", "Materialized-view traceability: instruct the traceability table to populate from the gap table same values rather than re-derive — converts generation to transcription, eliminates divergence between tables", "Criterion-ID-named final verification spine: terminal FINAL VERIFICATION block names each criterion by ID with YES/NO sub-questions — converts prompt to self-auditing artifact, scorer reads one block to verify all criteria"]}
```
