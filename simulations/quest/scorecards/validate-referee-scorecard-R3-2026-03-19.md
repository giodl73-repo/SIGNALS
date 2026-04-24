```json
{"top_score": 125, "all_essential_pass": true, "new_patterns": ["Embed failure test as self-verification instruction inside the prompt — 'if X still makes sense without Y, rewrite X' — makes structural dependency checkable at generation time, not just review time", "Anti-pattern vaccination with a plausible-looking FORBIDDEN example — show the fluent-but-wrong form labeled FORBIDDEN alongside the required form; if the FORBIDDEN example looks bad, it does not vaccinate against the actual failure mode"]}
```

---

**Scorecard written** to `simulations/quest/scorecards/validate-referee-scorecard-R3-2026-03-19.md`

---

## Summary

**Top score**: 125/125 — V-04 R3 and V-05 R3 (tie; V-05 R3 preferred)

| Variation | C-14 | C-15 | Total |
|-----------|------|------|-------|
| V-05 R3 | 5 | 5 | **125** |
| V-04 R3 | 5 | 5 | **125** |
| V-01 R3 | 5 | 4 | **124** |
| V-03 R3 | 5 | 4 | **124** |
| V-02 R3 | 2 | 5 | **122** |

**Tiebreak**: V-05 R3 is preferred over V-04 R3 at equal score — the SEED/EXPAND dependency test ("remove SEED; if EXPAND still makes sense on its own, rewrite EXPAND") makes C-14 self-verifying at generation time. V-04 R3 is checkable at review time only.

**Key finding**: C-14 and C-15 are independent failure modes requiring independent mechanisms. Verbatim-anchor quotation alone passes C-14 but leaves C-15 at 4/5. The FORBIDDEN/REQUIRED template alone passes C-15 but leaves C-14 at 2/5. The two compose without tension in V-04/V-05 R3.

**Two new patterns**:
1. **Self-verification instruction**: embed "if X still makes sense without Y, rewrite X" — turns a dependency into a generation-time check
2. **Anti-pattern vaccination**: show the plausible-but-wrong form labeled FORBIDDEN — targets the fluent default, not an obvious failure
y...without anchoring it in this referee's history does not satisfy C-15." Positive instruction + negative example + failure condition present. Missing: formatted FORBIDDEN/REQUIRED template that removes the fluent default path at generation time.

**Total: 124/125**

---

### V-02 R3 — Lifecycle Emphasis: Forbidden/Required Rationale Template

**C-01 through C-13**: 115/115 (inherited)

**C-14**: PARTIAL (2/5)
Phase 2 Experiential sketch: "this sketch will become the core of that referee's character brief in Phase 4" -- advisory only. Phase 4: "make the Phase 2 experiential sketch the foundation of this paragraph" -- advisory only. No structural output field, no verbatim-quote requirement, no SEED/EXPAND. A model can write C-11 and C-13 independently and comply with both instructions -- exactly the C-14 failure mode.

**C-15**: PASS (5/5)
Formatted two-block anti-pattern template:
- DO NOT USE (policy form): plausible-looking example shown and labeled FORBIDDEN
- REQUIRED (persona form): concrete correct example shown and labeled REQUIRED

"A rationale that could have been written without the character briefs existing does not satisfy C-15." The FORBIDDEN example looks like correct output (fluent, editorial-sounding) -- anti-pattern vaccination at its most effective. The label is not on an obviously wrong example but on the fluent default.

**Total: 122/125**

---

### V-03 R3 — Phrasing Register: SEED/EXPAND Character Brief Format

**C-01 through C-13**: 115/115 (inherited)

**C-14**: PASS (5/5)
SEED/EXPAND two-part format: SEED must be verbatim from Phase 2 Experiential sketch; EXPAND must derive from SEED; self-verification test: "remove SEED; if EXPAND still makes full sense on its own, rewrite EXPAND." The dependency test makes the linkage checkable at generation time -- not just at review time. Strongest single-mechanism C-14 enforcement across all variations.

**C-15**: PARTIAL (4/5)
Phase 5: "cite this referee's reviewing history from their character brief -- the reason must derive from who this reviewer is, not from what the journal's editors generically prefer." Explicit positive instruction + anti-form guidance. Clearer than V-05 R2's advisory "if the character brief illuminates why," but no FORBIDDEN/REQUIRED template. Policy form remains the lower-friction generation path.

**Total: 124/125**

---

### V-04 R3 — Combined: Brief-Anchor Quotation + Forbidden/Required Template

**C-01 through C-13**: 115/115 (inherited)

**C-14**: PASS (5/5)
Brief anchor field in Phase 2 (explicit: "structural output, not a note") + Phase 4 requirement: "character brief must open with the Brief anchor verbatim (copy it from Phase 2, inside quotes)." Verbatim quotation makes the sketch the explicit source of the brief. "The anchor must be visible at the start of the brief as a quoted sentence." Output-checkable at every point.

**C-15**: PASS (5/5)
Identical FORBIDDEN/REQUIRED template from V-02 R3. "A rationale that could have been written without character briefs existing does not satisfy C-15." Full enforcement -- both the negative example (policy form, labeled forbidden) and the positive template (persona form, labeled required) are present.

**Total: 125/125**

---

### V-05 R3 — All Three Combined: Brief-Anchor + SEED/EXPAND + Forbidden/Required

**C-01 through C-13**: 115/115 (inherited)

**C-14**: PASS (5/5)
Three-layer enforcement chain -- each link checkable against the previous output:
1. Phase 2: `Brief anchor:` output field ("structural output, not a note")
2. Phase 4: SEED must match Brief anchor verbatim ("If SEED does not match the Brief anchor, the linkage has failed")
3. Phase 4: EXPAND dependency test: "remove SEED; if EXPAND still makes full sense on its own, rewrite EXPAND so that it depends on SEED"

The SEED/EXPAND format adds the self-verification layer that V-04 R3 lacks -- not just that the anchor appears at the start, but that the brief's development is structurally dependent on it.

**C-15**: PASS (5/5)
FORBIDDEN/REQUIRED template from V-02 R3, plus V-05 R3 ties the rationale specifically to EXPAND content: "cite a specific fact from this referee's EXPAND content or character brief." Additional test: "would this rationale survive deleting all character briefs? If yes, rewrite." Anchors C-15 enforcement to the SEED/EXPAND output specifically, making the strongest-referee rationale traceable through the full artifact chain.

**Total: 125/125**

---

## Criterion Analysis

### C-14 difficulty

Three independent mechanisms enforce C-14:
- Verbatim-anchor quotation (V-01, V-04, V-05 R3): makes the sketch a named output that Phase 4 must cite
- SEED/EXPAND format (V-03, V-05 R3): makes the dependency structurally visible in the character brief
- EXPAND dependency test (V-05 R3 only): makes the linkage self-verifiable at generation time

V-02 R3 demonstrates that advisory language alone ("this sketch will become the core of...") scores only 2/5 -- exactly the failure mode C-14 was designed to close.

### C-15 difficulty

C-15 requires anti-pattern vaccination to score 5/5. Positive-instruction-only (V-01, V-03) scores 4/5. Only variations with the FORBIDDEN/REQUIRED template (V-02, V-04, V-05 R3) score 5/5. The policy form is the fluent default -- instruction alone does not displace it.

### Isolation finding

C-14 isolated (V-03 R3): 5/5 C-14, 4/5 C-15 -> 124
C-15 isolated (V-02 R3): 2/5 C-14, 5/5 C-15 -> 122
Both combined (V-04, V-05 R3): 5+5 -> 125

Neither criterion alone reaches ceiling. Both mechanisms are required for 125/125.

---

## Excellence Signals

### Signal 1 -- Self-verification instruction embedded in the prompt (V-05 R3)

V-05 R3's EXPAND dependency test: "remove SEED; if EXPAND still makes full sense on its own, rewrite EXPAND so that it depends on SEED." This instruction encodes the failure test inside the skill -- the model can verify the structural dependency before proceeding, not just after the artifact is produced.

Pattern: Embed the failure test inside the instruction, not just the success criterion. "If X still makes sense without Y, rewrite X" is more actionable than "X must derive from Y."

### Signal 2 -- Anti-pattern vaccination with a plausible-looking FORBIDDEN example (V-02/V-04/V-05 R3)

The FORBIDDEN example must look like correct output: "Referee 2's objections carry most weight because PNAS editors routinely desk-reject on power analysis grounds" -- fluent, editorial-sounding, precisely the form a model will generate by default. Labeling this FORBIDDEN (not an obviously wrong example) removes the fluent default path.

Pattern: Anti-pattern vaccination targets the plausible-but-wrong form, not the obviously wrong form. If the FORBIDDEN example looks bad, it does not vaccinate against the actual failure mode.

---

## New Patterns Extracted

| Pattern | Source | Applicable When |
|---------|--------|----------------|
| Embed failure test as self-verification instruction ("if X still makes sense without Y, rewrite X") | V-05 R3 EXPAND dependency test | Any criterion requiring structural dependency between two skill phases |
| Anti-pattern vaccination: show the plausible-but-wrong form labeled FORBIDDEN alongside the required form | V-02/V-04/V-05 R3 FORBIDDEN/REQUIRED template | Any criterion where the wrong form is fluent and easily generated |

---

## Verdict

- **Top score**: 125/125 (V-04 R3, V-05 R3 -- both at ceiling)
- **All essential pass**: Yes -- all five variations pass C-01 through C-05 (60/60)
- **Preferred variation**: V-05 R3 -- equal score to V-04 R3 but stronger implementation; SEED/EXPAND dependency test makes C-14 self-verifying at generation time
- **Key finding**: C-14 and C-15 are independent failure modes requiring independent enforcement mechanisms; composable without tension; neither alone reaches ceiling
