## quest-score Rubric v7

**Changes from v6:**

Two new aspirational criteria extracted from R6 excellence signals:

**C-21 — Echo Lock Record is a multi-field immutability artifact documenting when, what, and how** (`correctness | aspirational`)
Sourced from V-04 (R6) Phase 0 Echo Lock Record table, which carries three named fields: WHEN locked (Phase 0), WHAT the lock status is (LOCKED), and WHAT the authorized conflict response is (log only, never revise). C-17 requires an explicit LOCKED label on the Echo block; C-21 requires the lock designation to be a structured record — not just a label — with at minimum those three fields. A single LOCKED label (passing C-17) that carries no machine-readable record of the lock event and its conflict protocol does not pass this criterion.

**C-22 — Foil section records prior belief before signals are opened, not only post-hoc** (`depth | aspirational`)
Sourced from V-05 (R6) PRE-RETRO + POST-RETRO bracket structure, which requires documenting the prior belief before any signal data is reviewed and filling the actual finding after all phases complete. C-20 requires a status-quo foil section contrasting "Without This Retro" against "With This Retro"; C-22 requires that contrast to be a closed-loop epistemic record rather than a retrospective assertion: both sides cannot be written from hindsight. An output that includes a foil comparison (passing C-20) but records both the prior belief and the actual finding after all phases are complete does not pass this criterion.

**Scoring formula update:**
```
aspirational_pass / 14 * 10   (was / 12)
```

The layering chain now extends to six tiers:

| Axis | T1 (v2) | T2 (v3) | T3 (v4) | T4 (v5) | T5 (v6) | T6 (v7) |
|------|---------|---------|---------|---------|---------|---------|
| Formula | C-11: formula stated | C-13: formula in header | C-15: formula + example in header | — | — | — |
| Echo/Conflict | C-12: Echo before accuracy | C-14: conflict named as artifact | C-16: audit unconditional, always emits | C-17: Echo marked LOCKED | C-20: cost-of-inaction foil | C-22: prior belief captured before signals opened |
| Structure | — | — | — | C-18: phases numbered and named | C-19: phase boundary markers declared | — |
| Lock Record | — | — | — | — | C-17: LOCKED label | C-21: multi-field lock artifact |

---

## Essential Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Signal inventory lists every artifact** | completeness | essential | Output includes a complete table of all signals gathered for the topic — one row per artifact — with at minimum: namespace, artifact date, and prediction made at signal time. No artifact known to exist may be omitted. |
| C-02 | **Accuracy uses predicted-vs-actual comparison** | completeness | essential | Each artifact in C-01 is assessed against what actually happened: Correct (C), Partial (P), or Wrong (W). The comparison must be explicit — not a summary judgment applied retroactively to the full set. |
| C-03 | **Gap analysis identifies missing signals** | completeness | essential | Output identifies which signal types were absent for the topic. For each gap, the namespace and signal type must be named. A generic statement ("we had few signals") does not pass. |
| C-04 | **Exactly one Echo** | behavior | essential | Output contains exactly one Echo: the single most surprising finding from the retro — the thing that genuinely was not expected. Multiple echoes, no echo, or a list of observations all fail. The Echo must be framed as a single sentence. |
| C-05 | **Overall accuracy judgment rendered** | correctness | essential | Output provides an overall accuracy judgment — e.g., score, ratio, or qualitative rating — for the signal set as a whole. Must be grounded in the predicted-vs-actual comparisons in C-02. |

---

## Recommended Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Gap signals are actionable for future topics** | depth | recommended | Each gap in C-03 is accompanied by a concrete suggestion: which skill to run, what question to ask, or what threshold to set. Generic advice ("gather more signals") does not pass. |
| C-07 | **Signal accuracy is differentiated by namespace** | depth | recommended | Accuracy is broken down per namespace (scout, draft, flow, etc.) rather than averaged into a single number. Allows teams to identify which namespaces are consistently reliable vs noisy. |
| C-08 | **AMEND scope is respected when provided** | behavior | recommended | If an AMEND instruction limits scope (specific signal type or time window), the output honors that constraint throughout — inventory, accuracy, gaps, and Echo all stay within scope. |

---

## Aspirational Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Calibration trend is surfaced** | depth | aspirational | Output compares this topic's signal accuracy to a prior retro for the same team or namespace, identifying whether prediction quality is improving, degrading, or stable. Requires at least one prior retro as reference. |
| C-10 | **Echo feeds back into signal design** | depth | aspirational | The Echo finding is translated into a concrete change proposal: a new skill, a rubric amendment, or a threshold adjustment. Not just "we learned X" but "therefore we should do Y differently." |
| C-11 | **Per-namespace accuracy uses an explicit numeric formula** | depth | aspirational | Each namespace's accuracy is computed via a named formula (e.g., `(Correct*100 + Partial*50) / (Correct+Partial+Wrong)`) rather than a qualitative judgment. Makes C-07 output mechanically verifiable and reproducible across runs. A prose verdict per namespace does not pass; a scored result from a stated formula does. |
| C-12 | **Echo phase precedes accuracy scoring** | correctness | aspirational | The Echo is identified and documented before the accuracy verdict is rendered. Phase ordering is structural: naming the unexpected finding first prevents it from being absorbed post-hoc into the accuracy narrative. Output fails this criterion if accuracy is scored before the Echo is named. |
| C-13 | **Accuracy formula is embedded in the column header itself** | depth | aspirational | The per-namespace accuracy formula appears as the column header label (e.g., `Score: (C*100+P*50)/(C+P+W)`), not only in prose instructions. This structural placement makes it impossible to populate the column without the formula being visible at output time — the header IS the instruction. An output that states the formula in prose but uses a plain column label (e.g., `Score`) does not pass. |
| C-14 | **Echo-accuracy conflict is explicitly named when tension arises** | correctness | aspirational | When later analysis (accuracy or gap phases) would tempt revision of the locked Echo, the output explicitly names the tension and preserves the original Echo record. The conflict itself becomes a traceable artifact: if Phase N analysis would change the Echo, note the tension but preserve the earlier record. An output that silently revises the Echo after accuracy analysis, or that ignores the conflict entirely, fails this criterion. If no conflict arises in a given retro, mark as pass by default. |
| C-15 | **Accuracy column header includes a concrete worked example alongside the formula** | depth | aspirational | The column header contains not only the formula but a computed example showing sample inputs and the resulting score (e.g., `Score: (C*100+P*50)/(C+P+W) [e.g. C=2,P=1,W=1 -> 62.5]`). The example makes the formula executable at a glance: a scorer can verify their own computation without recalculating. An output that carries the formula in the header (passing C-13) but omits a worked example does not pass this criterion. |
| C-16 | **Conflict audit runs unconditionally and emits an explicit result in all cases** | correctness | aspirational | The output includes a dedicated conflict-audit mechanism — a mandatory phase, a pre-populated revision log column, or equivalent — that produces an explicit result whether or not tension is perceived. The result is either a conflict artifact (when tension exists) or an explicit no-conflict acknowledgment (when none exists). The audit must not be author-perception-gated: silence is not a valid no-conflict signal. A variation that names conflict only when the author recognizes tension (passing C-14) but has no unconditional audit structure does not pass this criterion. |
| C-17 | **Echo block carries an explicit immutability label visible in the output** | correctness | aspirational | The Echo block is marked with an explicit lock designation — e.g., `ECHO (LOCKED)` — that appears as a structural label in the output, not just implied by phase position or ordering. The label makes the Echo's immutability self-evident to any reader without requiring them to infer it from sequence. C-12 requires Echo precedes accuracy scoring; C-17 requires the lock status itself to be a visible artifact. An output that places the Echo first (passing C-12) but uses no explicit lock label does not pass this criterion. |
| C-18 | **Output structure is divided into explicitly numbered or named phases** | behavior | aspirational | The retro output organizes its sections as explicitly numbered or named phases (e.g., Phase 1 through Phase 5) appearing as structural labels in the output itself. Named phases make the execution sequence auditable by inspection — a scorer can verify that Echo preceded accuracy and that the conflict audit ran without reading prose instructions. C-16 requires the conflict audit runs unconditionally; C-18 requires the structural container (named phases) that makes unconditional execution verifiable at a glance. An output that follows the correct sequence but presents sections as undifferentiated prose blocks or unlabeled tables does not pass this criterion. |
| C-19 | **Explicit phase boundary markers appear between consecutive phases** | behavior | aspirational | The output declares an explicit phase boundary at each phase transition — e.g., `Phase boundary: Echo is now immutable. Proceed to Phase 2.` — as a structural label in the output itself. These markers make phase-sealing an auditable event beyond numbered headings alone: a reader can verify not only that phases are ordered correctly (passing C-18) but that the transition point was explicitly declared. An output that uses numbered and named phases (passing C-18) but moves silently from phase to phase without boundary declarations does not pass this criterion. |
| C-20 | **Output includes a status-quo foil section making cost-of-inaction explicit** | depth | aspirational | The output includes a required counterfactual section — a status-quo foil table or equivalent — that explicitly contrasts the pre-retro default assumption ("Without This Retro") against the actual finding ("With This Retro"). This grounds the Echo feedback loop (C-10) in demonstrated cost: not just "therefore we should do Y differently" but "without this retro, the default assumption would have been Z." An output that proposes a concrete change proposal (passing C-10) but omits the counterfactual comparison does not pass this criterion. |
| C-21 | **Echo Lock Record is a multi-field immutability artifact documenting when, what, and how** | correctness | aspirational | The Echo lock designation is a structured record — not merely a label — carrying at minimum three named fields: WHEN the Echo was locked (phase or step), WHAT the lock status is, and WHAT the authorized conflict response is (e.g., "log only, never revise"). This converts the lock from a reader-facing label into a machine-readable artifact: a scorer can verify the conflict protocol without reading prose. C-17 requires the LOCKED label to be visible in the output; C-21 requires that label to be a structured record with explicit fields. An output that marks the Echo LOCKED (passing C-17) but carries no multi-field record of the lock event and its conflict protocol does not pass this criterion. |
| C-22 | **Foil section records prior belief before signals are opened, not only post-hoc** | depth | aspirational | The status-quo foil is a closed-loop epistemic record: the PRE-RETRO prior belief is documented before any signal data is reviewed, and the POST-RETRO actual finding is recorded after all phases complete. Both sides cannot be written from hindsight — the bracket structure demonstrates belief shift rather than asserting it. C-20 requires a foil comparison contrasting "Without This Retro" against "With This Retro"; C-22 requires that contrast to be temporally anchored: prior belief captured at intake, actual finding captured at close. An output that includes a foil table (passing C-20) but records both sides after all phases are complete does not pass this criterion. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 14 * 10)
```

| Band | Condition |
|------|-----------|
| GOLDEN | All essential pass, composite >= 95 |
| SILVER | All essential pass, composite >= 80 |
