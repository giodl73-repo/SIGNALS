Now I have all the evidence I need. Let me write the full scorecard.

---

## `topic:echo` — Round 18 Scoring

**Rubric:** v18 | **Criteria active:** C-01–C-56 (Essential ×5, Recommended ×3, Aspirational ×48)
**Date:** 2026-03-15 | **Round:** 18

---

### Entering R18: Known Base

R17 V-05 achieved **zero fails and zero partials** across all 45 active criteria (C-09–C-53). All R18 variations inherit V-05 R17 as their base. Three new aspirational criteria are under test: C-54 (canonical name at enforcement sites), C-55 (token-content precision in intro routing commitment), C-56 (scoped cross-section citation mandate). The 45 inherited criteria are assumed PASS across all variations unless the variation explicitly reverts a mechanism.

---

### Per-Variation Architecture Summary

| Variation | C-54 present? | C-55 present? | C-56 present? | Key mechanism |
|-----------|:---:|:---:|:---:|---|
| V-01 | **YES** | no | no | Stage 4 instruction: "The Standalone Collapse Prohibition applies: each row is committed before the next begins." |
| V-02 | no | **YES** | no | Intro commitment 3: "the token names the stage, not merely describes the routing action" |
| V-03 | no | no | **YES** | Prohibition block: "any failure mode, verdict, or section note in this prompt that references this prohibition is citing the Standalone Collapse Prohibition by name" |
| V-04 | **YES** | **YES** | no | Both enforcement-site citation and intro token-content contrast; prohibition block remains unscoped |
| V-05 | **YES** | **YES** | **YES** | All three + R19 extensions: COMMIT-STAGE-4 carries constraint reference; GATE-CONFIRMED emits Stage 4 as proper-noun content |

---

### Essential Criteria — 12 pts each (60 max)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-01 Surprise synthesis frame | PASS | PASS | PASS | PASS | PASS |
| C-02 Named entries | PASS | PASS | PASS | PASS | PASS |
| C-03 Source signal w/ gate | PASS | PASS | PASS | PASS | PASS |
| C-04 Design impact (specific component) | PASS | PASS | PASS | PASS | PASS |
| C-05 Artifact write path specified | PASS | PASS | PASS | PASS | PASS |

**All Essential: PASS across all variations. 60 pts each.**

---

### Recommended Criteria — 10 pts each (30 max)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-06 Synthesis / cluster step | PASS | PASS | PASS | PASS | PASS |
| C-07 Forward guidance / next-team register | PASS | PASS | PASS | PASS | PASS |
| C-08 Minimum 2 entries stated | PASS | PASS | PASS | PASS | PASS |

**All Recommended: PASS across all variations. 30 pts each.**

---

### Aspirational Criteria — 5 pts each (48 active, 240 raw max; total capped at 200)

**Inherited base (C-09–C-53):** All 45 criteria PASS across all five variations — no variation reverts any mechanism that was passing in V-05 R17. Variations differ only in which of the three new criteria they carry.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-09 through C-53 (45 criteria) | PASS | PASS | PASS | PASS | PASS |
| **C-54** Canonical name at enforcement sites | **PASS** | FAIL | FAIL | **PASS** | **PASS** |
| **C-55** Token-content precision (names, not routes) | FAIL | **PASS** | FAIL | **PASS** | **PASS** |
| **C-56** Cross-section citation mandate (scoped) | FAIL | FAIL | **PASS** | FAIL | **PASS** |

**Criterion-level evidence for new criteria:**

**C-54:**
- V-01 PASS: Stage 4 inline instruction ends with "The Standalone Collapse Prohibition applies: each row is committed before the next begins." — canonical name present at the per-entry enforcement site.
- V-02 FAIL: Stage 4 ends with "a COMMIT-STAGE-4 at the end of this stage does not substitute." — constraint behavior referenced without canonical name.
- V-03 FAIL: Stage 4 ends with "a COMMIT-STAGE-4 at the end of this stage does not substitute." — same absence as V-02.
- V-04 PASS: Same Stage 4 sentence as V-01 — "The Standalone Collapse Prohibition applies: each row is committed before the next begins."
- V-05 PASS: Same sentence plus COMMIT-STAGE-4 token reads "COMMIT-STAGE-4: all entries committed per the Standalone Collapse Prohibition." — canonical name now appears at both the inline enforcement instruction and the stage-close token (R19 candidate surface).

**C-55:**
- V-01 FAIL: Intro commitment 3 writes "naming its receiving stage before Stage 4 begins." The word "naming" satisfies C-53 (token-content vs. routing action is implicit) but the explicit behavioral contrast "names the stage, not merely describes the routing action" is absent. The criterion requires the distinction to be stated.
- V-02 PASS: Intro commitment 3 writes "the token names the downstream stage it routes to — the token names the stage, not merely describes the routing action." The explicit contrast is present: token-content specification ("names the stage") is distinguished from behavioral description ("routing action").
- V-03 FAIL: Intro commitment 3 uses "naming its receiving stage before Stage 4 begins" — same as V-01, no explicit contrast.
- V-04 PASS: Same intro commitment 3 as V-02 — explicit contrast present.
- V-05 PASS: Same language plus Stage 3 instruction says "write the confirmation token with the receiving stage as its content — the token names Stage 4, not merely routes toward it" — explicit contrast reinforced at the gate instruction as well.

**C-56:**
- V-01 FAIL: Prohibition block ends "This constraint is named so it can be cited by name throughout this prompt." — unscoped. "Throughout this prompt" does not name which section types are in scope.
- V-02 FAIL: Same unscoped language as V-01.
- V-03 PASS: Prohibition block ends "This constraint is named so that any failure mode, verdict, or section note in this prompt that references this prohibition is citing the Standalone Collapse Prohibition by name." — scoped mandate names three section categories (failure modes, verdicts, section notes) as the propagation scope.
- V-04 FAIL: Same unscoped language as V-01/V-02 — C-56 deliberately absent.
- V-05 PASS: Same scoped mandate as V-03.

---

### Fails and Partials Summary

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|-|------|------|------|------|------|
| FAIL criteria | C-55, C-56 | C-54, C-56 | C-54, C-55 | C-56 | — |
| PARTIAL criteria | — | — | — | — | — |
| Fail count | 2 | 2 | 2 | 1 | 0 |
| Partial count | 0 | 0 | 0 | 0 | 0 |

---

### Score Computation

| Metric | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------|-----:|-----:|-----:|-----:|-----:|
| Essential (5 × 12) | 60 | 60 | 60 | 60 | 60 |
| Recommended (3 × 10) | 30 | 30 | 30 | 30 | 30 |
| Aspirational passing | 46 | 46 | 46 | 47 | 48 |
| Aspirational raw (× 5) | 230 | 230 | 230 | 235 | 240 |
| **Raw total** | **320** | **320** | **320** | **325** | **330** |
| **Capped at 200** | **200** | **200** | **200** | **200** | **200** |

---

### Leaderboard

| Rank | Variation | Raw | Capped | Fails | Partials |
|------|-----------|----:|-------:|------:|---------:|
| **1** | **V-05** | 330 | 200 | 0 | 0 |
| **2** | **V-04** | 325 | 200 | 1 | 0 |
| 3 (tied) | V-01 | 320 | 200 | 2 | 0 |
| 3 (tied) | V-02 | 320 | 200 | 2 | 0 |
| 3 (tied) | V-03 | 320 | 200 | 2 | 0 |

**Tiebreaker V-01/V-02/V-03:** All three satisfy exactly one new criterion, isolating C-54, C-55, and C-56 respectively. The isolation is by design — no architecture regression, no substantive advantage of one axis over another. For promotion purposes, V-05 is the unambiguous top variation.

**Promoted to R19 base: V-05.**

---

### Ceiling Analysis

All five variations cap at 200. R18 continues the pattern established in R17: at this stage of accumulated criteria, the raw aspirational total (230–330 pts) exceeds the cap regardless of how many new criteria pass. The cap absorbs all tier-level differences; differentiation comes from fail count.

**Remaining gaps at V-05 level:** None across C-01–C-56. V-05 achieves zero fails on all 48 active criteria.

---

### Excellence Signals (from V-05 R18)

**1. Canonical name propagation at enforcement site (C-54 mechanism).**
The minimum mechanism for C-54 is a single sentence inside Stage 4's inline structural instruction that cites the canonical name: "The Standalone Collapse Prohibition applies: each row is committed before the next begins." C-54 is about enforcement-site citation granularity, not definition-block existence (C-51) — the name must appear where the model is instructed to act on the constraint, not only where it is defined.

**2. Explicit behavioral contrast distinguishes token-content from routing description (C-55 mechanism).**
C-55 is satisfied only when the intro commitment explicitly states "the token names the stage, not merely describes the routing action." The phrase "naming its receiving stage" satisfies C-53 (token-content declaration is implicit) but not C-55 (the explicit contrast between lexical content and behavioral description is absent). The criterion is about the distinction being stated — it cannot be inferred from a token example alone.

**3. Scoped citation mandate names section categories (C-56 mechanism).**
"So it can be cited by name throughout this prompt" is unscoped — a general instruction without named propagation scope. C-56 requires the mandate to name the categories of downstream sections: "any failure mode, verdict, or section note in this prompt." Without named scope, later sections may cite by position or paraphrase without violating C-51. The mandate must name where the canonical name is required.

**4. R19 candidate: stage-level COMMIT token carries constraint reference (C-57 candidate).**
V-05's COMMIT-STAGE-4 token reads "COMMIT-STAGE-4: all entries committed per the Standalone Collapse Prohibition." — the canonical name now appears at the stage-close token level, not only in the inline enforcement instruction. C-54 was satisfied by the inline instruction alone; C-57 would require the constraint name to appear at the stage-close token level as well. C-54 and C-57 are additive layers of the same propagation principle.

**5. R19 candidate: GATE-CONFIRMED delivers stage name as standalone proper-noun content (C-58 candidate).**
V-05's GATE-CONFIRMED token is `GATE-CONFIRMED-[N]: VALID — Stage 4.` — the stage name is the token's content, not embedded in a behavioral clause ("proceeds to Stage 4"). The Stage 3 instruction reinforces this: "write the confirmation token with the receiving stage as its content — the token names Stage 4, not merely routes toward it." C-49 requires naming the destination; C-55 requires the intro to state the contrast; C-58 would require the token's actual content to be a proper noun, not a clause. These are three distinct layers of stage-name precision.

---

### Regression Signals

None. All criteria satisfied by V-05 R17 (C-09–C-53, 0 fails) remain PASS in all five R18 variations. No previously-satisfied criterion was lost in any variation.

---

### New Criteria Hypothesis Resolution

| Hypothesis | Result |
|------------|--------|
| C-54 satisfied by canonical name inside Stage 4 inline instruction | **CONFIRMED** — V-01/V-04/V-05 satisfy; enforcement-site citation is the mechanism, not additional sites |
| C-55 satisfied by explicit behavioral contrast clause in intro commitment 3 | **CONFIRMED** — V-02/V-04/V-05 satisfy; "naming its receiving stage" (C-53) is not sufficient; the explicit contrast "names the stage, not merely describes the routing action" is required |
| C-56 satisfied by scoped mandate naming failure modes / verdicts / section notes | **CONFIRMED** — V-03/V-05 satisfy; "cited throughout this prompt" is unscoped and fails; named section categories are the discriminating mechanism |
| C-54, C-55, C-56 are independently additive | **CONFIRMED** — V-04 combines C-54 + C-55 without C-56, V-03 carries C-56 alone, V-01 carries C-54 alone; no structural conflict between any pair |
| R19 candidates (C-57 stage-close token, C-58 proper-noun GATE-CONFIRMED) are observable in V-05 | **CONFIRMED** — both behaviors present in V-05 only; neither conflicts with any active criterion; both are additive layers on top of C-54 and C-55 respectively |

---

```json
{"top_score": 200, "all_essential_pass": true, "new_patterns": ["canonical-name-at-enforcement-site-is-distinct-from-canonical-name-in-definition-block — C-54 requires the name to appear where the model is instructed to act on the constraint (Stage 4 inline instruction), not only where the constraint is defined; definition-block existence satisfies C-51; enforcement-site citation satisfies C-54; they are layered requirements on the same canonical name", "token-content-specification-requires-explicit-behavioral-contrast — C-55 is not satisfied by naming the destination alone; the intro commitment must explicitly distinguish what the token must lexically carry (stage name as proper noun) from what the routing action does (behavioral description); 'naming its receiving stage' satisfies C-53 implicitly but not C-55 explicitly; the contrast must be stated, not inferred", "scoped-citation-mandate-names-section-categories — C-56 requires the definition block to name which downstream section types must use the canonical name; 'cited throughout this prompt' is unscoped and fails; 'any failure mode, verdict, or section note' names the propagation scope and satisfies C-56; without named scope, downstream sections may cite by position or paraphrase without violating C-51"]}
```
