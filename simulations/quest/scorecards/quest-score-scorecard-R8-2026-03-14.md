## quest-score R8 — Scoring Run

---

### PREAMBLE

**Formula (v8):**
```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 16 * 10)

N_essential=4, N_recommended=3, N_aspirational=16
PASS=1.0, PARTIAL=0.5, FAIL=0.0
Golden threshold: all 4 essentials PASS AND composite ≥ 80
```

**Auto-PASS declarations:**
- C-05 auto-PASS when no criterion fails universally across all outputs
- C-07 auto-PASS when no prior-round trace exists
- C-08 auto-PASS when no failure patterns exist
- C-10 auto-PASS when no failure patterns exist

**Gate instruction:** Preamble must be fully written before any variation output file is opened.

**Prior-round trace:** placeholder — C-07 fires auto-PASS for all variations.

---

### STEP 1 — SETUP ROSTER

| ID | Tier | Diagnostic Question |
|----|------|---------------------|
| C-01 | Essential | Does the skill define a complete verdict matrix — every criterion × every output cell labeled PASS/PARTIAL/FAIL with no missing cells? |
| C-02 | Essential | Does the skill require verbatim or near-verbatim evidence quotes individually tied to each criterion verdict? |
| C-03 | Essential | Does the skill state the composite formula with the correct N values (N_essential=4, N_recommended=3, N_aspirational=16) and verify the score from the visible verdict table? |
| C-04 | Essential | Does the skill produce a ranked leaderboard ordering all scored variations by composite score? |
| C-05 | Recommended | Does the skill include a FAILURE PATTERNS section? (auto-PASS if no criterion fails universally) |
| C-06 | Recommended | Does the skill include an EXCELLENCE SIGNALS section surfacing structural improvements from top scorers? |
| C-07 | Recommended | Does the skill include regression signal detection against prior-round data? (auto-PASS if no prior trace) |
| C-08 | Aspirational | Does the skill provide actionable per-failure-pattern diagnosis? (auto-PASS if no failure patterns) |
| C-09 | Aspirational | Does the skill include score distribution commentary interpreting the spread and concentration of scores across tiers? |
| C-10 | Aspirational | Does the FAILURE PATTERNS action line contain an instantiated worked example tied to the current round's axis criterion? (auto-PASS if no failure patterns) |
| C-11 | Aspirational | Are auto-PASS rules stated explicitly in the preamble block? |
| C-12 | Aspirational | Is the composite formula present in the preamble block, not only in the body? |
| C-13 | Aspirational | Does each verdict cell present evidence before the PASS/PARTIAL/FAIL label within the cell? |
| C-14 | Aspirational | Is there at least one diagnostic question per criterion in the SETUP roster before scoring begins? |
| C-15 | Aspirational | Is there an explicit preamble gate instruction that prohibits opening output files until the preamble block is fully written? |
| C-16 | Aspirational | Are auto-PASS conditions stated as named standalone declarations (not implied by TBD placeholders or embedded in prose)? |
| C-17 | Aspirational | Does each criterion's diagnostic question interrogate the specific mechanism of that criterion rather than a generic probe applicable to any row? |
| C-18 | Aspirational | Is there a named standalone REGRESSION SIGNALS section in the scoring template body, not handled implicitly through SETUP notes or inline commentary? |
| C-19 | Aspirational | Is there an explicit preservation rule stating that the C-10 worked example must be carried forward verbatim or updated to match the current axis when the rubric is versioned? |
| C-20 | Aspirational | Is the C-10 preservation rule stated in imperative grammar ("must", "shall", "is required to") — not interrogative form ("has it been carried forward?") or conditional/weak-modal? |
| C-21 | Aspirational | Does the preservation rule lock the worked example to the FAILURE PATTERNS action line specifically — not SETUP, not a roster diagnostic question, not a preservation checkpoint? |
| C-22 | Aspirational | Does the preservation rule explicitly name FAILURE PATTERNS as the required location AND explicitly name SETUP as a disqualifying alternative? |
| C-23 | Aspirational | Does the C-20 diagnostic question enumerate ≥3 distinct grammatical form failures — interrogative ("Has it been carried forward?"), conditional ("If the axis shifts, carry forward the example"), and weak-modal ("should be carried forward")? |

---

### STEP 2 — SCORING MATRICES

---

#### V-01 — Baseline R8 Full Stack

| ID | Tier | Verdict | Evidence |
|----|------|---------|----------|
| C-01 | Essential | PASS | Verdict matrix covers all 23 criteria × all output variations; complete coverage stated in skill definition |
| C-02 | Essential | PASS | Evidence quotes required per C-13 evidence-before-verdict ordering rule; criterion-tied, not generic excerpts |
| C-03 | Essential | PASS | Formula explicitly states N_essential=4, N_recommended=3, N_aspirational=16; score verifiable from verdict table |
| C-04 | Essential | PASS | Ranked leaderboard present in output structure |
| C-05 | Recommended | PASS | FAILURE PATTERNS section present; no criterion fails universally → auto-PASS applies |
| C-06 | Recommended | PASS | EXCELLENCE SIGNALS section present |
| C-07 | Recommended | PASS | auto-PASS — prior-round trace is placeholder, no comparison data available |
| C-08 | Aspirational | PASS | auto-PASS — no failure patterns at essential/recommended tier |
| C-09 | Aspirational | PASS | Score distribution commentary included interpreting spread and tier concentration |
| C-10 | Aspirational | PASS | auto-PASS — no failure patterns; instantiated worked example present in FAILURE PATTERNS action line when failures exist |
| C-11 | Aspirational | PASS | Auto-PASS rules stated in preamble block (C-05, C-07, C-08, C-10) |
| C-12 | Aspirational | PASS | Composite formula with N values present in preamble |
| C-13 | Aspirational | PASS | Evidence-before-verdict ordering enforced within each verdict cell |
| C-14 | Aspirational | PASS | Per-criterion diagnostic question present in SETUP roster for all 23 criteria |
| C-15 | Aspirational | PASS | Explicit gate instruction: "Complete preamble before opening any output file" |
| C-16 | Aspirational | PASS | Named standalone auto-PASS declarations present (e.g., "C-07 auto-PASS when no prior trace") |
| C-17 | Aspirational | PASS | Mechanism-level questions per criterion — e.g., C-22 asks specifically about location language + SETUP exclusion phrase, not "is it well-formed?" |
| C-18 | Aspirational | PASS | Named standalone REGRESSION SIGNALS section in template body |
| C-19 | Aspirational | PASS | Preservation rule present: "must remain in the FAILURE PATTERNS action line — do not relocate it to SETUP, to a roster diagnostic question, or to a preservation checkpoint" |
| C-20 | Aspirational | PASS | Imperative form confirmed: "must remain" + "do not relocate" — enforceable instruction, not diagnostic probe |
| C-21 | Aspirational | PASS | Worked example locked to FAILURE PATTERNS action line; SETUP, roster, and preservation checkpoint all named as non-qualifying locations |
| C-22 | Aspirational | PASS | Preservation rule names "FAILURE PATTERNS action line" as required location AND "do not relocate it to SETUP" as explicit exclusion — both elements present |
| C-23 | Aspirational | PASS | Three disqualifying forms enumerated: (1) interrogative, (2) conditional, (3) weak-modal |

**Essential:** 4/4 → 60.0
**Recommended:** 3/3 → 30.0
**Aspirational:** 16/16 → 10.0
**Composite: 100.0**

---

#### V-02 — C-22 Ablation

| ID | Tier | Verdict | Evidence |
|----|------|---------|----------|
| C-01 | Essential | PASS | Same as V-01 — unaffected by ablation axis |
| C-02 | Essential | PASS | Same as V-01 |
| C-03 | Essential | PASS | Same as V-01 |
| C-04 | Essential | PASS | Same as V-01 |
| C-05 | Recommended | PASS | Same as V-01 |
| C-06 | Recommended | PASS | Same as V-01 |
| C-07 | Recommended | PASS | auto-PASS |
| C-08 | Aspirational | PASS | auto-PASS |
| C-09 | Aspirational | PASS | Same as V-01 |
| C-10 | Aspirational | PASS | Worked example present in FAILURE PATTERNS action line — C-21 location lock intact; ablation affects preservation rule text only |
| C-11 | Aspirational | PASS | Same as V-01 |
| C-12 | Aspirational | PASS | Same as V-01 |
| C-13 | Aspirational | PASS | Same as V-01 |
| C-14 | Aspirational | PASS | Same as V-01 |
| C-15 | Aspirational | PASS | Same as V-01 |
| C-16 | Aspirational | PASS | Same as V-01 |
| C-17 | Aspirational | PASS | Same as V-01 |
| C-18 | Aspirational | PASS | Same as V-01 |
| C-19 | Aspirational | PASS | Preservation rule present and imperative: "must be carried forward verbatim from the prior round, or updated to reflect the current round's new axis criterion" |
| C-20 | Aspirational | PASS | Imperative form intact: "must be carried forward verbatim" + "Do not replace the worked example with a format instruction placeholder" |
| C-21 | Aspirational | PASS | C-21 tests whether the preservation rule locks to FAILURE PATTERNS; here the rule is imperative and does not relocate the example — C-21 concerns the example's location, not whether the preservation rule names the location |
| C-22 | Aspirational | **FAIL** | Preservation rule reads "must be carried forward verbatim... Do not replace with a format instruction placeholder" — no mention of FAILURE PATTERNS as required location, no mention of SETUP as disqualifying alternative; both required elements absent |
| C-23 | Aspirational | PASS | Three disqualifying forms retained — ablation axis is C-22, not C-23 |

**Essential:** 4/4 → 60.0
**Recommended:** 3/3 → 30.0
**Aspirational:** 15 PASS + 1 FAIL → (15.0/16) × 10 = 9.375
**Composite: 99.4**

---

#### V-03 — C-23 PARTIAL Ablation

| ID | Tier | Verdict | Evidence |
|----|------|---------|----------|
| C-01–C-22 | All tiers | PASS | Single-axis ablation; all criteria unaffected by removal of weak-modal form |
| C-23 | Aspirational | **PARTIAL** | Two disqualifying forms only: "(1) interrogative — 'Has the worked example been carried forward?' earns C-19 PARTIAL + C-20 FAIL; (2) conditional — 'If the axis shifts, carry forward the example' earns C-20 FAIL." Weak-modal form ("should be carried forward") absent; a scorer using V-03 would approve "The worked example should be carried forward" as a valid preservation rule |

**Essential:** 4/4 → 60.0
**Recommended:** 3/3 → 30.0
**Aspirational:** 15 PASS + 1 PARTIAL → (15.5/16) × 10 = 9.6875
**Composite: 99.7**

---

#### V-04 — C-23 FAIL Ablation

| ID | Tier | Verdict | Evidence |
|----|------|---------|----------|
| C-01–C-22 | All tiers | PASS | Single-axis ablation; all criteria unaffected by reduction to single-form diagnostic |
| C-23 | Aspirational | **FAIL** | One disqualifying form only: "Does the primary preservation rule contain a mandatory verb ('must', 'shall', 'is required to')? Interrogative form earns C-20 FAIL — 'Has the worked example been carried forward?' is a diagnostic probe, not an enforceable instruction." Neither conditional nor weak-modal forms enumerated; a scorer using V-04 approves both "If the axis shifts, carry forward the example" and "The worked example should be carried forward" as passing C-20 |

**Essential:** 4/4 → 60.0
**Recommended:** 3/3 → 30.0
**Aspirational:** 15 PASS + 1 FAIL → (15.0/16) × 10 = 9.375
**Composite: 99.4**

---

#### V-05 — Combination Pass (C-24 Seed)

| ID | Tier | Verdict | Evidence |
|----|------|---------|----------|
| C-01–C-23 | All tiers | PASS | All V-01 structures retained; single addition is the C-22 diagnostic three-scale enumeration, which is not a currently scored criterion |

Note on C-24 (unscored): V-05 adds "Three verdict cases with structural contrasts: (FAIL) rule is imperative but contains no location language — e.g., 'must be carried forward verbatim' without any FAILURE PATTERNS reference; (PARTIAL) rule names the required location ('must remain in the FAILURE PATTERNS action line') but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase." This element seeds C-24 but does not affect the composite under the v8 rubric.

**Essential:** 4/4 → 60.0
**Recommended:** 3/3 → 30.0
**Aspirational:** 16/16 → 10.0
**Composite: 100.0**

---

### STEP 3 — COMPOSITE SUMMARY

| Variation | Essential | Recommended | Aspirational Raw | Composite |
|-----------|-----------|-------------|-----------------|-----------|
| V-01 | 60.0 | 30.0 | 16.0/16 → 10.000 | **100.0** |
| V-05 | 60.0 | 30.0 | 16.0/16 → 10.000 | **100.0** |
| V-03 | 60.0 | 30.0 | 15.5/16 → 9.688 | **99.7** |
| V-02 | 60.0 | 30.0 | 15.0/16 → 9.375 | **99.4** |
| V-04 | 60.0 | 30.0 | 15.0/16 → 9.375 | **99.4** |

---

### RANKED LEADERBOARD

| Rank | Variation | Composite | Losing Criterion | Notes |
|------|-----------|-----------|-----------------|-------|
| 1 | **V-05** | 100.0 | — | Full stack + C-24 seed; structural tiebreak over V-01 |
| 2 | **V-01** | 100.0 | — | Full stack baseline |
| 3 | **V-03** | 99.7 | C-23 PARTIAL | 2-form diagnostic misses weak-modal |
| 4 | **V-02** | 99.4 | C-22 FAIL | Preservation rule lacks location language entirely |
| 4 | **V-04** | 99.4 | C-23 FAIL | 1-form diagnostic; conditional + weak-modal undetectable |

**Golden threshold** (all 4 essential PASS AND composite ≥ 80): **All five variations qualify.**

**Tiebreak note (V-01 vs V-05):** Identical composite under v8 rubric. V-05 ranked #1 on structural richness: it instantiates the same three-scale diagnostic pattern at C-22 that C-23 instantiates at C-20, reducing scorer ambiguity at the PARTIAL/FAIL boundary for a criterion that V-01 leaves underspecified.

**Tiebreak note (V-02 vs V-04):** Both lose exactly one aspirational point (0.625 pts) for different structural deficiencies — location omission (V-02) and form under-enumeration (V-04). No basis for breaking the tie under the current formula; both occupy rank 4.

---

### FAILURE PATTERNS

No essential or recommended criteria fail in any variation. All five variations are gold-qualified.

**Aspirational failures (3 instances across 2 criteria):**

**C-22 FAIL — V-02:** Preservation rule omits location language entirely. The rule "must be carried forward verbatim... Do not replace the worked example with a format instruction placeholder" satisfies C-19 (rule present) and C-20 (imperative form) but leaves the target location unspecified. A versioner reading this rule knows to preserve the example but cannot determine whether FAILURE PATTERNS or SETUP is the correct destination. The SETUP relocation trap — the exact failure C-22 was designed to prevent — remains open.

_Action:_ The preservation rule must contain both (a) "must remain in the FAILURE PATTERNS action line" and (b) an explicit disqualifying phrase such as "do not relocate it to SETUP." Neither element alone satisfies C-22; both are required.

**C-23 PARTIAL — V-03:** The C-20 diagnostic enumerates interrogative and conditional forms but omits weak-modal. A scorer using V-03 approves "The worked example should be carried forward" as a valid preservation rule because the word "should" is not in the FAIL list. The weak-modal gap means exactly one disqualifying grammatical pattern is undetectable.

_Action:_ Add weak-modal form: "weak-modal — 'The worked example should be carried forward' earns C-20 FAIL; 'should' converts an instruction into a suggestion, removing enforceability at version time."

**C-23 FAIL — V-04:** The C-20 diagnostic enumerates interrogative only. Both conditional ("If the axis shifts, carry forward the example") and weak-modal ("should be carried forward") survive V-04 scoring. A scorer using V-04 would PASS both forms, since the only check is presence of a mandatory verb — and interrogative form is the only named failure.

_Action:_ Enumerate all three disqualifying forms with structural contrasts. The three-form ladder (V-04 FAIL → V-03 PARTIAL → V-01 PASS) is the evidence corpus that grounds C-23 for future rounds.

---

### EXCELLENCE SIGNALS

**From V-05 (structural tiebreak leader):**

**Signal 1 — C-22 diagnostic three-scale enumeration.** V-05 adds to the C-22 row: FAIL case ("imperative but no location language — e.g., 'must be carried forward verbatim' without any FAILURE PATTERNS reference"), PARTIAL case ("names the required location but omits explicit SETUP exclusion language"), PASS case ("contains both the required location phrase and an explicit SETUP exclusion phrase"). This is structurally identical to what C-23 does for C-20: a three-scale FAIL/PARTIAL/PASS enumeration with contrasting structural examples at each verdict level. Without it, the C-22 PARTIAL/FAIL boundary is described but not illustrated — the same gap that motivated C-23.

**Signal 2 — recursive three-scale enumeration principle.** Both C-23 and V-05's C-24 seed apply the same structural solution: when a criterion defines a non-trivial PARTIAL threshold (one element present, one absent), the criterion's diagnostic question should enumerate all three verdict cases with distinct structural contrasting examples. This is now the second instance of the pattern. C-23 applied it to C-20 (imperative vs interrogative/conditional/weak-modal); V-05 applies it to C-22 (location + exclusion vs. location only vs. neither). The principle generalizes: any aspirational criterion with a PARTIAL verdict that turns on the presence or absence of a specific phrase benefits from three-scale enumeration rather than a binary diagnostic.

---

### REGRESSION SIGNALS

Prior-round trace: placeholder — **auto-PASS.** No regression comparison available for R8. Regression detection deferred to R9 when R8 trace artifacts are available.

---

### SCORE DISTRIBUTION COMMENTARY

Score range: 99.4–100.0 (0.6-point spread). All five variations pass the golden threshold. The tight spread confirms that C-22 and C-23 are correctly classified as aspirational: their absence narrows rubric precision at scoring-time decision boundaries (location ambiguity; multi-form blind spots) but does not compromise the essential contract (verdict matrix, evidence, composite, leaderboard). The 0.6-point ceiling on aspirational loss is a direct consequence of each failing criterion contributing exactly 0.625 points (10 / 16 per criterion). V-02 and V-04 tie at 99.4 despite failing on structurally distinct deficiencies — this is expected and desirable: the scoring formula does not penalize location failures more or less than form-enumeration failures. The evidence ladder design (V-04 FAIL / V-03 PARTIAL / V-01 PASS on C-23; V-02 FAIL / V-01 PASS on C-22) provides the minimum corpus needed to ground both criteria for panel review in R9.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["V-05 — C-22 diagnostic three-scale enumeration: the C-22 diagnostic question in the SETUP roster should enumerate all three verdict cases with structural contrasting examples (FAIL: imperative but no location language; PARTIAL: required location named but SETUP exclusion absent; PASS: both required location phrase and explicit SETUP exclusion phrase present) — the same three-scale pattern that C-23 applies to C-20, now applied to C-22 itself, seeding C-24", "V-05 — recursive three-scale enumeration principle: any aspirational criterion with a non-trivial PARTIAL threshold (one required element present, one absent) benefits from having its diagnostic question enumerate all three verdict cases with distinct structural contrasting examples; demonstrated by C-23 for C-20 and V-05 for C-22 — suggests a general design rule: when adding a criterion with a PARTIAL case, the criterion-level diagnostic question should always instantiate the FAIL/PARTIAL/PASS ladder with structural contrasts rather than a binary probe"]}
```
