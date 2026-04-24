Rubric written to `simulations/quest/rubrics/topic-echo-rubric-2026-03-14.md`.

---

**Design notes:**

The 4 essential criteria capture what makes `topic-echo` distinct from any other signal artifact:

- **C-01 (Surprise focus)** — guards against the most common failure: producing a summary masquerading as an echo. If every item could appear in a standard findings doc, it fails.
- **C-02 (Surprise naming)** — forces the author to crystallize each surprise into a memorable label. Generic headers ("Finding 1") indicate the author hasn't truly named the insight.
- **C-03 (Signal traceability)** — keeps the echo grounded. Untraceable surprises are just opinions dressed up as findings.
- **C-04 (Design impact)** — the "so what." An echo without consequence to the design direction is institutional trivia, not institutional memory.

The recommended criteria (contrast, cross-signal synthesis, breadth) push the output from "correct echo" to "rich echo." The aspirational criteria (standalone utility, pattern identification) target the document's long-term value as institutional memory — the explicit purpose stated in the skill description.
 -- a label that captures the essence of the unexpected finding, not a generic header.
- **Pass condition**: Each surprise has a named label (e.g., "The Inverted Adoption Curve", "The Missing Middle", not "Finding 1" or "Surprise A"). Names must be specific to the content. Generic labels FAIL.

---

### C-03 -- Signal traceability
- **Weight**: essential
- **Category**: correctness
- **Text**: Each surprise is traced to at least one source signal (namespace, skill, or artifact). The reader can locate where the surprise came from.
- **Pass condition**: Each surprise names its source (e.g., "from scout-feasibility", "surfaced by prove-interview"). Surprises with no traceable source FAIL this criterion.

---

### C-04 -- Design impact assessment
- **Weight**: essential
- **Category**: depth
- **Text**: Each surprise includes an explicit assessment of how it changes, challenges, or confirms the design direction. Impact must be stated -- not implied.
- **Pass condition**: Each surprise answers "so what for the design?" in at least one sentence. Surprises that describe the finding but omit design consequence FAIL.

---

## Recommended Criteria

> Output is better with these. Do not require for passing, but penalize absence.

### C-05 -- Expectation contrast
- **Weight**: recommended
- **Category**: depth
- **Text**: Each surprise articulates what was expected going in, making the contrast explicit. The gap between hypothesis and reality is visible.
- **Pass condition**: At least two-thirds of surprises include a stated prior expectation ("We assumed X, but found Y"). Surprises that only describe the finding without the expected baseline are weaker.

---

### C-06 -- Cross-signal synthesis
- **Weight**: recommended
- **Category**: coverage
- **Text**: At least one surprise is synthesized across multiple signals or namespaces -- not derived from a single artifact alone. The echo captures something that only became visible when signals were read together.
- **Pass condition**: At least one surprise cites two or more distinct sources and explains why the combination produced the unexpected finding.

---

### C-07 -- Breadth of surprise origin
- **Weight**: recommended
- **Category**: coverage
- **Text**: Surprises are drawn from at least three distinct namespaces or signal types. The echo is not dominated by a single source.
- **Pass condition**: Source signals span at least three namespaces (scout, draft, review, flow, trace, prove, listen, program, topic). If all surprises come from one namespace, FAIL.

---

## Aspirational Criteria

> Raise the bar once essential and recommended are stable.

### C-08 -- Institutional memory utility
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The echo reads as useful institutional memory -- a document the next team could read before starting this path to avoid repeating the same surprises. Each surprise includes enough context for a newcomer to understand why it matters.
- **Pass condition**: A reader with no prior project context can understand each surprise without reading the source signals. Jargon is explained or avoided. The document stands alone.

---

### C-09 -- Pattern identification
- **Weight**: aspirational
- **Category**: depth
- **Text**: The echo identifies whether any surprises form a pattern -- a systemic issue, a recurring theme, or a structural signal about the problem space that transcends individual findings.
- **Pass condition**: Output includes at least one explicit pattern observation linking two or more surprises (e.g., "Three separate surprises all point to the same root: teams underestimate coordination cost"). Single-surprise patterns do not qualify.

---

## Scoring Summary

| ID   | Text (short)               | Weight        | Category    |
|------|----------------------------|---------------|-------------|
| C-01 | Surprise focus             | essential     | correctness |
| C-02 | Surprise naming            | essential     | format      |
| C-03 | Signal traceability        | essential     | correctness |
| C-04 | Design impact assessment   | essential     | depth       |
| C-05 | Expectation contrast       | recommended   | depth       |
| C-06 | Cross-signal synthesis     | recommended   | coverage    |
| C-07 | Breadth of surprise origin | recommended   | coverage    |
| C-08 | Institutional memory       | aspirational  | behavior    |
| C-09 | Pattern identification     | aspirational  | depth       |

**Essential N = 4 | Recommended N = 3 | Aspirational N = 2**

### Example scores

| Scenario | E pass | R pass | A pass | Composite | Golden? |
|----------|--------|--------|--------|-----------|---------|
| Perfect  | 4/4    | 3/3    | 2/2    | 100       | YES     |
| Solid    | 4/4    | 2/3    | 1/2    | 85        | YES     |
| Weak     | 3/4    | 3/3    | 0/2    | 75        | NO (essential fail) |
| Minimal  | 4/4    | 1/3    | 0/2    | 70        | NO (composite < 80) |
