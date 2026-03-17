## /quest:score — mock-review R7 Scoring

**Note**: Only V-01 content was provided. V-02–V-05 were described by axis but content was not included in the input. Scoring V-01 in full; flagging gap.

---

## V-01 Scoring — Role Sequence Axis (Architect-first)

> Content note: STEP 5 (Decisions Output, write-back, next-steps) is truncated. Scoring reflects what is shown; STEP 5-dependent criteria are scored on available evidence.

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| **C-01 Decision completeness** | **PARTIAL** | STEP 0 lists all namespaces; STEP 1 routes all to AUTO-CLASSIFIED or REMAINING; evaluation steps cover REMAINING. Final consolidated decision list not shown (STEP 5 truncated). Structural routing is complete; output format unverifiable. |
| **C-02 Automatic rule correctness** | **PASS** | All three rules fire in STEP 1. Each has an explicit `DO NOT` forbidden-output statement. STOP gate separates auto phase from evaluation. Contamination guard ("DO NOT apply role evaluation to any namespace in the AUTO-CLASSIFIED list") is a named instruction, not implied. |
| **C-03 MOCK-ACCEPTED reason codes** | **FAIL** | `STRUCTURAL-COVERAGE-SUFFICIENT` and `DOMAIN-KNOWLEDGE-CONSISTENT` do not appear anywhere in the visible content. STEP 4 Strategy leads to MOCK-ACCEPTED for COVERAGE-ADEQUATE but defines no reason code. The MOCK-ACCEPTED decision block referenced ("below") is not shown. |
| **C-04 Status write-back** | **FAIL** | No write-back phase visible. STEP 5 truncated. The defining behavioral criterion cannot be verified. |
| **C-05 Next-steps priority order** | **FAIL** | No next-steps section shown. STEP 5 truncated. |

**Essential score**: (0.5 + 1 + 0 + 0 + 0) / 5 × 60 = **18.0 pts**

---

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| **C-06 Rule trigger named** | **PASS** | `trigger = {rule label}` present in STEP 1 output template. Evaluation-driven REAL-REQUIRED blocks use `architect-verdict = CONTRADICTS-ARCHITECTURE` and `pm-verdict = STRUCTURAL-GAP` — named verdict-to-decision links. |
| **C-07 PM/Architect/Strategy shown** | **PASS** | All three roles have dedicated steps with sub-questions. PM references sections/gates. Architect names invariants and platform facts. Strategy assesses coverage threshold vs tier decision. All produce verdicts. |
| **C-08 Tier flag respected** | **PASS** | STEP 0 requires `Tier: {N}  source: {TOPICS.md | default-Tier-1}` at output top. TIER-CRITICAL rule gates correctly on `Tier >= 2`. Tier applied as input to auto-classification before evaluation begins. |

**Recommended score**: 3/3 × 30 = **30.0 pts**

---

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-09 Coverage gap synthesis | **FAIL** | No next-steps section shown. |
| C-10 Namespace-specific MOCK-ACCEPTED rationale | **FAIL** | MOCK-ACCEPTED block not shown. STEP 4 leads to it but the block content is absent. No rationale template visible. |
| C-11 Forbidden-output enumeration | **PASS** | All three auto-rules have explicit DO NOT statements naming the prohibited outcome: "DO NOT mark an EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality…", "DO NOT mark a TIER-CRITICAL namespace…", "DO NOT mark a COMPLIANCE-TAGGED namespace…". Full triad covered. |
| C-12 Zero-remaining confirmation gate | **FAIL** | No write-back phase shown. |
| C-13 Verifiable role-step separation | **PASS** | STEP 2, STEP 3, STEP 4 each have their own heading, named sub-questions, output format, and required verdict. Each is independently completable. |
| C-14 SQ answer citation in verdict traceability | **PASS** | STEP 2: `Artifact state: {the specific invariant named in ASQ-2 that mock cannot satisfy}` — SQ answer propagates directly into the artifact state field, creating a named chain from diagnostic to verdict. |
| C-15 Entity-naming SQ grammar | **PASS** | All nine sub-questions use "Name the…" or "What specific X" grammar. ASQ-1: "Name the component." ASQ-2: "Name the invariant." PSQ-1/2: "Name the specific section, table, or gate." SSQ-1: "Name the decision." SSQ-3: "Name the specific risk." None produce yes/no or opinion answers. |
| C-16 Canary confirmation (prohibited under failure) | **FAIL** | No write-back or confirmation phase shown. |
| C-17 Auto-flagged contamination guard | **PASS** | Two contamination guards present: (1) "DO NOT apply role evaluation to any namespace in the AUTO-CLASSIFIED list" at STEP 1 exit; (2) "DO NOT apply PM evaluation to namespaces with `architect-verdict = CONTRADICTS-ARCHITECTURE`" at STEP 2 exit. Both name the error explicitly. |
| C-18 Inter-step gate with next-step reference | **PASS** | STEP 1: "STOP. Do not proceed to STEP 2 until…"; STEP 2: "DO NOT proceed to STEP 3 until…"; STEP 3: "DO NOT proceed to STEP 4 until…". All gates name the specific next step being blocked. |
| C-19 Structured trigger notation | **PASS** | `trigger = {rule label}` appears in the STEP 1 output template as a named field in fixed position, distinct from prose description. |
| C-20 Contrastive MOCK-ACCEPTED rationale | **PARTIAL** | Per rubric preamble signal: "single slot allows confirmatory escape — no Contrast sub-slot to guarantee structural contrast." DEFAULT DECISION POSITION in STEP 4 establishes inversion, which is necessary but insufficient. The MOCK-ACCEPTED rationale template (not shown) has a single slot that can be satisfied by a confirmatory sentence. |
| C-21 SQ answer structural signal | **PARTIAL** | `Artifact state: {the specific invariant named in ASQ-2}` provides a positive structural form linking to a named SQ answer. However, the template does not name the "verdict echo" error or distinguish present-tense artifact naming from past-tense assessment restatement. Positive signal present; negative prohibition absent. |
| C-22 Decision inversion framing | **PASS** | STEP 4 opens with `DEFAULT DECISION POSITION: REAL-REQUIRED. MOCK-ACCEPTED is an earned escape that requires a positive argument against the default.` Named block, skill-level, not only in rationale guidance. |
| C-23 Strategy SQ-1 anchor | **PARTIAL** | SSQ-1: "Name the decision. (This answer anchors the Structural position slot.)" — SSQ-1 is named as the anchor and requires naming the tier decision. However, the MOCK-ACCEPTED template is not shown; the `Structural position` slot itself cannot be verified as a named, required field. |
| C-24 Artifact state propagation | **FAIL** | Artifact state is defined in evaluation-driven REAL-REQUIRED blocks. Next-steps section not shown; propagation into `/{skill-id} {topic} — {artifact state}` format unverifiable. |
| C-25 Dedicated contrast sub-slot | **FAIL** | Per rubric preamble: "single slot allows confirmatory escape — no Contrast sub-slot." Rationale template does not have a structurally separate `Contrast:` slot. C-22 inversion framing is present but advisory; mechanical enforcement absent. |

**Aspirational tally**:

| C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | C-21 | C-22 | C-23 | C-24 | C-25 |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| 0 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0.5 | 0.5 | 1 | 0.5 | 0 | 0 |

Sum: 9.5 / 17 × 10 = **5.6 pts**

---

## V-01 Composite

| Component | Score |
|-----------|-------|
| Essential (5 criteria) | 18.0 |
| Recommended (3 criteria) | 30.0 |
| Aspirational (17 criteria) | 5.6 |
| **Total** | **53.6** |

---

## Missing Variations

V-02 through V-05 content was not included in the input. Based on rubric preamble signals and axis descriptions, expected scoring direction:

| Variation | Axis | Key Predicted Deltas |
|-----------|------|---------------------|
| V-02 | B — Inertia framing | C-10 PASS, C-20 PASS, C-25 PASS (two-slot template per preamble signal). Estimated +8–10 pts over V-01. |
| V-03 | C — Lifecycle emphasis | C-04 PASS, C-05 PASS, C-12 PASS, C-16 PASS expected. Estimated +10–14 pts over V-01. |
| V-04 | B+C | Cumulative V-02+V-03 gains. Likely top single-gap score. |
| V-05 | A+B+C | All axes. Highest potential. |

To complete this scoring run, provide V-02–V-05 content.

---

## Excellence Signals from V-01 (patterns worth carrying forward)

1. **Role-sequence gating as contamination control** — placing Architect before PM means architectural contradictions short-circuit structural analysis; the gate names the specific next step blocked (`DO NOT apply PM evaluation to namespaces with architect-verdict = CONTRADICTS-ARCHITECTURE`).
2. **Triad DO NOT coverage** — all three auto-rules have explicit forbidden-output statements; the pattern is complete and enumerable.
3. **Entity-naming SQ grammar discipline** — all nine sub-questions across three roles use "Name the specific X" form; none admit yes/no answers.
4. **Artifact state as SQ-to-verdict bridge** — `Artifact state: {specific invariant named in ASQ-2}` creates a named chain from diagnostic answer to decision record, not just a verdict label.

---

```json
{"top_score": 53.6, "all_essential_pass": false, "new_patterns": ["role-sequence-gate-as-contamination-control: Architect-first evaluation gates PM entry, naming the specific contamination error (DO NOT apply PM to CONTRADICTS-ARCHITECTURE namespaces) rather than just separating phases", "triad-DO-NOT-coverage: all three auto-rules carry explicit forbidden-output statements as an enumerable set, enabling mechanical verification that no rule is missing its prohibition"]}
```
