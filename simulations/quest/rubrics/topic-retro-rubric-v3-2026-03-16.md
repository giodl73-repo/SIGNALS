Written to `simulations/quest/rubrics/topic-retro-rubric-v3-2026-03-16.md`.

**Changes from v2:**

Two new aspirational criteria extracted from R2 excellence signals:

**C-13 — Accuracy formula is embedded in the column header itself** (`depth | aspirational`)
- Sourced from V-02 (R2), which labeled the accuracy column `Score: (C*100+P*50)/(C+P+W)` rather than just `Score`. The formula-as-header mechanism is structurally stronger than C-11: it makes the formula unavoidable at output time rather than instruction-dependent. A variation can pass C-11 (formula stated in prose) without passing C-13 (formula in the header itself).

**C-14 — Echo-accuracy conflict is explicitly named when tension arises** (`correctness | aspirational`)
- Sourced from V-03 (R2), which added the explicit gate: "If Phase N analysis would change the Echo, note the tension but preserve the earlier record." This converts the primary failure mode of C-12 (silent post-hoc Echo revision) into a named, traceable artifact. A variation can pass C-12 (Echo ordered before accuracy) without passing C-14 (conflict explicitly surfaced).

**Scoring formula update:**
```
aspirational_pass / 6 * 10   (was / 4)
```
Maximum composite is still 100. The pair C-13/C-14 are the structural enforcement layer above C-11/C-12 — a retro that achieves phase ordering and a formula but doesn't enforce them at the structural level now scores `4/6 * 10 ≈ 6.7` on the aspirational band rather than the full 10.
|
| C-04 | **Echo section is present and names exactly one unexpected learning** | correctness | essential | Output contains a section titled Echo (or equivalent) with a single finding that was not predicted by any gathered signal. Must be post-ship observable, not a known unknown at commit time. Outputs with zero echoes or multiple echoes fail this criterion. |
| C-05 | **Accuracy verdict is rendered** | correctness | essential | Output provides an overall accuracy judgment -- e.g., score, ratio, or qualitative rating -- for the signal set as a whole. Must be grounded in the predicted vs actual comparisons in C-02. |

---

## Recommended Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Gap signals are actionable for future topics** | depth | recommended | Each gap in C-03 is accompanied by a concrete suggestion: which skill to run, what question to ask, or what threshold to set. Generic advice (gather more signals) does not pass. |
| C-07 | **Signal accuracy is differentiated by namespace** | depth | recommended | Accuracy is broken down per namespace (scout, draft, flow, etc.) rather than averaged into a single number. Allows teams to identify which namespaces are consistently reliable vs noisy. |
| C-08 | **AMEND scope is respected when provided** | behavior | recommended | If an AMEND instruction limits scope (specific signal type or time window), the output honors that constraint throughout -- inventory, accuracy, gaps, and Echo all stay within scope. |

---

## Aspirational Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Calibration trend is surfaced** | depth | aspirational | Output compares this topic accuracy to a prior retro for the same team or namespace, identifying whether prediction quality is improving, degrading, or stable. Requires at least one prior retro as reference. |
| C-10 | **Echo feeds back into signal design** | depth | aspirational | The Echo finding is translated into a concrete change proposal: a new skill, a rubric amendment, or a threshold adjustment. Not just we learned X but therefore we should do Y differently. |
| C-11 | **Per-namespace accuracy uses an explicit numeric formula** | depth | aspirational | Each namespace accuracy is computed via a named formula (e.g., (Correct*100 + Partial*50) / (Correct+Partial+Wrong)) rather than a qualitative judgment. Makes C-07 output mechanically verifiable and reproducible across runs. A prose verdict per namespace does not pass; a scored result from a stated formula does. |
| C-12 | **Echo phase precedes accuracy scoring** | correctness | aspirational | The Echo is identified and documented before the accuracy verdict is rendered. Phase ordering is structural: naming the unexpected finding first prevents it from being absorbed post-hoc into the accuracy narrative. Output fails this criterion if accuracy is scored before the Echo is named. |
| C-13 | **Accuracy formula is embedded in the column header itself** | depth | aspirational | The per-namespace accuracy formula appears as the column header label (e.g., Score: (C*100+P*50)/(C+P+W)), not only in prose instructions. This structural placement makes it impossible to populate the column without the formula being visible at output time -- the header IS the instruction. An output that states the formula in prose but uses a plain column label (e.g., Score) does not pass. |
| C-14 | **Echo-accuracy conflict is explicitly named when tension arises** | correctness | aspirational | When later analysis (accuracy or gap phases) would tempt revision of the locked Echo, the output explicitly names the tension and preserves the original Echo record. The conflict itself becomes a traceable artifact: if Phase N analysis would change the Echo, note the tension but preserve the earlier record. An output that silently revises the Echo after accuracy analysis, or that ignores the conflict entirely, fails this criterion. If no conflict arises in a given retro, mark as pass by default. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
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
- C-13 strengthens C-11: the formula-in-header mechanism (first demonstrated in V-02, R2) is the strongest enforcement of C-11 because it makes the formula structurally unavoidable rather than instruction-dependent. A variation can satisfy C-11 without satisfying C-13.
- C-14 strengthens C-12: the explicit conflict-naming mechanism (first demonstrated in V-03, R2) is the strongest enforcement of C-12 because it converts the failure mode (silent Echo revision) into a named, traceable artifact. A variation can satisfy C-12 without satisfying C-14. If no tension arises in a given retro, C-14 passes by default.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-16 | Initial rubric -- 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-16 | Added C-11 (explicit numeric formula for per-namespace accuracy) and C-12 (Echo-before-accuracy phase ordering) from R1 excellence signals; aspirational denominator updated from 2 to 4 |
| v3 | 2026-03-16 | Added C-13 (formula embedded in column header) and C-14 (Echo-accuracy conflict named as artifact) from R2 excellence signals in V-02 and V-03; aspirational denominator updated from 4 to 6 |
