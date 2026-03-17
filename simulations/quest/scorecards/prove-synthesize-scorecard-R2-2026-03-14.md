## Round 2 Scoring — prove-synthesize

**Scorecard written to `simulations/quest/scorecards/prove-synthesize-scorecard-R2-2026-03-14.md`**

---

### Results

| Rank | Variation | Score | Result |
|------|-----------|-------|--------|
| 1 (tie) | V-01 | 100 | Golden |
| 1 (tie) | V-02 | 100 | Golden |
| 1 (tie) | V-04 | 100 | Golden |
| 1 (tie) | V-05 | 100 | Golden |
| 5 | V-03 | 97.5 | Golden |

All essential pass: **true**. All five variations are Golden.

---

### Key Finding: V-03's C-11 Trade-off

V-03 is the only variation that fails a criterion — and it's the most instructive failure in R2. The design axis was "continuous prose, no gates, no checklists." This produced the **strongest C-12** of any variation ("There are no tables permitted. The synthesis is prose from start to finish"). But eliminating gates eliminated the only structural mechanism available for C-11 (`"gate or checklist item"`). Inline anti-pattern phrases like "This is a ranked argument, not a ranked list" exist in V-03's prose — but they aren't gate items. C-11 requires one. **C-11 and C-12 are in structural tension when gates are removed.**

---

### New Patterns

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": [
  "NOT:-first gate format: listing failure modes before positive checks forecloses non-compliant outputs before the writer reaches the success condition",
  "formal verdict register (RULING/DISSENT/HOLDINGS) achieves anti-hedging at the lexical level, independent of gate structure",
  "continuous prose eliminates gates and creates a C-11/C-12 structural trade-off: maximum C-12 compliance costs C-11 compliance",
  "pre-verdict ADVERSARY role makes counter-evidence a pre-committed structural requirement rather than a post-hoc reflection section"
]}
```

---

### R2 Summary vs R1

| Round | Top score | Differentiator |
|-------|-----------|---------------|
| R1 | 100 (V-05 only) | C-10 standalone mandate + "ranked argument, not ranked list" |
| R2 | 100 (4-way tie) | R1 fixes baked in; C-11/C-12 now discriminate — only V-03 drops |

The rubric is saturated at 100 for well-designed variations. **R3 should test mechanism quality in adversarial conditions** (thin signal set, genuinely MAYBE hypothesis, inline gate language in prose).
 any named signal is absent from the Phase 1 inventory" |
| V-02 | PASS | Prose per rank in EVIDENCE BASIS; Seal "All named signals exist in PRELIMINARY FINDINGS" |
| V-03 | PASS | "Name up to three signals as most influential. For each, write a paragraph"; "each paragraph... argues why it carried more weight" |
| V-04 | PASS | ADVOCATE prose paragraphs per rank; Evidence Gate "any named signal absent from SURVEYOR inventory" fails the gate |
| V-05 | PASS | Phase 3 prose paragraphs; Gate 3 "All named signals exist in Phase 1 inventory -- invented signals fail this gate" |

### C-04 — Counter-evidence present

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | Phase 4 required with empty-case handling; Gate 4 "NOT: counter-evidence section skipped or collapsed to 'none identified'" |
| V-02 | PASS | DISSENT section required; "This section cannot be empty or replaced with 'no opposition identified.'" |
| V-03 | PASS | "Then write your counter-evidence paragraph... Do not skip this." + "If you found no counter-evidence, write a paragraph explaining that absence" |
| V-04 | PASS | ADVERSARY pre-verdict challenge + SKEPTIC section = dual-source counter-evidence. Strongest C-04: challenge is pre-committed before verdict is issued |
| V-05 | PASS | Phase 4 required; Gate 4 "Counter-evidence section is NOT skipped"; rebuttal or explicit "unresolved" required |

### C-05 — Synthesis supersedes signals

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | "This is a judgment, not a summary"; Gate 2 "NOT: verdict paragraph is a list of signal findings with a one-sentence conclusion appended at the end" |
| V-02 | PASS | "A RULING is a position, not an aggregation"; Ruling Seal "Ruling paragraph is a determination, not a list of findings with a conclusion appended" |
| V-03 | PASS | "Do not hedge in the verdict paragraph." -- register-level anti-hedging; "If you are uncertain, that belongs in the confidence score" |
| V-04 | PASS | JUDGE issues verdict "against the adversary's best case, not a summary of signal findings"; Verdict Gate "NOT: verdict is a list of signal summaries with a conclusion attached" |
| V-05 | PASS | "Do not list each signal's finding -- synthesize what they establish as a whole"; Gate 2 "Verdict paragraph is a synthesis judgment, NOT a list of signal findings with a conclusion attached" |

### C-06 — Principles extracted

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | Phase 5 "At least one declarative principle... Must generalize beyond the specific topic." |
| V-02 | PASS | Holdings "what this ruling establishes beyond this case"; "Holdings that merely restate the FINDING are not Holdings" |
| V-03 | PASS | "Declarative form required: 'X implies Y' or 'When Z, expect W.' A restatement of your verdict is not a principle." |
| V-04 | PASS | SCHOLAR section "declarative, generalizable -- not restatements of the verdict" + P-01 formatted template |
| V-05 | PASS | "Declarative form required: 'X implies Y' or 'When Z, expect W.' A restatement of your verdict is not a principle." |

### C-07 — Open questions identified

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | Phase 5 "at least one specific open question... Name the actual question... concrete next step" |
| V-02 | PASS | Open Record "next investigative action: which prove sub-skill or concrete step" |
| V-03 | PASS | "'More research needed' is not a question. Write the actual question, explain why it is still open, and name the concrete next step." |
| V-04 | PASS | NAVIGATOR Q-01 template: question + why open + next step |
| V-05 | PASS | "'More research needed' is not a question. Write the actual question, explain why it is still open, and name the concrete next step." |

### C-08 — Confidence is explained

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | Confidence rationale paragraph required; Gate 2 "NOT: confidence stated as a number only, without rationale paragraph" names the fail condition |
| V-02 | PASS | Ruling Seal "Confidence rationale paragraph present (score alone is insufficient)" -- explicit fail condition |
| V-03 | PASS | "A confidence number without this explanation fails the synthesis" -- inline fail condition named |
| V-04 | PASS | "A confidence number without this paragraph fails this section" -- explicit fail condition; high/low calibration thresholds specified |
| V-05 | PASS | "A number without this paragraph fails -- 'confidence is X' does not pass" -- strongest fail condition: names the exact output pattern that fails |

### C-09 — Evidence hierarchy is argued (ranked argument, not ranked list)

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | Phase 3 "each paragraph... argues why it carried more weight toward the Phase 2 verdict than the signals ranked below it"; Gate 3 "NOT: evidence hierarchy is a table with a 'why' column -- a table is an annotated list, not an argument" |
| V-02 | PASS | "arguing why this signal was more determinative than signals ranked below it -- not what it found, but why its weight exceeded the others"; Evidence Basis Seal "Comparative question answered for each rank" |
| V-03 | PASS | "This is a ranked argument, not a ranked list... Each paragraph must answer the comparative question: why this signal over the one ranked below it?" -- the R1 exemplar phrase, embedded inline |
| V-04 | PASS | ADVOCATE paragraphs per rank; Evidence Gate "NOT: rank 1 justified only as 'strongest support' without comparison to rank 2" names the exact failure mode |
| V-05 | PASS | "This is a ranked argument, not a ranked list. A table with a 'why' column is a ranked list -- it allows you to fill cells without constructing an argument." Gate 3 "Each paragraph answers the comparative question -- not just restates the finding" |

### C-10 — Synthesis is self-contained (explicit standalone mandate)

**This was the defining R1 failure (V-01..V-04 all failed). R2 fixed it by requiring explicit mandate in every variation.**

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | "Produce a synthesis that stands alone. A reader with no access to the underlying signals must understand the answer, the reasoning, and what to do next from this document alone. State this mandate in your opening paragraph before any inventory or verdict." -- explicit + placement requirement |
| V-02 | PASS | "This document stands alone: a reader with no prior knowledge of the investigation signals must understand the ruling, the evidence basis, the dissent, and the open record from this document alone. State this requirement in your opening paragraph." |
| V-03 | PASS | "A reader with no access to the underlying signals must understand the answer, the reasoning, and what to do next from this document alone. State this mandate explicitly in your opening sentence. The structure of the synthesis must emerge from the prose itself, not from headers that label it." -- adds structural reinforcement clause |
| V-04 | PASS | "Produce a synthesis that stands alone. A reader with no access to the underlying signals must understand the answer, the reasoning, and what to do next from this document alone. State this mandate explicitly in your opening paragraph." |
| V-05 | PASS | "Produce a synthesis that stands alone. State this now, in your opening sentence: ... Do not assume context. Explain everything." -- "Do not assume context" is the strongest reinforcement |

### C-11 — Anti-pattern gates named explicitly

**The new v2 criterion. The key question: does V-03 (no gates, no checklists) pass?**

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | Every gate is structured as NOT:-first. Gate 1: "NOT: signals listed without naming the artifact; NOT: evaluation or verdict present in this phase." Gate 2: "NOT: answer is a hedge; NOT: verdict paragraph is a list of signal findings." Gate 3: "NOT: evidence hierarchy is a table with a 'why' column." Gate 4: "NOT: counter-evidence section skipped." -- the defining axis of V-01, and the strongest C-11 implementation |
| V-02 | PASS | Seals embed failure mode naming: Ruling Seal "Ruling paragraph is a determination, not a list of findings with a conclusion appended"; Evidence Basis Seal "not a table row or bullet"; "not presence of support." Not NOT:-format but failure modes are named in seal items |
| V-03 | **FAIL** | V-03 explicitly eliminates gates and checklists as a structural design choice. Inline prose phrases ("This is a ranked argument, not a ranked list"; "Do not hedge") name failure modes, but C-11 requires "at least one gate or checklist item." V-03 has neither. The variation that most aggressively enforces C-12 (prose everywhere) undermines C-11 by removing the gate infrastructure that makes failure-mode naming structural. |
| V-04 | PASS | Verdict Gate and Evidence Gate use NOT: format: "NOT: verdict is a list of signal summaries"; "NOT: ADVERSARY challenge was acknowledged but not addressed"; "NOT: evidence hierarchy is a table with a 'why' column." Also: ADVERSARY section requires naming a specific failure mode ("Anti-pattern gate: Name one specific failure mode this synthesis must avoid") -- C-11 embedded as a required role output |
| V-05 | PASS | Phase 3 instruction: "A table with a 'why' column is a ranked list -- it allows you to fill cells without constructing an argument." Gate 2 "NOT a list of signal findings"; Gate 3 "NOT a table row or bullet point"; Gate 4 "Counter-evidence section is NOT skipped." |

**Why V-03 fails C-11**: The design axis for V-03 is "no section headers, no phase labels, no gate checklists." This was intended to force structural work into prose transitions (maximizing C-12). It succeeds at C-12 but eliminates the only mechanism available for C-11 compliance. Anti-pattern phrases exist inline, but they are prose directives -- not gate items. The criterion text is specific: "gate or checklist item." V-03 has neither by design.

### C-12 — Argumentative sections are prose

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | PASS | "Write argumentative sections -- verdict, evidence hierarchy, confidence rationale -- in prose paragraphs, not tables or bullet lists." Gate 3 "NOT: evidence hierarchy is a table with a 'why' column" |
| V-02 | PASS | "Write argumentative sections -- the ruling, the evidence basis, the confidence rationale -- in prose paragraphs. No tables in these sections." Evidence Basis Seal "Each evidence entry is a prose paragraph -- not a table row or bullet" |
| V-03 | PASS | "Write argumentative content -- verdict, evidence ranking, confidence rationale -- as prose paragraphs. There are no tables permitted. The synthesis is prose from start to finish." -- strongest C-12: tables prohibited globally |
| V-04 | PASS | "Write argumentative sections -- verdict, evidence hierarchy, confidence rationale -- in prose paragraphs, not tables or bullet lists." Evidence Gate "NOT: evidence hierarchy is a table with a 'why' column" |
| V-05 | PASS | "Write in prose. No tables in argumentative sections." Gate 3 "Each entry is a prose paragraph (NOT a table row or bullet point)" + Phase 3 inline explains WHY: "allows you to fill cells without constructing an argument" |

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
| C-09 | 2.5 | PASS | PASS | PASS | PASS | PASS |
| C-10 | 2.5 | PASS | PASS | PASS | PASS | PASS |
| C-11 | 2.5 | PASS | PASS | **FAIL** | PASS | PASS |
| C-12 | 2.5 | PASS | PASS | PASS | PASS | PASS |
| **Essential pts** | 60 | 60 | 60 | 60 | 60 | 60 |
| **Recommended pts** | 30 | 30 | 30 | 30 | 30 | 30 |
| **Aspirational pts** | 10 | 10 | 10 | 7.5 | 10 | 10 |
| **Composite** | 100 | **100** | **100** | **97.5** | **100** | **100** |
| **Result** | | Golden | Golden | Golden | Golden | Golden |

---

## Ranking

| Rank | Variation | Score | Differentiator |
|------|-----------|-------|----------------|
| 1 (tie) | V-01 | 100 | Strongest C-11: every gate is NOT:-first, failure modes listed before positive checks |
| 1 (tie) | V-02 | 100 | Novel mechanism: verdict register (RULING/DISSENT/HOLDINGS) as lexical-level anti-hedging |
| 1 (tie) | V-04 | 100 | Strongest C-04: ADVERSARY pre-verdict challenge is a pre-committed structural requirement |
| 1 (tie) | V-05 | 100 | R1 winner + full R2 upgrade: "Do not assume context. Explain everything." is the strongest C-10 reinforcement |
| 5 | V-03 | 97.5 | C-11 FAIL: continuous prose eliminates gates, removing the only mechanism for gate-based failure-mode naming |

**Separation note**: R2 has no single winner -- the four at 100 represent four distinct mechanisms that all achieve full compliance. V-03's failure is the most instructive result: the variation built around the strongest C-12 mechanism (prose everywhere) is the only one that fails C-11. The two new criteria are in tension when gates are eliminated.

---

## Excellence Signals from Round 2

**1. NOT:-first gate format (V-01)**
V-01's defining mechanism: every gate lists failure modes before positive checks. This ordering forecloses failure modes before the writer encounters the success condition. R1 gates mixed positive and negative checks; V-01 makes the negative check the default opening. The NOT: prefix is not cosmetic -- it positions the failure mode as the primary concern, with the positive check as confirmation.

**2. Formal verdict register as a novel anti-hedging mechanism (V-02)**
A RULING cannot be "it depends." The vocabulary creates cognitive commitment at the lexical level, independent of gate structure. DISSENT is structurally different from COUNTER-EVIDENCE: a dissent must be answered or acknowledged as unresolved; it cannot be noted and dismissed. V-02 achieves all four aspirational criteria through a mechanism none of the other variations use -- vocabulary, not structure.

**3. Pre-verdict ADVERSARY role as structural C-04 pre-commitment (V-04)**
The ADVERSARY runs before the verdict is issued. Counter-evidence is no longer a reflection phase after the conclusion is reached; it is a structural challenge the verdict must be issued against. The ADVERSARY section requires naming a specific failure mode for this particular signal set -- C-11 compliance is embedded as a required role output, not as a checklist item appended to a later section.

**4. Continuous prose reveals a C-11 / C-12 structural trade-off (V-03)**
V-03 achieves the strongest C-12 compliance: "There are no tables permitted. The synthesis is prose from start to finish." But it fails C-11 because eliminating gates removes the only structural mechanism that satisfies "gate or checklist item." This is a genuine design trade-off, not a flaw. A v3 variation testing whether prose-embedded anti-pattern sentences can be treated as "inline gates" would resolve whether the criterion requires structural formatting or just explicit failure-mode naming in any form.

---

## What R3 Should Test

The four-way tie at 100 means the v2 rubric is saturated for well-designed variations. R3 should probe mechanism quality, not mechanism presence:

- **V-01 NOT: format adversarial**: Does NOT:-first gate structure survive when the signal set is thin (1-2 signals)? Do NOT: checks produce better outputs than positive-check gates on real topics?
- **V-02 register stress test**: Does legal/verdict register hold when the hypothesis result is genuinely MAYBE? Can a RULING be inconclusive, or does the register force a false YES/NO?
- **V-03 + inline gate combo**: Can continuous prose satisfy C-11 by treating key anti-pattern sentences as "inline gates"? Test whether prose-embedded gate language ("A table is not an argument and fails this section") satisfies C-11 without a formatted checklist.
- **V-04 ADVERSARY in thin-signal conditions**: Does the ADVERSARY pre-challenge improve C-04 quality when there is only one signal? Or does it produce redundant content?

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["NOT:-first gate format: listing failure modes before positive checks forecloses non-compliant outputs before the writer reaches the success condition", "formal verdict register (RULING/DISSENT/HOLDINGS) achieves anti-hedging at the lexical level, independent of gate structure", "continuous prose eliminates gates and creates a C-11/C-12 structural trade-off: maximum C-12 compliance costs C-11 compliance", "pre-verdict ADVERSARY role makes counter-evidence a pre-committed structural requirement rather than a post-hoc reflection section"]}
```
