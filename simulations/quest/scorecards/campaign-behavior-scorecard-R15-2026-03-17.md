Now I have sufficient context. Let me produce the full scorecard.

---

# campaign-behavior — Round 15 Scorecard

**Rubric version:** v13 (denominator 34)
**Baseline:** R14 V-05 (34/34 on v13, all C-40/C-41/C-42 integrated)
**Date:** 2026-03-17

---

## Per-Variation Rubric Evaluation

### Essential Criteria (C-01 – C-05) — all variations

All five R15 variations are built directly on the R14 V-05 baseline. No variation removes or degrades the essential sections.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 (scope census) | PASS | PASS | PASS | PASS | PASS |
| C-02 (findings produced) | PASS | PASS | PASS | PASS | PASS |
| C-03 (spec gaps surfaced/cleared) | PASS | PASS | PASS | PASS | PASS |
| C-04 (contract violations surfaced/cleared) | PASS | PASS | PASS | PASS | PASS |
| C-05 (lifecycle violations surfaced/cleared) | PASS | PASS | PASS | PASS | PASS |

Evidence: CONSOLIDATE section in every variation carries labeled contract-violations, privilege-escalation-paths, and spec-gaps fields; Phase 4 carries combined nominal+exception table plus exception sub-cases table satisfying C-05 for all five.

---

### Recommended Criteria (C-06 – C-08) — all variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 (blast radius label per finding) | PASS | PASS | PASS | PASS | PASS |
| C-07 (confirmation status per finding) | PASS | PASS | PASS | PASS | PASS |
| C-08 (sub-skill attribution per finding) | PASS | PASS | PASS | PASS | PASS |

V-01/V-02/V-04 carry labeled fields 2/3/6 in numbered blocks. V-03/V-05 use pipe cards: `src:[phase]`, `blast:[tier]->[T-NN]`, classification slot in Row 1 — all three recommended fields structurally present.

---

### Aspirational Criteria (C-09 – C-42) — per variation

#### C-09 through C-26 (baseline block — 18 criteria)

All five variations inherit the R14 V-05 baseline without modification to the phase structure, DEFINITIONS vocabulary, calibration questions Q1–Q6, EXECUTIVE SUMMARY format, or CONSOLIDATE ranking. Every criterion from C-09 through C-26 passes across all five variations.

| Criteria | All 5 | Notes |
|----------|-------|-------|
| C-09 F-NN sequential IDs | PASS | Numbered IDs assigned in CONSOLIDATE |
| C-10 lifecycle phase tag | PASS | Phase tag column in Ph4/Ph5 tables |
| C-11 compound findings tracked | PASS | EXIT CRITERIA counts compound anchor hits |
| C-12 spec gap missing-clause citation | PASS | CONSOLIDATE spec-gaps field requires clause citation |
| C-13 contract violations name producer/consumer | PASS | Naming required in violations section |
| C-14 privilege escalation paths | PASS | Dedicated field in CONSOLIDATE |
| C-15 severity with defined scale | PASS | DEFINITIONS defines h/m/l; every finding carries sev: |
| C-16 executive summary top-3 | PASS | EXECUTIVE SUMMARY section present, 3 ranked bullets |
| C-17 evidence basis per CONFIRMED | PASS | Inline citation format enforced in field 6 / card classification slot |
| C-18 calibration questions n≥3 | PASS | Q1–Q8 + QL + QH = 10 in V-01/V-04/V-05; Q1–Q8 + QH = 9 in V-02/V-03 |
| C-19 atomic 7-field block | PASS (V-01/V-02/V-04: numbered) / PASS (V-03/V-05: card) | R14 evidence: card format passed C-09–C-39 (R14 V-03 32/34); card Row 1 carries all 7 logical fields labeled by position |
| C-20 tiebreaker protocol stated | PASS | DEFINITIONS tiebreaker block present; CONSOLIDATE states application |
| C-21 SYSTEMIC findings enumerate phases | PASS | DEFINITIONS enforces "SYSTEMIC: yes -- phases: [list]"; Q3 audits |
| C-22 state-anchor execution order | PASS | Phase 1 header carries [ANCHOR: state topology...] |
| C-23 permissions-anchor before flow | PASS | Phase 2 header carries [ANCHOR: privilege boundary...] |
| C-24 anchor tags on phase headers | PASS | Both Phase 1 and Phase 2 headers have [ANCHOR:...] tags |
| C-25 Q6 sequence integrity gate | PASS | Q6 present, fires post-phases, audits anchor delivery |
| C-26 propagation chain in field 3 | PASS | Format: [origin] -> [component] -> [terminal: T-NN] required in field 3 / blast field |

#### C-27 through C-39 (dual-pipeline + phase coverage block — 13 criteria)

| Criteria | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----------|------|------|------|------|------|-------|
| C-27 terminus registry Phase 0 | PASS | PASS | PASS | PASS | PASS | T-NN table with registry lock in all Phase 0 |
| C-28 dedicated EXECUTIVE SUMMARY | PASS | PASS | PASS | PASS | PASS | Section present with 3-bullet format |
| C-29 inline CONFIRMED citation in field 6 | PASS | PASS | PASS | PASS | PASS | Field 6 / card classification slot template encodes `CONFIRMED -- evidence: [phase]: [finding]` |
| C-30 EXECUTIVE SUMMARY chains use T-NN | PASS | PASS | PASS | PASS | PASS | VALIDITY RULES rule 1 prohibits free-form terminus |
| C-31 EXECUTIVE SUMMARY bullets inline citation | PASS | PASS | PASS | PASS | PASS | VALIDITY RULES rule 2 prohibits plain [CONFIRMED] token |
| C-32 VALIDITY RULES rejection gate | PASS | PASS | PASS | PASS | PASS | Both rules use "INVALID / NOT valid" prohibition language co-located at EXECUTIVE SUMMARY write site |
| C-33 Q7 post-write output gate | PASS | PASS | PASS | PASS | PASS | Q7 fires after EXECUTIVE SUMMARY, before CONSOLIDATE; per-bullet C-30/C-31 status |
| C-34 Q2 extended to preview compliance | PASS | PASS | PASS | PASS | PASS | Q2 explicitly previews EXECUTIVE SUMMARY slot compliance ("Also verify: for any finding entering EXECUTIVE SUMMARY as CONFIRMED...") |
| C-35 registry-lock declaration | PASS | PASS | PASS | PASS | PASS | "Registry locked: [N] terminus entries. Phase execution may begin." present in Phase 0 |
| C-36 per-phase T-NN exit gate | PASS | PASS | PASS | PASS | PASS | All 5 phases carry "[N] chains produced, [N] resolved to T-NN, [N] registry miss" in EXIT CRITERIA |
| C-37 Q8 CONSOLIDATE completeness gate | PASS | PASS | PASS | PASS | PASS | Q8 audits 7-field, T-NN, classification per block before VERDICT |
| C-38 exception sub-tables all trace phases | PASS | PASS | PASS | PASS | PASS | Phases 1, 2, 3, 5 each carry exception path sub-tables |
| C-39 I-NN inertia inventory Phase 0 | PASS | PASS | PASS | PASS | PASS | Numbered I-NN table in Phase 0; Q5 references I-NN codes in forward-verification |

#### C-40 – C-42 (finding structure expansion — 3 criteria)

**C-40 — Field 7 remediation-tier sub-structure with Q8 4th check**

| Variation | Status | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Field 7 template: `spec: [...] \| contract: [...] \| implementation: [...]` in both F-NN and M-NN blocks; Q8 audits 4 dimensions including "Remediation tier check: Field 7 has spec, contract, implementation sub-fields" |
| V-02 | PASS | Same 7-field numbered block inherited from R14 V-05; Field 7 sub-structure and Q8 4th check present |
| V-03 | PASS | Row 2: `rem> spec:[...] \| contract:[...] \| impl:[...]` satisfies three-tier sub-structure; Q8 audits "Row 2 rem> has spec, contract, impl each populated or 'none'" — 4th check dimension confirmed |
| V-04 | PASS | 7-field numbered block; Field 7 and Q8 4th check identical to V-01/V-02 |
| V-05 | PASS | Two-row card Row 2 = `rem> spec:[...] \| contract:[...] \| impl:[...]`; Q8 explicitly audits remediation tier across both rows; DEFINITIONS states "Both card rows required for every finding block (F-NN and M-NN)" |

**C-41 — M-NN meta-finding elevation into EXECUTIVE SUMMARY blast-radius pool**

| Variation | Status | Evidence |
|-----------|--------|----------|
| V-01 | PASS | DEFINITIONS: "M-NN items receive 7-field treatment, are ranked by blast radius in META-FINDINGS, and may appear in EXECUTIVE SUMMARY"; VALIDITY RULES rule 2 covers M-NN token: "M-NN confirmation slot: 'meta-finding: I-NN inventory miss'"; Q8 audits M-NN blocks |
| V-02 | PASS | Same M-NN definition and EXEC SUMMARY pool treatment as V-01; VALIDITY RULES explicitly names M-NN token format |
| V-03 | PASS | DEFINITIONS: "M-NN items receive the same two-row card treatment as F-NN findings and are ranked by blast radius in META-FINDINGS section"; EXEC SUMMARY permits "M-[N]:" prefix; VALIDITY RULES rule 2 covers M-NN token |
| V-04 | PASS | Identical to V-01/V-02 |
| V-05 | PASS | DEFINITIONS: "M-NN items receive the same two-row card treatment as F-NN findings, are ranked by blast radius in META-FINDINGS section, and may appear in EXECUTIVE SUMMARY"; Q8 explicitly audits M-NN blocks with `"meta-finding: I-NN inventory miss"` token check |

**C-42 — H-NN hypothesis pre-declaration with QH outcome gate**

| Variation | Status | Evidence |
|-----------|--------|----------|
| V-01 | PASS | H-NN table in Phase 0; DEFINITIONS states "QH fires between QL and EXECUTIVE SUMMARY"; QH assigns CONFIRMED/REFUTED/NO-EVIDENCE per H-NN; CONSOLIDATE has "Hypothesis outcomes:" section; VERDICT counts H-NN outcomes; QL ordering: Q6 → QL → QH → EXEC SUMMARY |
| V-02 | PASS | H-NN table in Phase 0; DEFINITIONS states "QH fires between Q6 and EXECUTIVE SUMMARY"; three-state QH outcomes; CONSOLIDATE hypothesis outcomes; VERDICT counts |
| V-03 | PASS | H-NN table in Phase 0; DEFINITIONS: "QH fires between Q6 and EXECUTIVE SUMMARY"; three-state QH; CONSOLIDATE hypothesis outcomes; VERDICT H-NN counts |
| V-04 | PASS | H-NN table in Phase 0; DEFINITIONS: "QH fires between QL and EXECUTIVE SUMMARY" (ordering: Q6 → QL → QH → EXEC SUMMARY explicitly in ordering note); three-state QH; CONSOLIDATE and VERDICT coverage |
| V-05 | PASS | Full integration: H-NN table; DEFINITIONS: "QH fires between QL and EXECUTIVE SUMMARY"; QL→QH→EXEC SUMMARY ordering stated in DEFINITIONS; QH explicitly includes QL-sourced findings in coverage ("including QL-sourced findings"); three-state outcomes; CONSOLIDATE hypothesis outcomes; VERDICT counts plus QL note |

---

### Aspirational Totals

| Variation | C-09–C-42 | Passed/34 | Asp score | Total |
|-----------|-----------|-----------|-----------|-------|
| V-01 | 34/34 | 34 | 10 | **90** |
| V-02 | 34/34 | 34 | 10 | **90** |
| V-03 | 34/34 | 34 | 10 | **90** |
| V-04 | 34/34 | 34 | 10 | **90** |
| V-05 | 34/34 | 34 | 10 | **90** |

---

## Ranking

All five R15 variations are built on the R14 V-05 baseline (34/34) and add new axes that are fully additive — no new axis removes or degrades any existing criterion. The v13 rubric ceiling is reached by all five.

| Rank | Variation | Score | Differentiator |
|------|-----------|-------|----------------|
| 1 | V-05 | 90 | Full integration: all three R15 axes compose without interaction degradation; QL source tag explicitly validated in Q8; most complete forcing structure |
| 1 | V-04 | 90 | Two axes (QL + HIGH-RISK) compose cleanly; VERDICT handles QL finding + HIGH-RISK assumption coordination |
| 1 | V-01 | 90 | QL gate self-standing; QL → QH → EXEC SUMMARY ordering clean |
| 1 | V-02 | 90 | HIGH-RISK tier self-standing; VERDICT inertia-lead framing clean |
| 1 | V-03 | 90 | Compact cards self-standing; C-40/C-41/C-42 all pass under card format |

Tiebreaker by integration depth: V-05 > V-04 > V-01 = V-02 = V-03. No rubric criterion differentiates them — all at ceiling.

---

## Excellence Signals

These patterns appear in V-05 (and component variations) that extend beyond the v13 rubric ceiling. They are candidates for v14 criteria.

### Signal 1 — QL concurrent-boundary gate as a named calibration question (V-01, V-04, V-05)

The Phase 4 combined nominal+exception table evaluates each lifecycle transition independently. QL forces cross-row concurrent reasoning — re-entry collisions, recovery-path escalations, cross-phase races — that the table format does not prompt. QL fires between Q6 and QH; QL-sourced findings enter CONSOLIDATE as F-NN blocks tagged `src: flow-lifecycle (QL)`. This creates a new finding attribution class that extends the fixed phase vocabulary. The gate is hypothesis-testable: if QL finds nothing, the table format is sufficient; if QL surfaces findings, the gate is load-bearing. v13 has no criterion for concurrent phase-boundary analysis or for calibration-gate-derived finding attribution.

**Pattern:** Dedicated concurrent-boundary calibration gate firing after Q6 with a named source attribution class for its findings.

### Signal 2 — HIGH-RISK inertia tier in Q5 with VERDICT inertia-lead (V-02, V-04, V-05)

Q5 gains a risk-triage step that classifies I-NN assumptions as HIGH-RISK when (a) wrong implies wide blast AND (b) no spec clause governs the domain. VERDICT opens with "Inertia averted" before naming the top finding — framing the campaign result as "what would have shipped unchallenged" rather than "what we found." This reframing is structurally distinct from the existing I-NN inventory (C-39) and meta-finding elevation (C-41): HIGH-RISK tier operates on declared assumptions, not finding overrides, and changes the narrative opening of VERDICT rather than the ranking of findings. v13 has no criterion for risk-tier classification applied to the I-NN inventory or for inertia-lead VERDICT structure.

**Pattern:** Q5 risk-triage producing HIGH-RISK labels on wide-blast, spec-uncovered I-NN assumptions; VERDICT structured as inertia-averted paragraph followed by top-finding paragraph.

### Signal 3 — QL source tag vocabulary as valid attribution value in Q8 (V-05 interaction)

When QL and compact cards combine (V-05), the Q8 template explicitly declares `"flow-lifecycle (QL)"` as a valid `src:` value in the card Row 1 source field. This is a vocabulary extension: the existing source attribution system names only the five phases (trace-state, trace-permissions, trace-contract, flow-lifecycle, flow-trigger); QL introduces a derived attribution class. V-05's Q8 validates the extended vocabulary, preventing false negatives in the completeness gate. v13 has no criterion for named calibration-gate source attribution or for Q8 vocabulary extension when new calibration questions produce finding-class artifacts.

**Pattern:** Named calibration-gate source attribution class (`"flow-lifecycle (QL)"`) declared in DEFINITIONS and validated as a recognized value in Q8's source field check.

---

## Summary Table

| Variation | Essential (50) | Recommended (30) | Aspirational (10) | Total | All Essential Pass |
|-----------|----------------|------------------|-------------------|-------|--------------------|
| V-01 | 50 | 30 | 10 | **90** | YES |
| V-02 | 50 | 30 | 10 | **90** | YES |
| V-03 | 50 | 30 | 10 | **90** | YES |
| V-04 | 50 | 30 | 10 | **90** | YES |
| V-05 | 50 | 30 | 10 | **90** | YES |

All five at ceiling. v13 rubric is saturated. R15 excellence signals (QL gate, HIGH-RISK tier, source-tag vocabulary extension) are candidates for v14 criteria C-43 through C-45.

---

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["QL concurrent-boundary gate between Q6 and QH forces cross-row concurrent phase reasoning not prompted by Phase 4 table; QL-sourced findings enter CONSOLIDATE tagged src: flow-lifecycle (QL) as a named attribution class", "HIGH-RISK inertia tier in Q5 classifies wide-blast, spec-uncovered I-NN assumptions; VERDICT opens with inertia-averted paragraph before top finding, reframing campaign from what-we-found to what-would-have-shipped-unchallenged", "Q8 source-field vocabulary extended to recognize flow-lifecycle (QL) as a valid src: value in card Row 1, preventing false negatives when calibration-gate-derived findings enter the completeness gate"]}
```
