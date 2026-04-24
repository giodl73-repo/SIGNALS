Scorecard written to `simulations/quest/scorecards/trace-contract-scorecard-R1-2026-03-14.md`.

---

## trace-contract — Round 1 Results

**All 5 variations pass golden** (5/5 essential, score >= 80). Full ranking:

| Rank | Variation | Score |
|------|-----------|-------|
| 1 | **V-03** Lifecycle phases | **100** |
| 2 (tie) | V-02 Role sequence | 97.5 |
| 2 (tie) | V-05 Format + role combo | 97.5 |
| 4 | V-01 Pre-printed table | 92.5 |
| 5 | V-04 Conversational | 87.5 |

**Prediction reversal:** V-05 was predicted as ceiling; V-03 wins. The margin: GATE 4's explicit calibration check (`"Severity distribution reviewed -- not all one level unless explicitly justified"`) is the only mechanism across all variations that converts C-09 from a nudge to enforcement. That single gate is worth 2.5 points — the exact margin over V-05.

**Three new patterns from V-03:**
1. **Classification-before-analysis gate** — PHASE 3 prohibits root cause hypotheses; diff phase is classification-only, preventing premature analysis
2. **Negative-constraint gate** — GATE 1 verifies actual output was *not* referenced, not just that expected was written (isolation check vs ordering check)
3. **Calibration gate** — GATE 4 checks distribution before findings finalize; unique to V-03

**Key open question for Round 2:** Does V-03's calibration gate actually produce better-calibrated severity distributions in live model runs, or does the model rubber-stamp the checkpoint? That's the durability test for the pattern.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["classification-before-analysis gate: PHASE 3 prohibits root cause hypotheses -- diff-only phase decouples classification from analysis and prevents premature reasoning", "negative-constraint gate: GATE 1 verifies actual output was NOT referenced during expected phase, not just that expected was written -- isolation check vs ordering check", "calibration gate: GATE 4 explicitly checks severity distribution before findings are finalized -- only mechanism that converts C-09 from nudge to enforcement"]}
```
lly |
| 2 (tie) | **V-02** Role sequence | **97.5** | YES | Role names integrate domain natively; C-06 passes via labeled role sections |
| 2 (tie) | **V-05** Format + role combo | **97.5** | YES | Pre-printed columns + role gate cover C-01/C-02/C-03 structurally; no C-09 gate |
| 4 | **V-01** Pre-printed table | **92.5** | YES | Column anchoring strongest for C-02/C-03; C-07 partial (domain in hints only) |
| 5 | **V-04** Conversational | **87.5** | YES | All essential pass; C-06/C-07 partial; floor test confirms instruction-level is sufficient |

---

## Criterion-Level Notes

### C-01 -- Expected before actual
All five variations pass. Mechanism strength differs:
- **V-01**: Section ordering (10+/20+/30+) -- structural sequence, no gate
- **V-02**: Role gate -- AUTOMATE ENGINEER cannot write until sign-off line present
- **V-03**: GATE 1 with negative constraint check -- verifies actual was not referenced
- **V-04**: Numbered step sequence with explicit "do this before you look at what comes back"
- **V-05**: Role gate (same as V-02) -- same structural guarantee

V-03 and V-05/V-02 are the strongest: gate language forces an explicit sign-off before advancing.

### C-06 -- Three-directory structure explicit
V-04 scores PARTIAL. Step labels (Step 2 = expected, Step 3 = actual) mirror the
three-directory function but do not reference or label the pattern explicitly. All other
variations use labeled section headers that map to input/expected/actual. V-01 is the only
variation to use the canonical 10+/20+/30+ notation.

### C-07 -- Automate/Connectors domain engaged
V-01 and V-04 score PARTIAL. Both provide domain-specific examples in hints and next step
prompts but do not integrate domain language structurally. V-02/V-03/V-05 pass because role
names (CONNECTORS EXPERT, AUTOMATE ENGINEER) are embedded throughout, severity definitions
reference "AUTOMATE consumer" and "connector unusable," and next step examples name connector
actions (regenerate schema, update Parse JSON, update OpenAPI definition).

### C-09 -- Severity distribution calibrated
**Only V-03 passes.** GATE 4 explicitly states: "Severity distribution reviewed -- not all
one level unless explicitly justified." All other variations have a three-section finding
structure or count summary that nudges toward calibration but provides no gate check. This is
the sole differentiator between V-03 (100) and V-05 (97.5).

---

## Prediction vs. Actual

| Prediction | Actual | Assessment |
|------------|--------|------------|
| V-05 ceiling | V-03 ceiling | Reversed -- V-03's GATE 4 calibration check is the decisive advantage |
| V-04 floor | V-04 floor | Confirmed -- conversational register scores lowest |
| V-03 close competitor | V-03 beats V-05 | Phase gate mechanism stronger than role+column combo for C-09 |

Key insight: The prediction assumed aspirational criteria would be approximately even across
variations. V-03 uniquely converted C-09 from PARTIAL to PASS via an explicit gate check --
a mechanism none of the other variations used. The two-point aspirational delta (10 vs 7.5)
was the margin.

---

## Excellence Signals -- V-03

Three structural patterns explain V-03's top score:

**1. Classification-before-analysis gate (GATE 3)**
PHASE 3 is classification only: "No finding analysis or root cause hypotheses in this
section." This prevents the most common trace-contract failure -- writing findings while
constructing the diff. Separating classification (PHASE 3) from analysis (PHASE 4) improves
both the diff quality and the finding quality. No other variation uses this separation.

**2. Negative constraint gate (GATE 1)**
GATE 1 checks not just that expected output was written, but that "No actual output has been
referenced in this phase." This is an isolation check, not just an ordering check. Other
mechanisms only confirm the expected block is present; V-03 confirms the expected block was
not contaminated.

**3. Calibration gate (GATE 4)**
GATE 4 explicitly checks: "Severity distribution reviewed -- not all one level unless
explicitly justified." This is the only C-09 enforcement mechanism across all five variations.
The severity summary table and three-section structure in other variations encourage
calibration; V-03's gate requires it.

---

## Open Questions for Round 2

1. **V-03 vs V-05 in live model runs**: Does V-03's phase gate language produce better
   expected-actual separation than V-05's role gate + column combo on C-01? Scoring predicts
   V-03 wins on mechanism quality but both pass on rubric. Live run comparison needed.

2. **V-04 C-06 floor**: Does conversational register lead models to produce structurally
   labeled output anyway (model defaults to headers) despite no labeled scaffold? If yes,
   V-04 scores higher on C-06 in practice than rubric predicts.

3. **C-09 durability in V-03**: Does GATE 4's calibration check actually produce
   better-calibrated severity distributions in output, or does the model rubber-stamp the
   gate without adjusting findings? Core R2 hypothesis for V-03.

4. **V-07 (not yet tested)**: Pre-printing connector-specific sub-fields (authentication
   handshake, action parameter mapping, trigger payload shape) as required artifact fields --
   would this push V-07 above V-03 on C-07? Current top score has no variation making domain
   fields structurally mandatory.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["classification-before-analysis gate: PHASE 3 prohibits root cause hypotheses -- diff-only phase decouples classification from analysis and prevents premature reasoning", "negative-constraint gate: GATE 1 verifies actual output was NOT referenced during expected phase, not just that expected was written -- isolation check vs ordering check", "calibration gate: GATE 4 explicitly checks severity distribution before findings are finalized -- only mechanism that converts C-09 from nudge to enforcement"]}
```
