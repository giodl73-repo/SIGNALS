Confirmed: the rubric v3 file (97 lines) contains only criteria + upgrade notes — the V-01/V-02 for Round 3 are in the user's prompt only. V-03–V-05 were not generated for this round. I'll score what exists.

---

# Round 3 Scorecard — `corps-achievements`

**Rubric:** v3 (5E + 3R + 7A)
**Variations scored:** V-01 and V-02 (V-03–V-05 not generated)
**Date:** 2026-03-16

---

## Pre-Scoring Self-Check

- [x] Rubric v3 loaded — 5E + 3R + 7A, scoring formula confirmed
- [x] V-01 (Role Sequence) fully read from prompt
- [x] V-02 (Scorecard Format) fully read from prompt — appears to end at STEP 5, STEP 6 label transitions into scoring instructions
- [x] V-03–V-05 absent; noted in summary
- [x] PARTIAL on any essential criterion = gate failure regardless of composite score

---

## V-01 — Role Sequence: Scan → Award → Synthesize

### Essential

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | PRE-WRITE GATE A explicitly: "I will only list topics I have confirmed by reading actual file paths… I will not infer, assume, or hallucinate topics." GATE-A CHECK removes unconfirmed topics by name. |
| C-02 | **PASS** | GATE-B: "Does every topic from Phase 1 appear in at least one achievement row? If not, list: GATE-B: [missing-topic] has no achievement row → halt." |
| C-03 | **PASS** | Phase 2 milestone registry table uses exact names: **First Team Signal**, **Shared Coverage**, **Debate Starter** with ✅/⬜ marking. |
| C-04 | **PASS** | Phase 3 leaderboard required: Rank \| Contributor \| Signals \| Topics \| Milestones. No omission allowed. |
| C-05 | **PASS** | PRE-WRITE GATE C checks each action row for "(a) exact thing to do, (b) exact achievement, (c) exact stagnation pattern." Format: `[Action] → Unlocks [Achievement] → Breaks [PATTERN_LABEL]`. |

**Essential: 5/5 → 60 pts**

### Recommended

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PARTIAL → 0** | Milestones get ✅/⬜ earned/not-earned marking. Topic-level achievements under DEPTH and COLLABORATION categories list condition text but no per-topic earned/available separation — the split is category-level, not earned-vs-available. |
| C-07 | **PASS** | **Category: DEPTH ACHIEVEMENTS** (Signal Starter, Multi-Namespace, Sprint Complete) and **Category: COLLABORATION ACHIEVEMENTS** (Pair Signal, Cross-Fire) — 2 named categories with explicit labels. |
| C-08 | **PASS** | Phase 7 SPRINT SUMMARY explicitly required: "date, topics scanned, signals counted, achievements awarded." |

**Recommended: 2/3 → 20 pts**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **FAIL** | No dedicated "Almost There" or "1-away" section anywhere in V-01. |
| C-10 | **PASS** | Phase 4: "State one cross-topic or cross-contributor insight that is not already captured by any stagnation pattern above" — uniqueness constraint explicit. |
| C-11 | **PASS** | Three inline pre-write gates: GATE A (before listing topics), GATE B (before rendering achievements), GATE C (before each action row). Strongest multi-gate enforcement seen. |
| C-12 | **PASS** | Phase 5 format: `[Specific Action] → Unlocks **[Achievement Name]** → Breaks **[PATTERN_LABEL from registry]**` — exact match to required format. |
| C-13 | **PASS** | Phase 4: "**TEAM INSIGHT — [Descriptive Title]:**" format explicitly required with named artifact title. |
| C-14 | **PASS** | STAGNATION PATTERN REGISTRY defined in Phase 4 (SOLO_ISLAND, NAMESPACE_MOAT, SPRINT_FREEZE, ORPHAN_TOPIC). Phase 5 enforces `[PATTERN_LABEL from registry]` syntax — not invented inline. |
| C-15 | **PASS** | GATE-A: "GATE-A: [topic-name] removed — no real file evidence." GATE-B: "GATE-B: [missing-topic] has no achievement row → halt." Both name the specific failing instance. |

**Aspirational: 6/7 → 8.57 pts**

### Score

```
V-01: 60 + 20 + 8.57 = 88.57 ≈ 89
Golden threshold: ALL 5 essential PASS + score ≥ 80 → YES
```

---

## V-02 — Output Format: Scorecard Tables

### Essential

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | GATE-A (pre-list): "Every topic I list below corresponds to a real file I observed… If excluded: GATE-A: [topic-name] excluded — no confirmed file path." |
| C-02 | **PASS** | GATE-B (post-scorecard): "Every topic from Step 1 appears in the scorecard above. If any topic is missing: GATE-B: [topic-name] missing from scorecard → halt." |
| C-03 | **PASS** | Step 3 milestone table rows: First Team Signal \| Shared Coverage \| Debate Starter — all three, exact names. |
| C-04 | **PASS** | Step 4 CONTRIBUTOR LEADERBOARD TABLE with scoring formula (Signals×1 + Topics×3 + Milestones×5). |
| C-05 | **PASS** | Step 5 1-AWAY CALLOUT TABLE: "Achievement" column (what unlocks) + "Exact Action Needed" column (specific action including namespace/skill/topic). The requirement — name action AND achievement — is structurally met even though the form is a gap-table rather than a prose list. |

**Essential: 5/5 → 60 pts**

### Recommended

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PARTIAL → 0** | Achievement scorecard uses a Status column (✅/⬜) rather than separate earned/available sections — interleaved in one table. Visual separation exists weakly but not as distinct sections. |
| C-07 | **PASS** | Step 2 scorecard "Category" column contains "Depth" and "Collaboration" — 2 named categories applied per achievement row. |
| C-08 | **PASS** | Step 1 topic registry table has "Sprint" column showing latest signal date. |

**Recommended: 2/3 → 20 pts**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Step 5 dedicated "1-AWAY CALLOUT TABLE" with Topic \| Achievement \| Gap \| Exact Action Needed. Quantified to one-signal/contributor/namespace level. |
| C-10 | **FAIL** | No cross-topic or cross-contributor insight section present in V-02 (STEP 6 transitions into scoring instructions; no synthesis section). |
| C-11 | **PASS** | GATE-A is a pre-write verification statement the model must affirm before listing topics. Satisfies "at least one inline pre-write self-test gate." |
| C-12 | **FAIL** | No anti-inertia framing. Step 5 callout table names action + achievement but does not include `→ Breaks [Pattern]`. |
| C-13 | **FAIL** | No **TEAM INSIGHT — [name]:** artifact. No synthesis section where this could appear. |
| C-14 | **FAIL** | No stagnation pattern registry defined or referenced in V-02. |
| C-15 | **PASS** | GATE-A: "GATE-A: [topic-name] excluded." GATE-B: "GATE-B: [topic-name] missing from scorecard → halt." Both name the specific failing instance. |

**Aspirational: 3/7 → 4.29 pts**

### Score

```
V-02: 60 + 20 + 4.29 = 84.29 ≈ 84
Golden threshold: ALL 5 essential PASS + score ≥ 80 → YES
```

---

## Summary Table

| Variation | E (5) | R (3) | A (7) | Score | Golden |
|-----------|-------|-------|-------|-------|--------|
| V-01 — Role Sequence | 5/5 | 2/3 | 6/7 | **89** | YES |
| V-02 — Scorecard Tables | 5/5 | 2/3 | 3/7 | **84** | YES |
| V-03 | — | — | — | not generated | — |
| V-04 | — | — | — | not generated | — |
| V-05 | — | — | — | not generated | — |

---

## Excellence Signal Analysis

**V-01 is the top variation.** Its decisive advantages over V-02:

1. **C-10/C-13 present**: Phase 4 CROSS-TOPIC SYNTHESIS + `**TEAM INSIGHT — [name]:**` format — V-02 has no synthesis section at all.
2. **C-12/C-14 present**: Anti-inertia action format + stagnation registry — V-02 has no registry or pattern-breaking framing.
3. **C-11 triple gate**: GATE A + B + C at distinct lifecycle phases vs V-02's single pre-list gate.

**V-02's sole advantage over V-01**: C-09 (1-away callout table) — V-01 misses this entirely.

**New pattern identified from V-01 not yet codified:**

V-01 Phase 4 says: "For each active pattern, name the specific topic or contributor instance." This instance-naming occurs in the **body of the synthesis section**, not just in gate failure messages. C-15 covers gate failure instance-naming. But V-01 extends instance-naming into the stagnation diagnosis itself — `SOLO_ISLAND: {topic-path}`, not "some topics are isolated." This is a stronger version of C-15 applied to synthesis prose.

**C-16 candidate**: _Stagnation pattern diagnoses in synthesis name the specific topic or contributor instance that exhibits the pattern — not just gate messages, but the body output: `[PATTERN_LABEL]: {topic-path or contributor}` rather than generic descriptions._

---

## Missing Variations

V-03, V-04, V-05 were not generated in this round. Recommended axes for completion:

- **V-03**: Contributor-first approach (starts with leaderboard scan, works backward to topic coverage) — tests whether C-01/C-02 still hold when grounding comes from contributor metadata rather than file scan
- **V-04**: Combination V-01 + V-02 (role sequence + scorecard tables) — tests C-09 + full aspirational stack
- **V-05**: Maximalist — all 7 aspirational criteria enforced including new C-16 candidate

---

```json
{"top_score": 89, "all_essential_pass": true, "new_patterns": ["Stagnation pattern diagnoses in synthesis name the specific topic or contributor instance that exhibits the pattern, not just gate failure messages — extends C-15 instance-naming from gates into body output"]}
```
