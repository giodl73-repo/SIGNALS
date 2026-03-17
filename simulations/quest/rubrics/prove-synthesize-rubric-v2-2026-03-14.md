Written to `simulations/quest/rubrics/prove-synthesize-rubric-v2-2026-03-14.md`.

---

**What changed from v1:**

Two new aspirational criteria, aspirational weight rebalanced from 5 pts each to 2.5 pts each (total unchanged at 10).

**C-11 — Anti-pattern gates named explicitly** (`behavior`)
Derived from V-05's "This is a ranked argument, not a ranked list." The insight is that a gate naming what *not* to do forecloses failure modes that pass presence checks. V-01 through V-04 all asked for WHY — none of them named the table-as-annotated-list failure mode. V-05 named it, and it stopped.

**C-12 — Argumentative sections are prose** (`depth`)
Derived from the structural difference between V-01 (ADVOCATE table) and V-02..V-05 (prose per rank). Tables are enumerative by nature — you satisfy them by filling cells. Prose requires constructing a sentence that connects one rank to the next. This is a mechanism, not a style preference.

**C-10 updated**: Added "The standalone mandate is stated explicitly in the opening, not assumed to emerge from structure" — closes the gap that caused V-01..V-04 to fail C-10 despite being structurally complete.

**Round 1 re-scored under v2**: V-05 would still score 100. V-01 would drop further (fails C-09, C-11, C-12). The rubric now has more discriminating power in the aspirational tier.
rose is an enforcement mechanism for argumentative sections -- tables allow summarization by filling cells and cannot be closed off by a presence check alone.

---

## Essential Criteria (weight: 60 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Answer-first** | format | The synthesis opens with a direct answer to the hypothesis before any evidence or reasoning. The answer is a complete declarative sentence, not a hedge or a restatement of the question. |
| C-02 | **Confidence score present and calibrated** | correctness | A numeric confidence score (0-100) is stated. It is calibrated: high confidence (>=75) only when evidence strongly converges; low confidence (<=40) when evidence is mixed or thin. |
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
| C-09 | **Evidence hierarchy is argued** | depth | The output explains *why* the top signals outweighed the others -- not just what they are. A comparative question is present for each rank: "why this signal over the one below it?" A ranked argument is present, not a ranked list. |
| C-10 | **Synthesis is self-contained** | behavior | A reader with no access to the underlying investigation signals can understand the answer, the reasoning, and what to do next from the synthesis alone. No unexplained references to prior artifacts. The standalone mandate is stated explicitly in the opening, not assumed to emerge from structure. |
| C-11 | **Anti-pattern gates named explicitly** | behavior | At least one gate or checklist item names the failure mode by name rather than only naming the success condition. Example: "This is a ranked argument, not a ranked list" is stronger than "Evidence hierarchy is argued." A gate that names what *not* to do forecloses compliant-but-wrong outputs that pass presence checks. |
| C-12 | **Argumentative sections are prose** | depth | Evidence ranking, synthesis judgment, and confidence rationale are written as prose paragraphs, not tables or bullet lists. Tables are permitted only for enumerative sections (e.g., open questions list, principles list). Prose is a structural enforcement mechanism: it requires argument construction and cannot be satisfied by filling cells. |

---

## Scoring Reference

| Result | Condition |
|--------|-----------|
| Golden | All C-01 through C-05 pass AND composite >= 80 |
| Passing | All essential pass, composite < 80 |
| Failing | Any essential criterion fails |

### Score weights

- Essential: 60 points total (5 criteria, 12 points each)
- Recommended: 30 points total (3 criteria, 10 points each)
- Aspirational: 10 points total (4 criteria, 2.5 points each)

### Example score calculation

- Essential: 4/5 pass -> 4/5 * 60 = 48
- Recommended: 2/3 pass -> 2/3 * 30 = 20
- Aspirational: 2/4 pass -> 2/4 * 10 = 5
- **Composite = 73** -- fails golden (essential incomplete), failing overall

### Round 1 calibration

All 5 Round 1 variations were Golden (90-100). Differentiation was entirely in the aspirational tier:

| Score | Variations | Pattern |
|-------|-----------|---------|
| 100 | V-05 | Standalone mandate in opening sentence + explicit "ranked argument, not ranked list" distinction |
| 95 | V-02, V-03, V-04 | Argued hierarchy (C-09 pass) but standalone not explicitly mandated (C-10 fail) |
| 90 | V-01 | Table-based hierarchy (C-09 fail) + no standalone mandate (C-10 fail) |

C-11 and C-12 are derived from V-05's winning mechanisms. C-11 targets the gate design that named the anti-pattern. C-12 targets the structural choice that made summarization harder.
