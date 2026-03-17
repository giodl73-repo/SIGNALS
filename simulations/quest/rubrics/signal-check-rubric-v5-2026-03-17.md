Done. Here's what changed in v5:

**C-17 — Mechanism-aware SEQUENCE** (from V-01, V-04)
When CAUSAL GAP findings are available, SEQUENCE audits whether discovery *established the mechanism evidence* — not just whether it preceded spec. Fails when SEQUENCE only checks temporal order despite identified mechanism gaps. This is a depth criterion, not a format one.

**C-18 — PART 2 inertia summary question** (from V-02)
The team coaching section must surface "clearly built / partially built / still open" as a top-level inertia frame before dimension observations — not just per-dimension. Advisory framing, so no C-05 risk. Distinct from C-15 (which anchors the analysis phase) and C-16 (which structures the registers).

**Scoring formula**: denominator updated from `/8` to `/10`.
reshold (not just vibes), every flagged issue gets a suggested next action, and a readiness summary opens the report.

**10 aspirational** push toward genuine analytical value: naming cross-dimension patterns when multiple flags share a root cause, inventorying missing signal namespaces (not just evaluating what exists), drafting the readiness summary before dimension analysis (not after), calibrating the staleness threshold from inventory contents rather than author judgment, boxing analysis phases with visual separators and scope budgets to prevent bleed, separating analytical scoring from coaching presentation via register protection, front-loading the status-quo alternative before inventory runs (inertia anchor), splitting the output into a dedicated internal analytical record and a team coaching report by document shape rather than instruction, asking whether SEQUENCE reflects whether discovery established the mechanism evidence (not just temporal order), and surfacing the inertia case-strength question as a top-level frame in the team coaching summary.

The coaching-tone criterion (C-05) is the unusual one — it enforces the "not punitive" design intent structurally, so a skill that produces a correct four-dimension analysis but frames it as a blocking gate fails on essential.

---

## Essential Criteria (60% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **All four dimensions are present** | coverage | The output addresses all four declared dimensions: SEQUENCE, COHERENCE, CAUSAL GAP, and STALENESS. A report that omits any dimension or collapses two into one = fail. |
| C-02 | **SEQUENCE finding is grounded in artifact dates or ordering** | correctness | Cites actual artifact timestamps or creation order. A SEQUENCE verdict with no artifact reference = fail. |
| C-03 | **COHERENCE finding identifies specific agreements or contradictions between signals** | correctness | Names at least two signals and states whether they align or contradict on a specific claim. Vague statements with no named comparison = fail. |
| C-04 | **CAUSAL GAP verdict states whether the feature-to-outcome mechanism has evidence** | correctness | States explicitly whether artifact evidence exists for the causal pathway and names what is present or missing. A section that only restates the hypothesis = fail. |
| C-05 | **Output is coaching, not verdictive** | behavior | Surfaces issues as observations the team can decide to address — not blocking failures or binary PASS/FAIL judgments. "You must fix X before proceeding" = fail. |

---

## Recommended Criteria (30% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **STALENESS finding applies a concrete threshold** | depth | Uses an explicit recency criterion (e.g., 30 days) rather than a subjective impression. No threshold stated = fail. |
| C-07 | **Each flagged issue includes a suggested next action** | behavior | Every flagged dimension gets at least one concrete action (e.g., "run discover-competitors again"). Flags without actions = fail. |
| C-08 | **Report opens with a readiness summary** | format | Output begins with a brief summary of clean vs. flagged dimensions and overall readiness. Diving straight into per-dimension detail = fail. |

---

## Aspirational Criteria (10% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Cross-dimension pattern is named when present** | depth | When multiple dimensions flag the same root weakness, the output names the pattern explicitly. Four separate flags with no root identification = fail when the pattern is obvious. |
| C-10 | **Missing signal types are identified by namespace** | coverage | Lists namespaces for which no artifact exists and notes whether those gaps are expected or concerning given topic stage. Only evaluating what exists = fail. |
| C-11 | **Readiness summary is drafted before dimension analysis and confirmed or revised after** | format | The readiness summary is positioned as an early draft, then confirmed or revised at the close of the dimension section. Summary assembled only after analysis, or contradicting findings without a revision note, = fail. *Source: V-05 R1 structural fix — STEP 2 before STEP 3, paired with "draft now, finalize after."* |
| C-12 | **Staleness threshold is calibrated from inventory contents, not author judgment** | depth | Threshold is dynamically derived from inventory (e.g., tightens to 14 days when competitor signals exist, relaxes for early-stage topics). Fixed threshold regardless of inventory composition = fail. *Source: V-05 R1 inventory-triggered tightening — "use 14 days if any competitor signals exist."* |
| C-13 | **Analysis phases are isolated via visual separators and scope budgets** | format | Each analysis phase is boxed with a visible border marker and annotated with a scope budget (word count or sentence limit). Phases that bleed into one another or carry no proportionality constraint = fail. *Source: V-04 R2 — prevents analysis bleed, enforces proportionality across phases. Compatible with conversational register: `---STEP N--- (~X words) ---` markers satisfy the criterion without a template frame.* |
| C-14 | **Severity scale is embedded in analysis but protected from coaching register** | behavior | The output uses a structured internal scoring mechanism (e.g., severity table, ranked flags) and labels it as internal-only, keeping the team-facing prose advisory in tone. Severity exposed directly to team as a gate, or no internal scoring structure present, = fail. *Source: V-02 R2 — separates analytical precision from coaching presentation without sacrificing either. Compatible with conversational register: inline `(internal: green/yellow/red)` notation satisfies the criterion.* |
| C-15 | **Status-quo alternative is anchored at Step 0 before inventory runs** | depth | The output front-loads an explicit "beats doing nothing?" framing before the dimension analysis begins — establishing the inertia baseline so each dimension can be evaluated against the cost of not acting rather than in isolation. Dimension analysis that begins without a declared inertia baseline = fail when the topic has any detectable status-quo alternative. *Source: V-04 R3 — propagates the beats-doing-nothing question through all four dimensions, making cross-dimension patterns more legible when they trace to a shared inertia-beating gap.* |
| C-16 | **Two-register separation is enforced by document shape, not instruction** | behavior | The output is divided into a named internal analytical record (e.g., PART 1) and a named team coaching report (e.g., PART 2) as distinct document sections. Register protection that depends solely on inline warnings or per-paragraph labels = fail; structural separation by section boundary is required. *Source: V-05 R3 — makes C-14 register leakage architecturally impossible rather than instruction-dependent: the team coaching section cannot acquire severity labels because it is a separate document section with no severity rows.* |
| C-17 | **SEQUENCE is evaluated as mechanism-evidence audit, not temporal ordering alone** | depth | When CAUSAL GAP has been evaluated first (or its findings are available), SEQUENCE asks whether the discovery phase established the mechanism evidence — not merely whether discovery preceded spec. A SEQUENCE section that only audits temporal order and ignores whether discovery built the right causal case = fail when mechanism evidence gaps have been identified. *Source: V-01 and V-04 R5 — CAUSAL GAP-first framing qualitatively changes SEQUENCE: "did discovery precede spec?" becomes "did discovery establish the mechanism evidence you just evaluated?" Strengthens mechanism depth without degrading the C-02 artifact-citation requirement.* |
| C-18 | **PART 2 opens with an inertia case-strength question at summary level** | behavior | The team coaching summary (PART 2 or equivalent) includes a top-level readiness frame that explicitly asks whether the case that the feature beats doing nothing is clearly built, partially built, or still open — before or alongside the dimension observations. Inertia framing that appears only within individual dimension coaching (never at summary level) = fail. *Source: V-02 R5 — extends C-15's Step 0 inertia anchor into the coaching register at summary level, adding a distinct framing that is advisory ("clearly built / partially built / still open") and does not risk C-05. Complements C-15 (which anchors the analysis) and C-16 (which structures the registers) without duplicating either.* |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 10 * 10)
```

**Golden threshold**: All 5 essential pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | all essential + >= 80 | Ready for production use |
