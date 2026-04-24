## Quest Score — corps-achievements R6

---

## Per-Variation Evaluation

### V-01 — C-21 axis: Correction-Loop Gate

**Essential: 5/5**

| C | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Glob `simulations/**/*.md`; SCAN RECORD built before output; gate names any hallucinated paths |
| C-02 | PASS | COMPUTE GATE [C-02/C-15] cross-checks topic count from scan to output |
| C-03 | PASS | MILESTONES GATE [C-03/C-15] checks exact names; failure quotes misnamed variant |
| C-04 | PASS | `## Contributor Leaderboard` table template present |
| C-05 | PASS | `→ Unlocks **[Achievement or Milestone name]**` in every action row |

**Recommended: 3/3**

| C | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | "Earned Achievements" and "Available Achievements — Locked" — separate labeled sections |
| C-07 | PASS | Two named category labels |
| C-08 | PASS | "## Earned Achievements — Sprint {{date}}" — explicit sprint + date |

**Aspirational: 13/15**

| C | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | 4-column "Almost There — 1-Away Gaps" table |
| C-10 | PASS | Insight must "Span topics or contributors"; named artifact format required |
| C-11 | PASS | Two pre-write self-tests labeled [C-11]: before leaderboard and before actions |
| C-12 | PASS | `→ Unlocks … → Breaks [PATTERN_LABEL from registry]: [sentence]` |
| C-13 | PASS | `**TEAM INSIGHT — [name]:**` format required |
| C-14 | PASS | Registry embedded; `[PATTERN_LABEL from registry]` syntax in action format |
| C-15 | PASS | COMPUTE GATE: "topic '[path]' missing"; MILESTONES GATE: "'[written name]' should be '[exact name]'" |
| C-16 | PASS | `Formula applied: Score = (Signals×1) + (Topics×3) + (Milestones×5)` shown inline |
| C-17 | PASS | Shared registry: SOLO_ISLAND, NAMESPACE_MOAT, SPRINT_FREEZE, SHALLOW_POOL, ORPHAN_TOPIC |
| C-18 | PASS | 4-column table: Topic/Milestone · Achievement to Unlock · Gap · Exact Action Needed |
| C-19 | PASS | "Rank-1 calculation: Score = {Signals}×1 + {Topics}×3 + {Milestones}×5 = {total}" inline |
| C-20 | PASS | SCAN GATE [C-01/C-15], COMPUTE GATE [C-02/C-15], FORMULA VERIFICATION GATE [C-19/C-21] |
| C-21 | PASS | "Correcting the Score column for Rank 1 to {total} before proceeding" — active correction with "Correction is required before this gate passes" |
| C-22 | **FAIL** | Requirement states "not derivable from a single topic view" in prose bullet — no gate tests it per-topic; the derivability framing is stated but not verified |
| C-23 | **FAIL** | Formula gate uses "Then compare: If YES/If NO" prose branches — no `(1)…(2)…(3)…` numbered sub-steps |

**Score = (5/5 × 60) + (3/3 × 30) + (13/15 × 10) = 60 + 30 + 8.67 = 98.7**

---

### V-02 — C-22 axis: Derivability Elimination Protocol

**Essential: 5/5** | **Recommended: 3/3**

**Aspirational: 14/15**

| C | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | 4-column "Almost There" table |
| C-10 | PASS | Full 3-step elimination: Candidate → per-topic YES/NO test → Verdict; discard if any single topic returns YES |
| C-11 | PASS | Pre-write self-test [C-11] before Next Actions section |
| C-12 | PASS | Anti-inertia format with registry syntax |
| C-13 | PASS | Named artifact format `**TEAM INSIGHT — [name]:**` |
| C-14 | PASS | Registry listed; label syntax enforced |
| C-15 | PASS | COMPUTE GATE names missing topic path; DERIVABILITY GATE cites "topic '[path]' alone" |
| C-16 | PASS | Formula shown; Score column in table |
| C-17 | PASS | Semantic registry labels |
| C-18 | PASS | 4-column table |
| C-19 | PASS | Worked example in FORMULA GATE |
| C-20 | PASS | SCAN GATE [C-01], COMPUTE GATE [C-02/C-15], FORMULA GATE [C-19/C-21], DERIVABILITY GATE [C-22/C-15] |
| C-21 | PASS | "If mismatch: correct the Score column to the calculated total before proceeding. No gate passage without confirmed match (or explicit correction applied)" |
| C-22 | PASS | Step A: candidate stated. Step B: each topic tested individually. Step C: if any YES → discard and retry. Full elimination loop. |
| C-23 | **FAIL** | Derivability procedure uses Step A/B/C (lettered phases, not `(1)/(2)/(3)` gate conditions); SCAN/COMPUTE/FORMULA gates use prose commitment statements |

**Score = (5/5 × 60) + (3/3 × 30) + (14/15 × 10) = 60 + 30 + 9.33 = 99.3**

---

### V-03 — C-23 axis: Numbered Sub-Step Gate Language (Universal)

**Essential: 5/5** | **Recommended: 3/3**

**Aspirational: 14.5/15**

| C | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | 4-column table + 1-AWAY GATE conditions (1)–(4) including per-row column completeness |
| C-10 | PASS | INSIGHT GATE condition (3): "not derivable from any single topic view alone" as a numbered gate condition |
| C-11 | PASS | Pre-write self-test before ACTIONS GATE |
| C-12 | PASS | Anti-inertia format |
| C-13 | PASS | Named artifact enforced |
| C-14 | PASS | ACTIONS GATE condition (3): registry label required, no invented labels |
| C-15 | PASS | SCAN GATE: "name the specific file that could not be assigned"; COMPUTE GATE: "topic '[path]' missing"; MILESTONES GATE: condition number + milestone name cited; 1-AWAY GATE: "row '[topic]' missing column '[column name]'" |
| C-16 | PASS | Formula shown |
| C-17 | PASS | Semantic labels |
| C-18 | PASS | 4-column table; 1-AWAY GATE condition (4) enforces completeness per row |
| C-19 | PASS | FORMULA GATE condition (1): worked example |
| C-20 | PASS | 7 gates labeled: SCAN [C-01], COMPUTE [C-02/C-15], MILESTONES [C-03/C-15], FORMULA [C-19/C-21], 1-AWAY [C-09/C-18], ACTIONS [C-05/C-12/C-14], INSIGHT [C-10/C-13] |
| C-21 | PASS | FORMULA GATE condition (3): "If calculated total does not match the Score column entry, I will correct the Score column before proceeding" |
| C-22 | **PARTIAL** | INSIGHT GATE condition (3) uses derivability language ("not derivable from any single topic view alone") — stronger than scope-only — but no per-topic elimination test executes; scope check asks "2+ topics or contributors" (scope framing only); C-22's distinguishing requirement is per-topic testing, which is absent |
| C-23 | PASS | Preamble establishes universal gate language; all 7 gates (SCAN, COMPUTE, MILESTONES, FORMULA, 1-AWAY, ACTIONS, INSIGHT) use `(1)…(2)…(3)…` format |

**Score = (5/5 × 60) + (3/3 × 30) + (14.5/15 × 10) = 60 + 30 + 9.67 = 99.7**

---

### V-04 — C-21 + C-22 combination

**Essential: 5/5** | **Recommended: 3/3**

**Aspirational: 14.5/15**

| C | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | 4-column table |
| C-10 | PASS | Full Steps A, B, C derivability elimination (same protocol as V-02) |
| C-11 | PASS | Pre-write self-test before leaderboard |
| C-12 | PASS | Anti-inertia format |
| C-13 | PASS | Named artifact |
| C-14 | PASS | Registry + label syntax |
| C-15 | PASS | SCAN GATE names inferred paths; COMPUTE GATE: "Missing topic: [path]"; DERIVABILITY GATE: "derivable from topic '[path]' alone" |
| C-16 | PASS | Formula shown |
| C-17 | PASS | Semantic labels |
| C-18 | PASS | 4-column table |
| C-19 | PASS | FORMULA CORRECTION GATE condition (1): worked example |
| C-20 | PASS | SCAN GATE [C-01], COMPUTE GATE [C-02/C-15], FORMULA CORRECTION GATE [C-19/C-21], DERIVABILITY GATE [C-22] |
| C-21 | PASS | FORMULA CORRECTION GATE condition (3): "correct the Score column to the calculated total before proceeding"; condition (4): confirm consistency |
| C-22 | PASS | Full Steps A, B, C elimination protocol identical to V-02 |
| C-23 | **PARTIAL** | Numbered sub-steps applied to FORMULA CORRECTION GATE (4 conditions) only; SCAN, COMPUTE, and other gates use prose; hypothesis explicitly limits C-23 to "formula gate only" |

**Score = (5/5 × 60) + (3/3 × 30) + (14.5/15 × 10) = 60 + 30 + 9.67 = 99.7**

---

### V-05 — C-21 + C-22 + C-23: Full Combination

**Essential: 5/5** | **Recommended: 3/3**

**Aspirational: 15/15**

| C | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | 4-column table + 1-AWAY GATE conditions (1)–(4) |
| C-10 | PASS | Full derivability elimination + INSIGHT GATE condition (3) double-confirms non-derivability |
| C-11 | PASS | Pre-write self-test before Phase 4 leaderboard |
| C-12 | PASS | Anti-inertia format |
| C-13 | PASS | Named artifact enforced by INSIGHT GATE condition (1) |
| C-14 | PASS | ACTIONS GATE condition (3): "exact label syntax — no invented labels" |
| C-15 | PASS | Every gate failure cites specific instance and condition number across all 7 phases; FORMULA GATE: "Score corrected from {old} to {new}" |
| C-16 | PASS | Formula shown with worked example |
| C-17 | PASS | Semantic labels |
| C-18 | PASS | 4-column table; 1-AWAY GATE condition (4) enforces per-row column completeness |
| C-19 | PASS | FORMULA CORRECTION GATE condition (1): worked example inline |
| C-20 | PASS | All 7 gates labeled with criterion IDs; deepest coverage of any variation |
| C-21 | PASS | FORMULA CORRECTION GATE condition (3): correction instruction; condition (4): consistency confirm; "State: 'Score corrected from {old} to {new}.'" |
| C-22 | PASS | Steps A, B, C elimination protocol (per-topic YES/NO test, discard-and-retry) + INSIGHT GATE condition (3) structural confirmation |
| C-23 | PASS | Preamble establishes universal gate standard; all 7 phase gates use `(1)…(2)…(3)…` format; C-21 correction step becomes condition (3), C-22 derivability verdict becomes condition (3) in INSIGHT GATE — both embedded inside the universal structure |

**Score = (5/5 × 60) + (3/3 × 30) + (15/15 × 10) = 60 + 30 + 10 = 100**

---

## Rankings

| Rank | Variation | Score | Gap |
|------|-----------|-------|-----|
| 1 | **V-05** | **100** | — |
| 2 | V-03 | 99.7 | C-22 partial — gate condition uses derivability language but no per-topic elimination test |
| 2 | V-04 | 99.7 | C-23 partial — numbered sub-steps on formula gate only, not universal |
| 4 | V-02 | 99.3 | C-23 fail — Step A/B/C procedure uses lettered phases, not `(1)/(2)/(3)` gate conditions |
| 5 | V-01 | 98.7 | C-22 fail (derivability stated in prose only, no gate); C-23 fail (prose comparison logic) |

---

## Excellence Signals from V-05

**Signal 1 — Universal gate preamble as binding standard**
V-05 opens with a skill-level declaration: "Every multi-condition gate in this skill enumerates its conditions as numbered sub-steps." This is structurally stronger than V-03's preamble because it's framed as an invariant the skill enforces, not just a description of what follows. The result: the C-21 correction step becomes condition (3) of the formula gate, and the C-22 derivability verdict becomes condition (3) of the insight gate — both structurally consistent with every other gate, without ad-hoc integration.

**Signal 2 — Before-after correction trace in gate output**
V-05's FORMULA CORRECTION GATE instructs: "State: 'Score corrected from {old} to {new}.'" V-01 and V-02 instruct correction but don't capture the original value. V-05's formulation makes corrections auditable from the output alone — the reader sees what changed, not just that something changed. This is a self-documenting correction trail inside the gate passage message.

**Signal 3 — Intra-phase label consistency gate condition**
V-05's ACTIONS GATE adds condition (5): "The pattern label in each action row is the same label identified at the top of this phase — no label drift between actions." C-14/C-17 prevent label invention and enforce semantic naming across runs; condition (5) prevents within-run drift where the model introduces a second label mid-section. This is a new category of consistency check (intra-output coherence) not addressed by any prior criterion.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["universal gate preamble — declares numbered-substep standard once at skill top binding all subsequent gates, making C-21 correction step and C-22 derivability verdict structurally consistent with every other gate without ad-hoc integration", "before-after correction trace — formula gate instructs model to state 'Score corrected from {old} to {new}' making table changes auditable from output alone, not just that correction occurred", "intra-phase label consistency — ACTIONS GATE condition checks that the same pattern label appears in every action row within a single run, closing the drift gap C-14/C-17 leave between runs but not within a single output"]}
```
