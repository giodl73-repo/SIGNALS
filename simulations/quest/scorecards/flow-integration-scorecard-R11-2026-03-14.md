## flow-integration — Round 11 Score Report (v11 rubric, 212 pt ceiling)

**Evaluator note:** Trace artifacts are structural prompts, not execution outputs. Scoring is against prompt-level criteria: does the instruction satisfy each structural requirement as written?

---

### Scoring Reference

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01–C-04 | 60 (15 ea) |
| Recommended | C-05–C-07 | 30 (10 ea) |
| Aspirational | C-08–C-09 | 10 (5 ea) |
| Aspirational | C-10–C-14 | 20 (4 ea) |
| Aspirational | C-15 | 3 |
| Aspirational | C-16–C-17 | 14 (7 ea) |
| Aspirational | C-18–C-28 | 55 (5 ea) |
| Aspirational | C-29–C-32 | 20 (5 ea) |
| **Total** | | **212** |

---

## V-01 — C-32 Per-Item IS Form (Q1 Probe)

**Structure summary:** Canonical terms, IS-form schema instruction, no YOU MUST NOT block.

### Criterion-by-Criterion

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Inventory table present; call types, confidence, flags explicit |
| C-02 | PASS | [N.1] AUTHENTICATION block present per call |
| C-03 | PASS | [N.2] REQUEST AND RESPONSE FORMAT with Method/Endpoint/fields, separate from auth |
| C-04 | PASS | [N.5] ERROR PROPAGATION with disposition, path, swallowing risk |
| C-05 | PASS | [N.3] RATE LIMITS with Limit value / Burst risk / Throttle response |
| C-06 | PASS | [N.4] RETRY AND IDEMPOTENCY with strategy, idempotency flag, mitigation |
| C-07 | PASS | STAGE 3 — GAP INVENTORY table with call-ID references and gap-type labels |
| C-08 | PASS | Stage 3 requires severity + one-line rationale; MEDIUM/LOW not exempt |
| C-09 | PASS | "HIGH findings require a call-specific remediation sketch; generic advice does not satisfy" |
| C-10 | PASS | INVENTORY GATE: Stage 2 does not open until table is complete |
| C-11 | PASS | Five labeled sections per call; single-concern per section |
| C-12 | PASS | INVENTORY GATE is explicit; CALL-[N] COMPLETION GATE gates next call block |
| C-13 | PASS | Each section carries "this section: X only — ...each have their own sections" exclusion |
| C-14 | PASS | Five-item CALL-[N] COMPLETION GATE checklist present; gates CALL-[N+1] |
| C-15 | PASS | NEW-CALL RULE: "add a row with all four flag cells set before opening that call's analysis block" |
| C-16 | PASS | EXPERT PERSONA DECLARATION before inventory gate; domain named; 4 obligations listed |
| C-17 | PASS | [N.3] RATE LIMITS is in-block with three labeled fields |
| C-18 | PASS | AGGREGATION RULE names all three: populated-FROM, not-authoritative, NOT-required |
| C-19 | PASS | All four categories: forgotten-call, assumed-to-work, unknown-system, delegation-chain |
| C-20 | PASS | CROSS-STAGE AGGREGATION STRUCTURES coda fires unconditionally; no-structures default path present |
| C-21 | PASS | Four flag columns in inventory matching obligation categories |
| C-22 | PASS | Flag names [forgotten-call] / [assumed-to-work] / [unknown-system] / [delegation-chain] match table obligation terms |
| C-23 | PASS | Coda is unnumbered, appended after Stage 3; no position number |
| C-24 | PASS | Four-row obligation table, one row per obligation category |
| C-25 | PASS | Inventory column headers are obligation table row terms; token identity verifiable by schema comparison |
| C-26 | PASS | Schema instruction present without VOCABULARY RULE block: "IS one of the Obligation Term values... use those exact tokens as column headers" |
| C-27 | PASS | Canonical terms; no substitution → dual-surface requirement not triggered; passes by default |
| C-28 | PASS | Header: `*(no stage number — appended after Stage 3, the last numbered stage)*`; prose: "It does not appear between any two numbered stages; it does not displace or renumber any existing element" |
| **C-29** | **FAIL** | Schema instruction uses IS ("Each flag column header... IS one of the Obligation Term values"), not the ARE keyword. C-29 requires "an explicit ARE directive of the form 'the flag column headers ARE the Obligation Term column values above'." IS is an uppercase assertive identity verb but is not ARE; C-29 names ARE specifically. |
| C-30 | PASS | Canonical terms; single-block requirement not triggered |
| C-31 | PASS | Canonical terms; inline enumeration requirement not triggered |
| **C-32** | **FAIL** | C-32 requires "the uppercase ARE keyword in an assertive declarative sentence." IS is uppercase and assertive but is not the ARE keyword. Both C-29 and C-32 criteria name ARE specifically and not "any uppercase assertive identity verb." |

**Score: 212 − 5 (C-29) − 5 (C-32) = 202/212**

**Q1 verdict (partial): IS per-item assertive form does NOT satisfy C-29 or C-32.** ARE is not interchangeable with IS at these criteria. C-29 is named "C-26 explicit ARE directive requirement" — the criterion title makes ARE a named requirement, not a proxy for assertive identity verbs generally. Conservative ruling stands.

---

## V-02 — C-31 Partial Inline Enumeration (Q2 Probe)

**Structure summary:** Non-standard terms (footprint-call / implicit-pass / ghost-system / relay-chain), uppercase ARE (confirmed pass axis), single YOU MUST NOT block naming only footprint-call, implicit-pass, ghost-system — relay-chain omitted.

### Criterion-by-Criterion

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-07 | PASS | Identical structural completeness to V-01 baseline |
| C-08–C-17 | PASS | All aspirational structural mechanisms present and complete |
| C-18–C-23 | PASS | Aggregation rule, coda, unnumbered suffix, all four obligations, flags — all intact |
| C-24 | PASS | Four-row obligation table (footprint-call / implicit-pass / ghost-system / relay-chain) |
| C-25 | PASS | Inventory column headers [footprint-call] / [implicit-pass] / [ghost-system] / [relay-chain] match obligation table row terms |
| C-26 | PASS | Schema instruction present: "The flag column headers... ARE the Obligation Term column values above — use those exact tokens as column headers" (no VOCABULARY RULE block) |
| **C-27** | **FAIL** | YOU MUST NOT block names footprint-call, implicit-pass, ghost-system but omits relay-chain. C-27 requires the block to name "the specific canonical tokens that are forbidden in this trace" — relay-chain is a substituted canonical token and is absent from the prohibition surface. The surface is not self-contained: a model can use relay-chain freely. |
| C-28 | PASS | Terminal-position formula complete in header and prose |
| C-29 | PASS | "The flag column headers... ARE the Obligation Term column values above" — uppercase ARE in assertive sentence |
| C-30 | PASS | YOU MUST NOT block is a single block (not distributed per-row). C-30's architectural requirement (single vs. distributed) is satisfied; the completeness of enumeration is tested by C-31. |
| **C-31** | **FAIL** | YOU MUST NOT block enumerates 3-of-4 substituted tokens inline. C-31 requires enumeration of "each substituted canonical token" — "each" = all. relay-chain is absent; the prohibition surface is incomplete. A reviewer verifying the YOU MUST NOT block cannot determine whether relay-chain is prohibited without cross-referencing the obligation table. Self-contained prohibition surface not achieved. |
| C-32 | PASS | uppercase ARE present — C-32 N/A (C-29 passes) |

**Score: 212 − 5 (C-27) − 5 (C-31) = 202/212**

**Q2 verdict (partial): Partial inline enumeration (3-of-4) does NOT satisfy C-31.** "Each substituted canonical token" requires all four. A prohibition surface with one missing token is not self-contained — relay-chain can appear at the prose/annotation surface without detection. Conservative ruling stands: full enumeration is required.

---

## V-03 — Lifecycle Emphasis Expansion (Structural Neutrality Probe)

**Structure summary:** Canonical terms, uppercase ARE (confirmed), rationale paragraphs added before each stage gate explaining purpose/failure mode/gate logic.

### Criterion-by-Criterion

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-07 | PASS | All structural sections intact; additions are prose-only |
| C-08–C-09 | PASS | Severity + rationale + HIGH remediation requirements unchanged |
| C-10 | PASS | INVENTORY GATE strengthened: "The gate is structural, not advisory — do not open Stage 2 with an incomplete table" |
| C-11–C-14 | PASS | Concern isolation, gate discipline, five-concern checklist — all intact |
| C-15 | PASS | NEW-CALL RULE present with added: "Late call discovery does not invalidate the prior inventory; it extends it" |
| C-16–C-19 | PASS | Persona, rate limits, aggregation rule, all four obligations — intact |
| C-20–C-28 | PASS | Coda, unnumbered suffix, terminal formula — intact |
| C-29 | PASS | "ARE the Obligation Term column values above" — uppercase ARE assertive form |
| C-30 | PASS | Canonical terms; single-block requirement not triggered |
| C-31 | PASS | Canonical terms; inline enumeration requirement not triggered |
| C-32 | PASS | Uppercase ARE present |

**Neutrality check:** Stage 1 rationale paragraph ("a trace that begins with per-call analysis is a product summary, not an integration trace...") is prose-only. Stage 2 rationale paragraph explaining concern-isolation architecture is prose-only. Stage 3 rationale paragraph ("a trace that does not name gaps is a description, not an analysis") is prose-only. None of these add schema instructions, obligation terms, or format directives. The gate instruction text slightly expanded ("do not open Stage 2 with an incomplete table" added to the gate) but the gate structure and C-12 pass condition are unchanged.

**Score: 212/212**

Confirms: lifecycle rationale blocks are a structurally neutral axis. Commentary on why a stage exists does not create or close any criterion exposure.

---

## V-04 — Combined: IS Form + Partial Enumeration (Q1+Q2 Joint Probe)

**Structure summary:** Non-standard terms (footprint-call / implicit-pass / ghost-system / relay-chain), IS-form schema instruction, single YOU MUST NOT block naming footprint-call + implicit-pass + ghost-system (relay-chain omitted).

### Criterion-by-Criterion

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-07 | PASS | Structural completeness identical to other variations |
| C-08–C-23 | PASS | All mechanisms intact — persona, gate, concern isolation, coda, etc. |
| C-24 | PASS | Four-row obligation table (non-standard terms) |
| C-25 | PASS | Inventory column headers match obligation table row terms |
| C-26 | PASS | IS-form schema instruction is schema-only (no VOCABULARY RULE block). C-26 pass condition is schema-only enforcement; the IS verb provides an identity assertion at the schema level. C-26 survives IS form per V-01 analysis. |
| **C-27** | **FAIL** | Single YOU MUST NOT block omits relay-chain. Same failure as V-02: prohibition surface is not self-contained for relay-chain. |
| C-28 | PASS | Terminal-position formula intact |
| **C-29** | **FAIL** | IS form used in schema instruction. Same failure as V-01: IS is not the ARE keyword. |
| C-30 | PASS | Single block (not per-row); architectural requirement satisfied |
| **C-31** | **FAIL** | 3-of-4 enumeration; relay-chain absent. Same failure as V-02. |
| **C-32** | **FAIL** | IS is not the uppercase ARE keyword. Same failure as V-01. |

**Score: 212 − 5 (C-27) − 5 (C-29) − 5 (C-31) − 5 (C-32) = 192/212**

**Joint verdict:** Both Q1 and Q2 resolve as FAIL independently. The two failure axes are additive — IS form does not rescue the partial enumeration failure, and vice versa. 192/212 = predicted matrix outcome for (Q1 FAIL, Q2 FAIL).

---

## V-05 — Phrasing Register Shift (Confirming Clean Sweep)

**Structure summary:** Canonical terms, uppercase ARE, imperative register throughout ("YOUR FOUR DISCOVERY COMMITMENTS", "Build this inventory now", "TRACE EVERY CALL", "NAME EVERY GAP").

### Criterion-by-Criterion

| ID | Result | Evidence |
|----|--------|----------|
| C-01–C-07 | PASS | Structural completeness intact; content sections renamed but structurally complete |
| C-08 | PASS | Stage 3 ("STAGE 3 — NAME EVERY GAP") requires severity label + one-line rationale |
| C-09 | PASS | "HIGH findings require a call-specific remediation sketch; point to the fix, not the category" |
| C-10 | PASS | "Open Stage 2 only when every call has a row" — inventory-first gate |
| C-11–C-14 | PASS | Five-section concern isolation, completion gate with five-item checklist — intact |
| C-15 | PASS | NEW-CALL RULE: "Stop. Add the row. Then continue." — imperative form of same rule |
| C-16 | PASS | "YOUR ROLE" + "YOUR FOUR DISCOVERY COMMITMENTS" — persona declaration before inventory gate, domain and all four obligations named |
| C-17 | PASS | [N.3] RATE LIMITS in-block with three fields |
| C-18 | PASS | AGGREGATION RULE with all three properties intact |
| C-19 | PASS | All four discovery commitments present in table |
| C-20 | PASS | CROSS-STAGE AGGREGATION STRUCTURES coda unconditional |
| C-21 | PASS | Four flag columns matching obligation categories |
| C-22 | PASS | [forgotten-call] / [assumed-to-work] / [unknown-system] / [delegation-chain] match obligation table terms |
| C-23 | PASS | Unnumbered coda, appended after "STAGE 3 — NAME EVERY GAP" |
| C-24 | PASS | Four-row obligation table ("YOUR FOUR DISCOVERY COMMITMENTS") |
| C-25 | PASS | Inventory column headers match obligation table row terms |
| C-26 | PASS | "ARE the Obligation Term column values above — use those exact tokens as column headers" — schema instruction only, no VOCABULARY RULE |
| C-27 | PASS | Canonical terms; dual-surface prohibition not triggered |
| C-28 | PASS | Header formula: `*(no stage number — appended after Stage 3, the last numbered stage)*`; prose: "It does not appear between any two numbered stages; it does not displace or renumber any existing element" |
| C-29 | PASS | Uppercase ARE in assertive sentence |
| C-30 | PASS | Canonical terms; not triggered |
| C-31 | PASS | Canonical terms; not triggered |
| C-32 | PASS | Uppercase ARE present |

**Note on "Each commitment IS a row in the table below":** This uses IS in a separate sentence ("Make these four commitments... Each commitment IS a row in the table below — a missing row is a broken commitment") — this is not the schema alignment instruction. The schema instruction "The flag column headers... ARE the Obligation Term column values above" is the distinct sentence that must satisfy C-29/C-32. The incidental use of IS elsewhere is irrelevant to C-29/C-32 evaluation.

**Score: 212/212**

Confirms: phrasing register is a confirmed free variation axis. Renaming stage headers, using imperative verbs, shifting persona framing to commitment language — none of these create or close criterion exposure.

---

## Composite Ranking

| Rank | Variation | Score | Delta | Failures |
|------|-----------|-------|-------|----------|
| 1 | V-03 (Lifecycle Emphasis) | 212/212 | 0 | None |
| 1 | V-05 (Register Shift) | 212/212 | 0 | None |
| 3 | V-01 (IS Form) | 202/212 | −10 | C-29, C-32 |
| 3 | V-02 (Partial Enumeration) | 202/212 | −10 | C-27, C-31 |
| 5 | V-04 (IS + Partial) | 192/212 | −20 | C-27, C-29, C-31, C-32 |

All essential criteria (C-01–C-04) pass in all five variations.

---

## Open Question Verdicts from R11

**Q1 — C-32 assertive form variants (RESOLVED — CONSERVATIVE):**
Per-item IS form does not satisfy C-29 or C-32. V-01 and V-04 both score −5 C-29 and −5 C-32. C-29 is named "C-26 explicit ARE directive requirement" — ARE is the specific required keyword. C-32 states "the uppercase ARE keyword in an assertive declarative sentence" — not "any uppercase assertive identity verb." IS is semantically equivalent in natural language but does not satisfy the rubric's named keyword requirement. The criterion language in C-29 explicitly invokes C-26 failure for constructions "without the explicit ARE keyword." IS is not ARE.

**Q2 — C-31 enumeration completeness (RESOLVED — CONSERVATIVE):**
Partial inline enumeration (3-of-4) does not satisfy C-31 or C-27. V-02 and V-04 both score −5 C-27 and −5 C-31. C-31 requires enumeration of "each substituted canonical token" — "each" applies to all four. A YOU MUST NOT block that names three terms leaves the fourth (relay-chain) uncovered at the prose/annotation surface. The self-containment test fails: a reviewer cannot determine relay-chain's prohibition status without cross-referencing the obligation table. Full enumeration is required.

---

## Excellence Signals from Top-Scoring Variations

**From V-03 (Lifecycle rationale blocks):**
- Detailed stage-purpose commentary is structurally free. Explaining *why* Stage 1 exists ("a trace that begins with per-call analysis is a product summary, not an integration trace"), *why* Stage 2 uses concern isolation, and *why* Stage 3 requires rationale — none of this creates criterion exposure or satisfies any criterion it was not already satisfying. Lifecycle commentary depth is a pure readability dial.
- The gate strengthening language ("The gate is structural, not advisory") is a neutral reinforcement — it does not change the C-10/C-12 pass conditions.

**From V-05 (Imperative register):**
- Renaming "EXPERT PERSONA DECLARATION" to "YOUR ROLE" + "YOUR FOUR DISCOVERY COMMITMENTS" is structurally neutral. C-16 and C-19 test for obligation content, not framing label.
- The "Stop. Add the row. Then continue." formulation of the NEW-CALL RULE is the strongest instructional form observed — action-gating language makes the rule structurally harder to skip. This may be the best C-15 implementation pattern.
- Stage header names ("BUILD THE CALL INVENTORY", "TRACE EVERY CALL", "NAME EVERY GAP") are structurally neutral — C-10 and C-20 test for gate presence and coda structure, not header naming.

---

```json
{"top_score": 212, "all_essential_pass": true, "new_patterns": ["IS per-item assertive form does not satisfy C-29/C-32 — ARE keyword is specifically required and IS is not a substitute even when uppercase and assertive", "Partial inline enumeration (3-of-4 substituted tokens) does not satisfy C-31 — each substituted canonical token must be named; partial coverage leaves the prohibition surface incomplete for the omitted token", "Lifecycle rationale prose blocks (stage purpose, failure mode, gate logic explanations) are a confirmed structurally neutral axis", "Imperative register throughout (action-oriented stage headers, commitment framing, gating imperatives) is a confirmed structurally neutral axis"]}
```
