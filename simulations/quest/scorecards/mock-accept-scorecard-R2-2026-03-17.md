# Quest Score — mock-accept R2

## Criterion Evaluation

### V-01 — Artifact-as-Subject Standing Rule

| Criterion | Weight | Verdict | Evidence |
|-----------|--------|---------|----------|
| C-01 Auto-flag rules | Essential | PASS | Rules A/B/C produce explicit statements per namespace |
| C-02 Forbidden triad | Essential | PASS | All three triggers acknowledged |
| C-03 Status writeback + Canary | Essential | PASS | Phase 4 Edit tool + Canary assertion |
| C-04 Review artifact structure | Essential | PASS | Phase 5 has Coverage table (4 cols), Structural records, Risk, Next Steps all under Write |
| C-05 MOCK-ACCEPTED positive argument | Essential | PASS | Labeled fields "Your codes: ___" + Slot 1 + Slot 2 with revert-on-violation |
| C-06 Entity-naming in roles | Recommended | PASS | "Required artifact citation" templates enforce specific element naming in output |
| C-07 Step sequencing and guard compliance | Recommended | FAIL | Two-list partition present but no explicit Arch-blocked/Strategy-blocked accumulator lists |
| C-08 Eval-driven REAL-REQUIRED template | Recommended | FAIL | Role + verdict recorded but 5-field template (trigger, SQ answer, Artifact state) absent |
| C-09 Artifact-as-subject grammar | Aspirational | PASS | Standing rule embedded — auto-flag rules use "The mock artifact's [ns] section records…" |
| C-10 Tier sourcing | Aspirational | FAIL | No "Tier: N (source: …)" opening statement |
| C-11 Inline completeness gate | Aspirational | PASS | "N + M = [total]. Expected: 9." completeness check |
| C-12 Reason-code at point of use | Aspirational | PASS | Labeled field with exact-token-only constraint |
| C-13 Phase exit assertions | Aspirational | FAIL | No named PHASE N EXIT ASSERTION blocking transitions |
| C-14 Blank-line failure signal | Aspirational | PASS | "Your codes: ___" / "Your statement: ___" fill-in blanks throughout Phase 3 |

**Score**: 60 + 10 + (3/6×10) = **75.0**

---

### V-02 — Named Blocking Completeness Gates

| Criterion | Weight | Verdict | Evidence |
|-----------|--------|---------|----------|
| C-01 Auto-flag rules | Essential | PASS | Rules explicit with exact tokens in Decision Grid column rule |
| C-02 Forbidden triad | Essential | PASS | All three triggers present |
| C-03 Status writeback + Canary | Essential | PASS | COMPLETENESS-GATE D + Canary pattern |
| C-04 Review artifact structure | Essential | FAIL | Decision Grid (Step 6 copy) lacks Category column; Next Steps in Step 7 not in file |
| C-05 MOCK-ACCEPTED positive argument | Essential | PASS | Reason codes in grid column rule + Structural Slot Table (Slot 1 + Slot 2) |
| C-06 Entity-naming in roles | Recommended | FAIL | Step 3 records verdicts only — no "Required artifact citation" template |
| C-07 Step sequencing and guard compliance | Recommended | FAIL | GATE A + GATE B serve partition; no named Arch-blocked/Strategy-blocked lists |
| C-08 Eval-driven REAL-REQUIRED template | Recommended | FAIL | "driven by: [role]" captures role only; 5-field template absent |
| C-09 Artifact-as-subject grammar | Aspirational | FAIL | No standing artifact-as-subject rule; column instructions don't enforce grammar |
| C-10 Tier sourcing | Aspirational | FAIL | No tier sourcing statement |
| C-11 Inline completeness gate | Aspirational | PASS | GATE A / B / C / D named blocking checkpoints — strongest C-11 implementation |
| C-12 Reason-code at point of use | Aspirational | PASS | Inline column rule: "constraint — write the exact token in this column cell" |
| C-13 Phase exit assertions | Aspirational | FAIL | GATES are mid-step integrity checks, not N+M pre-transition assertions |
| C-14 Blank-line failure signal | Aspirational | FAIL | No fill-in blank pattern; column cells are not structurally blank-visible |

**Score**: 48 + 0 + (2/6×10) = **51.3**

---

### V-03 — Inline CONSTRAINT Blocks

| Criterion | Weight | Verdict | Evidence |
|-----------|--------|---------|----------|
| C-01 Auto-flag rules | Essential | PASS | Phase 2 classification rules explicit |
| C-02 Forbidden triad | Essential | PASS | All three triggers present |
| C-03 Status writeback + Canary | Essential | PASS | Phase 5 Edit + Canary |
| C-04 Review artifact structure | Essential | FAIL | Next Steps in Phase 7 separate from the Write instruction in Phase 6 |
| C-05 MOCK-ACCEPTED positive argument | Essential | PASS | Phase 4 CONSTRAINT blocks enforce all three fields with revert-on-violation |
| C-06 Entity-naming in roles | Recommended | FAIL | Phase 3 roles have pass/fail verdicts only; no citation output template |
| C-07 Step sequencing and guard compliance | Recommended | FAIL | Exit check produces counts; no named Arch-blocked/Strategy-blocked lists |
| C-08 Eval-driven REAL-REQUIRED template | Recommended | FAIL | Role + verdict captured; 5-field template absent |
| C-09 Artifact-as-subject grammar | Aspirational | FAIL | No standing artifact-as-subject rule |
| C-10 Tier sourcing | Aspirational | FAIL | No tier sourcing statement |
| C-11 Inline completeness gate | Aspirational | PASS | "Inventory total = [N]. Required: 9." halt condition |
| C-12 Reason-code at point of use | Aspirational | PASS | Framed CONSTRAINT block co-located with Field 1 — strongest C-12 implementation |
| C-13 Phase exit assertions | Aspirational | FAIL | Exit check in Phase 2 is a count summary, not a blocking transition gate |
| C-14 Blank-line failure signal | Aspirational | PASS | "Your codes: ___" / "Your statement: ___" blank lines in CONSTRAINT blocks |

**Score**: 48 + 0 + (3/6×10) = **53.0**

---

### V-04 — Artifact-as-Subject + Phase Exit Assertions

| Criterion | Weight | Verdict | Evidence |
|-----------|--------|---------|----------|
| C-01 Auto-flag rules | Essential | PASS | Rules A/B/C with artifact-as-subject form; unconditional language |
| C-02 Forbidden triad | Essential | PASS | All three triggers present |
| C-03 Status writeback + Canary | Essential | PASS | Phase 4 Edit + Canary with artifact-as-subject count line |
| C-04 Review artifact structure | Essential | PASS | Phase 5 Write includes Coverage table (4 cols), Structural records, Risk, Next Steps |
| C-05 MOCK-ACCEPTED positive argument | Essential | PASS | Phase 3 labeled fields with exact-token constraint + revert-on-violation for each slot |
| C-06 Entity-naming in roles | Recommended | PASS | "Required artifact citation" templates for all three roles; named elements enforced in output |
| C-07 Step sequencing and guard compliance | Recommended | PASS | Phase 0/1/2 EXIT ASSERTIONs produce explicit counts; "Do not proceed until" language enforces sequential gates; Phase 2 exit counts X+Y=M before Phase 3 |
| C-08 Eval-driven REAL-REQUIRED template | Recommended | FAIL | Artifact citations for roles present; 5-field full template (trigger field, Artifact state) absent |
| C-09 Artifact-as-subject grammar | Aspirational | PASS | Standing rule at top: "PASS: 'The mock artifact's [namespace] section [shows/records/lacks]…' FAIL: 'I found…' / 'This namespace has…'" — covers all phases |
| C-10 Tier sourcing | Aspirational | FAIL | No "Tier: N (source: …)" opening statement |
| C-11 Inline completeness gate | Aspirational | PASS | Phase 0 EXIT ASSERTION: "The mock artifact contains [N] namespace sections. Expected: 9. Match: [YES/NO]" |
| C-12 Reason-code at point of use | Aspirational | PASS | Labeled field in Phase 3 with "Absent or paraphrased token = REASON-CODE-VIOLATION → revert" |
| C-13 Phase exit assertions | Aspirational | PASS | PHASE 0/1/2/3 EXIT ASSERTIONs explicit; each includes N+M count; "Do not proceed to Phase N+1 until written" |
| C-14 Blank-line failure signal | Aspirational | FAIL | No fill-in "___" pattern; fields described in prose, not blank-line format |

**Score**: 60 + 20 + (4/6×10) = **86.7**

---

### V-05 — Blank-Line Failure Signal + Artifact-as-Subject

| Criterion | Weight | Verdict | Evidence |
|-----------|--------|---------|----------|
| C-01 Auto-flag rules | Essential | PASS | Question 2 auto-flagged list with explicit per-namespace statements |
| C-02 Forbidden triad | Essential | PASS | All three check questions explicit |
| C-03 Status writeback + Canary | Essential | PASS | Question 7 Edit + Canary fill-in line |
| C-04 Review artifact structure | Essential | FAIL | Next Steps in Question 9 separate from Write instruction in Question 8 |
| C-05 MOCK-ACCEPTED positive argument | Essential | PASS | Question 6 checklist with blank=SLOT-VIOLATION revert on each item |
| C-06 Entity-naming in roles | Recommended | FAIL | Q3-Q5 frame questions with named elements but output is verdict-only; no citation template required in answers |
| C-07 Step sequencing and guard compliance | Recommended | FAIL | Question 2 produces auto-flagged list explicitly; no Arch-blocked/Strategy-blocked accumulator lists |
| C-08 Eval-driven REAL-REQUIRED template | Recommended | FAIL | Verdicts recorded; 5-field template absent |
| C-09 Artifact-as-subject grammar | Aspirational | PASS | Question 2 required grammar: "The mock artifact's [namespace] section: REAL-REQUIRED (AUTO-FLAG: ___)" + Question 6 checklist slots require artifact-as-subject form |
| C-10 Tier sourcing | Aspirational | FAIL | No tier sourcing statement |
| C-11 Inline completeness gate | Aspirational | PASS | "Count: ___ (must equal 9 — scout, draft, review, flow, trace, prove, listen, program, topic)" |
| C-12 Reason-code at point of use | Aspirational | PASS | Checkbox inline: "Blank or paraphrased = REASON-CODE-VIOLATION → revert to REAL-REQUIRED" |
| C-13 Phase exit assertions | Aspirational | FAIL | No N+M phase exit assertions between questions |
| C-14 Blank-line failure signal | Aspirational | PASS | Checklist "Your codes: ___" / "Your statement: ___" — blank line is structurally visible |

**Score**: 48 + 0 + (4/6×10) = **54.7**

---

## Composite Rankings

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden |
|------|-----------|-----------|-------------|--------------|-----------|--------|
| 1 | V-04 | 5/5 = 60 | 2/3 = 20 | 4/6 = 6.7 | **86.7** | YES |
| 2 | V-01 | 5/5 = 60 | 1/3 = 10 | 3/6 = 5.0 | **75.0** | No (score < 80) |
| 3 | V-05 | 4/5 = 48 | 0/3 = 0 | 4/6 = 6.7 | **54.7** | No (C-04 fail) |
| 4 | V-03 | 4/5 = 48 | 0/3 = 0 | 3/6 = 5.0 | **53.0** | No (C-04 fail) |
| 5 | V-02 | 4/5 = 48 | 0/3 = 0 | 2/6 = 3.3 | **51.3** | No (C-04 fail) |

---

## Excellence Signals from V-04

**1. Entry condition + exit assertion pairing per phase**
Every phase opens with "Entry condition: Phase N-1 exit assertion written" and closes with a named "PHASE N EXIT ASSERTION." This creates bidirectional gates — you can't enter a phase unless the previous exit was written, and you can't leave unless the current exit is written.

**2. "Do not proceed until" enforcement language**
"Do not proceed to Phase N until Phase N-1 exit assertion is written." This converts exit assertions from observations into mandatory blockers. No other variation uses this language.

**3. Phase exit assertion doubles as completeness gate + count citation**
"The mock artifact yields [N] AUTO-FLAGGED sections and [M] EVALUATION-ELIGIBLE sections. N + M = [total]. Expected: 9. Phase 1 complete." — a single output line satisfies both C-11 (count gate) and C-13 (phase transition assertion) simultaneously.

**4. Artifact-as-subject rule declared before all phases, not embedded in individual steps**
The standing rule covers "all phase outputs, exit assertions, Slot 1, Slot 2, Canary, review artifact" in one block. This is more durable than embedding grammar reminders per phase.

**Why V-04 beats V-01 by 11.7 points**: V-01 achieves C-06 and C-09 but has no C-13 and no C-07. V-04 adds both: phase exit assertions unlock C-13 and serve as the guard compliance mechanism that unlocks C-07.

**Why V-04 beats V-05 by 32 points**: V-05 achieves C-09 and C-14 but fails C-04 (next steps in separate question) and all three recommended criteria. V-04 keeps next steps within the same phase as the Write instruction, passes C-06 via required artifact citations, and passes C-07 via phase exit assertions.

---

```json
{"top_score": 86.7, "all_essential_pass": true, "new_patterns": ["phase entry condition declarations — each phase states its precondition explicitly, creating bidirectional entry+exit gates beyond C-13 exit-only", "mandatory gating language — 'Do not proceed until' converts exit assertions from observable outputs into hard blockers"]}
```
