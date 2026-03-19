## validate-inertia Scorecard — Round 4

**Rubric:** v4 | **Max:** 180 pts | **Variations:** V-16 through V-20

---

### Scoring Matrix

| Criterion | Tier | V-16 | V-17 | V-18 | V-19 | V-20 |
|-----------|------|------|------|------|------|------|
| C-01–C-05 Essential | 50 pts | PASS | PASS | PASS | PASS | PASS |
| C-06–C-08 Recommended | 30 pts | PASS | PASS | PASS | PASS | PASS |
| C-09 Methodology declared | Asp | PASS | **FAIL** | PASS | PASS | PASS |
| C-10 Timeline sensitivity | Asp | **FAIL** | PASS | **FAIL** | PASS | PASS |
| C-11 Status-quo competitor | Asp | PARTIAL | PARTIAL | PARTIAL | PARTIAL | **PASS** |
| C-12 Named social proof threshold | Asp | PASS | PASS | PASS | PASS | PASS |
| C-13 Mitigation → root cause | Asp | PASS | PASS | PASS | PASS | PASS |
| C-14 Temporal persistence | Asp | **FAIL** | PARTIAL | **FAIL** | PARTIAL | **PASS** |
| C-15 Four labeled sub-parts | Asp | **FAIL** | **FAIL** | **FAIL** | **FAIL** | **PASS** |
| C-16 Confirmation signal | Asp | **FAIL** | **FAIL** | **FAIL** | **FAIL** | **PASS** |
| C-17 Per-score trace | Asp | **PASS** | **FAIL** | **PASS** | **PASS** | **PASS** |
| C-18 Trajectory verdict | Asp | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** |
| **TOTAL** | **180** | **125** | **130** | **125** | **150** | **180** |

---

### Ranking

1. **V-20 — 180/180** — all 10 aspirationals closed; extends V-15 with C-17 trace column (Phase 4) + C-18 Part B trajectory verdict (Phase 6)
2. **V-19 — 150/180** — closes C-17 + C-18; still missing C-11/C-14/C-15/C-16
3. **V-17 — 130/180** — closes C-10 + C-18; missing C-09 cascades to C-17 failure
4. **V-16 = V-18 — 125/180** — both close C-09 + C-17 via different mechanisms; neither adds C-10/C-14/C-15/C-16/C-18

C-11 remains the only criterion that never closes without an explicit competitive inventory phase with a durability disqualifier. C-15/C-16 only close in V-20 via the four-part kill-barrier structure and AMEND confirmation signal.

---

### Excellence Signals from V-20

**Signal 1 — Methodology trace as mandatory table column** (C-17): V-16, V-19, and V-20 converge on the same mechanism — a required column that cannot be omitted without omitting the table. V-18's epistemic framing ("your reader must re-derive your score") is equivalent in instruction strength but more susceptible to partial traces. The column wins on structural visibility.

**Signal 2 — Part A / Part B within-phase split** (C-10 + C-18): Phase 6 houses the per-persona timeline grid and the kill-barrier trajectory verdict as labeled sub-sections of one phase. Related conceptually, kept distinct structurally. The explicit disqualifier ("a verdict present only in Part A fails C-18") prevents the specific substitution failure — no extra phase needed.

**Signal 3 — Explicit reselection gate** (C-14): Binary YES/NO at T=0 AND T=18mo with "If either is NO: reselect" upgrades from implicit persistence (V-19's grid row) to explicit confirmation. Only a barrier passing both horizons earns the CONFIRMED KILL BARRIER label.

---

```json
{"top_score": 180, "all_essential_pass": true, "new_patterns": ["Methodology trace as mandatory table column: enforcing C-17 by making the per-score derivation sentence a required column in the score table -- a column cannot be omitted without omitting the table, making non-compliance structurally visible (stronger than prose epistemic framing which is susceptible to partial traces that name values without citing the threshold)", "Part A / Part B within-phase organization: housing two logically related but structurally distinct outputs (per-persona timeline grid satisfying C-10, and kill-barrier trajectory verdict satisfying C-18) as labeled sub-sections of one phase with an explicit disqualifier preventing the grid from satisfying the verdict requirement -- no phase count inflation", "Explicit reselection gate on temporal persistence: requiring binary YES/NO answers at T=0 AND T=18mo with a literal reselect instruction if either fails -- forces the model to confirm the kill barrier survives both horizons rather than implying persistence through a grid row without stating it"]}
```
d at the longest time horizon considered." The grid implies it; no explicit statement.
- C-15 FAIL: Phase 4 has Kill barrier / Structural persistence / Most exposed persona -- three distinct fields, not four labeled sub-parts with merging prohibition.
- C-16 FAIL: AMEND requires mitigation with structural reasoning but no forward-looking confirmation signal.
- C-17 FAIL: Phase 3 "one sentence naming the primary inertia driver" does not reference a declared methodology threshold (C-09 was not satisfied). Trace connects score to driver; cannot connect to threshold that was never declared.
- C-18 PASS: Phase 6 produces a dedicated labeled KILL-BARRIER TRAJECTORY VERDICT block with direction, structural reasoning referencing Phase 4 persistence property by name, and relationship note to Phase 5 grid. Phase 5 explicitly states it does not satisfy Phase 6.

**V-18 (125/180)**
- C-09 PASS: Phase 1 "Declare Your Scoring Framework" requires dimension weights + reasoning + tier combination rules before any persona. "Declaring the framework first means every score can be checked against it."
- C-10 FAIL: No timeline phase. No per-persona T=0/T=6mo/T=18mo grid.
- C-11 PARTIAL: Phase 4 structural persistence field -- structural reasoning required, competitive-dimension naming not explicitly required.
- C-14 FAIL: No explicit T=0 AND T=18mo qualification gate on the kill barrier.
- C-15 FAIL: Phase 4 has Kill barrier / Structural persistence / Most exposed persona -- three elements, not four labeled sub-parts.
- C-16 FAIL: AMEND has no confirmation signal.
- C-17 PASS: Phase 3 requires a derivation sentence with explicit three-part structure: (1) name at least two dimension values from Phase 2, (2) reference the specific Phase 1 threshold those values satisfy, (3) independently verifiable. Failing and passing examples given. Epistemic framing ("your reader must be able to re-derive your score from your inputs alone") provides a different enforcement mechanism from V-16's table column but equivalent structural strength.
- C-18 FAIL: No dedicated kill-barrier trajectory verdict.

V-16 vs V-18 tie at 125: both close C-17 via different mechanisms (table column vs. epistemic obligation) but neither closes C-10, C-14, C-15, C-16, or C-18.

**V-19 (150/180)**
- C-09 PASS: Phase 1 methodology declaration, prerequisite for C-17.
- C-10 PASS: Phase 5 T=0/T=6mo/T=18mo grid; non-flat trajectory required; explicit note that this grid does not satisfy Phase 6.
- C-11 PARTIAL: Phase 4 "Structural persistence" field -- same gap as V-16/V-17/V-18. No explicit competitive-dimension naming required.
- C-14 PARTIAL: Phase 5 grid extends to T=18mo. Phase 6 trajectory verdict implies temporal persistence structurally. No explicit binary YES/NO gate requiring confirmation the barrier exists at T=0 AND persists at T=18mo.
- C-15 FAIL: Phase 4 has three fields (Kill barrier / Structural persistence / Most exposed persona). No four-part labeled causal chain.
- C-16 FAIL: AMEND has no confirmation signal.
- C-17 PASS: Phase 3 trace column (identical mechanism to V-16).
- C-18 PASS: Phase 6 dedicated KILL-BARRIER TRAJECTORY VERDICT block -- direction + structural reasoning referencing Phase 4 by name + relationship to Phase 5. Phase 5 explicitly marked "context only; does not satisfy Phase 6."

C-11 and C-14 are the remaining gaps in V-19. C-11 closes only with an explicit competitive inventory (V-20's Phase 2). C-14 closes only with binary YES/NO gates (V-20's Phase 5 temporal persistence test).

**V-20 (180/180)**
- All essential and recommended criteria met through structurally gated phases.
- C-09 PASS: Phase 1 dimension weights + tier thresholds, prerequisite gate enforced.
- C-10 PASS: Phase 6 Part A T=0/T=6mo/T=18mo grid, non-flat trajectory required.
- C-11 PASS: Phase 2 competitive inventory requires naming the dimension, the advantage, and the structural durability basis. "Familiarity is not durability" disqualifier explicitly stated. Phase 5 kill barrier "expressed as the competitive dimension on which the current solution wins."
- C-12 PASS: Phase 3 social proof threshold requires named count, role, or condition; binary Y/N disqualified.
- C-13 PASS: AMEND (b)+(c) requires naming the structural condition from Phase 5(2) + explaining the causal mechanism by which the lever reaches it.
- C-14 PASS: Phase 5 explicit YES/NO qualification at T=0 AND T=18mo with "If either is NO: reselect" gate. Barrier cannot proceed to Phase 6 without passing both.
- C-15 PASS: Phase 5 requires exactly four labeled, distinct sub-parts: (1) Barrier definition, (2) Structural persistence, (3) Intervention target, (4) Lever efficacy. Merging prohibition explicit.
- C-16 PASS: AMEND (d) requires falsifiable confirmation signal at T=6mo -- "must be possible to observe it as absent." Vague forward hopes disqualified.
- C-17 PASS: Phase 4 trace column -- names dimension values from Phase 3, cites Phase 1 threshold. Same structural mechanism as V-16/V-19.
- C-18 PASS: Phase 6 Part B KILL-BARRIER TRAJECTORY VERDICT -- dedicated labeled section, direction + structural reasoning referencing Phase 5(2) by name + relationship to Part A. "A trajectory direction present only in the Part A grid... fails C-18."

---

### Variation Ranking

| Rank | Variation | Score | Key differentiators |
|------|-----------|-------|---------------------|
| 1 | V-20 | 180/180 | All 10 aspirationals closed; extends V-15 with C-17 trace column + C-18 Part B trajectory |
| 2 | V-19 | 150/180 | Closes C-17 (trace column) + C-18 (trajectory verdict); missing C-11/C-14/C-15/C-16 |
| 3 | V-17 | 130/180 | Closes C-10 (timeline) + C-18 (trajectory verdict); missing C-09/C-14/C-15/C-16/C-17 |
| 4 | V-16 | 125/180 | Closes C-09 + C-17 (trace column); missing C-10/C-14/C-15/C-16/C-18 |
| 4 | V-18 | 125/180 | Closes C-09 + C-17 (prose epistemic); identical coverage profile to V-16 |

V-16 and V-18 tie at 125: both close exactly C-17 via different mechanisms but neither closes C-10, C-14, C-15, C-16, or C-18.

---

### Excellence Signals from V-20

**Signal 1 -- Methodology trace as mandatory table column (C-17 enforcement)**
V-16, V-19, and V-20 all converge on the same mechanism: making the per-score derivation sentence a required column in the score table. A column cannot be omitted without omitting the table -- the format makes non-compliance structurally visible. V-18's prose epistemic framing ("your reader must re-derive your score from your inputs alone") achieves equivalent coverage but is more susceptible to partial traces that name values without citing the threshold. The table column is the structurally stronger enforcement mechanism for C-17.

**Signal 2 -- Part A / Part B within-phase organization (C-10 + C-18 co-housing)**
V-20's Phase 6 houses the per-persona timeline grid (Part A, satisfying C-10) and the dedicated kill-barrier trajectory verdict (Part B, satisfying C-18) as labeled sub-sections of one phase. Two outputs that are logically related (both about temporal evolution) but must be kept distinct. Part B includes an explicit disqualifier: "A trajectory direction present only in the Part A grid... fails C-18." The within-phase split enforces the distinction while preserving the conceptual grouping -- no phase count inflation.

**Signal 3 -- Explicit reselection gate on temporal persistence (C-14 enforcement)**
V-20's Phase 5 requires a binary YES/NO answer at both T=0 and T=18mo, with a literal "If either is NO: reselect" instruction. This is stronger than V-19's implicit persistence (a T=18mo grid row implies persistence but never states it). The reselection gate forces the model to confront whether the kill barrier actually survives -- not just name it as if it does. Only a barrier that passes both horizons earns the CONFIRMED KILL BARRIER label and gates Phase 6.

---

### All-Essential Pass

All five variations pass all five essential criteria. The essential structure is stable across all R4 variations -- variation design correctly targets aspirational differentiation only.

---

```json
{"top_score": 180, "all_essential_pass": true, "new_patterns": ["Methodology trace as mandatory table column: enforcing C-17 by making the per-score derivation sentence a required column in the score table -- a column cannot be omitted without omitting the table, making non-compliance structurally visible (stronger than prose epistemic framing which is susceptible to partial traces that name values without citing the threshold)", "Part A / Part B within-phase organization: housing two logically related but structurally distinct outputs (per-persona timeline grid satisfying C-10, and kill-barrier trajectory verdict satisfying C-18) as labeled sub-sections of one phase with an explicit disqualifier preventing the grid from satisfying the verdict requirement -- no phase count inflation", "Explicit reselection gate on temporal persistence: requiring binary YES/NO answers at T=0 AND T=18mo with a literal reselect instruction if either fails -- forces the model to confirm the kill barrier survives both horizons rather than implying persistence through a grid row without stating it"]}
```
