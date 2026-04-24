Looking at the R4 scorecard, I can extract two new excellence patterns before writing the v5 rubric:

**C-17** — from V-01's `ECHO (LOCKED)` label: the Echo carries an explicit immutability marker as a structural artifact, not just implied by phase ordering. C-12 requires Echo precedes accuracy; C-17 requires the lock status itself to be marked.

**C-18** — from V-01's `Phase 1 / Phase 2 / ... / Phase 5` structure: phases are explicitly numbered and named in the output, making the execution sequence auditable by inspection. C-16 requires the conflict audit runs unconditionally; C-18 requires the structural container (named phases) that makes unconditional execution verifiable.

Scoring formula update: `aspirational_pass / 10 * 10`.

---

**Changes from v4:**

Two new aspirational criteria extracted from R4 excellence signals:

**C-17 — Echo block carries an explicit immutability label visible in the output** (`correctness | aspirational`)
Sourced from V-01 (R4), which labels Phase 1 as `ECHO (LOCKED)`. C-12 requires Echo precedes accuracy scoring (ordering); C-17 requires the lock status itself to be a visible structural artifact. The label makes the Echo's immutability self-evident to any reader without requiring them to infer it from phase position alone. An output that places the Echo first (passing C-12) but uses no explicit lock label does not pass this criterion.

**C-18 — Output structure is divided into explicitly numbered or named phases** (`behavior | aspirational`)
Sourced from V-01 (R4), which organizes the retro into Phase 1 through Phase 5 as structural labels in the output itself. Named phases make the execution sequence auditable by inspection — a scorer can verify that Echo preceded accuracy and that the conflict audit ran without reading prose instructions. An output that follows the correct sequence (passing C-12 and C-16) but presents sections as undifferentiated prose blocks or unlabeled tables does not pass this criterion.

**Scoring formula update:**
```
aspirational_pass / 10 * 10   (was / 8)
```

The layering chain now extends the Echo/Conflict axis to four tiers:

| Axis | T1 (v2) | T2 (v3) | T3 (v4) | T4 (v5) |
|------|---------|---------|---------|---------|
| Formula | C-11: formula stated | C-13: formula in header | C-15: formula + example in header | — |
| Echo/Conflict | C-12: Echo before accuracy | C-14: conflict named as artifact | C-16: audit unconditional, always emits | C-17: Echo marked LOCKED |
| Structure | — | — | — | C-18: phases numbered and named |

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

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 10 * 10)
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
- C-15 strengthens C-13: adding a worked example to the header (first demonstrated in V-02, R3) makes the formula executable at a glance. A variation can satisfy C-13 without satisfying C-15.
- C-16 strengthens C-14: the unconditional audit structure (first demonstrated in V-01, R3 via pre-populated revision log columns) eliminates the author-perception gate. A variation can satisfy C-14 without satisfying C-16.
- C-17 strengthens C-12: the explicit LOCKED label (first demonstrated in V-01, R4) makes the Echo's immutability a visible artifact rather than an inferred property of ordering. A variation can satisfy C-12 without satisfying C-17.
- C-18 strengthens C-16: named and numbered phases (first demonstrated in V-01, R4) make the unconditional execution of all phases auditable by structural inspection. A variation can satisfy C-16 without satisfying C-18.
