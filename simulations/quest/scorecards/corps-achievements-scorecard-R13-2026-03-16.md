## corps-achievements — Round 13 Scorecard (Rubric v12)

---

### Scoring Foundation

**Formula**: `score = (essential_pass/5 × 60) + (recommended_pass/3 × 20) + (aspirational_pass/33 × 20)`
**Per aspirational criterion**: 20/33 ≈ 0.606 pts
**PARTIAL** = 0.5 weight

---

### Essential (5) — All Variations

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|------|------|------|------|------|----------|
| C-01 | PASS | PASS | PASS | PASS | PASS | Glob instruction; hallucinated-topics prohibition in SCAN GATE sub-condition (1) |
| C-02 | PASS | PASS | PASS | PASS | PASS | SCAN GATE sub-condition (2): "none will be dropped" |
| C-03 | PASS | PASS | PASS | PASS | PASS | MILESTONE GATE enforces all three exact names |
| C-04 | PASS | PASS | PASS | PASS | PASS | Phase 4 leaderboard section present with table |
| C-05 | PASS | PASS | PASS | PASS | PASS | ACTIONS GATE sub-condition (1): exact achievement required |

**Essential subtotal**: 5/5 × 60 = **60 pts** — all variations identical.

---

### Recommended (3) — All Variations

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|------|------|------|------|------|----------|
| C-06 | PASS | PASS | PASS | PASS | PASS | ACHIEVEMENT CLUSTER GATE sub-condition (1): ✓/○ enforced |
| C-07 | PASS | PASS | PASS | PASS | PASS | Category A/B named labels mandated |
| C-08 | PASS | PASS | PASS | PASS | PASS | "Sprint ending {date} — {N} topics tracked." in Phase 2 |

**Recommended subtotal**: 3/3 × 20 = **20 pts** — all variations identical.

---

### Aspirational (33) — Per-Variation Detail

#### Criteria common to all R13 variations (inherited from R12 baseline)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-09 | P | P | P | P | P | Standalone 1-AWAY section with dedicated gate |
| C-10 | P | P | P | P | P | INSIGHT GATE sub-condition (1)/(2) |
| C-11 | P | P | P | P | P | ACHIEVEMENT CLUSTER GATE sub-condition (3): self-test |
| C-12 | P | P | P | P | P | `[Action] → Unlocks [Achievement] → Breaks [PATTERN]` enforced |
| C-13 | P | P | P | P | P | `**TEAM INSIGHT — [name]: [text]**` format |
| C-14 | P | P | P | P | P | Registry label syntax `[PATTERN_LABEL from registry]` enforced |
| C-15 | P | P | P | P | P | Gate fail-paths name specific instance (contributor/topic not evidenced) |
| C-16 | P | P | P | P | P | `Score = Signals×1 + Topics×3 + Milestones×5` in all leaderboards |
| C-17 | P | P | P | P | P | Semantic names: SOLO_ISLAND, NAMESPACE_MOAT, SPRINT_FREEZE, SHALLOW_POOL, ORPHAN_TOPIC |
| C-18 | P | P | P | P | P | 4-column table: Topic/Target \| Achievement \| Gap \| Exact Action |
| C-19 | P | P | P | P | P | Rank-1 inline worked example above table |
| C-20 | P | P | P | P | P | All gate labels carry criterion ID references |
| C-21 | P | P | P | P | P | Correction loop if worked example ≠ Score column |
| C-22 | P | P | P | P | P | INSIGHT GATE: "NOT derivable from any single topic view alone" |
| C-23 | P | P | P | P | P | All multi-condition gates use numbered sub-steps (1)(2)(3)… |
| C-24 | P | P | P | P | P | INSIGHT GATE sub-condition (4): prior-phase cross-check |
| C-25 | P | P | P | P | P | Multi-criterion gates enumerate all covered IDs in label |
| C-26 | P | P | P | P | P | STRUCTURAL AUDIT GATE sub-condition (1): meta-verification of gate ID labels |
| C-27 | P | P | P | P | P | Structural audit names each gate by full label + expected criterion IDs |
| C-28 | P | P | P | P | P | All gates: "Before I write... I confirm [C-XX]:" first-person framing |
| C-29 | P | P | P | P | P | Named correction triad + re-run instruction in RETRY PROTOCOL |
| C-30 | P | P | P | P | P | ATTRIBUTION INTEGRITY GATE prohibits backward inference |
| C-31 | P | P | P | P | P | Single global RETRY PROTOCOL block; gates reference by name only |
| C-32 | P | P | P | P | P | `> RETRY [C-XX]:` / `> END RETRY [C-XX]` delimiters |
| C-33 | P | P | P | P | P | ATTRIBUTION INTEGRITY GATE is standalone, fires before leaderboard phase |
| C-34 | P | P | P | P | P | Structural audit enumerates all 9 cluster gates (N=9) |

**26/33 pass for all variations before v12 delta.**

---

#### v12 New Criteria (C-35 through C-41)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Decision notes |
|----|------|------|------|------|------|----------------|
| C-35 | PASS | PASS | PASS | PASS | PASS | All carry `Step 1 TRIAD:` / `Step 2 DELIMIT:` / `Step 3 CONTINUE:` shorthand labels |
| C-36 | PASS | **FAIL** | **FAIL** | **FAIL** | PASS | V-01/V-05: `"Row count = 9. All 9 enumerated. [C-34/C-36]"` — explicit count assertion. V-02/V-03/V-04: use `"N=9, all N verified"` as a parenthetical; coverage summary confirms C-36 not targeted in those variations |
| C-37 | **FAIL** | PASS | **FAIL** | PASS | PASS | V-02/V-04/V-05: `OUTPUT SCHEMAS [C-37]` preamble block before any gate fires. V-01/V-03: no preamble schema block |
| C-38 | **FAIL** | PASS | **FAIL** | PASS | PASS | V-02/V-04/V-05: attribution gate fires in Phase 0 before any artifact is read; `Contributors: [empty]` commitment present. V-01: attribution gate fires between Phase 2 and 3 (post-scan). V-03: attribution gate fires after Phase 2 (which already consumed Phase 1 scan state) |
| C-39 | **FAIL** | **FAIL** | PASS | **FAIL** | PASS | V-03/V-05: explicit `EXIT CONTRACT` / `ENTRY CONTRACT` objects at every phase boundary. V-01/V-02/V-04: no formal handoff objects |
| C-40 | **FAIL** | **FAIL** | PASS | **FAIL** | PASS | V-03: `"### I will now perform the artifact scan — Phase 1"`, `"I am now generating..."` etc. V-05: `"### Phase 0 — I am declaring attribution pre-commitment"`, `"Phase 1 — I will now perform..."` etc. V-01/V-02/V-04: phase headers use `"### Phase N — [noun phrase]"` without first-person |
| C-41 | **FAIL** | **FAIL** | **FAIL** | PASS | PASS | V-04/V-05: `HYPOTHESIS PRE-SCAN [C-41]` preamble block requiring `CANDIDATE INSIGHT` before evidence; Phase 7 revisits with "Confirmed: …" or "Revised: …"; INSIGHT GATE sub-condition (5) verifies pre-evidence commitment. V-01/V-02/V-03: no hypothesis block |

---

### Aspirational Counts and Totals

| Variation | Passes (of 33) | Fails | Aspirational pts | Total Score |
|-----------|----------------|-------|-----------------|-------------|
| V-01 | 28 | C-37/C-38/C-39/C-40/C-41 | 28×0.606 = 16.97 | **96.97** |
| V-02 | 29 | C-36/C-39/C-40/C-41 | 29×0.606 = 17.58 | **97.58** |
| V-03 | 29 | C-36/C-37/C-38/C-41 | 29×0.606 = 17.58 | **97.58** |
| V-04 | 30 | C-36/C-39/C-40 | 30×0.606 = 18.18 | **98.18** |
| V-05 | 33 | — | 33×0.606 = 20.00 | **100.00** |

---

### Ranking

1. **V-05 — 100.00** (all 7 v12 criteria)
2. **V-04 — 98.18** (C-37/C-38/C-41; misses C-36/C-39/C-40)
3. **V-02 — 97.58** (C-37/C-38/C-35; misses C-36/C-39/C-40/C-41)
3. **V-03 — 97.58** (C-39/C-40/C-35; misses C-36/C-37/C-38/C-41)
5. **V-01 — 96.97** (C-35/C-36; misses C-37/C-38/C-39/C-40/C-41)

---

### Excellence Signals from V-05

**Pattern 1 — Pre-commitment cluster in preamble**
V-05 places C-37 (OUTPUT SCHEMAS), C-38 (empty contributor list), and C-41 (HYPOTHESIS PRE-SCAN) together in a single preamble block before any gate fires or any artifact is read. These three criteria all share the same structural logic — declare a constraint before its violation becomes possible. Grouping them in the preamble turns it into a "falsifiability zone": the model enters Phase 0 with schemas declared, contributor scope locked empty, and a synthesis prediction on record. Every subsequent phase either confirms or revises those pre-stated positions, and both outcomes are visible in the output.

**Pattern 2 — Phase contracts as typed handoff objects**
V-05 adds EXIT CONTRACT / ENTRY CONTRACT blocks at every phase boundary (C-39), but the ENTRY CONTRACTs go beyond C-24's single insight-gate cross-check — they actively ask cross-phase reconciliation questions inline: e.g., Phase 2's ENTRY CONTRACT asks "Did Phase 2 milestone analysis surface any topics not in Phase 1 SCAN STATE? Reconcile if yes." This makes phase ordering errors detectable at the transition point, not only when the insight gate fires.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Pre-commitment cluster in preamble: group schema declaration (C-37), empty contributor commitment (C-38), and hypothesis pre-scan (C-41) together before any gate fires — all three share the same structural logic of making violations impossible rather than prohibited", "Phase contracts as typed handoff objects: EXIT CONTRACT / ENTRY CONTRACT blocks at every phase boundary embed cross-phase reconciliation questions inline at the transition point, not only at the single insight gate"]}
```
