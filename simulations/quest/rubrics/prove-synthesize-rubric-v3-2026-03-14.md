Written to `simulations/quest/rubrics/prove-synthesize-rubric-v3-2026-03-14.md`.

---

**What changed from v2:**

Three new aspirational criteria (C-13, C-14, C-15), each 2.5 pts. Aspirational total rises 10 → 17.5 pts. Max composite rises 100 → 107.5. Golden threshold adjusted 80 → 85 (~79% of max, same intent).

---

**C-13 — NOT:-first gate ordering** (`behavior`)
Gates name the failure mode *before* the success condition. A writer who reads "NOT: verdict is a list of signal summaries" before the pass condition has been foreclosed before they can satisfy the check. Reverse-ordered gates allow satisfying the presence check before encountering the prohibition. Pattern: `NOT: [failure mode]` precedes the positive condition in each gate item.

**C-14 — Formal verdict register** (`behavior`)
A dedicated commitment word (RULING, VERDICT, DETERMINATION, FINDING) appears as a section label or sentence-level declaration. "RULING: the hypothesis is supported" cannot be followed by hedging in a way that "Based on the evidence..." can. This is what V-02's RULING/DISSENT/HOLDINGS and V-04's JUDGE/ADVOCATE/ADVERSARY/SCHOLAR structures bought — anti-hedging at the lexical level, independent of gate design.

**C-15 — Pre-committed counter-evidence** (`behavior`)
The adversarial challenge is issued structurally *before* the verdict section. Pre-commitment forces the determination to be made against the best opposing case already on the table. C-04 requires counter-evidence present; C-15 requires it structurally precede the verdict — a mechanism distinction, not a content one. NOT:-clause included: "counter-evidence section follows the verdict and is selected after the position is formed."

---

**Scoring update summary:**

| Tier | v2 | v3 |
|------|----|----|
| Essential | 60 pts / 5 criteria | 60 pts / 5 criteria |
| Recommended | 30 pts / 3 criteria | 30 pts / 3 criteria |
| Aspirational | 10 pts / 4 criteria | 17.5 pts / 7 criteria |
| Max composite | 100 | 107.5 |
| Golden threshold | >= 80 | >= 85 |
1/C-12 tension confirmed**: R2 confirmed that C-11 and C-12 are in structural tension when gates are removed. Continuous prose (maximum C-12 compliance) eliminates the gate structure required by C-11. Both criteria remain; the tension is a feature, not a defect -- it distinguishes designs that solve both from designs that maximize one at the cost of the other.

**Round 2 calibration**: All 5 R2 variations were Golden under v2 (97.5-100). R3 adversarial conditions (thin signal set, genuinely MAYBE hypothesis, inline gate language in prose) will determine whether v3 has sufficient discriminating power in the new criteria.

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

## Aspirational Criteria (weight: 17.5 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Evidence hierarchy is argued** | depth | The output explains *why* the top signals outweighed the others -- not just what they are. A comparative question is present for each rank: "why this signal over the one below it?" A ranked argument is present, not a ranked list. |
| C-10 | **Synthesis is self-contained** | behavior | A reader with no access to the underlying investigation signals can understand the answer, the reasoning, and what to do next from the synthesis alone. No unexplained references to prior artifacts. The standalone mandate is stated explicitly in the opening, not assumed to emerge from structure. |
| C-11 | **Anti-pattern gates named explicitly** | behavior | At least one gate or checklist item names the failure mode by name rather than only naming the success condition. Example: "This is a ranked argument, not a ranked list" is stronger than "Evidence hierarchy is argued." A gate that names what *not* to do forecloses compliant-but-wrong outputs that pass presence checks. |
| C-12 | **Argumentative sections are prose** | depth | Evidence ranking, synthesis judgment, and confidence rationale are written as prose paragraphs, not tables or bullet lists. Tables are permitted only for enumerative sections (e.g., open questions list, principles list). Prose is a structural enforcement mechanism: it requires argument construction and cannot be satisfied by filling cells. |
| C-13 | **NOT:-first gate ordering** | behavior | Gates that enforce anti-patterns list the failure mode *before* the success condition. NOT: "[failure mode]" precedes the positive pass condition in each gate item. A gate that names the failure mode after the pass condition allows the writer to satisfy the presence check before encountering the prohibition. NOT:-first ordering forecloses the failure mode before the pass condition is reached. |
| C-14 | **Formal verdict register** | behavior | The synthesis uses a dedicated lexical register for its judgment -- a term (RULING, VERDICT, DETERMINATION, FINDING, or equivalent) that signals commitment rather than summary. The register word appears as a section label or sentence-level declaration. Register-level commitment enforces anti-hedging independent of gate structure: a RULING cannot be followed by hedging language in a way that "Based on the evidence..." can. |
| C-15 | **Pre-committed counter-evidence** | behavior | The adversarial challenge (counter-evidence obligation) is issued structurally *before* the verdict section, not as a post-hoc reflection section after the determination. Pre-commitment forces the synthesis to issue its judgment against the best opposing case already on the table. NOT: counter-evidence section follows the verdict and is selected after the position is formed. C-04 requires counter-evidence present; C-15 requires it structurally precede the verdict. |

---

## Scoring Reference

| Result | Condition |
|--------|-----------|
| Golden | All C-01 through C-05 pass AND composite >= 85 |
| Passing | All essential pass, composite < 85 |
| Failing | Any essential criterion fails |

### Score weights

- Essential: 60 points total (5 criteria, 12 points each)
- Recommended: 30 points total (3 criteria, 10 points each)
- Aspirational: 17.5 points total (7 criteria, 2.5 points each)
- Max composite: 107.5

### Example score calculation

- Essential: 4/5 pass -> 4/5 * 60 = 48
- Recommended: 2/3 pass -> 2/3 * 30 = 20
- Aspirational: 3/7 pass -> 3/7 * 17.5 = 7.5
- **Composite = 75.5** -- fails golden (essential incomplete), failing overall

### Round 1 calibration (under v2 rubric)

All 5 Round 1 variations were Golden (90-100). Differentiation was entirely in the aspirational tier:

| Score | Variations | Pattern |
|-------|-----------|---------|
| 100 | V-05 | Standalone mandate in opening sentence + explicit "ranked argument, not ranked list" distinction |
| 95 | V-02, V-03, V-04 | Argued hierarchy (C-09 pass) but standalone not explicitly mandated (C-10 fail) |
| 90 | V-01 | Table-based hierarchy (C-09 fail) + no standalone mandate (C-10 fail) |

### Round 2 calibration (under v2 rubric)

All 5 Round 2 variations were Golden (97.5-100). Differentiation narrowed to C-11/C-12 structural tension:

| Score | Variation | Pattern |
|-------|-----------|---------|
| 100 | V-01, V-02, V-04, V-05 | R1 fixes baked in; C-11 and C-12 both satisfied |
| 97.5 | V-03 | Continuous prose design maximized C-12; eliminating gates made C-11 structurally impossible |

C-13, C-14, C-15 are derived from R2 winning mechanisms. C-13 targets gate ordering that names failure before success. C-14 targets lexical register that commits at the word level. C-15 targets structural pre-commitment of counter-evidence before verdict formation.
