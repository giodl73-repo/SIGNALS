Written to `simulations/quest/golden/mock-all-golden-2026-03-16.md`.

**Winning variation:** V-05 (100.0/100.0, rubric v21, denominator 33)

**What made it golden — 5 key patterns:**

1. **Architecturally separate declarations (C-39)** — Declaration A owns only REAL-REQUIRED identifier authority; Declaration B owns only per-stage firing. No cross-contamination. Earlier V-01/V-03 failed because each declaration mentioned both dimensions, making the labeling decorative.

2. **Pre-seeded example phrases per stage (C-40/C-41)** — Each stage body prints a domain-appropriate example before the model writes. Stage 1: HIGH-STRUCTURE ("trigger condition that determines when..."). Stage 2: EVIDENCE-HEAVY ("prototype result showing whether..."). Stage 3: MIXED ("open question about whether..."). Model copies, doesn't generate — eliminating the instruction-compliance risk that V-04 still carried.

3. **Ontological category error named explicitly (C-18/C-26)** — Not "don't produce artifacts yet" but "producing artifacts while you are the CLASSIFIER means you have ceased to be the CLASSIFIER... that is a category error." Role isolation enforced at identity level.

4. **Verbatim seed list with explicit paraphrase prohibition (C-19/C-21/C-23)** — Nine phrases declared as authoritative before ROLE 1. STOP gate states: "A restatement, synonym, abbreviated form, or adaptation of a seed phrase is not the seed phrase."

5. **Template-authored REAL-REQUIRED block (C-22)** — Rationale text is pre-written in the prompt with "The template is the author; the GENERATOR copies." Canonical identifier reference, not location heuristic, enforced by Declaration A and every stage gate.
