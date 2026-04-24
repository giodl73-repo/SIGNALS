That was a background search task that completed — it just returned the path to the R4 variations file I had already used. Nothing new to act on.
tional=11:

---

| V | Axis | Key mechanism |
|---|------|---------------|
| **V-01** | Output format | Named standalone `### REGRESSION SIGNALS` section in template body — C-18 axis alone; parallel to R4 V-01's named auto-PASS block |
| **V-02** | Phrasing register | C-07/C-18 coupling declaration — C-07 auto-PASS block in SETUP explicitly references and activates C-18 section; C-18 axis via preamble coupling |
| **V-03** | Lifecycle emphasis | REGRESSION SIGNALS as first-class STOP-gated phase in a three-phase SYNTHESIS structure — C-18 via lifecycle enforcement |
| **V-04** | V-01 + R4 winners | Named regression section (C-18) + named auto-PASS block (C-16) + mechanism-level diagnostic questions (C-17) — structural trinity |
| **V-05** | Full synthesis | All axes: C-18 + C-16 + C-17 + three STOP gates + evidence-before-verdict mandate + score distribution note; builds on R4 V-05 (100/100) with one structural addition |

**Key design decisions for R5:**

1. **C-18 isolation (V-01, V-02, V-03):** Three single-axis approaches test whether C-18 PASS comes from: (a) a named section in the body alone, (b) SETUP coupling that activates the section, or (c) lifecycle elevation with a STOP gate.

2. **C-07/C-18 dependence test (V-02):** If the C-07 named declaration explicitly references the C-18 section, does that couple their verdicts? C-07 PASS should not require C-18 PASS — they are distinct criteria. V-02 tests whether preamble coupling creates a false dependency.

3. **N_aspirational shift:** v5 uses N=11. A single FAIL costs 0.91 pt (vs. 1.0 pt in v4). The golden composite threshold is marginally more achievable. A perfect aspirational run is still required for composite > 99.

4. **R4 V-05 inheritance:** V-05 scored 100/100 on v4. The only change needed for 100/100 on v5 is adding C-18 PASS. All other criteria were already satisfied. V-05 here makes that minimal addition.

5. **Regression prediction:** All variations should inherit C-16 and C-17 behavior from R4. V-01 should mirror R4 V-01 on C-16 (PASS) and C-17 (FAIL). V-04 and V-05 should both PASS C-16 and C-17.

---

## V-01 — Named Standalone REGRESSION SIGNALS Section

**Axis:** Output format — add a named `### REGRESSION SIGNALS` section to the template body as a structurally mandated section, separate from SETUP and from per-output scoring tables. C-18 axis alone.

**Hypothesis:** C-18 requires a dedicated named section (not inline commentary or SETUP notes) that contains structured comparison entries keyed to criterion ID, prior verdict, and current verdict. A standalone `### REGRESSION SIGNALS` section after EXCELLENCE SIGNALS, gated by C-07 auto-PASS status, is sufficient for C-18 PASS without requiring a lifecycle phase or preamble coupling.

---

### SETUP

- **Rubric**: quest-score v5 — 18 criteria (4 essential, 3 recommended, 11 aspirational)
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

### Composite Formula (v5 N values)

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 11 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 11.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Do not open any output file until SETUP is fully written.

---

### SCORING

For each output, produce a scoring table with 18 rows (C-01 through C-18):

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 ... | [verbatim or near-verbatim quote from output] | PASS/PARTIAL/FAIL |
| C-02 ... | [quote] | PASS/PARTIAL/FAIL |
| ... | | |
| C-18 ... | [quote] | PASS/PARTIAL/FAIL |

Then compute:
- Essential: (C-01 + C-02 + C-03 + C-04) / 4 x 60
- Recommended: (C-05 + C-06 + C-07) / 3 x 30
- Aspirational: (C-08 through C-18) / 11 x 10
- Composite = sum. Golden = all 4 essentials PASS AND composite >= 80.

---

### FAILURE PATTERNS

For each criterion that received FAIL or PARTIAL in every scored output:
- Criterion ID and name
- Pattern evidence (quote from each output showing the failure)
- Action: [verb] [specific artifact filename] [section location] — e.g., "Add a named `### REGRESSION SIGNALS` section to quest-score.md after the EXCELLENCE SIGNALS section, with columns for Criterion | Prior Verdict | Current Verdict | Mechanism"

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

## V-02 — C-07/C-18 Coupling Declaration

**Axis:** Phrasing register — the C-07 auto-PASS declaration in SETUP explicitly names and activates the C-18 section. The declaration is written to make the section's mandatory status unmistakable when C-07 auto-PASS does not apply. C-18 axis via preamble coupling.

**Hypothesis:** Embedding the C-18 section reference inside the C-07 named declaration creates structural coupling: the same instruction that declares C-07's auto-PASS condition also mandates the `### REGRESSION SIGNALS` section when prior data exists. This produces C-18 PASS without a standalone C-18 declaration, by making C-18 a consequence of the C-07 block. Risk: the coupling may cause the scorer to conflate C-07 and C-18, under-filling the REGRESSION SIGNALS section if C-07 passes through auto-PASS.

---

### SETUP

- **Rubric**: quest-score v5 — 18 criteria (4 essential, 3 recommended, 11 aspirational)
- **Outputs to score**: [list output identifiers]
- **Prior-round scorecard**: [path, or "none provided"]
- **Scoring date**: [date]

### Auto-PASS Conditions

**C-05 auto-PASS when no criterion fails universally across all scored outputs.**
Status for this run: TBD — resolves after all outputs are scored.

**C-07 auto-PASS when no prior-round scorecard is provided to the scorer.**
Status for this run: [set from input]
When C-07 auto-PASS does NOT apply (prior scorecard exists): the `### REGRESSION SIGNALS` section defined in this template body is mandatory. It must contain one structured row per regressed criterion, keyed to criterion ID, prior-round verdict, current verdict, and mechanism. The section must appear as a standalone named section, not as inline commentary within per-output scoring tables.

**C-08 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-08 auto-PASS).**
Status for this run: TBD — resolves after C-05.

**C-10 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-10 auto-PASS).**
Status for this run: TBD — resolves after C-05.

### Evidence-Ordering Mandate

Column order in every scoring table: **Criterion | Evidence Quote | Verdict**. Evidence quote precedes verdict in every cell. Never write a verdict before its evidence.

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

### Composite Formula (v5 N values)

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 11 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 11.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Do not open any output file until SETUP is fully written.

---

### SCORING

For each output, produce a scoring table with 18 rows (C-01 through C-18):

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 ... | [quote] | PASS/PARTIAL/FAIL |
| ... | | |
| C-18 ... | [quote] | PASS/PARTIAL/FAIL |

Compute composite per the formula. State Golden status.

---

### FAILURE PATTERNS

For each criterion that received FAIL or PARTIAL in every scored output:
- Criterion ID and name
- Pattern evidence with quotes from each scored output
- Action: [verb] [specific artifact] [section] — fully instantiated, no placeholders

If C-05 auto-PASS: write "C-05 auto-PASS — no universal failures. C-08 auto-PASS. C-10 auto-PASS."

---

### EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by >= one tier:
- Output identifier, criterion ID
- What it did differently (evidence quote)

If no signals: write "No excellence signals."

---

### REGRESSION SIGNALS

_This section is mandatory when C-07 auto-PASS does NOT apply (prior scorecard was provided), per the C-07 declaration in SETUP. Write "C-07 auto-PASS — section not applicable" if and only if the C-07 declaration resolves to auto-PASS._

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

## V-03 — REGRESSION SIGNALS as First-Class Lifecycle Phase

**Axis:** Lifecycle emphasis — the scoring template is structured as three named phases: PHASE 1 (SETUP), PHASE 2 (SCORING), PHASE 3 (SYNTHESIS). PHASE 3 is gated behind STOP-3 and begins with regression detection before proceeding to leaderboard and aggregate analysis. Regression detection is a mandatory first step of the SYNTHESIS phase, not a section that can be deferred or skipped.

**Hypothesis:** Elevating REGRESSION SIGNALS to a first-class STOP-gated phase (rather than a body section that could be skipped) is a stronger structural variant of C-18 than a named section alone. The STOP gate forces structured regression comparison before LEADERBOARD can be produced, preventing the implicit-commentary failure mode seen in R4.

---

### PHASE 1: SETUP

**Inputs:**
- **Rubric**: quest-score v5 — 18 criteria (4 essential, 3 recommended, 11 aspirational)
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

**Step 1.2 — Composite Formula (v5 N values):**

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 11 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 11.
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

**STOP-1.** PHASE 1 complete. Do not open any output file until STOP-1 is passed.

---

### PHASE 2: SCORING

For each output, produce a scoring table with 18 rows (C-01 through C-18):

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 ... | [quote] | PASS/PARTIAL/FAIL |
| ... | | |
| C-18 ... | [quote] | PASS/PARTIAL/FAIL |

Compute composite and Golden status per the PHASE 1 formula. State composite below each table.

**STOP-2.** All outputs scored. Do not advance to PHASE 3 until all per-output tables are complete.

---

### PHASE 3: SYNTHESIS

Enter PHASE 3 only after STOP-2 is passed. Produce sections in this order: REGRESSION SIGNALS -> FAILURE PATTERNS -> EXCELLENCE SIGNALS -> LEADERBOARD.

**Step 3.1 — Resolve TBD auto-PASS conditions:**
Resolve C-05: did any criterion fail universally? Update C-05, C-08, C-10 status accordingly.

**Step 3.2 — REGRESSION SIGNALS:**

_Mandatory when prior-round scorecard was provided (C-07 auto-PASS does not apply). Write the section in all cases._

Compare each criterion's current verdict distribution to its prior-round median verdict. For each criterion where current < prior:

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

## V-04 — Structural Trinity: C-18 + C-16 + C-17

**Axis:** V-01 + R4 winners — combines the three "strengthening" aspirational criteria: named standalone regression signals section (C-18), named standalone auto-PASS block (C-16), and criterion-specific diagnostic questions (C-17). All three structural gaps addressed simultaneously.

**Hypothesis:** C-16, C-17, and C-18 address three distinct structural locations — SETUP declarations, criterion roster questions, and template body sections — and are orthogonal: satisfying one does not interfere with satisfying the others. A prompt that explicitly targets all three via named structures in their respective locations achieves all three PASS simultaneously.

---

### SETUP

- **Rubric**: quest-score v5 — 18 criteria (4 essential, 3 recommended, 11 aspirational)
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

Column order in every scoring table: **Criterion | Evidence Quote | Verdict**. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13.

### Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | essential | -- | Can you count exactly 18 verdict rows (C-01 through C-18) in the scoring table, with none missing or duplicated? |
| C-02 | Evidence quote for every verdict | essential | -- | In the row for C-18 (the hardest to quote), is the evidence cell non-empty and verbatim from the scored output — not a template slot or fabricated summary? |
| C-03 | Composite score computed correctly | essential | -- | Does the output use N_aspirational=11? Re-derive the composite from the 18 visible verdict values: does your derivation match the stated score within +-1? |
| C-04 | Ranked leaderboard present | essential | -- | Are all N scored outputs listed exactly once in descending order, with a Golden column, and ties broken by essential-tier score? |
| C-05 | Failure patterns surfaced | recommended | TBD | If any criterion received FAIL or PARTIAL from every output: is it named with a pattern diagnosis? If no universal failure: is auto-PASS declared explicitly as resolved text (not TBD)? |
| C-06 | Excellence signals surfaced | recommended | -- | Is at least one output-criterion pair identified where that output is >= one tier above the rest of the group, with a "What it did differently" evidence quote? |
| C-07 | Regression signals surfaced | recommended | [set from input] | If prior-round data was provided: are regressions listed by criterion with prior-round vs. current-round verdict? If no data: is auto-PASS stated as resolved text? |
| C-08 | Actionable diagnosis in failure patterns | aspirational | TBD | For each failure pattern entry, does the action line name a specific artifact filename and a section location within that file — not a generic verb+placeholder? |
| C-09 | Score distribution commentary | aspirational | -- | Does the leaderboard section include a sentence naming min score, max score, and spread, with a calibration implication (e.g., whether scores cluster or discriminate)? |
| C-10 | Worked example in action line | aspirational | TBD | Is at least one action line fully instantiated with a real artifact name and exact section — no bracket placeholders? |
| C-11 | Auto-PASS rules stated in preamble | aspirational | -- | Does the SETUP contain a block listing C-05, C-07, C-08, C-10 each with their trigger phrases and a status line for this run? |
| C-12 | Formula reproduced before first output section | aspirational | -- | Does the composite formula appear in SETUP with all three N values (N_essential=4, N_recommended=3, N_aspirational=11) before any per-output heading? |
| C-13 | Evidence-before-verdict ordering enforced | aspirational | -- | Is there a written mandate (not just correct column order) stating that evidence precedes verdict — visible in the SETUP text? |
| C-14 | Per-criterion diagnostic question in roster | aspirational | -- | Does the SETUP roster include a Diagnostic Question column with a non-empty question for each of the 18 criteria? |
| C-15 | Preamble gate instruction present | aspirational | -- | Is there an imperative instruction ("Do not open output files until..." or equivalent) positioned in SETUP before the first output section — imperative in tone, not advisory? |
| C-16 | Named standalone auto-PASS block | aspirational | -- | Does the output contain a dedicated block (not a column in the roster, not a TBD marker) that names each of C-05, C-07, C-08, C-10 by criterion ID with its trigger phrase spelled out? |
| C-17 | Criterion-specific diagnostic questions | aspirational | -- | For each of the 18 diagnostic questions, does the question interrogate the specific mechanism of that criterion (count, named block, artifact format, explicit declaration) — not a generic probe applicable to any row? |
| C-18 | Named standalone regression signals section | aspirational | -- | Is there a named `### REGRESSION SIGNALS` section in the template body (separate from SETUP and per-output tables), with columns for Criterion | Prior Verdict | Current Verdict | Mechanism? |

### Composite Formula (v5 N values)

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 11 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 11.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Do not open any output file until SETUP is fully written.

---

### SCORING

For each output, produce a scoring table with 18 rows:

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 ... | [quote] | PASS/PARTIAL/FAIL |
| ... | | |
| C-18 ... | [quote] | PASS/PARTIAL/FAIL |

Compute composite and Golden status.

---

### FAILURE PATTERNS

For each criterion receiving FAIL or PARTIAL in every scored output:
- Criterion ID and name
- Pattern evidence (quote from each output)
- Action: [verb] [specific artifact filename] [exact section location] — no placeholders

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

**Axis:** All axes — builds on R4 V-05 (100/100 on v4) with the single structural addition required for 100/100 on v5: a named standalone `### REGRESSION SIGNALS` section (C-18). Updates N_aspirational to 11. Adds C-18 diagnostic question to criterion roster (C-17 axis). Retains all R4 V-05 mechanisms: named auto-PASS block (C-16), mechanism-level diagnostic questions (C-17), three-phase STOP gates, evidence-before-verdict mandate, no-placeholder mandate, score distribution calibration note.

**Hypothesis:** A template that achieved 100/100 on v4 requires exactly one structural addition (the named `### REGRESSION SIGNALS` section in the template body with structured comparison rows) to achieve 100/100 on v5. No existing criterion degrades. The C-18 mechanism is orthogonal to all 17 prior criteria.

---

### PHASE 1: PREAMBLE

**Inputs:**
- **Rubric**: quest-score v5 — 18 criteria (4 essential, 3 recommended, 11 aspirational)
- **Outputs to score**: [list output identifiers]
- **Prior-round scorecard**: [path, or "none provided"]
- **Scoring date**: [date]

**Step 1.1 — Auto-PASS Conditions:**

Write each declaration in full. These are the auto-PASS conditions for this run.

**C-05 auto-PASS when no criterion fails universally across all scored outputs.**
Status for this run: TBD — resolves after PHASE 2 completes.

**C-07 auto-PASS when no prior-round scorecard is provided to the scorer.**
Status for this run: [set from input — "none provided" -> auto-PASS applies; path given -> does not apply. When does not apply, the `### REGRESSION SIGNALS` section in PHASE 3 must be populated with structured comparison rows.]

**C-08 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-08 auto-PASS).**
Status for this run: TBD — resolves after C-05.

**C-10 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-10 auto-PASS).**
Status for this run: TBD — resolves after C-05.

**STOP-1.** Declarations complete. Proceed to Step 1.2.

**Step 1.2 — Formula and Evidence Mandate:**

**Composite Formula (v5 N values):**

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 11 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 11.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

**Evidence-ordering mandate:** In every scoring table, column order is **Criterion | Evidence Quote | Verdict**. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names and exact section locations visible in the scored outputs. Placeholders such as `[artifact name]`, `[section]`, or `[add here]` are not permitted.

**STOP-2.** Formula and mandates written. Proceed to Step 1.3.

**Step 1.3 — Criterion Roster with Mechanism-Level Diagnostic Questions:**

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | essential | -- | Can you count exactly 18 verdict rows (C-01 through C-18) in the scoring table, with none missing or duplicated? |
| C-02 | Evidence quote for every verdict | essential | -- | For the most mechanism-specific criterion (pick C-16, C-17, or C-18), is the evidence quote verbatim from the scored output — not a fabricated summary or template slot? |
| C-03 | Composite score computed correctly | essential | -- | Does the output use N_aspirational=11? Can you re-derive the composite from the 18 visible verdict values within +-1? |
| C-04 | Ranked leaderboard present | essential | -- | Are all N scored outputs listed exactly once, ranked highest to lowest, with a Golden column, and ties broken by essential-tier score then recommended-tier score? |
| C-05 | Failure patterns surfaced | recommended | TBD | If any criterion received FAIL or PARTIAL in every scored output: is it listed with a pattern diagnosis? If none: is C-05 auto-PASS declared as resolved text (not TBD)? |
| C-06 | Excellence signals surfaced | recommended | -- | Is at least one output-criterion pair identified where that output outperforms the group by >= one tier, with a "What it did differently" evidence quote? |
| C-07 | Regression signals surfaced | recommended | [set from input] | If prior-round data exists: are regressions listed by criterion ID with prior-round and current-round verdicts? If no prior data: is C-07 auto-PASS declared as resolved text? |
| C-08 | Actionable diagnosis in failure patterns | aspirational | TBD | Does every failure pattern action line name a specific artifact filename and an exact section location within that file — verb + artifact + location, all three present? |
| C-09 | Score distribution commentary | aspirational | -- | Does the LEADERBOARD section include a sentence naming min score, max score, and spread, plus a calibration implication (whether outputs cluster or discriminate)? |
| C-10 | Worked example in action line | aspirational | TBD | Is at least one action line fully instantiated with a real artifact name and section location from the scored outputs — no bracket placeholders? |
| C-11 | Auto-PASS rules stated in preamble | aspirational | -- | Does PHASE 1 contain a block that lists C-05, C-07, C-08, C-10 each with their trigger phrase and a status line for this run? |
| C-12 | Formula reproduced before first output section | aspirational | -- | Does the composite formula appear in PHASE 1 with all three N values (N_essential=4, N_recommended=3, N_aspirational=11) before any per-output heading? |
| C-13 | Evidence-before-verdict ordering enforced | aspirational | -- | Is there a written mandate in PHASE 1 (not just correct column order in the tables) stating that evidence quote precedes verdict? |
| C-14 | Per-criterion diagnostic question in roster | aspirational | -- | Does the PHASE 1 roster include a Diagnostic Question column with a non-empty question for each of the 18 criteria (C-01 through C-18)? |
| C-15 | Preamble gate instruction present | aspirational | -- | Is there an imperative instruction in PHASE 1 ("Do not open output files until..." or equivalent STOP gate) prohibiting output file access until PHASE 1 is complete? |
| C-16 | Named standalone auto-PASS block | aspirational | -- | Does PHASE 1 contain a dedicated auto-PASS block (not a roster column, not TBD markers) that names each of C-05, C-07, C-08, C-10 by criterion ID with trigger phrase spelled out? |
| C-17 | Criterion-specific diagnostic questions | aspirational | -- | For each of the 18 diagnostic questions, does the question name the specific mechanism of that criterion (count, named block, explicit declaration, artifact format) — not a generic probe applicable to any row? |
| C-18 | Named standalone regression signals section | aspirational | -- | Is there a named `### REGRESSION SIGNALS` section in the template body (separate from SETUP and per-output tables) in PHASE 3, with columns for Criterion | Prior Verdict | Current Verdict | Mechanism? |

**STOP-3.** PHASE 1 complete. Do not open any output file until STOP-3 is passed.

---

### PHASE 2: SCORING

For each output, produce a scoring table with 18 rows (C-01 through C-18):

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

Below each table, compute:
- Essential: (C-01 + C-02 + C-03 + C-04) / 4 x 60 = ___ pts
- Recommended: (C-05 + C-06 + C-07) / 3 x 30 = ___ pts
- Aspirational: (C-08 + C-09 + C-10 + C-11 + C-12 + C-13 + C-14 + C-15 + C-16 + C-17 + C-18) / 11 x 10 = ___ pts
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

Example of a fully instantiated action line: "Add a named `### REGRESSION SIGNALS` section to quest-score.md after the EXCELLENCE SIGNALS section, with four columns: Criterion | Prior Verdict | Current Verdict | Mechanism — so C-18 is satisfied on every run where prior data exists."

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

Score distribution note: State min score, max score, and spread. State whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread, suggesting the rubric is well-differentiated). Note that N_aspirational=11 reduces the per-criterion aspirational weight to 0.91 pt (vs. 1.0 pt in v4), meaning a single aspirational FAIL now costs slightly less — but achieving composite >= 99 still requires all aspirational criteria to PASS.
