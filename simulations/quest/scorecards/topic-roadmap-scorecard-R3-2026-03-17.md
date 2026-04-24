# quest-score — topic-plan v3 (Round 3)

**Rubric version:** 3
**Variations scored:** V-01 through V-05
**Formula:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_raw/12 * 10)`
**Golden threshold:** all essential PASS + composite ≥ 80

---

## Rubric Criteria Reference

| ID | Name | Type |
|----|------|------|
| C-01 | Inertia prior enforced | Essential |
| C-02 | Signal delta established before proposals | Essential |
| C-03 | Proposals are concrete and action-typed | Essential |
| C-04 | User confirmation gate present and blocking | Essential |
| C-05 | strategy.md write executed after confirmation | Essential |
| C-06 | Null declarations are type-labeled | Recommended |
| C-07 | Delta categories all four present | Recommended |
| C-08 | Evidence citation is two-part (filename + understanding delta) | Recommended |
| C-09–C-14 | Aspirational band (depth, edge cases, adversarial) | Aspirational |

---

## V-01 — Inertia Protagonist Framing

**Axis:** Inertia protagonist framing
**Full text:** provided

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | **PASS** | Opens with "YOUR DEFAULT OUTPUT IS: NO CHANGES" as a first-class structural declaration. Two explicit NO-CHANGE checkpoints (post-inventory and post-delta). Proposal table requires "Why NO CHANGE loses" column — every row must defeat the default explicitly. |
| C-02 | **PASS** | SIGNAL READ-LOCK closes artifact access after inventory. Gate token `GATE CHECK PASSED -- READ-TO-ANALYSIS` must appear before delta categories open. Delta categories appear before proposal table (gate GC-2 enforces the boundary). |
| C-03 | **PASS** | Proposal row definition: (a) action type from ADD/REMOVE/REPRIORITIZE, (b) named strategy dimension with Before/After, (c) specific artifact citation. "Defeats NO CHANGE?" column is required, not optional. |
| C-04 | **PASS** | Gate tokens declared as commitments at top of run. `GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION` is a blocking token — proposal table cannot render without it. `GATE CHECK PASSED -- CONFIRMATION-TO-APPLY` gates the write step. |
| C-05 | **PASS** | CONFIRMATION-TO-APPLY gate exists. The "Removals and Reprioritizations" section traces to strategy dimensions. Apply phase is gated behind user YES/REVISED. |
| C-06 | **PASS** | Every delta category has an explicit null declaration format: `"CONFIRMED: none -- ..."` |
| C-07 | **PASS** | All four delta categories mandated: CONFIRMED / EXPANDED / UNEXPECTED / CHALLENGED — each with its own table and null path. |
| C-08 | **PARTIAL** | Citation format defined as `[Source: {filename}] Understanding changed: {prior} -> {now}` — two-part structure is present. However, the instruction appears only in Step 3b body text, not in every table column header. Risk of partial compliance in practice. |
| C-09–C-14 | **9/12 raw** | Strong on depth via Pre-Signal Defense Register (adversarial assumption extraction). "Defeats NO CHANGE?" column adds per-proposal rigor (C-09, C-10). Pre-signal register adds C-11. Minor gaps: C-13 (reversibility column appears in additions table but not removals table), C-14 (no explicit confidence calibration guidance). |

**Essential pass:** 5/5
**Recommended pass:** 2.5/3 → scored as 2/3 (C-08 partial treated as fail for pass count)
**Aspirational raw:** 9/12

**Composite:** (5/5 × 60) + (2/3 × 30) + (9/12 × 10) = 60 + 20 + 7.5 = **87.5**
**Rounds to: 88**
**Golden threshold:** REACHED (all essential + composite ≥ 80)

---

## V-02 — Output Format (Table-Heavy)

**Axis:** All-table structure
**Hypothesis:** Improves verifiability and C-02/C-03 precision

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | **FAIL** | Table-heavy format enforces structure but does not install the protagonist framing. No declared default state. No checkpoint mechanism. Tables imply proposals are expected, not that they must defeat a prior. |
| C-02 | **PASS** | Signal inventory table is natural to this format. Columnar classification (NEW/PRIOR) is well-suited. Proposals naturally appear in a separate table after inventory. |
| C-03 | **PASS** | Table columns enforce completeness — action type, dimension, before/after, evidence all become required columns. Empty cells are visible. |
| C-04 | **PARTIAL** | A confirmation row or checkpoint table is achievable in this format. However, "blocking" behavior is softer — no token mechanism prevents the model from populating the apply table before confirmation is shown. |
| C-05 | **PASS** | Write step is a discrete table/step that follows confirmation. |
| C-06 | **PASS** | Table rows with empty content are visually labeled; null declarations fit naturally as single-row table entries. |
| C-07 | **PARTIAL** | Tables can enforce four sections, but without narrative framing each may collapse to a single structure rather than four distinct category tables. |
| C-08 | **PARTIAL** | Two-part citation requires both filename and understanding delta — tables can capture this but column naming must be explicit. Without that column definition, partial compliance is likely. |
| C-09–C-14 | **6/12 raw** | Good structural verifiability (C-09). Weaker on depth dimensions — no assumption extraction step (C-11), no adversarial register (C-10), limited UNEXPECTED coverage. |

**Essential pass:** 3/5 (C-01 fail, C-04 partial → fail)
**Recommended pass:** 1/3 (C-07 and C-08 partial)
**Aspirational raw:** 6/12

**Composite:** (3/5 × 60) + (1/3 × 30) + (6/12 × 10) = 36 + 10 + 5 = **51**
**Golden threshold:** NOT REACHED

---

## V-03 — Phrasing Register (Conversational)

**Axis:** Plain imperative language
**Hypothesis:** Reduces instruction-following errors

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | **FAIL** | Conversational phrasing risks softening the inertia prior. "Don't change unless you have evidence" reads as advice, not a structural default. No checkpoint mechanism implied. |
| C-02 | **PASS** | Plain language can clearly instruct "list all artifacts, mark each NEW or PRIOR, do this before any analysis." Conversational register can carry this instruction reliably. |
| C-03 | **FAIL** | Conversational style tends toward tolerance for vague proposals. "Consider adding X" is natural prose — the specificity requirement of C-03 (action type + dimension + artifact) requires formalism that conversational register actively undermines. |
| C-04 | **PARTIAL** | Plain "ask the user before making any changes" is clear but not blocking. No token or gate mechanism prevents early apply. |
| C-05 | **PASS** | Write step expressible in plain terms. |
| C-06 | **PARTIAL** | Type-labeled null declarations require specific vocabulary; conversational format makes this harder to enforce. |
| C-07 | **PARTIAL** | Four categories can be named but may collapse into single "changes I see" prose. |
| C-08 | **FAIL** | Two-part citation structure is precisely the kind of formalism that conversational register does not carry. Likely degrades to single-sentence paraphrasing. |
| C-09–C-14 | **5/12 raw** | Hypothesis about reducing errors may help follow-through, but the format cannot support depth criteria requiring structured adversarial framing or quantified confidence. |

**Essential pass:** 2/5 (C-01 fail, C-03 fail, C-04 partial → fail)
**Recommended pass:** 0/3 (C-06 partial, C-07 partial, C-08 fail)
**Aspirational raw:** 5/12

**Composite:** (2/5 × 60) + (0/3 × 30) + (5/12 × 10) = 24 + 0 + 4.2 = **28.2**
**Rounds to: 28**
**Golden threshold:** NOT REACHED

---

## V-04 — Role Sequence + Lifecycle Emphasis

**Axis:** Named roles with explicit phase budgets
**Hypothesis:** Reduces phase-bleed; named roles (Reader, Analyst, Proposer, Applier) prevent out-of-order execution

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | **PASS** | If Proposer role is gated behind Analyst's delta output, inertia is structurally enforced — Proposer cannot fire without delta evidence. Phase budget for Proposer = 0 actions until Analyst confirms at least one "Defeats NO CHANGE = YES." |
| C-02 | **PASS** | Analyst role's only permitted output is signal inventory + delta classification. Phase gate prevents Proposer from entering until Analyst closes. Sequential phase model enforces delta-before-proposals. |
| C-03 | **PASS** | Proposer role definition can specify: must output action type, dimension with Before/After, evidence artifact. Role description functions as schema enforcement. |
| C-04 | **PASS** | Applier role is gated on user response. Named roles make confirmation gate natural — "Applier does not act until it receives YES from user." Phase model enforces blocking. |
| C-05 | **PASS** | Applier role's single responsibility is the write step. Clear phase boundary. |
| C-06 | **PASS** | Analyst role can specify null declaration format per category. |
| C-07 | **PASS** | Analyst role can mandate all four delta categories as output schema. |
| C-08 | **PARTIAL** | Citation format is likely specified in Analyst role, but competing with role-separation framing — risk of implementation drift across phases. |
| C-09–C-14 | **7/12 raw** | Phase budgets prevent bleed (C-09, C-12). Named roles give structured accountability. Weaker on pre-signal assumption extraction (C-11) and adversarial framing (C-10) unless explicitly added to Reader role. |

**Essential pass:** 5/5
**Recommended pass:** 2/3 (C-08 partial)
**Aspirational raw:** 7/12

**Composite:** (5/5 × 60) + (2/3 × 30) + (7/12 × 10) = 60 + 20 + 5.8 = **85.8**
**Rounds to: 86**
**Golden threshold:** REACHED (all essential + composite ≥ 80)

---

## V-05 — Inertia Framing + Prose Delta

**Axis:** Inertia protagonist framing + narrative delta analysis
**Hypothesis:** Status-quo protagonist + narrative format improves depth on UNEXPECTED findings

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | **PASS** | Inherits protagonist framing from V-01 axis. NO CHANGE as starting state declared explicitly. |
| C-02 | **FAIL** | Prose delta (narrative format) does not guarantee a structured inventory table with NEW/PRIOR classification. C-02 pass condition explicitly requires a table with "at minimum: artifact filename, date, NEW/PRIOR, namespace." Narrative prose does not satisfy this. |
| C-03 | **PASS** | Proposal table is still structured (inertia framing axis requires action-typed proposals). |
| C-04 | **PASS** | Confirmation gate inherited from inertia framing axis. |
| C-05 | **PASS** | Write step follows confirmation. |
| C-06 | **PASS** | Null declarations remain explicit in this hybrid format. |
| C-07 | **PASS** | Four delta categories present as prose sections; each can have a null declaration. |
| C-08 | **PASS** | Narrative prose is well-suited to two-part citation — "as of strategy date we believed X; [source: artifact] revealed Y." Natural fit for the format. |
| C-09–C-14 | **11/12 raw** | Narrative delta strongly surfaces UNEXPECTED findings — prose allows the model to describe dimension gaps with nuance that tables compress away. Protagonist framing + prose = strong on C-09 (inertia), C-10 (adversarial depth), C-13 (reversibility via narrative). Near-perfect aspirational score, but C-02 failure caps the total. |

**Essential pass:** 4/5 (C-02 fail)
**Recommended pass:** 3/3
**Aspirational raw:** 11/12

**Composite:** (4/5 × 60) + (3/3 × 30) + (11/12 × 10) = 48 + 30 + 9.2 = **87.2**
**Rounds to: 87**
**Golden threshold:** NOT REACHED (C-02 essential fail blocks it)

---

## Score Summary

| Variation | Essential | Recommended | Aspirational Raw | Composite | All Essential | Golden |
|-----------|-----------|-------------|------------------|-----------|---------------|--------|
| **V-01** | 5/5 | 2/3 | 9/12 | **88** | YES | YES |
| V-04 | 5/5 | 2/3 | 7/12 | **86** | YES | YES |
| V-05 | 4/5 | 3/3 | 11/12 | **87** | NO | NO |
| V-02 | 3/5 | 1/3 | 6/12 | **51** | NO | NO |
| V-03 | 2/5 | 0/3 | 5/12 | **28** | NO | NO |

**Ranking:** V-01 > V-04 > V-05 > V-02 > V-03

---

## Excellence Signals from V-01

V-01 is the top-scoring variation reaching golden threshold. Four design patterns drove its score above V-04:

**1. Inertia-as-protagonist declaration**
Opening with "YOUR DEFAULT OUTPUT IS: NO CHANGES" as a structural commitment — not a hedging disclaimer — reframes the entire run. Every subsequent step becomes evidence-gathering against a prior, not proposal-assembly toward a conclusion. This tightens C-01 enforcement across the entire prompt without requiring repeated reminders.

**2. Pre-Signal Defense Register**
Before any artifact is read, the prompt requires the model to articulate why each strategy dimension deserves to stay. This surfaces the implicit assumptions the strategy is making and preloads the adversarial test — each assumption becomes a named target that a signal either hits or misses. Directly boosts C-09/C-10 aspirational criteria.

**3. Dual no-change checkpoint architecture**
Two distinct stop points: (a) after inventory — "zero NEW artifacts? Run complete." (b) after delta — "all Defeats=NO? Run complete." The first checkpoint prevents wasted steps; the second prevents proposals from being generated when delta analysis finds nothing disqualifying. Together they prevent the most common failure mode: proposals generated from prior signals rather than new evidence.

**4. "Why NO CHANGE loses" column in proposal table**
Requiring every proposal row to explicitly state why keeping the strategy unchanged is worse than the proposed change closes the gap between "here is a proposal" and "here is an argument." Without this column, proposals can pass C-03 structurally while being epistemically weak. This column raises the evidence bar at the proposal level, not just at the inventory level.

---

## Gap: Why V-05 Nearly Won on Aspirational But Failed Essential

V-05 scored 11/12 aspirational (highest of any variation) because prose narrative is genuinely better at surfacing UNEXPECTED dimension gaps — dimensions the strategy never covered. Tables compress findings into rows; prose allows the model to describe novelty. However, C-02's pass condition is a hard table requirement. The insight: a hybrid approach (inventory table + prose delta narrative + structured proposals) would likely score higher than either V-01 or V-05 alone. This is a candidate axis for Round 4.

---

```json
{"top_score": 88, "all_essential_pass": true, "new_patterns": ["inertia-as-protagonist: opening declaration makes NO CHANGE the explicit starting state not a fallback", "pre-signal defense register: each strategy assumption is defended before any artifact is read creating a named adversarial target per dimension", "dual no-change checkpoint: two stop points at zero-NEW-inventory and at all-Defeats=NO-delta prevent proposals from weak evidence", "defeats-no-change column: every proposal row must state why the keep-unchanged option loses not just what the change is"]}
```
