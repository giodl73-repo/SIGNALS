Scorecard written to `simulations/quest/scorecards/signal-check-scorecard-R8-2026-03-18.md`.

---

## R8 Results

**Top score**: 100.00 (V-04 and V-05)
**All essential pass**: true

### Final Scores

| Rank | Var | Composite | Failures |
|------|-----|-----------|----------|
| 1st | V-04 | 100.00 | none |
| 1st | V-05 | 100.00 | none |
| 2nd | V-01 | 99.47 | C-26 (no obligation register alongside validity) |
| 2nd | V-03 | 99.47 | C-27 ("not operative" only — no existence claim) |
| 3rd | V-02 | 98.95 | C-26, C-27 (obligation-only baseline) |

### Key findings

**Isolation confirmed**: V-01 and V-03 are symmetric at 18/19 with different single failures — C-26 and C-27 are independently testable exactly as designed. V-03 vs V-04 confirms that one phrase ("it does not exist as an active rule") is the precise minimum unit for C-27.

**Table estimate correction**: V-01 estimated at 17/19 but actually scores 18/19. R8-V-01 added "Rule 3 itself declares its scope below" (satisfying C-25) which the estimate missed — it conflated R7-V-01's failure pattern with R8-V-01.

**5 new patterns from V-05** (all potential R9 criteria):
1. Heading-level ontological claim — existence assertion recoverable from rule name without body inspection
2. Named sub-registers with non-substitutability declaration — dual-register made structurally surface-parseable
3. Step-up disclaimer — body explicitly names the C-24/C-27 distinction as an upgrade, not just states it
4. Creation-time contract — temporal gate tightened from "before becoming active" to "at rule-creation time"
5. Forward-scope Applies-to — location annotation covers rules not yet written
1 and Rule 2 present | PASS | Both rules present with full body text |
| C-11 | Pilot-briefing language in readiness | PASS | "pilot briefing" named explicitly |
| C-12 | Four dimensions with consistent labeling | PASS | Item 1-4 with STATUS / Basis / Finding / Action |
| C-13 | MISSING SIGNAL GUIDE names signal types | PASS | Named examples: CAUSAL GAP, SEQUENCE, STALENESS, COHERENCE |
| C-14 | STANDING RULES precedes inventory | PASS | STANDING RULES block appears before GATHER YOUR SIGNALS |
| C-15 | Each dimension specifies verbatim absence phrases | PASS | "Required verbatim absence phrase for this item:" in all four dimensions |
| C-16 | Every constraint enumerates all governed locations | PASS | Rule 1 and Rule 2 carry explicit Applies-to lists |
| C-17 | Verbatim absence phrases embedded at point of use | PASS | Phrases appear inline within each dimension's instruction block |
| C-18 | Advisory register carried structurally | PASS | "preflight," "pilot" framing in section headings and dimension labels |
| C-19 | Triple enforcement stack declared as unit with interdependency | PASS | ENFORCEMENT STACK NOTE names all three, states "No rule substitutes for another" |
| C-20 | Location-enumeration expressed as named meta-rule | PASS | Rule 3 is a named rule in STANDING RULES block governing all rule declarations |
| C-21 | Each rule assigned a named failure class | PASS | "prevents silent omissions," "prevents reference ambiguity," "prevents constraint scope gaps" |

**Essential (C-01 to C-05): PASS across all variations.**

---

## Per-Variation Assessment: C-22 to C-27

These criteria depend entirely on Rule 3 body text, which differs across variations.

### C-22 -- Temporal activation gate

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | "scope declaration is a precondition for rule existence, not a retroactive correction" -- precondition framing is equivalent to "before becoming active"; "not a retroactive correction" explicitly rules out post-hoc compliance |
| V-02 | PASS | "must declare all output locations it governs before becoming active" -- canonical temporal gate phrase present |
| V-03 | PASS | "before becoming active" present |
| V-04 | PASS | "before becoming active" present |
| V-05 | PASS | "before becoming active" + "scope must be discharged at rule-creation time, not retroactively" -- doubly anchored |

### C-23 -- Meta-rule self-application in rule body

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | "This requirement self-applies: Rule 3 itself declares its scope below." |
| V-02 | PASS | "This requirement self-applies: Rule 3 itself declares its scope below." |
| V-03 | PASS | "This requirement self-applies: Rule 3 itself declares its scope below." |
| V-04 | PASS | "This requirement self-applies: Rule 3 itself declares its scope below." |
| V-05 | PASS | "This requirement self-applies: Rule 3 itself declares its scope below." |

### C-24 -- Activation gate framed as rule-validity condition

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | "does not exist as an active rule" satisfies C-24 via C-27 subsumption (C-27 -> C-24) |
| V-02 | FAIL | "before becoming active" is obligation only -- no "not operative," "not valid," or existence-denial language; obligation register without any validity register |
| V-03 | PASS | "is not operative until its scope is discharged" -- status-level validity framing present |
| V-04 | PASS | "is not operative -- it does not exist as an active rule until its scope is discharged" |
| V-05 | PASS | "Existence condition: a Rule that has not declared its scope does not exist as an active rule" |

### C-25 -- Proximate scope pointer creating co-location contract

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | "Rule 3 itself declares its scope below" -- directional pointer present |
| V-02 | PASS | "Rule 3 itself declares its scope below" |
| V-03 | PASS | "Rule 3 itself declares its scope below" |
| V-04 | PASS | "Rule 3 itself declares its scope below" |
| V-05 | PASS | "Rule 3 itself declares its scope below" |

### C-26 -- Dual-register enforcement (obligation + validity in same body)

Requires BOTH obligation register ("must declare... before becoming active") AND validity register ("is not operative / does not exist as an active rule") in the same rule body.

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | FAIL | Validity register present ("does not exist as an active rule"). Obligation register absent -- "must declare all output locations it governs" lacks the "before becoming active" temporal qualifier in the obligation clause. The temporal framing appears only in the validity clause ("precondition for rule existence, not a retroactive correction"), not as a standalone obligation gate. One register only. |
| V-02 | FAIL | Obligation register present ("before becoming active"). Validity register absent -- no "not operative," no "does not exist." One register only. |
| V-03 | PASS | Obligation: "before becoming active." Validity: "is not operative until its scope is discharged." Both registers present in same body. |
| V-04 | PASS | Obligation: "before becoming active." Validity: "is not operative -- it does not exist as an active rule until its scope is discharged." Both registers present. |
| V-05 | PASS | Obligation register labeled: "Obligation: every Rule in this STANDING RULES block must declare all output locations it governs before becoming active." Existence register labeled: "Existence condition: a Rule that has not declared its scope does not exist as an active rule." Both named and explicitly declared non-substitutable. |

### C-27 -- Existence framing ("does not exist as an active rule")

Requires the ontological claim -- the rule "does not exist as an active rule" -- not merely "is not operative."

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | "A Rule that has not declared its scope does not exist as an active rule" -- exact ontological claim present |
| V-02 | FAIL | No existence framing. Only obligation language. C-24 failed; C-27 fails by subsumption. |
| V-03 | FAIL | "is not operative until its scope is discharged" -- rule-status framing only. "Is not operative" admits the rule as a declared object with suspended force. The ontological claim ("does not exist") is absent. This is the status/existence distinction C-27 was written to capture. |
| V-04 | PASS | "it does not exist as an active rule until its scope is discharged" -- existence framing added alongside status framing |
| V-05 | PASS | "a Rule that has not declared its scope does not exist as an active rule." Additionally: "'Not operative' understates the condition -- an inoperative rule is still a declared object with suspended force." The C-27 distinction is named as a step-up from C-24 within the body. |

---

## Score Summary

**Aspirational criteria**: C-09 through C-27 = 19 criteria.

**Counting model**: When C-24 fails, C-26 and C-27 fail by subsumption. Leaf failures (C-26, C-27) are counted as independent failures; C-24 failing is captured by the leaf count when both leaves also fail.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 thru C-21 | PASS | PASS | PASS | PASS | PASS |
| C-22 | PASS | PASS | PASS | PASS | PASS |
| C-23 | PASS | PASS | PASS | PASS | PASS |
| C-24 | PASS | FAIL* | PASS | PASS | PASS |
| C-25 | PASS | PASS | PASS | PASS | PASS |
| C-26 | FAIL | FAIL | PASS | PASS | PASS |
| C-27 | PASS | FAIL | FAIL | PASS | PASS |
| **Asp. pass** | **18/19** | **17/19** | **18/19** | **19/19** | **19/19** |
| **Composite** | **99.47** | **98.95** | **99.47** | **100.00** | **100.00** |

*V-02 C-24 fail is structurally implied by both C-26 and C-27 failing; counted as 2 leaf failures (C-26, C-27).

**Note on V-01 table estimate**: The R8 variation table estimated V-01 at 17/19. Actual scoring finds 18/19 -- V-01 fails only C-26. The estimate appears to have conflated R7 V-01 (which failed C-25 and C-26) with R8 V-01 (which adds "Rule 3 itself declares its scope below," satisfying C-25). The isolation structure confirms: V-01 vs V-03 are symmetric 18/19 variations, each failing a different single criterion -- the intended isolation for C-26 vs C-27 testability.

---

## Ranking

| Rank | Variation | Composite | Failures |
|------|-----------|-----------|----------|
| 1st (tied) | V-04 | 100.00 | None |
| 1st (tied) | V-05 | 100.00 | None |
| 2nd (tied) | V-01 | 99.47 | C-26 (no obligation register alongside validity) |
| 2nd (tied) | V-03 | 99.47 | C-27 (status framing only -- "not operative," no existence claim) |
| 3rd | V-02 | 98.95 | C-26, C-27 (obligation-only baseline -- no validity register of any kind) |

---

## Isolation Verification

| Comparison | What it tests | Result |
|------------|---------------|--------|
| V-01 vs V-02 | C-27 in isolation: existence framing alone satisfies C-27? | CONFIRMED -- V-01 passes C-27 (existence framing), V-02 fails (no validity); both fail C-26 (no dual register) |
| V-03 vs V-04 | C-27 as sole differentiator | CONFIRMED -- V-04 adds "it does not exist as an active rule" to V-03's "not operative"; that single phrase is the C-27 distinguisher; 19/19 vs 18/19 |
| V-01 vs V-03 | C-26 vs C-27 independently testable | CONFIRMED -- V-01 fails C-26 (validity-only, no obligation register), V-03 fails C-27 (obligation + status, no existence claim); symmetric 18/19 with different single failures |
| V-04 minimal diff | Ceiling from V-03 | CONFIRMED -- V-04 is V-03 plus one phrase; "it does not exist as an active rule" is the minimum unit for C-27 |

---

## Excellence Signals

**From V-04 (minimal ceiling):**
- The minimum unit for C-27: adding "it does not exist as an active rule" to "is not operative" achieves the ceiling with zero additional structural change. Removing this phrase drops to 18/19. The phrase boundary is precisely located.

**From V-05 (elaborated ceiling -- potential R9 signals):**

1. **Heading-level ontological claim**: Rule name "RULES WITHOUT DECLARED SCOPE DO NOT EXIST" encodes the existence assertion at the heading -- recoverable without reading the body text. The ontological claim is surface-parseable before any body inspection.

2. **Named sub-registers with non-substitutability declaration**: "Obligation:" and "Existence condition:" as labeled, structurally distinct sections. The body explicitly names them as "not substitutes" and explains what each tells you ("the obligation tells you what to do; the existence condition tells you what you lose if you do not"). Dual-register is visible as a structural fact, not inferrable from combined prose.

3. **Step-up disclaimer making the C-24/C-27 distinction explicit**: "'Not operative' understates the condition -- an inoperative rule is still a declared object with suspended force." The body names the inadequacy of C-24 semantics before introducing C-27 semantics. The reader sees why the existence claim is stronger, not just that it is stronger.

4. **Creation-time contract**: "scope must be discharged at rule-creation time, not retroactively" -- tightens the temporal gate beyond "before becoming active." "Before becoming active" permits edge cases; "at rule-creation time" forecloses them: the discharge point is creation, not activation.

5. **Forward-scope Applies-to**: "including Rule 3 itself and any rule added in the future." The location annotation covers rules not yet written. The meta-rule governs future rule additions without requiring an amendment when Rule 4 appears.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Heading-level ontological claim: rule name encodes existence assertion recoverable without reading body", "Named sub-registers (Obligation: / Existence condition:) with explicit non-substitutability declaration making dual-register surface-parseable", "Step-up disclaimer: body names inadequacy of status framing before introducing existence claim, making the C-24/C-27 distinction visible as a named upgrade", "Creation-time contract: temporal gate tightened to rule-creation time rather than activation, foreclosing edge cases", "Forward-scope Applies-to: location annotation covers future rule additions without requiring amendment"]}
```
