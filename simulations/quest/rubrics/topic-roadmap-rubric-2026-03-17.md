Rubric written to `simulations/quest/rubrics/topic-roadmap-rubric-v1-2026-03-17.md`.

Here's what drove each decision:

**Essential (5 criteria — the non-negotiable floor):**
- **C-01 Inertia prior** — the skill's core design philosophy; a run that ignores it produces proposals with no evidential basis
- **C-02 Signal delta before proposals** — without the inventory + delta analysis, proposals have no causal chain
- **C-03 Concrete proposals** — vague "consider this" outputs are not useful for strategy revision
- **C-04 Confirmation gate** — the skill explicitly requires user confirmation before touching strategy.md; a skill that skips this is broken regardless of proposal quality
- **C-05 Only confirmed changes applied** — the confirmation gate is meaningless if unchecked proposals land anyway

**Recommended (3 criteria — better with these):**
- **C-06 Delta-Finding traceability** — distinguishes evidence-driven from preference-driven change; the "Strategy assumed X / Signal revealed Y" format is the structural proof
- **C-07 Type-labeled nulls** — ambiguous null coverage across change types is a silent failure mode
- **C-08 Before/after diff** — makes the net effect of the revision reviewable at a glance

**Aspirational (2 criteria — raises the bar once stable):**
- **C-09 Defender Challenge Table** — adversarial self-challenge with calibration; prevents rubber-stamp acceptance of all proposals
- **C-10 Conflict audit** — catches contradicting signals that would produce incoherent proposals if left unresolved
