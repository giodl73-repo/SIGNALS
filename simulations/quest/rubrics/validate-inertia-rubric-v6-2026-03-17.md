Done. Here's what was extracted and why each is a new criterion rather than a pass-condition tightening:

---

**C-21 — Phase-zero methodology gate** (behavior)
C-09 only requires the methodology declaration to exist. C-21 requires it to be positioned as Phase 1 output — before any persona — and explicitly framed as the infrastructure C-17 will draw from. Without this, models pass C-09 with a methodology section buried after scoring, then produce C-17 traces that cite dimension values against a threshold the reader has to search backward to find. The cascade double-failure (C-09 + C-17) across all R5 non-V-25 variations is diagnostic: ordering is the structural defect.

**C-22 — Competitive strength inventory in persona phase** (depth)
C-11 requires naming the win dimension at kill-barrier analysis time. C-22 requires the Dimension/Advantage/Durability inventory to be built during persona identification — before Phase 5 — so Phase 5's Part (2) structural persistence can cite a named property rather than construct one on demand. The R4 pattern where C-11 was PARTIAL across all variations confirms the root cause: competitive framing under analytical pressure produces "familiarity" rather than structural durability.

**C-23 — Named intervention target as falsifiable anchor** (depth)
C-15 requires four labeled sub-parts and Part (3) to name what the intervention targets. C-23 requires Part (3) to name a *mechanism*, not an approach — specific enough that C-16 can express a falsifiable observable condition tied to it. "Improve onboarding" is approach granularity; "the moment a user completes their first cross-team workflow" is mechanism granularity. Without the mechanism name, C-16 produces vague forward hopes ("adoption will increase") rather than falsifiable conditions ("at T=6mo, X is observable as absent").

**Scoring:** 230 pts max (was 200). File at `simulations/quest/rubrics/validate-inertia-rubric-v6-2026-03-17.md`.
ction, habit lock-in + social proof coverage,
  mitigation path for the kill barrier
- **15 aspirational (C-09--C-23):** scoring methodology transparency, time-dependent inertia
  trajectory, status-quo competitor framing, named social proof threshold, mitigation tied to
  structural root cause, kill-barrier temporal persistence test, causal chain with labeled
  structural sub-parts, mitigation confirmation signal, per-score methodology trace,
  kill-barrier trajectory verdict, related-output structural segregation with disqualifier,
  kill-barrier reselection gate, phase-zero methodology gate, competitive strength inventory
  in persona phase, named intervention target as falsifiable anchor

Scoring: Essential = 10 pts each (50 total), Recommended = 10 pts each (30 total), Aspirational =
10 pts each (150 total) = **230 pts max**.

---

## Essential Criteria (all must pass)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | **Per-persona inertia mapping** | correctness | Output identifies two or more named user personas and maps each to one or more inertia factors. Generic "users" without persona differentiation fails. |
| C-02 | **Quantified switching cost** | correctness | At least one persona has a switching cost expressed as a measurable value -- time, money, effort rating (1-10), or steps. Qualitative-only ("it's hard") fails. |
| C-03 | **Per-persona inertia score** | correctness | Each mapped persona has an explicit inertia score (numeric or Low/Medium/High/Critical). A single blanket score for all personas fails. |
| C-04 | **Kill-barrier identification** | depth | Output identifies exactly one adoption killer -- the single factor most likely to block adoption even if all other inertia is resolved. Must be labeled distinctly. |
| C-05 | **Overall adoption inertia risk** | correctness | Output produces an aggregate risk verdict with a sentence of rationale tying it back to the per-persona scores. |

---

## Recommended Criteria

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | **Current workaround satisfaction assessed** | coverage | For at least one persona, output describes how satisfied they are with their current workaround and why that satisfaction creates inertia. |
| C-07 | **Habit lock-in and social proof addressed** | coverage | Output addresses habit lock-in AND social proof for at least one persona each. Missing both fails; covering one partially passes. |
| C-08 | **Mitigation path per critical barrier** | depth | For the kill barrier in C-04, output proposes at least one concrete mitigation that could reduce or eliminate that barrier. |

---

## Aspirational Criteria

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | **Inertia score methodology explained** | behavior | Output briefly explains how inertia scores were derived -- what factors were weighted and why. A single sentence per dimension suffices. |
| C-10 | **Adoption timeline sensitivity** | depth | Output includes at least one time-dependent statement on how inertia evolves (e.g., "after 6 months of workaround use, lock-in doubles"). |
| C-11 | **Status-quo framed as named competitor** | depth | For the kill barrier in C-04, output names the dimension on which the current solution *wins* and explains why that competitive advantage is durable -- not just "people are used to it" but what property of the current solution makes it structurally hard to displace. |
| C-12 | **Named social proof threshold** | coverage | For at least one persona where social proof is a factor, output specifies the adoption threshold as a concrete condition or count (e.g., "needs 2+ teammates before committing," "will adopt solo if manager mandates it"). Binary Y/N without a named threshold fails. |
| C-13 | **Mitigation tied to structural root cause** | depth | The mitigation from C-08 explicitly explains *why* the intervention neutralizes the structural reason the barrier exists -- not just what to do, but why that lever addresses the specific root cause named in C-04. Addressing a symptom rather than the stated structural cause fails. |
| C-14 | **Kill barrier tested against temporal persistence** | depth | The kill barrier identified in C-04 is explicitly qualified against a temporal horizon -- output states that the barrier persists at T=0 AND remains unresolved at the longest time horizon considered (e.g., T=18mo). A kill barrier identified only as a current-state snapshot without temporal qualification fails. |
| C-15 | **Causal chain with labeled structural sub-parts** | depth | For the kill barrier, output provides a causal chain with explicitly labeled, distinct sub-parts covering: (1) what the barrier is, (2) why it structurally persists, (3) what the intervention targets, and (4) why that lever resolves the structural root cause. An analysis that merges any two sub-parts into a single statement, or that provides fewer than four labeled parts, fails. |
| C-16 | **Mitigation confirmation signal specified** | depth | The kill barrier mitigation from C-08 includes a named leading indicator or observable condition at a future time point (e.g., "at T=6mo, [X behavior] would confirm the barrier is reducing") that would confirm the intervention is working. A mitigation without a forward-looking confirmation condition fails. |
| C-17 | **Per-score methodology trace** | behavior | For each persona scored in C-03, output includes a derivation sentence that explicitly connects that persona's dimension values to the declared scoring threshold from C-09, showing how the score was produced. The strongest enforcement mechanism is a required column in the score table -- a column cannot be omitted without omitting the table, making non-compliance structurally visible. A global methodology declaration (C-09) without per-persona derivation fails. A trace that cites dimension values but not the threshold, or the threshold but not the dimension values, earns PARTIAL. |
| C-18 | **Kill-barrier trajectory verdict** | depth | Beyond any per-persona timeline grid satisfying C-10, output provides a separate, explicitly labeled verdict for the kill barrier's own time-sensitivity -- a trajectory direction (Resolving / Stable / Worsening) with structural reasoning tied to the persistence property identified in C-15(2). A verdict present in the grid only, without a dedicated kill-barrier trajectory statement, fails. |
| C-19 | **Related-output structural segregation with disqualifier** | behavior | When output produces two related but structurally distinct required outputs (e.g., a per-persona timeline grid satisfying C-10 and a kill-barrier trajectory verdict satisfying C-18), each is housed as an explicitly labeled sub-section AND the first sub-section includes a literal statement that it does not satisfy the second criterion. Absence of the explicit disqualifier statement fails; implicit separation without the disqualifier earns PARTIAL. |
| C-20 | **Kill-barrier reselection gate** | depth | The temporal persistence test for the kill barrier includes an explicit binary YES/NO confirmation that the barrier exists at T=0 AND persists at the longest time horizon considered, followed by a literal reselection instruction triggered if either answer is NO. Implicit persistence conveyed through a grid row or trajectory statement without a binary confirmation gate fails; a gate present at one horizon only earns PARTIAL. |
| C-21 | **Phase-zero methodology gate** | behavior | The methodology declared in C-09 is positioned as Phase 1 output -- before any persona is identified or scored -- and explicitly framed as the scoring infrastructure from which per-score traces (C-17) will draw. The phase must declare dimension weights AND tier thresholds AND identify itself as the source C-17 traces will cite. A methodology section placed after persona analysis fails. A declaration that omits the explicit framing as C-17 infrastructure earns PARTIAL. C-09 can pass without C-21; C-21 requires C-09 to be structured as a prerequisite gate. |
| C-22 | **Competitive strength inventory in persona phase** | depth | For each persona, output includes a per-persona competitive strength inventory structured as three named fields: (a) the Dimension on which the current solution wins, (b) the structural Advantage that win represents, and (c) the Durability basis explaining why that advantage is structurally persistent rather than merely habitual. This inventory is completed in the persona identification phase, before kill-barrier analysis begins. A competitive framing constructed on demand at kill-barrier analysis time, without an upstream per-persona inventory, fails. An inventory present but missing any of the three fields earns PARTIAL. |
| C-23 | **Named intervention target as falsifiable anchor** | depth | Within the four-part kill barrier structure from C-15, Part (3) -- the intervention target -- must name a specific mechanism or lever point, not a general approach, precise enough to anchor the confirmation signal from C-16 as a falsifiable observable condition tied to that mechanism. A Part (3) that names a general approach ("improve onboarding") without specifying the lever point ("the moment a user completes their first cross-team workflow") fails. An intervention target present but expressed too generally to yield a falsifiable confirmation condition earns PARTIAL. |

---

## Notes

- A rubric pass requires all 5 essential criteria to pass individually.
- Aspirational criteria may receive PARTIAL (5 pts) for genuine attempts that fall short of the
  full pass condition.
- C-19 and C-20 codify structural enforcement patterns from R4: C-19 captures the Part A / Part B
  disqualifier mechanism; C-20 captures the binary YES/NO reselection gate.
- C-21 codifies the cascade dependency revealed in R5: C-09 is prerequisite infrastructure for
  C-17, not a parallel criterion. Placing methodology declaration after persona analysis breaks
  the C-17 trace chain -- models produce derivation sentences with no threshold to cite.
- C-22 codifies the upstream inventory pattern from R5: embedding the Dimension/Advantage/Durability
  table in the persona identification phase closes C-11 by reference rather than requiring
  competitive framing to be constructed at kill-barrier time under analytical pressure.
- C-23 codifies the intervention target specificity requirement from R5: C-15 Part (3) at approach
  granularity is insufficient to anchor C-16's confirmation signal as a falsifiable condition.
  The named mechanism is the structural bridge between the causal chain (C-15) and the
  confirmation requirement (C-16).
```
