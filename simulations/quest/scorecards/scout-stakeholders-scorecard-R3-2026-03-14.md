## Round 3 Scoring — scout-stakeholders

### V-01: Reversed Sequence via Structural Phase Headers

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 CODEOWNERS fallback | PASS 12 | "Check for a CODEOWNERS file... ask exactly one question... Do not infer silently." First step, explicit. |
| C-02 Power/Interest grid | PASS 12 | Phase 3 grid with power/interest columns, quadrant labels, 4+ row minimum. |
| C-03 Veto risks ranked | PASS 12 | "List veto risks ordered by probability -- highest first. Do not sort alphabetically or by grid order." Prob + Impact per row. |
| C-04 Champion concrete action | PASS 12 | Specific schedulable examples given; "Generic 'engage the champion' language is not a champion action." |
| C-05 Comms per quadrant | PASS 12 | Four-quadrant table with Frame Type + relative timing signal required. |
| C-06 Conflict identification | PASS 10 | "Identify at least two structural conflicts... both parties named... nature of tension." |
| C-07 Role framing | PASS 10 | Phase 1 = Strategy, Phase 2 = UX, Phase 3 = PM -- three structurally distinct phases. |
| C-08 Critical-path gatekeepers | PASS 10 | "[CRITICAL PATH] with minimum lead time required" in Phase 1; confirmed in Step 7. |
| C-09 Amendment phase | PASS 5 | Step 8 amendment pass with update mandate; distinct findings required. |
| C-10 NOT doing framing | PASS 5 | Phase 2, item 4: "One explicit NOT-doing statement: what this product does not provide for this segment." |
| C-11 Source-tracking column | PASS 5 | Phase 3 grid has Source column; four source labels defined with semantics. |
| C-12 Amendment update mandate | PASS 5 | "do not observe without updating" at Step 8 execution point. |
| C-13 Prefilled frame types | PASS 5 | "Frame Type must be distinct per row" with five examples -- distinct label per quadrant enforced. |
| C-14 Named failure modes inline | PASS 5 | "Generic 'engage the champion' language is not a champion action" at Step 5; "do not observe without updating" at Step 8. Two+ inline failure mode descriptions at execution points. |
| C-15 Reversed sequence | PASS 5 | Phase 1 (Strategy) → Phase 2 (UX) → Phase 3 (PM). Phase 3 header: "Do not build this grid before Phase 1 and Phase 2 are complete." Structural enforcement. |
| C-16 Before/after pair | **FAIL 0** | Amendment step (Step 8) gives a positive rule ("do not observe without updating") and per-amendment checklist, but no bad-form example adjacent to a correct-form example. Axis intentionally excluded. |

**V-01 Total: 125 / 130**

---

### V-02: Before/After Amendment Pair

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 CODEOWNERS fallback | PASS 12 | "ask exactly one question: 'What org or team is this decision for?' Do not proceed by inferring silently." |
| C-02 Power/Interest grid | PASS 12 | Step 2 grid with Source, quadrant labels, 4+ row minimum. |
| C-03 Veto risks ranked | PASS 12 | "ordered by probability -- highest first. Not alphabetically, not by grid sequence." Rank table with Prob + Impact + Mitigation. |
| C-04 Champion concrete action | PASS 12 | Specific examples; "Generic 'engage the champion' language is not a champion action." |
| C-05 Comms per quadrant | PASS 12 | Four-quadrant table; distinct Frame Types; relative timing required. |
| C-06 Conflict identification | PASS 10 | "At least two structural conflicts. Each conflict requires both parties named and nature of tension." |
| C-07 Role framing | PASS 10 | Step 1 = Strategy, Step 2 = PM, Step 3 = UX -- three distinct sections. |
| C-08 Critical-path gatekeepers | PASS 10 | "[CRITICAL PATH -- lead time: X]" labels in Step 1; confirmed in Step 7. |
| C-09 Amendment phase | PASS 5 | "Run one amendment pass. Minimum one amendment required." |
| C-10 NOT doing framing | PASS 5 | Step 3: "One NOT-doing statement: what this product does not provide for this segment." |
| C-11 Source-tracking column | PASS 5 | Grid Source column in Step 2; four source labels defined. |
| C-12 Amendment update mandate | PASS 5 | "Update the affected table (grid, veto, or comms) -- do not observe without updating." |
| C-13 Prefilled frame types | PASS 5 | "Frame Type must be distinct per row" with labeled examples. |
| C-14 Named failure modes inline | PASS 5 | "Generic 'engage the champion' language is not a champion action" at Step 5. Bad-form example at Step 8 names the failure mode inline at execution. Two inline anti-pattern signals. |
| C-15 Reversed sequence | **FAIL 0** | Sequence is Step 1 (Strategy) → Step 2 (PM Grid) → Step 3 (UX). PM grid built before UX analysis. Intentional axis isolation. |
| C-16 Before/after pair | PASS 5 | Step 8: "Amendment execution rule -- read both forms before proceeding:" → "**Bad form** (do not do this):" [prose-only example] adjacent to "**Correct form** (required):" [full structured amendment]. Paired, adjacent, at execution point. |

**V-02 Total: 125 / 130**

---

### V-03: Anti-Pattern Saturation at Every Phase Gate

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 CODEOWNERS fallback | PASS 12 | First step + FAIL_SILENT_INFERENCE label inline. |
| C-02 Power/Interest grid | PASS 12 | Step 2 grid + FAIL_PROSE_ONLY; FAIL_NO_SOURCE. |
| C-03 Veto risks ranked | PASS 12 | Probability-ordered table + FAIL_WRONG_ORDER + FAIL_NO_MITIGATION inline. |
| C-04 Champion concrete action | PASS 12 | Concrete examples + FAIL_GENERIC_CHAMPION inline. |
| C-05 Comms per quadrant | PASS 12 | Four-quadrant table + FAIL_SAME_FRAME + FAIL_VAGUE_TIMING inline. |
| C-06 Conflict identification | PASS 10 | "At least two structural conflicts before building the grid." FAIL_ONE_PARTY inline. |
| C-07 Role framing | PASS 10 | Step 1 = Strategy, Step 2 = PM, Step 3 = UX -- distinct sections. |
| C-08 Critical-path gatekeepers | PASS 10 | "[CRITICAL PATH -- lead time: X]" in Step 1 + FAIL_NO_TIMING inline. |
| C-09 Amendment phase | PASS 5 | Step 8 amendment pass required; update mandate present. |
| C-10 NOT doing framing | PASS 5 | Step 3 NOT-doing statement + FAIL_NO_NOT_DOING inline. |
| C-11 Source-tracking column | PASS 5 | Grid Source column + FAIL_NO_SOURCE inline. |
| C-12 Amendment update mandate | PASS 5 | "update the affected artifact -- not observe without revising" + FAIL_OBSERVATION_ONLY. |
| C-13 Prefilled frame types | PASS 5 | "Frame Type must be distinct per row" + FAIL_SAME_FRAME. |
| C-14 Named failure modes inline | PASS 5 | FAIL_ labels at every step: FAIL_SILENT_INFERENCE, FAIL_ONE_PARTY, FAIL_NO_INERTIA, FAIL_NO_SOURCE, FAIL_PROSE_ONLY, FAIL_MONOLITH_ASSUMPTION, FAIL_NO_NOT_DOING, FAIL_WRONG_ORDER, FAIL_NO_MITIGATION, FAIL_GENERIC_CHAMPION, FAIL_SAME_FRAME, FAIL_VAGUE_TIMING, FAIL_NO_TIMING, FAIL_OBSERVATION_ONLY. 14 inline labels at execution points -- maximum saturation. |
| C-15 Reversed sequence | **FAIL 0** | Sequence is Step 1 (Strategy) → Step 2 (PM Grid) → Step 3 (UX). PM built before UX. Axis not targeted by this variation. |
| C-16 Before/after pair | **FAIL 0** | FAIL_OBSERVATION_ONLY label names the bad form but does NOT show it as an adjacent paired example alongside a correct-form example. A negative label is not a before/after pair. Hypothesis tested: failure-mode density at amendment gate does not incidentally produce C-16. |

**V-03 Total: 120 / 130**

**V-03 diagnostic note**: C-16 requires an adjacent correct-form example, not merely a named failure label. Saturation of FAIL_ labels (C-14 at maximum) does not substitute for the structural paired example. The v4 rule for C-14 vs C-16 distinction is confirmed: they are genuinely independent criteria.

---

### V-04: Minimal Combo -- C-15 + C-16

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 CODEOWNERS fallback | PASS 12 | "ask exactly one question: 'What org or team is this decision for?' Do not infer silently." First step. |
| C-02 Power/Interest grid | PASS 12 | Phase 3 grid with Source column, quadrant labels, 4+ row minimum, critical-path notes. |
| C-03 Veto risks ranked | PASS 12 | "ordered by probability -- highest first. Not alphabetically, not by grid order." Rank table. |
| C-04 Champion concrete action | PASS 12 | Specific schedulable examples; "Generic 'engage the champion' language does not pass." |
| C-05 Comms per quadrant | PASS 12 | Frame Types distinct per row; relative timing; inertia row displacement note. |
| C-06 Conflict identification | PASS 10 | "at least two structural conflicts. Each entry requires both parties named and nature of tension." |
| C-07 Role framing | PASS 10 | Phase 1 = Strategy, Phase 2 = UX, Phase 3 = PM -- three distinct phases. |
| C-08 Critical-path gatekeepers | PASS 10 | "[CRITICAL PATH -- lead time: X]" in Phase 1; confirmed in Step 7. |
| C-09 Amendment phase | PASS 5 | "Minimum one amendment required." Full update protocol. |
| C-10 NOT doing framing | PASS 5 | Phase 2, item 4: "One NOT-doing statement -- what this product explicitly does not provide for them." |
| C-11 Source-tracking column | PASS 5 | Phase 3 grid Source column; four label definitions including `amendment`. |
| C-12 Amendment update mandate | PASS 5 | "no observation without revision"; four-point per-amendment checklist. |
| C-13 Prefilled frame types | PASS 5 | "Frame Type must be distinct per row" with five label examples enforced. |
| C-14 Named failure modes inline | PASS 5 | "Generic 'engage the champion' language does not pass" at Step 5; bad-form example at Step 8 names the failure mode at execution; "no observation without revision" inline. Two+ named failure modes at execution steps. |
| C-15 Reversed sequence | PASS 5 | Phase 1 (Strategy) → Phase 2 (UX) → Phase 3 (PM: "build this last"). Phase 3 header: "Build this grid now -- after Phase 1 and Phase 2 are complete." Structural enforcement with explicit instruction. |
| C-16 Before/after pair | PASS 5 | Step 8: "the two forms side by side:" → "**Bad form** (do not do this):" [observation-only prose] adjacent to "**Correct form** (required):" [full structured amendment with grid + veto + comms updates]. Both forms immediate, labeled, at execution point. |

**V-04 Total: 130 / 130**

---

### V-05: Full 130 Target

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 CODEOWNERS fallback | PASS 12 | "ask exactly one question... Do not infer. Do not proceed on an assumed org." First step; framed as "most consequential check." |
| C-02 Power/Interest grid | PASS 12 | Phase 3 grid with Source column, quadrant labels, minimum 4 rows + FAIL_NO_SOURCE. |
| C-03 Veto risks ranked | PASS 12 | Probability-ordered table + FAIL_WRONG_ORDER. |
| C-04 Champion concrete action | PASS 12 | Specific schedulable examples + FAIL_GENERIC_CHAMPION. |
| C-05 Comms per quadrant | PASS 12 | "Prefill all four Frame Type values before completing the rows. Assign one label per quadrant -- no two rows may share a Frame Type." Strongest C-05/C-13 formulation of any variation. |
| C-06 Conflict identification | PASS 10 | "at least two conflicts. Each entry requires both parties named and nature of tension." + FAIL_ONE_PARTY. |
| C-07 Role framing | PASS 10 | Phase 1 = Strategy, Phase 2 = UX, Phase 3 = PM -- distinct phases. |
| C-08 Critical-path gatekeepers | PASS 10 | "[CRITICAL PATH -- lead time: X]" + FAIL_NO_TIMING. Step 7 confirmation with "specific, not generic" blocking reason required. |
| C-09 Amendment phase | PASS 5 | "Minimum one amendment required." Per-amendment checklist + post-pass `initial-inventory` audit. |
| C-10 NOT doing framing | PASS 5 | Phase 2, item 4 + FAIL_NO_NOT_DOING. |
| C-11 Source-tracking column | PASS 5 | Phase 3 grid Source column + FAIL_NO_SOURCE + five label definitions. |
| C-12 Amendment update mandate | PASS 5 | "no observation without revision" + FAIL_OBSERVATION_ONLY + four-point per-amendment checklist. |
| C-13 Prefilled frame types | PASS 5 | "Prefill all four Frame Type values" + accepted values enumerated including `displacement-acknowledgment`. Most directive C-13 formulation across all rounds. |
| C-14 Named failure modes inline | PASS 5 | FAIL_ labels at every phase gate: FAIL_ONE_PARTY, FAIL_NO_TIMING, FAIL_NO_NOT_DOING, FAIL_NO_SOURCE, FAIL_WRONG_ORDER, FAIL_GENERIC_CHAMPION, FAIL_SAME_FRAME, FAIL_VAGUE_TIMING, FAIL_OBSERVATION_ONLY. Nine inline labels at execution points. |
| C-15 Reversed sequence | PASS 5 | Phase 1 (Strategy) → Phase 2 (UX) → Phase 3 (PM: "Build this grid now -- after Phase 1 and Phase 2 are complete.") Structural labeling + explicit instruction. |
| C-16 Before/after pair | PASS 5 | Step 8: "read both forms before proceeding:" → "**Bad form**:" [observation prose] adjacent to "**Correct form**:" [structured amendment with all tables updated]. |

**V-05 Total: 130 / 130**

---

## Composite Rankings

| Rank | Variation | Score | Gap Criteria |
|------|-----------|-------|--------------|
| 1 | V-04 | 130 / 130 | — |
| 1 | V-05 | 130 / 130 | — |
| 3 | V-01 | 125 / 130 | C-16 (-5) |
| 3 | V-02 | 125 / 130 | C-15 (-5) |
| 5 | V-03 | 120 / 130 | C-15 (-5), C-16 (-5) |

**Golden threshold (>= 80)**: All five variations pass.

---

## Excellence Signals

**What made V-04 and V-05 reach 130 vs 125 in V-01/V-02:**

Both C-15 and C-16 must be present simultaneously. Neither alone is sufficient -- V-01 shows reversed sequence without the paired example reaches 125; V-02 shows the paired example without reversed sequence reaches 125. The two criteria are genuinely independent and additive.

**Key observations from V-04 (minimal combo):**

- C-15 and C-16 require no other criteria to succeed -- the minimal combination is sufficient. V-04 carries no extra FAIL labels, no prefill directives, no named `displacement-acknowledgment` frame type -- just the two new structural patterns on top of a solid v2 baseline.
- The "two forms side by side" framing in V-04's amendment header is slightly different from V-02's "read both forms before proceeding" -- but both reliably trigger C-16. The exact header wording does not appear to be load-bearing.

**V-05-specific patterns not yet in the rubric (v4 candidates):**

1. **Prefill-before-execute directive for Frame Types**: V-05's "Prefill all four Frame Type values before completing the rows" is a generative execution pattern -- it creates the correct output by construction rather than constraining a post-hoc check. C-13 currently measures the output (distinct labels present); this pattern targets the execution path. Could become C-17: "Frame Types assigned before rows are populated" as a stronger variant of C-13.

2. **Named displacement frame type**: V-05 introduces `displacement-acknowledgment` as an explicit Frame Type in the accepted values vocabulary, with "For the inertia stakeholder's quadrant, use `displacement-acknowledgment`..." This encodes the inertia-acknowledgment requirement (currently a prose instruction) into the frame vocabulary itself, making it structurally checkable. Could become a C-18 targeting the inertia row specifically.

**V-03 diagnostic (C-14 vs C-16 independence confirmed):** FAIL_ label saturation at every step does not incidentally produce C-16. The FAIL_OBSERVATION_ONLY label names the bad form without showing the correct form adjacent to it. C-14 and C-16 measure structurally different things -- named prohibition vs paired demonstration. V-03 at 120 closes this question for v4.

---

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["prefill-before-execute directive for frame types: assigning all four frame type labels before populating rows creates correct output by construction rather than post-hoc constraint", "named displacement frame type: introducing displacement-acknowledgment as an explicit accepted frame type value for the inertia stakeholder row encodes the inertia-acknowledgment requirement into the frame vocabulary itself"]}
```
