Here is the complete updated rubric:

---

# signal-check-rubric v3

**16 criteria across 3 tiers.**

---

## Essential Criteria (60% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Covers all four named dimensions** | coverage | Output analyzes all four dimensions: CAUSAL GAP, SEQUENCE, COHERENCE, STALENESS. Omitting or merging any two dimensions = fail. |
| C-02 | **CAUSAL GAP section uses artifact evidence, not hypothesis restatement** | correctness | Names specific artifacts present or explicitly names the gap when no artifact exists. Any section that only restates the feature hypothesis as evidence = fail. |
| C-03 | **STALENESS analysis applies a concrete recency threshold with named artifacts** | depth | States a specific threshold (e.g., 30 days) and lists each artifact that falls beyond it by name. A STALENESS finding with no numeric threshold or no named artifacts = fail. |
| C-04 | **States explicitly whether artifact evidence exists for the causal pathway and names what is present or missing** | correctness | States explicitly whether artifact evidence exists for the causal pathway and names what is present or missing. A section that only restates the hypothesis = fail. |
| C-05 | **Output is coaching, not verdictive** | behavior | Surfaces issues as observations the team can decide to address — not blocking failures or binary PASS/FAIL judgments. "You must fix X before proceeding" = fail. |

---

## Recommended Criteria (30% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **STALENESS finding applies a concrete threshold** | depth | Uses an explicit recency criterion (e.g., 30 days) rather than a subjective impression. No threshold stated = fail. |
| C-07 | **Each flagged issue includes a suggested next action** | behavior | Every flagged dimension gets at least one concrete action (e.g., "run discover-competitors again"). Flags without actions = fail. |
| C-08 | **Report opens with a readiness summary** | format | Output begins with a brief summary of clean vs. flagged dimensions and overall readiness before diving into per-dimension detail. Diving straight into per-dimension analysis without any summary = fail. |

---

## Aspirational Criteria (10% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Cross-dimension pattern is named when present** | depth | When multiple dimensions flag the same root weakness, the output names the pattern explicitly. Four separate flags with no root identification = fail when the pattern is obvious. |
| C-10 | **Missing signal types are identified and characterized by namespace** | coverage | Lists namespaces for which no artifact exists and characterizes each gap as expected or concerning given the topic stage. "Inventory" alone without characterization = fail. |
| C-11 | **CAUSAL GAP is presented first among the four dimensions** | format | Report leads with the CAUSAL GAP section (not the summary) before the other three dimensions. Any other dimension-first ordering = fail. |
| C-12 | **CAUSAL GAP includes an inertia check** | depth | Explicitly asks whether doing nothing — or the current approach without the feature — would also produce the claimed outcome. A CAUSAL GAP section that only evaluates the direct mechanism without addressing the null-action alternative = fail. |
| **C-13** | **Readiness summary is issued as a pre-analysis draft with CONFIRMED/REVISED resolution** | format | A DRAFT readiness summary is declared before per-dimension analysis begins. Each dimension explicitly marks its finding as CONFIRMED or REVISED against the draft. A summary that appears only after analysis without a pre-declared draft = fail. |
| **C-14** | **Next actions are expressed in `/namespace:skill` command format** | behavior | Every flagged dimension's next action names the specific skill command (e.g., "Run `/signal:scout-inertia`") rather than a generic directive. Next actions that do not include `/namespace:skill` syntax = fail. |
| **C-15** | **Staleness threshold is calibrated from inventory composition with declared rationale** | depth | Threshold is chosen based on inventory characteristics (e.g., "14 days because competitive signals are present; 30 days otherwise") and the calibration reason is stated alongside the threshold. A fixed threshold with no calibration rationale, or a dynamic threshold without a declared reason = fail. |
| **C-16** | **Per-dimension analysis applies a named internal severity tier decoupled from the coaching register** | depth | Each dimension is assessed against an explicit internal scale (e.g., clean / concern / gap) that is labeled as internal and not presented to the team as a blocking gate. Purely narrative assessment without named severity tiers, or tiers framed as team-facing verdicts = fail. |

---

## Scoring Formula

```
composite = (essential_pass / 5) * 60
          + (recommended_pass / 3) * 30
          + (aspirational_pass / 8) * 10

golden threshold: all 5 essential pass AND composite >= 80
```

---

## Criterion Change Log

| Version | Change |
|---------|--------|
| v1 | Initial: C-01–C-10, aspirational denominator = 2 |
| v2 | Added C-11 (CAUSAL GAP-first ordering) from R1 V-03/V-04. Added C-12 (inertia check) from R1 V-05. Aspirational denominator updated to 4. |
| v3 | Added C-13 (DRAFT readiness summary with CONFIRMED/REVISED lifecycle) from R2 V-01/V-04. Added C-14 (`/namespace:skill` next action format) from R2 V-04. Added C-15 (threshold calibrated from inventory composition) from R2 V-02. Added C-16 (internal severity tier decoupled from coaching register) from R2 V-03. Aspirational denominator updated to 8. |

---

**What changed from v2:**

All four additions come from the R2 excellence signal set. Each addresses a distinct structural gap:

- **C-13** locks in the pre-analysis DRAFT pattern from V-01/V-04. The CONFIRMED/REVISED lifecycle forces a structurally verifiable commitment — a post-hoc summary cannot satisfy it.
- **C-14** raises the C-07 floor. The `/namespace:skill` format from V-04 makes next actions immediately executable; "re-run the analysis" does not pass.
- **C-15** captures V-02's dynamic staleness insight. Calibration rationale declared alongside the threshold makes the finding defensible, not just concrete.
- **C-16** captures V-03's severity table pattern. The key constraint is the decoupling: analytically precise tiers that are explicitly not team-facing gates.

**Re-scoring R2 under v3:** All four 100-tier variations (V-01–V-04) pass C-13 and C-14 at minimum. V-02 passes C-15. V-03 passes C-16. No variation passes all four new criteria, so a v3 perfect score of 100 remains unachieved — correct behavior for a rubric that raises the bar.
