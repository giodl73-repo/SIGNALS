## Quest Score — corps-achievements R9

**Rubric version**: v8 | **Variations**: V-01 through V-05

---

## Per-Variation Scorecard

### Essential Criteria (C-01–C-05)

All five variations carry the full baseline. Quick check:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Scan grounded in real files | PASS | PASS | PASS | PASS | PASS |
| C-02 Every topic in achievements | PASS | PASS | PASS | PASS | PASS |
| C-03 Three named milestones | PASS | PASS | PASS | PASS | PASS |
| C-04 Contributor leaderboard populated | PASS | PASS | PASS | PASS | PASS |
| C-05 Next actions name unlock | PASS | PASS | PASS | PASS | PASS |

All variations: **5/5 essential**.

---

### Recommended Criteria (C-06–C-08)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Earned vs. locked visually separated | PASS — two labeled sections | PASS — two explicitly labeled tables | PASS — two sections w/ pattern context headers | PASS — Earned/Locked w/ pattern headers | PASS — two labeled tables |
| C-07 Achievements in 2+ named categories | PASS | PASS | PASS | PASS | PASS |
| C-08 Sprint/date framing | PASS — "Week of {{date}}" in leaderboard | PASS | PASS | PASS | PASS |

All variations: **3/3 recommended**.

---

### Aspirational Criteria (C-09–C-28)

#### C-09 1-Away callouts with dedicated section

All five variations include a "## Almost There — 1-Away Gaps" section with 1-AWAY GATE [C-09/C-18]. **PASS all**.

#### C-10 Cross-topic insight as named conclusion distinct from gap statements

All five: INSIGHT GATE step D confirms "Differs from stagnation pattern statement or gap statement already written." **PASS all**.

#### C-11 Inline pre-write self-test gate

All five have pre-write confirmation gates before achievement and leaderboard sections.
- V-05 adds a distinctive wrinkle: phrasing as first-person ownership — "Before I write this section, I confirm [C-11]: …" — rather than a procedural sub-step.
**PASS all**.

#### C-12 Anti-inertia framing: `[Action] → Unlocks [X] → Breaks [Pattern]`

This is the sole differentiator across the five variations.

| Variation | Gate sub-step for C-12 | Format template used | Verdict |
|-----------|------------------------|----------------------|---------|
| V-01 | Sub-step (3): "Each action uses format [Action] → Unlocks [Achievement] → Breaks [Pattern]. [C-12]" | Arrow format in template | **PASS** |
| V-02 | No C-12 sub-step — gate has sub-steps for C-05 and C-14 only; gate label claims C-12 but does not verify the arrow format | Table columns (Action / Unlocks / Breaks) with no format enforcement | **PARTIAL** (0.5) |
| V-03 | Sub-step (3): "Each action uses format [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]" | Arrow format in template | **PASS** |
| V-04 | Sub-step (3): "Format [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]" | Arrow format in template | **PASS** |
| V-05 | Sub-step (3): "Format used: [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]" | Arrow format in template | **PASS** |

V-02's table columns preserve the three information elements (action, unlock, breaks-pattern) but the format criterion specifies the arrow syntax, and the gate sub-steps do not verify it. PARTIAL.

#### C-13 Insight formatted as `**TEAM INSIGHT — [descriptive name]:**`

All five: INSIGHT GATE sub-step (1) checks formatting. **PASS all**.

#### C-14 Pattern labels from named registry, label syntax enforced

All five include the Stagnation Pattern Registry and instruct `[PATTERN_LABEL from registry]`. ACTIONS CLUSTER GATE explicitly checks registry sourcing. V-03 and V-04 add STAGNATION DIAGNOSIS GATE [C-14/C-17] in Phase 0. **PASS all**.

#### C-15 Gate fail messages name the specific instance

All five: fail messages use `— [specific path or file]`, `— [specific topic or row]`, `— [milestone name]` format. **PASS all**.

#### C-16 Leaderboard uses explicit weighted formula

All five: LEADERBOARD CLUSTER GATE sub-step (1) checks `Score = (Signals×1) + (Topics×3) + (Milestones×5)`. **PASS all**.

#### C-17 Pattern labels are semantic names

All five: registry defines SOLO_ISLAND, NAMESPACE_MOAT, SPRINT_FREEZE, SHALLOW_POOL, ORPHAN_TOPIC. V-03/V-04 add STAGNATION DIAGNOSIS GATE sub-step (8) explicitly checking semantic naming. **PASS all**.

#### C-18 1-Away callout as structured table with 4 columns

All five: template `| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |`. **PASS all**.

#### C-19 Worked example calculation for Rank 1 contributor

All five: LEADERBOARD CLUSTER GATE sub-step (2) `Score = {S}×1 + {T}×3 + {M}×5 = {total}`. **PASS all**.

#### C-20 Gate labels carry criterion ID references

All five: every gate label in every variation carries at least one [C-XX] reference. **PASS all**.

#### C-21 Reconciliation correction loop after worked example

All five: LEADERBOARD CLUSTER GATE sub-steps (3)–(5) — compare total, correct if mismatch, confirm match. **PASS all**.

#### C-22 Derivability test: insight must fail single-topic derivation

All five: INSIGHT GATE Step B applies per-topic derivability elimination for every topic in scan state; Step C generates new candidate if any YES. **PASS all**.

#### C-23 Multi-condition gates use numbered sub-steps

All five: every gate block uses `"(1) … (2) … (3) …"` enumeration. **PASS all**.

#### C-24 Later-phase gate asks whether prior-phase findings alter current output

All five: CROSS-PHASE GATE [C-24/C-01/C-02] in the final phase explicitly asks "Did Phase N gaps surface topic names absent from Phase 1 scan state? YES/NO" and instructs additions if YES. **PASS all**.

#### C-25 Multi-criterion super-gate labels enumerate all covered criterion IDs

All five: both super-gates — LEADERBOARD CLUSTER GATE [C-16/C-19/C-21] and ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20] — enumerate all IDs in the label; sub-step (6) in each gate checks enumeration. **PASS all**.

#### C-26 Structural audit gate verifies all other gate labels carry criterion IDs

All five: STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27] sub-step (2) audits every gate label in the run for criterion ID presence. **PASS all**.

#### C-27 Structural audit names each super-gate by full label with exact expected IDs

All five: STRUCTURAL AUDIT GATE sub-step (3) explicitly lists:
- `'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — confirm label enumerates C-16, C-19, C-21.`
- `'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — confirm label enumerates C-05, C-12, C-14, C-20.`

Sub-step (5) flags wrong enumeration with `'AUDIT FAIL [C-27]: gate "[label]" — expected [C-XX/...], found [C-XX/...].'` **PASS all**.

#### C-28 Super-gate pass confirmation names the enumeration verification as a separate line item

All five: both super-gate pass messages include `"Label enumeration (C-25): [C-XX/C-XX/C-XX] verified."` as a named line item. **PASS all**.

---

## Composite Scores

```
Formula: (essential_pass/5 × 60) + (recommended_pass/3 × 20) + (aspirational_pass/20 × 20)
PARTIAL = 0.5 weight
```

| Variation | Essential (60) | Recommended (20) | Aspirational (20) | Total |
|-----------|----------------|------------------|-------------------|-------|
| V-01 Leaderboard-first | 60 | 20 | 20.0 (20/20) | **100.0** |
| V-02 Dense table, prose-minimized | 60 | 20 | 19.5 (19.5/20, C-12 PARTIAL) | **99.5** |
| V-03 Stagnation-first | 60 | 20 | 20.0 (20/20) | **100.0** |
| V-04 Combined: Leaderboard-first + Stagnation-first + STOP barriers | 60 | 20 | 20.0 (20/20) | **100.0** |
| V-05 Dense tables + Conversational | 60 | 20 | 20.0 (20/20) | **100.0** |

---

## Ranking

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 (tied) | V-01, V-03, V-04, V-05 | 100.0 | All achieve full aspirational coverage |
| 2 | V-02 | 99.5 | C-12 PARTIAL: gate label claims C-12 coverage but no sub-step enforces arrow format |

**Tiebreak analysis** — among the four 100s:

- **V-04** is architecturally the richest: combines stagnation-first Phase 0 (pattern frame before any computation), leaderboard-first Phase 1 (contributor attribution before achievement enumeration), and explicit STOP barriers between phases. Three mutually-reinforcing innovations. Most tightly gated.
- **V-03** introduces the Phase 0 pattern frame as a standalone innovation with the valuable secondary effect: pre-write gates ask "Does the stagnation pattern frame explain why any topics have only Locked achievements?" — a novel cross-section interrogation not present in other variations.
- **V-05** is the most consumer-ready: first-person pre-write gate phrasing ("Before I write this section, I confirm…") may improve model self-alignment with the intent of the check versus mechanical execution.
- **V-01** is the cleanest single-axis variation and the simplest path to leaderboard-first attribution.

**Declared top variation: V-04** (combination depth + maximum structural integrity).

---

## Excellence Signals from R9

### ES-1 — Phase-zero stagnation diagnosis creates a downstream evaluative frame

**Pattern**: Running a lightweight pattern diagnosis (glob + counts, no content reading) as Phase 0 — before any achievement computation — produces a named dominant pattern (`SOLO_ISLAND`, `SHALLOW_POOL`, etc.) that propagates into all subsequent section headers, pre-write gate prompts, and action ordering. Earned achievements become "earned *despite* [PATTERN_LABEL]"; locked achievements become "locked *by* [PATTERN_LABEL]." Actions are ordered by pattern-breaking impact rather than achievement value alone.

**Why it's better**: Reverses the frame from celebration to diagnosis. Every achievement and gap is interpreted through a named context that the team can recognize and debate. The pre-write gate in Phase 1B asks "Does the stagnation pattern frame explain why any topics have only Locked achievements?" — a question that forces cross-section coherence, not just per-section completeness.

**Seen in**: V-03, V-04.

### ES-2 — Explicit STOP barriers enforce phase independence at the instruction level

**Pattern**: Adding "PHASE N COMPLETE. Do not read Phase N+1 instructions until the gate above passes." at the end of each phase creates a hard sequential barrier — the model cannot load downstream context (which could influence upstream output) until the current gate passes. This is different from implicit phase ordering: the STOP instruction explicitly prohibits context bleed from later phases into earlier ones.

**Why it's better**: Without STOP barriers, a model with full context might unconsciously structure Phase 1 output to satisfy Phase 3's structural audit — importing correctness from future knowledge rather than from present data. The barrier enforces genuine forward-only execution. Particularly valuable when Phase 0 stagnation context could prematurely shape Phase 1 scan output.

**Seen in**: V-04 exclusively.

---

## Key Observation: V-02's Structural Gap

V-02 demonstrates a generalizable failure mode: **a gate label can claim criterion coverage that its sub-steps do not enforce**. ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20] claims C-12 in the label and in the pass confirmation (`"Anti-inertia format (C-12): confirmed"`), but no sub-step verifies the `[Action] → Unlocks [Achievement] → Breaks [Pattern]` arrow format. The table columns preserve the three information elements but the format constraint — which is the measurable commitment C-12 enforces — disappears. The lesson: every criterion ID in a multi-criterion gate label must have an addressable sub-step.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase-zero stagnation diagnosis creates a downstream evaluative frame that propagates into section headers, pre-write gate prompts, and action ordering — reversing the evaluative posture from celebration to diagnosis before any achievement computation", "Explicit STOP barriers between phases enforce forward-only instruction execution, preventing downstream context from shaping upstream output before gates pass"]}
```
