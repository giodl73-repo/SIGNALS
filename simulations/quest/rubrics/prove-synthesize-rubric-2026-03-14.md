Rubric written to `simulations/quest/rubrics/prove-synthesize-rubric-2026-03-14.md`.

**10 criteria across 3 tiers:**

**Essential (C-01..C-05)** — the synthesis must be answer-first, carry a calibrated confidence score, cite traceable key evidence, include counter-evidence, and take an actual position rather than summarizing signals.

**Recommended (C-06..C-08)** — generalized principles extracted, specific open questions named, and the confidence score explained (not just stated).

**Aspirational (C-09..C-10)** — the evidence ranking is argued (not just listed), and the synthesis stands alone without requiring access to the underlying artifacts.

The key design tension in this rubric is C-05 vs simple summarization: many LLM outputs will pass the format checks but fail to actually *synthesize* — they restate the signals without committing to a judgment. C-05 is the criterion that enforces that.
ted. It is calibrated: high confidence (>=75) only when evidence strongly converges; low confidence (<=40) when evidence is mixed or thin. |
| C-03 | **Key evidence cited** | coverage | Exactly or up to 3 signals are named as key evidence. Each named signal is traceable to an artifact produced during the investigation (not invented). Each signal is explained in terms of *why* it influenced the answer. |
| C-04 | **Counter-evidence present** | correctness | At least one piece of evidence arguing *against* the answer is explicitly named. If none exists, the output states "no counter-evidence found" with a brief rationale. Omitting this section entirely is a fail. |
| C-05 | **Synthesis supersedes signals** | behavior | The synthesis takes a position -- it does not merely restate or list the investigation signals. The answer and confidence together constitute a judgment call, not a summary. |

---

## Recommended Criteria (weight: 30 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Principles extracted** | depth | At least one principle is stated -- something learned beyond this specific hypothesis that generalizes to future investigations. Principles are declarative ("X implies Y") not restatements of the finding. |
| C-07 | **Open questions identified** | coverage | At least one question the investigation did not resolve is named. Questions are specific and actionable, not generic ("more research needed"). |
| C-08 | **Confidence is explained** | depth | The confidence score is accompanied by a brief rationale (1-3 sentences) explaining what drove it up or down. Score alone without rationale is a partial pass (counts as fail for this criterion). |

---

## Aspirational Criteria (weight: 10 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Evidence hierarchy is argued** | depth | The output explains *why* the top 3 signals outweighed the others -- not just what they are. A ranked argument is present, not just a list. |
| C-10 | **Synthesis is self-contained** | behavior | A reader with no access to the underlying investigation signals can understand the answer, the reasoning, and what to do next from the synthesis alone. No unexplained references to prior artifacts. |

---

## Scoring Reference

| Result | Condition |
|--------|-----------|
| Golden | All C-01 through C-05 pass AND composite >= 80 |
| Passing | All essential pass, composite < 80 |
| Failing | Any essential criterion fails |

### Example score calculation

- Essential: 4/5 pass -> 4/5 * 60 = 48
- Recommended: 2/3 pass -> 2/3 * 30 = 20
- Aspirational: 1/2 pass -> 1/2 * 10 = 5
- **Composite = 73** -- fails golden (essential incomplete), failing overall
