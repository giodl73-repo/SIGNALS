Scorecard written to `simulations/quest/scorecards/prove-synthesize-scorecard-R1-2026-03-14.md`.

---

## Round 1 Results

**All 5 variations are Golden.** Every essential criterion passed across the board — this skill's rubric is well-calibrated: even the weakest variation (V-01) clears the golden threshold.

**The only differentiation is in the aspirational tier:**

| Variation | C-09 (argued hierarchy) | C-10 (self-contained) | Score |
|-----------|------------------------|----------------------|-------|
| V-05 | PASS | PASS | 100 |
| V-02/V-03/V-04 | PASS | FAIL | 95 |
| V-01 | FAIL | FAIL | 90 |

**Why V-01 loses C-09**: A table with a "Why" column is an annotated list. No mechanism asks "why did this outrank the one below it." The comparative question is absent from the structure.

**Why V-01..V-04 all lose C-10**: None of them explicitly mandate standalone readability. They assume self-containment emerges from structure. V-05 requires it by declaration in the opening sentence.

**V-05's winning mechanism**: "This is a ranked argument, not a ranked list." Three words that name the failure mode. The other variations ask for WHY but don't foreclose the table-with-WHY-annotations failure mode. V-05 also uniquely opens with the standalone mandate before any template structure.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["explicit standalone mandate in opening sentence locks C-10 where structural assumptions fail", "gates that name the anti-pattern prevent failure modes that pass presence checks", "ranked argument vs ranked list distinction must be named explicitly to enforce C-09", "prose over tables is a structural mechanism not a style choice -- tables allow summarization by filling cells"]}
```
th |
| V-04 | PASS | Strongest calibration: inertia rating gates confidence ceiling ("If STRONG, confidence >= 75 requires named evidence that directly overcomes current practice") |
| V-05 | PASS | "If >= 75: state which signals converge and why their convergence is meaningful. If <= 40: name the gap or conflict that prevents higher confidence." |

### C-03 -- Key evidence cited (traceable, explained by influence)

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | ADVOCATE table: Rank / Signal / "Why it influenced the verdict" / Weight columns. "Inventing signals not in SURVEYOR inventory is not acceptable" |
| V-02 | PASS | Prose per rank with "Why most influential: [Not what it found -- why it moved the needle more than others]" |
| V-03 | PASS | "For each: name the signal artifact. Then say WHY it moved the needle more than the others -- not what it found." Invented artifact check included |
| V-04 | PASS | Same prose-per-rank pattern with "Signals that directly address the inertia weakness are candidates for rank 1" -- adds traceability constraint |
| V-05 | PASS | PHASE 3 prose paragraphs + GATE 3 "All named signals exist in Phase 1 inventory (no invented signals)" |

### C-04 -- Counter-evidence present

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | SKEPTIC table required; explicit fallback row ("none found") for empty case |
| V-02 | PASS | "At least one argument against the verdict. If none exists, state that explicitly." |
| V-03 | PASS | Q4 "You must have an answer. If nothing argues against it: write 'No counter-evidence found.'" + "Do not skip this question." |
| V-04 | PASS | Dual-source requirement: inertia counter-argument always present + signal artifact table. Cannot skip both |
| V-05 | PASS | PHASE 4 required; GATE 4 "Counter-evidence section present (not skipped)"; empty-case handling in prose form |

### C-05 -- Synthesis supersedes signals (position, not summary)

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | COMMIT GATE "Answer is a judgment, not a restatement of the SURVEYOR inventory" -- checklist enforcement, moderate |
| V-02 | PASS | SEAL GATE "This is a judgment, not a signal summary" + provisional vs. final comparison mechanism forces a real position |
| V-03 | PASS | Strongest: "Do not hedge. Do not qualify. If you are uncertain, say so in the confidence score -- not in the answer." Anti-hedging at register level |
| V-04 | PASS | COMMIT GATE "This is a judgment call, not a signal summary" + inertia framing forces comparison to baseline |
| V-05 | PASS | GATE 2 "Verdict paragraph is a synthesis judgment (not a list of signal findings)" + prose requirement makes summarization structurally harder |

### C-06 -- Principles extracted (declarative, generalizable)

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | SCHOLAR table with "Restatements of the verdict are not principles" guard |
| V-02 | PASS | "Declarative generalizations only. Minimum 1." |
| V-03 | PASS | Q5 "It must be declarative: 'X implies Y' or 'When Z, expect W.' A restatement of your answer... is not a principle." |
| V-04 | PASS | "At minimum, one principle about the inertia relationship" -- domain scoping improves principle quality |
| V-05 | PASS | "At least one declarative principle... The principle must generalize beyond the specific topic." |

### C-07 -- Open questions identified (specific, actionable)

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | NAVIGATOR table with "Minimum 1 question. 'More research needed' is not an open question." |
| V-02 | PASS | "Minimum 1. Specific questions only." |
| V-03 | PASS | Q6 "Write the actual question, explain why it is still open, and name the concrete next step." |
| V-04 | PASS | "At minimum, one question about the inertia boundary condition" -- forces specificity through domain constraint |
| V-05 | PASS | Prose form with "which prove sub-skill would address it, or what external action is needed" as next-step anchor |

### C-08 -- Confidence is explained (rationale, not score alone)

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | COMMIT GATE requires "Confidence table has at least one UP and one DOWN driver" -- structured two-sided rationale |
| V-02 | PASS | "Confidence has explicit rationale (not just score)" as SEAL GATE item |
| V-03 | PASS | Q2 "explain it in two sentences: Sentence 1: What pushed the number up? Sentence 2: What held it down." Sentence-level structure |
| V-04 | PASS | "Confidence rationale: [2-3 sentences covering signal convergence and inertia interaction. Both required.]" |
| V-05 | PASS | "A confidence score without a rationale paragraph is a fail" -- explicit fail condition named inline |

### C-09 -- Evidence hierarchy is argued (ranked argument, not ranked list)

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | FAIL | ADVOCATE is a table with "Why it influenced the verdict" column -- captures WHY per row but a table is an annotated list, not a comparative ranked argument. No mechanism asks "why did this outrank the one below it" |
| V-02 | PASS | Prose per entry with "Why second: [What does it add that rank 1 did not establish?]" -- comparative question baked in |
| V-03 | PASS | "WHY it moved the needle more than the others" + "why second, not first" -- explicitly comparative |
| V-04 | PASS | Prose per entry with "Why rank 1 over others?" framing; inertia adds a comparison baseline |
| V-05 | PASS | "This is a ranked argument, not a ranked list." Explicit distinction + GATE 3 "Each paragraph argues the signal's rank (not just restates its finding)" |

### C-10 -- Synthesis is self-contained

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | FAIL | No standalone mandate. Tables carry column-header context but a reader without artifacts cannot reconstruct the reasoning chain |
| V-02 | FAIL | No standalone mandate. Provisional/final comparison still assumes artifact familiarity |
| V-03 | FAIL | No standalone mandate. Q&A framing helps orientation but does not require full self-explanation |
| V-04 | FAIL | ANCHOR section adds status-quo context (strongest among V-01..V-04) but no explicit standalone mandate |
| V-05 | PASS | Explicit opening mandate: "Produce a synthesis that stands alone. A reader with no access to the underlying signals must understand the answer, reasoning, and next steps from this document alone." Prose + phase gates enforce it structurally |

---

## Score Summary

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 | 12 | PASS | PASS | PASS | PASS | PASS |
| C-02 | 12 | PASS | PASS | PASS | PASS | PASS |
| C-03 | 12 | PASS | PASS | PASS | PASS | PASS |
| C-04 | 12 | PASS | PASS | PASS | PASS | PASS |
| C-05 | 12 | PASS | PASS | PASS | PASS | PASS |
| C-06 | 10 | PASS | PASS | PASS | PASS | PASS |
| C-07 | 10 | PASS | PASS | PASS | PASS | PASS |
| C-08 | 10 | PASS | PASS | PASS | PASS | PASS |
| C-09 | 5 | FAIL | PASS | PASS | PASS | PASS |
| C-10 | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| **Essential pts** | 60 | 60 | 60 | 60 | 60 | 60 |
| **Recommended pts** | 30 | 30 | 30 | 30 | 30 | 30 |
| **Aspirational pts** | 10 | 0 | 5 | 5 | 5 | 10 |
| **Composite** | 100 | **90** | **95** | **95** | **95** | **100** |
| **Result** | | Golden | Golden | Golden | Golden | **Golden** |

---

## Ranking

| Rank | Variation | Score | Differentiator |
|------|-----------|-------|----------------|
| 1 | **V-05** | 100 | Only variation with C-10 PASS; explicit standalone mandate + prose + phase gates |
| 2 (tie) | V-02 | 95 | Provisional/final comparison is strongest C-05 mechanism; prose evidence wins C-09 |
| 2 (tie) | V-03 | 95 | Strongest C-05 enforcement (anti-hedging at register level); cleanest imperative structure |
| 2 (tie) | V-04 | 95 | Strongest C-02 calibration (inertia gates ceiling); best C-04 (dual-source counter-evidence) |
| 5 | V-01 | 90 | Table format correct but loses C-09 (table = annotated list) and C-10 (no standalone mandate) |

Separation note: V-02, V-03, V-04 are tied at 95 -- each best-in-class on one criterion while failing only C-10. V-05 wins because it treats self-containment as a design requirement rather than a hoped-for outcome.

---

## Excellence Signals from V-05

**1. Explicit standalone mandate in the opening sentence**
V-05 opens with "Produce a synthesis that stands alone. A reader with no access to the underlying signals must understand the answer, reasoning, and next steps from this document alone." This is the mechanism that locks C-10. The other four variations assume self-containment emerges from structure; V-05 requires it by declaration before any content is written.

**2. Gates that name failure modes, not just presence checks**
V-05's gates verify what a section must not be, not only that it exists. GATE 2: "Verdict paragraph is a synthesis judgment (not a list of signal findings)." GATE 3: "Each paragraph argues the signal's rank (not just restates its finding)." Naming the anti-pattern inside the gate prevents the failure mode that would otherwise pass the presence check.

**3. "Ranked argument, not ranked list" as an explicit distinction**
Phase 3 states: "This is a ranked argument, not a ranked list." This three-word distinction is what separates C-09 pass from fail. The other variations ask for WHY but don't name the failure mode of a list that contains WHY annotations -- V-05 names it.

**4. Prose requirement as structural enforcement for C-05 and C-10**
"Write in prose. No tables." is not a style choice -- it is a mechanism. Tables allow summarization by filling cells. Prose requires the writer to construct sentences that connect findings, which forces synthesis. This indirectly enforces C-05 (synthesis supersedes signals) by making summarization structurally harder to produce.

---

## What R2 Should Test

V-05 achieves 100 in structural scoring, but the ceiling may be a scoring artifact. R2 should test whether V-05's gates prevent failures in practice:

- **C-05 adversarial**: conflict the input signal set so no clean YES/NO emerges -- does V-05 produce a judgment or a "signals are mixed" hedge?
- **C-10 depth**: does standalone readability hold when signal artifacts have domain-specific names the reader doesn't know?
- **V-03 + V-05 combo**: combine imperative register with phase gates -- does the combination outperform either alone on C-05 and C-10 simultaneously?
