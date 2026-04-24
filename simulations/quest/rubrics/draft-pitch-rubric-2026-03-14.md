Rubric written to `simulations/quest/rubrics/draft-pitch-rubric-2026-03-14.md`.

**Summary of decisions:**

**4 essential criteria** (all must pass):
- C-01: All three versions present (exec, dev, maker)
- C-02: Each version has all four elements (hook, what, why, CTA)
- C-03: Exec version is outcome-first — if it opens with features, it fails
- C-04: Anti-positioning section exists — hard structural requirement

**3 recommended criteria:**
- C-05: Dev version shows concrete tool interaction, not business case rephrased
- C-06: Maker version passes the "non-technical reader" test
- C-07: Prior signals consulted — waived if none available

**2 aspirational criteria:**
- C-08: Proof points are traceable to named sources (not vague claims)
- C-09: Inertia named as primary competitor — the positioning insight, not just a product list

The key design choice: C-03 and C-04 are essential (not recommended) because a pitch that leads with features or omits anti-positioning is structurally broken — it fails before the quality questions even apply.
e-first with ROI framing** | correctness | The exec version leads with a business outcome (cost, risk, productivity) -- not a feature list, not a technology description. ROI or cost framing appears before any mention of how the tool works. |
| C-04 | **Anti-positioning section present** | coverage | Output contains an explicit "what we are NOT" section. It rules out at least one adjacent category (e.g., not a test runner, not a documentation generator). Absence of this section is a hard fail. |

---

## Recommended Criteria (30% weight)

Output is materially better with these. Not individually blocking.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Dev version shows the tool, not the business case** | depth | Developer version demonstrates concrete interaction -- a command, an artifact, a workflow step. It does not repeat the ROI framing from the exec version. A reader should be able to answer "what would I actually type?" after reading it. |
| C-06 | **Maker version is jargon-free** | depth | Maker version contains no unexplained acronyms, no namespace references, no internal terminology. A non-technical reader could understand it. The framing centers on "can I do this?" rather than "here is the architecture." |
| C-07 | **Prior signals consulted** | behavior | If scout-positioning or competitor signals are available, the pitch reflects their framing (e.g., primary competitor identified as inertia, not a named product). If no prior signals exist, this criterion is waived. |

---

## Aspirational Criteria (10% weight)

These raise the bar once essential and recommended are stable.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Proof points are specific and traceable** | depth | Claims include a source or basis (e.g., "730+ scenarios from techniques/01-09", "40% from Q01/Q02 research"). Vague claims ("many teams", "proven results") do not pass. At least two proof points must be traceable to a named source. |
| C-09 | **Competitive framing names inertia as primary competitor** | depth | The exec or strategy framing identifies "doing nothing" or "the meeting that never happened" as the real competition -- not just a named tool like Cursor or Copilot. This reflects the positioning insight from scout signals and elevates the pitch beyond surface comparison. |

---

## Composite Score Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: All 4 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | All essential + >= 80 | Ship it |
| Pass | All essential + 70-79 | Usable, recommended gaps noted |
| Conditional | All essential + < 70 | Needs recommended work before use |
| Fail | Any essential fails | Do not use -- structural gap |

---

## Scoring Notes

- C-01 and C-02 are evaluated structurally -- check for presence, not quality
- C-03 is evaluated by reading the first 3 sentences of the exec version; if they describe features, it fails
- C-04 fails if the section is absent; a weak anti-positioning still passes (quality handled by C-08/C-09)
- C-07 is waived if the run has no prior signals or no scout-positioning artifact exists
- C-09 is the highest-value aspirational criterion; it signals the skill has internalized the positioning insight, not just applied a template
