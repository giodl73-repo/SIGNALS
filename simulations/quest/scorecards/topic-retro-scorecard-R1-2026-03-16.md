Scorecard written to `simulations/quest/scorecards/topic-retro-scorecard-R1-2026-03-16.md`.

**Results:**

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | V-01 (Table-First) | 100 | YES |
| 1 | V-03 (Echo-First) | 100 | YES |
| 3 | V-04 (Auditor-First) | 95 | YES |
| 3 | V-05 (Inertia Frame) | 95 | YES |
| 5 | V-02 (Conversational) | 81.5 | NO |

**Discriminating criterion: C-07** (per-namespace accuracy differentiation). V-01 and V-03 pass it with explicit scoring schemas; V-04/V-05 partial it (evidence collected but no per-namespace score); V-02 fails it entirely (prose verdict only).

**Two new patterns:**
1. Explicit per-namespace accuracy formula (0-100) makes C-07 mechanically verifiable
2. Echo-first phase ordering prevents post-hoc rationalization of the unexpected finding

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["explicit per-namespace accuracy formula with 0-100 scoring produces mechanically verifiable C-07 output", "Echo-first phase ordering prevents post-hoc rationalization of the unexpected finding into the accuracy narrative"]}
```
_pass/3 * 30) + (aspirational_pass/2 * 10)
Golden: all 5 essential PASS + composite >= 80

**Note on C-09:** No prior retro exists for any topic in this repo. Rubric states this counts as PASS (N/A) for scoring.

---

## V-01 -- Table-First, Scored Scale

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory | PASS | Section 1 requires explicit table: one row per artifact with namespace, date, signal type, summary; plus namespace summary table with ABSENT flagging |
| C-02 | Predicted vs actual | PASS | Section 2 table schema: "What signals predicted" / "What actually happened" / "Match?" -- both sides required to be explicit; CORRECT/PARTIAL/WRONG/NO-DATA enumerated |
| C-03 | Gaps | PASS | Section 3 numbered list requires: Gap name, "Why it would have mattered" (1-2 sentences), "Skill to run next time" (specific skill); blank section called failure |
| C-04 | Echo | PASS | Section 4 dedicated to exactly one Echo with "Why it was unpredicted" and "Design implication" fields; "No Echo identified. All outcomes were within signal bounds." valid result |
| C-05 | Accuracy verdict | PASS | Section 5 per-namespace table with formula: (Correct*100 + Partial*50) / (Correct+Partial+Wrong); overall verdict line with STRONG/ADEQUATE/WEAK thresholds and score/100 |
| C-06 | Actionable gaps | PASS | Section 3 requires "Skill to run next time: [specific skill name, e.g., /listen-adoption]" -- named skill, not generic advice |
| C-07 | Per-namespace accuracy | PASS | Section 5 explicitly produces per-namespace accuracy table (Namespace / Signals / Correct / Partial / Wrong / Score) before aggregate verdict |
| C-08 | AMEND scope | PASS | AMEND section scopes all five sections; "State the applied scope constraint at the top of the output before Section 1" |
| C-09 | Calibration trend | PASS (N/A) | No prior retro exists; counts as pass per rubric note |
| C-10 | Echo -> signal design | PASS | Section 4 "Design implication: [what skill, threshold, or rubric change would catch this class of surprise earlier]" -- explicit named-change requirement |

essential_pass = 5.0 | recommended_pass = 3.0 | aspirational_pass = 2.0
**Composite = (5/5 * 60) + (3/3 * 30) + (2/2 * 10) = 60 + 30 + 10 = 100**
**Golden: YES**

---

## V-02 -- Conversational Register

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory | PASS | Question 1: list every artifact grouped by namespace, count per namespace, call out empty namespaces -- required elements covered in list format |
| C-02 | Predicted vs actual | PARTIAL | Question 2 asks for comparison but instructs "conversational -- not a table. Lead with the surprising misses." Leading-with-misses can suppress the predicted side to implication. Both sides required but prose format reduces enforcement. Present_mechanism: comparison instruction and "be honest about the match" directive. Absent_mechanism: explicit schema enforcing both "predicted" and "actual" as named fields. |
| C-03 | Gaps | PASS | Question 3: "Name the namespace, name the skill, name what it would have surfaced" -- rejects generic, demands skill + catch |
| C-04 | Echo | PASS | Question 4: "Pick exactly one thing... the most surprising post-ship observable. Call it the Echo." Nearest signal + design change question. |
| C-05 | Accuracy verdict | PASS | Question 5: "Give a verdict: strong... adequate... weak?" grounded in Question 2 evidence; qualitative rating is rubric-allowed |
| C-06 | Actionable gaps | PASS | Question 3: "Name the namespace, name the skill, name what it would have surfaced" -- explicit |
| C-07 | Per-namespace accuracy | FAIL | Question 2 produces per-namespace narratives with match language but no accuracy score per namespace. Question 5 renders overall qualitative verdict only. No per-namespace accuracy breakdown required or produced. |
| C-08 | AMEND scope | PASS | AMEND section applies scope to all five questions and states clearly at top |
| C-09 | Calibration trend | PASS (N/A) | No prior retro; N/A = pass |
| C-10 | Echo -> signal design | PARTIAL | Question 4: "what would you change in your signal design to catch this class of thing earlier?" -- open question, not typed-change requirement. Direction is right but change type unspecified. Present_mechanism: design-change question present in Echo section. Absent_mechanism: enumerated change-type options (skill / rubric amendment / threshold) forcing a typed concrete proposal. |

essential_pass = 4.5 | recommended_pass = 2.0 | aspirational_pass = 1.5
**Composite = (4.5/5 * 60) + (2/3 * 30) + (1.5/2 * 10) = 54 + 20 + 7.5 = 81.5**
**Golden: NO** -- C-02 is PARTIAL (Golden requires all essential to be full PASS)

---

## V-03 -- Lifecycle Emphasis: Echo-First

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory | PASS | Phase 1: flat list "[namespace] / [artifact name] / [one-phrase summary]" with total count and list of empty namespaces; intentionally compact |
| C-02 | Predicted vs actual | PASS | Phase 3: "State what the signals predicted... State what actually happened... Rate the match: CORRECT / PARTIAL / WRONG / NO-DATA." Both sides required, one paragraph per namespace |
| C-03 | Gaps | PASS | Phase 4: "Name the missing signal type -- Name the skill that generates it -- State specifically what it would have caught." Includes DESIGN GAP flag for structural catalog gaps |
| C-04 | Echo | PASS | Phase 2 is an expanded phase dedicated to Echo with 2-step candidate process; Step 2 selects exactly one; valid stop condition for no-Echo included |
| C-05 | Accuracy verdict | PASS | Phase 5: "Accuracy: [N correct] / [N total scored] ([percent]%)" plus "By namespace: [highest]...[lowest]" plus STRONG/ADEQUATE/WEAK overall rating |
| C-06 | Actionable gaps | PASS | Phase 4: "Name the skill that generates it -- State specifically what it would have caught" |
| C-07 | Per-namespace accuracy | PASS | Phase 5 explicitly: "By namespace: [highest accuracy namespace]...[lowest accuracy namespace]" plus Phase 3 per-namespace blocks with match verdicts |
| C-08 | AMEND scope | PASS | AMEND section applies throughout all phases; "State applied scope before Phase 1" |
| C-09 | Calibration trend | PASS (N/A) | No prior retro; N/A = pass |
| C-10 | Echo -> signal design | PASS | Phase 2, Step 3: "Design change: [specific skill, rubric amendment, or threshold to add]" -- typed enumeration of change options; strongest C-10 formulation in the set |

essential_pass = 5.0 | recommended_pass = 3.0 | aspirational_pass = 2.0
**Composite = 60 + 30 + 10 = 100**
**Golden: YES**

---

## V-04 -- Role Sequence: Auditor-First, Verdict Card

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory | PASS | Role 1 (Inventory Auditor) produces confirmed inventory list with namespace/artifact/date/claim, namespace coverage summary (Present/Absent), and total confirmed signal count |
| C-02 | Predicted vs actual | PASS | Role 2, Step A: "Predicted: [what confirmed signals claimed would happen] -- Actual: [post-ship observation] -- Match: CORRECT / PARTIAL / WRONG / NO-DATA" -- both sides explicit per namespace |
| C-03 | Gaps | PASS | Role 2, Step B: review WRONG and PARTIAL matches; name missing signal, name skill, one sentence on catch; also flags absent namespaces that would have changed commit |
| C-04 | Echo | PASS | Role 2, Step C: "Name exactly one post-ship finding that no confirmed signal predicted... If no such finding exists, state so explicitly." Echo entry with Nearest signal + Design change |
| C-05 | Accuracy verdict | PASS | Role 2, Step D (Verdict Card): "Accuracy: [N correct / N scored] = [%]" and "Rating: STRONG / ADEQUATE / WEAK" -- quantitative grounding |
| C-06 | Actionable gaps | PASS | Role 2, Step B: "Name the skill to run next time" -- explicit |
| C-07 | Per-namespace accuracy | PARTIAL | Step A has per-namespace match blocks (CORRECT/PARTIAL/WRONG/NO-DATA) but Verdict Card shows only aggregate accuracy percentage. Present_mechanism: per-namespace match verdicts in Step A blocks. Absent_mechanism: per-namespace accuracy score/percentage in final output. |
| C-08 | AMEND scope | PASS | AMEND section scopes both roles; "State applied scope before Role 1 begins" |
| C-09 | Calibration trend | PASS (N/A) | No prior retro; N/A = pass |
| C-10 | Echo -> signal design | PASS | Step C: "Design change: [skill, rubric amendment, or threshold addition]" -- typed change options required |

essential_pass = 5.0 | recommended_pass = 2.5 | aspirational_pass = 2.0
**Composite = (5/5 * 60) + (2.5/3 * 30) + (2/2 * 10) = 60 + 25 + 10 = 95**
**Golden: YES**

---

## V-05 -- Full Integration: Inertia Framing + Conversational + Expanded Gaps

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory | PASS | Section 1 "WHAT WE HAD": group by namespace, note empty namespaces, total count -- explicitly called a setup step, kept brief |
| C-02 | Predicted vs actual | PASS | Section 2 per-namespace narrative requires: (1) what signals told you, (2) did prediction hold after ship?, (3) counterfactual. "The mismatch... should be explicit here -- not softened." Both sides enforced |
| C-03 | Gaps | PASS | Section 3 tiered: Tier 1 requires "Which skill generates this signal? (Name the exact skill.)" -- most explicit skill-naming instruction of all 5 variations |
| C-04 | Echo | PASS | Section 4: "One thing... the thing that no signal predicted and that wasn't even a named unknown at commit time." Named Echo with nearest signal and design change. Valid no-Echo statement included. |
| C-05 | Accuracy verdict | PASS | Section 5: "Honest overall rating: STRONG / ADEQUATE / WEAK. Grounded in the per-namespace evidence from Section 2." Plus inertia frame verdict sentence |
| C-06 | Actionable gaps | PASS | Section 3 Tier 1: "Which skill generates this signal? (Name the exact skill.)" and inertia check -- most thorough gap + skill requirement |
| C-07 | Per-namespace accuracy | PARTIAL | Section 2 has explicit per-namespace narratives with prediction vs actual. Section 5 references "per-namespace evidence from Section 2" but renders only overall qualitative verdict. Present_mechanism: per-namespace evidence collected with explicit mismatch requirement. Absent_mechanism: per-namespace accuracy score/percentage in Section 5 verdict. |
| C-08 | AMEND scope | PASS | AMEND section applies scope throughout all sections; "State the applied scope as the first line of output" |
| C-09 | Calibration trend | PASS (N/A) | No prior retro; N/A = pass |
| C-10 | Echo -> signal design | PASS | Section 4: "a specific skill, a rubric amendment, a new threshold, or a signal type that doesn't exist yet in the namespace catalog" -- typed enumeration; adds non-existing-skill-type as fourth change category |

essential_pass = 5.0 | recommended_pass = 2.5 | aspirational_pass = 2.0
**Composite = (5/5 * 60) + (2.5/3 * 30) + (2/2 * 10) = 60 + 25 + 10 = 95**
**Golden: YES**

---

## Leaderboard

| Rank | Variation | Composite | Golden? | Discriminating criterion |
|------|-----------|-----------|---------|--------------------------|
| 1 | V-01 | 100 | YES | C-07 PASS (explicit per-namespace formula) |
| 1 | V-03 | 100 | YES | C-07 PASS (by namespace in Phase 5) |
| 3 | V-04 | 95 | YES | C-07 PARTIAL (per-ns match present; no per-ns score) |
| 3 | V-05 | 95 | YES | C-07 PARTIAL (per-ns evidence present; no per-ns score) |
| 5 | V-02 | 81.5 | NO | C-02 PARTIAL (prose format; C-07 FAIL) |

C-07 is the sole discriminating criterion in this round.

---

## Excellence Signals

**Signal 1 -- V-01 / C-07:** Explicit per-namespace accuracy formula in the prompt produces mechanically verifiable output. The schema `(Correct * 100 + Partial * 50) / (Correct + Partial + Wrong)` makes C-07 pass deterministic -- no evaluator judgment required about whether a "per-namespace breakdown" has occurred.

**Signal 2 -- V-03 / C-04:** Echo-first phase ordering (Phase 2 before Phase 3) is the only design that structurally prevents the unexpected finding from being absorbed into the predicted-vs-actual narrative. The constraint "The Echo must not be revised after Phase 3 runs" locks the finding before accuracy scoring begins.

**Signal 3 -- V-03 / C-10:** "Design change: [specific skill, rubric amendment, or threshold to add]" is the strongest Echo-to-design-change formulation -- typed enumeration with three named option categories. V-05 extends it with "a signal type that doesn't exist yet in the namespace catalog" as a fourth category.

---

## Failure Patterns

**C-07 (per-namespace accuracy differentiation):** Fails or partially fails in 3 of 5 variations.
- V-02 (FAIL): prose-only Question 5 verdict drops per-namespace differentiation entirely
- V-04, V-05 (PARTIAL): collect per-namespace evidence in narrative sections but do not produce a labeled per-namespace accuracy score

Diagnosis: **skill design issue** -- prose-format verdict sections consistently drop per-namespace differentiation. Only variations with an explicit per-namespace scoring table/schema (V-01, V-03) produce the required breakdown.

Pattern to carry forward into rubric: any variation that uses a prose or narrative verdict section will PARTIAL or FAIL C-07 unless it explicitly mandates a per-namespace accuracy value alongside the prose.

No other criterion fails consistently.

---

## Regression Signals

No prior round data -- regression analysis not possible.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["explicit per-namespace accuracy formula with 0-100 scoring produces mechanically verifiable C-07 output", "Echo-first phase ordering prevents post-hoc rationalization of the unexpected finding into the accuracy narrative"]}
```
