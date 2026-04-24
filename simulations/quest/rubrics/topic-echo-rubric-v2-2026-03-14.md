Written to `simulations/quest/rubrics/topic-echo-rubric-v2-2026-03-14.md`.

---

**Three new aspirational criteria added:**

| ID | Name | Origin | Mechanism |
|----|------|--------|-----------|
| C-10 | Counterfactual discipline | V-04, "strongest C-04 mechanism" | Each surprise states why passive observation would have missed it |
| C-11 | Length discipline | V-03, 800-word ceiling + C-08 PASS | Short form forces synthesis over transcription; readable in <10 min |
| C-12 | Authoritative voice | V-05, Echo Archaeologist ceiling on C-02 | Zero hedging — claims not possibilities; author takes epistemic responsibility |

**Scoring table updated**: Aspirational N goes from 2 → 5. Weights adjusted accordingly (each aspirational criterion is now 2 pts to keep total at 100).

**Key design decision**: C-10 is aspirational (not recommended) because it requires the author to have done enough signal synthesis to compare active vs. passive discovery — that's a high bar only the best echoes will clear. C-11 and C-12 are aspirational for the same reason: they're discipline markers, not structural requirements.
h the output from "correct echo" to "rich echo." The aspirational criteria target the document's long-term value as institutional memory — the explicit purpose stated in the skill description.

**v2 additions**: Round 1 scoring revealed three mechanisms that consistently differentiated 100/100 outputs from 85/100 outputs. These are now codified as C-10, C-11, and C-12. See "Round 1 Excellence Signals" section below.

---

## Essential Criteria

> All must pass for the output to be considered a valid echo.

### C-01 -- Surprise focus
- **Weight**: essential
- **Category**: correctness
- **Text**: Every item in the echo is a genuine surprise -- something the team did not expect before gathering signals. Items that confirm prior assumptions, restate known requirements, or summarize what was planned do not belong in an echo.
- **Pass condition**: No item could appear unchanged in a standard research summary, findings doc, or project brief. If even one item is an expected finding dressed as a surprise, FAIL.

---

### C-02 -- Surprise naming
- **Weight**: essential
- **Category**: format
- **Text**: Each surprise has a named label that captures the essence of the unexpected finding -- not a generic header.
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

### C-10 -- Counterfactual discipline
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each surprise explicitly passes a counterfactual test: it would not have emerged from a team operating without active signal-gathering. The echo makes visible why sensing was necessary -- not just what was found, but why passive observation would have missed it.
- **Pass condition**: At least two-thirds of surprises include a counterfactual framing (e.g., "A team that skipped scout would have assumed X and shipped Y", "This only surfaced because prove-interview probed Z directly"). Surprises that could have been discovered through normal planning or review FAIL this criterion.
- **Origin**: Round 1, V-04. The inertia filter ("would a team doing nothing have discovered this?") was identified as the strongest C-04 enforcement mechanism across all five variations. Promoted to aspirational because it is the sharpest form of the "so what" test and raises the institutional value of every surprise in the echo.

---

### C-11 -- Length discipline
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The echo respects a tight length constraint (~800 words). Each surprise is stated once, sharply, without elaboration beyond what a newcomer needs. The document is readable end-to-end in under ten minutes.
- **Pass condition**: Total word count is at or below 800 words (excluding headers and scoring metadata). No surprise requires more than three sentences to state fully. Institutional memory that requires study to absorb fails as memory.
- **Origin**: Round 1, V-03. The combination of an explicit 800-word ceiling and the directive "Write it for a reader who wasn't on the team" produced the strongest C-08 performance across all variations. Short form forces the author to have actually synthesized the surprise rather than transcribed it.

---

### C-12 -- Authoritative voice
- **Weight**: aspirational
- **Category**: format
- **Text**: Each surprise is stated as a claim -- a finding the author stands behind. The echo does not hedge. No surprise is framed as a possibility, a suggestion, or a preliminary observation.
- **Pass condition**: Zero hedging language in surprise statements ("may suggest", "could potentially", "seems to indicate", "it is possible that"). Each surprise is asserted: "X is true", not "X might be true". The author takes epistemic responsibility for every item in the echo.
- **Origin**: Round 1, V-05. The "Echo Archaeologist" expert persona produced the highest ceiling on C-02 naming across all variations. The mechanism: expert identity commits the author to a judgment, not a log. A named expert states findings; a passive recorder lists observations. Authoritative voice is the output-level marker of that commitment.

---

## Round 1 Excellence Signals

> These signals from Round 1 scoring drove the v2 additions.

| Signal | Source | Mechanism | Promoted to |
|--------|--------|-----------|-------------|
| Counterfactual filter ("would passive observation have revealed this?") | V-04 C-04 | Strongest C-04 enforcement across all variations | C-10 |
| 800-word limit + "readable in under ten minutes" | V-03 C-08 | Only variation to earn full C-08 PASS; short form forces real synthesis | C-11 |
| Echo Archaeologist persona: "highest ceiling on C-02" | V-05 C-02 | Expert identity commits author to claims, not observations | C-12 |

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
| C-10 | Counterfactual discipline  | aspirational  | depth       |
| C-11 | Length discipline          | aspirational  | behavior    |
| C-12 | Authoritative voice        | aspirational  | format      |

**Essential N = 4 | Recommended N = 3 | Aspirational N = 5**

### Scoring weights

| Tier | Per criterion | Max |
|------|--------------|-----|
| Essential (4) | 15 pts each | 60 |
| Recommended (3) | 10 pts each | 30 |
| Aspirational (5) | 2 pts each | 10 |
| **Total** | | **100** |

PARTIAL = half points. FAIL = 0 points.

A PARTIAL on any essential criterion fails the output regardless of composite score.

---

### Example scores

| Scenario | E pass | R pass | A pass | Composite | Golden? |
|----------|--------|--------|--------|-----------|---------|
| Perfect  | 4/4    | 3/3    | 5/5    | 100       | YES     |
| Solid    | 4/4    | 2/3    | 2/5    | 84        | YES     |
| Weak     | 3/4    | 3/3    | 0/5    | 75        | NO (essential fail) |
| Minimal  | 4/4    | 1/3    | 0/5    | 70        | NO (composite < 80) |
