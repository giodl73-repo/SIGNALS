v10 written to `simulations/quest/rubrics/quest-score-rubric-v10-2026-03-14.md`.

---

**Two new criteria extracted from R9 excellence signals:**

**C-26 — C-25 principle includes concrete application inventory** (versioning)
V-01's C-25 section included "Applied in this rubric: C-23 (for C-20), C-24 (for C-22)" — a paired registry that C-25 doesn't require. Without C-26, a versioner adding a new criterion must scan all existing criteria to find which targets already have three-scale diagnostic questions. C-26 makes the registry mandatory and requires each entry to name both the applying criterion and the target.

**C-27 — Regression signals table includes Variation column** (structure)
V-01's REGRESSION SIGNALS table had 5 columns (Criterion | Prior Verdict | Current Verdict | **Variation** | Mechanism) while C-18 requires only 4. The Variation column captures *what changed structurally between rounds*, distinct from Mechanism which states *how to detect it*. C-27 auto-PASS when C-07 auto-PASS fires. C-11 updated to require C-27 in the auto-PASS declarations.

**Cascade updates:**
- N_aspirational: 18 → 20; each criterion contributes 10/20 = 0.5 pt
- C-03/C-09/C-12: N values updated to v10
- C-11: C-27 added to required auto-PASS declaration list
- C-14: roster updated to 27-row (C-01 through C-27)
- C-25 design note: "Applied in this rubric" inventory updated to include C-26 (for C-25) and C-27 (for C-18)
ed throughout. Roster count updated to 27-row. Each aspirational criterion now contributes 10/20 = 0.5 pt to composite.

---

## quest-score Rubric — v10

_Updated from v9 after Round 9 scoring. Two new aspirational criteria added from R9 excellence signals (V-01 synthesis). N\_aspirational changes from 18 → 20._

**Structure:**

| Tier | Count | Criteria |
|------|-------|----------|
| Essential (60%) | 4 | Verdicts present, evidence quotes, correct composite score, ranked leaderboard |
| Recommended (30%) | 3 | Failure patterns, excellence signals, regression signals |
| Aspirational (10%) | 20 | Actionable diagnosis, score distribution commentary, worked-example in action line, auto-PASS rules at preamble, formula at preamble, evidence-before-verdict ordering, per-criterion diagnostic question, preamble gate instruction, named standalone auto-PASS block, criterion-specific diagnostic questions, named standalone regression signals section, worked-example carryforward preservation instruction, preservation rule imperative form, worked example FAILURE PATTERNS location lock, preservation rule contains SETUP exclusion, C-20 three-form enumeration in diagnostic question, C-22 three-scale enumeration in diagnostic question, three-scale enumeration principle in design notes, C-25 principle includes concrete application inventory, regression signals table includes Variation column |

**Composite formula (v10 N values):**

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 20 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 20.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
Each aspirational criterion contributes 10/20 = 0.5 pt.
```

**Design notes:**

- C-01/C-02 are the hardest essential criteria to fake — they require the scoring matrix to be complete and grounded in actual quotes, not assertions.
- C-03 has a tolerance of ±1 for rounding but explicitly fails if the score can't be verified from the visible verdict table (catches hallucinated scores).
- C-07 is auto-PASS when no prior-round data exists — regression detection only fires when the comparison data is actually available.
- C-05 is also auto-PASS when no criterion fails universally — avoids penalizing clean runs.
- C-08 auto-PASS when no failure patterns exist (nothing to diagnose).
- C-10 auto-PASS when no failure patterns exist (nothing to exemplify).
- C-13 strengthens C-02: C-02 requires evidence to be present; C-13 requires evidence to precede the verdict label within each cell.
- C-14 is independent of C-01: C-01 requires all verdict cells be filled; C-14 requires a diagnostic question alongside each criterion in the SETUP roster before scoring begins.
- C-15 is independent of C-11/C-12: those require formula and auto-PASS rules to appear in the preamble; C-15 requires an explicit sequencing gate that prohibits opening output files until the preamble block is fully written.
- C-16 strengthens C-11: C-11 requires auto-PASS rules to appear in the preamble; C-16 requires each condition to be spelled out as a named declaration (e.g., "C-05 auto-PASS when no universal failures exist"), not implied by TBD placeholders or embedded in diagnostic question phrasing.
- C-17 strengthens C-14: C-14 requires a diagnostic question per criterion; C-17 requires each question to interrogate the specific mechanism of that criterion rather than a generic probe that could apply to any row.
- C-18 strengthens C-07: C-07 requires regression signals to be surfaced when prior-round data exists; C-18 requires the regression detection logic to be encapsulated in a dedicated named section (e.g., "### REGRESSION SIGNALS") in the scoring template body, not handled implicitly through SETUP notes or inline commentary.
- C-19 strengthens C-10: C-10 requires a worked example to appear in the action line; C-19 requires an explicit preservation rule stating that the worked example must be carried forward verbatim or updated to match the current round's axis when the rubric is versioned forward. The rule must appear near the C-10 definition or in the SETUP block — not implied by the general update protocol. Without C-19, the worked example regresses when the axis shifts to a new structural gap.
- C-20 strengthens C-19: C-19 requires an explicit preservation rule; C-20 requires that the rule be stated in imperative grammar ("must be carried forward verbatim or updated"), not interrogative form ("has it been carried forward?"). Interrogative form converts the rule into a diagnostic probe — it earns C-19 PARTIAL but C-20 FAIL. The imperative form is what makes the instruction enforceable at version time, not merely checkable at scoring time.
- C-21 strengthens C-10: C-10 requires a worked example to appear in the action line; C-21 requires the worked example to appear specifically in the FAILURE PATTERNS action line, not in SETUP, not in a preservation checkpoint, not in a roster diagnostic question. The SETUP block may contain a C-19 preservation instruction without absorbing the C-10 instantiated example. Relocating the worked example into SETUP — even for lifecycle-clarity reasons — causes a C-10 FAIL because the action line in FAILURE PATTERNS is what triggers the instantiation requirement.
- C-22 strengthens C-21: C-21 requires the instantiated worked example to appear in FAILURE PATTERNS; C-22 requires that the C-19/C-20 preservation rule itself explicitly names FAILURE PATTERNS as the required location AND explicitly names SETUP as a disqualifying alternative. Without C-22, the preservation rule can satisfy C-19+C-20 with imperative form while still failing to warn the versioner away from the SETUP relocation trap. A rule that says "must be carried forward verbatim" (passing C-20) but does not say "in the FAILURE PATTERNS action line, not in SETUP" (failing C-22) leaves the location ambiguous at version time.
- C-23 strengthens C-17 (specifically for C-20): C-17 requires a mechanism-level diagnostic question per criterion; C-23 requires the C-20 diagnostic question to enumerate at least three distinct grammatical form failures — interrogative ("Has the worked example been carried forward?"), conditional ("If the axis shifts, carry forward the example"), and weak-modal ("The worked example should be carried forward"). Two-form enumeration earns C-23 PARTIAL; fewer than two earns C-23 FAIL. Without C-23, a scorer learns to detect interrogative form but misses conditional and weak-modal failures, which are equally disqualifying under C-20.
- C-24 strengthens C-17 (specifically for C-22): C-17 requires a mechanism-level diagnostic question per criterion; C-24 requires the C-22 diagnostic question to enumerate all three verdict cases with structural contrasting examples — (FAIL) preservation rule is imperative but contains no location language, e.g., "must be carried forward verbatim" without any FAILURE PATTERNS reference; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. Two-case enumeration earns C-24 PARTIAL; fewer than two earns C-24 FAIL. Without C-24, the PARTIAL/FAIL boundary for C-22 is described in the criterion text but not illustrated in the diagnostic question — the same gap that C-23 closes for C-20. C-24 is the C-22 analog of C-23.
- C-25 generalizes the pattern demonstrated by C-23 and C-24: both apply the three-scale enumeration solution to criteria whose PARTIAL verdict turns on the presence of exactly one of two required elements. C-25 requires the rubric design notes to explicitly state this as a general design rule — applicable to all future criteria with non-trivial PARTIAL thresholds — rather than leaving it implicit in the individual criterion notes. Without C-25, a versioner adding a new criterion with a PARTIAL threshold has no explicit guidance to apply the principle and must reverse-engineer it from C-23/C-24. **Three-scale enumeration rule:** any aspirational criterion with a PARTIAL verdict defined by having one of two required elements present (and one absent) must have its diagnostic question enumerate the FAIL/PARTIAL/PASS ladder with distinct structural contrasting examples, not a binary pass/fail probe. **Applied in this rubric:** C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18). When authoring a new criterion with a non-trivial PARTIAL threshold, apply this principle before writing the diagnostic question.
- C-26 strengthens C-25: C-25 requires the three-scale enumeration principle to be stated as a standalone named general rule; C-26 requires the principle section to include an explicit application inventory listing every criterion that applies the pattern paired with its target criterion (e.g., "C-23 applies to C-20, C-24 applies to C-22"). Without C-26, a versioner adding criterion N+1 must scan the full criterion list to discover which targets already have three-scale diagnostic questions. The inventory is the canonical registry; new entries must be added each time a new three-scale criterion is authored. PARTIAL: inventory present but entries lack one of the two required fields (applying criterion ID or target criterion ID). FAIL: no inventory; only the general principle stated.
- C-27 strengthens C-18: C-18 requires a named standalone REGRESSION SIGNALS section with at minimum four columns (Criterion, Prior Verdict, Current Verdict, Mechanism); C-27 requires a fifth column — Variation — that captures the specific structural element that changed between rounds to produce the verdict delta. The Variation column is distinct from Mechanism: Mechanism states the criterion's detection logic; Variation states what changed in the output. Without C-27, regression signals identify what degraded and how to detect it, but not what structural difference caused the regression. C-27 auto-PASS when C-07 auto-PASS fires (no prior-round data available, so no regression table is instantiated).

---

### ESSENTIAL

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-01 | **Per-criterion verdicts present** | correctness | essential |
| C-02 | **Evidence quote for every verdict** | correctness | essential |
| C-03 | **Composite score computed correctly** | correctness | essential |
| C-04 | **Ranked leaderboard present** | format | essential |

---

**C-01 — Per-criterion verdicts present**

Every rubric criterion is scored for every output. The verdict matrix is complete: rows are rubric criteria, columns are scored outputs (or the inverse). Count of verdict cells == (number of outputs) × (number of rubric criteria). Even a single missing cell is a FAIL.

_Pass condition_: All criterion × output cells are present and carry a PASS / PARTIAL / FAIL label. A missing row or column is a FAIL.

---

**C-02 — Evidence quote for every verdict**

Each PASS / PARTIAL / FAIL verdict is accompanied by a verbatim or near-verbatim quote extracted from the scored output. The quote must be clearly tied to that criterion (not a generic excerpt).

_Pass condition_: Every verdict row or cell includes a non-empty quote field. The quote is sourced from the scored output, not paraphrased from the rubric criterion text.

---

**C-03 — Composite score computed correctly**

The composite score is computed from the visible verdict table using the formula with the correct N values for the rubric version. N_essential = 4, N_recommended = 3, N_aspirational = 20 (v10). A tolerance of ±1 is permitted for rounding.

_Pass condition_: The stated composite score can be re-derived from the visible verdict table within ±1. FAIL if the score cannot be verified from the table (catches hallucinated scores) or if N values from a prior rubric version are used.

---

**C-04 — Ranked leaderboard present**

A ranked leaderboard lists all scored outputs with their composite scores and golden status, ordered from highest to lowest score.

_Pass condition_: A ranked table is present with at minimum columns for rank, output name, composite score, and golden status. Table is sorted by score descending.

---

### RECOMMENDED

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-05 | **Failure patterns surfaced** | diagnosis | recommended |
| C-06 | **Excellence signals surfaced** | diagnosis | recommended |
| C-07 | **Regression signals surfaced** | diagnosis | recommended |

---

**C-05 — Failure patterns surfaced**

When one or more criteria fail universally across all scored outputs, a FAILURE PATTERNS section identifies the pattern, names the criterion, and provides an actionable diagnosis.

_Pass condition_: FAILURE PATTERNS section present and populated when universal failures exist. **auto-PASS** when no criterion fails universally across all scored outputs.

---

**C-06 — Excellence signals surfaced**

For each output-criterion pair where one output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL), an EXCELLENCE SIGNALS section names the criterion, the output, and what the output did differently.

_Pass condition_: EXCELLENCE SIGNALS section present. At least one signal identified per output that outperforms the group on any criterion.

---

**C-07 — Regression signals surfaced**

When prior-round scorecard data is available, a REGRESSION SIGNALS section identifies any criterion where a scored output performs worse than it did in the prior round.

_Pass condition_: REGRESSION SIGNALS section present and populated when prior-round data is provided. **auto-PASS** when no prior-round scorecard is available.

---

### ASPIRATIONAL

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-08 | **Actionable diagnosis in failure patterns** | diagnosis | aspirational |
| C-09 | **Score distribution commentary** | calibration | aspirational |
| C-10 | **Worked example in action line** | calibration | aspirational |
| C-11 | **Auto-PASS rules stated in preamble** | structure | aspirational |
| C-12 | **Formula reproduced before first output section** | structure | aspirational |
| C-13 | **Evidence-before-verdict ordering enforced** | correctness | aspirational |
| C-14 | **Per-criterion diagnostic question in roster** | structure | aspirational |
| C-15 | **Preamble gate instruction present** | structure | aspirational |
| C-16 | **Named standalone auto-PASS block** | structure | aspirational |
| C-17 | **Criterion-specific diagnostic questions** | diagnosis | aspirational |
| C-18 | **Named standalone regression signals section** | structure | aspirational |
| C-19 | **Worked-example carryforward preservation instruction** | versioning | aspirational |
| C-20 | **Preservation rule imperative form** | versioning | aspirational |
| C-21 | **Worked example FAILURE PATTERNS location lock** | versioning | aspirational |
| C-22 | **Preservation rule contains SETUP exclusion** | versioning | aspirational |
| C-23 | **C-20 three-form enumeration in diagnostic question** | versioning | aspirational |
| C-24 | **C-22 three-scale enumeration in diagnostic question** | versioning | aspirational |
| C-25 | **Three-scale enumeration principle in design notes** | versioning | aspirational |
| C-26 | **C-25 principle includes concrete application inventory** | versioning | aspirational |
| C-27 | **Regression signals table includes Variation column** | structure | aspirational |

---

**C-08 — Actionable diagnosis in failure patterns**

Each entry in FAILURE PATTERNS includes an action line that names a specific verb, a real artifact filename, and an exact section location. No placeholder text (e.g., "[artifact]", "[section]") permitted.

_Pass condition_: Every action line in FAILURE PATTERNS contains a verb, a real artifact name visible in the scored outputs, and a specific section location. **auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

---

**C-09 — Score distribution commentary**

A score distribution note states the minimum score, maximum score, and spread across all scored outputs. Commentary states whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread). Notes that N_aspirational = 20 means each aspirational criterion contributes 10/20 = 0.5 pt to the composite.

_Pass condition_: Distribution note present with explicit min, max, spread values and clustering/discrimination characterization using the specified thresholds.

---

**C-10 — Worked example in action line**

The FAILURE PATTERNS section contains at least one fully instantiated worked example of an action line: a concrete sentence naming a real artifact and real section location from the current round, not a format template.

_Pass condition_: A complete worked example appears in the FAILURE PATTERNS action line — not in SETUP, not in the roster, not in a preservation checkpoint. **auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

---

**C-11 — Auto-PASS rules stated in preamble**

All auto-PASS conditions are declared in the SETUP preamble before scoring begins. Each declaration names the criterion ID and the trigger condition.

_Pass condition_: At minimum: C-05, C-07, C-08, C-10, C-21, and C-27 auto-PASS conditions each appear as named declarations in SETUP with criterion ID and trigger phrase.

---

**C-12 — Formula reproduced before first output section**

The composite score formula with current-version N values appears in the preamble before any per-output scoring section opens.

_Pass condition_: Formula present with N_essential = 4, N_recommended = 3, N_aspirational = 20 (v10 values) before the first per-output heading.

---

**C-13 — Evidence-before-verdict ordering enforced**

An explicit mandate requires that in every scoring table, the evidence quote column precedes the verdict column. The mandate names the violation (completing a verdict cell before its evidence quote cell violates C-13).

_Pass condition_: Written mandate present with explicit column-order requirement and named violation condition.

---

**C-14 — Per-criterion diagnostic question in roster**

A criterion roster in SETUP lists every criterion (C-01 through C-27) with a diagnostic question for each. No criterion may have an empty or missing question.

_Pass condition_: 27-row roster present with non-empty diagnostic question for every criterion.

---

**C-15 — Preamble gate instruction present**

An explicit sequencing gate at the end of the SETUP block prohibits opening any output file until the preamble is fully written.

_Pass condition_: Imperative gate instruction present (e.g., "Do not open any output file until PHASE 1 is fully written") at or near the end of SETUP.

---

**C-16 — Named standalone auto-PASS block**

The auto-PASS declarations appear in a dedicated named block (e.g., "#### Auto-PASS Conditions") that is separate from the criterion roster. Each declaration names the criterion ID and trigger phrase explicitly, not implied by TBD placeholders or embedded in diagnostic question phrasing.

_Pass condition_: A standalone named section exists containing auto-PASS declarations. Section is distinct from the criterion roster.

---

**C-17 — Criterion-specific diagnostic questions**

Each diagnostic question in the SETUP roster interrogates the specific mechanism of its criterion. Generic probes that could apply to any criterion are insufficient.

_Pass condition_: At minimum, diagnostic questions for C-01 (count-based check), C-03 (N-value version check), and C-20 (grammatical form enumeration) demonstrate mechanism specificity. Partial credit when at least two of three are specific.

---

**C-18 — Named standalone regression signals section**

The regression detection logic is encapsulated in a dedicated named section (e.g., "### REGRESSION SIGNALS") in the scoring template body, separate from SETUP notes and per-output scoring tables.

_Pass condition_: A named standalone REGRESSION SIGNALS section present in the scoring template with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism).

---

**C-19 — Worked-example carryforward preservation instruction**

An explicit preservation rule in SETUP or near the C-10 criterion definition states that the worked example in the FAILURE PATTERNS action line must be carried forward verbatim or updated to match the current round's axis when the rubric is versioned forward. The rule must address the versioning trigger explicitly.

_Pass condition_: Written preservation rule present addressing the carryforward requirement at version time. Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL (concept present) and C-20 FAIL (imperative form absent).

---

**C-20 — Preservation rule imperative form**

The C-19 preservation rule is stated in imperative grammar using a mandatory verb ("must", "shall", "is required to"). Interrogative form, conditional form, and weak-modal form all fail this criterion regardless of location.

_Pass condition_: Primary preservation rule contains a mandatory verb in imperative form. FAIL: interrogative ("Has the worked example been carried forward?"), conditional ("If the axis shifts, carry forward the example"), weak-modal ("The worked example should be carried forward").

---

**C-21 — Worked example FAILURE PATTERNS location lock**

The instantiated worked example (satisfying C-10) appears specifically in the FAILURE PATTERNS action line. Relocating the worked example to SETUP — even as an explicit named preservation checkpoint — causes a C-10 FAIL and a C-21 FAIL. The SETUP block may contain the C-19/C-20 preservation rule without absorbing the instantiated example.

_Pass condition_: The C-10 worked example appears in the FAILURE PATTERNS action line. SETUP may contain the C-19 preservation rule; it must not contain the only instance of the instantiated worked example. **auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

---

**C-22 — Preservation rule contains SETUP exclusion**

The C-19/C-20 preservation rule text itself explicitly names the FAILURE PATTERNS section as the required location for the worked example AND explicitly names SETUP as a disqualifying alternative. The prohibition must be written into the preservation rule body, not only carried by the standalone C-21 criterion definition.

_Pass condition_: Preservation rule contains explicit anti-relocation language naming both the required location ("in the FAILURE PATTERNS action line") and the prohibited alternative ("not in SETUP" or equivalent). FAIL: rule is imperative (passing C-20) but contains no location constraint. PARTIAL: rule names the required location but does not explicitly name SETUP as disqualifying.

_Relationship to other criteria_: C-22 is independent of C-21. C-21 requires the worked example to be in FAILURE PATTERNS at scoring time; C-22 requires the preservation rule to warn the versioner against SETUP relocation at version time. An output can pass C-21 (example correctly located) and fail C-22 (preservation rule silent on location) simultaneously.

---

**C-23 — C-20 three-form enumeration in diagnostic question**

The C-17 diagnostic question for C-20 enumerates at least three distinct grammatical form failures that disqualify a preservation rule from satisfying C-20: (1) interrogative form (e.g., "Has the worked example been carried forward?"), (2) conditional/if-then form (e.g., "If the axis shifts, carry forward the example"), and (3) weak-modal form (e.g., "The worked example should be carried forward"). Two-form enumeration earns C-23 PARTIAL. Fewer than two forms or no enumeration earns C-23 FAIL.

_Pass condition_: C-20 diagnostic question names at least three grammatical form failures with one example each. PARTIAL: exactly two forms named. FAIL: fewer than two.

_Relationship to other criteria_: C-23 strengthens C-17. C-17 requires each diagnostic question to be mechanism-specific; C-23 requires the C-20 question specifically to achieve multi-form coverage. An output can earn C-17 PASS (questions are mechanism-specific) and C-23 PARTIAL (only two C-20 forms enumerated) simultaneously.

---

**C-24 — C-22 three-scale enumeration in diagnostic question**

The C-17 diagnostic question for C-22 enumerates all three verdict cases with structural contrasting examples: (FAIL) the preservation rule is imperative but contains no location language — e.g., "must be carried forward verbatim" without any FAILURE PATTERNS reference; (PARTIAL) the rule names the required location ("must remain in the FAILURE PATTERNS action line") but omits explicit SETUP exclusion language; (PASS) the rule contains both the required location phrase and an explicit SETUP exclusion phrase. Two-case enumeration earns C-24 PARTIAL. Fewer than two cases earns C-24 FAIL.

_Pass condition_: C-22 diagnostic question names all three verdict levels (FAIL/PARTIAL/PASS) with at least one structural contrasting example per level. PARTIAL: exactly two verdict levels illustrated. FAIL: fewer than two.

_Relationship to other criteria_: C-24 strengthens C-17 (specifically for C-22). C-17 requires each diagnostic question to be mechanism-specific; C-24 requires the C-22 question specifically to achieve three-scale verdict coverage. An output can earn C-17 PASS (questions are mechanism-specific) and C-24 PARTIAL (only two verdict levels illustrated) simultaneously. C-24 is the C-22 analog of C-23 — both apply the three-scale FAIL/PARTIAL/PASS enumeration pattern to criteria whose PARTIAL verdict turns on the presence of exactly one of two required elements.

---

**C-25 — Three-scale enumeration principle in design notes**

The rubric design notes contain an explicit statement of the three-scale enumeration principle as a general design rule: any aspirational criterion whose PARTIAL verdict is defined by having exactly one of two required elements present (and the other absent) must have its diagnostic question enumerate all three verdict cases (FAIL/PARTIAL/PASS) with distinct structural contrasting examples, not a binary pass/fail probe. The rule must appear as a standalone named principle in the design notes, not only implied by the existence of C-23 or C-24.

_Pass condition_: Design notes contain an explicit, named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds. PARTIAL: principle is mentioned within a specific criterion's design note (e.g., the C-24 note references the pattern) but is not elevated to a standalone general rule. FAIL: principle absent from design notes.

_Relationship to other criteria_: C-25 is independent of C-23 and C-24. Those criteria require three-scale enumeration in specific diagnostic questions; C-25 requires the principle itself to be documented as a versioning rule so that future criterion authors find explicit guidance rather than reverse-engineering the pattern from examples. An output can earn C-23 PASS and C-24 PASS (three-scale enumeration correctly applied to C-20 and C-22) and C-25 FAIL (principle not stated as a general design rule) simultaneously.

---

**C-26 — C-25 principle includes concrete application inventory**

The Three-Scale Enumeration Principle section (satisfying C-25) must include an explicit application inventory — a named list pairing each criterion that applies the three-scale pattern with the target criterion it covers (e.g., "C-23 applies to C-20, C-24 applies to C-22"). The inventory is the canonical registry for the principle; new entries must be added each time a new three-scale diagnostic criterion is authored.

_Pass condition_: The C-25 principle section contains an application inventory with at least one entry, each entry naming both the applying criterion ID and the target criterion ID. PARTIAL: inventory present but entries lack one of the two required fields (applying criterion ID or target criterion ID). FAIL: no inventory present; only the general principle stated.

_Relationship to other criteria_: C-26 strengthens C-25. C-25 requires the principle to be stated as a general rule; C-26 requires the principle section to include a concrete registry of existing applications. An output can earn C-25 PASS (principle stated as a general rule) and C-26 FAIL (no application inventory) simultaneously. Without C-26, a versioner adding a new criterion must scan every criterion definition to discover which targets already have three-scale diagnostic questions.

---

**C-27 — Regression signals table includes Variation column**

The REGRESSION SIGNALS table (satisfying C-18) includes a Variation column capturing the specific structural element that changed between rounds to produce the verdict delta. The Variation column is distinct from the Mechanism column: Mechanism states the criterion's detection logic; Variation states what changed in the output between rounds.

_Pass condition_: Regression signals table contains at minimum 5 columns including Criterion, Prior Verdict, Current Verdict, Variation, and Mechanism. PARTIAL: table has the 4 required C-18 columns but the Variation column is absent. **auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression table is instantiated).

_Relationship to other criteria_: C-27 strengthens C-18. C-18 requires a named standalone section with a four-column table; C-27 requires a fifth column distinguishing the structural change from the detection mechanism. An output can earn C-18 PASS (four-column table present and named) and C-27 PARTIAL (Variation column absent) simultaneously. Without C-27, regression analysis identifies what degraded and the detection rule, but not what structural variation caused the regression — losing the diagnostic information most useful for the next round's author.
