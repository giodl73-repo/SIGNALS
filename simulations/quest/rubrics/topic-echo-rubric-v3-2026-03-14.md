Here is the complete updated rubric:

---

# topic-echo rubric — v3

---

**Two new aspirational criteria added:**

| ID | Name | Origin | Mechanism |
|----|------|--------|-----------|
| C-13 | Schema field completeness | R3, V-04 C-10/C-11/C-12 mechanism | Every schema field populated for every surprise -- no missing fields, no N/A |
| C-14 | Surprise portability | R3, V-05 convergence (first 100/100) | Each surprise stands alone as a self-contained institutional claim for any reader |

**Scoring table updated**: Aspirational N goes from 5 -> 7. Aspirational budget stays at 10 pts. C-10, C-11, C-12 (proven by two rounds) earn 2 pts each; C-08, C-09, C-13, C-14 earn 1 pt each.

**Key design decision**: C-13 is aspirational (not recommended) because schema completeness depends on the active variation -- some echoes use extended schemas, some minimal schemas, and neither is wrong. The criterion rewards completeness-within-chosen-schema, not a specific schema shape. C-14 is aspirational because surprise portability only emerges when all four quality mechanisms converge (C-08+C-10+C-11+C-12) -- the R3 finding is that single-axis optimization reliably fails to reach it.

**v3 additions**: Round 3 scoring revealed two structural patterns that consistently differentiated 100/100 from 94-99. These are now codified as C-13 and C-14. See "Round 3 Excellence Signals" section below.

**v2 additions**: Round 1 scoring revealed three mechanisms that consistently differentiated 100/100 outputs from 85/100 outputs. These are codified as C-10, C-11, and C-12. See "Round 1 Excellence Signals" section below.

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
- **Weight**: aspirational (1 pt)
- **Category**: behavior
- **Text**: The echo reads as useful institutional memory -- a document the next team could read before starting this path to avoid repeating the same surprises. Each surprise includes enough context for a newcomer to understand why it matters.
- **Pass condition**: A reader with no prior project context can understand each surprise without reading the source signals. Jargon is explained or avoided. The document stands alone.

---

### C-09 -- Pattern identification
- **Weight**: aspirational (1 pt)
- **Category**: depth
- **Text**: The echo identifies whether any surprises form a pattern -- a systemic issue, a recurring theme, or a structural signal about the problem space that transcends individual findings.
- **Pass condition**: Output includes at least one explicit pattern observation linking two or more surprises (e.g., "Three separate surprises all point to the same root: teams underestimate coordination cost"). Single-surprise patterns do not qualify.

---

### C-10 -- Counterfactual discipline
- **Weight**: aspirational (2 pts)
- **Category**: depth
- **Text**: Each surprise explicitly passes a counterfactual test: it would not have emerged from a team operating without active signal-gathering. The echo makes visible why sensing was necessary -- not just what was found, but why passive observation would have missed it.
- **Pass condition**: At least two-thirds of surprises include a counterfactual framing (e.g., "A team that skipped scout would have assumed X and shipped Y", "This only surfaced because prove-interview probed Z directly"). The counterfactual reasoning is embedded in the surprise body -- not applied only at culling. Surprises that could have been discovered through normal planning or review FAIL this criterion.
- **Origin**: Round 1, V-04. The inertia filter was identified as the strongest C-04 enforcement mechanism across all five variations. R3 refinement: V-03 earned PARTIAL because its counterfactual gate operated at culling only and did not appear in the artifact body. V-04 earned PASS by embedding "Why passive observation missed this" as a mandatory schema field. Reader-visible counterfactual framing is the distinguishing mechanism.

---

### C-11 -- Length discipline
- **Weight**: aspirational (2 pts)
- **Category**: behavior
- **Text**: The echo respects a tight length constraint (~800 words total, ~120 words per surprise). Each surprise is stated once, sharply, without elaboration beyond what a newcomer needs. The document is readable end-to-end in under ten minutes.
- **Pass condition**: Total word count is at or below 800 words (excluding headers and scoring metadata). No surprise body exceeds 120 words. Institutional memory that requires study to absorb fails as memory.
- **Origin**: Round 1, V-03. The 800-word ceiling plus "Write it for a reader who wasn't on the team" produced the strongest C-08 performance across all variations. R3 refinement: V-01/V-02/V-03 earned PARTIAL because the 800-word ceiling alone is insufficient -- one verbose surprise absorbs the budget. V-04 added a 120-word per-item cap, closing the gap. Both constraints are now required for PASS.

---

### C-12 -- Authoritative voice
- **Weight**: aspirational (2 pts)
- **Category**: format
- **Text**: Each surprise is stated as a claim -- a finding the author stands behind. The echo does not hedge. No surprise is framed as a possibility, a suggestion, or a preliminary observation.
- **Pass condition**: Zero hedging language in surprise statements ("may suggest", "could potentially", "seems to indicate", "it is possible that"). Each surprise is asserted: "X is true", not "X might be true". The author takes epistemic responsibility for every item in the echo.
- **Origin**: Round 1, V-05. The "Echo Archaeologist" expert persona produced the highest ceiling on C-02 naming across all variations. Expert identity commits the author to a judgment, not a log. Authoritative voice is the output-level marker of that commitment.

---

### C-13 -- Schema field completeness
- **Weight**: aspirational (1 pt)
- **Category**: format
- **Text**: Every surprise has all schema fields populated. No field is absent, marked N/A, or replaced with free-form prose that bypasses the schema structure. The schema is identical across all surprises in the echo.
- **Pass condition**: A reader can scan the echo field-by-field across surprises and find every field populated for every surprise. Any surprise with a missing or N/A field FAILS this criterion. Schema completeness applies to whichever schema the echo adopts -- minimal or extended -- but that schema must be applied uniformly.
- **Origin**: Round 3, V-04. Every PASS on C-10, C-11, and C-12 in R3 relied on mandatory schema field completion with explicit "not N/A" enforcement. Variations without per-field completeness checks earned PARTIAL across all three aspirational dimensions. Schema completeness is both a structural quality (enables scanning and comparison) and an output quality signal (incomplete fields indicate synthesis was not carried to completion).

---

### C-14 -- Surprise portability
- **Weight**: aspirational (1 pt)
- **Category**: behavior
- **Text**: Each surprise functions as a portable institutional claim -- it can stand alone outside the echo in a new context (new-hire onboarding, design brief, postmortem) and fully inform a reader who has no background knowledge of the project.
- **Pass condition**: Any single surprise, extracted from the echo in isolation, would communicate the finding, why it was unexpected, and why it matters for design -- to a reader who has not seen the rest of the echo or the source signals. Surprises that depend on surrounding context, other surprises, or assumed project knowledge FAIL this criterion.
- **Origin**: Round 3, V-05 (first 100/100 in the series). The combination of C-08 (stranger accessibility) + C-10 (counterfactual grounding) + C-11 (bounded scope) + C-12 (authoritative claim) produces surprises that are self-contained institutional claims -- verifiable by domain experts and accessible to newcomers, without compromise between the two. Single-axis variations (V-01 through V-03) peaked at 94-95; V-04 (three axes) reached 99; V-05 (all four axes) reached 100. Surprise portability is the emergent quality that appears only when all four mechanisms converge.

---

## Round 3 Excellence Signals

> These signals from Round 3 scoring drove the v3 additions.

| Signal | Source | Mechanism | Promoted to |
|--------|--------|-----------|-------------|
| Mandatory schema field completion ("every cell populated -- not N/A") | R3, V-04 mechanisms for C-10/C-11/C-12 | All three aspirational PASS in V-04 relied on schema completeness enforcement; PARTIAL in V-01/V-02/V-03 traced to missing or optional fields | C-13 |
| Convergence effect: first 100/100 via all-mechanism combination | R3, V-05 (C-08+C-10+C-11+C-12 together) | Single-axis variations peaked at 95; three-axis at 99; four-axis at 100. Surprise portability only emerges when precision, brevity, accessibility, and counterfactual grounding are all present in every surprise | C-14 |

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

| ID   | Text (short)               | Weight        | Pts | Category    |
|------|----------------------------|---------------|-----|-------------|
| C-01 | Surprise focus             | essential     | 15  | correctness |
| C-02 | Surprise naming            | essential     | 15  | format      |
| C-03 | Signal traceability        | essential     | 15  | correctness |
| C-04 | Design impact assessment   | essential     | 15  | depth       |
| C-05 | Expectation contrast       | recommended   | 10  | depth       |
| C-06 | Cross-signal synthesis     | recommended   | 10  | coverage    |
| C-07 | Breadth of surprise origin | recommended   | 10  | coverage    |
| C-08 | Institutional memory       | aspirational  | 1   | behavior    |
| C-09 | Pattern identification     | aspirational  | 1   | depth       |
| C-10 | Counterfactual discipline  | aspirational  | 2   | depth       |
| C-11 | Length discipline          | aspirational  | 2   | behavior    |
| C-12 | Authoritative voice        | aspirational  | 2   | format      |
| C-13 | Schema field completeness  | aspirational  | 1   | format      |
| C-14 | Surprise portability       | aspirational  | 1   | behavior    |

**Essential N = 4 | Recommended N = 3 | Aspirational N = 7**

### Scoring weights

| Tier | Criteria | Pts each | Max |
|------|----------|----------|-----|
| Essential (4) | C-01 through C-04 | 15 | 60 |
| Recommended (3) | C-05 through C-07 | 10 | 30 |
| Aspirational -- proven (3) | C-10, C-11, C-12 | 2 | 6 |
| Aspirational -- standard (4) | C-08, C-09, C-13, C-14 | 1 | 4 |
| **Total** | | | **100** |

PARTIAL = half points. FAIL = 0 points.

A PARTIAL on any essential criterion fails the output regardless of composite score.

---

### Example scores

| Scenario | E pass | R pass | A pts | Composite | Golden? |
|----------|--------|--------|-------|-----------|---------|
| Perfect  | 4/4    | 3/3    | 10/10 | 100       | YES     |
| Strong   | 4/4    | 3/3    | 5/10  | 95        | YES     |
| Solid    | 4/4    | 2/3    | 3/10  | 83        | YES     |
| Weak     | 3/4    | 3/3    | 0/10  | 75        | NO (essential fail) |
| Minimal  | 4/4    | 1/3    | 0/10  | 70        | NO (composite < 80) |

---

**What changed from v2:**

The two new criteria and the rationale behind each:

**C-13 (Schema field completeness)** comes from a structural observation in R3: V-04's PASS on C-10, C-11, and C-12 all shared the same enforcement mechanism — "every cell populated, not N/A." Variations that lacked this had the counterfactual at culling only (V-03 C-10 PARTIAL), had a total ceiling but no per-item cap (V-01/02/03 C-11 PARTIAL), or had no schema-field-level claim framing (V-01/02/03 C-12 FAIL). Schema completeness is the structural substrate that makes the other aspirational criteria achievable. It isn't folded into C-03/C-04/C-05 because those criteria each require one specific field; C-13 requires that ALL fields are populated, uniformly, across ALL surprises.

**C-14 (Surprise portability)** comes from the R3 convergence finding: V-05 (100/100) was the first variation to achieve full portability by combining all four mechanisms. The gap between V-04 (99) and V-05 (100) is precisely C-08 — adding newcomer framing throughout execution. C-14 captures the emergent output quality produced by that convergence, which neither C-08 alone nor C-12 alone nor the other mechanisms describe. A portable surprise is simultaneously bounded (C-11), non-hedging (C-12), counterfactually grounded (C-10), and stranger-accessible (C-08). When all four are present, the surprise doesn't need its context to be useful.

**Scoring redistribution**: The aspirational budget stays at 10 pts. C-10/C-11/C-12 retain 2 pts each (validated across two scoring rounds). The four standard aspirational criteria (C-08, C-09, C-13, C-14) each get 1 pt, totaling 4 pts. Total = 60 + 30 + 6 + 4 = 100.
