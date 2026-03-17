Written to `simulations/quest/variations/quest-score-variations-R6-2026-03-14.md`.

---

## Round 6 Variation Map

| V | Axis | Key mechanism | Predicted score |
|---|------|---------------|-----------------|
| **V-01** | Output format | C-19 as standalone imperative sentence in SETUP auto-PASS block, adjacent to C-10 declaration | ~97.50 (C-09, C-14, C-17 FAIL) |
| **V-02** | Phrasing register | C-19 embedded in C-10 diagnostic question row — interrogative form tests whether "near the C-10 definition" + interrogative satisfies C-19 | ~96.67 (C-09 FAIL; C-19 PARTIAL boundary case) |
| **V-03** | Lifecycle emphasis | C-19 as STOP-PRESERVATION checkpoint between SETUP and SCORING — imperative gate forces example to be written before any output opens | ~97.50 (C-09, C-14, C-17 FAIL) |
| **V-04** | V-01 + R5 winners | C-19 + named auto-PASS block (C-16) + mechanism diagnostic questions (C-17) + named REGRESSION SIGNALS section (C-18) | ~99.17 (only C-09 FAIL) |
| **V-05** | Full synthesis | R5 V-05 (100/100) + C-19 preservation rule + C-19 roster row + N_aspirational=12 | 100.00 |

**Key design decisions:**

1. **C-19 form test (V-01 vs V-02):** V-01 is imperative ("must be carried forward"); V-02 is interrogative ("has it been carried forward?"). The rubric says "explicit preservation rule" — V-02 tests whether an interrogative probe in the right location earns PASS or PARTIAL. This is the boundary case for R6.

2. **C-19 enforcement mode test (V-01 vs V-03):** V-01 is a passive declaration; V-03 is a STOP gate that blocks SCORING until the example is written. Both are imperative and in SETUP. Scoring will reveal whether enforcement strength affects C-19 verdict, or both PASS equally.

3. **C-10 carryforward protection:** All 5 variations include a real worked example in FAILURE PATTERNS (instantiated, not a format placeholder). R5's lesson that C-10 is carryforward-fragile is applied — the axis shift is C-19, not C-10.

4. **N_aspirational=12 update:** Every variation uses the v6 formula throughout. Each aspirational FAIL now costs 0.833 pt. V-05's score distribution note calls this out explicitly.
try is added for C-19 in any variation.

3. **C-10 carryforward protection:** R5 found C-10 (worked example in action line) carryforward-fragile — it regressed in V-02, V-03, V-04 when axis shifted. All R6 variations include an instantiated worked example in FAILURE PATTERNS to prevent C-10 FAIL from confounding the C-19 isolation test.

4. **N_aspirational shift:** v6 uses N=12. A single FAIL costs 10/12 = 0.833 pt (vs. 0.909 in v5). Achieving composite >= 99 requires at most one aspirational FAIL.

5. **R5 V-05 inheritance:** V-05 scored 100/100 on v5. The minimal change for 100/100 on v6 is: add C-19 preservation rule to SETUP, add C-19 row with mechanism-specific diagnostic question to roster, update N_aspirational=12 in formula. All 18 prior criteria are inherited unchanged.

---

## V-01 — C-19 Standalone Preservation Rule

**Axis:** Output format — C-19 is addressed as a standalone named sentence in the SETUP block, immediately after the C-10 auto-PASS declaration. The rule is imperative: it states what must happen to the worked example when the rubric is versioned forward. No diagnostic question column (C-14/C-17 not targeted). Named auto-PASS block (C-16) included because it was already passing in R5 V-01 and does not interfere with the C-19 isolation.

**Hypothesis:** A sentence-level imperative preservation rule, placed in SETUP immediately after the C-10 auto-PASS declaration and titled "C-10 Worked-Example Preservation Rule:", is sufficient for C-19 PASS. C-19 does not require a block or section — a named sentence that states "carry verbatim or update for the new axis" and is positioned in the SETUP block satisfies the rubric's location requirement. Expected score: 97.50/100 (C-09, C-14, C-17 FAIL; all others PASS).

---

### SETUP

- **Rubric**: quest-score v6 — 19 criteria (4 essential, 3 recommended, 12 aspirational)
- **Outputs to score**: [list output identifiers]
- **Prior-round scorecard**: [path, or "none provided"]
- **Scoring date**: [date]

### Auto-PASS Conditions

**C-05 auto-PASS when no criterion fails universally across all scored outputs.**
Status for this run: TBD — resolves after all outputs are scored.

**C-07 auto-PASS when no prior-round scorecard is provided to the scorer.**
Status for this run: [set from input — if "none provided" → auto-PASS applies and REGRESSION SIGNALS section should read "C-07 auto-PASS — no prior data"; if path provided → auto-PASS does NOT apply]

**C-08 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-08 auto-PASS).**
Status for this run: TBD — resolves after C-05.

**C-10 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-10 auto-PASS).**
Status for this run: TBD — resolves after C-05.

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action line must be carried forward verbatim from the prior round, or updated to reflect the current round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example with a format instruction placeholder. This rule is in force at every rubric version change.

### Evidence-Ordering Mandate

Column order in every scoring table: **Criterion | Evidence Quote | Verdict**. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13.

### Criterion Roster

| ID | Name | Tier | Auto-PASS Status |
|----|------|------|-----------------|
| C-01 | Per-criterion verdicts present | essential | -- |
| C-02 | Evidence quote for every verdict | essential | -- |
| C-03 | Composite score computed correctly | essential | -- |
| C-04 | Ranked leaderboard present | essential | -- |
| C-05 | Failure patterns surfaced | recommended | TBD |
| C-06 | Excellence signals surfaced | recommended | -- |
| C-07 | Regression signals surfaced | recommended | [set from input] |
| C-08 | Actionable diagnosis in failure patterns | aspirational | TBD |
| C-09 | Score distribution commentary | aspirational | -- |
| C-10 | Worked example in action line | aspirational | TBD |
| C-11 | Auto-PASS rules stated in preamble | aspirational | -- |
| C-12 | Formula reproduced before first output section | aspirational | -- |
| C-13 | Evidence-before-verdict ordering enforced | aspirational | -- |
| C-14 | Per-criterion diagnostic question in roster | aspirational | -- |
| C-15 | Preamble gate instruction present | aspirational | -- |
| C-16 | Named standalone auto-PASS block | aspirational | -- |
| C-17 | Criterion-specific diagnostic questions | aspirational | -- |
| C-18 | Named standalone regression signals section | aspirational | -- |
| C-19 | Worked-example carryforward preservation instruction | aspirational | -- |

### Composite Formula (v6 N values)

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 12.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Do not open any output file until SETUP is fully written.

---

### SCORING

For each output, produce a scoring table with 19 rows (C-01 through C-19):

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 ... | [verbatim or near-verbatim quote from output] | PASS/PARTIAL/FAIL |
| C-02 ... | [quote] | PASS/PARTIAL/FAIL |
| C-03 ... | [quote] | PASS/PARTIAL/FAIL |
| C-04 ... | [quote] | PASS/PARTIAL/FAIL |
| C-05 ... | [quote] | PASS/PARTIAL/FAIL |
| C-06 ... | [quote] | PASS/PARTIAL/FAIL |
| C-07 ... | [quote] | PASS/PARTIAL/FAIL |
| C-08 ... | [quote] | PASS/PARTIAL/FAIL |
| C-09 ... | [quote] | PASS/PARTIAL/FAIL |
| C-10 ... | [quote] | PASS/PARTIAL/FAIL |
| C-11 ... | [quote] | PASS/PARTIAL/FAIL |
| C-12 ... | [quote] | PASS/PARTIAL/FAIL |
| C-13 ... | [quote] | PASS/PARTIAL/FAIL |
| C-14 ... | [quote] | PASS/PARTIAL/FAIL |
| C-15 ... | [quote] | PASS/PARTIAL/FAIL |
| C-16 ... | [quote] | PASS/PARTIAL/FAIL |
| C-17 ... | [quote] | PASS/PARTIAL/FAIL |
| C-18 ... | [quote] | PASS/PARTIAL/FAIL |
| C-19 ... | [quote] | PASS/PARTIAL/FAIL |

Then compute:
- Essential: (C-01 + C-02 + C-03 + C-04) / 4 x 60
- Recommended: (C-05 + C-06 + C-07) / 3 x 30
- Aspirational: (C-08 through C-19) / 12 x 10
- Composite = sum. Golden = all 4 essentials PASS AND composite >= 80.

---

### FAILURE PATTERNS

For each criterion that received FAIL or PARTIAL in every scored output:
- Criterion ID and name
- Pattern evidence (quote from each output showing the failure)
- Action: [verb] [specific artifact filename] [section location] — e.g., "Add a 'C-10 Worked-Example Preservation Rule:' sentence to quest-score.md in the SETUP block immediately after the C-10 auto-PASS declaration, stating that the worked example must be carried forward verbatim or updated to reflect the current round's axis criterion when the rubric is versioned forward — so C-19 is satisfied on every versioning run."

If C-05 auto-PASS: write "C-05 auto-PASS — no universal failures. C-08 auto-PASS. C-10 auto-PASS."

---

### EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by >= one tier:
- Output identifier and criterion ID
- What it did differently (evidence quote from output)

If no excellence signals: write "No excellence signals."

---

### REGRESSION SIGNALS

_Active when prior-round scorecard was provided. If C-07 auto-PASS applies, write "C-07 auto-PASS — no prior data provided. Section present but not applicable."_

For each criterion where the current verdict is lower than the prior-round verdict:

| Criterion | Prior Verdict | Current Verdict | Mechanism |
|-----------|--------------|-----------------|-----------|
| [C-ID name] | [PASS/PARTIAL/FAIL from prior] | [PASS/PARTIAL/FAIL this run] | [why it degraded] |

If no regressions detected: write "No regressions detected — no criterion degraded from prior round."

---

### LEADERBOARD

Rank all outputs from highest to lowest composite score:

| Rank | Output | Score | Golden |
|------|--------|-------|--------|

Ties broken by essential-tier score, then recommended-tier score.

---

## V-02 — C-19 Embedded in C-10 Diagnostic Question

**Axis:** Phrasing register — C-19's preservation mandate is embedded inside the C-10 diagnostic question in the criterion roster. The C-10 row's question explicitly states that the worked example must be carried forward verbatim or updated for this round's axis — interrogative in form but imperative in intent. A full diagnostic question column is included for all 19 criteria (C-14/C-17 axis included as collateral). No separate C-19 preservation sentence appears in the SETUP block outside the roster.

**Hypothesis:** The rubric requires C-19's preservation rule to appear "near the C-10 definition or in the SETUP block." The criterion roster's C-10 row IS near the C-10 definition. However, the C-19 rubric says the rule must be "explicit" and "not implied" — and a diagnostic question that asks "has it been carried forward?" probes for the rule's existence rather than stating it. Risk: a question in interrogative form earns C-19 PARTIAL (preservation concept present but not stated as an imperative rule) rather than PASS. This test isolates whether form (imperative vs. interrogative) affects C-19 verdict. Expected score: ~96.67/100 (C-09, C-19 FAIL or PARTIAL; C-09 FAIL confirmed; C-19 boundary case).

---

### SETUP

- **Rubric**: quest-score v6 — 19 criteria (4 essential, 3 recommended, 12 aspirational)
- **Outputs to score**: [list output identifiers]
- **Prior-round scorecard**: [path, or "none provided"]
- **Scoring date**: [date]

### Auto-PASS Conditions

**C-05 auto-PASS when no criterion fails universally across all scored outputs.**
Status for this run: TBD — resolves after all outputs are scored.

**C-07 auto-PASS when no prior-round scorecard is provided to the scorer.**
Status for this run: [set from input]

**C-08 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-08 auto-PASS).**
Status for this run: TBD — resolves after C-05.

**C-10 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-10 auto-PASS).**
Status for this run: TBD — resolves after C-05.

### Evidence-Ordering Mandate

Column order in every scoring table: **Criterion | Evidence Quote | Verdict**. Evidence quote precedes verdict in every cell. Never write a verdict before its evidence.

### Criterion Roster with Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | essential | -- | Can you count exactly 19 verdict rows (C-01 through C-19) in the scoring table, with none missing or duplicated? |
| C-02 | Evidence quote for every verdict | essential | -- | For the hardest-to-quote criterion this run (likely C-19), is the evidence cell non-empty and verbatim from the scored output — not a template slot or fabricated summary? |
| C-03 | Composite score computed correctly | essential | -- | Does the output use N_aspirational=12? Re-derive the composite from the 19 visible verdict values: does your derivation match the stated score within +-1? |
| C-04 | Ranked leaderboard present | essential | -- | Are all N scored outputs listed exactly once in descending order, with a Golden column, and ties broken by essential-tier score? |
| C-05 | Failure patterns surfaced | recommended | TBD | If any criterion received FAIL or PARTIAL from every output: is it named with a pattern diagnosis? If no universal failure: is auto-PASS declared as resolved text (not TBD)? |
| C-06 | Excellence signals surfaced | recommended | -- | Is at least one output-criterion pair identified where that output is >= one tier above the rest, with a "What it did differently" evidence quote? |
| C-07 | Regression signals surfaced | recommended | [set from input] | If prior-round data was provided: are regressions listed by criterion with prior-round vs. current-round verdict? If no data: is auto-PASS stated as resolved text? |
| C-08 | Actionable diagnosis in failure patterns | aspirational | TBD | For each failure pattern entry, does the action line name a specific artifact filename and a section location within that file — not a generic verb+placeholder? |
| C-09 | Score distribution commentary | aspirational | -- | Does the leaderboard section include a sentence naming min score, max score, and spread, with a calibration implication (whether scores cluster or discriminate)? |
| C-10 | Worked example in action line | aspirational | TBD | Is at least one action line fully instantiated with a real artifact name and exact section — no bracket placeholders? Has the worked example been carried forward verbatim from the prior round, or updated to reflect this round's new axis criterion? A format instruction (e.g., "Action: [verb] [artifact] [section]") without a real instantiated example does not satisfy C-10. |
| C-11 | Auto-PASS rules stated in preamble | aspirational | -- | Does the SETUP contain a block listing C-05, C-07, C-08, C-10 each with their trigger phrases and a status line for this run? |
| C-12 | Formula reproduced before first output section | aspirational | -- | Does the composite formula appear in SETUP with all three N values (N_essential=4, N_recommended=3, N_aspirational=12) before any per-output heading? |
| C-13 | Evidence-before-verdict ordering enforced | aspirational | -- | Is there a written mandate (not just correct column order) stating that evidence precedes verdict — visible in the SETUP text? |
| C-14 | Per-criterion diagnostic question in roster | aspirational | -- | Does the SETUP roster include a Diagnostic Question column with a non-empty question for each of the 19 criteria (C-01 through C-19)? |
| C-15 | Preamble gate instruction present | aspirational | -- | Is there an imperative instruction ("Do not open output files until..." or equivalent) positioned in SETUP before the first output section? |
| C-16 | Named standalone auto-PASS block | aspirational | -- | Does the output contain a dedicated block (not a roster column, not a TBD marker) that names each of C-05, C-07, C-08, C-10 by criterion ID with its trigger phrase spelled out? |
| C-17 | Criterion-specific diagnostic questions | aspirational | -- | For each of the 19 diagnostic questions, does the question interrogate the specific mechanism of that criterion (count, named block, artifact format, explicit declaration) — not a generic probe applicable to any row? |
| C-18 | Named standalone regression signals section | aspirational | -- | Is there a named `### REGRESSION SIGNALS` section in the template body (separate from SETUP and per-output tables), with columns for Criterion | Prior Verdict | Current Verdict | Mechanism? |
| C-19 | Worked-example carryforward preservation instruction | aspirational | -- | Does the C-10 diagnostic question in this roster contain an explicit statement mandating that the worked example be carried forward verbatim or updated for the current round's axis when the rubric is versioned forward? Is the statement imperative (a rule: "must be carried forward"), or merely interrogative (a probe: "has it been carried forward")? |

### Composite Formula (v6 N values)

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 12.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Do not open any output file until SETUP is fully written.

---

### SCORING

For each output, produce a scoring table with 19 rows (C-01 through C-19):

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 ... | [quote] | PASS/PARTIAL/FAIL |
| C-02 ... | [quote] | PASS/PARTIAL/FAIL |
| C-03 ... | [quote] | PASS/PARTIAL/FAIL |
| C-04 ... | [quote] | PASS/PARTIAL/FAIL |
| C-05 ... | [quote] | PASS/PARTIAL/FAIL |
| C-06 ... | [quote] | PASS/PARTIAL/FAIL |
| C-07 ... | [quote] | PASS/PARTIAL/FAIL |
| C-08 ... | [quote] | PASS/PARTIAL/FAIL |
| C-09 ... | [quote] | PASS/PARTIAL/FAIL |
| C-10 ... | [quote] | PASS/PARTIAL/FAIL |
| C-11 ... | [quote] | PASS/PARTIAL/FAIL |
| C-12 ... | [quote] | PASS/PARTIAL/FAIL |
| C-13 ... | [quote] | PASS/PARTIAL/FAIL |
| C-14 ... | [quote] | PASS/PARTIAL/FAIL |
| C-15 ... | [quote] | PASS/PARTIAL/FAIL |
| C-16 ... | [quote] | PASS/PARTIAL/FAIL |
| C-17 ... | [quote] | PASS/PARTIAL/FAIL |
| C-18 ... | [quote] | PASS/PARTIAL/FAIL |
| C-19 ... | [quote] | PASS/PARTIAL/FAIL |

Compute composite per the formula. State Golden status.

---

### FAILURE PATTERNS

For each criterion that received FAIL or PARTIAL in every scored output:
- Criterion ID and name
- Pattern evidence with quotes from each scored output
- Action: [verb] [specific artifact] [section] — fully instantiated, no placeholders — e.g., "Add a 'C-10 Worked-Example Preservation Rule:' sentence to quest-score.md in the SETUP block after the C-10 auto-PASS declaration, stating that the worked example must be carried forward verbatim or updated for the current round's axis when the rubric is versioned forward — so C-19 satisfies the imperative-rule requirement."

If C-05 auto-PASS: write "C-05 auto-PASS — no universal failures. C-08 auto-PASS. C-10 auto-PASS."

---

### EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by >= one tier:
- Output identifier, criterion ID
- What it did differently (evidence quote)

If no signals: write "No excellence signals."

---

### REGRESSION SIGNALS

_This section is mandatory when C-07 auto-PASS does NOT apply (prior scorecard was provided). Write "C-07 auto-PASS — section not applicable" if and only if the C-07 declaration resolves to auto-PASS._

For each criterion where current verdict < prior-round verdict:

| Criterion | Prior Verdict | Current Verdict | Mechanism |
|-----------|--------------|-----------------|-----------|
| [C-ID name] | [prior] | [current] | [mechanism] |

If no regressions: write "No regressions detected."

---

### LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|

Ties broken by essential-tier score, then recommended-tier score.

---

## V-03 — C-19 as STOP-Gated Preservation Checkpoint

**Axis:** Lifecycle emphasis — C-19 is implemented as an imperative STOP-gated checkpoint inserted at the end of SETUP, before any output file is opened. The checkpoint requires the scorer to write or confirm the C-10 worked example before proceeding to SCORING. If the rubric was versioned since the prior round, the checkpoint explicitly requires updating the example to reflect the new axis criterion. The preservation rule is enforced by lifecycle sequencing rather than by a passive standalone sentence.

**Hypothesis:** An imperative STOP gate titled "Step 1.4 — C-10 Worked-Example Preservation Checkpoint" that says "Before proceeding to SCORING: write the C-10 worked example below. If the rubric was versioned since the last run, update it for this round's new axis. Do not proceed until the example is instantiated." satisfies C-19 as a rule "in the SETUP block" — it is in SETUP, it is imperative, it states the preservation requirement. The STOP gate may be structurally stronger than a passive sentence (V-01) because it actively blocks progression rather than stating a rule that can be read and ignored. Expected score: 97.50/100 (C-09, C-14, C-17 FAIL; all others PASS).

---

### PHASE 1: SETUP

**Inputs:**
- **Rubric**: quest-score v6 — 19 criteria (4 essential, 3 recommended, 12 aspirational)
- **Outputs to score**: [list output identifiers]
- **Prior-round scorecard**: [path, or "none provided"]
- **Scoring date**: [date]

**Step 1.1 — Auto-PASS Resolution:**

Declare the status of each auto-PASS condition for this run before proceeding.

**C-05 auto-PASS when no criterion fails universally across all scored outputs.**
Status: TBD — resolves after PHASE 2.

**C-07 auto-PASS when no prior-round scorecard is provided to the scorer.**
Status: [auto-PASS / does not apply — set from input]

**C-08 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-08 auto-PASS).**
Status: TBD — resolves after C-05.

**C-10 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-10 auto-PASS).**
Status: TBD — resolves after C-05.

**Step 1.2 — Composite Formula (v6 N values):**

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 12.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

**Evidence-ordering mandate:** Column order in every scoring table is **Criterion | Evidence Quote | Verdict**. Write the evidence quote first, then the verdict; never the reverse.

**Step 1.3 — Criterion Roster:**

| ID | Name | Tier | Auto-PASS Status |
|----|------|------|-----------------|
| C-01 | Per-criterion verdicts present | essential | -- |
| C-02 | Evidence quote for every verdict | essential | -- |
| C-03 | Composite score computed correctly | essential | -- |
| C-04 | Ranked leaderboard present | essential | -- |
| C-05 | Failure patterns surfaced | recommended | TBD |
| C-06 | Excellence signals surfaced | recommended | -- |
| C-07 | Regression signals surfaced | recommended | [set from input] |
| C-08 | Actionable diagnosis in failure patterns | aspirational | TBD |
| C-09 | Score distribution commentary | aspirational | -- |
| C-10 | Worked example in action line | aspirational | TBD |
| C-11 | Auto-PASS rules stated in preamble | aspirational | -- |
| C-12 | Formula reproduced before first output section | aspirational | -- |
| C-13 | Evidence-before-verdict ordering enforced | aspirational | -- |
| C-14 | Per-criterion diagnostic question in roster | aspirational | -- |
| C-15 | Preamble gate instruction present | aspirational | -- |
| C-16 | Named standalone auto-PASS block | aspirational | -- |
| C-17 | Criterion-specific diagnostic questions | aspirational | -- |
| C-18 | Named standalone regression signals section | aspirational | -- |
| C-19 | Worked-example carryforward preservation instruction | aspirational | -- |

**STOP-1.** Roster complete. Do not open any output file until STOP-1 is passed.

**Step 1.4 — C-10 Worked-Example Preservation Checkpoint:**

STOP-PRESERVATION. Before proceeding to PHASE 2 (SCORING): write the C-10 worked example below. If the rubric has been versioned since the last run (i.e., a new axis criterion was added), update the example to reflect this round's structural gap. Do not replace the example with a format instruction placeholder. The worked example must name a real artifact filename and a real section location.

Write the example here — carry forward from prior round or update for current axis:

> Action: [verb] [artifact filename] [section location] — e.g., "Add a 'C-10 Worked-Example Preservation Rule:' sentence to quest-score.md in the SETUP block after the C-10 auto-PASS declaration, stating that the worked example must be carried forward verbatim or updated for the current round's axis when the rubric is versioned forward — so C-19 is satisfied on every versioning run."

Do not proceed to PHASE 2 until the example above is instantiated with real artifact names from the scored outputs.

---

### PHASE 2: SCORING

For each output, produce a scoring table with 19 rows (C-01 through C-19):

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 ... | [quote] | PASS/PARTIAL/FAIL |
| C-02 ... | [quote] | PASS/PARTIAL/FAIL |
| C-03 ... | [quote] | PASS/PARTIAL/FAIL |
| C-04 ... | [quote] | PASS/PARTIAL/FAIL |
| C-05 ... | [quote] | PASS/PARTIAL/FAIL |
| C-06 ... | [quote] | PASS/PARTIAL/FAIL |
| C-07 ... | [quote] | PASS/PARTIAL/FAIL |
| C-08 ... | [quote] | PASS/PARTIAL/FAIL |
| C-09 ... | [quote] | PASS/PARTIAL/FAIL |
| C-10 ... | [quote] | PASS/PARTIAL/FAIL |
| C-11 ... | [quote] | PASS/PARTIAL/FAIL |
| C-12 ... | [quote] | PASS/PARTIAL/FAIL |
| C-13 ... | [quote] | PASS/PARTIAL/FAIL |
| C-14 ... | [quote] | PASS/PARTIAL/FAIL |
| C-15 ... | [quote] | PASS/PARTIAL/FAIL |
| C-16 ... | [quote] | PASS/PARTIAL/FAIL |
| C-17 ... | [quote] | PASS/PARTIAL/FAIL |
| C-18 ... | [quote] | PASS/PARTIAL/FAIL |
| C-19 ... | [quote] | PASS/PARTIAL/FAIL |

Compute composite and Golden status per the PHASE 1 formula. State composite below each table.

**STOP-2.** All outputs scored. Do not advance to PHASE 3 until all per-output tables are complete.

---

### PHASE 3: SYNTHESIS

Enter PHASE 3 only after STOP-2 is passed. Produce sections in this order: REGRESSION SIGNALS → FAILURE PATTERNS → EXCELLENCE SIGNALS → LEADERBOARD.

**Step 3.1 — Resolve TBD auto-PASS conditions:**
Resolve C-05: did any criterion fail universally? Update C-05, C-08, C-10 status accordingly.

**Step 3.2 — REGRESSION SIGNALS:**

_Mandatory when prior-round scorecard was provided (C-07 auto-PASS does not apply). Write the section in all cases._

For each criterion where current verdict < prior-round verdict:

| Criterion | Prior Verdict | Current Verdict | Mechanism |
|-----------|--------------|-----------------|-----------|
| [C-ID name] | [prior] | [current] | [why it degraded] |

If no regressions detected: write "No regressions detected."
If C-07 auto-PASS applies: write "C-07 auto-PASS — no prior data provided. Section present but empty."

**STOP-3.** Regression detection complete. Proceed to FAILURE PATTERNS.

**Step 3.3 — FAILURE PATTERNS:**

For each criterion that received FAIL or PARTIAL in every scored output:
- Criterion ID and name
- Pattern evidence (quote from each output)
- Action: [verb] [artifact filename] [section location] — fully instantiated

If C-05 auto-PASS: write "C-05 auto-PASS — no universal failures. C-08 auto-PASS. C-10 auto-PASS."

**Step 3.4 — EXCELLENCE SIGNALS:**

For each output-criterion pair where one output outperforms the group by >= one tier:
- Output identifier, criterion ID, what it did differently (evidence quote)

**Step 3.5 — LEADERBOARD:**

| Rank | Output | Score | Golden |
|------|--------|-------|--------|

Ties broken by essential-tier score, then recommended-tier score.

---

## V-04 — Structural Quadruple: C-19 + C-18 + C-17 + C-16

**Axis:** V-01 + R5 winners — adds C-19 standalone preservation rule to the three structural winners from R5 V-04 (named standalone regression signals section, named standalone auto-PASS block, criterion-specific diagnostic questions). All four structural criteria (C-16, C-17, C-18, C-19) addressed simultaneously. Inherits R5 V-04's 98.18/100 baseline; adds C-19 as the fourth axis.

**Hypothesis:** C-16, C-17, C-18, and C-19 address four distinct structural locations — SETUP auto-PASS declarations, criterion roster questions, template body regression section, and SETUP preservation rule — and are orthogonal. A prompt targeting all four via named structures in their respective locations achieves all four PASS simultaneously. C-09 (score distribution commentary) remains the only aspirational FAIL, giving predicted score: 99.17/100 (11/12 aspirational PASS).

---

### SETUP

- **Rubric**: quest-score v6 — 19 criteria (4 essential, 3 recommended, 12 aspirational)
- **Outputs to score**: [list output identifiers]
- **Prior-round scorecard**: [path, or "none provided"]
- **Scoring date**: [date]

### Auto-PASS Conditions

**C-05 auto-PASS when no criterion fails universally across all scored outputs.**
Status for this run: TBD — resolves after all outputs are scored.

**C-07 auto-PASS when no prior-round scorecard is provided to the scorer.**
Status for this run: [set from input]

**C-08 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-08 auto-PASS).**
Status for this run: TBD — resolves after C-05.

**C-10 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-10 auto-PASS).**
Status for this run: TBD — resolves after C-05.

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action line must be carried forward verbatim from the prior round, or updated to reflect the current round's new axis criterion, whenever the rubric is versioned forward. Do not replace the example with a format instruction placeholder. This rule is in force at every rubric version change.

### Evidence-Ordering Mandate

Column order in every scoring table: **Criterion | Evidence Quote | Verdict**. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13.

### Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | essential | -- | Can you count exactly 19 verdict rows (C-01 through C-19) in the scoring table, with none missing or duplicated? |
| C-02 | Evidence quote for every verdict | essential | -- | For the hardest-to-quote criterion this run (likely C-19 — the preservation rule), is the evidence cell non-empty and verbatim from the scored output — not a fabricated summary or template slot? |
| C-03 | Composite score computed correctly | essential | -- | Does the output use N_aspirational=12? Re-derive the composite from the 19 visible verdict values: does your derivation match the stated score within +-1? |
| C-04 | Ranked leaderboard present | essential | -- | Are all N scored outputs listed exactly once in descending order, with a Golden column, and ties broken by essential-tier score then recommended-tier score? |
| C-05 | Failure patterns surfaced | recommended | TBD | If any criterion received FAIL or PARTIAL in every scored output: is it listed with a pattern diagnosis? If none: is C-05 auto-PASS declared as resolved text (not TBD)? |
| C-06 | Excellence signals surfaced | recommended | -- | Is at least one output-criterion pair identified where that output outperforms the group by >= one tier, with a "What it did differently" evidence quote? |
| C-07 | Regression signals surfaced | recommended | [set from input] | If prior-round data exists: are regressions listed by criterion ID with prior-round and current-round verdicts? If no prior data: is C-07 auto-PASS declared as resolved text? |
| C-08 | Actionable diagnosis in failure patterns | aspirational | TBD | Does every failure pattern action line name a specific artifact filename and an exact section location within that file — verb + artifact + location, all three present? |
| C-09 | Score distribution commentary | aspirational | -- | Does the leaderboard section include a sentence naming min score, max score, and spread, with a calibration implication (whether outputs cluster or discriminate)? |
| C-10 | Worked example in action line | aspirational | TBD | Is at least one action line fully instantiated with a real artifact name and exact section location from the scored outputs — no bracket placeholders? Is the example carried forward from the prior round verbatim, or updated for this round's axis per the C-10 preservation rule? |
| C-11 | Auto-PASS rules stated in preamble | aspirational | -- | Does the SETUP contain a block listing C-05, C-07, C-08, C-10 each with their trigger phrases and a status line for this run? |
| C-12 | Formula reproduced before first output section | aspirational | -- | Does the composite formula appear in SETUP with all three N values (N_essential=4, N_recommended=3, N_aspirational=12) before any per-output heading? |
| C-13 | Evidence-before-verdict ordering enforced | aspirational | -- | Is there a written mandate (not just correct column order) stating that evidence quote precedes verdict — visible in the SETUP text? |
| C-14 | Per-criterion diagnostic question in roster | aspirational | -- | Does the SETUP roster include a Diagnostic Question column with a non-empty question for each of the 19 criteria (C-01 through C-19)? |
| C-15 | Preamble gate instruction present | aspirational | -- | Is there an imperative instruction in SETUP ("Do not open output files until..." or equivalent STOP gate) prohibiting output file access until SETUP is complete? |
| C-16 | Named standalone auto-PASS block | aspirational | -- | Does the output contain a dedicated auto-PASS block (not a roster column, not TBD markers) that names each of C-05, C-07, C-08, C-10 by criterion ID with its trigger phrase spelled out? |
| C-17 | Criterion-specific diagnostic questions | aspirational | -- | For each of the 19 diagnostic questions, does the question name the specific mechanism of that criterion (count, named block, artifact format, explicit declaration, verbatim carryforward) — not a generic probe applicable to any row? |
| C-18 | Named standalone regression signals section | aspirational | -- | Is there a named `### REGRESSION SIGNALS` section in the template body (separate from SETUP and per-output tables), with columns for Criterion | Prior Verdict | Current Verdict | Mechanism? |
| C-19 | Worked-example carryforward preservation instruction | aspirational | -- | Is there a standalone imperative preservation rule (not just a diagnostic question) in the SETUP block or near the C-10 definition, stating that the worked example must be carried forward verbatim or updated for the current round's axis when the rubric is versioned forward? |

### Composite Formula (v6 N values)

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 12.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Do not open any output file until SETUP is fully written.

---

### SCORING

For each output, produce a scoring table with 19 rows (C-01 through C-19):

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 ... | [quote] | PASS/PARTIAL/FAIL |
| C-02 ... | [quote] | PASS/PARTIAL/FAIL |
| C-03 ... | [quote] | PASS/PARTIAL/FAIL |
| C-04 ... | [quote] | PASS/PARTIAL/FAIL |
| C-05 ... | [quote] | PASS/PARTIAL/FAIL |
| C-06 ... | [quote] | PASS/PARTIAL/FAIL |
| C-07 ... | [quote] | PASS/PARTIAL/FAIL |
| C-08 ... | [quote] | PASS/PARTIAL/FAIL |
| C-09 ... | [quote] | PASS/PARTIAL/FAIL |
| C-10 ... | [quote] | PASS/PARTIAL/FAIL |
| C-11 ... | [quote] | PASS/PARTIAL/FAIL |
| C-12 ... | [quote] | PASS/PARTIAL/FAIL |
| C-13 ... | [quote] | PASS/PARTIAL/FAIL |
| C-14 ... | [quote] | PASS/PARTIAL/FAIL |
| C-15 ... | [quote] | PASS/PARTIAL/FAIL |
| C-16 ... | [quote] | PASS/PARTIAL/FAIL |
| C-17 ... | [quote] | PASS/PARTIAL/FAIL |
| C-18 ... | [quote] | PASS/PARTIAL/FAIL |
| C-19 ... | [quote] | PASS/PARTIAL/FAIL |

Compute composite and Golden status.

---

### FAILURE PATTERNS

For each criterion receiving FAIL or PARTIAL in every scored output:
- Criterion ID and name
- Pattern evidence (quote from each output)
- Action: [verb] [specific artifact filename] [exact section location] — no placeholders

Example of a fully instantiated action line: "Add a 'Score distribution note:' instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score, spread, and whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread) — so C-09 is satisfied on every run."

If C-05 auto-PASS: write "C-05 auto-PASS — no universal failures. C-08 auto-PASS. C-10 auto-PASS."

---

### EXCELLENCE SIGNALS

For each output-criterion pair outperforming the group by >= one tier:
- Output identifier, criterion ID, what it did differently (evidence quote)

---

### REGRESSION SIGNALS

_Active when prior-round scorecard was provided. Write the section in all cases; state "C-07 auto-PASS — no prior data" only if auto-PASS applies._

| Criterion | Prior Verdict | Current Verdict | Mechanism |
|-----------|--------------|-----------------|-----------|

If no regressions: write "No regressions detected."

---

### LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|

Ties broken by essential-tier score, then recommended-tier score.

---

## V-05 — Full Synthesis

**Axis:** All axes — builds on R5 V-05 (100/100) with the three structural changes required for 100/100 on v6: (1) C-19 standalone preservation rule in SETUP, (2) C-19 row added to criterion roster with mechanism-specific diagnostic question, (3) N_aspirational updated from 11 to 12 in formula. All R5 V-05 mechanisms retained unchanged: three-phase STOP gates, named auto-PASS block (C-16), mechanism-level diagnostic questions (C-17), evidence-before-verdict mandate (C-13), no-placeholder mandate, named REGRESSION SIGNALS section (C-18), worked example in FAILURE PATTERNS (C-10), score distribution calibration note (C-09).

**Hypothesis:** A template that achieved 100/100 on v5 requires exactly three structural changes to achieve 100/100 on v6. C-19 is orthogonal to all 18 prior criteria — adding it to SETUP and to the roster does not disturb any prior criterion's PASS. The formula N update is mechanical. Predicted score: 100/100.

---

### PHASE 1: PREAMBLE

**Inputs:**
- **Rubric**: quest-score v6 — 19 criteria (4 essential, 3 recommended, 12 aspirational)
- **Outputs to score**: [list output identifiers]
- **Prior-round scorecard**: [path, or "none provided"]
- **Scoring date**: [date]

**Step 1.1 — Auto-PASS Conditions:**

Write each declaration in full. These are the auto-PASS conditions for this run.

**C-05 auto-PASS when no criterion fails universally across all scored outputs.**
Status for this run: TBD — resolves after PHASE 2 completes.

**C-07 auto-PASS when no prior-round scorecard is provided to the scorer.**
Status for this run: [set from input — "none provided" → auto-PASS applies; path given → does not apply. When does not apply, the `### REGRESSION SIGNALS` section in PHASE 3 must be populated with structured comparison rows.]

**C-08 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-08 auto-PASS).**
Status for this run: TBD — resolves after C-05.

**C-10 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-10 auto-PASS).**
Status for this run: TBD — resolves after C-05.

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action line must be carried forward verbatim from the prior round, or updated to reflect the current round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example with a format instruction placeholder. This rule is in force at every rubric version change and applies regardless of whether C-10 auto-PASS fires this run.

**STOP-1.** Declarations complete. Proceed to Step 1.2.

**Step 1.2 — Formula and Evidence Mandate:**

**Composite Formula (v6 N values):**

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 12.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

**Evidence-ordering mandate:** In every scoring table, column order is **Criterion | Evidence Quote | Verdict**. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names and exact section locations visible in the scored outputs. Placeholders such as `[artifact name]`, `[section]`, or `[add here]` are not permitted.

**STOP-2.** Formula and mandates written. Proceed to Step 1.3.

**Step 1.3 — Criterion Roster with Mechanism-Level Diagnostic Questions:**

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | essential | -- | Can you count exactly 19 verdict rows (C-01 through C-19) in the scoring table, with none missing or duplicated? |
| C-02 | Evidence quote for every verdict | essential | -- | For the hardest-to-quote criterion this run (likely C-19 — the preservation rule), is the evidence quote verbatim from the scored output — not a fabricated summary or template slot? |
| C-03 | Composite score computed correctly | essential | -- | Does the output use N_aspirational=12? Can you re-derive the composite from the 19 visible verdict values within +-1? |
| C-04 | Ranked leaderboard present | essential | -- | Are all N scored outputs listed exactly once, ranked highest to lowest, with a Golden column, and ties broken by essential-tier score then recommended-tier score? |
| C-05 | Failure patterns surfaced | recommended | TBD | If any criterion received FAIL or PARTIAL in every scored output: is it listed with a pattern diagnosis? If none: is C-05 auto-PASS declared as resolved text (not TBD)? |
| C-06 | Excellence signals surfaced | recommended | -- | Is at least one output-criterion pair identified where that output outperforms the group by >= one tier, with a "What it did differently" evidence quote? |
| C-07 | Regression signals surfaced | recommended | [set from input] | If prior-round data exists: are regressions listed by criterion ID with prior-round and current-round verdicts? If no prior data: is C-07 auto-PASS declared as resolved text? |
| C-08 | Actionable diagnosis in failure patterns | aspirational | TBD | Does every failure pattern action line name a specific artifact filename and an exact section location within that file — verb + artifact + location, all three present? |
| C-09 | Score distribution commentary | aspirational | -- | Does the LEADERBOARD section include a sentence naming min score, max score, and spread, plus a calibration implication (whether outputs cluster or discriminate)? |
| C-10 | Worked example in action line | aspirational | TBD | Is at least one action line fully instantiated with a real artifact name and section location from the scored outputs — no bracket placeholders? Is the example carried forward verbatim from the prior round, or updated for this round's axis per the C-10 preservation rule in Step 1.1? |
| C-11 | Auto-PASS rules stated in preamble | aspirational | -- | Does PHASE 1 contain a block that lists C-05, C-07, C-08, C-10 each with their trigger phrase and a status line for this run? |
| C-12 | Formula reproduced before first output section | aspirational | -- | Does the composite formula appear in PHASE 1 with all three N values (N_essential=4, N_recommended=3, N_aspirational=12) before any per-output heading? |
| C-13 | Evidence-before-verdict ordering enforced | aspirational | -- | Is there a written mandate in PHASE 1 (not just correct column order in the tables) stating that evidence quote precedes verdict? |
| C-14 | Per-criterion diagnostic question in roster | aspirational | -- | Does the PHASE 1 roster include a Diagnostic Question column with a non-empty question for each of the 19 criteria (C-01 through C-19)? |
| C-15 | Preamble gate instruction present | aspirational | -- | Is there an imperative instruction in PHASE 1 ("Do not open output files until..." or equivalent STOP gate) prohibiting output file access until PHASE 1 is complete? |
| C-16 | Named standalone auto-PASS block | aspirational | -- | Does PHASE 1 contain a dedicated auto-PASS block (not a roster column, not TBD markers) that names each of C-05, C-07, C-08, C-10 by criterion ID with trigger phrase spelled out? |
| C-17 | Criterion-specific diagnostic questions | aspirational | -- | For each of the 19 diagnostic questions, does the question name the specific mechanism of that criterion (count, named block, artifact format, explicit declaration, verbatim carryforward) — not a generic probe applicable to any row? |
| C-18 | Named standalone regression signals section | aspirational | -- | Is there a named `### REGRESSION SIGNALS` section in the template body (separate from SETUP and per-output tables) in PHASE 3, with columns for Criterion | Prior Verdict | Current Verdict | Mechanism? |
| C-19 | Worked-example carryforward preservation instruction | aspirational | -- | Is there a standalone imperative preservation rule in PHASE 1 (near the C-10 auto-PASS declaration or the C-10 roster row) stating that the worked example must be carried forward verbatim or updated for the current round's axis when the rubric is versioned forward? Is it a rule (imperative: "must be carried forward"), not merely an interrogative probe? |

**STOP-3.** PHASE 1 complete. Do not open any output file until STOP-3 is passed.

---

### PHASE 2: SCORING

For each output, produce a scoring table with 19 rows (C-01 through C-19):

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-02 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-03 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-04 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-05 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-06 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-07 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-08 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-09 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-10 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-11 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-12 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-13 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-14 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-15 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-16 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-17 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-18 ... | [verbatim quote] | PASS/PARTIAL/FAIL |
| C-19 ... | [verbatim quote] | PASS/PARTIAL/FAIL |

Below each table, compute:
- Essential: (C-01 + C-02 + C-03 + C-04) / 4 x 60 = ___ pts
- Recommended: (C-05 + C-06 + C-07) / 3 x 30 = ___ pts
- Aspirational: (C-08 + C-09 + C-10 + C-11 + C-12 + C-13 + C-14 + C-15 + C-16 + C-17 + C-18 + C-19) / 12 x 10 = ___ pts
- Composite: ___ / 100
- Golden: yes / no

---

### PHASE 3: SYNTHESIS

Resolve TBD auto-PASS conditions (C-05, C-08, C-10) from PHASE 2 results. Produce sections in order.

**FAILURE PATTERNS**

For each criterion receiving FAIL or PARTIAL in every scored output:
- Criterion ID and name
- Pattern evidence (quote from each output showing the failure)
- Action: [verb] [artifact filename] [section location] — fully instantiated, no placeholders

Example of a fully instantiated action line: "Add a 'C-10 Worked-Example Preservation Rule:' sentence to quest-score.md in the SETUP block after the C-10 auto-PASS declaration, stating that the worked example must be carried forward verbatim or updated for the current round's new axis criterion when the rubric is versioned forward — so C-19 is satisfied on every versioning run."

If C-05 auto-PASS: write "C-05 auto-PASS — no universal failures. C-08 auto-PASS. C-10 auto-PASS."

**EXCELLENCE SIGNALS**

For each output-criterion pair outperforming the group by >= one tier:
- Output identifier, criterion ID
- What it did differently (evidence quote)

If no excellence signals: write "No excellence signals."

**REGRESSION SIGNALS**

_Write this section in all cases. Populate with structured rows when prior data exists._

| Criterion | Prior Verdict | Current Verdict | Mechanism |
|-----------|--------------|-----------------|-----------|
| [criterion] | [prior] | [current] | [mechanism] |

If no regressions: write "No regressions detected."
If C-07 auto-PASS: write "C-07 auto-PASS — no prior data. No regressions to detect."

**LEADERBOARD**

| Rank | Output | Score | Golden |
|------|--------|-------|--------|

Ties broken by essential-tier score, then recommended-tier score.

Score distribution note: State min score, max score, and spread. State whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread, suggesting the rubric is well-differentiated). Note that N_aspirational=12 reduces the per-criterion aspirational weight to 0.833 pt (vs. 0.909 pt in v5), meaning a single aspirational FAIL now costs slightly less — but achieving composite >= 99 requires at most one aspirational FAIL.
