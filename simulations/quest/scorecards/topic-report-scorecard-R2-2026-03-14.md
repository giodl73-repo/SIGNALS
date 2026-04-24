## Round 2 Scorecard — `topic-report`

Written to `simulations/quest/scorecards/topic-report-scorecard-R2-2026-03-14.md`.

---

### Summary Table

| Rank | Variation | C-09 | C-10 | C-11 | C-12 | Aspirational | Score | Golden? |
|------|-----------|------|------|------|------|--------------|-------|---------|
| 1 | V-02 Branch isolation | PASS | PASS | PASS | PASS | 4/4 | **100** | YES |
| 1 | V-03 Contract register | PASS | PASS | PASS | PASS | 4/4 | **100** | YES |
| 1 | V-04 Combined (V-01+V-02) | PASS | PASS | PASS | PASS | 4/4 | **100** | YES |
| 1 | V-05 All three combined | PASS | PASS | PASS | PASS | 4/4 | **100** | YES |
| 5 | V-01 Bidirectional only | PASS | PASS | PASS | FAIL | 3/4 | **97.5** | YES |

---

### Key Findings

**C-12 is the sole discriminator.** All five variations pass C-09, C-10, and C-11. The single split: V-01 lacks explicit branch isolation; V-02–V-05 all have structural isolation ("sealed branches" or "execute only / skip").

**C-11 does not discriminate in R2.** Every variation includes some form of bidirectionality — V-01/V-04/V-05 via named COMPLETENESS/EXCLUSIVITY sub-rules, V-02 via compound phrasing ("every name… and only names"), V-03 via G-7a/G-7b guarantee conditions. All forms pass.

**Why V-01 fails C-12:** No branch sealing instruction. Without "do not reference the other branch," a model may read both default and teams format descriptions and carry patterns across — even when the default format's SLOT 2 has no backtick notation. C-12's aspirational bar requires the structural guarantee, not just the absence of a known contamination source.

**Recommended golden: V-05** — combines all three mechanisms. **Minimal fix: V-04** — COMPLETENESS/EXCLUSIVITY + sealed branches, 100/100 with lower overhead.

### New Patterns vs Round 1

1. **COMPLETENESS/EXCLUSIVITY naming** — naming both directions as separate invariants closes the "used verbatim" ambiguity gap; each direction becomes independently verifiable
2. **Branch sealing instruction** — "branches are sealed; do not reference the other branch" is the structural mechanism C-12 requires; explicit prohibition (C-10) alone is insufficient

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["COMPLETENESS/EXCLUSIVITY naming — bidirectionality must be stated as two separately named invariants to close the 'used verbatim' ambiguity gap from R1 V-05; named sub-rules make each direction independently verifiable and more reliable in live execution than compound phrasing alone", "Branch sealing instruction — 'branches are sealed; do not reference the other branch's format descriptions' is the structural mechanism that guarantees C-12 compliance; explicit character prohibition (C-10) is necessary but not sufficient because a model may read both branches and carry patterns across without structural isolation"]}
```
Readiness statement calibrated | PASS | Readiness tied to BLOCKERS list; "If BLOCKERS is none: Ready..." enforces calibration |
| C-05 | Recommended next step present | PASS | SLOT 4 / Next Step requires specific skill + namespace; highest-priority open signal; generic steps rejected |
| C-06 | --format teams compact ASCII | PASS | Teams card spec: <=40 lines, <=80 chars, four required sections, + - | table borders |
| C-07 | Matches topic-status output | PASS | Same discovery logic (glob + strategy.md); CHECKPOINT-locked counts are ground truth |
| C-08 | Open signals include namespace + type | PASS | Open-signal entries include both namespace and skill type in format |
| C-09 | Readiness names blocking signals | PASS | SLOT 3 "The sentence is governed by rule 2c (bidirectional): COMPLETENESS/EXCLUSIVITY" + example |
| C-10 | Teams card prohibition explicitly enumerated | PASS | "No backtick characters (`) anywhere in the card"; "No angle-bracket characters (< or >) anywhere in the card" — explicit by name |
| C-11 | BLOCKERS block with bidirectional constraint | PASS | 2b emits BLOCKERS block explicitly; 2c names COMPLETENESS (cannot omit) + EXCLUSIVITY (cannot introduce) as separate rules; "Both constraints hold simultaneously. Do not add... Do not drop..." |
| C-12 | Teams card structural isolation | FAIL | No explicit branch isolation between default and teams rendering paths. SLOT 2 uses plain dash format (contamination source absent) but a model reading PHASE 3 in full may carry format patterns across without structural constraint |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 3/4 (C-09 PASS, C-10 PASS, C-11 PASS, C-12 FAIL)

```
composite = (5/5 * 60) + (3/3 * 30) + (3/4 * 10)
          = 60 + 30 + 7.5
          = 97.5
```

**Score: 97.5 / 100 — GOLDEN**

Note: V-01's C-11 mechanism (named COMPLETENESS/EXCLUSIVITY sub-rules) is the strongest bidirectionality design among all five. C-12 is the sole failure: absence of a known contamination source is not equivalent to structural isolation.

---

### V-02: Branch isolation

Explicit "sealed branches" instruction between default and teams rendering paths. Bidirectionality via compound phrasing ("every name in this list and only names in this list").

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Artifact written + path echoed | PASS | Write instruction with deterministic path + PHASE 4 / STEP 5 CONFIRM echo |
| C-02 | Progress table with accurate counts | PASS | 1d / STEP 1 CHECKPOINT locks counts before render; "values from PHASE 1 only — do not re-derive"; Total row present |
| C-03 | Open signals listed with owners | PASS | SLOT 2 / Open Signals list requires namespace, skill type, and owner per entry; "unassigned" default |
| C-04 | Readiness statement calibrated | PASS | Readiness tied to BLOCKERS list; "If BLOCKERS is none: Ready..." enforces calibration |
| C-05 | Recommended next step present | PASS | SLOT 4 / Next Step requires specific skill + namespace; highest-priority open signal; generic steps rejected |
| C-06 | --format teams compact ASCII | PASS | Teams card spec: <=40 lines, <=80 chars, four required sections, + - | table borders |
| C-07 | Matches topic-status output | PASS | Same discovery logic (glob + strategy.md); CHECKPOINT-locked counts are ground truth |
| C-08 | Open signals include namespace + type | PASS | Open-signal entries include both namespace and skill type in slash-notation |
| C-09 | Readiness names blocking signals | PASS | Branch A: "Must cite every name in PHASE 2 BLOCKERS list, no more and no less." + Branch B READINESS line |
| C-10 | Teams card prohibition explicitly enumerated | PASS | Branch B Rule 1: "Zero backtick characters (`). Tolerate none."; Rule 2: "Zero angle-bracket characters (< and >). Tolerate none." — strongest character-level enumeration |
| C-11 | BLOCKERS block with bidirectional constraint | PASS | 2b emits BLOCKERS block; 2c: "must reference every name in this list and only names in this list. Do not revise this list in PHASE 3." Bidirectional via compound phrasing |
| C-12 | Teams card structural isolation | PASS | PHASE 3 explicitly states "The branches are sealed — do not reference the other branch's format descriptions when executing." Branch A and B separated by visual dividers with explicit scoping labels; character rules for Branch B include scan-level instructions |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 4/4

```
composite = (5/5 * 60) + (3/3 * 30) + (4/4 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

Note: V-02's C-11 uses compound phrasing rather than named sub-rules; functionally equivalent for the rubric criterion, slightly less explicit in live runs where a model may fail each direction independently. C-12 sealed-branches mechanism is the most transferable design pattern across skill types.

---

### V-03: Contract register

G-n guarantee framing with G-7a/G-7b as separately named guarantee conditions. Branch isolation via "execute only / skip" selection instruction.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Artifact written + path echoed | PASS | Write instruction with deterministic path + PHASE 4 / STEP 5 CONFIRM echo |
| C-02 | Progress table with accurate counts | PASS | 1d / STEP 1 CHECKPOINT locks counts before render; "values from PHASE 1 only — do not re-derive"; Total row present |
| C-03 | Open signals listed with owners | PASS | SLOT 2 / Open Signals list requires namespace, skill type, and owner per entry; "unassigned" default |
| C-04 | Readiness statement calibrated | PASS | Readiness tied to BLOCKERS list; "If BLOCKERS is none: Ready..." enforces calibration |
| C-05 | Recommended next step present | PASS | SLOT 4 / Next Step requires specific skill + namespace; highest-priority open signal; generic steps rejected |
| C-06 | --format teams compact ASCII | PASS | Teams card spec: <=40 lines, <=80 chars, four required sections, + - | table borders |
| C-07 | Matches topic-status output | PASS | Same discovery logic (glob + strategy.md); CHECKPOINT-locked counts are ground truth |
| C-08 | Open signals include namespace + type | PASS | Open-signal entries include both namespace and skill type in format |
| C-09 | Readiness names blocking signals | PASS | G-7a/G-7b in STEP 2 + STEP 4A "Apply G-7a and G-7b simultaneously" + example with named signals |
| C-10 | Teams card prohibition explicitly enumerated | PASS | G-8: "zero backtick characters (`) and zero angle-bracket characters (< and >), verified character by character" — count guarantee framing |
| C-11 | BLOCKERS block with bidirectional constraint | PASS | STEP 2 emits BLOCKERS; G-7a COMPLETENESS + G-7b EXCLUSIVITY named as separate guarantee conditions; "Both G-7a and G-7b are required. This list is final." Most formal bidirectionality design |
| C-12 | Teams card structural isolation | PASS | STEP 3 BRANCH SELECTION: "If --format teams is set, execute STEP 4B only. Skip STEP 4A." Functional isolation via execute-only/skip instruction; G-8 character-count verification in STEP 4B |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 4/4

```
composite = (5/5 * 60) + (3/3 * 30) + (4/4 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

Note: V-03's C-12 mechanism ("execute only, skip") differs from V-02/V-04/V-05's sealed-branches language but achieves the same structural isolation. G-8 framed as a count guarantee ("zero backtick characters") rather than a prohibition imperative is an independent quality signal worth carrying into future variations.

---

### V-04: V-01 + V-02 combined

COMPLETENESS/EXCLUSIVITY named sub-rules (V-01 mechanism) plus sealed branches (V-02 mechanism). Minimal overhead, full structural coverage.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Artifact written + path echoed | PASS | Write instruction with deterministic path + PHASE 4 / STEP 5 CONFIRM echo |
| C-02 | Progress table with accurate counts | PASS | 1d / STEP 1 CHECKPOINT locks counts before render; "values from PHASE 1 only — do not re-derive"; Total row present |
| C-03 | Open signals listed with owners | PASS | SLOT 2 / Open Signals list requires namespace, skill type, and owner per entry; "unassigned" default |
| C-04 | Readiness statement calibrated | PASS | Readiness tied to BLOCKERS list; "If BLOCKERS is none: Ready..." enforces calibration |
| C-05 | Recommended next step present | PASS | SLOT 4 / Next Step requires specific skill + namespace; highest-priority open signal; generic steps rejected |
| C-06 | --format teams compact ASCII | PASS | Teams card spec: <=40 lines, <=80 chars, four required sections, + - | table borders |
| C-07 | Matches topic-status output | PASS | Same discovery logic (glob + strategy.md); CHECKPOINT-locked counts are ground truth |
| C-08 | Open signals include namespace + type | PASS | Open-signal entries include both namespace and skill type in format |
| C-09 | Readiness names blocking signals | PASS | SLOT 3 "Apply rule 2c (bidirectional): COMPLETENESS/EXCLUSIVITY" + example with named signals |
| C-10 | Teams card prohibition explicitly enumerated | PASS | "Zero backtick characters (`). None anywhere."; "Zero angle-bracket characters (< and >). None anywhere." |
| C-11 | BLOCKERS block with bidirectional constraint | PASS | 2c names COMPLETENESS + EXCLUSIVITY as separate explicit rules; "Both constraints required simultaneously. This list is closed." |
| C-12 | Teams card structural isolation | PASS | "The branches are sealed — do not reference the other branch's format descriptions when executing." Branch A uses plain slash notation (no backtick); Branch B has CHARACTER RULES with scan-level enforcement |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 4/4

```
composite = (5/5 * 60) + (3/3 * 30) + (4/4 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

Note: V-04 is the minimal structural fix over V-01 — adds only sealed-branches language. Achieves 100/100 without contract register overhead. This is the lowest-complexity path to full aspirational coverage in R2.

---

### V-05: All three combined

G-n contract register + COMPLETENESS/EXCLUSIVITY named sub-rules + sealed branches. Highest design robustness.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Artifact written + path echoed | PASS | Write instruction with deterministic path + PHASE 4 / STEP 5 CONFIRM echo |
| C-02 | Progress table with accurate counts | PASS | 1d / STEP 1 CHECKPOINT locks counts before render; "values from PHASE 1 only — do not re-derive"; Total row present |
| C-03 | Open signals listed with owners | PASS | SLOT 2 / Open Signals list requires namespace, skill type, and owner per entry; "unassigned" default |
| C-04 | Readiness statement calibrated | PASS | Readiness tied to BLOCKERS list; "If BLOCKERS is none: Ready..." enforces calibration |
| C-05 | Recommended next step present | PASS | SLOT 4 / Next Step requires specific skill + namespace; highest-priority open signal; generic steps rejected |
| C-06 | --format teams compact ASCII | PASS | Teams card spec: <=40 lines, <=80 chars, four required sections, + - | table borders |
| C-07 | Matches topic-status output | PASS | Same discovery logic (glob + strategy.md); CHECKPOINT-locked counts are ground truth |
| C-08 | Open signals include namespace + type | PASS | Open-signal entries include both namespace and skill type in format |
| C-09 | Readiness names blocking signals | PASS | G-7 contract with G-7a/G-7b named separately; "name every BLOCKER, name only BLOCKERs" enforced in both branches |
| C-10 | Teams card prohibition explicitly enumerated | PASS | G-8 same as V-03 + character-level scan instruction; count guarantee framing over imperative prohibition |
| C-11 | BLOCKERS block with bidirectional constraint | PASS | G-7a/G-7b named as separate guarantee conditions; "This list is closed and final. It cannot be revised in PHASE 3. Both G-7a and G-7b are required simultaneously." Strongest bidirectionality design |
| C-12 | Teams card structural isolation | PASS | "The branches are sealed — do not reference the other branch's format descriptions when executing." + G-8 character-by-character scan in Branch B. Strongest isolation design |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 4/4

```
composite = (5/5 * 60) + (3/3 * 30) + (4/4 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

Note: V-05 combines the strongest available mechanism for each aspirational criterion: G-7a/G-7b naming for C-11, sealed branches + G-8 character scan for C-12, count-guarantee framing for C-10. Highest robustness for live execution.

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? | C-11 mechanism | C-12 mechanism |
|------|-----------|-----------|-------------|--------------|-----------|---------|----------------|----------------|
| 1 | V-02 Branch isolation | 5/5 | 3/3 | 4/4 | **100** | YES | compound phrasing ("every name... and only names") | sealed branches language |
| 1 | V-03 Contract register | 5/5 | 3/3 | 4/4 | **100** | YES | G-7a/G-7b named guarantee conditions | execute-only / skip selection |
| 1 | V-04 V-01+V-02 combined | 5/5 | 3/3 | 4/4 | **100** | YES | COMPLETENESS + EXCLUSIVITY named sub-rules | sealed branches language |
| 1 | V-05 All three combined | 5/5 | 3/3 | 4/4 | **100** | YES | G-7a/G-7b + COMPLETENESS/EXCLUSIVITY (strongest) | sealed branches + G-8 scan (strongest) |
| 5 | V-01 Bidirectional BLOCKERS | 5/5 | 3/3 | 3/4 | **97.5** | YES | COMPLETENESS + EXCLUSIVITY named sub-rules | none — no branch isolation |

**C-12 is the sole full-point discriminator in R2.** V-01 fails C-12 despite having the clearest C-11 language; absence of a contamination source is not equivalent to structural isolation.

**C-11 does not discriminate in R2** because all five variations implement bidirectionality in some form. Any of the three mechanisms (named sub-rules, compound phrasing, named guarantee conditions) is sufficient for the rubric criterion.

---

## Discriminator Analysis

**C-12 is the R2 discriminator.** All five variations pass C-09, C-10, and C-11. The single split is V-01 failing C-12.

**Why V-01 fails C-12**: V-01 eliminates the primary contamination source (SLOT 2 uses plain dash format, no backtick notation) but does not structurally prevent a model from reading both the default and teams rendering sections during execution. Without an instruction that constrains which section descriptions are processed — "sealed branches" or "execute only, skip" — cross-branch pattern carry-over is possible even when no specific contamination source is identified.

**Why V-02 through V-05 pass C-12**: Each implements structural isolation that constrains which branch descriptions the model processes at execution time.

| Variation | C-12 structural mechanism |
|-----------|--------------------------|
| V-02 | "The branches are sealed — do not reference the other branch's format descriptions when executing." |
| V-03 | "If --format teams is set, execute STEP 4B only. Skip STEP 4A." |
| V-04 | "The branches are sealed — do not reference the other branch's format descriptions when executing." |
| V-05 | "The branches are sealed — do not reference the other branch's format descriptions when executing." + G-8 character-by-character scan |

**C-11 forms in R2**: Three syntactic forms all satisfy the criterion.

| Form | Used by | Mechanism |
|------|---------|-----------|
| Named sub-rules | V-01, V-04, V-05 | COMPLETENESS and EXCLUSIVITY as separately labeled rules |
| Compound phrasing | V-02 | "every name in this list and only names in this list" |
| Named guarantee conditions | V-03, V-05 | G-7a and G-7b as separately labeled output guarantees |

The R2 experiment confirms: bidirectionality in any of these three forms is sufficient for C-11; structural isolation of the teams rendering path is necessary and sufficient for C-12.

---

## Excellence Signals — Round 2

### E-1: COMPLETENESS/EXCLUSIVITY naming closes the C-11 ambiguity gap from R1

R1 V-05's "reference by name" instruction passed C-09 under v1 but was ambiguous under v2's C-11, which requires that the readiness sentence cannot ADD names (exclusivity) AND cannot DROP names (completeness) from the pre-computed BLOCKERS block. Naming both directions as separate sub-rules — COMPLETENESS and EXCLUSIVITY — makes each independently verifiable and removes the "used verbatim" ambiguity. A model can fail each direction independently when they are separately labeled; compound phrasing achieves functional equivalence for the rubric criterion but provides less granular failure diagnosis in live runs. Named sub-rules are more durable under iterative spec refinement because each direction is a separately auditable invariant.

### E-2: Branch sealing is the structural mechanism for C-12

Explicit character-level prohibition (C-10) is necessary but not sufficient for C-12. C-10 ensures the spec forbids backticks; C-12 requires the spec structurally prevents cross-branch contamination. Without branch isolation, a model may process both the default and teams rendering descriptions during execution and carry format patterns across — even when the specific contamination source from R1 (backtick notation in SLOT 2) has been removed. The "sealed branches" or "execute only / skip" instruction eliminates this risk by constraining which branch descriptions the model reads at execution time. This is the specific design pattern C-12 was created to require.

### E-3: Contract register (G-n guarantees) raises formalism without adding spec overhead

V-03 and V-05's contract framing — listing output guarantees G-1 through G-8 before execution steps — makes guarantees independently testable rather than buried in procedural instructions. G-7a/G-7b as separately named conditions is the most explicit bidirectionality design for C-11. G-8 framed as "zero backtick characters, verified character by character" is a count guarantee rather than a prohibition imperative: models are more likely to comply with a count-zero guarantee (verify and confirm the count is zero) than an imperative prohibition (do not emit backticks), because the count framing triggers a verification behavior rather than a suppression behavior.

---

## Recommended Golden Candidate

**V-05** is the recommended golden candidate. Combines all three mechanisms and achieves highest design robustness:
- G-7a/G-7b COMPLETENESS/EXCLUSIVITY as named guarantee conditions (strongest C-11 language)
- Sealed branches + G-8 character-by-character scan (strongest C-12 design)
- Contract register with G-n naming (most verifiable spec format; count-guarantee framing for C-10)

**V-04** is the minimal structural fix: COMPLETENESS/EXCLUSIVITY named sub-rules + sealed branches achieves 100/100 without contract register overhead. Lowest-complexity path to full aspirational coverage.

**V-03** achieves 100 via contract register + execute-only/skip branch selection, demonstrating that "execute only, skip" is a valid alternative to "sealed" language for C-12. The G-8 count-guarantee framing for C-10 is an independent quality signal worth carrying into future variations.

---

## New Patterns vs Round 1

Round 1 established:
1. BLOCKERS phase before readiness
2. Explicit character enumeration (backticks, angle brackets) over catch-all

Round 2 adds:
1. **COMPLETENESS/EXCLUSIVITY naming** — bidirectionality must be stated as two separately named invariants to close the "used verbatim" ambiguity gap from R1 V-05; COMPLETENESS (cannot omit) and EXCLUSIVITY (cannot add) as named sub-rules make each direction independently verifiable and more reliable in live execution than compound phrasing alone; compound phrasing is sufficient for the rubric criterion but not for granular failure diagnosis
2. **Branch sealing instruction** — "branches are sealed; do not reference the other branch's format descriptions" is the structural mechanism that guarantees C-12 compliance; explicit character prohibition (C-10) is necessary but not sufficient because a model may read both branches and carry patterns across without structural isolation; "execute only, skip" is a valid alternative form

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["COMPLETENESS/EXCLUSIVITY naming — bidirectionality must be stated as two separately named invariants to close the 'used verbatim' ambiguity gap from R1 V-05; COMPLETENESS (cannot omit) and EXCLUSIVITY (cannot add) as named sub-rules make each direction independently verifiable and more reliable in live execution than compound phrasing alone", "Branch sealing instruction — 'branches are sealed; do not reference the other branch's format descriptions' is the structural mechanism that guarantees C-12 compliance; explicit character prohibition (C-10) is necessary but not sufficient because a model may read both branches and carry patterns across without structural isolation"]}
```
