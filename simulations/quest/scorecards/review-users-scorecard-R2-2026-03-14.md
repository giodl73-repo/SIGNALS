## Scorecard: review-users Round 2

### Rubric Version
v2 — 13 criteria: 5 essential (60 pts), 3 recommended (30 pts), 5 aspirational (10 pts)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

---

### Per-Variation Scores

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 (essential) | PASS | PASS | PASS | PASS | PASS |
| C-02 (essential) | PASS | PASS | PASS | PASS | PASS |
| C-03 (essential) | PASS | PASS | PASS | PASS | PASS |
| C-04 (essential) | PASS | PASS | PASS | PASS | PASS |
| C-05 (essential) | PASS | PASS | PASS | PASS | PASS |
| C-06 (recommended) | PASS | PASS | PASS | PASS | PASS |
| C-07 (recommended) | PASS | PASS | PASS | PASS | PASS |
| C-08 (recommended) | PASS | PASS | PASS | PASS | PASS |
| C-09 (aspirational) | PASS | PARTIAL | PARTIAL | PASS | PASS |
| C-10 (aspirational) | PASS | PASS | PASS | PASS | PASS |
| C-11 (aspirational) | PASS | PASS | PASS | PASS | PASS |
| C-12 (aspirational) | FAIL | PASS | FAIL | PASS | PASS |
| C-13 (aspirational) | FAIL | FAIL | PASS | FAIL | PASS |
| **Composite** | **96** | **96** | **96** | **98** | **100** |
| **Golden** | YES | YES | YES | YES | YES |

**All 5 variations are Golden.** All essential criteria pass in every variation.

---

### Criterion-Level Evidence

#### C-09 — PARTIAL in V-02 and V-03

**V-02**: Instruction present — `"Flag friction inline: (confusion) (friction) (fear) (jargon)"` — but no correct/wrong examples. The mechanic is stated once in a bullet list without contrast examples. Models following this variation will often tag inline correctly, but the structural enforcement is weaker than variations providing the anti-example pattern.

**V-03**: Same weakness — `"Flag friction inline: [confusion] [friction] [fear] [jargon]"` embedded in a template placeholder line with no contrast pattern. Additionally uses square brackets (`[]`) rather than parentheses (`()`) used in other variations, introducing minor inconsistency.

**V-01, V-04, V-05**: PASS — all three provide the full correct/wrong contrast block:
> Correct: I read "deploy on merge" and (confusion) had no idea which merge this meant.
> Wrong: **Confusion findings:** "deploy on merge" — the persona did not understand this.

This pattern explicitly names the failure mode, making the criterion structurally unfailable.

#### C-12 — FAIL in V-01 and V-03

V-01 uses generic role headers (`### Maker`, `### Developer`) with no character names. V-03 same. No scenario briefs ground the character before the walkthrough. The rubric requires "a named character with a concrete situational detail before the walkthrough begins."

#### C-13 — FAIL in V-01, V-02, V-04

No Beats/Loses fields in these variations. V-03 and V-05 both include explicit `**Beats current process:**` / `**Loses to current process:**` template slots per persona.

---

### Ranking

| Rank | Variation | Composite | Golden | Key Gap |
|------|-----------|-----------|--------|---------|
| 1 | **V-05** | **100** | YES | None — all 13 criteria pass |
| 2 | **V-04** | **98** | YES | C-13 absent (no Beats/Loses fields) |
| 3 (tie) | **V-01** | **96** | YES | C-12 and C-13 absent |
| 3 (tie) | **V-02** | **96** | YES | C-09 weak enforcement; C-13 absent |
| 3 (tie) | **V-03** | **96** | YES | C-09 weak enforcement; C-12 absent |

V-04 breaks the three-way tie at 96 by hitting C-09 strongly (correct/wrong examples) and C-12 (named characters). Its only gap is C-13 — the inertia fields that V-05 adds.

---

### Why V-05 Wins All Five Aspirationals

**C-11** — Pre-committed table with named characters appears as the first output block. Structural lock on C-01/C-02.

**C-12** — Named characters (Sam/Dev/Casey/Jordan/Alex) with scenario briefs *plus* the "What X does today instead" field. Two layers of character grounding before the walkthrough begins.

**C-13** — Explicit `**Beats current process:**` / `**Loses to current process:**` template slots. Non-omissible structural fields.

**C-09** — Inline friction tags with full correct/wrong contrast block. Same strength as V-01 and V-04.

**C-10** — Amend loop references the character's "Loses to current process" entry, producing actionable amendments grounded in named workarounds rather than abstract usability gaps.

No structural trade-offs remain in V-05. Named characters make inline tags feel like personal observations — writing *as Sam* produces "I read X and (confusion) couldn't tell…" naturally. Inertia fields feed mechanically into the synthesis conflict detection. The three mechanisms (character grounding, inline typing, inertia fields) reinforce rather than compete.

---

### Excellence Signals

**Signal 1 — "What X does today instead" as a pre-walkthrough context field (V-05)**

Adding a pre-narrative context field ("Sam's current workaround or manual process when this feature doesn't exist") changes the character of the Beats/Loses output. Instead of scoring the artifact in isolation, the persona evaluates it against a named alternative. This grounds the inertia summary in specifics and makes the amend loop proposals actionable: the proposed change closes a named gap rather than an abstract usability problem.

**Signal 2 — Named character + inline tag + inertia fields are structurally compatible (V-05)**

The R1 tension between C-06 and C-09 was a structural problem: sub-section friction typing (V-03 R1) required analytical mode, which broke first-person voice. V-05 resolves this because all three mechanisms pull in the same direction when combined: named character grounding makes first-person feel natural, inline tags fit inside first-person sentences, and inertia fields follow naturally from "what Sam does today." No format switching needed.

**Signal 3 — Inertia summary section elevates C-08 output quality (V-03/V-05)**

The synthesis section in V-03 and V-05 adds an inertia summary block (`Strongest adoption pull / Highest inertia / Rollout implication`) that was absent in R1. This converts conflict detection (identifying trade-offs) into actionable rollout sequencing (who to onboard first). The Beats/Loses fields supply the inputs; the inertia summary section synthesizes the rollout implication. The output is more useful than a conflict list alone.

---

### R3 Hypothesis

V-05 is the combination target; no gaps remain among the 13 v2 criteria. The natural next question is whether the template is over-specified — V-05 is the longest and most constrained of the five variations. R3 could test:

1. **Length/complexity reduction** — can V-05 be simplified while preserving the structural guarantees? Remove the "What X does today instead" field from the template, keep only Beats/Loses, and verify C-12 still passes via the character brief alone.
2. **Synthesis depth** — add a quantitative adoption-risk score (e.g., net inertia score per persona = count(Beats) − count(Loses)) to drive the inertia summary from field counts rather than free-form prose.

---

### Round Summary

| Metric | Value |
|--------|-------|
| Variations scored | 5 |
| Golden | 5 (all) |
| Top composite | 100 |
| All essential pass | YES |
| Failing essential criteria | None |
| Weakest criterion across round | C-09 (PARTIAL in V-02/V-03 — no contrast examples); C-13 (FAIL in V-01/V-02/V-04) |
| Best aspirational reliability | V-05 (all 5 aspirationals pass) |
| Best structural enforcement | V-05 = V-01 (both have correct/wrong inline tag examples) |
| New pattern count | 3 |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["'What X does today instead' pre-narrative field grounds inertia before walkthrough begins — makes Beats/Loses fields feel natural and amend proposals actionable against a named workaround rather than abstract usability gaps", "named character + inline friction tags + inertia fields are structurally compatible with no trade-offs — all three mechanisms reinforce first-person voice when combined, resolving the R1 C-06/C-09 tension", "inertia summary section (strongest adoption pull / highest inertia / rollout implication) elevates conflict detection to rollout sequencing — Beats/Loses fields supply inputs, synthesis section converts to actionable output"]}
```
