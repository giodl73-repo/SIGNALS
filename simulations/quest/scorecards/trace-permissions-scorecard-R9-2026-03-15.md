Now I have everything needed to score. Let me compile the full analysis.

---

# Round 9 Scoring Report — trace-permissions rubric v9

**Rubric structure (v9):**
- Essential: C-01 through C-04 (N=4) → 60 pts max
- Recommended: C-05 through C-07 (N=3) → 30 pts max
- Aspirational: C-08 through C-32 (N=25) → 10 pts max
- Formula: `(essential/4 × 60) + (recommended/3 × 30) + (aspirational/25 × 10)`

**Entering state:** All C-01 through C-30 PASS in prior best. C-31 and C-32 both absent. 23/25 aspirational.

---

## V-01 — Single-Axis: Verbatim Cross-Audit (C-31 isolation)

**Axis:** C-31 target; equivalence clauses remain bare (C-32 fails by design)

| Tier | Criteria | Pass | Fail | PARTIAL |
|------|----------|------|------|---------|
| Essential | C-01 through C-04 | 4 | 0 | 0 |
| Recommended | C-05 through C-07 | 3 | 0 | 0 |
| Aspirational | C-08 through C-30, C-31 | 24 | 1 (C-32) | 0 |

**Key criterion evidence:**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | TABLE_1 declared at Step 0.1; every role column present; blank-cell rule enforced |
| C-02 | PASS | TABLE_3 Record Scope schema declared; Effective Scope enumeration present |
| C-03 | PASS | TABLE_2 FLS Coverage schema declared; Gap? per-row trigger active |
| C-04 | PASS | TABLE_5 declared; enumerated gap types; three-field Remediation format |
| C-05 | PASS | TABLE_4 all four vectors; escalation chain mechanism → TABLE_5 forward |
| C-06 | PASS | Sharing rules vector in TABLE_4; CS-2 cross-reference schema present |
| C-07 | PASS | Team inheritance vector in TABLE_4; TABLE_3 Scope Modifier names team grants |
| C-22 | PASS | Three blind spot CONTEXT blocks; CONTEXT-CLOSES labels per SE section |
| C-27 | PASS | Prohibition names: "see table above", "mechanisms cited in SE-4", "per the analysis above", "as documented above"; "or any equivalent form" present |
| C-29 | PASS | Cross-Audit verbatim format declared at Step 0.1 TABLE_4 + EL-12 APPLICATION-SITE RULE-BLOCK at SE-4; match verdict present |
| C-30 | PASS | "or any equivalent form -- restate each mechanism inline" — bare equivalence clause satisfies C-30 |
| C-31 | **PASS** | `Pre-decl: "[exact text]" | Filed: "[exact text]" | Match: CONFIRMED` format declared at Step 0.1 TABLE_4 with PLACEMENT annotation; SE-4 RULE-BLOCK with negative-example ("A characterization-based cross-audit does not satisfy C-31"); EL-12 APPLICATION-SITE confirmed in INDEX |
| C-32 | **FAIL** | Equivalence clause is bare: "or any equivalent form" — no named prohibited effect. No delegation / co-mingling / effect anchor present anywhere |

**Composite:** (4/4 × 60) + (3/3 × 30) + (24/25 × 10) = 60 + 30 + **9.60** = **99.6**
**Golden threshold:** PASS (all essential pass, composite ≥ 80)

---

## V-02 — Single-Axis: Intent-Anchored Equivalence Clause (C-32 isolation)

**Axis:** C-32 target; cross-audit uses characterization format (C-31 fails by design)

| Tier | Criteria | Pass | Fail | PARTIAL |
|------|----------|------|------|---------|
| Essential | C-01 through C-04 | 4 | 0 | 0 |
| Recommended | C-05 through C-07 | 3 | 0 | 0 |
| Aspirational | C-08 through C-30, C-32 | 24 | 1 (C-31) | 0 |

**Key criterion evidence:**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-27 | PASS | Prohibition names six specific forms; "whether that form is a sentence, a label, a parenthetical phrase" adds structural category enumeration |
| C-29 | PASS | Cross-Audit field confirms pre-declaration / mechanism column alignment — assertion IS stated (characterization format satisfies C-29 which requires the assertion to be stated, not verbatim) |
| C-30 | PASS | Equivalence clause with named effect: "or any equivalent form that delegates mechanism content to another section rather than restating it inline" |
| C-31 | **FAIL** | Cross-Audit field declaration: "states that the pre-declared assumption and the closing mechanism column name the same structural fact for each vector. A cross-audit identifies the structural fact at both sites and confirms alignment. [Note: this variation uses characterization format -- C-31 verbatim-quote format is NOT applied here]." SE-4 explicitly says "Characterization format -- C-31 verbatim-quote not applied." |
| C-32 | **PASS** | Prohibition text: "or any equivalent form that delegates mechanism content to another section rather than restating it inline"; PLACEMENT annotation confirms C-30/C-32 at Step 0.1 TABLE_4; EL-13 DECLARATION-SITE confirmed in INDEX; SE-4 RULE-BLOCK repeats "A form that produces the effect of delegation -- routing the reader to another location for the mechanism content -- is prohibited regardless of its structural appearance" |

**Composite:** (4/4 × 60) + (3/3 × 30) + (24/25 × 10) = 60 + 30 + **9.60** = **99.6**
**Golden threshold:** PASS (all essential pass, composite ≥ 80)

---

## V-03 — SE-First Sequence + Verbatim Cross-Audit (C-31 stress test)

**Axis:** SE-first phase order; C-31 verbatim cross-audit survives inversion; C-32 absent

| Tier | Criteria | Pass | Fail | PARTIAL |
|------|----------|------|------|---------|
| Essential | C-01 through C-04 | 4 | 0 | 0 |
| Recommended | C-05 through C-07 | 3 | 0 | 0 |
| Aspirational | C-08 through C-30, C-31 | 24 | 1 (C-32) | 0 |

**Key criterion evidence:**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01–C-04 | PASS | TABLE_1-5 schemas declared at Phase 0 Step 0.1 before PHASE 1 (SE). SE-first variant note explicit: "SE-first variant: CS-2 and CS-3 are SE-authored in PHASE 1; CS responds in PHASE 2" |
| C-22 | PASS | Three blind spots retained in CONTEXT; CONTEXT-CLOSES labels on SE-1/SE-2/SE-3 preserved under SE-first ordering |
| C-29 | PASS | Cross-Audit verbatim format declared Step 0.1 + EL-12 APPLICATION-SITE RULE-BLOCK at SE-4 |
| C-30 | PASS | "or any equivalent form -- restate each mechanism inline" — bare equivalence clause |
| C-31 | **PASS** | Verbatim format declared at Step 0.1 with PLACEMENT annotation; SE-4 RULE-BLOCK includes worked example: `Pre-decl: "Sharing rules for this entity are restricted to same-BU access; no sharing rule targets this role for cross-BU grants" | Filed: "Sharing rules for this entity are restricted to same-BU access; no sharing rule targets this role for cross-BU grants" | Match: CONFIRMED`; EL-12 confirmed in INDEX; CA-1 COMPLETENESS CONFIRMATION checks EL-12 YES/NO |
| C-32 | **FAIL** | Prohibition: "do not write 'see table above', 'as documented above', 'per the analysis above', or any equivalent form -- restate each mechanism inline." Bare equivalence clause; no named prohibited effect of delegation |

**Composite:** (4/4 × 60) + (3/3 × 30) + (24/25 × 10) = 60 + 30 + **9.60** = **99.6**
**Golden threshold:** PASS (all essential pass, composite ≥ 80)

---

## V-04 — Combined C-31 + C-32, Formal/Technical Register

**Axis:** Both mechanisms active; SHALL/MUST/PROHIBITED framing throughout; CS-first canonical

| Tier | Criteria | Pass | Fail | PARTIAL |
|------|----------|------|------|---------|
| Essential | C-01 through C-04 | 4 | 0 | 0 |
| Recommended | C-05 through C-07 | 3 | 0 | 0 |
| Aspirational | C-08 through C-32 | 25 | 0 | 0 |

**Key criterion evidence:**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-27 | PASS | Seven specific disallowed forms named; structural category enumeration ("whether that form is a sentence, a label, a parenthetical phrase"); full equivalence with effect anchor |
| C-29 | PASS | Cross-Audit INSTRUCTION at Step 0.1; EL-12 APPLICATION-SITE confirmed; SE-4 RULE-BLOCK with both `Pre-decl` and `Filed` format |
| C-30 | PASS | "or any equivalent form that delegates mechanism content to another section rather than restating it inline" — equivalence clause present with two+ examples plus effect clause |
| C-31 | **PASS** | Step 0.1 Cross-Audit field INSTRUCTION: "PARAPHRASE IS PROHIBITED. CHARACTERIZATION IS PROHIBITED. Both cells MUST be quoted verbatim. Match verification MUST be a zero-judgment mechanical string comparison." EL-12 APPLICATION-SITE RULE-BLOCK at SE-4. CA-1 COMPLETENESS CONFIRMATION checks EL-12 YES/NO explicitly |
| C-32 | **PASS** | Step 0.1 Mechanisms Cited: "A form PRODUCES THE PROHIBITED EFFECT OF DELEGATION if it routes the reader to another section to obtain the mechanism content rather than providing the content at the current location." PLACEMENT annotation confirms C-27/C-30/C-32. EL-13 DECLARATION-SITE confirmed. SE-4 RULE-BLOCK present. CA-1 checks EL-13 YES/NO explicitly |
| C-28 (INDEX completeness) | PASS | 13/13 enforcement points; Site Type breakdown 7 DECLARATION + 5 APPLICATION + 1 BOTH; EL-12 and EL-13 both present |

**Composite:** (4/4 × 60) + (3/3 × 30) + (25/25 × 10) = 60 + 30 + **10.00** = **100.0**
**Golden threshold:** PASS (all essential pass, composite ≥ 80)

---

## V-05 — Full Combination: C-31 + C-32 + Quantified Inertia Framing

**Axis:** Both mechanisms + measurable CONTEXT failure modes; CS-first; CONTEXT-CLOSES names failure mode AND structural mechanism

| Tier | Criteria | Pass | Fail | PARTIAL |
|------|----------|------|------|---------|
| Essential | C-01 through C-04 | 4 | 0 | 0 |
| Recommended | C-05 through C-07 | 3 | 0 | 0 |
| Aspirational | C-08 through C-32 | 25 | 0 | 0 |

**Key criterion evidence:**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-22 | PASS (strongest) | CONTEXT names each failure mode with specific structural mechanism: "Failure mode 1 -- FLS discovery deferred to post-incident" (mechanism: triggered by incident, not by audit). CONTEXT-CLOSES labels: "CONTEXT-CLOSES: Failure Mode 1 (FLS discovery deferred) -- structural mechanism: Gap? per-row boolean forces registration at discovery time, not at trace close." Inertia anchor is mechanistically linked to the structural enforcement |
| C-27 | PASS | Seven specific prohibited forms named; structural categories enumerated |
| C-29 | PASS | Step 0.1 Cross-Audit: verbatim format with three negative constraints ("no paraphrase, no characterization, no abbreviation"); EL-12 APPLICATION-SITE confirmed; SE-4 RULE-BLOCK with explicit negative counterexample |
| C-30 | PASS | Equivalence clause: "or any equivalent form that delegates mechanism content to another section rather than restating it inline" |
| C-31 | **PASS** | Step 0.1 Cross-Audit negative counterexample: "A cross-audit that characterizes both sites ('Pre-decl identifies no team inheritance path; Filed confirms no team inheritance path; Match: CONFIRMED') does not satisfy C-31 -- it states a conclusion without presenting the evidence in a form that is independently verifiable character-for-character." SE-4 RULE-BLOCK reinforces. EL-12 APPLICATION-SITE confirmed |
| C-32 | **PASS** | Step 0.1 Mechanisms Cited: equivalence clause "or any equivalent form that delegates mechanism content to another section rather than restating it inline"; standalone definition sentence: "The prohibited effect is delegation: routing the reader elsewhere to obtain the mechanism content instead of providing it at the current location." SE-4 RULE-BLOCK: "The prohibited effect is delegation -- routing the reader to another location for the mechanism content. A form produces this effect regardless of its structural appearance if it requires the reader to look elsewhere for the mechanism." EL-13 DECLARATION-SITE confirmed; CA-1 checks EL-13 both annotation AND RULE presence |
| C-28 (INDEX completeness) | PASS | 13/13 enforcement points; "EL-12 (C-31 verbatim cross-audit) + EL-13 (C-32 intent-anchored equivalence) both confirmed at Step 0.1 TABLE_4" in Phase 0 gate state log |

**Composite:** (4/4 × 60) + (3/3 × 30) + (25/25 × 10) = 60 + 30 + **10.00** = **100.0**
**Golden threshold:** PASS (all essential pass, composite ≥ 80)

---

## Composite Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Golden |
|-----------|---------------|-----------------|-------------------|-----------|--------|
| V-01 | 60.0 | 30.0 | 9.60 (24/25) | 99.6 | PASS |
| V-02 | 60.0 | 30.0 | 9.60 (24/25) | 99.6 | PASS |
| V-03 | 60.0 | 30.0 | 9.60 (24/25) | 99.6 | PASS |
| **V-04** | **60.0** | **30.0** | **10.00 (25/25)** | **100.0** | **PASS** |
| **V-05** | **60.0** | **30.0** | **10.00 (25/25)** | **100.0** | **PASS** |

**Ranking:** V-05 ≥ V-04 > V-01 = V-03 > V-02

V-05 edges V-04 on excellence signal density (CONTEXT-CLOSES names structural mechanism, negative counterexample at DECLARATION-SITE, standalone effect-definition sentence). V-02 ranks last among the 99.6 group because C-31 (verbatim format) is more structurally foundational than C-32 (intent anchor) — without verbatim, C-29's cross-audit assertion still leaves residual semantic judgment that C-31 eliminates.

---

## Excellence Signals from Top-Scoring Variation (V-05)

**1. Negative counterexample embedded at DECLARATION-SITE (not only at APPLICATION-SITE RULE-BLOCK)**

V-05 places the failing example at Step 0.1 TABLE_4 Cross-Audit field, before PHASE 1: *"A cross-audit that characterizes both sites ('Pre-decl identifies no team inheritance path; Filed confirms no team inheritance path; Match: CONFIRMED') does not satisfy C-31 -- it states a conclusion without presenting the evidence in a form that is independently verifiable character-for-character."* Prior rounds placed negative guidance only in the SE-4 RULE-BLOCK. Front-loading the counterexample at the schema declaration site means a model reading the schema definition cannot confuse characterization with verbatim even before executing the trace.

**2. Standalone effect-definition sentence separating the prohibition criterion from the equivalence clause**

V-05 adds: *"The prohibited effect is delegation: routing the reader elsewhere to obtain the mechanism content instead of providing it at the current location."* This appears as a separate sentence after the equivalence clause, not embedded in it. It converts the equivalence test from "does this resemble named examples?" to "does this produce delegation?" — an independently testable criterion. V-04 embeds this as a sub-clause inside the INSTRUCTION block; V-05 isolates it as a definitional anchor. Isolation makes the effect-test referable independent of the form-list.

**3. CONTEXT-CLOSES labels naming both the failure mode and the structural closing mechanism**

Prior rounds had CONTEXT-CLOSES labels naming the blind spot (e.g., "CONTEXT-CLOSES: post-incident FLS discovery"). V-05 extends to: *"CONTEXT-CLOSES: Failure Mode 1 (FLS discovery deferred) -- structural mechanism: Gap? per-row boolean forces registration at discovery time, not at trace close."* The structural mechanism annotation creates a verifiable link between the inertia framing (C-22) and the specific prompt mechanism that closes it. A model satisfying the CONTEXT-CLOSES label must also engage the named structural mechanism.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["negative counterexample at DECLARATION-SITE: characterization-based cross-audit failure shown at Step 0.1 schema registry (before PHASE 1), not only in the SE-4 RULE-BLOCK — front-loads the format boundary before any execution begins", "effect-definition as standalone sentence after equivalence clause: 'The prohibited effect is delegation: routing the reader elsewhere to obtain the mechanism content instead of providing it at the current location' — isolates the equivalence criterion as an independently testable effect-membership test, separate from the form-enumeration list"]}
```
