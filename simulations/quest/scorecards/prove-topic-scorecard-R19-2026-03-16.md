Now I have all five variations and the complete rubric. Let me score them.

---

# prove-topic — Quest Score R19 (rubric v14)

**Skill**: prove-topic | **Round**: R19 | **Rubric**: v14 | **Date**: 2026-03-16

---

## Rubric Reference

| ID | Description | Weight |
|----|-------------|--------|
| C-01 | All five sub-skills orchestrated in sequence | essential |
| C-02 | Scout artifact loaded and named before hypothesis | essential |
| C-03 | Progressive artifact writes — one per stage | essential |
| C-04 | Synthesis explicitly signals readiness for topic-story | essential |
| C-05 | Artifact paths named on every write instruction | essential |
| C-06 | Forward-only stage order with gate block | recommended |
| C-07 | Scout anchor in hypothesis artifact (not just preamble) | recommended |
| C-08 | Evidence gaps flagged at point of discovery | recommended |
| C-09 | Thin-evidence propagates to synthesis with confidence qual. | aspirational |
| C-10 | Hypothesis structurally blocked until scout confirmation | aspirational |

Formula: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)`
Golden threshold: all 5 essential PASS **and** composite ≥ 80.

---

## V-01 — Output Format (Tables → Inline Blocks)

**Axis**: tables replaced with inline `key: value` blocks and numbered lists.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS** | All five stages present in order: S1 hypothesis → S2 websearch → S3 interview → S4 prototype → S5 synthesis. Clear stage headers with entry conditions. |
| C-02 | **PASS** | ROLE B names `{topic}-scout-record-{date}.md` in CAMPAIGN OPEN. Stage 1 body: `source_scout_artifact: [path from ROLE B — copied, not inferred]`. Named before hypothesis forms. |
| C-03 | **PASS** | Write instruction at every stage: S1 `{topic}-hypothesis-{date}.md`, S2 `{topic}-websearch-{date}.md`, S3 `{topic}-interview-{date}.md`, S4 `{topic}-prototype-{date}.md`, S5 two artifacts. No batching. |
| C-04 | **PASS** | `topic_story_readiness: "Evidence brief complete. Displacement case: [value]. Confidence: [value]. Ready for /topic-story."` Names topic-story explicitly. |
| C-05 | **PASS** | Every write instruction includes full `{topic}-{signal}-{date}.md` pattern, not prefix-only. |
| C-06 | **PASS** | STAGE 0 clearance check with three steps; ROLE B enforces `gate_s_cleared: [true if scout_loaded; CAMPAIGN BLOCKED otherwise]`. Scout presence is a required condition. |
| C-07 | **PASS** | `source_scout_artifact` field is in Stage 1 body (written to hypothesis artifact), not only in campaign preamble. |
| C-08 | **PARTIAL** | Per-source INCUMBENT CHECK verdicts and running null tally track CE absence, but no explicit "flag thin evidence" instruction at discovery. Stage verdict summary present but doesn't name evidence quality gap. |
| C-09 | **PARTIAL** | ATOMIC DUAL-LOCK applies null cap and adversarial review when `null_tally_final >= 3`, propagating weakness. But synthesis doesn't name which specific finding weakens which specific claim. |
| C-10 | **PASS** | STAGE 0 Step 2 (`gate_s_cleared`, ROLE B required) structurally blocks advance. STAGE 1 entry conditions require `gate_open` from Stage 0. `CAMPAIGN BLOCKED` if scout not loaded. |

**Essential pass**: 5/5 | **Recommended pass**: 2/3 (C-08 PARTIAL) | **Aspirational pass**: 1/2 (C-09 PARTIAL)

**Composite**: `(5/5 × 60) + (2/3 × 30) + (1/2 × 10)` = 60 + 20 + 5 = **85**
**Golden**: YES — all 5 essential PASS, 85 ≥ 80.

---

## V-02 — Inertia Framing (Displacement Thesis as Narrative Lead)

**Axis**: DISPLACEMENT THESIS block before roles; STAGE DISPLACEMENT QUESTION at S2/S3/S4; synthesis leads with `displacement_conclusion`.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS** | Five stages in order. STAGE DISPLACEMENT QUESTIONs are lead lines, not stage reorganization. |
| C-02 | **PASS** | ROLE B names scout artifact in ROLE OWNERSHIP TABLE. Stage 1 adds `displacement_context` field plus `source_scout_artifact: [path from ROLE B — not inferred]`. Strengthened over baseline. |
| C-03 | **PASS** | Write instruction at each stage with named paths. |
| C-04 | **PASS** | `topic_story_readiness: "Displacement case for {topic} over {comparator}: [value]. Evidence brief ready for /topic-story."` Names topic-story. |
| C-05 | **PASS** | Full `{topic}-{signal}-{date}.md` on every write instruction. |
| C-06 | **PASS** | STAGE 0 CLEARANCE TABLE adds Step 4 `displacement_thesis_filed`. Scout presence still enforced via ROLE B. Forward-only. |
| C-07 | **PASS** | Stage 1 has `source_scout_artifact` + new `displacement_context` field in hypothesis artifact. Richer anchor than baseline. |
| C-08 | **PASS** | STAGE DISPLACEMENT QUESTION leads each evidence stage. Per-stage verdict fields `s{N}_stage_displacement_verdict: [SUPPORTING / MIXED / OPPOSING]` create an explicit at-stage flag when evidence is mixed or opposing. Satisfies "flags it at that stage." |
| C-09 | **PARTIAL** | BLOCK 3 adds `displacement_per_stage: S2=[v], S3=[v], S4=[v]` — names source stages. `evidence_summary` covers "confidence trajectory." But no explicit "Finding X in Stage N weakens claim Y" statement — aggregate rather than specific. |
| C-10 | **PASS** | STAGE 0 Step 2 `gate_s_cleared` structurally blocks Stage 1. |

**Essential pass**: 5/5 | **Recommended pass**: 3/3 | **Aspirational pass**: 1/2 (C-09 PARTIAL)

**Composite**: `(5/5 × 60) + (3/3 × 30) + (1/2 × 10)` = 60 + 30 + 5 = **95**
**Golden**: YES — all 5 essential PASS, 95 ≥ 80.

---

## V-03 — Lifecycle Emphasis (Compressed S0–S4, Expanded S5)

**Axis**: Stage 0 compressed to checklist; Stages 1–4 to essential fields only; Stage 5 expanded with per-block entry conditions, intermediate compute steps, `chain_integrity_check`.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS** | All five stages present in order with stage headers. Compression doesn't remove stages. |
| C-02 | **PASS** | ROLE B: `scout_artifact = [{topic}-scout-record-{date}.md]`. Stage 1: `source_scout_artifact: [path from ROLE B]`. Named before hypothesis. |
| C-03 | **PASS** | Write instruction at every stage. Compressed format retains per-stage write with named paths. |
| C-04 | **PASS** | `topic_story_readiness: "Evidence brief complete. Hypothesis [value]. Displacement: [value]. Confidence: [value]. All five stage artifacts written. Ready for /topic-story."` Most informative readiness signal of all five variations. |
| C-05 | **PASS** | Full `{topic}-{signal}-{date}.md` on every write instruction despite compression. |
| C-06 | **PASS** | STAGE 0 (compressed) still enforces: `[ ] gate_s_cleared = true (ROLE B)`. "CAMPAIGN BLOCKED at item [N]" if false. Scout presence required. |
| C-07 | **PASS** | Stage 1 retains `source_scout_artifact: [path from ROLE B]` in body, written to hypothesis artifact. |
| C-08 | **PARTIAL** | Compressed stages 2–4 don't add per-stage displacement verdict fields. `s2_ce_verdict` and null tally track CE absence but not stage-level evidence quality. No STAGE DISPLACEMENT QUESTION. Evidence gaps captured only in synthesis via BLOCK 2 open_risk counts. |
| C-09 | **PARTIAL** | BLOCK 1 `chain_integrity_check` catches running-confidence discrepancies. BLOCK 2 has `refuted_count` / `partially_refuted_count` / `open_risk_count`. BLOCK 3 Step 4 adds `incumbent_defense_closed` with `closure_basis` (cites S2/S3/S4 summaries). Closer to full C-09 than V-01 but still aggregate. |
| C-10 | **PASS** | STAGE 0 gate must clear (`gate_s_cleared = true`) before Stage 1 runs. "CAMPAIGN BLOCKED at item [N]." |

**Essential pass**: 5/5 | **Recommended pass**: 2/3 (C-08 PARTIAL) | **Aspirational pass**: 1/2 (C-09 PARTIAL)

**Composite**: `(5/5 × 60) + (2/3 × 30) + (1/2 × 10)` = 60 + 20 + 5 = **85**
**Golden**: YES — all 5 essential PASS, 85 ≥ 80.

---

## V-04 — Output Format + Inertia Framing (combined)

**Axes**: V-01 inline format + V-02 displacement thesis.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS** | Five stages in order. Inline format preserves stage structure. |
| C-02 | **PASS** | ROLE B inline with scout_artifact named. Stage 1: `source_scout_artifact` + `displacement_context`. Named before hypothesis. |
| C-03 | **PASS** | Write instruction at each stage with named paths. |
| C-04 | **PASS** | `topic_story_readiness: "Displacement case for {topic} over {comparator}: [value]. Hypothesis: [value]. Confidence: [value]. Ready for /topic-story."` |
| C-05 | **PASS** | Full `{topic}-{signal}-{date}.md` per write instruction. |
| C-06 | **PASS** | STAGE 0 clearance check: Steps 1–4 including `displacement_thesis_filed`. Scout via ROLE B. Forward-only. |
| C-07 | **PASS** | `source_scout_artifact` + `displacement_context` in Stage 1 body (hypothesis artifact). |
| C-08 | **PASS** | STAGE DISPLACEMENT QUESTION at S2/S3/S4. Per-stage verdict fields `s{N}_stage_displacement_verdict`. Flags evidence direction at discovery. Same mechanism as V-02. |
| C-09 | **PARTIAL** | BLOCK 3 has `displacement_per_stage`, `incumbent_defense_closed`. `evidence_summary` references confidence trajectory. Aggregate tracing, not per-finding claim identification. |
| C-10 | **PASS** | STAGE 0 Step 2 `gate_s_cleared` required. STAGE 1 entry condition: `gate_open`. CAMPAIGN BLOCKED if scout absent. |

**Essential pass**: 5/5 | **Recommended pass**: 3/3 | **Aspirational pass**: 1/2 (C-09 PARTIAL)

**Composite**: `(5/5 × 60) + (3/3 × 30) + (1/2 × 10)` = 60 + 30 + 5 = **95**
**Golden**: YES — all 5 essential PASS, 95 ≥ 80.

---

## V-05 — Full Integration (All Three Axes + Complete Structural Stack)

**Axes**: V-01 + V-02 + V-03 + full R19 baseline.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS** | Five stages in order. Compressed setup stages don't alter sequence; expanded Stage 5 doesn't create a new stage. |
| C-02 | **PASS** | ROLE B inline: `scout_artifact: [{topic}-scout-record-{date}.md]`. Stage 1: `source_scout_artifact: [path from ROLE B — not inferred]` + `displacement_context`. Named before hypothesis. |
| C-03 | **PASS** | Write instruction at every stage with full paths. S5 writes two artifacts (`synthesis` + `handoff`). Confirmed at stage close. |
| C-04 | **PASS** | `topic_story_readiness: "Displacement case: [value]. Hypothesis [value]. Confidence [value]. Five stage artifacts written. Evidence brief ready for /topic-story."` Richest readiness signal. Stage 5 EXIT SIGNAL also names `incumbent_defense_closed` and "Five stage artifacts on disk." |
| C-05 | **PASS** | Full `{topic}-{signal}-{date}.md` pattern on every write instruction; inline format doesn't compromise path specificity. |
| C-06 | **PASS** | STAGE 0 (compressed) checklist: `[ ] gate_s_cleared = true (ROLE B)`, `[ ] displacement_thesis_filed = true`, others. "CAMPAIGN BLOCKED at item [N]" enforced. |
| C-07 | **PASS** | Stage 1 body includes `source_scout_artifact` + `displacement_context` written to hypothesis artifact. `counter_hypothesis` note: "grounds BLOCK 2 resolution" — explicit downstream linkage. |
| C-08 | **PASS** | STAGE DISPLACEMENT QUESTION at S2/S3/S4. Per-stage `s{N}_stage_displacement_verdict: [SUPPORTING / MIXED / OPPOSING]` fields flag evidence direction at discovery. Combines V-02's displacement framing with V-03's compressed structural discipline. |
| C-09 | **PARTIAL** | BLOCK 1 `chain_integrity_check` reconciles running confidence before synthesis. BLOCK 3 Step 2: `displacement_per_stage: S2=[v], S3=[v], S4=[v]` names source stages. BLOCK 3 Step 3: `closure_basis: [cite S2, S3, S4 incumbent check summaries]` most explicit tracing of stage findings. `key_risk` framed as "residual incumbent strength from incumbent_vulnerability analysis." Closest approach to C-09 full pass — all structural ingredients present but no explicit "Finding X weakens Claim Y" sentence. |
| C-10 | **PASS** | STAGE 0 compressed gate: `[ ] gate_s_cleared = true (ROLE B)` — BLOCKED if false. Stage 1 entry: "Skip if RESUME-SKIP" with overall structural rule that no stage body begins until entry conditions confirm. Dual-path blocking (gate_s_cleared + RESUME AUDIT). |

**Essential pass**: 5/5 | **Recommended pass**: 3/3 | **Aspirational pass**: 1/2 (C-09 PARTIAL)

**Composite**: `(5/5 × 60) + (3/3 × 30) + (1/2 × 10)` = 60 + 30 + 5 = **95**
**Golden**: YES — all 5 essential PASS, 95 ≥ 80.

---

## Variation Rankings

| Rank | Variation | Score | Golden | Differentiator |
|------|-----------|-------|--------|----------------|
| 1 | **V-05** | 95 | YES | All three axes + full stack; richest Stage 5; `chain_integrity_check`; `closure_basis` for C-09 tracing |
| 2 | **V-04** | 95 | YES | V-01 + V-02 combined; matches V-05 numerically; weaker Stage 5 |
| 2 | **V-02** | 95 | YES | First to unlock C-08 via STAGE DISPLACEMENT QUESTION; tabular format only |
| 4 | **V-01** | 85 | YES | Baseline; format-only axis; C-08 PARTIAL blocks recommended tier |
| 4 | **V-03** | 85 | YES | Best Stage 5 mechanics but no displacement framing → C-08 PARTIAL |

---

## Excellence Signals (from V-05)

**Signal 1 — Stage displacement question as C-08 unlocking mechanism.** Adding a labeled `STAGE DISPLACEMENT QUESTION` at S2/S3/S4 and requiring a per-stage verdict field `s{N}_stage_displacement_verdict: [SUPPORTING / MIXED / OPPOSING]` converts implicit evidence assessment into an explicit at-stage flag. This is the minimum structural addition needed to move C-08 from PARTIAL to PASS, and it appears in V-02/V-04/V-05.

**Signal 2 — `displacement_per_stage` in BLOCK 3 chains evidence into synthesis.** Recording `displacement_per_stage: S2=[v], S3=[v], S4=[v]` at BLOCK 3 creates a named provenance chain from per-stage verdicts to the final `displacement_conclusion`. This is the structural precursor to fully satisfying C-09 (which still needs explicit "Finding X weakens Claim Y" language to clear fully).

**Signal 3 — Per-block entry conditions and `chain_integrity_check` in expanded Stage 5.** V-03/V-05 add explicit BLOCK 1/2/3 entry conditions and a `chain_integrity_check` step that verifies `running_confidence` at Stage 4 close matches the reconstructed chain sum. This guards against confidence drift across a multi-stage campaign and is the correct structural pattern for a long-running orchestration skill. `closure_basis` citing S2/S3/S4 summaries is the closest approach yet to satisfying C-09.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["STAGE DISPLACEMENT QUESTION at each evidence stage with per-stage verdict field (SUPPORTING/MIXED/OPPOSING) unlocks C-08 by creating an explicit at-stage evidence quality flag", "displacement_per_stage field in BLOCK 3 chains per-stage verdicts into synthesis creating a named provenance trail that is the structural precursor to C-09 full pass", "Per-block entry conditions with chain_integrity_check in expanded Stage 5 prevents confidence drift and produces the richest synthesis_complete exit signal recognizable to topic-story"]}
```
