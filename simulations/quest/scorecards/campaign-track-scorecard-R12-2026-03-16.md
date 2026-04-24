## campaign-track / Round 12 — Quest Scorecard

### Scoring Framework

From the rubric preamble:
- **Essential** (C-01–C-05): 10 pts each → 50 max
- **Recommended** (C-06–C-08): 5 pts each → 15 max
- **Aspirational** (C-09–C-37): 3 pts each → 72 max
- **Total max (v11)**: 137 pts (131 baseline + 3 for C-36 + 3 for C-37)

All five variations inherit the R10 V-05 baseline (131/131 on C-01–C-35). Differences are isolated to C-36 and C-37.

---

### Per-Criterion Evaluation

#### Essential (C-01–C-05) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-01 Four-phase structure | PASS | PASS | PASS | PASS | PASS | All: Register→Plan→Status→Narrative, four labeled sections |
| C-02 Artifact-per-phase | PASS | PASS | PASS | PASS | PASS | All: strategy.md, roadmap.md, status.md, story.md + delta.md |
| C-03 Nine-namespace coverage table | PASS | PASS | PASS | PASS | PASS | All: Phase 3 Contract declares all 9 rows with 5 typed fields |
| C-04 Readiness verdict from enumerated set | PASS | PASS | PASS | PASS | PASS | All: READY\|NOT READY\|CONDITIONALLY READY declared and enforced |
| C-05 Narrative verdict with evidence | PASS | PASS | PASS | PASS | PASS | All: Phase 4 Contract requires verdict_verb + hypothesis_mutation + echoes + 3 recommendations |

**Essential subtotal: 50/50 for all variations.**

---

#### Recommended (C-06–C-08) — All Variations

| Criterion | All | Evidence |
|-----------|-----|----------|
| C-06 Artifact write paths | PASS | All four phases have `simulations/topic/{{topic}}-{artifact}-{{date}}.md` write paths |
| C-07 Coverage ratio + readiness label | PASS | coverage_ratio ("X/N") + readiness_verdict both in Phase 3 Contract |
| C-08 Cross-namespace signal balance | PASS | per-namespace breakdown with zero_flag = "NO SIGNALS" when planned=0 AND collected=0 |

**Recommended subtotal: 15/15 for all variations.**

---

#### Aspirational — Baseline Criteria (C-09–C-35)

All five variations inherit R10 V-05 baseline at PASS. Selecting the most diagnostic for confirmation:

| Criterion | All | Evidence note |
|-----------|-----|---------------|
| C-09 Echo integration | PASS | echoes list with ["NONE"] fallback in Phase 4 Contract |
| C-10 Dual-session delta | PASS | delta.md Two-Pass protocol; signals_added/removed; verdict_change summary |
| C-11 Role-gated phases | PASS | Registrar/Planner/Analyst/Narrator distinct, each owns exactly one phase |
| C-12 Explicit progression gates | PASS | GATE statements between all adjacent phases |
| C-13 Empty-state as named section | PASS | "First Invocation (0 signals collected)" with per-phase behavior |
| C-14 Per-role prohibition lists | PASS | 5 numbered forbidden actions per role (Prohibition Parity Rule enforces count) |
| C-15 Typed output contracts | PASS | All four phases + delta.md have typed contracts with field-level constraints |
| C-16 Terminal completion checklist | PASS | 27-item TERMINAL section; targeted re-run by phase; dashboard gated |
| C-17–C-35 (baseline) | PASS | Inherited from R10 V-05 baseline |

**Aspirational baseline subtotal (C-09–C-35): 81/81 for all variations.**

---

#### New Criteria — C-36 and C-37

**C-36 — Phase 4 obligation header names specific stale-value consequence**

| Variation | Result | Evidence |
|-----------|--------|----------|
| **V-01** | **PASS** | Phase 4 header: "If Phase 4 completes without writing story.md, `verdict_after` in `delta.md` becomes stale — the 'NOT YET REACHED' placeholder will persist indefinitely, causing all downstream delta comparisons to report the campaign as incomplete." Reinforced in empty-state section. Assertion → named consequence → downstream failure mode. |
| **V-02** | **FAIL** | Phase 4 header: bare "**Obligation**: Write story.md before declaring Phase 4 complete." No stale-value consequence named. |
| **V-03** | **FAIL** | Phase 4 header: "**Obligation**: The Narrator SHALL write story.md before declaring Phase 4 complete." SHALL register adds emphasis but no stale-value consequence. |
| **V-04** | **PASS** | Phase 4 header names stale-value consequence: "`verdict_after` in `delta.md` becomes stale — the 'NOT YET REACHED' placeholder persists, and all downstream delta comparisons report the campaign as incomplete." Empty-state reinforces obligation applies on first invocation. |
| **V-05** | **PASS** | Three scoring surfaces: (1) Phase 4 obligation header (same framing as V-04 with added "actual readiness verdict determined by this session's signals"); (2) Phase Boundary Summary: "If Phase 4 completes without writing story.md, `verdict_after` in `delta.md` becomes stale — the placeholder persists and downstream delta comparisons cannot determine whether the campaign produced a real verdict or was interrupted"; (3) Empty-state section. Strongest per-site framing of any variation. |

**C-37 — Cascade rule explains WHY non-cascade fields are excluded**

| Variation | Result | Evidence |
|-----------|--------|----------|
| **V-01** | **FAIL** | Cascade Rule: "session_number, signals_added, signals_removed, verdict_before, and verdict_changed are not affected by the cascade." Bare enumeration — no WHY for scope exclusion. |
| **V-02** | **PASS** | Cascade Rule: "The remaining delta.md fields are excluded from the cascade because they were finalized at Phase 3 Step B: session_number was assigned, signals_added and signals_removed were computed from the session diff, verdict_before was read from the prior run's verdict, and verdict_changed was derived from the before/after pair. Phase 4 cannot change any of these values — they describe session-level facts that exist independently of what Phase 4 concludes. Cascading them would overwrite finalized session history with Phase 4 data that is not session-scoped." Full per-field causal justification. |
| **V-03** | **FAIL** | Cascade Rule with SHALL: "The remaining delta.md fields SHALL NOT be modified: session_number, signals_added, signals_removed, verdict_before, and verdict_changed are outside the cascade scope." SHALL register adds nothing — still bare enumeration, no WHY. |
| **V-04** | **PASS** | Cascade Rule names per-field finalization reasons and closes with "Phase 4 produces a verdict about the topic; it does not revise the session record. Cascading non-cascade fields would overwrite finalized session history with Phase 4-scoped data that was never session-scoped to begin with. Only verdict_after is Phase 4-dependent. That dependency is why it alone cascades." Stronger than V-02 — closes the causal loop with "dependency is why it alone cascades." |
| **V-05** | **PASS** | Cascade Rule (same framing as V-04) + Phase Boundary Summary: "Phase 4 does NOT receive namespace counts (planned, collected, missing, zero_flag) — these fields were finalized at Phase 3 Step A and Phase 4 cannot change them. They are Phase 3 domain. Receiving them as inputs would imply Phase 4 could revise them, which it cannot." + Phase 4 role header: "Phase 4 does NOT receive namespace counts — those were finalized at Phase 3 Step A." Three sites. Note: Phase Boundary Summary addresses RECEIVING scope (what Phase 4 gets), not just CASCADING scope (what Phase 3 Step B re-run updates) — structurally novel from C-37's Cascade Rule locus. |

---

### Composite Scores

| Variation | Essential (50) | Recommended (15) | Aspirational Baseline (81) | C-36 (3) | C-37 (3) | **Total (/137)** |
|-----------|---------------|-------------------|---------------------------|----------|----------|------------------|
| V-01 | 50 | 15 | 81 | 3 | 0 | **134** |
| V-02 | 50 | 15 | 81 | 0 | 3 | **134** |
| V-03 | 50 | 15 | 81 | 0 | 0 | **131** |
| V-04 | 50 | 15 | 81 | 3 | 3 | **137** |
| V-05 | 50 | 15 | 81 | 3 | 3 | **137** |

---

### Ranked Leaderboard

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 | **V-05** | **137/137** | All criteria; three scoring surfaces for C-36 and C-37; Phase Boundary Summary adds novel input/output declaration pattern; SHALL phrasing consistent throughout |
| 1 | **V-04** | **137/137** | All criteria; single scoring surface per new criterion; strongest single-site C-37 causal loop closure ("dependency is why it alone cascades") |
| 3 | **V-01** | **134/137** | C-36 PASS, C-37 FAIL; bare cascade enumeration prevents C-37 |
| 3 | **V-02** | **134/137** | C-37 PASS, C-36 FAIL; bare Phase 4 obligation prevents C-36 |
| 5 | **V-03** | **131/137** | Neither C-36 nor C-37; SHALL phrasing confirms register is not a hidden scoring axis in v11 |

**V-04 vs. V-05 tiebreaker**: On the defined v11 rubric, both score 137/137 — binary PASS on C-36 and C-37. V-05 is elevated over V-04 on excellence-signal grounds (three-site assertion density, Phase Boundary Summary as new structural pattern) but does not score a currently-defined criterion the other doesn't. If a partial ordering between tied variations is required, V-05 ranks first due to higher PASS+ signal density.

---

### Excellence Signals from V-05

**Signal 1 — Phase Boundary Summary as explicit phase data-flow contract**
V-05 introduces a "Phase Boundary Summary" section declaring, for each phase transition, what the receiving phase gets and what it does NOT get (with causal justification for the exclusions). The Phase 3→Phase 4 boundary entry names: read-only inputs (readiness_verdict, coverage_ratio), the placeholder requiring post-write (delta.md), and the exclusion with justification ("Phase 4 does NOT receive namespace counts — these fields were finalized at Phase 3 Step A and Phase 4 cannot change them. They are Phase 3 domain. Receiving them as inputs would imply Phase 4 could revise them, which it cannot."). This is structurally distinct from the Cascade Rule (which governs Phase 3 Step B re-run → cascade direction) and from Typed Output Contracts (which specify field types for outputs, not input ownership boundaries). First occurrence of an "upstream receiving-scope declaration with causal scope justification" pattern. Candidate criterion: **explicit phase input ownership boundary with finalization constraint at receiving site**.

**Signal 2 — Multi-site C-36/C-37 assertion density: three occurrences each**
V-04 achieves C-36 and C-37 PASS via single-site assertions (Phase 4 obligation header for C-36; Cascade Rule for C-37). V-05 asserts each pattern at three independent sites:
- C-36: Phase 4 obligation header → Phase Boundary Summary → empty-state section
- C-37: Cascade Rule → Phase Boundary Summary → Phase 4 role activation header

Each site uses distinct framing. The Phase Boundary Summary's C-36 variant adds a new failure mode phrase ("cannot determine whether the campaign produced a real verdict or was interrupted") not present in V-04. The Phase Boundary Summary's C-37 variant frames the exclusion from the receiving side ("Receiving them as inputs would imply Phase 4 could revise them, which it cannot") rather than the cascade source side. Multi-site, multi-register assertion of the same causal constraint is a structural robustness pattern distinct from density alone.

---

### Verdict on V-03 (SHALL phrasing)

V-03 confirms that phrasing register is **not a scoring axis in v11**. Replacing imperative forms with SHALL throughout produces no new criterion hits — C-36 and C-37 are content-defined (stale-value consequence language; cascade scope causal justification), not register-defined. SHALL might contribute to a future criterion around formal contract specification language, but it requires pairing with new causal content (as V-05 demonstrates) to generate scoring value. V-03's data point: phrasing register alone → 0 new criteria.

---

### Open Question for R13

Does the Phase Boundary Summary pattern in V-05 activate a new criterion around **explicit phase data-flow declaration** (what each phase receives and is prohibited from changing, with causal justification at the transition site)? The pattern is structurally separable from C-15 (typed output contracts), C-37 (cascade scope exclusion), and C-12 (progression gates). If a model executing the V-05 prompt demonstrates correct phase isolation behavior traceable specifically to the boundary section rather than to the contracts or gates alone, that is diagnostic of a new mechanism.

---

```json
{"top_score": 137, "all_essential_pass": true, "new_patterns": ["Phase Boundary Summary as explicit phase data-flow contract — each transition names what the receiving phase gets and does NOT get, with causal justification for exclusions at the receiving site (e.g., 'Phase 4 does NOT receive namespace counts — those were finalized at Phase 3 Step A and Phase 4 cannot change them'); structurally distinct from Cascade Rule (cascade direction) and Typed Output Contracts (field typing); candidate new criterion for R13", "Multi-site C-36/C-37 assertion density — each new pattern asserted at three independent sites with distinct framing; Phase Boundary Summary's C-36 variant adds 'cannot determine whether campaign produced a real verdict or was interrupted'; C-37 variant frames exclusion from receiving direction ('receiving them would imply Phase 4 could revise them, which it cannot') rather than cascade-source direction"]}
```
