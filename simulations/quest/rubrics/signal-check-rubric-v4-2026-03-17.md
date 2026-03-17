Reading the scorecard carefully to isolate the net-new R3 pattern not yet captured in v3.

The four `new_patterns` entries map as follows:
- Pattern 1 → C-13 (already in v3)
- Pattern 2 → C-15 (already in v3)
- Pattern 3 → C-16 (already in v3)
- Pattern 4 → **evidence census matrix** — genuinely new, not captured anywhere in v3

One new criterion: **C-17**.

---

# signal-check-rubric v4

**17 criteria across 3 tiers.**

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
| C-13 | **Readiness summary is issued as a pre-analysis draft with CONFIRMED/REVISED resolution** | format | A DRAFT readiness summary is declared before per-dimension analysis begins. Each dimension explicitly marks its finding as CONFIRMED or REVISED against the draft at the production site — immediately after the finding is reached, not assembled post-hoc. A summary that appears only after analysis without a pre-declared draft, or a single overall CONFIRMED/REVISED check appended after all dimensions = fail. |
| C-14 | **Next actions are expressed in `/namespace:skill` command format** | behavior | Every flagged dimension's next action names the specific skill command (e.g., "Run `/signal:scout-inertia`") rather than a generic directive. Next actions that do not include `/namespace:skill` syntax = fail. |
| C-15 | **Staleness threshold is calibrated from inventory composition with declared rationale** | depth | Threshold is chosen based on inventory characteristics (e.g., "14 days because competitive signals are present; 30 days otherwise") and the calibration reason is stated alongside the threshold. A fixed threshold with no calibration rationale, or a dynamic threshold without a declared reason = fail. |
| C-16 | **Per-dimension analysis applies a named internal severity tier decoupled from the coaching register** | depth | Each dimension is assessed against an explicit internal scale (e.g., clean / concern / gap) that is labeled as internal and not presented to the team as a blocking gate. Severity labels must not appear in the coaching narrative — the architectural separation is enforced across the full report, not only at the tier definition. Purely narrative assessment without named severity tiers, or tiers framed as team-facing verdicts, or severity labels that bleed into the coaching sections = fail. |
| C-17 | **Pre-analysis evidence census maps all artifacts before any analytical claim** | coverage | When the artifact inventory is non-trivial (artifacts present across multiple namespaces), the report opens with a census matrix (namespace × artifacts × dates) that establishes the shared evidentiary foundation before any dimension is analyzed. Reports with substantial inventories that dive directly into analysis without a shared reference layer = fail. Reports with sparse inventories (1–2 artifacts total across all namespaces) are exempt. |

---

## Scoring Formula

```
composite = (essential_pass / 5) * 60
          + (recommended_pass / 3) * 30
          + (aspirational_pass / 9) * 10

golden threshold: all 5 essential pass AND composite >= 80
```

---

## Criterion Change Log

| Version | Change |
|---------|--------|
| v1 | Initial: C-01–C-10, aspirational denominator = 2 |
| v2 | Added C-11 (CAUSAL GAP-first ordering) from R1 V-03/V-04. Added C-12 (inertia check) from R1 V-05. Aspirational denominator updated to 4. |
| v3 | Added C-13 (DRAFT readiness summary with CONFIRMED/REVISED lifecycle) from R2 V-01/V-04. Added C-14 (`/namespace:skill` next action format) from R2 V-04. Added C-15 (threshold calibrated from inventory composition) from R2 V-02. Added C-16 (internal severity tier decoupled from coaching register) from R2 V-03. Aspirational denominator updated to 8. |
| v4 | Sharpened C-13 pass condition: inline per-dimension markers required at production site — single post-hoc CONFIRMED/REVISED check no longer passes. Sharpened C-16 pass condition: cross-step prohibition added — severity labels must be absent from the coaching narrative throughout, not only at the tier definition. Added C-17 (pre-analysis evidence census conditional on inventory depth) from R3 V-05. Aspirational denominator updated to 9. |

---

**What changed from v3:**

R3 produced two 100-scoring variations (V-04 and V-05), confirming the four R2 axes are structurally compatible. Two existing criteria were sharpened, and one new criterion was added:

- **C-13 sharpened**: V-02 and V-03 both passed v3's C-13 via a single post-hoc CONFIRMED/REVISED step. V-04's inline per-dimension markers represent the structurally stronger pattern — the lifecycle event must occur at the production site of each finding, not assembled afterward. The pass condition now excludes the post-hoc form.

- **C-16 sharpened**: The R3 new_patterns entry explicitly names a "cross-step prohibition on severity labels appearing in the coaching narrative." V-03 established the INTERNAL ANALYSIS BLOCK; R3 confirms that architectural separation must hold throughout the full report. The pass condition now requires severity labels to be absent from coaching sections, not only correctly labeled at their source.

- **C-17 added**: V-05's evidence census matrix — a namespace × artifacts × dates pre-analysis inventory — was flagged in the R3 scorecard as adding genuine evidentiary value without affecting the v3 score. The criterion is conditional: non-trivial inventories require the census layer; sparse inventories (1–2 artifacts total) are exempt, consistent with the R3 suggestion to calibrate the requirement against inventory depth.

**Re-scoring R3 under v4:** V-04 and V-05 retain 100. V-01, V-02, V-03 each now face stricter C-13 and C-16 pass conditions — V-02 and V-03 likely drop on C-13 (their post-hoc CONFIRMED/REVISED pattern no longer passes), and any variation without the cross-step separation drops on C-16. V-05's census passes the new C-17; V-01 through V-04 lack a census and would fail C-17 on non-trivial inventories, making a clean v4 score of 100 require all five features simultaneously.
