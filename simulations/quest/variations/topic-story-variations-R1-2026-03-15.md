---

## Variations — topic-story (Round 1, Rubric v1)

Five complete variations. Three single-axis, two combinations.

---

### V-01 — Lifecycle emphasis: pre-write synthesis worksheet

**Axis**: Lifecycle emphasis
**Hypothesis**: C-04 fails when extraction and synthesis happen simultaneously while reading. A mandatory written worksheet — with a Q3 that explicitly requires naming what two or more signals show together that no single signal shows alone — forces the cross-signal reasoning to complete as a discrete deliverable before any narrative prose begins. The worksheet is a prerequisite gate, not a scratchpad.

**Mechanism**: Stage 1 produces a 4-question worksheet (original question → key findings → cross-signal pattern → recommendation preview). Stage 2 may not begin until all four answers are complete and satisfying. The Q3 answer becomes the seed of Beat 3.

---

### V-02 — Role sequence: anti-summary prohibition with precise contrast

**Axis**: Role sequence (prohibition placement)
**Hypothesis**: "Synthesize" is ambiguous enough to admit sequential summarization as a valid interpretation. Placing a precise contrast — *synthesis answers "what do these say together?", summary answers "what did each one say?"* — as the opening content (before any task description) creates primacy anchoring that primes against the model's default behavior. Precision matters: a general "don't enumerate" instruction leaves the escape route open; a definition that makes the failure mode recognizable closes it.

**Mechanism**: The prohibition is the first two paragraphs. The task description follows. The model must hold the synthesis/summary distinction through the entire prompt.

---

### V-03 — Phrasing register: decision memo to a named stakeholder

**Axis**: Phrasing register
**Hypothesis**: A memo structure addressed to a decision-maker imposes forward pressure that a story structure does not: the BLUF opens with the recommendation, so the evidence sections must justify a conclusion that is already stated. This creates automatic proportionality checking (C-07) — an inconsistent Bottom Line and Pattern section are visibly contradictory. Risk: the model writes the Bottom Line first and then builds backward uncritically, producing a C-03 pass but a C-04 failure.

**Mechanism**: BLUF → What We Set Out to Understand → What the Signals Showed → The Pattern → What We Don't Know Yet. Bottom Line must be consistent with The Pattern; the prompt names this explicitly.

---

### V-04 — Combination: pre-write worksheet (V-01) + anti-summary prohibition (V-02)

**Axis**: Combination — analytical gate + framing gate
**Hypothesis**: V-01 closes the analytical gap (pattern not identified before writing); V-02 closes the compositional gap (model respects the prohibition but still produces thin Beat 3 because pattern was identified too loosely). These are orthogonal interventions at different points in the generation: V-01 before the artifact opens, V-02 at the moment composition begins. Together they enforce both the identification step and the composition step. Also includes the explicit labeled scaffold to enforce C-02.

---

### V-05 — Combination: decision memo (V-03) + anti-summary prohibition (V-02)

**Axis**: Combination — register + framing gate
**Hypothesis**: V-03's BLUF structure produces strong C-03/C-07 coverage but risks a Bottom Line written before the cross-signal pattern is found. The anti-summary prohibition, placed at the very top, primes the model to find the pattern before committing to the Bottom Line. The combination tests whether leading with the synthesis prohibition and then using memo format to enforce recommendation grounding produces better joint C-04 + C-07 coverage than either alone. Falsifiability test embedded inside The Pattern section.

---

Written to `simulations/quest/golden/topic-story-variate-R1-2026-03-15.md`.

**Key design choices for this round:**
- V-01 targets C-04 via analytical gate (worksheet must name a cross-signal pattern before prose begins)
- V-02 targets C-01 via primacy + precision (synthesis/summary contrast as the opening content)
- V-03 targets C-03 + C-07 via structural pressure (BLUF forces recommendation consistency)
- V-04 is the strongest C-04 candidate (worksheet gates the pattern, prohibition gates the prose)
- V-05 is the strongest C-03/C-07 candidate (memo structure + pattern-first discipline)
