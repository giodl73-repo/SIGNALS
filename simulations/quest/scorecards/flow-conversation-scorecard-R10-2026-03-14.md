# Scorecard — flow-conversation — Round 10 (v9 rubric)

**Date:** 2026-03-15 | **Rubric version:** v9 | **Max score:** 136

---

## Scoring Matrix

### Essential Criteria (60 pts)

| ID | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|--------|------|------|------|------|------|
| C-01 Dialog path as turns | 15 | PASS | PASS | PASS | PASS | PASS |
| C-02 All four defect classes | 15 | PASS — all 7 classes including the 4 essential | PASS | PASS | PASS | PASS |
| C-03 Session state tracked | 15 | PASS — derived from Phase 1-S replay | PASS | PASS | PASS — same mutation-first | PASS |
| C-04 Copilot Studio framing | 15 | PASS — vocabulary gate signed | PASS | PASS | PASS — CS_VOCABULARY_BINDING + PROHIBITED_TERMS | PASS |

**Essential subtotal:** V-01/V-02/V-03/V-04/V-05 = 60/60 each

---

### Recommended Criteria (30 pts)

| ID | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|--------|------|------|------|------|------|
| C-05 Defect reproduction steps | 10 | PASS — Phase 3 | PASS | PASS | PASS | PASS — Step 11 |
| C-06 Fallback chain coverage | 10 | PASS — Phase 4 | PASS | PASS | PASS | PASS — Step 14 |
| C-07 Intent collision disambiguation | 10 | PASS — Phase 4 conditional | PASS | PASS | PASS | PASS — Step 14 |

**Recommended subtotal:** 30/30 each

---

### Aspirational Criteria (46 pts)

| ID | Weight | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|--------|------|------|------|------|------|-------|
| C-08 Graph coverage metric | 1 | PASS | PASS | PASS | PASS | PASS | All four ratios with fractions |
| C-09 Adversarial turn injection | 1 | PASS — Phase 6 with Phase 1-S entries | PASS | PASS | PASS | PASS — Step 15 |
| C-10 Prohibited vocabulary gate | 1 | PASS — 0-D-2 VOCABULARY_GATE: SIGNED | PASS | PASS | PASS — PROHIBITED_TERMS declared | PASS — gate signed Step 1 |
| C-11 Turn-level conformance verdict | 1 | PASS — CONFORMANCE column every row | PASS | PASS | PASS | PASS — + CONSTRAINT_VERDICTS per turn |
| C-12 Topic graph pre-declaration | 1 | PASS — 0-D-1 with CONTRACT_GAP | PASS | PASS | PASS — 0-A-1 (Architect) | PASS — Step 1 |
| C-13 Session variable registry | 1 | PASS — 0-D-3 PERSISTENCE_CLASS | PASS | PASS | PASS — 0-A-1 includes vars | PASS — Step 3 |
| C-14 Invariant register | 1 | PASS — 0-D-4 INVARIANT-TOPO-NN/SV-NN | PASS | PASS | PASS — 0-A-7 | **PARTIAL** — CONV-NN in Step 5 substitutes structurally but no Phase 0-D-4 block |
| C-15 Escalation path traced | 1 | PASS | PASS | PASS | PASS | PASS |
| C-16 Phase 0 pre-execution contract | 1 | PASS — Phase 0-D block seals before Phase 1 | PASS | PASS | PASS — Phase 0-A + 0-D separate but both pre-trace | **PARTIAL** — Steps 1–6 serve the function but no explicit Phase 0 block or PHASE_0_CONTRACT: SEALED marker |
| C-17 Developer/Auditor role separation | 1 | PASS — [ROLE_COMPLETE] gates, no retroactive alteration | PASS | PASS | PASS — 4-role chain, stronger isolation | PASS |
| C-18 Slot-fill path tracking | 1 | PASS — 0-D-7 SLOT_PATH_MAP + SLOT_PATH_ID | PASS | PASS | PASS | PASS — Step 4 + Step 7 SLOT_PATH_ID |
| C-19 Orphaned topic detection | 1 | PASS — 0-D-6 ORPHANED list; in coverage denominator | PASS | PASS | PASS — 0-A-2 | PASS — Step 2 orphans logged before trace |
| C-20 Recovery verdict classification | 1 | PASS — RECOVERABLE/UNRECOVERABLE/MASKED_BY forms | PASS | PASS | PASS | PASS |
| C-21 Severity co-residency audit | 3 | PASS — Phase 6-B structured table | PASS | PASS | PASS | PASS — Audit 3 adds CONV_VIOLATIONS_PRESENT column |
| C-22 Transition completeness map | 3 | PASS — 0-D-5 TRANSITION_MAP + coverage ratio | PASS | PASS | PASS — 0-A-3 (Architect) | PASS — Step 2 edges numbered TRANS-NN |
| C-23 Defect entanglement analysis | 3 | PASS — Phase 3-E + Phase 6-C | PASS | PASS | PASS | PASS — Step 12 + Audit 1 indirectly |
| C-24 Topic-indexed trace aggregation | 4 | PASS — Phase 1-T + C-28 gate present | PASS | PASS | PASS — Phase 1-T + 6-D | PASS — Step 9 + Audit 4 |
| C-25 Session variable timeline contract | 4 | PASS — 0-D-8 sealed at Phase 0 close | PASS — 0-D-8 | PASS — 0-D-8 | **PASS+** — 0-A-6 adds AUTHORIZED_REWRITERS; Contract Auditor verifies completeness before trace | PASS — Step 3 lifecycle |
| C-26 Session timeline mutation log | 4 | **PASS+** — Phase 1-S authored FIRST; SESSION_STATE derived from replay | PASS — additive after Phase 1 | PASS — additive after Phase 1 | **PASS+** — mutation-first same as V-01 | PASS — Step 8, additive; CONV_01_EVIDENCE arithmetic check |
| C-27 Timeline anomaly defect class | 4 | PASS — 4th coverage ratio in Phase 5 | PASS | **PASS+** — Phase 5-A COVERAGE_QUALITY_GATE: CLEAN/DEGRADED; downstream ratios marked PROVISIONAL | PASS | PASS |
| C-28 Phase 6-D topic aggregate consistency audit | 4 | PASS — Phase 6-D | PASS | PASS | PASS | PASS — Audit 4 |
| C-29 Phase 6-E session timeline consistency audit | 4 | **PASS+** — Phase 6-E present; mutation-first makes TIMELINE_STATE_MISMATCH structurally impossible | PASS — Phase 6-E | PASS — Phase 6-E | **PASS+** — same mutation-first guarantee + Auditor verifies AUTHORIZED_REWRITERS compliance | PASS — Audit 4, CONV_01_EVIDENCE closes loop |

**Aspirational subtotals:**
- V-01: 46/46 (all PASS, two PASS+)
- V-02: 46/46
- V-03: 46/46
- V-04: 46/46 (all PASS, three PASS+)
- V-05: 44/46 (C-14 PARTIAL = 0.5, C-16 PARTIAL = 0.5)

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** |
|-----------|-----------|-------------|--------------|-----------|
| V-04 | 60 | 30 | 46 | **136** |
| V-01 | 60 | 30 | 46 | **136** |
| V-03 | 60 | 30 | 46 | **136** |
| V-02 | 60 | 30 | 46 | **136** |
| V-05 | 60 | 30 | 44 | **134** |

---

## Ranking

Four variations tie at 136. Tie-breaking by innovation quality within full-compliance tier:

**1. V-04 — 136** (tie-break: first)
CONTRACT AUDITOR role promotes C-25 from a documentation requirement to a hard pre-execution gate. AUTHORIZED_REWRITERS field in Phase 0-A-6 handles legitimate off-topic writes without generating false OFF_CONTRACT_WRITE anomalies — a semantic gap that previous rounds left open. Phase 0-CA-1 produces a VARS_IN_TOPOLOGY vs VARS_IN_CONTRACT completeness check that no other variation has. Phase 6-A adds CONTRACT_AUDIT_GATE_HONORED to close the verification loop.

**2. V-01 — 136** (tie-break: second)
Mutation-first authoring turns Phase 6-E from a retroactive discrepancy-finder into a structural impossibility check. Any SESSION_STATE value that lacks a Phase 1-S mutation event cannot exist, because SESSION_STATE is reconstructed from Phase 1-S replay rather than independently authored. This eliminates an entire class of developer error at source rather than at audit.

**3. V-03 — 136** (tie-break: third)
COVERAGE_QUALITY_GATE as CLEAN|DEGRADED headline for Phase 5 makes TIMELINE_ANOMALY_RATE the primary quality signal rather than one of four parallel ratios. A developer with TIMELINE_ANOMALY_RATE > 0 must acknowledge PROVISIONAL coverage ratios before reporting topic and transition coverage — prevents coverage-washing over temporal defects.

**4. V-02 — 136** (tie-break: fourth)
SIMULATION_DELTA and STATUS_QUO_GAP are the most operationally useful additions for team adoption: the artifact self-justifies against "we already reviewed this flow" resistance. Auditor verification of SIMULATION_DELTA_COMPLETE is a genuine gate. However, the innovation is in the meta-narrative layer, not in structural contract enforcement.

**5. V-05 — 134**
CONSTRAINT_VERDICTS per turn and CONV_01_EVIDENCE arithmetic checks are genuinely innovative — especially CONV_01_EVIDENCE which makes the PRE+MUTATION=POST computation explicit. Loses 1 point on C-14 and C-16 because Step-N framing departs from Phase 0-D-N structure the rubric criteria reference explicitly. CONV-NN constraints serve as invariant IDs but the Phase 0-D-4 block and PHASE_0_CONTRACT: SEALED marker are absent.

---

## Excellence Signals from V-04

1. **AUTHORIZED_REWRITERS field in timeline contract** — distinguishes legitimate off-topic writes (approved by Architect) from anomalous ones. Prior variations left OFF_CONTRACT_WRITE as binary: any write in a non-FIRST_WRITTEN_TOPIC topic was an anomaly. V-04 introduces a third category: authorized re-writer. This prevents false defect inflation and makes the timeline contract semantically complete.

2. **CONTRACT AUDITOR as a hard role gate** — the Developer receives a formal PASS/BLOCKED verdict before Phase 1. If BLOCKED, Developer's first output must be a CONTRACT_REMEDIATION section. This converts C-25 from a write-it-and-hope requirement into a pre-verified contract. No prior variation enforced this boundary.

3. **Phase 0-CA coverage check separates topology vars from contract vars** — explicitly computing VARS_IN_TOPOLOGY (union of all SESSION_VARS_WRITTEN + SESSION_VARS_READ across all topics) and VARS_IN_CONTRACT (from Phase 0-A-6) produces COVERAGE_GAPS as a findable, traceable list. Prior variations required all variables to be declared but provided no mechanism to verify completeness before tracing.

4. **CONTRACT_AUDIT_GATE_HONORED in Phase 6-A** — the Auditor independently verifies that the Developer did not begin Phase 1 without CONTRACT_AUDIT: PASS. This closes the role-gate loop: the gate exists, the Developer must honor it, and the Auditor verifies it was honored.

---

```json
{"top_score": 136, "all_essential_pass": true, "new_patterns": ["Contract Auditor role as hard pre-execution gate for session variable timeline contract — separates contract completeness verification from trace execution, eliminating retroactive contract gap rationalization", "AUTHORIZED_REWRITERS field in timeline contract distinguishes approved off-topic writes from anomalies — prevents false OFF_CONTRACT_WRITE defect inflation and makes the contract semantically complete before the first turn is traced"]}
```
