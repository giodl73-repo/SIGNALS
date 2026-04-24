Here is the complete updated rubric:

---

**Changes from v3:**

Two new aspirational criteria extracted from R3 excellence signals:

**C-15 — Accuracy column header includes a concrete worked example alongside the formula** (`depth | aspirational`)
Sourced from V-02 (R3), which extended the header from `Score: (C*100+P*50)/(C+P+W)` to `Score: (C*100+P*50)/(C+P+W) [e.g. C=2,P=1,W=1 -> 62.5]`. Formula-in-header (C-13) makes the formula visible; example-in-header (C-15) makes it executable — a scorer can verify their computation without recalculating. A variation can pass C-13 without passing C-15.

**C-16 — Conflict audit runs unconditionally and emits an explicit result in all cases** (`correctness | aspirational`)
Sourced from V-01 (R3) via mandatory Phase 5 (always runs, always emits either conflict artifact or explicit "no conflict") and V-03 (R3) via pre-populated LOCKED revision log column (absence of revision is as traceable as presence). Both eliminate the author-perception gate in C-14: "when tension arises" becomes "always, unconditionally." C-14 requires naming conflict when perceived; C-16 requires the audit structure to produce output regardless. A variation can pass C-14 without passing C-16.

**Scoring formula update:**
```
aspirational_pass / 8 * 10   (was / 6)
```

The layering chain now has four tiers per axis:

| Axis | T1 (v2) | T2 (v3) | T3 (v4) |
|------|---------|---------|---------|
| Formula | C-11: formula stated | C-13: formula in header | C-15: formula + example in header |
| Conflict | C-12: Echo before accuracy | C-14: conflict named as artifact | C-16: audit unconditional, always emits |
ndered** | correctness | essential | Output provides an overall accuracy judgment -- e.g., score, ratio, or qualitative rating -- for the signal set as a whole. Must be grounded in the predicted vs actual comparisons in C-02. |

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
| C-13 | **Accuracy formula is embedded in the column header itself** | depth | aspirational | The per-namespace accuracy formula appears as the column header label (e.g., `Score: (C*100+P*50)/(C+P+W)`), not only in prose instructions. This structural placement makes it impossible to populate the column without the formula being visible at output time -- the header IS the instruction. An output that states the formula in prose but uses a plain column label (e.g., `Score`) does not pass. |
| C-14 | **Echo-accuracy conflict is explicitly named when tension arises** | correctness | aspirational | When later analysis (accuracy or gap phases) would tempt revision of the locked Echo, the output explicitly names the tension and preserves the original Echo record. The conflict itself becomes a traceable artifact: if Phase N analysis would change the Echo, note the tension but preserve the earlier record. An output that silently revises the Echo after accuracy analysis, or that ignores the conflict entirely, fails this criterion. If no conflict arises in a given retro, mark as pass by default. |
| C-15 | **Accuracy column header includes a concrete worked example alongside the formula** | depth | aspirational | The column header contains not only the formula but a computed example showing sample inputs and the resulting score (e.g., `Score: (C*100+P*50)/(C+P+W) [e.g. C=2,P=1,W=1 -> 62.5]`). The example makes the formula executable at a glance: a scorer can verify their own computation without recalculating. An output that carries the formula in the header (passing C-13) but omits a worked example does not pass this criterion. |
| C-16 | **Conflict audit runs unconditionally and emits an explicit result in all cases** | correctness | aspirational | The output includes a dedicated conflict-audit mechanism -- a mandatory phase, a pre-populated revision log column, or equivalent -- that produces an explicit result whether or not tension is perceived. The result is either a conflict artifact (when tension exists) or an explicit no-conflict acknowledgment (when none exists). The audit must not be author-perception-gated: silence is not a valid no-conflict signal. A variation that names conflict only when the author recognizes tension (passing C-14) but has no unconditional audit structure does not pass this criterion. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
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
- C-15 strengthens C-13: the worked-example-in-header mechanism (first demonstrated in V-02, R3) extends formula visibility to executability -- the scorer can verify their own arithmetic without recalculating, not merely read the formula. A variation can satisfy C-13 without satisfying C-15.
- C-16 strengthens C-14: the unconditional-audit mechanism (first demonstrated in V-01 via mandatory Phase 5 and in V-03 via pre-populated LOCKED revision log, both R3) eliminates the author-perception gate in C-14. C-14 requires naming conflict when the author perceives tension; C-16 requires the audit structure to run and emit output regardless of whether tension is perceived. A variation can satisfy C-14 without satisfying C-16. The mechanism may be a dedicated phase, a pre-initialized table column, or any structure that makes the absence of conflict as traceable as the presence.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-16 | Initial rubric -- 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-16 | Added C-11 (explicit numeric formula for per-namespace accuracy) and C-12 (Echo-before-accuracy phase ordering) from R1 excellence signals; aspirational denominator updated from 2 to 4 |
| v3 | 2026-03-16 | Added C-13 (formula embedded in column header) and C-14 (Echo-accuracy conflict named as artifact) from R2 excellence signals in V-02 and V-03; aspirational denominator updated from 4 to 6 |
| v4 | 2026-03-16 | Added C-15 (worked example in column header alongside formula) and C-16 (conflict audit runs unconditionally, emits explicit result) from R3 excellence signals in V-02 and V-01/V-03; aspirational denominator updated from 6 to 8 |
