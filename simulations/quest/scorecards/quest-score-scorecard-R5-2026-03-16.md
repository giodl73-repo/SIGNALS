## quest-score Round 5 Scorecard (v5 rubric)

---

### PHASE 1: LOAD AND DELTA REGISTER

**1a. Load summary**

Rubric loaded: v5-2026-03-16

| Tier | Criteria |
|------|----------|
| Essential (C-01--C-05) | C-01 load verification, C-02 verdict matrix, C-03 evidence, C-04 composite score, C-05 failure patterns |
| Recommended (C-06--C-08) | C-06 leaderboard, C-07 excellence signals, C-08 per-output notes |
| Aspirational (C-09--C-18) | C-09 regression, C-10 arithmetic, C-11 evidence anchor, C-12 discrepancy declaration, C-13 formula delta, C-14 pre-scoring placement, C-15 symmetric completeness, C-16 phase distribution, C-17 inertia labeling, C-18 bilateral sweep |

Formula (v5, active):
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 10 * 10)
PARTIAL = 0.5. FAIL = 0.
```

Golden threshold: ALL 5 essentials PASS AND composite >= 80.

Outputs scored: 5 (V-01, V-02, V-03, V-04, V-05)

Inertia (C-01): Without this load block, criteria count (18, not 16), formula denominator (/10 not /8), and threshold are unverified before any verdict is written. Errors in C-02 (wrong criterion count) and C-04 (wrong denominator) remain invisible until Phase 3.

---

**1b. Formula version delta**

Formula version delta: N_aspirational changed from 8 (v4) to 10 (v5).

Inertia (C-13, C-15): "N_aspirational=10" in the load summary confirms the current value was loaded but does not confirm the prior value (8) was registered as distinct. C-15 requires both sides of every delta comparison. A current-only statement fails C-15 even when C-01 is PASS.

---

**1c. SYMMETRIC DELTA REGISTER**

| Comparison type | Prior state | Current state |
|-----------------|-------------|---------------|
| N_aspirational (formula denominator) | 8 (v4) | 10 (v5) |
| Regression verdicts | No prior-round data (trace artifact: placeholder) -- row N/A | -- |
| Arithmetic discrepancies | No discrepancy found (pending Phase 3) -- row N/A | -- |

Inertia (C-15): Without the two-column table, a scorer writes "N_aspirational=10" with no visible Prior State column. The column structure makes a one-sided entry a detectable structural gap by column scan rather than by re-reading prose.

**BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

| Comparison | Symmetric? |
|------------|-----------|
| N_aspirational (formula denominator) | YES -- Prior: 8 (v4), Current: 10 (v5) |
| Regression verdicts | PARTIAL -- no prior-round data; N/A rule invoked |
| Arithmetic discrepancies | PARTIAL -- no discrepancy found at this stage; N/A rule invoked |

Inertia (C-18): The DELTA REGISTER prevents asymmetric comparisons by requiring both columns. This sweep provides an independent catch mechanism -- a Symmetric: NO cell is detectable by column scan without reading the register prose. An output can pass C-15 (both sides present through structural enforcement) while failing C-18 (no independent catch exists). The sweep complements prevention; both are required.

---

### PHASE 2: SCORE EACH OUTPUT

**MODEL CELL (Phase 2 entry -- before any verdict row)**

Evidence (model): "from V-01, Phase 1 section 1c: the 'SYMMETRIC DELTA REGISTER' is a two-column table with explicit column headers 'Prior state' and 'Current state' -- the column structure makes a blank Prior State cell detectable by scanning column 2 without reading the comparison prose"

Locatability test: YES -- the feature (two-column table with named headers) can be located in any output following the V-01 prompt by scanning the Phase 1 section for a table with those exact column names.

Inertia (C-11, C-14): Without this model cell before any verdict, evidence defaults to criterion restatement -- "the output has a DELTA REGISTER" cannot locate the specific structural feature (the column headers that make asymmetry visible). The model cell fires before the first verdict, establishing the evidence standard before any cell can establish a lower norm.

ENTRY LOCK: no verdict row written before model cell. Confirmed.

---

#### V-01: Axis N -- Standardized Inertia Departure Labels

**Design summary:** All R4 base mechanisms (FORMULA CHANGE ALERT, load summary 1a, formula delta 1b, DELTA REGISTER 1c, MODEL CELL + ENTRY LOCK, arithmetic verify 3a, regression 3b). Adds: standardized "Inertia (C-XX): [failure mode]" required labeled fields after each mechanism. No bilateral audit sweep (1d absent). No pre-Phase-1 mechanism index.

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Rubric load verification | E | PASS | V-01 Phase 1 section 1a explicitly instructs the scorer to produce a block covering all four required elements: criteria IDs with tier labels, exact composite formula, golden threshold, and count/list of outputs. The prompt states "A load summary missing any one of (a)--(d) earns PARTIAL on C-01." |
| C-02 | Per-criterion verdict matrix | E | PASS | Phase 2 instructs a scoring table with columns "ID | Criterion | Tier | Verdict | Evidence" for each output; the prompt states "No row may be blank or missing." |
| C-03 | Evidence for every verdict | E | PASS | Phase 2 evidence column rule: "must quote, paraphrase with location, or name a specific structural feature of the scored output. Criterion restatement is not evidence." The MODEL CELL instruction explicitly mandates locatable evidence before any verdict row. |
| C-04 | Composite score per output | E | PASS | After each scoring table, V-01 requires explicit calculation format: "essential_pass = [count] ... composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 10 * 10) = [result]". Tier counts shown before final number. |
| C-05 | Failure patterns section | E | PASS | SYNTHESIS section includes FAILURE PATTERNS with the required empty-case text: "No failure patterns -- all criteria passed in at least one output." |
| C-06 | Ranked leaderboard | R | PASS | SYNTHESIS includes LEADERBOARD as a standalone ranked table with "All N outputs ranked descending" and explicit tie-noting requirement. |
| C-07 | Excellence signals | R | PASS | SYNTHESIS includes EXCELLENCE SIGNALS section requiring "output-criterion pair and structural explanation." Generic "V-05 scored highest overall" explicitly rejected in prompt. |
| C-08 | Per-output synthesis notes | R | PASS | SYNTHESIS includes PER-OUTPUT SYNTHESIS NOTES with "structural explanation per output. Not verdict counts." |
| C-09 | Regression signals | A | PARTIAL | Phase 3 section 3b present with N/A rule: "No prior round data -- regression analysis cannot be performed." Section is required and exists. Trace artifact is placeholder -- no prior data. N/A rule earns PARTIAL per rubric. |
| C-10 | Score arithmetic verification | A | PASS | Phase 3 section 3a: pick one output, recompute composite from stated counts and formula, show full derivation. |
| C-11 | Evidence positive anchor | A | PASS | MODEL CELL instruction at Phase 2 entry demonstrates what locatable evidence looks like: "from [output ID], [section or structural element]: [verbatim quote or structural observation]" with explicit locatability test (YES/NO). |
| C-12 | Discrepancy declaration | A | PASS | 3a arithmetic verification includes: "Matches stated score: YES \| NO -- discrepancy: stated [X], computed [Y]". Labeled binary field is required; narrative equivalents rejected. |
| C-13 | Formula version delta declaration | A | PASS | 1b instructs scorer to write: "Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N]." Both prior and current values required. FORMULA CHANGE ALERT at top provides prior=8 (v4). |
| C-14 | Pre-scoring mechanism placement | A | PASS | MODEL CELL + ENTRY LOCK placed at Phase 2 entry with explicit gate: "Do not write any verdict row until the model cell is written and passes the test." Fires before first evidence cell. |
| C-15 | Symmetric comparison completeness | A | PASS | 1c SYMMETRIC DELTA REGISTER two-column table (Prior state / Current state) with blank-cell structural violation rule: "A blank Prior State cell is a structural violation." Applied to N_aspirational, regression, and arithmetic rows. |
| C-16 | Phase-distinct mechanism distribution | A | PASS | Phase 1: load summary + formula delta + DELTA REGISTER (active C-01/C-13/C-15 enforcement). Phase 2: MODEL CELL + ENTRY LOCK (C-11/C-14 enforcement). Phase 3: arithmetic verify + regression (C-10/C-12/C-09 enforcement). Three distinct phases. |
| C-17 | Inertia departure labeling | A | PASS | V-01 introduces Axis N: "write this required labeled field: Inertia (C-XX): [failure mode text]" after every mechanism in the scorer's output. Required fields after 1a (C-01), 1b (C-13/C-15), 1c (C-15), MODEL CELL (C-11/C-14), 3a (C-12), 3b (C-09). All output-level mechanisms carry a mandatory departure label. |
| C-18 | Bilateral symmetry audit sweep | A | FAIL | No 1d bilateral audit sweep section. Phase 1 ends at 1c DELTA REGISTER with no post-register sweep producing Symmetric: YES/NO per-comparison verdicts. C-15 compliance relies entirely on the two-column prevention structure; no independent catch mechanism exists. |

**V-01 Score:**
```
essential_pass = 5/5
recommended_pass = 3/3
aspirational_pass = 8.5/10 (C-09 PARTIAL=0.5, C-18 FAIL=0, all others PASS=1)
composite = (5/5 * 60) + (3/3 * 30) + (8.5/10 * 10)
          = 60 + 30 + 8.5
          = 98.5
Golden: YES -- all essentials PASS; composite 98.5 >= 80
```

---

#### V-02: Axis O -- Bilateral Symmetry Audit Sweep

**Design summary:** All R4 base mechanisms. Adds: 1d BILATERAL SYMMETRY AUDIT SWEEP at Phase 1 exit with per-comparison "Symmetric: YES/NO" verdicts. Departure labels present as informal italic "*Departure from inertia*" advisory notes in the prompt -- not as mandatory "write this required labeled field" directives. No pre-Phase-1 mechanism index.

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Rubric load verification | E | PASS | 1a section instructs all four required elements; same structure as V-01. |
| C-02 | Per-criterion verdict matrix | E | PASS | Scoring table required for each output; no blank rows. |
| C-03 | Evidence for every verdict | E | PASS | Evidence column requires specific structural feature, quote, or named section. MODEL CELL locatability test enforces this before any verdict row. |
| C-04 | Composite score per output | E | PASS | Explicit calculation format "E=[n]/5, R=[n]/3, A=[n]/10; composite = (E/5*60)+(R/3*30)+(A/10*10) = [result]" after each output table. |
| C-05 | Failure patterns section | E | PASS | FAILURE PATTERNS required even when empty. |
| C-06 | Ranked leaderboard | R | PASS | Standalone ranked LEADERBOARD; "See scores above" rejected. |
| C-07 | Excellence signals | R | PASS | Output-criterion-mechanism triples required; generic observations rejected. |
| C-08 | Per-output synthesis notes | R | PASS | Structural explanation per output; verdict counts insufficient. |
| C-09 | Regression signals | A | PARTIAL | 3b present with N/A text. Trace artifact is placeholder. PARTIAL per N/A rule. |
| C-10 | Score arithmetic verification | A | PASS | 3a arithmetic recomputation present. |
| C-11 | Evidence positive anchor | A | PASS | MODEL CELL at Phase 2 entry with locatability test. |
| C-12 | Discrepancy declaration | A | PASS | "Matches stated score: YES \| NO -- discrepancy: stated [X], computed [Y]" |
| C-13 | Formula version delta declaration | A | PASS | 1b requires both prior and current values: "N_aspirational changed from [prior] to [current] in v[N]." |
| C-14 | Pre-scoring mechanism placement | A | PASS | MODEL CELL + ENTRY LOCK at Phase 2 entry; verdict row prohibited before model cell fires. |
| C-15 | Symmetric comparison completeness | A | PASS | 1c SYMMETRIC DELTA REGISTER with blank-cell structural violation rule. |
| C-16 | Phase-distinct mechanism distribution | A | PASS | Phase 1: load summary + formula delta + DELTA REGISTER + BILATERAL AUDIT SWEEP at Phase 1 exit. Phase 2: MODEL CELL. Phase 3: arithmetic + regression. Three distinct phases with active mechanisms. |
| C-17 | Inertia departure labeling | A | PARTIAL | V-02 carries M-axis informal italic notes ("*Departure from inertia (C-15): Without the two-column table...*") as advisory text in the prompt. These are framed as explanatory context, not as mandatory "write this required labeled field" directives. The scorer sees them as motivations, not required output fields. Some informal departure notes likely appear in scorer output, but not as standardized required fields at all mechanisms. At least one mechanism carries a departure label (by convention), but not all -- formal "Inertia: [failure mode]" required fields are absent. PARTIAL: some but not all mechanisms carry labeled departure explanations as mandatory scorer output fields. |
| C-18 | Bilateral symmetry audit sweep | A | PASS | V-02 1d BILATERAL SYMMETRY AUDIT SWEEP at Phase 1 exit: "Comparison \| Symmetric?" table with per-row "YES -- Prior: [value], Current: [value] \| NO -- [missing side] \| PARTIAL -- N/A declared" verdicts for each register row. Symmetric: NO requires remediation before Phase 2. Independent catch mechanism exists. |

**V-02 Score:**
```
essential_pass = 5/5
recommended_pass = 3/3
aspirational_pass = 9/10 (C-09 PARTIAL=0.5, C-17 PARTIAL=0.5, all others PASS=1 → 8×1 + 2×0.5 = 9)
composite = (5/5 * 60) + (3/3 * 30) + (9/10 * 10)
          = 60 + 30 + 9
          = 99
Golden: YES -- all essentials PASS; composite 99 >= 80
```

---

#### V-03: Axes N+O -- Departure Labels + Bilateral Sweep (Minimum Combination)

**Design summary:** All R4 base mechanisms. Adds: standardized "Required field after writing: Inertia (C-XX): [text]" required output fields after every mechanism (N-axis), PLUS 1d BILATERAL SYMMETRY AUDIT SWEEP with Symmetric: YES/NO (O-axis). The sweep itself has a required Inertia field. No pre-Phase-1 mechanism index.

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Rubric load verification | E | PASS | 1a with all four required elements; required Inertia field after: "Criteria count, formula denominator, and threshold unverified without this block. Errors in C-02/C-04 invisible until Phase 3." |
| C-02 | Per-criterion verdict matrix | E | PASS | Scoring table per output; no blank rows. |
| C-03 | Evidence for every verdict | E | PASS | Evidence column standard + MODEL CELL locatability test. |
| C-04 | Composite score per output | E | PASS | Explicit calculation with tier counts before final score. |
| C-05 | Failure patterns section | E | PASS | Required even when empty. |
| C-06 | Ranked leaderboard | R | PASS | Standalone ranked structure. |
| C-07 | Excellence signals | R | PASS | Output-criterion-mechanism triple format. |
| C-08 | Per-output synthesis notes | R | PASS | Structural explanation, not verdict counts. |
| C-09 | Regression signals | A | PARTIAL | 3b present with N/A rule. No prior data. PARTIAL per N/A rule. Inertia field present: "Absent section indistinguishable from no regressions. Required even empty." |
| C-10 | Score arithmetic verification | A | PASS | 3a recomputation present. |
| C-11 | Evidence positive anchor | A | PASS | MODEL CELL with locatability test at Phase 2 entry. |
| C-12 | Discrepancy declaration | A | PASS | "Matches stated score: YES \| NO" labeled field. Inertia field present. |
| C-13 | Formula version delta declaration | A | PASS | 1b with prior+current values. Inertia field present: "current-only statement confirms endpoint but not transition; both sides required." |
| C-14 | Pre-scoring mechanism placement | A | PASS | MODEL CELL + ENTRY LOCK at Phase 2 entry. Inertia field present. |
| C-15 | Symmetric comparison completeness | A | PASS | DELTA REGISTER two-column structure. Inertia field present. |
| C-16 | Phase-distinct mechanism distribution | A | PASS | Phase 1 (load + formula delta + DELTA REGISTER + bilateral sweep), Phase 2 (MODEL CELL), Phase 3 (arithmetic + regression). Three phases. |
| C-17 | Inertia departure labeling | A | PASS | V-03 upgrades V-02's informal italic notes to V-01's "Required field after writing: Inertia (C-XX): [text]" format at every mechanism, including 1a, 1b, 1c, 1d (bilateral sweep), MODEL CELL, 3a, 3b. Every output-level structural enforcement mechanism carries a mandatory labeled departure statement. |
| C-18 | Bilateral symmetry audit sweep | A | PASS | 1d BILATERAL SYMMETRY AUDIT SWEEP with "Symmetric: YES/NO" per-comparison verdicts at Phase 1 exit. Required Inertia field: "J's DELTA REGISTER prevents asymmetric comparisons by requiring both columns. The AUDIT SWEEP catches asymmetric entries independently -- a Symmetric: NO cell is visible by scanning the sweep without reading the register prose. C-15 compliance through prevention only has no independent catch mechanism; C-18 requires the sweep to exist." |

**V-03 Score:**
```
essential_pass = 5/5
recommended_pass = 3/3
aspirational_pass = 9.5/10 (C-09 PARTIAL=0.5, all others PASS=1 → 9×1 + 0.5 = 9.5)
composite = (5/5 * 60) + (3/3 * 30) + (9.5/10 * 10)
          = 60 + 30 + 9.5
          = 99.5
Golden: YES -- all essentials PASS; composite 99.5 >= 80
```

---

#### V-04: Axes K+N -- Mechanism Index with Departure Labels

**Design summary:** Pre-Phase-1 MECHANISM INDEX table declaring each mechanism, phase, criterion, and Inertia failure prevented. Each mechanism's departure label is pre-declared in the index and reproduced as a required field during execution. No bilateral audit sweep (1d absent -- the mechanism index lists the bilateral sweep as a mechanism but does not include a 1d section).

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Rubric load verification | E | PASS | 1a section with all four required elements; "Inertia (C-01): [as declared in Mechanism Index -- ...]" reproduced. |
| C-02 | Per-criterion verdict matrix | E | PASS | Scoring table structure present. |
| C-03 | Evidence for every verdict | E | PASS | Evidence standard + MODEL CELL locatability test. |
| C-04 | Composite score per output | E | PASS | Explicit calculation with tier counts. |
| C-05 | Failure patterns section | E | PASS | Required even when empty. |
| C-06 | Ranked leaderboard | R | PASS | Standalone ranked structure. |
| C-07 | Excellence signals | R | PASS | Output-criterion-mechanism triple format. |
| C-08 | Per-output synthesis notes | R | PASS | Structural explanation per output. |
| C-09 | Regression signals | A | PARTIAL | 3b present with N/A rule. Inertia field reproduced from index. No prior data. PARTIAL per N/A rule. |
| C-10 | Score arithmetic verification | A | PASS | 3a recomputation present. |
| C-11 | Evidence positive anchor | A | PASS | MODEL CELL at Phase 2 entry. |
| C-12 | Discrepancy declaration | A | PASS | "Matches stated score: YES \| NO" field. Inertia reproduced from index. |
| C-13 | Formula version delta declaration | A | PASS | 1b with both prior and current values. Inertia reproduced from index. |
| C-14 | Pre-scoring mechanism placement | A | PASS | MODEL CELL + ENTRY LOCK at Phase 2 entry. |
| C-15 | Symmetric comparison completeness | A | PASS | DELTA REGISTER two-column structure. Inertia reproduced from index. |
| C-16 | Phase-distinct mechanism distribution | A | PASS | Pre-Phase-1 (MECHANISM INDEX), Phase 1 (load + formula delta + DELTA REGISTER), Phase 2 (MODEL CELL), Phase 3 (arithmetic + regression). Four phases. |
| C-17 | Inertia departure labeling | A | PASS | MECHANISM INDEX pre-Phase-1 table has an "Inertia (failure prevented)" column declaring the departure label for every mechanism. At each mechanism during execution, the prompt requires "Inertia (C-01): [as declared in Mechanism Index -- ...]" reproduced as a labeled field. Double declaration: planned in index AND reproduced at execution. The mechanism index itself carries its own departure label: "Inertia (mechanism index): Without this pre-Phase-1 declaration, phase distribution (C-16) and departure labeling (C-17) depend on scorer memory." All mechanisms labeled. |
| C-18 | Bilateral symmetry audit sweep | A | FAIL | No 1d bilateral audit sweep section. The MECHANISM INDEX lists "BILATERAL SYMMETRY AUDIT SWEEP (1d)" as a declared mechanism at Phase 1 exit, but Phase 1 ends at "PHASE 1 COMPLETE" after 1c with no 1d section. Declaration in an index does not constitute execution -- no Symmetric: YES/NO per-comparison verdicts produced. C-15 compliance relies on the DELTA REGISTER prevention structure with no independent catch mechanism. |

**V-04 Score:**
```
essential_pass = 5/5
recommended_pass = 3/3
aspirational_pass = 8.5/10 (C-09 PARTIAL=0.5, C-18 FAIL=0, all others PASS=1 → 8×1 + 0.5 = 8.5)
composite = (5/5 * 60) + (3/3 * 30) + (8.5/10 * 10)
          = 60 + 30 + 8.5
          = 98.5
Golden: YES -- all essentials PASS; composite 98.5 >= 80
```

---

#### V-05: Axes N+O+K -- Full Integration

**Design summary:** Pre-Phase-1 MECHANISM INDEX with Inertia column (K), bilateral symmetry audit sweep at Phase 1 exit with Symmetric: YES/NO (O), and standardized "Inertia: [failure mode]" required fields reproduced at every mechanism (N). FORMULA CHANGE ALERT itself carries an Inertia label in the prompt. Highest-ceiling candidate.

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Rubric load verification | E | PASS | 1a with all four elements; "Inertia (C-01): Criteria count, formula denominator, and threshold unverified without this block." Mechanism declared in index AND reproduced at 1a. |
| C-02 | Per-criterion verdict matrix | E | PASS | Scoring table per output. |
| C-03 | Evidence for every verdict | E | PASS | Evidence standard: "each cell names a specific structural element, section heading, field label, or direct quote." MODEL CELL locatability test. |
| C-04 | Composite score per output | E | PASS | Explicit calculation with tier counts. aspirational denominator /10. |
| C-05 | Failure patterns section | E | PASS | Required even when empty. |
| C-06 | Ranked leaderboard | R | PASS | Standalone ranked structure. "See scores above" explicitly rejected. |
| C-07 | Excellence signals | R | PASS | Output-criterion-mechanism triple format required. |
| C-08 | Per-output synthesis notes | R | PASS | Structural mechanism explanation per output. |
| C-09 | Regression signals | A | PARTIAL | 3b present with N/A text. Inertia field: "An absent regression section is structurally indistinguishable from a section with no regressions." No prior data. PARTIAL per N/A rule. |
| C-10 | Score arithmetic verification | A | PASS | 3a recomputation present. |
| C-11 | Evidence positive anchor | A | PASS | MODEL CELL at Phase 2 entry. |
| C-12 | Discrepancy declaration | A | PASS | "Matches stated score: YES \| NO -- discrepancy: stated [X], computed [Y]" field. Inertia: "score checks out" is indistinguishable from silent pass-through; YES/NO forces explicit affirmation. |
| C-13 | Formula version delta declaration | A | PASS | 1b requires both prior (8) and current (10) values. Inertia: "N_aspirational=10" passes C-01 but fails C-15 (prior absent). |
| C-14 | Pre-scoring mechanism placement | A | PASS | MODEL CELL + ENTRY LOCK at Phase 2 entry. "Phase 2 protocol violation" if verdict written before model cell. |
| C-15 | Symmetric comparison completeness | A | PASS | DELTA REGISTER. 3b regression note: "Both verdicts required -- writing only the current verdict violates C-15." |
| C-16 | Phase-distinct mechanism distribution | A | PASS | Pre-Phase-1 (MECHANISM INDEX + FORMULA CHANGE ALERT labeled), Phase 1 (load + formula delta + DELTA REGISTER + bilateral sweep), Phase 2 (MODEL CELL), Phase 3 (arithmetic + regression). Four phases with active mechanisms. |
| C-17 | Inertia departure labeling | A | PASS | MECHANISM INDEX with Inertia column (pre-planned departure labels), reproduced as required "Inertia (C-XX): [text]" fields at 1a, 1b, 1c, 1d, MODEL CELL, 3a, 3b. FORMULA CHANGE ALERT itself carries "Inertia (FORMULA CHANGE ALERT): A scorer who does not read this alert may use the v4 denominator (/8)." The mechanism index has its own departure label: "Without this pre-Phase-1 declaration, phase distribution (C-16) and departure labeling (C-17) depend on scorer memory -- the index converts accidental compliance into a structural contract." Maximum departure-label coverage across all phases and mechanism types. |
| C-18 | Bilateral symmetry audit sweep | A | PASS | 1d BILATERAL SYMMETRY AUDIT SWEEP with Symmetric: YES/NO per-comparison verdicts. Required Inertia field: "J's DELTA REGISTER prevents asymmetric comparisons by requiring both columns. The AUDIT SWEEP provides an independent catch mechanism -- a Symmetric: NO cell is detectable by scanning the sweep without reading the register. An output can pass C-15 (both sides present through prevention) while failing C-18 (no independent catch)." Mechanism declared in index AND executed at Phase 1 exit. |

**V-05 Score:**
```
essential_pass = 5/5
recommended_pass = 3/3
aspirational_pass = 9.5/10 (C-09 PARTIAL=0.5, all others PASS=1 → 9×1 + 0.5 = 9.5)
composite = (5/5 * 60) + (3/3 * 30) + (9.5/10 * 10)
          = 60 + 30 + 9.5
          = 99.5
Golden: YES -- all essentials PASS; composite 99.5 >= 80
```

---

### PHASE 3: VERIFY

**3a. Arithmetic verification**

Verification (output: V-03):
```
stated counts: E=5/5, R=3/3, A=9.5/10
computed composite: (5/5 * 60) + (3/3 * 30) + (9.5/10 * 10)
                  = (1.0 * 60) + (1.0 * 30) + (0.95 * 10)
                  = 60 + 30 + 9.5
                  = 99.5
Matches stated score: YES
```

Inertia (C-12): "Verification performed" satisfies C-10 at PARTIAL but does not produce a binary result. The YES/NO field forces an explicit affirmation or names the exact discrepancy -- making arithmetic errors visible even when the scorer is not looking for them.

No discrepancy found. DELTA REGISTER Arithmetic row remains N/A.

**3b. Regression section**

No prior round data -- regression analysis cannot be performed. (Trace artifact: placeholder.)

Inertia (C-09): An absent regression section is structurally indistinguishable from a section with no regressions. The user cannot determine whether regressions were checked or skipped. Required even when empty -- presence confirms the check was performed.

---

### BILATERAL SYMMETRY AUDIT SWEEP (Phase 3 post-verify update)

| Comparison | Symmetric? |
|------------|-----------|
| N_aspirational (formula denominator) | YES -- Prior: 8 (v4), Current: 10 (v5) |
| Regression verdicts | PARTIAL -- no prior-round data; N/A rule invoked |
| Arithmetic discrepancies | PARTIAL -- no discrepancy found; N/A rule confirmed by Phase 3 verification |

All rows: YES or PARTIAL. No Symmetric: NO cells requiring remediation.

---

### SYNTHESIS

**LEADERBOARD**

| Rank | Output | Axes | Composite | Golden? |
|------|--------|------|-----------|---------|
| 1 (tie) | V-03 | N+O | 99.5 | YES |
| 1 (tie) | V-05 | N+O+K | 99.5 | YES |
| 3 | V-02 | O | 99.0 | YES |
| 4 (tie) | V-01 | N | 98.5 | YES |
| 4 (tie) | V-04 | K+N | 98.5 | YES |

All five outputs are Golden. Score spread: 1.0 point (98.5--99.5).

---

**EXCELLENCE SIGNALS**

Signal: V-03 and V-05 -- C-17 -- standardized "Required field after writing: Inertia (C-XX): [text]" directives convert departure labels from prompt-level advisory text (V-02's italic notes) into mandatory scorer output fields. V-02's "*Departure from inertia*" notes are framed as explanatory context that the scorer reads but need not reproduce; V-03's N-axis explicitly instructs "write this required labeled field" before giving the exact text to produce, making the labeled field structurally mandatory in the scorer's artifact.

Signal: V-02, V-03, V-05 -- C-18 -- bilateral audit sweep with per-comparison Symmetric: YES/NO at Phase 1 exit provides an independent catch mechanism for asymmetric comparisons, analogous to E-axis's YES/NO for arithmetic. V-01 and V-04 rely entirely on the DELTA REGISTER's two-column prevention; V-02/V-03/V-05 add a post-register sweep that detects a Symmetric: NO without requiring the reader to re-examine register prose column by column.

Signal: V-05 -- C-17 (depth) -- FORMULA CHANGE ALERT carries its own "Inertia (FORMULA CHANGE ALERT):" label in the prompt, and the mechanism index itself carries a departure label for the index mechanism. V-05 achieves full-stack departure labeling: pre-phase, all phases, and the meta-mechanism (the index) are all labeled. V-01/V-03/V-04 label all output-level mechanisms but leave the FORMULA CHANGE ALERT prompt section unlabeled.

---

**FAILURE PATTERNS**

No failure patterns -- all criteria passed in at least one output.

Note: C-18 fails in V-01 and V-04 (no bilateral sweep), and C-17 fails to PARTIAL in V-02 (no mandatory labeled field directives). These are single-variation gaps, not universal failures. No criterion receives zero PASS across all five outputs.

---

**PER-OUTPUT SYNTHESIS NOTES**

**V-01 (N only, 98.5):** V-01's score driver is Axis N -- converting M-axis informal departure notes into mandatory required output fields produces C-17 PASS. The design makes "Inertia: [failure mode]" a structural output artifact, not a motivation. V-01 scores identically to V-04 (98.5) despite having no mechanism index because both fail C-18 (no bilateral sweep). The N-axis alone cannot push V-01 to the ceiling because C-18 is unaddressed.

**V-02 (O only, 99.0):** V-02's score driver is Axis O -- the bilateral audit sweep at Phase 1 exit achieves C-18 PASS that V-01 and V-04 cannot reach. Its ceiling is bounded by C-17 PARTIAL: inheriting M-axis informal departure notes from R4 V-05 satisfies C-17 at 0.5, not 1.0. The informal "*Departure from inertia*" framing in V-02 serves as motivational context in the prompt but does not mandate labeled fields in the scorer's output. V-02 demonstrates that the bilateral sweep (O) contributes more score value (+0.5 from C-18 PASS) than is lost by the informal departure framing (−0.5 from C-17 PARTIAL) versus V-01, netting exactly 0.5 points higher.

**V-03 (N+O, 99.5 -- co-champion):** V-03 is the minimum combination achieving both C-17 PASS and C-18 PASS simultaneously. The mechanism index (K) is absent, but every output-level mechanism carries a required Inertia: field (N) and the bilateral sweep fires at Phase 1 exit with per-comparison Symmetric: YES/NO (O). V-03 ties V-05 exactly, establishing the key diagnostic finding: K is non-additive given N+O. The golden prompt for v5 is the V-03 design -- N+O without K.

**V-04 (K+N, 98.5):** V-04's MECHANISM INDEX provides the highest C-16/C-17 structural depth among the non-sweep variations: departure labels are pre-planned in a table before any phase begins and reproduced at each mechanism during execution. The double-declaration pattern (planned + reproduced) is structurally more rigorous than V-01's single-point required fields. However, V-04 fails C-18 for the same reason as V-01 -- the mechanism index declares the bilateral sweep as a mechanism but does not execute it. Declaration is not execution; the sweep must produce actual Symmetric: YES/NO verdicts to satisfy C-18. V-04 ties V-01 at 98.5 despite greater structural planning depth because C-18 is still FAIL.

**V-05 (N+O+K, 99.5 -- co-champion):** V-05 achieves maximum structural depth: the mechanism index is declared pre-Phase-1 (planning), departure labels are reproduced as required fields during execution (N), the bilateral sweep fires at Phase 1 exit (O), and even the FORMULA CHANGE ALERT prompt section carries its own Inertia label. V-05 ties V-03 at 99.5 rather than exceeding it because the mechanism index (K) adds planning artifacts that help C-16 reach 4 phases (vs V-03's 3) but cannot push any criterion from PASS to a higher tier -- the rubric has no tier above PASS. K's value is pedagogical (planning before execution) but not additive to composite score when N+O are already producing PASS on all criteria K targets.

---

**KEY DIAGNOSTIC FINDING:** V-03 == V-05 (both 99.5). The mechanism index (K) is non-additive given N+O. The golden prompt is the V-03 design.

---

```json
{"top_score": 99.5, "all_essential_pass": true, "new_patterns": ["Mandatory-field framing: requiring the scorer to write 'Inertia: [failure mode]' as an explicit required output field (not optional italic advisory) is what separates C-17 PASS from C-17 PARTIAL -- the distinction between V-01/V-03 and V-02 is not content but directive register", "N+O is the minimal sufficient combination for v5 ceiling: departure labels (N) and bilateral sweep (O) together achieve all PASS verdicts; mechanism index (K) adds pre-execution planning depth but is non-additive because no criterion can score above PASS regardless of structural redundancy"]}
```
