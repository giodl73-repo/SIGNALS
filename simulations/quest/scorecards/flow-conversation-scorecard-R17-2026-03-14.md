---

## Scorecard — flow-conversation — Round 17 (v16 rubric)

**Date:** 2026-03-15 | **Rubric version:** v16 | **Max score:** 240

---

### Scoring Framework

| Tier | Pts | Criteria |
|------|-----|----------|
| Essential | 60 | C-01 to C-04 (15 pts each) |
| Recommended | 30 | C-05 to C-07 (10 pts each) |
| Aspirational | 150 | C-08 to C-71 (variable) |
| **Max** | **240** | |

All five variations carry the full v16 baseline (C-01 through C-65, C-67, C-68 = 232 pts). Differential criteria are C-66, C-69, C-70, C-71 (2 pts each).

---

### Criterion-Level Evidence

#### Baseline Criteria (all variations, C-01–C-65, C-67, C-68) — 232 pts

All five variations explicitly carry the full v16 baseline: structured turn-by-turn trace (C-01–C-04), defect reproduction/fallback/disambiguation (C-05–C-07), and the full aspirational chain through C-65 (schema registry, invariant chains, deviation/chain budgets, prediction contract, status quo method, pre-flight manifest with SCHEMA_TYPE column, row-count parentheticals in CA output). C-67 (WRONG_SCHEMA_RESIDUAL_CHECK in Phase 6-A) and C-68 (PARENTHETICAL_PRESENCE_VERIFICATION in Phase 6-A) are baseline-included for v16 — all variations PASS. **Baseline: 232/240.**

---

#### Differential Criteria

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-66** — Dedicated `## LIFECYCLE_PROTOCOL` named section; "silent fallthrough is structural violation" at top; all 5 labeled pairs within section. Req C-63. | PASS | FAIL | FAIL | PASS | PASS |
| **C-69** — `WRONG_SCHEMA_RESIDUAL_SWEEP` embedded as gate field in `CONTRACT_AUDIT_GATE_HONORED` (not standalone parallel block). Req C-67. | FAIL | PASS | **PASS†** | PASS | PASS |
| **C-70** — Zero inline HANDOFF_TO/Received in role instruction blocks; pointer-only references ("per LIFECYCLE_PROTOCOL Transition N"). Req C-66. | PASS | FAIL | FAIL | PASS | PASS |
| **C-71** — `PARENTHETICAL_VERIFICATION` embedded as gate field in `CONTRACT_AUDIT_GATE_HONORED`. Req C-68. | FAIL | FAIL | PASS | FAIL | PASS |

**† V-03 C-69 note:** The variation description states "no WRONG_SCHEMA_RESIDUAL_SWEEP in gate (C-69 unaddressed)" and the variation matrix marks it NO — but the actual gate code in V-03 contains `WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN before Phase 1: CONFIRMED|NOT_CONFIRMED` as its **first field**, explicitly paired with `PARENTHETICAL_VERIFICATION` as the second field. The governing CONSTRAINT in V-03 reads: *"CONTRACT_AUDIT_GATE_HONORED without both WRONG_SCHEMA_RESIDUAL_SWEEP and PARENTHETICAL_VERIFICATION fields present and CONFIRMED is an INCOMPLETE_GATE_ASSERTION."* The structural criterion (gate field present and part of gate assertion) is satisfied. Scoring follows code, not stated intent: **C-69 PASS for V-03**.

---

#### Per-Variation Detail

**V-01 — Axis S (C-70 target)**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-66 | PASS | `## LIFECYCLE_PROTOCOL` section opens with "Silent fallthrough is a structural violation." All 5 transitions labeled with outgoing/incoming pairs. |
| C-69 | FAIL | Gate block has no `WRONG_SCHEMA_RESIDUAL_SWEEP` field. Standalone check block runs; gate does not consume its result. |
| C-70 | PASS | `SOLE_AUTHORITY` declaration present. All role instructions use "Close/Open per LIFECYCLE_PROTOCOL Transition N" — zero inline HANDOFF_TO or Received strings outside the section. |
| C-71 | FAIL | Gate block has no `PARENTHETICAL_VERIFICATION` field. Standalone verification table runs; gate does not consume its result. |

**Score: 232 + 2(C-66) + 0(C-69) + 2(C-70) + 0(C-71) = 236/240**

---

**V-02 — Axis T (C-69 target)**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-66 | FAIL | Lifecycle protocol appears as inline header bullets ("**Lifecycle protocol transitions: 1. Phase -1 close: ...**"). No dedicated named section. Tokens re-declared in role instruction closes ("Close with: **HANDOFF_TO: TOPOLOGY ARCHITECT**"). |
| C-69 | PASS | Gate block opens with `WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN before Phase 1: CONFIRMED|NOT_CONFIRMED` as first field. Explicit note: "A gate that asserts HONORED without a CONFIRMED sweep field is a structurally incomplete assertion." C-67 prerequisite satisfied. |
| C-70 | FAIL | C-66 prerequisite fails. Also, role instructions contain inline tokens ("Close with: **HANDOFF_TO: TOPOLOGY ARCHITECT**"). |
| C-71 | FAIL | Gate block has no `PARENTHETICAL_VERIFICATION` field. |

**Score: 232 + 0(C-66) + 2(C-69) + 0(C-70) + 0(C-71) = 234/240**

---

**V-03 — Axis U (C-71 target)**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-66 | FAIL | Lifecycle protocol rendered as inline CONSTRAINT language ("CONSTRAINT: Phase -1 MUST close with..."). No dedicated named `LIFECYCLE_PROTOCOL` section. |
| C-69 | PASS | Gate block contains `WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN before Phase 1: CONFIRMED|NOT_CONFIRMED` as **first field** — structurally present despite description saying otherwise. CONSTRAINT mandates both fields. C-67 prerequisite satisfied. |
| C-70 | FAIL | C-66 prerequisite fails. Role instructions contain inline tokens with CONSTRAINT framing ("REQUIRED — absence is LIFECYCLE_CONSTRAINT_VIOLATION"). |
| C-71 | PASS | Gate block contains `PARENTHETICAL_VERIFICATION: PASS before Phase 1: CONFIRMED|NOT_CONFIRMED` as second field, immediately after sweep field. CONSTRAINT: "gate without both fields is an INCOMPLETE_GATE_ASSERTION." C-68 prerequisite satisfied. |

**Score: 232 + 0(C-66) + 2(C-69) + 0(C-70) + 2(C-71) = 236/240**

---

**V-04 — Axes S+T (C-70+C-69 targets)**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-66 | PASS | `## LIFECYCLE_PROTOCOL` section with `SOLE_AUTHORITY` declaration. "Silent fallthrough is a structural violation." All 5 labeled transition pairs within section. |
| C-69 | PASS | Gate block opens with `WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN before Phase 1: CONFIRMED|NOT_CONFIRMED`. Explicit: "sweep result is then consumed as the first field in the gate assertion — not a parallel block the gate can ignore." C-67 satisfied. |
| C-70 | PASS | SOLE_AUTHORITY declared. All role instructions use pointer-only form ("Close/Open per LIFECYCLE_PROTOCOL Transition N"). Explicit note: "PARENTHETICAL_VERIFICATION result does not appear in the gate assertion." |
| C-71 | FAIL | Gate block explicitly excludes `PARENTHETICAL_VERIFICATION`. Standalone table present but standalone-only — "the PARENTHETICAL_VERIFICATION result does not appear in the gate assertion." |

**Score: 232 + 2(C-66) + 2(C-69) + 2(C-70) + 0(C-71) = 238/240**

---

**V-05 — Axes S+T+U (C-70+C-69+C-71 targets)**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-66 | PASS | `## LIFECYCLE_PROTOCOL` section with `SOLE_AUTHORITY`. "Silent fallthrough is a structural violation." All 5 transitions labeled. |
| C-69 | PASS | Block 3 gate opens with `WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN before Phase 1: CONFIRMED|NOT_CONFIRMED` as first field. Explicitly cross-referenced from Block 1 result. C-67 satisfied. |
| C-70 | PASS | SOLE_AUTHORITY declared. All role instructions pointer-only ("Close/Open per LIFECYCLE_PROTOCOL Transition N"). Zero inline tokens outside the section. |
| C-71 | PASS | Block 3 gate has `PARENTHETICAL_VERIFICATION: PASS before Phase 1: CONFIRMED|NOT_CONFIRMED` as **second field**, immediately after sweep field. Cross-referenced from Block 2 result. C-68 satisfied. Phase 6-A explicitly structured as Block 1 → Block 2 → Block 3 (sequential, labeled). |

**Score: 232 + 2(C-66) + 2(C-69) + 2(C-70) + 2(C-71) = 240/240**

---

### Composite Scores

| Variation | Axes | C-66 | C-69 | C-70 | C-71 | Score | Delta from Max |
|-----------|------|:----:|:----:|:----:|:----:|------:|----------------|
| **V-05** | S+T+U | PASS | PASS | PASS | PASS | **240** | 0 |
| V-04 | S+T | PASS | PASS | PASS | FAIL | 238 | −2 |
| V-01 | S | PASS | FAIL | PASS | FAIL | 236 | −4 |
| V-03 | U (†bonus C-69) | FAIL | PASS | FAIL | PASS | 236 | −4 |
| V-02 | T | FAIL | PASS | FAIL | FAIL | 234 | −6 |

**Rank: V-05 > V-04 > V-01 = V-03 > V-02**

---

### Excellence Signals from V-05

**Signal 1 — Three-block sequential Phase 6-A with explicit data flow**
V-05 labels Phase 6-A as three numbered, sequential blocks: "Block 1 — WRONG_SCHEMA Residual Check," "Block 2 — Parenthetical Presence Verification," "Block 3 — Contract Audit Gate Verification." The sequential dependency is declared structurally: "The results of Blocks 1 and 2 are consumed as the first two fields of Block 3's gate assertion." This makes the execution order, the data flow between blocks, and the completeness contract for the gate all visible in the prompt structure itself — not implied by position.

**Signal 2 — Logical pair: format-compliance + completeness as gate preconditions**
V-05 frames the two gate precondition fields as a logical pair: Block 1 checks **format compliance** (WRONG_SCHEMA — were declarations in the right format?), Block 2 checks **declaration completeness** (parentheticals — were row counts accounted for?). Together they constitute the full Phase 0-CA-1 output audit summary inside the gate. The V-05 note: "A gate without both fields has not verified the complete Phase 0-CA-1 output contract." This framing gives the pair a conceptual identity beyond the individual checks.

**Signal 3 — FAIL propagation chain made explicit**
V-05 states the cascade: "PARENTHETICAL_VERIFICATION field: cross-referenced from Block 2 result. FAIL forces NOT_CONFIRMED and FAIL on the gate." This creates a traceable enforcement chain: Block 2 finding → Block 3 NOT_CONFIRMED field → gate FAIL. The prior variations had standalone blocks adjacent to the gate; V-05 makes them structurally upstream.

---

### Surprise Finding — V-03 C-69 Code/Description Discrepancy

V-03's stated design intent was to isolate C-71 only, leaving C-69 unaddressed. The variation description and matrix both mark V-03 as NO for WRONG_SCHEMA_RESIDUAL_SWEEP in gate. However, the actual gate block in V-03 contains the sweep field as its **first entry**, and the governing CONSTRAINT explicitly requires both fields to be present for a valid gate assertion. The code supersedes the stated intent: **V-03 unexpectedly satisfies C-69**, causing it to tie V-01 at 236 despite targeting only one new criterion. This discrepancy should be noted when designing R18 variations — V-03 effectively demonstrated that the phrasing-register axis (imperative CONSTRAINT language) and the parenthetical-in-gate axis are best isolated by explicitly omitting the sweep field from the gate template, not just omitting it from the stated hypothesis.

---

```json
{"top_score": 240, "all_essential_pass": true, "new_patterns": ["Three-block sequential Phase 6-A structure with explicit block labels and data-flow declarations: Block 1 and Block 2 results are named as consumed inputs to Block 3 gate, making execution order and completeness contract visible in prompt structure", "Paired gate precondition fields as logical unit: Block 1 (format compliance = WRONG_SCHEMA sweep) and Block 2 (declaration completeness = row-count parentheticals) constitute the full Phase 0-CA-1 output audit summary inside the gate; a gate without both confirmed fields has not closed the Phase 0-CA-1 enforcement loop"]}
```
