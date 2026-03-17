## scout-inertia R3 Scorecard

**All five variations score Gold. All essential criteria pass across the board.**

| Rank | Variation | Score | Failing aspirational |
|------|-----------|-------|----------------------|
| 1 | V-05 | **100.00** | none |
| 2 | V-04 | 98.57 | C-13 only |
| 3 | V-01 | 97.14 | C-11, C-12 |
| 4 | V-02 | 96.43 | C-10 partial, C-12, C-13 |
| 4 | V-03 | 96.43 | C-11, C-15 |

---

**Top score**: 100 | **All essential pass**: true

**New patterns**:

1. **Column-level > prose-level for structural enforcement** — V-01's labeled bullets (Trigger: / Impact:) admit partially-compliant entries that pass the label check but fail the depth check. V-02/V-05's Impact column makes non-compliance structurally visible: a blank cell is obviously malformed, a half-sentence label is not.

2. **Synthesis heading mandate is orthogonal to role structure** — V-03 proves C-14 can be added to any adversarial role prompt by grafting a heading manifest onto the synthesis step only. Roles are untouched. V-05 inherits this pattern.

3. **R3 delta = 1 mechanism; scaffold maturity confirmed** — R2 needed three new mechanisms. R3 needed one (Impact column). The gap between current best and 100/100 compresses each round. V-05 now accumulates all prior excellence signals with no gaps remaining.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Column-level decomposition (separate Impact column) is structurally more reliable than prose-level format constraint for trigger/impact separation -- blank column cell is visibly malformed; partially-compliant prose label is not", "Synthesis heading mandate is a synthesis-step constraint orthogonal to role structure -- C-14 enforcement can be added to any adversarial role prompt by adding a heading manifest to the synthesis step only, without modifying roles", "R3 required one mechanism delta (vs three in R2), confirming scaffold maturity -- the gap between current best and 100/100 on updated rubric narrows each round as the scaffold accumulates all prior excellence signals"]}
```
4 pts
**Composite**: 60 + 30 + 7.14 = **97.14** | **Band**: Gold

---

## V-02 — Impact Column in Failure Mode Table (C-15 target)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Workaround concretely described | PASS | Section 1: workaround named, workflow described concretely |
| C-02 | Switching costs quantified | PASS | Section 2 table: Dimension / Estimate / Basis rows |
| C-03 | Threat score HIGH | PASS | Section 3 code block: `Threat: HIGH` required |
| C-04 | Why Inertia Loses answered | PASS | Section 4 table: 2+ rows, falsifiable conditions |
| C-05 | Failure modes identified | PASS | Section 5 table: min 2 rows required |
| C-06 | Switching cost dimensions separate | PASS | Time / Training / Disruption each a separate row |
| C-07 | Threshold-based loss conditions | PASS | Section 4 Observable Threshold column required |
| C-08 | Long-term risk stated | PASS | Section 6: 6-12 month time horizon required |
| C-09 | Severity ranked | PASS | Severity column in failure mode table |
| C-10 | Steelman rebutted | PARTIAL | Section 7 marked "(optional but scored)" — model may omit entirely |
| C-11 | Verification method | PASS | Section 4 Verification Command column with format examples and fail conditions |
| C-12 | Anchored rebuttal | FAIL | No STRONGEST CLAIM / NAMED CLAIM mechanism |
| C-13 | Replication fidelity | FAIL | Section 1 at "reader can picture" level — no product naming, enumerated steps, or institutional knowledge requirement |
| C-14 | Labeled sections | PASS | Sections 1-7 with descriptive headings |
| C-15 | Trigger/Impact decomposed | PASS | Dedicated Impact column; blank Impact cell structurally visible as malformed |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 4.5/7 = 6.43 pts
**Composite**: 60 + 30 + 6.43 = **96.43** | **Band**: Gold

---

## V-03 — Required Section Heading List in Synthesis Output (C-14 target)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Workaround concretely described | PASS | Role 1 Step 1: describe exact workflow, tools, commands |
| C-02 | Switching costs quantified | PASS | Role 2 Step 2: three dimensions with numbers required |
| C-03 | Threat score HIGH | PASS | Role 2 Step 1: "HIGH by default. Only downgrade with written justification." |
| C-04 | Why Inertia Loses answered | PASS | Role 2 Step 4: 2+ falsifiable conditions required |
| C-05 | Failure modes identified | PASS | Role 2 Step 3: 2+ specific failure modes required |
| C-06 | Switching cost dimensions separate | PASS | Role 2 Step 2: Time / Training / Disruption separately |
| C-07 | Threshold-based loss conditions | PASS | Role 2 Step 4: "checkable against a real team's situation" |
| C-08 | Long-term risk stated | PASS | Role 2 Step 5: 6-12 month horizon required |
| C-09 | Severity ranked | PASS | Role 2 Step 3: "Rank by severity" with HIGH/MED/LOW |
| C-10 | Steelman rebutted | PASS | Full adversarial structure: Role 1 independently builds advocate case |
| C-11 | Verification method | FAIL | No Verification Command column; Step 4 asks for falsifiable conditions only |
| C-12 | Anchored rebuttal | PASS | STRONGEST CLAIM (Role 1 Step 3) -> NAMED CLAIM verbatim copy (Anchored Rebuttal Step 6a) |
| C-13 | Replication fidelity | PARTIAL | Role 1 "specific enough that someone else could follow" implies steps but does not require product-named tools or institutional knowledge flagging |
| C-14 | Labeled sections | PASS | Required heading list: 7 descriptive section names; fail condition defined; synthesis heading mandate |
| C-15 | Trigger/Impact decomposed | FAIL | Role 2 Step 3 finds failure modes and ranks severity but no trigger/impact structural separation; Impact column absent |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 4.5/7 = 6.43 pts
**Composite**: 60 + 30 + 6.43 = **96.43** | **Band**: Gold

---

## V-04 — Impact Column + Section Label Compliance in Phase Structure (C-14 + C-15)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Workaround concretely described | PASS | Phase 1: named workaround, operational detail, fail condition for vague category descriptions |
| C-02 | Switching costs quantified | PASS | Phase 2: three dimensions, numeric estimate or explicit N/A |
| C-03 | Threat score HIGH | PASS | Phase 2: "Threat score: HIGH. Required. Do not omit." |
| C-04 | Why Inertia Loses answered | PASS | Phase 4 Part A: 2+ falsifiable conditions in table |
| C-05 | Failure modes identified | PASS | Phase 3: 2+ failure modes, table format |
| C-06 | Switching cost dimensions separate | PASS | Phase 2: Time / Training / Disruption as separate items |
| C-07 | Threshold-based loss conditions | PASS | Phase 4 Part A: Observable Threshold column required |
| C-08 | Long-term risk stated | PASS | Phase 4 Part C: "6-12 months... name a specific compounding cost" |
| C-09 | Severity ranked | PASS | Phase 3: "Rank failure modes by severity: HIGH / MED / LOW" |
| C-10 | Steelman rebutted | PASS | Phase 4 Part B: STEELMAN -> NAMED CLAIM -> anchored rebuttal |
| C-11 | Verification method | PASS | Phase 4 Part A: Verification Command column with format and fail conditions |
| C-12 | Anchored rebuttal | PASS | Three-step: STEELMAN -> NAMED CLAIM: "[exact text]" -> rebuttal of named claim only |
| C-13 | Replication fidelity | FAIL | Phase 1 stays at "reader can picture" level -- no Replication Fidelity Standard; no product naming, step enumeration, or tribal knowledge flagging |
| C-14 | Labeled sections | PASS | Phase headings enforced + section label compliance note: "A reader scanning only the headings must locate each component" |
| C-15 | Trigger/Impact decomposed | PASS | Phase 3 table has separate Trigger and Impact columns; "do not merge them" + blank Impact cell = fail condition |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 6/7 = 8.57 pts
**Composite**: 60 + 30 + 8.57 = **98.57** | **Band**: Gold

---

## V-05 — R2 V-05 Scaffold + Impact Column + Section Label Reinforcement (C-14 + C-15)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Workaround concretely described | PASS | STEP 1 Workaround Profile section required |
| C-02 | Switching costs quantified | PASS | Section A Switching Cost Table with three rows, numeric estimates |
| C-03 | Threat score HIGH | PASS | Section B: `Inertia Threat: HIGH` code block, required |
| C-04 | Why Inertia Loses answered | PASS | Section D: 2+ rows, falsifiable conditions |
| C-05 | Failure modes identified | PASS | Section C: min 2 rows required |
| C-06 | Switching cost dimensions separate | PASS | Time / Training / Disruption in separate table rows |
| C-07 | Threshold-based loss conditions | PASS | Section D Observable Threshold column required |
| C-08 | Long-term risk stated | PASS | Section E: "6-12 months" time horizon required |
| C-09 | Severity ranked | PASS | Section C severity column: HIGH / MED / LOW |
| C-10 | Steelman rebutted | PASS | Two-pass structure; Section F anchored rebuttal |
| C-11 | Verification method | PASS | Section D Verification Command column with format + examples + fail conditions |
| C-12 | Anchored rebuttal | PASS | STRONGEST CLAIM (STEP 1) -> NAMED CLAIM verbatim copy -> rebuttal "traceable to the named claim" |
| C-13 | Replication fidelity | PASS | STEP 1 Replication Fidelity Standard: product-named tools, numbered steps, institutional knowledge flagging |
| C-14 | Labeled sections | PASS | Sections A-F descriptive + compliance note: "do not rename, merge, or omit any section heading" |
| C-15 | Trigger/Impact decomposed | PASS | Section C Impact column; "blank Impact cell = automatic fail for that row" |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 7/7 = 10 pts
**Composite**: 60 + 30 + 10 = **100.00** | **Band**: Gold

---

## Rankings

| Rank | Variation | Score | Band | C-14 | C-15 | Failing aspirational |
|------|-----------|-------|------|------|------|----------------------|
| 1 | V-05 | 100.00 | Gold | PASS | PASS | none |
| 2 | V-04 | 98.57 | Gold | PASS | PASS | C-13 only |
| 3 | V-01 | 97.14 | Gold | PASS | PASS | C-11, C-12 |
| 4 | V-02 | 96.43 | Gold | PASS | PASS | C-10 partial, C-12, C-13 |
| 4 | V-03 | 96.43 | Gold | PASS | FAIL | C-11, C-15 |

All five variations: all essential pass, all recommended pass, Gold band.

---

## Excellence Signals

**Signal 1 -- Column-level Impact enforcement is structurally more reliable than prose-level labeled bullet format**

V-01 uses Trigger: / Impact: labeled bullets per failure mode entry. V-02 uses a dedicated
Impact column. Both target C-15 and both predict PASS -- but the mechanisms differ in
reliability. With a column, merging trigger and impact leaves the Impact cell blank, which
is visibly malformed at a glance. With labeled bullets, a model can write
"Trigger: high load. Impact: causes problems" and pass the label check while failing the
depth check. The column eliminates the partial-compliance escape hatch. V-05 inherits the
column approach and carries it to the full scaffold.

**Signal 2 -- Synthesis heading mandate is orthogonal to role structure; C-14 can be grafted without modifying roles**

V-03 shows that C-14 enforcement only requires prescribing analytical headings at the
synthesis step -- the adversarial roles run unchanged. The decoupling means any role-based
prompt can acquire C-14 compliance by adding a heading manifest to the synthesis step, not
by modifying the roles. V-05 demonstrates the same: Sections A-F appear in STEP 2 as a
structural contract and do not touch STEP 1's advocate logic.

**Signal 3 -- R3 delta = 1 mechanism; scaffold maturity confirmed**

R1 to R2 required three new mechanisms (C-11, C-12, C-13). R2 to R3 required one (C-15
Impact column). The gap between the current best prompt and 100/100 has compressed by 2/3
in one round. When the delta reaches zero and holds across multiple rubric extensions, the
scaffold is mature. V-05 is that scaffold: every new aspirational criterion extracted from
its own excellence signals is already present in the structure.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Column-level decomposition (separate Impact column) is structurally more reliable than prose-level format constraint for trigger/impact separation -- blank column cell is visibly malformed; partially-compliant prose label is not", "Synthesis heading mandate is a synthesis-step constraint orthogonal to role structure -- C-14 enforcement can be added to any adversarial role prompt by adding a heading manifest to the synthesis step only, without modifying roles", "R3 required one mechanism delta (vs three in R2), confirming scaffold maturity -- the gap between current best and 100/100 on updated rubric narrows each round as the scaffold accumulates all prior excellence signals"]}
```
