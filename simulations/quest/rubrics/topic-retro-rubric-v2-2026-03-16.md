Written to `simulations/quest/rubrics/topic-retro-rubric-v2-2026-03-16.md`.

**Changes from v1:**

Two new aspirational criteria extracted from R1 excellence signals:

**C-11 — Per-namespace accuracy uses an explicit numeric formula** (`depth | aspirational`)
- Sourced from V-01 and V-03, both of which stated a formula (`Correct*100 + Partial*50) / total`) before computing namespace scores. Makes C-07 mechanically verifiable — a scorer can reproduce the number, not just agree with the prose.

**C-12 — Echo phase precedes accuracy scoring** (`correctness | aspirational`)
- Sourced from V-03 (Echo-First), which placed the Echo identification in Phase 2 before Phase 5 accuracy. The ordering is load-bearing: once an unexpected finding is named first, it cannot be unconsciously folded into the "adequate prediction" bucket.

**Scoring formula update:**
```
aspirational_pass / 4 * 10   (was / 2)
```
Maximum composite is still 100. A retro that passes all 12 criteria scores `60 + 30 + 10 = 100`. A retro that passes C-09 through C-10 but not C-11/C-12 now scores `aspirational_pass=2/4*10 = 5` on the aspirational band rather than the full 10 — correctly penalizing outputs that stop at "good enough" rather than reaching the verifiable, phase-ordered form.
ection is present and names exactly one unexpected learning** | correctness | essential | Output contains a section titled Echo (or equivalent) with a single finding that was not predicted by any gathered signal. Must be post-ship observable, not a known unknown at commit time. |
| C-05 | **Accuracy verdict is rendered** | correctness | essential | Output provides an overall accuracy judgment -- e.g., score, ratio, or qualitative rating -- for the signal set as a whole. Must be grounded in the predicted vs actual comparisons in C-02. |

---

## Recommended Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Gap signals are actionable for future topics** | depth | recommended | Each gap in C-03 is accompanied by a concrete suggestion: which skill to run, what question to ask, or what threshold to set. Generic advice ("gather more signals") does not pass. |
| C-07 | **Signal accuracy is differentiated by namespace** | depth | recommended | Accuracy is broken down per namespace (scout, draft, flow, etc.) rather than averaged into a single number. Allows teams to identify which namespaces are consistently reliable vs noisy. |
| C-08 | **AMEND scope is respected when provided** | behavior | recommended | If an AMEND instruction limits scope (specific signal type or time window), the output honors that constraint throughout -- inventory, accuracy, gaps, and Echo all stay within scope. |

---

## Aspirational Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Calibration trend is surfaced** | depth | aspirational | Output compares this topic's signal accuracy to a prior retro for the same team or namespace, identifying whether prediction quality is improving, degrading, or stable. Requires at least one prior retro as reference. |
| C-10 | **Echo feeds back into signal design** | depth | aspirational | The Echo finding is translated into a concrete change proposal: a new skill, a rubric amendment, or a threshold adjustment. Not just "we learned X" but "therefore we should do Y differently." |
| C-11 | **Per-namespace accuracy uses an explicit numeric formula** | depth | aspirational | Each namespace's accuracy is computed via a named formula (e.g., `(Correct*100 + Partial*50) / (Correct+Partial+Wrong)`) rather than a qualitative judgment. Makes C-07 output mechanically verifiable and reproducible across runs. A prose verdict per namespace does not pass; a scored result from a stated formula does. |
| C-12 | **Echo phase precedes accuracy scoring** | correctness | aspirational | The Echo is identified and documented before the accuracy verdict is rendered. Phase ordering is structural: naming the unexpected finding first prevents it from being absorbed post-hoc into the accuracy narrative. Output fails this criterion if accuracy is scored before the Echo is named. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | 80-100, all essential pass | Retro is complete and trustworthy |
| Passing | 60-79 or 1 essential miss | Usable but has a notable gap |
| Failing | < 60 or 2+ essential miss | Retro is incomplete; do not use to improve signal design |

---

## Notes

- C-01 and C-02 are the load-bearing criteria: a retro without a full signal inventory or explicit predicted-vs-actual comparison cannot be scored or acted on.
- C-04 (Echo) is non-negotiable: it is the primary learning mechanism of the retro format. An output that omits Echo or lists multiple echoes fails this criterion.
- C-08 applies only when an AMEND instruction is present; if no AMEND is given, mark as pass by default.
- C-09 requires prior retro data; if this is the first retro for a topic, mark as not applicable (counts as pass for scoring).
- C-11 and C-12 were added in v2 from R1 excellence signals: V-01 (Table-First) and V-03 (Echo-First) both scored 100 and demonstrated that an explicit formula and Echo-first ordering are achievable and structurally superior.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-16 | Initial rubric -- 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-16 | Added C-11 (explicit numeric formula for per-namespace accuracy) and C-12 (Echo-before-accuracy phase ordering) from R1 excellence signals; aspirational denominator updated from 2 to 4 |
