## Scorecard: quest-rubric — Round 2

**Rubric**: v2 | **Trace**: prompt-quality projections

### Scoring Grid

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 All 5 fields present | essential | PASS | PASS | PASS | PASS | PASS |
| C-02 Weight distribution in spec | essential | PASS | PASS | PASS | PASS | PASS |
| C-03 Formula + threshold stated | essential | PASS | PASS | PASS | PASS | PASS |
| C-04 Criteria are skill-specific | essential | **PASS** | PARTIAL | PASS | PASS | PASS |
| C-05 Pass conditions binary/testable | essential | PASS | PASS | PASS | PASS | PASS |
| C-06 Ordered by tier | recommended | PASS | PASS | PASS | PASS | PASS |
| C-07 Categories from allowed set | recommended | PARTIAL | PASS | PARTIAL | PASS | PASS |
| C-08 Distinct failure modes | recommended | **PASS** | PARTIAL | PARTIAL | PASS | PASS |
| C-09 Rubric is calibrated | aspirational | PARTIAL | PARTIAL | PASS | PARTIAL | PASS |
| C-10 Evolution hook present | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-11 Inertia framing before criteria | aspirational | PARTIAL | FAIL | FAIL | PARTIAL | **PASS** |
| C-12 Closed-world gates | aspirational | PARTIAL | PASS | PARTIAL | PASS | PASS |
| C-13 Rejection log proves filter ran | aspirational | **PASS** | FAIL | FAIL | PASS | PASS |

### Composite Scores

| | Essential (60) | Recommended (30) | Aspirational (10) | Total | Golden |
|--|--|--|--|--|--|
| V-01 | 60 | 25 | 7 | **92** | YES |
| V-02 | 54 | 25 | 5 | **84** | NO |
| V-03 | 60 | 20 | 5 | **85** | YES |
| V-04 | 60 | 30 | 8 | **98** | YES |
| V-05 | 60 | 30 | 10 | **100** | YES |

**Ranking**: V-05 (100) > V-04 (98) > V-01 (92) > V-03 (85) > V-02 (84)

**Ranking shift from R1**: V-05 > V-03 > V-04 > V-02 > V-01 → V-05 > V-04 > **V-01** > V-03 > V-02

---

### Key Bets — Verdicts

- **V-01 (rejection log alone → C-13)**: YES. Step 0 forces the named rejection log; C-13 PASS confirmed. V-01 also gains C-04 PASS (the log gates construction) and C-08 PASS (amend distinctness check). Jumps from 84 → 92.
- **V-02 (banned-qualifier list → C-12)**: YES for C-12. But no rejection log = C-13 FAIL, no inertia framing = C-11 FAIL, C-04 still PARTIAL. Single-axis bet wins its target, loses all-essential-pass. Drops to 84.
- **V-03 (self-application → C-09)**: YES for C-09. But no rejection log = C-13 FAIL, no closure = C-07 PARTIAL, weak C-08. New criteria punish V-03 more than R1's 2-criterion aspirational set did. Drops from 92.5 → 85.
- **V-05 R2 vs R1 (design-rationale-first → C-11)**: YES. V-05 is the only variation to satisfy C-11's positional requirement. V-04 has identical content but puts design rationale after criteria tables — PARTIAL vs PASS. The structural gate is the decisive discriminator.

---

### Excellence Signals (new in R2)

1. **design-rationale-first** — requiring the design rationale section *before* criteria tables in the output file makes inertia framing causally prior to construction, not retrospective. V-04 has the same content; only V-05 has the position.

2. **stacked-self-application-plus-rejection-log** — V-05 achieves both C-09 and C-13 simultaneously by putting the rejection log and the self-application results in the same design rationale paragraph. Both populate different slots with zero mutual interference. No other variation achieved both.

3. **amend-as-three-gate-check** — three distinct questions in amend (skill-specific? binary pass condition? distinct failure mode?) cover all three primary criterion failure modes, converting revision from freeform editorial to structured validation gate.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["design-rationale-first: require design rationale section before criteria tables in the output file -- makes inertia framing causally prior to criteria design, not retrospective, guaranteeing C-11 as a structural property", "stacked-self-application-plus-rejection-log: combining self-application gate (C-09) with rejection log named in design rationale (C-13) -- these populate different design rationale slots with zero mutual interference; no other variation achieved both simultaneously", "amend-as-three-gate-check: amend step covers all three primary criterion failure modes (generic content + untestable pass condition + redundant failure mode) as distinct explicit questions, converting amend from a freeform editorial pass to a structured validation gate"]}
```
: "correctness / depth / format / coverage / behavior -- **no other values**" -- closure present, bolded.

**V-05 PASS**: Same as V-04.

---

#### C-08 -- Essential criteria cover distinct failure modes

Three relevant mechanisms: (A) amend-step distinctness check ("Does it catch a failure mode not already caught by another criterion?"), (B) design rationale requires enumerating "failure modes the essential criteria catch," (C) rejection log reduces generic-criteria overlap that causes redundant coverage.

**V-01 PASS**: All three mechanisms present. Amend asks "Does it catch a failure mode not already caught by another criterion?" Design rationale requires failure modes enumeration. Step 0 rejection log enforces specificity. The combination turns distinctness from intent into structural evidence.

**V-02 PARTIAL**: Amend has the distinctness check; design rationale enumerates failure modes. No rejection log -- filter is intent-dependent rather than evidence-backed. Two of three mechanisms.

**V-03 PARTIAL**: Design rationale enumerates failure modes. V-03's amend step does not include a distinctness check (only re-runs self-application gate). No rejection log. One of three mechanisms.

**V-04 PASS**: All three mechanisms. Identical basis to V-01 plus the "competitor you are beating" inertia framing adds additional pressure.

**V-05 PASS**: All three mechanisms plus design rationale is written before criteria tables, making the failure-modes enumeration happen before construction is finalized.

---

#### C-09 -- Rubric is calibrated

**V-01 PARTIAL**: Design rationale requires "failure modes the essential criteria catch" -- demonstrates the author thought about which outputs fail. No concrete poor-output thought experiment, no specific essential criterion ID named, no strong-output thought experiment. PARTIAL.

**V-02 PARTIAL**: Design rationale requires "dominant failure mode" and "hardest criterion to satisfy." Calibration reasoning present but no structured good/poor output thought experiment. PARTIAL.

**V-03 PASS**: Self-application gate questions 2 and 3: (2) construct a mediocre output, identify which essential criterion it fails first, name the ID; (3) construct a strong output, name which recommended/aspirational criterion it would still fail. Gate enforces: "If you cannot complete (2), your essential set is not catching real failures. Revise." Both thought experiments are mandated with specific IDs required. PASS.

**V-04 PARTIAL**: No self-application gate. Design rationale has failure modes, rejection log, hardest criterion. Richer than V-01/V-02 but no concrete poor/strong thought experiment with named criterion IDs. PARTIAL.

**V-05 PASS**: Same self-application gate as V-03 with identical enforcement. Design rationale also requires recording both results. PASS.

---

#### C-11 -- Inertia framing in design rationale

Pass condition: "Design rationale contains an explicit statement of the dominant failure mode; this statement appears before the first criteria table."

**V-01 PARTIAL**: Step 0 names the dominant failure mode explicitly before the spec is read. But in the output FILE the design rationale section appears after Essential/Recommended/Aspirational tables. Content requirement met; positional requirement not met. PARTIAL.

**V-02 FAIL**: No pre-construction inertia framing. Design rationale after criteria tables. FAIL.

**V-03 FAIL**: No inertia framing. Design rationale after criteria tables. FAIL.

**V-04 PARTIAL**: "The competitor you are beating" section opens with explicit naming of the generic failure mode -- clearest pre-construction framing outside V-05. But output FILE has design rationale after criteria tables. Content strong; structural position wrong. PARTIAL.

**V-05 PASS**: File structure enforced: "## Design Rationale → ## Essential Criteria → ## Recommended Criteria → ..." Design rationale must open with the dominant failure mode as the first sentence. Both content AND position requirements satisfied by structural enforcement. PASS.

---

#### C-12 -- Pass conditions use closed-world gates

**V-01 PARTIAL**: "Binary and observable. Use counts, presence/absence, specific patterns, or measurable thresholds" -- states what to use but bans no specific qualifiers by name. "Appropriate," "thorough," "complete" could still appear without anchor. PARTIAL.

**V-02 PASS**: 12-term banned-qualifier list with 6 acceptable patterns enumerated. Explicit rule: "Rewrite until the pass condition is a count, a presence/absence check, a specific pattern, or a measurable threshold." V-02's core innovation. PASS.

**V-03 PARTIAL**: "No 'sufficient', 'good', or 'appropriate' without a measurable anchor" -- 3-term partial list. "Thorough," "complete," "clear," "comprehensive" unbanned. Higher residual risk than V-02. PARTIAL.

**V-04 PASS**: 8-term banned-qualifier list ("good * sufficient * appropriate * thorough * complete * clear * comprehensive * adequate") plus binary-observable requirement and acceptable patterns. PASS.

**V-05 PASS**: 5-term banned-qualifier list plus self-application gate (question 1) verifies each essential criterion satisfies its own pass condition -- catches bare subjective qualifiers during self-review. Two-layer protection. PASS.

---

#### C-13 -- Rejection log proves specificity filter ran

**V-01 PASS**: Step 0 writes the rejection log before the spec is opened. Step 3 explicitly requires copying it into the design rationale: "the rejection log from Step 0 -- copy it in, marking which criteria you considered and discarded." Named examples present by construction. PASS.

**V-02 FAIL**: No Step 0 rejection log. Design rationale template does not require naming rejected criteria. No mechanism to produce C-13 evidence. FAIL.

**V-03 FAIL**: No Step 0 rejection log. Design rationale includes self-application results but does not require naming rejected generic criteria. FAIL.

**V-04 PASS**: Step 0 writes the rejection log. Design rationale explicitly requires: "the rejection log from Step 0 verbatim -- name the generic criteria considered and discarded." Same mechanism as V-01. PASS.

**V-05 PASS**: No separate Step 0, but design rationale (written before criteria tables) requires "which generic criteria were considered and rejected (name them explicitly)." The pre-criteria position makes the rejection log a natural output of the framing step before construction. PASS.

---

### Ranking Change: R1 to R2

| Variation | R1 Score | R2 Score | Delta | Key driver |
|-----------|----------|----------|-------|------------|
| V-05 | 97.5 | 100 | +2.5 | C-11 PASS (design-rationale-first gate); C-13 PASS (named in design rationale) |
| V-04 | 90 | 98 | +8 | C-07 PASS (closure); C-08 PASS (amend distinctness); C-12 PASS; C-13 PASS |
| V-01 | 84 | 92 | +8 | C-04 now PASS (rejection log gates it); C-08 PASS (amend distinctness); C-13 PASS |
| V-03 | 92.5 | 85 | -7.5 | C-09 PASS unchanged; but C-07 PARTIAL, C-08 PARTIAL, C-13 FAIL -- new criteria hurt V-03 |
| V-02 | 86.5 | 84 | -2.5 | C-12 PASS unchanged; but C-11 FAIL, C-13 FAIL; lost all-essential-pass |

**Ranking shift**: V-05 > V-03 > V-04 > V-02 > V-01 (R1) to V-05 > V-04 > V-01 > V-03 > V-02 (R2)

The three new aspirational criteria reshuffle the middle tier. V-04 and V-01 jump because both have rejection logs (C-13 PASS) and inertia framing (C-11 PARTIAL). V-03 drops because it has neither C-13 nor C-11 -- its C-09 PASS alone cannot hold position against the new criteria weight.

---

### Key Bets -- Verdicts

**V-01 vs V-05 R1: Does Step 0 rejection log alone get C-13 to PASS?**
YES. V-01 scores C-13 PASS. The Step 0 mechanism directly produces the named rejection log required by C-13. Additionally, V-01 unexpectedly gains C-08 PASS (via the amend distinctness check which was always present but counted less under v1). Net: V-01 jumps from 84 to 92.

**V-02 vs V-05 R1: Does the banned-qualifier list move C-12 from PARTIAL to PASS without the other signals?**
YES for C-12. V-02 scores C-12 PASS -- the 12-term list is the strongest C-12 signal. But V-02 does not escape the C-04 PARTIAL trap and now fails C-11 and C-13. The banned-qualifier bet wins its target criterion but the axis isolation costs more than it gains. Score drops from 86.5 to 84 with all-essential failing.

**V-03 vs V-05 R1: Does the self-application gate alone move C-09 from PARTIAL to PASS?**
YES for C-09. V-03 scores C-09 PASS. But V-03 has no rejection log (C-13 FAIL), no closure on categories (C-07 PARTIAL), and weak C-08. The single-axis bet wins C-09 but loses on three new criteria. V-03 drops from 92.5 to 85.

**V-05 R2 vs V-05 R1: Does the design-rationale-before-criteria structural requirement guarantee C-11?**
YES, definitively. V-05 achieves C-11 PASS via the enforced file structure order. No other variation achieves C-11 PASS because all others place design rationale after criteria tables. The structural position requirement is what C-11 tests -- and V-05 is the only variation that addresses it explicitly.

---

### Excellence Signals

Three new patterns from V-05 R2 that explain its perfect score:

**1. Design-rationale-first as structural gate**
V-05 requires the design rationale section to appear before the first criteria table in the output file. This is the only variation to satisfy C-11's positional requirement. V-04 has nearly identical content in the design rationale (dominant failure mode, rejection log, failure modes caught) but places it after the criteria tables. The difference is entirely structural. Lesson: naming the failure mode in a section that follows criteria tables is weaker than naming it before criteria are written, because the author's framing was already shaped by construction rather than shaping construction. The structural gate makes inertia framing causally prior to criteria design, not retrospective.

**2. Stacked self-application + rejection log in design rationale**
V-05 is the only variation that achieves both C-09 PASS (self-application gate) and C-13 PASS (rejection log in design rationale). V-01 and V-04 get C-13 but not C-09. V-03 gets C-09 but not C-13. V-05 stacks both by requiring the design rationale to include (a) rejected generic criteria by name and (b) self-application results. Neither mechanism interferes with the other -- they populate different slots in the same design rationale paragraph. The combination is additive with zero cost.

**3. Amend-as-three-gate-validation**
V-05's amend step asks three distinct questions: (1) Is it specific to this skill? (2) Is the pass condition binary and free of bare subjective qualifiers? (3) Does it catch a failure mode not caught by another criterion? This covers all three primary criterion failure modes (generic content, untestable pass condition, redundant coverage). V-03's amend only re-runs self-application. V-02's amend has the three questions but lacks the upstream mechanisms to produce good criteria in the first place, making amend a corrective patch rather than a quality amplifier.

---

## Notes

This is Round 2. No golden output exists yet. Scores are projected from prompt quality. When `/quest:golden` produces actual rubric artifacts, re-run this scorecard against the real outputs.

C-11 is the decisive new discriminator in v2 -- it distinguishes V-05 (structural enforcement) from V-04 (content intent only). V-04 has everything V-05 has except the positional gate; V-04 scores 98 vs V-05's 100.

Candidates for Round 3 variations: test whether V-05's full combination with an explicit Step 0 rejection log (like V-04) would break the tie and produce C-13 with stronger evidence than the retrospective design rationale requirement alone.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["design-rationale-first: require design rationale section before criteria tables in the output file -- makes inertia framing causally prior to criteria design, not retrospective, guaranteeing C-11 as a structural property", "stacked-self-application-plus-rejection-log: combining self-application gate (C-09) with rejection log named in design rationale (C-13) -- these populate different design rationale slots with zero mutual interference; no other variation achieved both simultaneously", "amend-as-three-gate-check: amend step covers all three primary criterion failure modes (generic content + untestable pass condition + redundant failure mode) as distinct explicit questions, converting amend from a freeform editorial pass to a structured validation gate"]}
```
