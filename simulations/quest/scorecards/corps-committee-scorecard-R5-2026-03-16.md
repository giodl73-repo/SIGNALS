# corps-committee — R5 Scoring (Rubric v5)

## Criterion Inventory

The v5 rubric contains **7 essential criteria** (C-01, C-02, and the inherited C-03–C-07 from prior rounds), **5 aspirational criteria from rounds R1–R3** (C-08–C-12), **4 aspirational criteria from R4** (C-13–C-16), and **3 new aspirational criteria introduced in v5** (C-17, C-18, C-19). Total: **12-way aspirational pool at ≈0.83 pts each**.

---

## Criteria Evaluation

### Essential Criteria

#### C-01 — Typed Agenda Item Declaration

| V | Status | Evidence |
|---|--------|----------|
| V-01 | **PASS** | `Committee Type:` and `Agenda Item:` fields in skeleton Phase 0; fill rules enforce accepted vocabulary (ROB / shiproom / arch-board); V-01 adds COMMITTEE TYPE GATE skeleton block that ticks both fields before PHASE-0-COMMIT. |
| V-02 | **PASS** | Same fields present; fill rules enforce correct vocabulary; no gate, but prose enforcement identical to R4 V-05 baseline. |
| V-03 | **PASS** | Same fields present. No change to Phase 0 declaration. |
| V-04 | **PASS** | V-01 + V-02 additive; Committee Type and Agenda Item enforced by both skeleton gate and fill rule. |
| V-05 | **PASS** | All three R5 mechanisms; Phase 0 gate inherited from V-01. Full COMMITTEE TYPE GATE present. |

#### C-02 — Five-Phase Structure with Terminal Commits

| V | Status | Evidence |
|---|--------|----------|
| V-01 | **PASS** | Phases 0–5 present in sequence; each PHASE-N-COMMIT carries `| ENFORCE: terminal position` directive. |
| V-02 | **PASS** | Same. Bridge expansion does not alter phase count or commit placement. |
| V-03 | **PASS** | Same. TALLY LEDGER PROTOCOL operates inside Phase 4 before the PHASE-4-COMMIT. |
| V-04 | **PASS** | Same. |
| V-05 | **PASS** | Same. All three R5 additions remain within phase boundaries. |

---

### Aspirational Criteria (C-03 through C-16, inherited from R4 V-05 foundation)

All five variations are built **on the complete R4 V-05 foundation**. R4 V-05 earned all 9 prior aspirational criteria (C-08–C-16) under v4. Under v5 those same criteria remain present. Status: **PASS for all variations, all criteria C-03–C-16**.

---

### v5 New Aspirational Criteria

#### C-17 — Phase 5 Completeness Skeleton Gate (MINUTES INTEGRITY CHECK)

| V | Status | Evidence |
|---|--------|----------|
| V-01 | **PASS** | Inherited from R4 V-05. 5-checkbox block present between PHASE-4-COMMIT and Phase 5 skeleton header. Halting declaration "Any unticked box halts Phase 5." Phase 5 fill rule mandates all five ticked before content generated. |
| V-02 | **PASS** | Same. Bridge expansion does not touch MINUTES INTEGRITY CHECK. |
| V-03 | **PASS** | Same. TALLY LEDGER operates before PHASE-4-COMMIT; MINUTES INTEGRITY CHECK at Phase 4→5 transition unchanged. |
| V-04 | **PASS** | Same. |
| V-05 | **PASS** | Same. |

#### C-18 — Phase 3 Named Correction Protocol (TIER SEQUENCE PROTOCOL)

| V | Status | Evidence |
|---|--------|----------|
| V-01 | **PASS** | Inherited. `*** TIER SEQUENCE PROTOCOL ***` / `*** END TIER SEQUENCE PROTOCOL ***` delimited block in Phase 3 fill rules. Self-referencing restart: "Execute TIER SEQUENCE PROTOCOL again from the top." |
| V-02 | **PASS** | Same. Bridge expansion precedes Phase 3; TIER SEQUENCE PROTOCOL inside Phase 3 fill rules unchanged. |
| V-03 | **PASS** | Same. |
| V-04 | **PASS** | Same. |
| V-05 | **PASS** | Same. |

#### C-19 — Inertia Citation Audit Block

| V | Status | Evidence |
|---|--------|----------|
| V-01 | **PASS** | Inherited. `## INERTIA CITATION AUDIT` skeleton block with per-finding `Cited by:` fields, AUDIT RESULT declaration, `PHASE-3-COMMIT halts until AUDIT RESULT is COMPLETE`. |
| V-02 | **PASS** | Same. |
| V-03 | **PASS** | Same. |
| V-04 | **PASS** | Same. |
| V-05 | **PASS** | Same. |

---

### R5 Candidate Criteria (v6 preview — not scored under v5)

These are new mechanisms introduced in R5 that exceed v5's rubric. Noted here as excellence signals.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-20 (cand.)** COMMITTEE TYPE GATE | PASS | FAIL | FAIL | PASS | PASS |
| **C-21 (cand.)** Structured Bridge Completeness | FAIL | PASS | FAIL | PASS | PASS |
| **C-22 (cand.)** TALLY LEDGER PROTOCOL | FAIL | FAIL | PASS | FAIL | PASS |

---

## Composite Scores

All R5 variations inherit R4 V-05's full criterion set, satisfying all 12 v5 aspirational criteria. No redistribution penalty applies. The variate file confirms this directly: *"Scoring against rubric v5 will not yet reveal a score delta because v5 criteria (C-17, C-18, C-19) are already satisfied by all R5 variations (they inherit R4 V-05)."*

| Variation | Essential Pass | Aspir. Earned (of 12) | Score (v5) | v6-candidate criteria earned |
|-----------|---------------|----------------------|------------|------------------------------|
| V-01 | YES | 12/12 | **97.83** | C-20 only |
| V-02 | YES | 12/12 | **97.83** | C-21 only |
| V-03 | YES | 12/12 | **97.83** | C-22 only |
| V-04 | YES | 12/12 | **97.83** | C-20 + C-21 |
| V-05 | YES | 12/12 | **97.83** | C-20 + C-21 + C-22 |

---

## Ranking

**All five variations tie at 97.83.** The differentiator is v6-candidate criterion coverage:

1. **V-05** — closes all three new phase-boundary gaps (C-20 + C-21 + C-22)
2. **V-04** — closes Phase 0 exit + Bridge entry (C-20 + C-21)
3. **V-01** — closes Phase 0 exit only (C-20)
4. **V-02** — closes Bridge entry only (C-21)
5. **V-03** — closes Phase 4 counting only (C-22)

---

## Excellence Signals from V-05

**Signal 1 — Progressive phase-boundary coverage closes all unguarded transitions.** R4 V-05 had skeleton gates at Phase 1 (REWRITE PROTOCOL), Phase 3 (TIER SEQUENCE PROTOCOL + INERTIA CITATION AUDIT + SYMMETRY CHECK), and Phase 5 (MINUTES INTEGRITY CHECK). V-05 fills the three remaining gaps: Phase 0 exit (COMMITTEE TYPE GATE), Phase 2→3 transition (Structured Bridge with BRIDGE RESULT halt), and Phase 4 counting (TALLY LEDGER PROTOCOL). Together the skeleton now gates every phase exit.

**Signal 2 — Commit acknowledgment as audit trail.** V-01 and V-03 (and their combined V-05) add named confirmation strings into the PHASE-N-COMMIT body itself: `"COMMITTEE TYPE GATE ticked."` in PHASE-0-COMMIT and `"TALLY LEDGER confirmed."` in PHASE-4-COMMIT. This mirrors the existing `INERTIA CITATION AUDIT RESULT is COMPLETE` in PHASE-3-COMMIT (C-19). A consistent pattern: every skeleton gate that produces a boolean outcome writes its outcome into the phase commit that seals the phase.

**Signal 3 — Inspection field decoupled from Decision field.** The structured Bridge (V-02/V-05) separates `Inspection complete: YES` from `Decision: YES/NO`. This two-step structure prevents the C-08 failure mode where a model writes `YES` without completing the inspection: to satisfy both fields the model must first confirm the inspection was done and then declare its conclusion. The same decoupling pattern could be applied to GATE-N in Phase 1 (currently `Answer:` conflates "evaluated" with "result").

---

```json
{"top_score": 97.83, "all_essential_pass": true, "new_patterns": ["Progressive phase-boundary coverage: skeleton gates now close all six phase transitions when V-05 mechanisms are co-applied", "Commit acknowledgment audit trail: PHASE-N-COMMIT body records named gate outcome string, extending the INERTIA CITATION AUDIT RESULT pattern to Phase 0 and Phase 4", "Inspection-Decision field split in structured Bridge: decouples the act of inspecting from the conclusion, preventing YES-without-inspection failure mode"]}
```
