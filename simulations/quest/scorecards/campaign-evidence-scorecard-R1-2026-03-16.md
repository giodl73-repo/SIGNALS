# Quest Score — campaign-evidence R1

> **Note**: The variate file contains V-01 and V-02. V-03 through V-05 appear truncated — scoring covers the two complete variations provided.

---

## V-01 — Post-Evidence Hypothesis (Role Sequence)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All five prove skills executed | **PASS** | All 5 stages listed explicitly in order: prove-websearch → prove-intelligence → prove-analysis → prove-hypothesis → prove-synthesize |
| C-02 | Confidence level per finding | **PASS** | Stage 3 requires confidence per thematic cluster; Stage 5 brief format requires "[WEB-NN] with confidence labels" per finding |
| C-03 | Falsification status declared | **PASS** | Hypothesis Register table in Stage 5 requires Supported / Refuted / Indeterminate per hypothesis |
| C-04 | Evidence brief is self-contained | **PASS** | Stage 5 produces titled brief with scope paragraph, structured sections, synthesized narrative |
| C-05 | Source attribution per claim | **PASS** | [WEB-NN] / [INT-NN] markers used throughout; Key Evidence column in hypothesis table cross-references IDs |
| C-06 | Consensus vs. conflict explicit | **PASS** | Section 4 explicitly instructs: "State this explicitly — do not just list both" |
| C-07 | Confidence levels calibrated | **PASS** | Explicit calibration rule: "If every finding is 'Medium,' you have not calibrated — revise" |
| C-08 | Gaps and open questions | **PASS** | Section 5 "Open Questions" with explicit instruction |
| C-09 | Decision readiness signal | **PASS** | Section 6 "Decision Readiness: One sentence: Ready to proceed / Needs more investigation on [X]" |

**Essential**: 4/4 → 60 pts
**Recommended**: 3/3 → 30 pts
**Aspirational**: 2/2 → 10 pts
**Composite**: **100**

---

## V-02 — Table-First, Numeric Scale

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All five prove skills executed | **PASS** | All 5 stages present (reordered — hypothesis first): prove-hypothesis → prove-websearch → prove-intelligence → prove-analysis → prove-synthesize |
| C-02 | Confidence level per finding | **PASS** | Numeric 1–5 scale per row in findings tables; minimum 5 rows required in final brief |
| C-03 | Falsification status declared | **PASS** | "Hypothesis Register (final)" table with Status column: Supported / Refuted / Indeterminate |
| C-04 | Evidence brief is self-contained | **PASS** | Structured EVIDENCE BRIEF block with topic, date, labeled sections |
| C-05 | Source attribution per claim | **PASS** | "Stage Source" and "Attribution" columns in Top Findings table; [IDs] cross-referenced |
| C-06 | Consensus vs. conflict explicit | **PASS** | **Consensus** and **Conflict** sections in Stage 5 with explicit instructions (not a list) |
| C-07 | Confidence calibrated, not uniform | **PASS** | Numeric scale with named anchors (1=Speculative → 5=Definitive) structurally discourages uniform rating |
| C-08 | Gaps and open questions | **PARTIAL** | **Open Questions** section header present in Stage 5 template but content instruction is absent (cut off); output likely sparse |
| C-09 | Decision readiness signal | **FAIL** | No Decision Readiness section in the prompt; brief ends at Open Questions |

**Essential**: 4/4 → 60 pts
**Recommended**: 3/3 → 30 pts
**Aspirational**: 0/2 → 0 pts
**Composite**: **90**

---

## Ranking

| Rank | Variation | Composite | All Essential | Notes |
|------|-----------|-----------|---------------|-------|
| 1 | V-01 | 100 | Yes | Perfect coverage across all 9 criteria |
| 2 | V-02 | 90 | Yes | Stronger calibration mechanism; missing C-09, C-08 partial |

---

## Excellence Signals from V-01

**1. Calibration rule baked into the prompt.** The explicit instruction "If every finding is 'Medium,' you have not calibrated — revise" is more likely to produce varied confidence than a scale definition alone. V-02's numeric scale helps structurally but V-01's explicit anti-pattern guard is more direct.

**2. Post-evidence hypothesis order eliminates forward-anchoring.** Stating hypotheses after web + intelligence gathering means falsification decisions are grounded in actual findings, not confirmed against pre-committed assumptions. The falsification status in Stage 4 is sharper because the model hasn't already committed to a direction.

**3. Decision Readiness as a required one-liner.** Forcing a single actionable verdict sentence (Section 6) compresses synthesis into a posture statement — it doesn't just report, it recommends. V-02 omits this and the output stops at findings rather than reaching a recommendation.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["post-evidence hypothesis declaration produces sharper falsification because the model calibrates against actual findings rather than assumed ones", "explicit calibration anti-pattern guard ('if every finding is Medium, revise') outperforms scale definitions alone at producing varied confidence distribution", "required single-sentence decision readiness verdict compresses synthesis into an actionable posture rather than stopping at findings"]}
```
