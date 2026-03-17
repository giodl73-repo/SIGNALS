# Signal-Check Rubric — v7 (2026-03-17)

## What This Rubric Evaluates

The `signal:check` skill produces a four-dimension signal integrity report across SEQUENCE, COHERENCE, CAUSAL GAP, and STALENESS. This rubric asks whether a given prompt or output reliably produces that report at the quality bar the skill design intends.

**Version history**

| Version | Key addition |
|---------|-------------|
| v1 | 5 essential criteria (C-01–C-05) |
| v2 | 3 recommended added (C-06–C-08); `/8` denominator |
| v3 | C-09–C-13 aspirational; `/8` → analysis-phase focus |
| v4 | C-14–C-16 (register separation, inertia anchor, document shape) |
| v5 | C-17 (SEQUENCE as mechanism-evidence audit); C-18 (PART 2 inertia summary); `/10` denominator |
| v6 | C-19 (verbatim mechanism handoff); C-20 (inertia-relevance column propagation); C-21 (inertia case-strength as dedicated section); `/13` denominator |
| **v7** | C-22 (PART 2 inertia case opens with verbatim mechanism verdict); C-23 (named binary outputs consumed by label in STEP 3 and PART 2); `/15` denominator |

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
| C-19 | **Mechanism verdict from CAUSAL GAP is embedded as a required literal input to SEQUENCE** | depth | SEQUENCE does not run until the CAUSAL GAP mechanism verdict is explicitly quoted in-place (e.g., `Quoting mechanism verdict: "..."`) — making architectural handoff impossible to skip rather than merely instructed. A SEQUENCE section that runs without the mechanism verdict as a named, quoted input = fail when mechanism evidence gaps are present. *Source: V-01 and V-04 R6 differentiation on C-17 — the verbatim-quote requirement elevates C-17 from an instructional norm to an architectural constraint: SEQUENCE literally cannot proceed without consuming the CAUSAL GAP verdict. Strengthens mechanism depth without replacing the C-02 artifact-citation requirement.* |
| C-20 | **Inertia-relevance is a named column in the artifact inventory that CAUSAL GAP explicitly consumes** | depth | The Step 0 inertia anchor seeds a named "Inertia Relevant?" (or equivalent) column in the artifact inventory table, and CAUSAL GAP explicitly scores mechanism evidence against inertia-relevant signals only — creating a traceable inertia thread across at least three phases (Step 0 declaration → inventory tagging → CAUSAL GAP scoring). An inertia anchor that declares the baseline at Step 0 but does not propagate as a named column through inventory = fail; CAUSAL GAP that scores all artifacts equally without filtering to inertia-relevant signals = fail. *Source: V-04 R6 differentiation on C-15 — converts the static Step 0 declaration into a living artifact: the inertia-relevance tag flows from anchor through inventory into CAUSAL GAP, making the mechanism question operationally traceable rather than rhetorically present.* |
| C-21 | **Inertia case-strength occupies a dedicated named section in PART 2, not a combined or inline position** | behavior | The team coaching summary gives the inertia case-strength frame (C-18's "clearly built / partially built / still open") its own named section header at the same structural level as the readiness summary — not merged into the readiness section, not introduced as a sub-question, not positioned inline. An inertia frame that shares a section boundary with readiness or appears as a paragraph within another section = fail. *Source: V-02 and V-04 R6 differentiation on C-18 — dedicating a named section (e.g., `STEP A: INERTIA CASE STRENGTH`) before the readiness draft elevates the inertia question to a structural peer of readiness rather than an addendum, signaling to the team that the two questions are independently answerable and neither subordinates the other.* |
| C-22 | **PART 2 inertia case-strength section opens with mechanism verdict quoted verbatim** | behavior | The dedicated inertia case-strength section in PART 2 (C-21) opens by quoting the CAUSAL GAP mechanism verdict verbatim (e.g., `Quoting mechanism verdict: "..."`) before stating the coaching judgment — making the inertia case architecturally grounded in the analytical record rather than independently re-inferred across the register boundary. A PART 2 inertia section that reaches a coaching conclusion without quoting the mechanism verdict explicitly = fail when mechanism evidence gaps have been identified. *Source: V-01/V-04/V-05 R7 EX-01 — extends C-19's verbatim-quote constraint from SEQUENCE into PART 2: the same architectural guarantee that prevents SEQUENCE from re-inferring the mechanism verdict now prevents the coaching register from doing so. Divergence between coaching conclusion and mechanism verdict becomes detectable by inspection rather than by inference.* |
| C-23 | **Named binary outputs from dimension analysis are consumed by label in STEP 3 and PART 2** | depth | When a dimension analysis produces a named binary verdict (e.g., `Pre-specification gap: YES/NO`), STEP 3's cross-dimension pattern analysis and PART 2's coaching sections explicitly reference that binary by its label — not by re-deriving the conclusion from prose. Cross-dimension synthesis that re-infers a timing or mechanism verdict from analytical prose rather than consuming a named output = fail; PART 2 coaching that references the conclusion without naming the source binary = fail. *Source: V-02/V-04/V-05 R7 EX-02 — converts dimension analysis outputs from prose findings into named artifacts that downstream phases must consume structurally. Cross-dimension patterns become traceable: STEP 3 cannot construct a pattern narrative that contradicts the named binary without the contradiction being visible in the label reference.* |

---

## Scoring Formula

```
composite = (essential_pass / 5  * 60)
          + (recommended_pass / 3  * 30)
          + (aspirational_pass / 15 * 10)
```

**Golden threshold**: All 5 essential pass AND composite >= 80.
