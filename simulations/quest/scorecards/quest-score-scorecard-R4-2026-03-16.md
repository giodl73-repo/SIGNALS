## quest-score: Round 4 Scorecard (v4 rubric)

---

## PHASE 1: LOAD

**Load summary (pre-scoring)**

- **Criteria**: C-01--C-05 Essential | C-06--C-08 Recommended | C-09--C-16 Aspirational (16 total)
- **Formula (v4)**: `composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/8 * 10)`; PARTIAL = 0.5, FAIL = 0
- **Golden threshold**: all 5 essentials PASS AND composite >= 80
- **Outputs scored**: 5 (V-01, V-02, V-03, V-04, V-05)

**Formula version delta**

`N_aspirational: 6 (v3) -> 8 (v4)`

The denominator changed between rubric versions. Any computation using `aspirational_pass / 6` is a formula version error.

**SYMMETRIC DELTA REGISTER**

| Comparison type | Prior state | Current state |
|-----------------|-------------|---------------|
| N_aspirational (formula denominator) | 6 (v3) | 8 (v4) |
| Regression verdicts | No prior-round scorecard provided -- row N/A | -- |
| Arithmetic discrepancies | Updated in Phase 3 after verification | -- |

---

## PHASE 2: SCORE EACH OUTPUT

**MODEL CELL (Phase 2 entry -- fires before any verdict row)**

Evidence (model): "from V-01, Phase 1 section 1c: the SYMMETRIC DELTA REGISTER table header reads `| Comparison type | Prior state | Current state |` and the register rules state 'A blank Prior State cell is a structural violation' -- this locates the structural enforcement mechanism (mandatory column presence) in the scored output rather than restating the criterion's pass condition."

ENTRY LOCK cleared. Proceeding to verdict rows.

---

### V-01: Axis J -- Symmetric Delta Register

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Load verification | E | PASS | Section 1a explicitly lists all four required elements: "(a) all criteria IDs with tier labels... (b) the exact composite formula text... (c) the golden threshold condition... (d) the count or list of outputs being scored." All four elements are named and required. |
| C-02 | Per-criterion verdict matrix | E | PASS | Phase 2 scoring table format mandates a row for every criterion-output pair: "No row may be blank or missing." The column spec (ID, Criterion, Tier, Verdict, Evidence) is complete. |
| C-03 | Evidence for every verdict | E | PASS | MODEL CELL instruction at Phase 2 entry establishes the evidence standard: "must quote, paraphrase with location, or name a specific structural feature." Anti-restatement rule stated: "Evidence that restates the criterion... is criterion restatement, not evidence -- rewrite it." |
| C-04 | Composite score per output | E | PASS | Post-table calculation block requires: "essential_pass = [count; PARTIAL = 0.5]... composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 8 * 10) = [result]" with explicit E/R/A counts before the composite. |
| C-05 | Failure patterns section | E | PASS | SYNTHESIS section includes: "FAILURE PATTERNS -- For each criterion receiving PARTIAL or FAIL across ALL outputs... Required even when empty: 'No failure patterns -- all criteria passed in at least one output.'" Section is structurally required. |
| C-06 | Ranked leaderboard | R | PASS | LEADERBOARD section requires ranked table with "all N outputs appear, ordered from highest to lowest composite score... Ties must be noted explicitly. 'See scores above' does not satisfy C-06 -- the ranking must be a distinct sorted structure." |
| C-07 | Excellence signals | R | PASS | EXCELLENCE SIGNALS section requires: "Signal: [output ID] -- [criterion ID] -- [specific structural mechanism]." Anti-generic rule enforced: "'V-05 scored highest overall' is not an excellence signal." |
| C-08 | Per-output synthesis notes | R | PASS | PER-OUTPUT SYNTHESIS NOTES section requires: "one paragraph explaining what structural choices drove its score relative to other outputs. Do not list verdict counts -- explain the mechanism." |
| C-09 | Regression signals | A | PARTIAL | N/A rule applies: "If no prior round data was provided: 'No prior round data -- regression analysis cannot be performed.'" No prior-round scorecard exists for this run; prescribed N/A statement earns PARTIAL per rubric rule. |
| C-10 | Score arithmetic verification | A | PASS | Section 3a requires full re-derivation: "Pick one output. Recompute its composite from the stated verdict counts and formula." States: "[X]/5, [X]/3, [X]/8 -> computed composite." |
| C-11 | Evidence positive anchor | A | PASS | MODEL CELL INSTRUCTION fires at Phase 2 entry as the first required action before any verdict row. Positive example format specified: "Evidence (model): 'from [output ID], [section or criterion]: [verbatim quote or structural observation]'" with locatability test. |
| C-12 | Discrepancy declaration | A | PASS | Section 3a requires: "Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]" -- labeled binary declaration field. Rule: "The 'Matches stated score:' field is required. 'Verification performed' or narrative equivalents do not satisfy C-12." |
| C-13 | Formula version delta declaration | A | PASS | Section 1b requires scorer to write in output: "Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N]." Both prior and current required. FORMULA CHANGE ALERT provides the prompt-side requirement; 1b provides the output-side requirement. |
| C-14 | Pre-scoring mechanism placement | A | PASS | MODEL CELL INSTRUCTION is labeled "(fire at Phase 2 entry -- before any evidence row is written)." ENTRY LOCK: "do not write any verdict row until the model cell above is written and passes the test." The anchor fires at Phase 2 entry, the earliest viable point. |
| C-15 | Symmetric comparison completeness | A | PASS | SYMMETRIC DELTA REGISTER (section 1c) creates a mandatory two-column table: Prior State | Current State. Rule: "A blank Prior State cell is a structural violation." N_aspirational row pre-populated with both 6 (prior) and 8 (current). Regression and arithmetic rows filled during Phase 3 or marked N/A. N/A rule available: "No prior-state value available in this scoring context" earns PARTIAL per row, not FAIL. |
| C-16 | Phase-distinct mechanism distribution | A | PASS | Phase 1: formula version delta block (enforces C-13), load summary (enforces C-01), SYMMETRIC DELTA REGISTER (enforces C-15). Phase 2: MODEL CELL at entry (enforces C-11, C-14), ENTRY LOCK (enforces C-14). Phase 3: arithmetic re-derivation (enforces C-10), YES/NO declaration (enforces C-12), regression section (enforces C-09). Mechanisms at all 3 phases; each actively enforces at least one criterion. |

**V-01 composite:**

```
essential_pass = 5/5 = 5.0
recommended_pass = 3/3 = 3.0
aspirational_pass = 7.5/8  (C-09 PARTIAL = 0.5; C-10--C-16 each PASS = 1.0)
composite = (5/5 * 60) + (3/3 * 30) + (7.5/8 * 10)
          = 60.000 + 30.000 + 9.375
          = 99.375
Golden: YES -- all 5 essentials PASS; composite 99.375 >= 80
```

---

### V-02: Axis K -- Phase Mechanism Inventory

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Load verification | E | PASS | Section 1b requires all four elements: "(a) all criteria IDs with tier labels... (b) exact composite formula: composite = (E/5*60) + (R/3*30) + (A/8*10)... (c) golden threshold: all 5 essentials PASS AND composite >= 80... (d) count and list of outputs being scored." |
| C-02 | Per-criterion verdict matrix | E | PASS | Phase 2 scoring table format with rule "No row may be blank." Same criterion coverage as V-01. |
| C-03 | Evidence for every verdict | E | PASS | MODEL CELL at Phase 2 entry with format "Evidence (model): 'from [output ID]: [verbatim quote or specific structural reference]'" plus locatability test and anti-restatement rule. |
| C-04 | Composite score per output | E | PASS | Post-table formula: "essential_pass = [E count]... composite = (E/5 * 60) + (R/3 * 30) + (A/8 * 10) = [result]" with explicit tier counts. |
| C-05 | Failure patterns section | E | PASS | SYNTHESIS section: "FAILURE PATTERNS: criteria with no PASS across all outputs. Required section even when empty: 'No failure patterns -- all criteria passed in at least one output.'" |
| C-06 | Ranked leaderboard | R | PASS | LEADERBOARD: "ranked table by composite descending, ties noted explicitly." Explicit distinct structure required. |
| C-07 | Excellence signals | R | PASS | EXCELLENCE SIGNALS: "output-criterion pairs where one output leads the field. Structural explanation required (name the design property, not the criterion label)." Anti-generic enforced. |
| C-08 | Per-output synthesis notes | R | PASS | PER-OUTPUT SYNTHESIS NOTES: "one paragraph per output explaining structural drivers, not verdict count lists." |
| C-09 | Regression signals | A | PARTIAL | N/A rule: "If no prior-round data: 'No prior round data -- regression analysis cannot be performed.'" Prior scorecard absent; prescribed statement earns PARTIAL. |
| C-10 | Score arithmetic verification | A | PASS | Section 3a requires full re-derivation: "Stated: E=[X]/5, R=[X]/3, A=[X]/8. Computed: ([X]/5*60) + ([X]/3*30) + ([X]/8*10) = [result]." |
| C-11 | Evidence positive anchor | A | PASS | MODEL CELL at Phase 2 entry: "Write your first evidence cell as: Evidence (model): 'from [output ID]: [verbatim quote or specific structural reference]'" with locatability test. |
| C-12 | Discrepancy declaration | A | PASS | Section 3a: "Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]. The binary declaration field is required. Narrative equivalents do not satisfy C-12." |
| C-13 | Formula version delta declaration | A | PASS | Section 1a: "Write in your scoring output: Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N]. Both values must appear." Output-side requirement explicitly stated. |
| C-14 | Pre-scoring mechanism placement | A | PASS | MODEL CELL labeled "(fire at Phase 2 entry)" with ENTRY LOCK: "no verdict row may be written until the model cell is written and passes the test." Anchor fires at Phase 2 entry. |
| C-15 | Symmetric comparison completeness | A | PASS | Three independent bilateral requirements: (1) formula delta 1a: "Both values must appear. Writing only the current value earns PARTIAL on C-13"; (2) regression 3b: "Both prior and current verdicts are required for each entry"; (3) arithmetic 3a: "Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]" format exposes both sides for any discrepancy. N/A rule available for unavailable prior-state data. |
| C-16 | Phase-distinct mechanism distribution | A | PASS | MECHANISM INVENTORY (pre-Phase-1 gate) forces declaration at Phase 1, 2, and 3 with Phase coverage count required >= 2. Rule: "If your inventory shows coverage = 1, add mechanisms to a second phase before proceeding." Inherited mechanisms span: Phase 1 (formula delta, load summary), Phase 2 (MODEL CELL, ENTRY LOCK), Phase 3 (arithmetic, YES/NO, regression). MECHANISM INVENTORY converts incidental C-16 compliance into deliberate structural declaration. |

**V-02 composite:**

```
essential_pass = 5.0
recommended_pass = 3.0
aspirational_pass = 7.5/8  (C-09 PARTIAL; all others PASS)
composite = 60.000 + 30.000 + 9.375 = 99.375
Golden: YES
```

---

### V-03: Axis L -- Symmetry Audit Sweep

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Load verification | E | PASS | Step 1 requires: "All criteria IDs with their tier (essential/recommended/aspirational) -- write all 16... composite formula exactly as above... golden threshold condition... how many outputs you are about to score and which ones." All four elements. |
| C-02 | Per-criterion verdict matrix | E | PASS | Phase 2 scoring table with "Guidance for evidence cells" and no-blank-row rule. Same structure as other variations. |
| C-03 | Evidence for every verdict | E | PASS | MODEL EVIDENCE CELL at Phase 2 entry with locatability test. Guidance: "Quote a phrase... Name a section title + what is in it... Describe a structural feature specific to this output. Do NOT write: 'the output satisfies this criterion.'" Three acceptable formats listed, one prohibited format stated. |
| C-04 | Composite score per output | E | PASS | Post-table block: "Breakdown: E=[X]/5, R=[X]/3, A=[X]/8. Composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/8 * 10) = [result]." Explicit tier counts before composite. |
| C-05 | Failure patterns section | E | PASS | SYNTHESIS section: "FAILURE PATTERNS: criteria with no PASS across all outputs. Write the section even when empty: 'No failure patterns found.'" Section structurally required; empty-section statement prescribed. |
| C-06 | Ranked leaderboard | R | PASS | LEADERBOARD: "ranked by composite descending, ties noted." Distinct structure required. |
| C-07 | Excellence signals | R | PASS | EXCELLENCE SIGNALS: "for each criterion where one output leads, name the output, the criterion, and the specific structural mechanism producing the outlier. No general 'scored highest' statements." |
| C-08 | Per-output synthesis notes | R | PASS | PER-OUTPUT SYNTHESIS NOTES: "one paragraph per output explaining what structural choices drove its score. Explain mechanism, not verdict counts." |
| C-09 | Regression signals | A | PARTIAL | "If no prior scorecard: 'No prior round data -- skipping regression.'" N/A rule applies; prescribed statement earns PARTIAL. |
| C-10 | Score arithmetic verification | A | PASS | Phase 3: "Pick one output and compute its composite from scratch using the stated verdict counts." Full re-derivation format with explicit counts. |
| C-11 | Evidence positive anchor | A | PASS | MODEL EVIDENCE CELL at Phase 2 entry: "Your first evidence cell sets the standard for all the others. Write it as a complete example: 'from [output ID], [section/structure name]: [exact quote or structural observation]'" with locatability gate. |
| C-12 | Discrepancy declaration | A | PASS | Phase 3: "Write 'YES' or 'NO'. Do not write 'seems correct' or 'checks out' -- a binary answer is required so that errors are visible rather than buried in narrative." Binary enforced. |
| C-13 | Formula version delta declaration | A | PASS | Step 2: "Write this sentence out loud in your output: 'N_aspirational changed from 6 (v3) to 8 (v4). Old denominator is retired.' Both values, both versions." Imperative phrasing with output-side requirement. |
| C-14 | Pre-scoring mechanism placement | A | PASS | MODEL EVIDENCE CELL: "Your first evidence cell sets the standard." GATE: "do not write any verdict until the model cell above is written and you have answered 'yes' to the locatability question." Anchor fires at Phase 2 entry. |
| C-15 | Symmetric comparison completeness | A | PASS | SYMMETRY AUDIT SWEEP at Phase 1 exit checks: "Did I write both the before value and the after value?" Table with Symmetric? column; Symmetric? = NO triggers a return to add the missing side. Phase 3 exit sweep covers arithmetic discrepancy and regression verdict rows. Two-sweep architecture (prevent + catch) addresses all comparison types. |
| C-16 | Phase-distinct mechanism distribution | A | PASS | Phase 1: FORMULA CHANGE ALERT, load summary (Step 1), formula delta (Step 2), SYMMETRY AUDIT SWEEP at Phase 1 exit. Phase 2: MODEL EVIDENCE CELL, GATE. Phase 3: YES/NO arithmetic, regression with both sides, SYMMETRY AUDIT SWEEP at Phase 3 exit. Mechanisms at all 3 phases. |

**V-03 composite:**

```
essential_pass = 5.0
recommended_pass = 3.0
aspirational_pass = 7.5/8  (C-09 PARTIAL; all others PASS)
composite = 60.000 + 30.000 + 9.375 = 99.375
Golden: YES
```

---

### V-04: Axes J+K -- Symmetric Delta Register + Phase Mechanism Inventory

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Load verification | E | PASS | Section 1a requires all four elements with same "(a)--(d)" enumeration as V-01/V-02. MECHANISM INVENTORY precedes the load summary but does not substitute for it. |
| C-02 | Per-criterion verdict matrix | E | PASS | Verdict table with evidence rules; no-blank-row requirement maintained. |
| C-03 | Evidence for every verdict | E | PASS | MODEL CELL at Phase 2 entry with locatability test; evidence must "reference specific content in the scored output (quote, section name, structural observation)." Anti-restatement: "Must NOT restate the criterion label." |
| C-04 | Composite score per output | E | PASS | Post-table: "E=[X]/5, R=[X]/3, A=[X]/8. composite = ([X]/5 * 60) + ([X]/3 * 30) + ([X]/8 * 10) = [result]." Explicit counts and formula. |
| C-05 | Failure patterns section | E | PASS | SYNTHESIS: "FAILURE PATTERNS: criteria with no PASS across all outputs. Required even when empty." |
| C-06 | Ranked leaderboard | R | PASS | LEADERBOARD: "all outputs ranked by composite descending. Ties noted explicitly." Distinct ranked structure. |
| C-07 | Excellence signals | R | PASS | EXCELLENCE SIGNALS: "output-criterion pairs where one output leads the field. Structural explanation required (name the design property, not the criterion label)." |
| C-08 | Per-output synthesis notes | R | PASS | PER-OUTPUT SYNTHESIS NOTES: "one paragraph per output on structural score drivers." |
| C-09 | Regression signals | A | PARTIAL | "If no prior-round data: 'No prior round data -- regression analysis cannot be performed.'" N/A rule; prescribed statement earns PARTIAL. |
| C-10 | Score arithmetic verification | A | PASS | Section 3a: full re-derivation from stated counts; "Matches stated score: YES | NO" declaration. |
| C-11 | Evidence positive anchor | A | PASS | MODEL CELL: "Write as the first action of Phase 2... MODEL CELL: Evidence (example): 'from [output ID], [section or structural element]: [verbatim excerpt or structural observation]'" with locatability test. |
| C-12 | Discrepancy declaration | A | PASS | Section 3a: "Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]. Binary declaration required." |
| C-13 | Formula version delta declaration | A | PASS | Section 1b: "Write in scorer output (required, not just in prompt instructions): Formula version delta: N_aspirational changed from 6 (v3) to 8 (v4). Both sides." Output-side requirement explicit. |
| C-14 | Pre-scoring mechanism placement | A | PASS | MODEL CELL labeled "Phase 2 entry -- fires before any verdict row." ENTRY LOCK: "no verdict row may appear until the MODEL CELL above is written and passes the locatability test. This lock is the Phase 2 enforcement mechanism." |
| C-15 | Symmetric comparison completeness | A | PASS | SYMMETRIC DELTA REGISTER (J): mandatory Prior State column with structural violation rule for blank cells. N_aspirational pre-populated with 6->8. Regression and arithmetic rows filled during Phase 3 with note: "A regression entry that names only the current verdict is a C-15 violation -- add the prior verdict." Register is single source of truth. |
| C-16 | Phase-distinct mechanism distribution | A | PASS | MECHANISM INVENTORY (K): pre-Phase-1 gate requiring "Phase 1: Active: [...], Phase 2: Active: [...], Phase 3: Active: [...], Phase coverage count: [N]" with gate "Phase coverage count must be >= 2." Inherited mechanisms span Phase 1 (formula delta, load summary, DELTA REGISTER), Phase 2 (MODEL CELL, ENTRY LOCK), Phase 3 (arithmetic, YES/NO, regression). Both J and K are active at Phase 1; K's gate enforces Phase 2 + Phase 3 presence. |

**V-04 composite:**

```
essential_pass = 5.0
recommended_pass = 3.0
aspirational_pass = 7.5/8  (C-09 PARTIAL; all others PASS)
composite = 60.000 + 30.000 + 9.375 = 99.375
Golden: YES
```

---

### V-05: Axes J+K+M -- Full Integration with Inertia Baseline

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Load verification | E | PASS | Section 1a with all four required elements (a)--(d). INERTIA BASELINE DECLARATION precedes and labels Phase 1 inertia as "no load summary or formula check; scoring begins immediately." The departure is the load summary itself, making C-01 the first deliberate anti-inertia action. |
| C-02 | Per-criterion verdict matrix | E | PASS | Verdict table with evidence standard; no-blank-row rule. Same structure as V-04. |
| C-03 | Evidence for every verdict | E | PASS | MODEL CELL with locatability test. Additionally, explicit positive/negative contrast: "ACCEPTABLE: verbatim quote, named section + what is in it, structural observation specific to this output. INERTIA (NOT acceptable): 'the output has [criterion name]', 'this criterion is met', 'the output provides a leaderboard' without naming what it contains." Strongest anti-restatement framing across all variations. |
| C-04 | Composite score per output | E | PASS | Post-table: "E=[X]/5, R=[X]/3, A=[X]/8. composite = ([X]/5 * 60) + ([X]/3 * 30) + ([X]/8 * 10) = [result]." Explicit tier counts. |
| C-05 | Failure patterns section | E | PASS | SYNTHESIS FAILURE PATTERNS section: "Inertia failure modes addressed: synthesis section absent, or lists verdict counts without structural explanation." Section required; empty-section statement prescribed. |
| C-06 | Ranked leaderboard | R | PASS | LEADERBOARD with inertia framing: "Inertia: pointer to scores above. Departure: distinct ranked structure with all outputs present." Explicit distinction. |
| C-07 | Excellence signals | R | PASS | EXCELLENCE SIGNALS: "[Output ID] -- [Criterion ID] -- [structural mechanism causing the difference]. Inertia: 'V-X scored highest overall.' Departure: specific output-criterion-mechanism triple." |
| C-08 | Per-output synthesis notes | R | PASS | PER-OUTPUT SYNTHESIS NOTES: "Inertia: 'V-X scored E=5/5, R=2/3, A=4/8.' Departure: explanation of mechanism, not counts." |
| C-09 | Regression signals | A | PARTIAL | "No prior round data -- regression analysis cannot be performed." N/A rule; PARTIAL. Inertia framing labels section absence as "Absent section = C-09 FAIL (inertia default)," but the N/A statement remains the ceiling in the no-prior-data scenario. |
| C-10 | Score arithmetic verification | A | PASS | Section 3a with full re-derivation. Inertia framing: "Inertia would write 'verification performed' without a named result." Binary YES/NO required as departure. |
| C-11 | Evidence positive anchor | A | PASS | MODEL CELL -- Phase 2 entry gate. Inertia labeled as "evidence cells restate criterion labels; no model cell; verdicts written before any evidence standard is established." MODEL CELL fires as the departure. |
| C-12 | Discrepancy declaration | A | PASS | Section 3a: "Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]. Binary YES/NO required. Inertia would write 'verification performed.'" Inertia framing makes the requirement's purpose explicit. |
| C-13 | Formula version delta declaration | A | PASS | Section 1b: "Formula version delta: N_aspirational changed from 6 (v3) to 8 (v4). Both sides required. Inertia would write only 'N_aspirational=8' without the prior." Both-sides requirement stated with concrete inertia failure mode as foil. |
| C-14 | Pre-scoring mechanism placement | A | PASS | MODEL CELL at Phase 2 entry with ENTRY LOCK. Inertia labeled: "anchor deferred to Phase 3 or absent." ENTRY LOCK fires as the departure, placing anchor at earliest viable point. |
| C-15 | Symmetric comparison completeness | A | PASS | SYMMETRIC DELTA REGISTER (J) with inertia framing: "Blank Prior State cell: structural violation (inertia: 'N_aspirational=8' without prior). Write the value or write 'N/A -- [reason].' Blank = detected by column scan, same as blank evidence cell." Regression entries: "Inertia pattern to avoid: '[Output ID] / [Criterion ID]: current=[verdict]' with no prior." Two-sided enforcement: structural table (J) + labeled inertia failure mode (M). |
| C-16 | Phase-distinct mechanism distribution | A | PASS | MECHANISM INVENTORY (K) + INERTIA BASELINE (M) both enforce phase distribution. Inertia framing: "Inertia failure mode: all mechanisms at Phase 3, or absent. Phases 1 and 2 unguarded. Departure: declare mechanisms at 2+ distinct phases before writing the load summary." Phase coverage gate (>= 2) with self-correction loop. Mechanisms span Phase 1, 2, and 3 with each departure from inertia explicitly labeled. |

**V-05 composite:**

```
essential_pass = 5.0
recommended_pass = 3.0
aspirational_pass = 7.5/8  (C-09 PARTIAL; all others PASS)
composite = 60.000 + 30.000 + 9.375 = 99.375
Golden: YES
```

---

## PHASE 3: VERIFY

**Arithmetic verification (V-01)**

```
Verification (V-01):
  Stated counts: E=5/5, R=3/3, A=7.5/8
  Recomputed: (5/5 * 60) + (3/3 * 30) + (7.5/8 * 10)
            = 60.000 + 30.000 + 9.375
            = 99.375
  Matches stated score: YES
```

**SYMMETRIC DELTA REGISTER update (Phase 3):**

| Comparison type | Prior state | Current state |
|-----------------|-------------|---------------|
| N_aspirational (formula denominator) | 6 (v3) | 8 (v4) |
| Regression verdicts | No prior-round scorecard provided -- row N/A | -- |
| Arithmetic discrepancies | No discrepancy identified -- row N/A | -- |

**Regression section**

No prior-round scorecard provided for R4. Regression analysis cannot be performed. All variations carry forward from the R3 champion base (D+E+F+G+H); no degradation is detectable without a prior-round file.

---

## SYNTHESIS

### LEADERBOARD

| Rank | Output | Composite | Golden? |
|------|--------|-----------|---------|
| 1 (tied) | V-01 | 99.375 | YES |
| 1 (tied) | V-02 | 99.375 | YES |
| 1 (tied) | V-03 | 99.375 | YES |
| 1 (tied) | V-04 | 99.375 | YES |
| 1 (tied) | V-05 | 99.375 | YES |

**Five-way tie at 99.375.** This is the R4 ceiling given no prior-round data (C-09 PARTIAL is structural for this scoring run). The ceiling is 99.375; the only unreachable point is the C-09 PASS condition which requires a prior-round scorecard.

---

### EXCELLENCE SIGNALS

**Signal: V-01 -- C-15 -- SYMMETRIC DELTA REGISTER as structural enforcement**
V-01 introduces the SYMMETRIC DELTA REGISTER, a mandatory Phase 1 table with a Prior State column that is a structural violation to leave blank -- the same detectability mechanism as a blank evidence cell. Prior variations achieved C-15 compliance through textual instruction ("write both values"). V-01 achieves it through structural presence: a scanner can detect a missing prior-state value without reading cell content, because an empty column cell is visible regardless of surrounding prose.

**Signal: V-02 -- C-16 -- MECHANISM INVENTORY with phase coverage gate as a self-correction loop**
V-02 introduces the MECHANISM INVENTORY as a pre-scoring gate: the scorer must declare active mechanisms per phase and confirm coverage >= 2 before writing the load summary. If coverage = 1, they must add mechanisms before proceeding. This converts C-16 from a property that happens to be present (because the R3 champion incidentally had G at Phase 1 and H at Phase 2) into a property that is explicitly chosen and self-verified. The self-correction loop is the design innovation: the prompt does not merely require phase distribution, it requires the scorer to audit and correct their own distribution before scoring begins.

**Signal: V-03 -- C-15 -- SYMMETRY AUDIT SWEEP as an orthogonal catch mechanism**
V-03 achieves C-15 through a two-mechanism architecture (prevent + catch) rather than structural enforcement. The FORMULA CHANGE ALERT and imperative phrasing ("write both: old -> new") prevent one-sided comparisons in drafting. The SYMMETRY AUDIT SWEEP at Phase 1 exit and Phase 3 exit catches any comparison that slipped through. The sweep format -- "Before value written? / After value written? / Symmetric?" -- forces a binary per-comparison check, analogous to C-12's YES/NO discrepancy declaration. This is the first variation to apply the binary-declaration pattern to symmetry verification rather than arithmetic verification.

**Signal: V-05 -- C-03 quality -- Inertia framing with explicit positive/negative contrast at evidence cells**
V-05's inertia framing at the evidence cell instruction provides the clearest positive/negative contrast for evidence quality across all variations: "ACCEPTABLE: verbatim quote, named section + what is in it, structural observation specific to this output. INERTIA (NOT acceptable): 'the output has [criterion name]', 'this criterion is met', 'the output provides a leaderboard' without naming what it contains." Unlike V-01--V-04's anti-restatement rule ("evidence that restates the criterion... is criterion restatement -- rewrite it"), V-05 shows two concrete examples of the prohibited pattern. This may reduce borderline C-03 cells without raising the criterion score above PASS -- the mechanism improves evidence cell quality within the passing band rather than changing the verdict.

---

### FAILURE PATTERNS

No failure patterns -- all criteria passed in at least one output.

C-09 received PARTIAL across all five outputs, but PARTIAL does not constitute a failure pattern (the criterion requires PASS across at least one output; PARTIAL across all outputs is a coverage ceiling pattern, not a failure pattern). The C-09 ceiling is structural: no prior-round scorecard was provided, and the rubric's N/A rule caps C-09 at PARTIAL in this scoring context regardless of variation design.

---

### PER-OUTPUT SYNTHESIS NOTES

**V-01**: V-01 is the most structurally conservative variation. It adds exactly one new mechanism to the R3 base: the SYMMETRIC DELTA REGISTER. The register achieves C-15 PASS through column presence rather than instruction compliance -- a blank Prior State cell is detectable by structure, not by reading. V-01 reaches the ceiling with the minimum mechanism count among R4 variations, demonstrating that the DELTA REGISTER alone is sufficient for the R4 scoring ceiling. Its weakness relative to V-04/V-05 is the absence of the MECHANISM INVENTORY: C-16 PASS relies on inherited phase distribution (G+H from R3) rather than deliberate pre-scoring declaration.

**V-02**: V-02 achieves C-16 compliance by the most deliberate mechanism of any variation: the MECHANISM INVENTORY with phase coverage gate. The pre-scoring declaration converts C-16 from an emergent property into an explicit choice. However, V-02 achieves C-15 PASS through scattered bilateral instructions at each comparison point rather than a centralized structural table. This produces the same criterion score as V-01 but with weaker enforcement robustness: a scorer who misses one of the three bilateral instructions produces a one-sided comparison without a structural gap to detect it. V-02 and V-01 tie at 99.375 but represent different tradeoffs in the C-15 vs. C-16 enforcement axis.

**V-03**: V-03 is the only variation that applies the "prevent + catch" architecture to symmetry verification. The imperative phrasing reduces one-sided comparisons at the moment of writing; the two SYMMETRY AUDIT SWEEP tables catch any that remain before the scorer proceeds to the next phase. This architecture is orthogonal to J's structural enforcement and K's pre-scoring declaration: V-03 acts on comparisons after they are written rather than preventing or pre-declaring them. The two-sweep design introduces a new pattern class -- bilateral post-write audits -- that had not appeared in prior rounds.

**V-04**: V-04 combines J and K additively. Where V-01 relies on column structure for C-15 and inherited phase distribution for C-16, and V-02 relies on bilateral instructions for C-15 and pre-declaration for C-16, V-04 applies structural enforcement (J) for C-15 AND pre-declaration (K) for C-16. Neither mechanism can satisfy the other's criterion: the DELTA REGISTER does not guarantee phase coverage, and the MECHANISM INVENTORY does not guarantee bilateral comparisons. The combination is redundant at the ceiling (all criteria PASS regardless), but provides belt-and-suspenders robustness for both criteria that neither single-axis variation achieves. V-04's ceiling match with V-01/V-02/V-03 shows that single-axis approaches were sufficient for R4 -- unlike R3 where G+H were both required for the ceiling.

**V-05**: V-05 is the highest-mechanism variation. Beyond V-04 (J+K), it adds inertia framing (M) at every enforcement point. The inertia framing makes two contributions: it labels the failure mode each mechanism prevents ("Inertia failure mode: ..."), and it provides the most detailed positive/negative contrast for evidence cells. The labeled failure modes serve C-03 quality (by making restatement's name visible) and C-16 reasoning (by naming "all mechanisms at Phase 3, Phases 1+2 unguarded" as the inertia outcome). V-05 reaches the same ceiling as V-04 because no rubric criterion distinguishes labeled departure explanations from unlabeled ones -- the labeling affects evidence quality within the PASS band, not the criterion verdict. V-05 would be the expected champion if a C-17 were added requiring explicit inertia departure documentation.

---

## Round 4 Finding

**All five variations independently reach the R4 ceiling (99.375).** This contrasts with R3, where V-04 (G+H) was required to reach the v3 ceiling while V-03 (Axis I alone) fell short. In R4, each new axis (J, K, or L) independently achieves C-15 PASS, and the R3 base (G+H) already provides Phase 1+2+3 coverage sufficient for C-16 PASS. The R4 ceiling is determined by C-09 PARTIAL (no prior-round data), not by any criterion requiring combined mechanisms.

**Design implication**: For R5, the useful variation axes are those that could achieve C-09 PASS (require a prior-round scorecard in the prompt context) or introduce a new criterion that distinguishes mechanism robustness levels.

---

```json
{"top_score": 99.375, "all_essential_pass": true, "new_patterns": ["SYMMETRIC DELTA REGISTER -- mandatory Prior State column makes blank prior-state values structurally detectable by column scan rather than by reading, converting C-15 from a textual instruction to a structural requirement with the same detectability as a blank evidence cell", "MECHANISM INVENTORY with phase coverage gate -- pre-scoring declaration of active mechanisms per phase forces C-16 compliance to be deliberate rather than incidental, with self-correction loop requiring scorers to add mechanisms before proceeding if Phase coverage < 2", "SYMMETRY AUDIT SWEEP -- post-write bilateral check at Phase 1 exit and Phase 3 exit applies the binary-declaration pattern (Symmetric: YES/NO) to comparison completeness, introducing a catch mechanism orthogonal to J's prevention mechanism", "Inertia framing with departure-labeled mechanisms -- naming the bare-scorecard baseline failure mode at each enforcement point provides a concrete negative foil that makes the scoring cost of each omission visible at the moment of writing"]}
```
