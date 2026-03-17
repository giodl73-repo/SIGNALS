Now I have all the variation content. Let me score each variation against the v5 rubric.

---

## Round 5 — scout-stakeholders — Scoring

### Rubric Summary (v5)

| Tier | Criteria | Pts |
|------|----------|-----|
| Essential (×5) | C-01 through C-05 | 12 each = 60 |
| Recommended (×3) | C-06 through C-08 | 10 each = 30 |
| Aspirational (×11) | C-09 through C-19 | 5 each = 55 |
| **Max** | | **145** |

---

### V-01 — Inertia Framing: Three-Position Structural Elevation (C-18 alone)

**Design intent**: C-18 single axis. Standard PM-first sequence (fails C-15). Three FAIL labels (fails C-17 saturation). No before/after pair (fails C-16). Inline Frame Type enumeration (fails C-19).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | CODEOWNERS fallback | **PASS** | Step 0 checks CODEOWNERS; asks one question if absent; "Do not infer silently" present |
| C-02 | Power/Interest grid | **PASS** | Grid with Stakeholder / Power / Interest / Quadrant / [INERTIA] / Source / Notes — 4+ rows implied |
| C-03 | Veto risks ranked by probability | **PASS** | Step 4 ranked table required, highest first, with probability + impact |
| C-04 | Champion with concrete action | **PASS** | Step 5 requires schedulable action with examples ("demo slot", "early access") |
| C-05 | Communication strategy per quadrant | **PASS** | Step 6 table with Key Message + Timing per quadrant row |
| C-06 | Conflict identification | **PASS** | Step 1a requires two+ conflicts with both parties named |
| C-07 | Role framing | **PASS** | Strategy (Step 1) / PM (Step 2) / UX (Step 3) structurally distinct |
| C-08 | Critical-path gatekeepers flagged | **PASS** | Step 1c: `[CRITICAL PATH -- lead time: X]` label required |
| C-09 | Amendment phase | **PASS** | Step 8 with update mandate |
| C-10 | "What we are NOT doing" | **PASS** | Step 3 requires one NOT-doing statement per segment |
| C-11 | Source-tracking column | **PASS** | Grid has Source column with origin labels |
| C-12 | Amendment loop with update mandate | **PASS** | Step 8: "Update the affected table… do not observe without updating" |
| C-13 | Prefilled frame types in comms table | **PASS** | Step 6 has Frame Type column; accepted values listed; distinct per row required |
| C-14 | Named failure modes inline | **PASS** | FAIL_SILENT_INFERENCE, FAIL_NO_INERTIA_SUBSTEP, FAIL_MISSING_INERTIA_TAG = 3 inline labels |
| C-15 | Reversed sequence | **FAIL** | Standard sequence: Steps 1→2→3 (Strategy→PM→UX), not Phase 1→2→3 reversed |
| C-16 | Amendment before/after pair | **FAIL** | Step 8 gives positive instructions only; no bad-form example shown adjacent |
| C-17 | FAIL saturation at every gate | **FAIL** | Only ~3 FAIL labels (FAIL_SILENT_INFERENCE, FAIL_NO_INERTIA_SUBSTEP, FAIL_MISSING_INERTIA_TAG). Steps 3, 4, 5, 7 have no inline FAIL labels — coverage is not complete |
| C-18 | Inertia structural elevation | **PASS** | All three positions present: (1) Step 1b sub-step with current-approach/displaced-by/displacement-type vocabulary; (2) `[INERTIA]` column in grid (not Notes); (3) `displacement-acknowledgment` required + FAIL_NO_DISPLACEMENT_FRAME at Step 6 |
| C-19 | Frame Type prefill constraint table | **FAIL** | Step 6 enumerates accepted values inline in instructions; no separate Step 6a prefill table |

**Scores**:
- Essential: 5×12 = **60** ✓
- Recommended: 3×10 = **30** ✓
- Aspirational: C-09✓ C-10✓ C-11✓ C-12✓ C-13✓ C-14✓ C-15✗ C-16✗ C-17✗ C-18✓ C-19✗ = 7×5 = **35**

**Total: 125/145** — matches hypothesis exactly.

---

### V-02 — Standalone Frame Type Prefill Table (C-19 alone)

**Design intent**: C-19 single axis. Standard sequence (fails C-15). No before/after pair (fails C-16). Moderate FAIL coverage, not every gate (fails C-17). Inertia mentioned but not structurally elevated (fails C-18).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | CODEOWNERS fallback | **PASS** | Step 0 present with FAIL_SILENT_INFERENCE |
| C-02 | Power/Interest grid | **PASS** | Grid at Step 2 with required columns |
| C-03 | Veto risks ranked by probability | **PASS** | Step 4 ranked table |
| C-04 | Champion with concrete action | **PASS** | Step 5 with calendar examples |
| C-05 | Communication strategy per quadrant | **PASS** | Step 6b communication table with timing |
| C-06 | Conflict identification | **PASS** | Step 1 item 1 requires two+ conflicts with parties named |
| C-07 | Role framing | **PASS** | Strategy (Step 1) / PM (Step 2) / UX (Step 3) distinct |
| C-08 | Critical-path gatekeepers | **PASS** | Step 1 item 3: `[CRITICAL PATH -- lead time: X]` |
| C-09 | Amendment phase | **PASS** | Step 8 with update mandate + FAIL_OBSERVATION_ONLY |
| C-10 | NOT-doing framing | **PASS** | Step 3 item 3: NOT-doing statement required with FAIL_NO_NOT_DOING |
| C-11 | Source-tracking column | **PASS** | Step 2 grid has Source column with origin labels |
| C-12 | Amendment loop with update mandate | **PASS** | Step 8: "Update the affected table" + note what changed |
| C-13 | Prefilled frame types in comms table | **PASS** | Step 6b Frame Type column matches Step 6a; FAIL_SAME_FRAME present |
| C-14 | Named failure modes inline | **PASS** | FAIL_SILENT_INFERENCE, FAIL_ONE_PARTY, FAIL_NO_SOURCE, FAIL_NO_NOT_DOING, FAIL_WRONG_ORDER, FAIL_GENERIC_CHAMPION, FAIL_SAME_FRAME, FAIL_VAGUE_TIMING, FAIL_OBSERVATION_ONLY = many inline labels |
| C-15 | Reversed sequence | **FAIL** | Standard sequence: Steps 0→1→2→3 (conflict/Strategy→PM grid→UX→…) |
| C-16 | Amendment before/after pair | **FAIL** | Step 8 has no before/after bad-form example; positive mandate only |
| C-17 | FAIL saturation at every gate | **FAIL** | Step 7 has no FAIL label; Step 5 has FAIL_GENERIC_CHAMPION but Step 1c has no FAIL for gatekeeper-without-timing. Not every gate covered. Actually let me re-check: Step 1 has FAIL_ONE_PARTY, Step 2 has FAIL_NO_SOURCE, Step 3 has FAIL_NO_NOT_DOING, Step 4 has FAIL_WRONG_ORDER, Step 5 has FAIL_GENERIC_CHAMPION, Step 6a has assignment rules, Step 6b has FAIL_SAME_FRAME + FAIL_VAGUE_TIMING, Step 7 has **no FAIL label**, Step 8 has FAIL_OBSERVATION_ONLY. Step 7 is uncovered. FAIL. |
| C-18 | Inertia structural elevation | **FAIL** | Step 1 item 2 names inertia stakeholder but: no sub-step with current-approach/displaced-by/displacement-type vocabulary (just "Name who benefits… state why their resistance is structural"), no `[INERTIA]` column in grid (grid is Stakeholder/Power/Interest/Quadrant/Source/Notes only), no `displacement-acknowledgment` mandate at Step 6 for inertia rows. All three positions absent. |
| C-19 | Frame Type prefill constraint table | **PASS** | Step 6a is a standalone step with an empty prefill table, accepted values list, and explicit "do not proceed to Step 6b until complete" rule. Structurally distinct from inline enumeration. |

**Scores**:
- Essential: 5×12 = **60** ✓
- Recommended: 3×10 = **30** ✓
- Aspirational: C-09✓ C-10✓ C-11✓ C-12✓ C-13✓ C-14✓ C-15✗ C-16✗ C-17✗ C-18✗ C-19✓ = 7×5 = **35**

**Total: 125/145** — matches hypothesis exactly.

---

### V-03 — Role Sequence: Analysis-Before-Synthesis (C-15 alone)

**Design intent**: C-15 single axis test. No FAIL saturation (fails C-17). No before/after pair (fails C-16). Inertia mentioned but not structurally elevated (fails C-18). Inline Frame Type enumeration (fails C-19).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | CODEOWNERS fallback | **PASS** | Step 0: CODEOWNERS check, ask one question if absent, "Never assume an org structure" |
| C-02 | Power/Interest grid | **PASS** | Phase 3 grid with Stakeholder/Power/Interest/Quadrant/Source/Notes |
| C-03 | Veto risks ranked by probability | **PASS** | Step 4 ranked table |
| C-04 | Champion with concrete action | **PASS** | Step 5 with calendar examples |
| C-05 | Communication strategy per quadrant | **PASS** | Step 6 table with accepted Frame Types and timing requirement |
| C-06 | Conflict identification | **PASS** | Phase 1a: two+ conflicts with both parties named |
| C-07 | Role framing | **PASS** | Phase 1 (Strategy) / Phase 2 (UX) / Phase 3 (PM) — structurally distinct with explicit headers |
| C-08 | Critical-path gatekeepers | **PASS** | Phase 1c: `[CRITICAL PATH -- lead time: X]` required; gatekeeper without timing = incomplete entry |
| C-09 | Amendment phase | **PASS** | Step 8 with update mandate |
| C-10 | NOT-doing framing | **PASS** | Phase 2 item 4: NOT-doing statement required per segment |
| C-11 | Source-tracking column | **PASS** | Phase 3 grid has Source column with definitions |
| C-12 | Amendment loop with update mandate | **PASS** | Step 8: "Update the affected table"; "Writing a finding without updating is not an amendment" |
| C-13 | Prefilled frame types in comms table | **PASS** | Step 6 has Frame Type column; accepted values listed inline; distinct per row required |
| C-14 | Named failure modes inline | **PARTIAL** | Only one inline FAIL label found at Phase 1c area ("A gatekeeper without a timing note is an incomplete entry" — not a FAIL_ label). No explicit FAIL_ labels present. Wait — re-reading V-03: there are no FAIL_ labels at all in V-03. The instructions say "Never assume an org structure" at Step 0 but no FAIL_ label. Phase 1a says "A single stakeholder's concern is not a conflict" but no FAIL_ label. Phase 1c says "A gatekeeper without a timing note is an incomplete entry" — no FAIL_ label. Step 6: "Each row must carry a distinct Frame Type" — no FAIL_ label. Step 8: "Writing a finding without updating a table is not an amendment" — no FAIL_ label. **Zero explicit FAIL_ labels** → C-14 requires "two or more inline anti-pattern labels placed at the steps where those failures occur." These are expressed as prose warnings, not labeled patterns. FAIL. |
| C-15 | Reversed sequence | **PASS** | Explicit: "Run this phase first. The Power/Interest Grid is built in Phase 3, not here." Phase 1 = Strategy conflict analysis, Phase 2 = UX segment analysis, Phase 3 = PM grid construction. "Grid construction is synthesis, not discovery." |
| C-16 | Amendment before/after pair | **FAIL** | Step 8 gives positive mandate only ("Update the affected table"); no bad-form example |
| C-17 | FAIL saturation at every gate | **FAIL** | No FAIL_ labels present; C-17 requires every gate to have at least one |
| C-18 | Inertia structural elevation | **FAIL** | Phase 1b names the inertia stakeholder but: no current-approach/displaced-by/displacement-type fields required; no `[INERTIA]` column in grid (grid is Stakeholder/Power/Interest/Quadrant/Source/Notes only); Step 6 has no `displacement-acknowledgment` mandate for inertia rows |
| C-19 | Frame Type prefill constraint | **FAIL** | Step 6 enumerates accepted values inline; no separate 6a prefill table |

**Note on C-14**: V-03 uses prose anti-pattern warnings ("A single stakeholder's concern listed alone is not a conflict", "Writing a finding without updating a table is not an amendment") but none are formatted as FAIL_ labels. C-14 pass condition requires "two or more inline anti-pattern labels" — the word "labels" matters. FAIL.

**Scores**:
- Essential: 5×12 = **60** ✓
- Recommended: 3×10 = **30** ✓
- Aspirational: C-09✓ C-10✓ C-11✓ C-12✓ C-13✓ C-14✗ C-15✓ C-16✗ C-17✗ C-18✗ C-19✗ = 6×5 = **30**

**Total: 120/145** — matches hypothesis exactly. C-15 alone without FAIL coverage yields 120 (not 125), confirming the hypothesis: "If ~120/145, the sequence alone without FAIL coverage is insufficient."

---

### V-04 — Combination: C-15 + C-16 + C-17 + C-18

**Design intent**: Proven R4 triple (C-15+C-16+C-17) plus C-18. Expected 140/145 (no C-19).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | CODEOWNERS fallback | **PASS** | Step 0 with FAIL_SILENT_INFERENCE |
| C-02 | Power/Interest grid | **PASS** | Phase 3 grid with [INERTIA] column |
| C-03 | Veto risks ranked by probability | **PASS** | Step 4 ranked table |
| C-04 | Champion with concrete action | **PASS** | Step 5 with calendar examples |
| C-05 | Communication strategy per quadrant | **PASS** | Step 6 table with timing |
| C-06 | Conflict identification | **PASS** | Phase 1a: two+ named-party conflicts |
| C-07 | Role framing | **PASS** | Phase 1 / Phase 2 / Phase 3 distinct |
| C-08 | Critical-path gatekeepers | **PASS** | Phase 1c with FAIL_NO_TIMING |
| C-09 | Amendment phase | **PASS** | Step 8 with update mandate |
| C-10 | NOT-doing framing | **PASS** | Phase 2 with FAIL_NO_NOT_DOING |
| C-11 | Source-tracking column | **PASS** | Phase 3 grid Source column with labels |
| C-12 | Amendment loop with update mandate | **PASS** | Step 8: "no observation without revision" |
| C-13 | Prefilled frame types in comms table | **PASS** | Step 6 Frame Type column; distinct values required; FAIL_SAME_FRAME |
| C-14 | Named failure modes inline | **PASS** | FAIL_SILENT_INFERENCE, FAIL_ONE_PARTY, FAIL_NO_INERTIA, FAIL_NO_TIMING, FAIL_NO_NOT_DOING, FAIL_MONOLITH_ASSUMPTION, FAIL_NO_SOURCE, FAIL_PROSE_ONLY, FAIL_MISSING_INERTIA_TAG, FAIL_WRONG_ORDER, FAIL_NO_MITIGATION, FAIL_GENERIC_CHAMPION, FAIL_SAME_FRAME, FAIL_VAGUE_TIMING, FAIL_NO_DISPLACEMENT_FRAME, FAIL_GATEKEEPER_INCOMPLETE, FAIL_OBSERVATION_ONLY = 17 inline labels |
| C-15 | Reversed sequence | **PASS** | "Run Phase 1 first. The grid is built in Phase 3, after Phases 1 and 2 are complete." Explicit at Phase 1 and Phase 3 headers. |
| C-16 | Amendment before/after pair | **PASS** | Step 8 shows: **Bad form** (prose observation, italic) immediately adjacent to **Correct form** (Amendment 1 with full table updates) |
| C-17 | FAIL saturation at every gate | **PASS** | Checking all gates: Step 0 ✓ (FAIL_SILENT_INFERENCE), Phase 1a ✓ (FAIL_ONE_PARTY), Phase 1b ✓ (FAIL_NO_INERTIA), Phase 1c ✓ (FAIL_NO_TIMING), Phase 2 ✓ (FAIL_NO_NOT_DOING + FAIL_MONOLITH_ASSUMPTION), Phase 3 ✓ (FAIL_NO_SOURCE + FAIL_PROSE_ONLY + FAIL_MISSING_INERTIA_TAG), Step 4 ✓ (FAIL_WRONG_ORDER + FAIL_NO_MITIGATION), Step 5 ✓ (FAIL_GENERIC_CHAMPION), Step 6 ✓ (FAIL_SAME_FRAME + FAIL_VAGUE_TIMING + FAIL_NO_DISPLACEMENT_FRAME), Step 7 ✓ (FAIL_GATEKEEPER_INCOMPLETE), Step 8 ✓ (FAIL_OBSERVATION_ONLY). All gates covered. |
| C-18 | Inertia structural elevation | **PASS** | All three positions: (1) Phase 1b sub-step with current-approach/displaced-by/displacement-type; (2) `[INERTIA]` column in Phase 3 grid; (3) `displacement-acknowledgment` required at Step 6 + FAIL_NO_DISPLACEMENT_FRAME |
| C-19 | Frame Type prefill constraint | **FAIL** | Step 6 enumerates accepted Frame Types inline; no separate Step 6a prefill table |

**Scores**:
- Essential: 5×12 = **60** ✓
- Recommended: 3×10 = **30** ✓
- Aspirational: C-09✓ C-10✓ C-11✓ C-12✓ C-13✓ C-14✓ C-15✓ C-16✓ C-17✓ C-18✓ C-19✗ = 10×5 = **50**

**Total: 140/145** — matches hypothesis exactly. C-18 cleanly adds 5 points to the proven 135/145 triple.

---

### V-05 — Full Five-Axis Combination (145/145 attempt)

**Design intent**: All five axes — C-15 + C-16 + C-17 + C-18 + C-19. The Step 8 amendment example shows returning to Step 6a as part of a correct amendment, demonstrating C-18/C-19 interaction.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | CODEOWNERS fallback | **PASS** | Step 0: CODEOWNERS check; FAIL_SILENT_INFERENCE; "Do not proceed on an assumed org" |
| C-02 | Power/Interest grid | **PASS** | Phase 3 grid with [INERTIA] column |
| C-03 | Veto risks ranked by probability | **PASS** | Step 4 ranked table |
| C-04 | Champion with concrete action | **PASS** | Step 5 with calendar examples |
| C-05 | Communication strategy per quadrant | **PASS** | Step 6b table with Timing requirement |
| C-06 | Conflict identification | **PASS** | Phase 1a: two+ named-party conflicts |
| C-07 | Role framing | **PASS** | Phase 1 / Phase 2 / Phase 3 distinct with explicit run-order headers |
| C-08 | Critical-path gatekeepers | **PASS** | Phase 1c with FAIL_NO_TIMING |
| C-09 | Amendment phase | **PASS** | Step 8 with update mandate |
| C-10 | NOT-doing framing | **PASS** | Phase 2 with FAIL_NO_NOT_DOING |
| C-11 | Source-tracking column | **PASS** | Phase 3 grid Source column; `amendment` label defined |
| C-12 | Amendment loop with update mandate | **PASS** | Step 8: "Update the affected table… no observation without revision" |
| C-13 | Prefilled frame types in comms table | **PASS** | Step 6b Frame Type column matches Step 6a; FAIL_SAME_FRAME present |
| C-14 | Named failure modes inline | **PASS** | FAIL_SILENT_INFERENCE, FAIL_ONE_PARTY, FAIL_NO_INERTIA, FAIL_NO_TIMING, FAIL_NO_NOT_DOING, FAIL_MONOLITH_ASSUMPTION, FAIL_NO_SOURCE, FAIL_PROSE_ONLY, FAIL_MISSING_INERTIA_TAG, FAIL_WRONG_ORDER, FAIL_NO_MITIGATION, FAIL_GENERIC_CHAMPION, FAIL_MISSING_DISPLACEMENT_PREFILL, FAIL_SAME_FRAME, FAIL_VAGUE_TIMING, FAIL_GATEKEEPER_INCOMPLETE, FAIL_OBSERVATION_ONLY = 17 inline labels |
| C-15 | Reversed sequence | **PASS** | "Run Phase 1 first. The Power/Interest Grid is built in Phase 3, after this phase and Phase 2 are complete." Explicit at Phase 1, Phase 2, and Phase 3 headers. |
| C-16 | Amendment before/after pair | **PASS** | Step 8: **Bad form** (prose observation about Data Governance) immediately adjacent to **Correct form** (Amendment 1 with table updates including Step 6a prefill update) |
| C-17 | FAIL saturation at every gate | **PASS** | Step 0 ✓ (FAIL_SILENT_INFERENCE), Phase 1a ✓ (FAIL_ONE_PARTY), Phase 1b ✓ (FAIL_NO_INERTIA), Phase 1c ✓ (FAIL_NO_TIMING), Phase 2 ✓ (FAIL_NO_NOT_DOING + FAIL_MONOLITH_ASSUMPTION), Phase 3 ✓ (FAIL_NO_SOURCE + FAIL_PROSE_ONLY + FAIL_MISSING_INERTIA_TAG), Step 4 ✓ (FAIL_WRONG_ORDER + FAIL_NO_MITIGATION), Step 5 ✓ (FAIL_GENERIC_CHAMPION), Step 6a ✓ (FAIL_MISSING_DISPLACEMENT_PREFILL), Step 6b ✓ (FAIL_SAME_FRAME + FAIL_VAGUE_TIMING), Step 7 ✓ (FAIL_GATEKEEPER_INCOMPLETE), Step 8 ✓ (FAIL_OBSERVATION_ONLY). All gates covered including the new 6a gate. |
| C-18 | Inertia structural elevation | **PASS** | All three positions: (1) Phase 1b sub-step with current-approach/displaced-by/displacement-type; (2) `[INERTIA]` column in Phase 3 grid; (3) `displacement-acknowledgment` required — and at the **prefill stage** (Step 6a rule 3 explicitly states this, not during row population). FAIL_MISSING_DISPLACEMENT_PREFILL confirms. |
| C-19 | Frame Type prefill constraint | **PASS** | Step 6a is a standalone step with an empty prefill table, accepted values list, rule 4 ("Do not proceed to Step 6b until all four assignments are complete"), and explicit constraint that values not in the list are prohibited. Structurally distinct from V-04's inline enumeration. |

**Scores**:
- Essential: 5×12 = **60** ✓
- Recommended: 3×10 = **30** ✓
- Aspirational: C-09✓ C-10✓ C-11✓ C-12✓ C-13✓ C-14✓ C-15✓ C-16✓ C-17✓ C-18✓ C-19✓ = 11×5 = **55**

**Total: 145/145** — all five axes are compatible. No interference detected.

---

## Round 5 Summary

| Variation | Focus | Score | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 |
|-----------|-------|-------|------|------|------|------|------|------|
| V-01 | Inertia elevation (C-18 alone) | **125/145** | PASS | FAIL | FAIL | FAIL | PASS | FAIL |
| V-02 | Frame prefill (C-19 alone) | **125/145** | PASS | FAIL | FAIL | FAIL | FAIL | PASS |
| V-03 | Reversed sequence (C-15 alone) | **120/145** | FAIL | PASS | FAIL | FAIL | FAIL | FAIL |
| V-04 | C-15+C-16+C-17+C-18 | **140/145** | PASS | PASS | PASS | PASS | PASS | FAIL |
| V-05 | Full five axes | **145/145** | PASS | PASS | PASS | PASS | PASS | PASS |

### Excellence Signals from V-05

1. **C-19 absorbs C-18's third position cleanly**: In V-05, the `displacement-acknowledgment` mandate moves from a note inside Step 6 instructions (V-04 pattern) to Step 6a rule 3. The prefill table becomes the structural vehicle for the third inertia position, creating a tighter binding: inertia stakeholders now have a single mandatory prefill assignment rather than a runtime check.

2. **C-16's amendment example extends into the 6a/6b interaction**: V-05's bad/correct pair includes "Step 6a prefill updated — Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly." This demonstrates amendment round-trip through both new steps, making the pair load-bearing for both C-16 and C-18/C-19 simultaneously — the correct form example teaches the interaction without requiring a separate section.

3. **FAIL_MISSING_DISPLACEMENT_PREFILL replaces FAIL_NO_DISPLACEMENT_FRAME at Step 6**: The failure label shifts from the content-population step to the prefill step, earlier in execution. This is structurally sound: catching the omission before content entry is more useful than detecting it after. The gate is now upstream.

4. **Phase 1b downstream-tracking language gains a third position**: V-04 says "tracks through two downstream steps"; V-05 says "tracks through three downstream positions: `[INERTIA]` tag in Phase 3 grid, ranked veto entry in Step 4, and `displacement-acknowledgment` in the Step 6a prefill." The explicit enumeration of three positions in Phase 1b language reinforces the structural contract for the entire inertia chain.

### Diagnostic confirmation

- V-03 at 120 (not 125) confirms: **C-15 without C-14 loses 5 points**. The reversed sequence registers as an independent axis but requires FAIL labels to reach the 125-tier.
- V-01, V-02 each at 125: **C-18 and C-19 are both stable single axes** at the same tier.
- V-04 at 140: **C-18 adds cleanly to the triple** with no interference.
- V-05 at 145: **All five axes are independent and compatible**.

---

```json
{"top_score": 145, "all_essential_pass": true, "new_patterns": ["C-19 prefill gate absorbs C-18 third position: displacement-acknowledgment mandate migrates from Step 6 runtime check to Step 6a prefill assignment, creating upstream detection and tighter inertia chain binding", "C-16 amendment example extends into 6a/6b round-trip: the bad/correct pair demonstrates prefill update + content revision together, making the example load-bearing for both C-16 and the C-18/C-19 interaction simultaneously"]}
```
