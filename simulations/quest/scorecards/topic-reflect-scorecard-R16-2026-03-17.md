## quest:score — topic-reflect, Round 16

**Note:** Only V-01 was present in the input. V-02 through V-05 are absent. Scoring V-01 against v14 rubric.

---

## V-01 — Scoring Detail

**Axis:** Named invariant cross-reference namespace (C-34) + DEFINITION formal elements per stage (C-35)

---

### Essential — 54 / 60

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** (12) | INVARIANT V-1 requires B-# on every entry; COMMIT-ENTRY gate checks it; calibration entry models "What We Expected (B-2)"; Stage 2 scans only for contradictions; deviation routing through adversarial gate ensures at least one contradicts |
| C-02 | **PARTIAL** (6) | Stage 1 complete — B-# beliefs, dimensions, confidence, Epistemic Profile all required ✓. Stage 6: DEFINITION present ("verdict table plus foreknowledge final stance") and ENTER condition present, but procedural content ends at "For each B-# belief from Stage 1:" — verdict table format, COHERENT/CONTRADICTORY/FOREKNOWLEDGE-FLAGGED labels, revision direction instruction, EXIT criterion, and COMMIT-STAGE-6 are all absent from the visible text. Stage 6 is structurally begun but unpublished. |
| C-03 | **PASS** (12) | INVARIANT V-2 names 6 prohibited phrases; COMMIT-ENTRY gate enforces; Field Reference consolidates; calibration entry models correct format |
| C-04 | **PASS** (12) | FIELD REFERENCE prohibits "the system / the design / the architecture"; COMMIT-ENTRY gate includes Design Impact specificity check with corrective action; calibration entry demonstrates component-level specificity |
| C-05 | **PASS** (12) | Stage 3 five-check table present; VALID/INVALID verdict assigned per deviation; GATE-CONFIRMED-[N] and GATE-REJECTED-[N] tokens emitted per row |

---

### Recommended — 30 / 30

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** (10) | INVARIANT V-3 declares canonical set; Stage 1 EXIT cites V-3 mapping with correction instruction; Stage 4 EXIT rescans and corrects before COMMIT-STAGE-4 |
| C-07 | **PASS** (10) | Gate map: "Fewer than 2 GATE-CONFIRMED entries → SWEEP-EXTENDED"; Entry loop repeats same instruction for borderline GATE-REJECTED rows |
| C-08 | **PASS** (10) | Stage 5 requires named skill (e.g., `/trace-permissions`, `/scout-feasibility`) or named role — explicitly prohibits "investigate further" or "the team"; Stage 5 EXIT enforces |

---

### Aspirational — 128 / 135

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** (5) | Gate map enumerates COMMIT-STAGE-1 through COMMIT-STAGE-7; GATE-CONFIRMED-[N] routes to Stage 4; COMMIT-ENTRY per-row in entry loop |
| C-10 | **PARTIAL** (3) | Stage 3 issues COMMIT-STAGE-3-FLAGGED with B-# identification ✓; Gate map references FOREKNOWLEDGE-FLAGGED at Stage 7 halt ✓; Stage 6 DEFINITION references "foreknowledge final stance" ✓ — but Stage 6's procedural instructions are absent, so the explicit "record CLEAR or FLAGGED" instruction with responsible belief naming is not present as a runtime directive. Partial credit for structural scaffolding; Stage 6 incompleteness blocks full pass. |
| C-11 | **PASS** (5) | "Format as a prose block with labeled sub-fields. Do not use a table." ✓; calibration entry is prose with labeled sub-fields ✓ |
| C-12 | **PASS** (5) | Signal Source requires "name, namespace, and/or date" with named artifact; Design Impact requires named component/API/flow/decision; COMMIT-ENTRY enforces both; calibration entry demonstrates full-sentence values |
| C-13 | **PASS** (5) | INVARIANT V-3 declared as a standalone section: "The only valid epistemic dimension names are: Feasibility · Usability · Scalability · Adoptability · Correctness. Do not substitute." — not embedded in Stage 1 prose |
| C-14 | **PASS** (5) | Stage 3: "Foreknowledge evaluation" issues COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED; gate map confirms binary token pair; gate map shows Stage 4 blocked for GATE-REJECTED rows |
| C-15 | **PASS** (5) | GATE SEQUENCE MAP table present before Stage 1; lists all 8 stages with emitted token and halt condition |
| C-16 | **PASS** (5) | Surprise 0 present with `topic-readiness-rubric-v3-2026-01-14.md` (name, namespace, date) in Signal Source; Design Impact names `assess()` method in topic evaluator module |
| C-17 | **PASS** (5) | INVARIANT V-3 names 6 prohibited synonyms: Reliability, Performance, Complexity, Maintainability, Discoverability, Robustness |
| C-18 | **PASS** (5) | 6 explicit mappings: Reliability → Correctness, Performance → Scalability, Complexity → Correctness, Maintainability → Correctness, Discoverability → Usability, Robustness → Correctness |
| C-19 | **PASS** (5) | Stages 1, 2, 3, 4, 5 all have explicit ENTER conditions and EXIT criteria; Stage 6 has ENTER but EXIT is in the absent section — 5 complete contracts, well above threshold of 3 |
| C-20 | **PASS** (5) | "Surprise 0" label; positioned between FIELD REFERENCE and ENTRY LOOP within Stage 4 structure; format identical to live entry template |
| C-21 | **PASS** (5) | Stage 1 EXIT: "correct any violations before proceeding" citing INVARIANT V-3 ✓; Stage 4 EXIT: "Scan all dimension names used — correct any malformed names using the INVARIANT V-3 mapping before proceeding" ✓ |
| C-22 | **PASS** (5) | FIELD REFERENCE defines Build Risk as labeled sub-field; "a different component, dependency, or contract that could fail or require rework"; modeled in Surprise 0 with `/quest-score` skill as named component |
| C-23 | **PASS** (5) | Design Impact: `assess()` method in topic evaluator module (forward-looking change surface) ✓; Build Risk: `/quest-score` rubric weighting assumptions invalidated (different component, implication of the change) ✓; conceptually distinct, non-redundant, paired |
| C-24 | **PASS** (5) | COMMIT-ENTRY gate: "Build Risk distinction: Names a different component/contract from Design Impact — not a paraphrase, not a general risk category. → If same or generic: identify the downstream dependency that could break before emitting." ✓ |
| C-25 | **PASS** (5) | All four fields covered by ≥2 mechanisms: What We Expected — (Surprise 0, COMMIT-ENTRY gate, INVARIANT V-1 citation); Signal Source — (Surprise 0, COMMIT-ENTRY gate, INVARIANT V-2 citation); Design Impact — (Surprise 0, COMMIT-ENTRY gate); Build Risk — (Surprise 0, COMMIT-ENTRY gate) |
| C-26 | **PASS** (5) | Field Reference: "*Paired formula:* Design Impact names what must change; Build Risk names what is implicated by that change — a different component, dependency, or contract that could fail." ✓ |
| C-27 | **PASS** (5) | Three anchors present: (a) "*Purpose:* Names what is implicated by the change required in Design Impact." (b) "*Paired formula:* Design Impact names what must change; Build Risk names what is implicated…" (c) "*Structural gloss:* One field is forward-looking (what to update); the other is risk-surface (what could break because of that update). They name different parts of the system." |
| C-28 | **PASS** (5) | COMMIT-ENTRY renders as four ✓ bullets; each bullet has gate condition and inline corrective action ("→ If missing: rewrite…", "→ If prohibited phrase detected: replace…", "→ If too generic: drill…", "→ If same or generic: identify…") |
| C-29 | **PASS** (5) | "### FIELD REFERENCE" section with header "Consult this block before entering the entry loop. All four sub-field definitions are consolidated here." — positioned before CALIBRATION ENTRY and ENTRY LOOP; all four fields defined ✓ |
| C-30 | **PASS** (5) | "Surprise 0 *(Calibration Entry — not a live entry; live entries begin at Surprise 1)*" — exact language from pass condition; live/example boundary made explicit at the entry |
| C-31 | **FAIL** (0) | Stage 7 appears only in the GATE SEQUENCE MAP row — no "## STAGE 7" section exists with its own ENTER condition, EXIT criterion, and COMMIT-STAGE-7 token as discrete structural content. Pass condition explicitly excludes "merely a row in the gate overview table." |
| C-32 | **PASS** (5) | INVARIANT V-2 names 6 prohibited phrases: "multiple sources," "the signals," "various artifacts," "several signals," "the namespace," "the data" ✓; Field Reference repeats 5 of them ✓ |
| C-33 | **PASS** (5) | FIELD REFERENCE: "**What We Expected (B-[#]):** … This is the first labeled sub-field of every entry." ✓; Surprise 0 demonstrates with "(B-2)" ✓; COMMIT-ENTRY: "contains a full sentence referencing a specific B-# from Stage 1 → If missing: rewrite as 'We expected that… (B-[#])'" ✓ |
| C-34 | **PASS** (5) | INVARIANT NAMESPACE section declares V-1 (Belief Traceability), V-2 (Signal Source Specificity), V-3 (Dimension Vocabulary); Stage 2 cites "INVARIANT V-1" and "INVARIANT V-2" by identifier; Stage 3 check 4 cites "INVARIANT V-2"; COMMIT-ENTRY gate: "✓ INVARIANT V-1 (Belief Traceability):" and "✓ INVARIANT V-2 (Signal Source Specificity):" — enforcement by citation, not restatement ✓ |
| C-35 | **PASS** (5) | All six stages have DEFINITION blocks positioned before ENTER/procedure: Stage 1 "Opening Model," Stage 2 "Deviation Record," Stage 3 "Gate Verdict," Stage 4 "Surprise Entry," Stage 5 "Cluster Map," Stage 6 "Symmetric Verdict" — each names the typed artifact before any procedural instruction |

---

## Score Summary

| Tier | Score | Max |
|------|-------|-----|
| Essential | 54 | 60 |
| Recommended | 30 | 30 |
| Aspirational | 128 | 135 |
| **Total** | **212** | **225** |

**All essential pass:** No (C-02 PARTIAL — Stage 6 procedural content absent)

---

## Ranking

Only V-01 provided.

| Rank | Variation | Score | All Essential |
|------|-----------|-------|---------------|
| 1 | V-01 | 212/225 | No |

---

## Excellence Signals

V-01 demonstrates clean execution on both new rubric axes:

**C-34 (PASS):** The INVARIANT NAMESPACE pattern works structurally — invariants declared at the top before the gate map, each carrying a semantic label, and downstream stages cite by number and name simultaneously ("✓ INVARIANT V-1 (Belief Traceability)"). The COMMIT-ENTRY gate is the most valuable citation point: it creates an auditable compliance surface at the exact moment of token emission.

**C-35 (PASS):** DEFINITION blocks with "typed artifact" framing per stage are present and clean. The pattern of separating artifact typing from procedural construction is consistent across all six visible stages.

**Primary gap:** Stage 6 is unpublished. The DEFINITION and ENTER condition exist, but all procedural content (verdict table format, COHERENT/CONTRADICTORY/FOREKNOWLEDGE-FLAGGED label declaration, revision direction instruction, EXIT, COMMIT-STAGE-6) is absent. This cascades to C-02 (PARTIAL), C-10 (PARTIAL), and C-31 (FAIL — Stage 7 has no structural complement to Stage 6's verdict table).

**No new patterns** emerge that are not already captured by v14's criterion set.

---

```json
{"top_score": 212, "all_essential_pass": false, "new_patterns": []}
```
