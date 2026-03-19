v7 written. Here's what was extracted and why each is a new criterion rather than a pass-condition tightening:

---

**C-24 — Named boundary artifact at phase transition** (behavior)
C-21 requires Phase 1 to be framed as C-17 infrastructure. C-24 requires that framing to take the form of a *named, produced artifact* — a literal statement the model must write (e.g., "SCORING INFRASTRUCTURE DECLARED.") — not a downstream instruction. The artifact has an address Phase 4 can cite by exact name. Without it, C-17 traces produce paraphrase chains, and chain breaks (a trace that omits the threshold) are invisible because there is no named anchor whose absence signals the failure. V-26/V-29/V-30 passed C-21 and C-24; V-27/V-28 passed C-21 but earned PARTIAL on C-24 because their Phase 1 self-identification was an instruction, not an artifact.

**C-25 — Structural prohibition gate vs. format instruction** (behavior)
C-22 and C-23 require upstream completion before downstream phases. C-25 requires the advance condition to be a structural prohibition ("Do not proceed to Phase X until..."), not a format instruction ("include Y before Z"). Format instructions allow weak content inside a required slot to formally comply. Prohibitions require the model to skip a named gate to continue — making non-compliance structurally visible. The R6 differentiator: V-27/V-30 used prohibitions; V-26/V-28/V-29 used format instructions. Only the prohibition form mechanically prevented "familiarity" Durability from clearing the inventory gate.

**C-26 — Cross-phase citation chain with named anchors** (behavior)
C-17 requires Phase 4 to cite Phase 1. C-26 requires the entire output to form a traceable chain where every link names its upstream artifact: Phase 1 produces a named artifact → Phase 4 cites it by name → Phase 5 Part (3) produces a named lever point → AMEND (d) names that lever point as its observable anchor. A paraphrase chain (correct content, no named source) earns PARTIAL. A link that constructs its own content without a named upstream anchor fails. C-17 can pass without C-26; C-26 requires named anchors at every link.

**C-27 — Self-rejection gate for mechanism specificity** (behavior)
C-23 requires Part (3) to name a specific mechanism. C-27 requires a self-rejection test embedded between Part (3) and Part (4): completion sentence + rejection clause ("If you cannot complete this with a specific observable condition, replace Part (3)"). Approach-level framing cannot complete the falsifiability sentence, causing the model to self-reject before writing Part (4) — stronger than a rubric criterion that evaluates specificity after the fact. Completion sentence without the rejection clause earns PARTIAL.

**Scoring:** 270 pts max (was 230). 19 aspirational criteria (was 15).
pstream source. A chain
where any link draws from the correct upstream content but without naming it (paraphrase chain)
earns PARTIAL. A chain where any link constructs its own content without reference to a named
upstream artifact fails. C-17 can pass without C-26; C-26 requires the entire chain to use named
anchors at every link.

**C-27 — Self-rejection gate for mechanism specificity** (behavior)
C-23 requires Part (3) to name a specific mechanism. C-27 requires output to include a
self-rejection test between Part (3) and Part (4): a required completion sentence
("At T=[horizon], the absence of this lever would be observable as: ___") followed by a
literal rejection condition ("If you cannot complete this sentence with a specific observable
condition, replace Part (3)"). The self-rejection gate makes mechanism specificity self-evaluating
at write time rather than externally evaluated after the fact: the model rejects its own output if
Part (3) is at approach granularity, because approach-level framing cannot complete the
falsifiability sentence with a specific condition. This is stronger than a rubric criterion that
evaluates specificity post-hoc, because the rejection is embedded in the output structure, not
applied from outside. C-23 can pass without C-27; C-27 requires the falsifiability test to be a
self-rejecting gate embedded between Part (3) and Part (4). A completion sentence present without
the rejection clause earns PARTIAL.

**Scoring:** 270 pts max (was 230). 19 aspirational criteria (was 15).

---

## Criterion Summary

- **5 essential (C-01--C-05):** per-persona inertia mapping, quantified switching cost,
  per-persona inertia score, kill-barrier identification, overall adoption inertia risk
- **3 recommended (C-06--C-08):** current workaround satisfaction, habit lock-in + social proof
  coverage, mitigation path for the kill barrier
- **19 aspirational (C-09--C-27):** scoring methodology transparency, time-dependent inertia
  trajectory, status-quo competitor framing, named social proof threshold, mitigation tied to
  structural root cause, kill-barrier temporal persistence test, causal chain with labeled
  structural sub-parts, mitigation confirmation signal, per-score methodology trace,
  kill-barrier trajectory verdict, related-output structural segregation with disqualifier,
  kill-barrier reselection gate, phase-zero methodology gate, competitive strength inventory
  in persona phase, named intervention target as falsifiable anchor, named boundary artifact at
  phase transition, structural prohibition gate vs. format instruction, cross-phase citation chain
  with named anchors, self-rejection gate for mechanism specificity

Scoring: Essential = 10 pts each (50 total), Recommended = 10 pts each (30 total), Aspirational =
10 pts each (190 total) = **270 pts max**.

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
| C-24 | **Named boundary artifact at phase transition** | behavior | The scoring infrastructure declared in C-21 is expressed as a named, produced artifact -- a literal statement the model must write (e.g., "SCORING INFRASTRUCTURE DECLARED.") that appears as its own line at the Phase 1 boundary, not as a downstream instruction ("per-persona traces must reference these thresholds"). The artifact name is then cited by name in Phase 4 traces, creating a reference chain rather than a paraphrase chain. A Phase 1 declaration that identifies itself as infrastructure via instruction rather than via a named artifact earns PARTIAL. A Phase 4 trace that cites the correct Phase 1 content but does not name the artifact fails C-24 regardless of whether C-17 passes. C-21 can pass without C-24; C-24 requires C-21's infrastructure framing to be embodied as a named boundary artifact with a citable address. |
| C-25 | **Structural prohibition gate vs. format instruction** | behavior | Any phase boundary where upstream completion is required for downstream correctness (C-22's inventory before Phase 5, C-23's mechanism specification before Part (4)) must express the advance condition as a structural prohibition -- a literal "Do not proceed to Phase X until [condition]" -- not a format instruction ("include Y before Z"). Format instructions allow a model to produce weak content inside a required slot and formally comply; structural prohibitions require the model to skip a named gate to continue, making non-compliance structurally visible. A single prohibition gate on any required phase boundary satisfies C-25. A gate expressed only as a format instruction earns PARTIAL. |
| C-26 | **Cross-phase citation chain with named anchors** | behavior | The full output forms a traceable citation chain in which each downstream section explicitly names the upstream artifact it draws from: Phase 1 produces a named artifact (C-24) → Phase 4 cites that artifact by name (C-17) → Phase 5 Part (3) produces a named lever point (C-23) → the confirmation signal names that lever point as its observable anchor (C-16). Each link must name its upstream source. A chain where any link draws from correct upstream content but without naming it (paraphrase chain) earns PARTIAL. A chain where any link constructs its own content without reference to a named upstream artifact fails. C-17 can pass without C-26; C-26 requires every link in the chain to use named anchors. |
| C-27 | **Self-rejection gate for mechanism specificity** | behavior | Within the four-part kill barrier structure from C-15, output includes a self-rejection test between Part (3) and Part (4) consisting of: (a) a required completion sentence ("At T=[horizon], the absence of this lever would be observable as: ___") and (b) a literal rejection condition ("If you cannot complete this sentence with a specific observable condition, replace Part (3)"). The completion sentence forces self-evaluation at mechanism-specification time: approach-level framing cannot complete it with a specific condition, causing the model to self-reject and revise Part (3) before writing Part (4). A completion sentence present without the rejection clause earns PARTIAL. A Part (3) followed directly by Part (4) with no self-rejection test fails. C-23 can pass without C-27; C-27 requires the falsifiability test to be a self-rejecting gate embedded in the output structure. |

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
- C-24 codifies the named artifact pattern from R6: C-21 framing expressed as a downstream
  instruction creates a paraphrase chain; framing expressed as a named artifact creates a
  reference chain. The difference is detectability of chain breaks.
- C-25 codifies the prohibition gate pattern from R6: the R6 differentiator for C-22 was that
  V-27/V-30 used "Do not proceed" prohibitions while V-26/V-28/V-29 used format instructions.
  Only the prohibition form mechanically blocks "familiarity" Durability from passing the
  inventory check, because a format instruction cannot prevent a model from writing weak content
  inside a required slot.
- C-26 codifies the full chain traceability requirement from R6: V-30's named artifact anchor
  created a Phase 1 → Phase 4 → Phase 5 → AMEND chain where each link names its upstream
  source. The chain makes structural failures detectable at the link level rather than requiring
  holistic re-evaluation.
- C-27 codifies the self-rejection gate pattern from R6: requiring the model to complete a
  falsifiability sentence before writing Part (4) converts mechanism specificity from an external
  rubric judgment into a self-evaluating constraint embedded in the output structure. The
  rejection clause is what distinguishes a self-rejection gate from a completion prompt.
