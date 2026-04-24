## Round 4 Scoring — scout-stakeholders

### V-01: Anti-Pattern Saturation at Every Phase Gate (Single Axis)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 CODEOWNERS fallback | PASS 12 | Step 0: "Check for a CODEOWNERS file... ask exactly one question... FAIL_SILENT_INFERENCE" at first gate. |
| C-02 Power/Interest grid | PASS 12 | Step 2 table with Source, Quadrant labels, 4-row minimum; FAIL_NO_SOURCE + FAIL_PROSE_ONLY inline. |
| C-03 Veto risks ranked | PASS 12 | "ordered by probability -- highest first" + FAIL_WRONG_ORDER + FAIL_NO_MITIGATION in Step 4. |
| C-04 Champion concrete action | PASS 12 | Specific schedulable examples at Step 5 + FAIL_GENERIC_CHAMPION inline. |
| C-05 Comms per quadrant | PASS 12 | Step 6: distinct Frame Types + quantified relative timing required. |
| C-06 Conflict identification | PASS 10 | "at least two structural conflicts... both parties named... nature of tension" + FAIL_ONE_PARTY. |
| C-07 Role framing | PASS 10 | Step 1 = Strategy, Step 2 = PM, Step 3 = UX — three structurally distinct sections. |
| C-08 Critical-path gatekeepers | PASS 10 | "[CRITICAL PATH -- lead time: X]" in Step 1 + FAIL_NO_GATEKEEPER_TIMING at Step 7. |
| C-09 Amendment phase | PASS 5 | "Minimum one amendment required" + update mandate at Step 8. |
| C-10 NOT-doing framing | PASS 5 | Step 3: "One NOT-doing statement: what this product explicitly does not provide" + FAIL_NO_NOT_DOING. |
| C-11 Source-tracking column | PASS 5 | Step 2 Source column; four origin labels defined. |
| C-12 Amendment update mandate | PASS 5 | "Update the affected table... do not observe without updating." |
| C-13 Prefilled frame types | PASS 5 | "Frame Type must be distinct per row" with five labeled values. |
| C-14 Named failure modes inline | PASS 5 | 14 FAIL_ labels at execution points — maximum saturation. |
| C-15 Reversed sequence | **FAIL 0** | Step 1 (Strategy) → Step 2 (PM Grid) → Step 3 (UX). PM built before UX. Deliberately excluded. |
| C-16 Before/after pair | **FAIL 0** | FAIL_OBSERVATION_ONLY label at Step 8 names the bad form but no paired correct-form example adjacent to it. Deliberately excluded. |
| C-17 Anti-pattern saturation | PASS 5 | FAIL_ labels at every gate: Step 0 (FAIL_SILENT_INFERENCE), Step 1 (FAIL_ONE_PARTY, FAIL_NO_INERTIA), Step 2 (FAIL_NO_SOURCE, FAIL_PROSE_ONLY), Step 3 (FAIL_MONOLITH_ASSUMPTION, FAIL_NO_NOT_DOING), Step 4 (FAIL_WRONG_ORDER, FAIL_NO_MITIGATION), Step 5 (FAIL_GENERIC_CHAMPION), Step 6 (FAIL_SAME_FRAME, FAIL_VAGUE_TIMING), Step 7 (FAIL_NO_GATEKEEPER_TIMING), Step 8 (FAIL_OBSERVATION_ONLY). All 9 gates covered. |

**V-01 Total: 125 / 135**

---

### V-02: Inertia Prominence as Structural Section

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 CODEOWNERS fallback | PASS 12 | Step 0: "ask exactly one question... Do not infer silently." |
| C-02 Power/Interest grid | PASS 12 | Step 2 table with Source, quadrant, 4-row minimum; inertia stakeholder required with `[INERTIA]` tag. |
| C-03 Veto risks ranked | PASS 12 | "ordered by probability -- highest first. Not alphabetically, not by grid sequence." Rank table with Prob + Impact + Mitigation. |
| C-04 Champion concrete action | PASS 12 | Schedulable examples at Step 5; "Generic 'engage the champion' language is not a champion action." |
| C-05 Comms per quadrant | PASS 12 | Step 6: distinct Frame Types per row, `displacement-acknowledgment` required for inertia row; quantified timing. |
| C-06 Conflict identification | PASS 10 | "at least two structural conflicts... both parties named... nature of tension." |
| C-07 Role framing | PASS 10 | Step 1 = Strategy (1a conflict, 1b inertia, 1c gatekeepers), Step 2 = PM, Step 3 = UX — three structurally distinct sections. |
| C-08 Critical-path gatekeepers | PASS 10 | "[CRITICAL PATH -- lead time: X]" at Step 1c + Step 7 requires blocking reason + lead time. |
| C-09 Amendment phase | PASS 5 | "Minimum one amendment required" + five-point update protocol at Step 8. |
| C-10 NOT-doing framing | PASS 5 | Step 3: "One NOT-doing statement" per segment; inertia variant requires displacement-specific NOT-doing. |
| C-11 Source-tracking column | PASS 5 | Step 2 Source column; four origin labels defined. |
| C-12 Amendment update mandate | PASS 5 | "update the affected table -- do not observe without updating." |
| C-13 Prefilled frame types | PASS 5 | "One label per row. No two rows may share the same Frame Type." Accepted values enumerated including `displacement-acknowledgment`. |
| C-14 Named failure modes inline | PASS 5 | "Generic 'engage the champion' language is not a champion action" at Step 5; "do not observe without updating" at Step 8. Two inline anti-pattern descriptions at execution points. |
| C-15 Reversed sequence | **FAIL 0** | Step 1 (Strategy) → Step 2 (PM Grid) → Step 3 (UX). PM built before UX. Deliberately excluded. |
| C-16 Before/after pair | **FAIL 0** | Step 8 gives "do not observe without updating" and a five-item checklist, but no bad-form example adjacent to a correct-form example. Deliberately excluded. |
| C-17 Anti-pattern saturation | **FAIL 0** | Steps 0, 1, 2, 3, 4, 6, 7, 8 carry no FAIL_ labels. Step 5 carries a prose prohibition but not a FAIL_ token. Multiple gates uncovered. |

**V-02 Total: 120 / 135**

---

### V-03: Prefill-Before-Execute for Frame Types

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 CODEOWNERS fallback | PASS 12 | Step 0: "ask exactly one question: 'What org or team is this decision for?' Do not infer silently." |
| C-02 Power/Interest grid | PASS 12 | Step 2 table with Source, quadrant, 4-row minimum + FAIL_NO_SOURCE inline. |
| C-03 Veto risks ranked | PASS 12 | "ordered by probability -- highest first. Not alphabetically, not by grid sequence." Table with Prob + Impact + Mitigation + FAIL_WRONG_ORDER. |
| C-04 Champion concrete action | PASS 12 | Schedulable examples at Step 5 + FAIL_GENERIC_CHAMPION inline. |
| C-05 Comms per quadrant | PASS 12 | Step 6: prefill table first, then full table; distinct Frame Types enforced; quantified timing required. |
| C-06 Conflict identification | PASS 10 | "at least two structural conflicts... both parties named... nature of tension." |
| C-07 Role framing | PASS 10 | Step 1 = Strategy, Step 2 = PM, Step 3 = UX — three structurally distinct sections. |
| C-08 Critical-path gatekeepers | PASS 10 | "[CRITICAL PATH -- lead time: X]" at Step 1 + Step 7 requires blocking reason + hard deadline. |
| C-09 Amendment phase | PASS 5 | "Minimum one amendment required" + four-item update protocol + FAIL_OBSERVATION_ONLY. |
| C-10 NOT-doing framing | PASS 5 | Step 3: "One NOT-doing statement: what this product explicitly does not provide." |
| C-11 Source-tracking column | PASS 5 | Step 2 Source column + FAIL_NO_SOURCE. |
| C-12 Amendment update mandate | PASS 5 | "do not observe without updating" + FAIL_OBSERVATION_ONLY at Step 8. |
| C-13 Prefilled frame types | PASS 5 | Explicit prefill table before row population; accepted values enumerated; `FAIL_SAME_FRAME` if prefill not honored. Strongest C-13 implementation to date. |
| C-14 Named failure modes inline | PASS 5 | FAIL_NO_SOURCE (Step 2), FAIL_WRONG_ORDER (Step 4), FAIL_GENERIC_CHAMPION (Step 5), FAIL_SAME_FRAME + FAIL_VAGUE_TIMING (Step 6), FAIL_OBSERVATION_ONLY (Step 8) — six inline labels at execution points. |
| C-15 Reversed sequence | **FAIL 0** | Step 1 (Strategy) → Step 2 (PM) → Step 3 (UX). PM before UX. Deliberately excluded. |
| C-16 Before/after pair | **FAIL 0** | FAIL_OBSERVATION_ONLY at Step 8 names the failure but no adjacent correct-form example. Deliberately excluded. |
| C-17 Anti-pattern saturation | **FAIL 0** | Steps 0, 1, 3, 7 have no FAIL_ labels. Multiple gates uncovered. |

**V-03 Total: 120 / 135**

**V-03 diagnostic**: Prefill-before-execute is the strongest C-13 formulation yet, but the rubric measures the output (distinct labels present), not the execution path. V-03 at 120 — same as V-02 without prefill — confirms the pattern is not yet discriminating. The prefill pattern targets C-13 in a different way than the rubric currently measures. This is a confirmed v5 candidate axis.

---

### V-04: Minimal Triple Combo — C-15 + C-16 + C-17

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 CODEOWNERS fallback | PASS 12 | Step 0: explicit fallback chain + FAIL_SILENT_INFERENCE. |
| C-02 Power/Interest grid | PASS 12 | Phase 3 grid "build this last" — Source column, quadrant labels, 4-row minimum + FAIL_NO_SOURCE + FAIL_PROSE_ONLY. |
| C-03 Veto risks ranked | PASS 12 | "ordered by probability -- highest first" + FAIL_WRONG_ORDER + FAIL_NO_MITIGATION at Step 4. |
| C-04 Champion concrete action | PASS 12 | Schedulable examples + FAIL_GENERIC_CHAMPION at Step 5. |
| C-05 Comms per quadrant | PASS 12 | Step 6: distinct Frame Types, inertia row displacement note, quantified timing + FAIL_SAME_FRAME + FAIL_VAGUE_TIMING. |
| C-06 Conflict identification | PASS 10 | Phase 1a: "at least two structural conflicts... both parties named" + FAIL_ONE_PARTY. |
| C-07 Role framing | PASS 10 | Phase 1 = Strategy, Phase 2 = UX, Phase 3 = PM — three structurally separate phases. |
| C-08 Critical-path gatekeepers | PASS 10 | Phase 1c: "[CRITICAL PATH -- lead time: X]" + FAIL_NO_TIMING; Step 7: FAIL_GATEKEEPER_INCOMPLETE requires both blocking reason and timing. |
| C-09 Amendment phase | PASS 5 | "Minimum one amendment required" + four-point update checklist + post-pass inventory audit. |
| C-10 NOT-doing framing | PASS 5 | Phase 2, item 4: "One NOT-doing statement" + FAIL_NO_NOT_DOING. |
| C-11 Source-tracking column | PASS 5 | Phase 3 Source column + five label definitions (including `amendment`) + FAIL_NO_SOURCE. |
| C-12 Amendment update mandate | PASS 5 | "no observation without revision" + FAIL_OBSERVATION_ONLY at Step 8. |
| C-13 Prefilled frame types | PASS 5 | "Frame Type must be distinct per row" with five values; inertia row displacement note. |
| C-14 Named failure modes inline | PASS 5 | FAIL_ labels at every gate: FAIL_SILENT_INFERENCE, FAIL_ONE_PARTY, FAIL_NO_INERTIA, FAIL_NO_TIMING (Phase 1), FAIL_NO_NOT_DOING, FAIL_MONOLITH_ASSUMPTION (Phase 2), FAIL_NO_SOURCE, FAIL_PROSE_ONLY (Phase 3), FAIL_WRONG_ORDER, FAIL_NO_MITIGATION (Step 4), FAIL_GENERIC_CHAMPION (Step 5), FAIL_SAME_FRAME, FAIL_VAGUE_TIMING (Step 6), FAIL_GATEKEEPER_INCOMPLETE (Step 7), FAIL_OBSERVATION_ONLY (Step 8). |
| C-15 Reversed sequence | PASS 5 | Phase 1 (Strategy) → Phase 2 (UX) → Phase 3 (PM): "Build this grid now -- after Phase 1 and Phase 2 are complete." Structural header enforces PM-last. |
| C-16 Before/after pair | PASS 5 | Step 8: "Amendment execution rule -- read both forms before proceeding:" → **Bad form** (observation prose, labeled, no table updates) immediately adjacent to **Correct form** (structured amendment with grid + veto + comms all updated). Both forms labeled, adjacent, at execution point. |
| C-17 Anti-pattern saturation | PASS 5 | FAIL_ labels confirmed at all 9 gates: Step 0, Phase 1 (sub-steps 1a/1b/1c), Phase 2, Phase 3, Steps 4-8. No gate uncovered. 15 inline labels total. |

**V-04 Total: 135 / 135**

---

### V-05: Full 135 Target — Triple Combo + Prefill + Displacement Vocabulary

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 CODEOWNERS fallback | PASS 12 | Step 0: "Do not infer. Do not proceed on an assumed org. This is the first and most consequential check." + FAIL_SILENT_INFERENCE. |
| C-02 Power/Interest grid | PASS 12 | Phase 3 grid "build this last" + FAIL_NO_SOURCE + FAIL_PROSE_ONLY + `[INERTIA]` tag required in Notes. |
| C-03 Veto risks ranked | PASS 12 | "ordered by probability -- highest first" + FAIL_WRONG_ORDER + FAIL_NO_MITIGATION. Inertia veto rank enforcement: "do not artificially lower structural resistance." |
| C-04 Champion concrete action | PASS 12 | Schedulable examples with calendar phrasing + FAIL_GENERIC_CHAMPION at Step 5. |
| C-05 Comms per quadrant | PASS 12 | Step 6: prefill table with distinct labels before row population, accepted values including `displacement-acknowledgment`, `displacement-acknowledgment` mandatory for inertia row, quantified timing + FAIL_SAME_FRAME + FAIL_VAGUE_TIMING. |
| C-06 Conflict identification | PASS 10 | Phase 1a: "at least two structural conflicts... both parties named" + FAIL_ONE_PARTY. |
| C-07 Role framing | PASS 10 | Phase 1 = Strategy, Phase 2 = UX, Phase 3 = PM — three structurally separate phases. |
| C-08 Critical-path gatekeepers | PASS 10 | Phase 1c + FAIL_NO_TIMING; Step 7 + FAIL_GATEKEEPER_INCOMPLETE. |
| C-09 Amendment phase | PASS 5 | "Minimum one amendment required" + four-point update checklist + post-pass `initial-inventory` audit. |
| C-10 NOT-doing framing | PASS 5 | Phase 2 NOT-doing + FAIL_NO_NOT_DOING; inertia segment: "must address what the new approach does not preserve from the current approach." |
| C-11 Source-tracking column | PASS 5 | Phase 3 Source column + five label definitions + FAIL_NO_SOURCE. "`initial-inventory` after the amendment pass is a visible gap" — strongest C-11 framing. |
| C-12 Amendment update mandate | PASS 5 | "no observation without revision" + FAIL_OBSERVATION_ONLY + four-point checklist. |
| C-13 Prefilled frame types | PASS 5 | Prefill table before row content; accepted values enumerated; `displacement-acknowledgment` mandatory for inertia row; FAIL_SAME_FRAME tied to prefill enforcement. |
| C-14 Named failure modes inline | PASS 5 | FAIL_ labels at all gates: FAIL_SILENT_INFERENCE (Step 0), FAIL_ONE_PARTY, FAIL_NO_INERTIA, FAIL_NO_TIMING (Phase 1), FAIL_NO_NOT_DOING, FAIL_MONOLITH_ASSUMPTION (Phase 2), FAIL_NO_SOURCE, FAIL_PROSE_ONLY (Phase 3), FAIL_WRONG_ORDER, FAIL_NO_MITIGATION (Step 4), FAIL_GENERIC_CHAMPION (Step 5), FAIL_SAME_FRAME, FAIL_VAGUE_TIMING (Step 6), FAIL_GATEKEEPER_INCOMPLETE (Step 7), FAIL_OBSERVATION_ONLY (Step 8). |
| C-15 Reversed sequence | PASS 5 | Phase 1 (Strategy) → Phase 2 (UX) → Phase 3 (PM: "Build this grid now -- after Phase 1 and Phase 2 are complete."). |
| C-16 Before/after pair | PASS 5 | Step 8: "read both forms before proceeding:" → **Bad form** (observation-only prose) adjacent to **Correct form** (full structured amendment with all three tables updated). |
| C-17 Anti-pattern saturation | PASS 5 | FAIL_ labels at all 9 gates — same coverage as V-04. 15 inline labels. |

**V-05 Total: 135 / 135**

---

## Composite Rankings

| Rank | Variation | Score | Gap Criteria |
|------|-----------|-------|--------------|
| 1 | V-04 | 135 / 135 | — |
| 1 | V-05 | 135 / 135 | — |
| 3 | V-01 | 125 / 135 | C-15 (−5), C-16 (−5) |
| 4 | V-02 | 120 / 135 | C-15 (−5), C-16 (−5), C-17 (−5) |
| 4 | V-03 | 120 / 135 | C-15 (−5), C-16 (−5), C-17 (−5) |

**Golden threshold (>= 80)**: All five variations pass.

---

## Excellence Signals

**V-04 and V-05 both reach 135 — triple combo is sufficient; additions in V-05 do not improve the score:**

The round's central finding is a diagnostic, not an improvement: V-05 adds prefill-before-execute and full displacement vocabulary (`[INERTIA]` tracking, `displacement-acknowledgment` required for inertia row) on top of V-04's minimal triple combo. Both score 135. The rubric does not yet differentiate them. This is a clean signal that V-05's additions target behavior beyond what the current 17 criteria measure.

**V-03 prefill diagnostic confirmed (second confirmation):** V-03 at 120 — same as variations without prefill — and V-05 at 135 — same as V-04 without prefill — both confirm that prefill-before-execute does not independently produce points under the current rubric. It targets the execution path for C-13, not the output C-13 measures.

**V-02 inertia diagnostic confirmed:** Inertia prominence as a structural section (displacement vocabulary, `[INERTIA]` tag, `displacement-acknowledgment` frame type requirement) scores 120 without the triple combo and 135 with it (V-05). The inertia additions are not independently scored — they are absorbed by C-10, C-11, C-13 — but V-05 demonstrates they coexist cleanly with the triple combo.

**New pattern — cross-phase inertia commitment (v5 C-18 candidate):** V-05 is the first variation to enforce a named inertia stakeholder thread across all phases: Phase 1b (named with `current-approach`/`displaced-by` vocabulary), Phase 3 grid (`[INERTIA]` tag required in Notes), Step 4 veto list (rank protected from artificial depression), Step 6 comms (`displacement-acknowledgment` mandatory). V-04 achieves 135 without this; V-05 achieves 135 with it. The thread is not yet independently scored but represents a structural commitment pattern that no other variation targets as a first-class design element. Could become C-18: "Inertia stakeholder carries a consistent named marker through every subsequent phase after Phase 1 identification."

---

```json
{"top_score": 135, "all_essential_pass": true, "new_patterns": ["cross-phase inertia commitment: V-05 enforces a named inertia stakeholder thread across all phases (Phase 1b displacement vocabulary, [INERTIA] tag in grid, rank-protected veto entry, displacement-acknowledgment mandatory in comms) — V-04 reaches 135 without this; V-05 reaches 135 with it; the pattern is not yet discriminating but is the strongest unexploited structural commitment in the top-scoring variation"]}
```
