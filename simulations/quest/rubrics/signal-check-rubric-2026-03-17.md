Rubric written to `simulations/quest/rubrics/signal-check-rubric-2026-03-17.md`.

**5 essential** criteria map directly onto the 4 declared dimensions plus the coaching-not-verdictive constraint: SEQUENCE must cite artifact dates, COHERENCE must name specific signal pairs, CAUSAL GAP must evaluate mechanism evidence (not just restate the hypothesis), all four dimensions must appear, and tone must stay advisory throughout.

**3 recommended** raise fidelity: staleness needs a concrete threshold (not just vibes), every flagged issue gets a suggested next action, and a readiness summary opens the report.

**2 aspirational** push toward genuine analytical value: naming cross-dimension patterns when multiple flags share a root cause, and inventorying missing signal namespaces (not just evaluating what exists).

The coaching-tone criterion (C-05) is the unusual one — it enforces the "not punitive" design intent structurally, so a skill that produces a correct four-dimension analysis but frames it as a blocking gate fails on essential.
another = fail. |
| C-02 | **SEQUENCE finding is grounded in artifact dates or ordering** | correctness | The SEQUENCE assessment cites actual artifact timestamps or creation order to determine whether discovery happened before specification. A SEQUENCE verdict based on no evidence, or stated without artifact reference, = fail. |
| C-03 | **COHERENCE finding identifies specific agreements or contradictions between signals** | correctness | The COHERENCE assessment names at least two signals and states whether they align or contradict on a specific claim (e.g., two competitor signals disagree on market size). Vague statements like "signals are broadly coherent" with no named comparison = fail. |
| C-04 | **CAUSAL GAP verdict states whether the feature-to-outcome mechanism has evidence** | correctness | The CAUSAL GAP assessment states explicitly whether there is artifact evidence for the causal pathway between the feature and its claimed outcome, and names what is present or missing. A CAUSAL GAP section that only restates the hypothesis without evaluating evidence = fail. |
| C-05 | **Output is coaching, not verdictive** | behavior | The output surfaces issues as observations the team can decide to address -- not as blocking failures or pass/fail judgments. Tone must be actionable and forward-looking. A report that concludes "you must fix X before proceeding" or uses binary PASS/FAIL framing across the full report = fail. |

---

## Recommended Criteria (30% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **STALENESS finding applies a concrete threshold** | depth | The STALENESS assessment uses an explicit recency criterion (e.g., artifacts older than 30 days in a fast-moving market are flagged) rather than a subjective impression. A staleness section that flags nothing and states no threshold = fail. |
| C-07 | **Each flagged issue includes a suggested next action** | behavior | For every dimension where a gap or inconsistency is found, the output provides at least one concrete action the team could take to resolve it (e.g., "run discover-competitors again to refresh the competitive signal"). Flags without actions = fail. |
| C-08 | **Report opens with a readiness summary** | format | Output begins with a brief summary stating how many dimensions are clean, how many have flags, and whether the overall signal set looks ready for commitment. A report that dives straight into per-dimension detail without any summary framing = fail. |

---

## Aspirational Criteria (10% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Cross-dimension pattern is named when present** | depth | If multiple dimensions flag the same underlying weakness (e.g., SEQUENCE and COHERENCE both point to a discovery gap), the output names the cross-dimension pattern explicitly rather than treating each flag independently. A report that lists four separate flags without noticing they share a root = fail when the pattern is present and obvious. |
| C-10 | **Missing signal types are identified by namespace** | coverage | The output lists signal namespaces (discover, specify, validate, simulate, etc.) for which no artifact exists for this topic, and notes whether the gaps are expected or concerning given the topic's stage. A report that only evaluates what exists without noting what is absent = fail. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | all essential + >= 80 | Ready for production use |
| Silver | all essential + 70-79 | Usable, recommended gaps noted |
| Bronze | 4/5 essential + >= 60 | Partial utility, key gap present |
| Fail | any essential miss | Not suitable for use |
