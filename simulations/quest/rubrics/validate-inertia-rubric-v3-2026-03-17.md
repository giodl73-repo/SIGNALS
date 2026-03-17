v3 is written. Here's what changed:

**Three new aspirational criteria extracted from Round 2:**

| ID | Source | Pattern |
|----|--------|---------|
| C-13 | V-02 | Pre-persona inertia landscape classification (Structural/Behavioral/Mixed). V-02's Phase 2 ran this before any persona analysis, making inertia type gate the analysis rather than be derived from it -- propagating specificity downstream into C-09. |
| C-14 | V-02 | Type-conditioned mitigation. V-02's "if structural: name the product change / if behavioral: name the launch sequence" is a stronger C-09 guarantee than anti-patterns lists -- it constrains the answer space before writing. |
| C-15 | V-02 | Lost TAM implication as a non-conditional required statement. V-01/V-03/V-04 all got PARTIAL on C-10 despite using structural/behavioral vocabulary, because the section was gated on "if evidence supports it". V-02's unconditional "Lost TAM implication: {one sentence}" locked in the framing. |

**Point redistribution:** C-09=2, C-10=2, C-11=1, C-12=1, C-13=2, C-14=1, C-15=1 = 10 pts total unchanged.

**Added reviewer note** on C-13/C-14 complementarity: you can pass C-13 without C-14 (classifies early but collapses to unconditional mitigation), but C-14 without C-13 is structurally unusual.
rrier", "adoption stopper", "the one thing that would prevent adoption"). Must be specific to this feature, not a generic observation. |
| C-04 | **Workaround satisfaction assessed** | correctness | essential | Output evaluates how well the current workaround already solves the problem for at least one persona -- including what the workaround is and why it feels "good enough" to that persona. |
| C-05 | **Per-persona inertia score present** | format | essential | Each analyzed persona receives a discrete inertia score on a consistent scale (e.g., 1-5, Low/Medium/High/Critical, or 0-10). All scores must use the same scale and appear in the output. |

---

## Recommended Criteria (30 pts total)

*Each recommended criterion is worth 10 pts.*

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Habit lock-in addressed** | depth | recommended | Output goes beyond cost analysis to identify a behavioral or habitual pattern (muscle memory, workflow ritual, team convention) that would cause the persona to revert even after initial adoption. Must be persona-specific, not generic. |
| C-07 | **Social proof requirement mapped** | depth | recommended | Output identifies what social proof threshold a skeptical persona would need before adopting -- e.g., "needs to see 3 teammates use it first", "requires a public case study from a similar team", "won't move until their tech lead endorses it". |
| C-08 | **Learning curve quantified** | depth | recommended | At least one persona's learning curve is expressed in concrete terms: ramp time estimate, number of new concepts to internalize, or comparison to something the persona already knows ("similar to learning X, which took Y"). |

---

## Aspirational Criteria (10 pts total)

*Aspirational criteria reward structural sophistication. Partial credit is common; full pass is rare. Point weights redistributed in v3 to accommodate C-13, C-14, and C-15.*

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Overall risk rating with mitigation** | depth | aspirational | Output synthesizes per-persona scores into an overall adoption inertia risk level (Low/Medium/High/Critical) AND proposes at least one specific mitigation per barrier identified -- actionable enough to include in a launch plan. Mitigation must target the kill barrier named in C-03; restating the barrier as a recommendation does not pass. | 2 pts |
| C-10 | **Inertia asymmetry identified** | correctness | aspirational | Output distinguishes between personas for whom inertia is structural (will not adopt without product changes) vs. behavioral (can be overcome with onboarding/framing), and calls out which personas represent permanent lost TAM vs. delayed adoption. | 2 pts |
| C-11 | **Kill barrier hypothesized before persona analysis** | structure | aspirational | Kill barrier is stated as an explicit hypothesis in the first section of the output, before any per-persona analysis begins. The hypothesis must be feature-specific (not derived from persona aggregation). This structural sequencing prevents the kill barrier from being buried, genericized, or synthesized post-hoc. | 1 pt |
| C-12 | **Status-quo treated as competitor** | depth | aspirational | Output reasons about why at least one persona *chose* or *stays with* the incumbent/workaround -- not just what it is, but why they selected it. Uses framing such as "they adopted X because...", "X won this persona because...", or "the reason they haven't switched is..." that captures an adoption decision, not merely current state. | 1 pt |
| C-13 | **Inertia landscape classified before persona analysis** | structure | aspirational | A dedicated pre-persona phase classifies the overall inertia landscape as Structural, Behavioral, or Mixed before any individual persona is analyzed. The classification must state the type and its implication (e.g., "Structural: product changes required before any adoption is possible"). This forces inertia type to gate the analysis rather than be derived from it, and propagates specificity into C-09 mitigations. | 2 pts |
| C-14 | **Type-conditioned mitigation** | depth | aspirational | The C-09 mitigation is explicitly conditioned on inertia type: if the kill barrier is structural, the mitigation names a specific product change required; if the kill barrier is behavioral, the mitigation names a specific launch sequence or social proof intervention. Unconditional mitigations ("improve onboarding", "create a tutorial") do not pass even if they reference the kill barrier. | 1 pt |
| C-15 | **Lost TAM implication stated unconditionally** | correctness | aspirational | Output includes a non-conditional statement -- labeled "Lost TAM implication" or equivalent -- that explicitly names which personas (or persona type) represent permanent lost TAM until product changes, vs. which represent delayed adoption reachable with launch strategy. The statement must appear as a required synthesis line; sections gated on "if evidence supports it" or "if the analysis reveals" do not pass. | 1 pt |

---

## Scoring Reference

| Score Range | Interpretation |
|-------------|----------------|
| 100 | All criteria pass -- exemplary output |
| 80-99 | Golden threshold met -- output is useful and publishable |
| 60-79 | Essential pass but recommended gaps -- usable, needs improvement |
| < 60 | One or more essential criteria fail -- output is not useful |

---

## Reviewer Notes

- C-01 and C-03 are the two criteria most commonly failed by shallow outputs. If both fail, the output is a generic risk list, not an inertia analysis.
- C-02 passes if at least one cost is quantified; not all costs need numbers.
- C-05 fails if personas receive narrative assessments with no discrete score -- the score is the primary artifact.
- C-09 mitigation must target the kill barrier named in C-03; restating the barrier as a recommendation does not pass.
- C-10 is strictly aspirational: structural vs. behavioral inertia is a sophisticated distinction that requires domain knowledge about the persona's org context.
- C-11 is achievable only when the output is structured as a two-phase analysis (barrier hypothesis -> persona analysis). Single-phase outputs that derive the kill barrier at the end fail this criterion even if C-03 passes.
- C-12 is strengthened by competitor framing at the prompt level (e.g., "treat the current workaround as a competitor"). Outputs that merely describe what a persona uses without reasoning about the adoption decision do not pass.
- C-13 is achievable only when the output has a dedicated pre-persona phase (e.g., "Inertia Landscape" or "Phase 1: Classification") that names the type and its structural implication. Outputs that classify inertia type inline with persona analysis or in a closing synthesis fail this criterion.
- C-14 requires the mitigation to branch explicitly on inertia type. "If structural... / If behavioral..." is the target form. Anti-patterns lists and unconditional interventions do not pass.
- C-15 fails if the Lost TAM statement is conditional. The statement must appear regardless of what the analysis found -- its content varies, but its presence must not.
- C-13 and C-14 are complementary: C-13 places the classification before the personas; C-14 propagates that classification into the mitigation. An output can pass C-13 without passing C-14 (classifies early but collapses to unconditional mitigation), but passing C-14 without C-13 is structurally unusual.

---

## Version Notes

**v3 changes (2026-03-17):**
- Added C-13: Inertia landscape classified before persona analysis -- extracted from V-02 excellence signal (pre-persona Structural/Behavioral/Mixed classification phase transforms C-10 from post-hoc synthesis to deliberate analytical choice; inertia type structurally gates mitigation specificity)
- Added C-14: Type-conditioned mitigation -- extracted from V-02 excellence signal (if-structural/if-behavioral branching is a stronger C-09 guarantee than anti-patterns lists; constrains answer space before writing rather than naming failures after)
- Added C-15: Lost TAM implication stated unconditionally -- extracted from V-02 excellence signal (conditional asymmetry sections reliably produce PARTIAL on C-10 regardless of structural/behavioral vocabulary; non-conditional required statement locks in the framing)
- Redistributed aspirational point weights: C-09=2, C-10=2, C-11=1, C-12=1, C-13=2, C-14=1, C-15=1 (total aspirational tier unchanged at 10 pts)

**v2 changes (2026-03-17):**
- Added C-11: Kill barrier sequenced first -- extracted from V-05 excellence signal (Phase 1 hypothesis before persona analysis produced the strongest C-03 results across all variants)
- Added C-12: Status-quo as competitor -- extracted from V-03 excellence signal (competitor framing produced the strongest C-04 results across all variants, including "why they chose it" reasoning)
- Redistributed aspirational point weights: C-09=3, C-10=3, C-11=2, C-12=2 (total aspirational tier unchanged at 10 pts)
- Completed C-01 pass condition (was truncated in v1)
