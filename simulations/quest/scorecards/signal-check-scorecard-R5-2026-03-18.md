Now I have all five variations. Let me evaluate each against all 21 criteria.

---

# signal-check — Quest Score Report (Round 5)

**Rubric version:** v5 (2026-03-18)
**Variations file:** `simulations/quest/variations/signal-check-variations-R5-2026-03-18.md`
**R5 axis matrix:** C-20 (meta-rule self-applies) × C-21 (named failure classes per rule)

---

## Variation Analysis

### Shared Structure (V-01 through V-05)

All five variations share identical bodies for the preflight check dimensions. Essential and Recommended criteria are evaluated once; they pass or fail the same way across all variations. The only axis of variation is in the STANDING RULES block (Rule 3 wording) and the ENFORCEMENT STACK NOTE.

---

### Essential Criteria — Common Evaluation

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | All four dimensions present | PASS | PASS | PASS | PASS | PASS |
| C-02 | SEQUENCE grounded in artifact dates | PASS | PASS | PASS | PASS | PASS |
| C-03 | COHERENCE names specific signal pairs | PASS | PASS | PASS | PASS | PASS |
| C-04 | CAUSAL GAP states mechanism or names absence | PASS | PASS | PASS | PASS | PASS |
| C-05 | Advisory/coaching register throughout | PASS | PASS | PASS | PASS | PASS |

**Evidence:** All variants open with "Think of this as a preflight check... Nothing here blocks you from proceeding." All four dimensions (CAUSAL GAP, SEQUENCE, STALENESS, COHERENCE) present with structured STATUS/Basis/Finding/Action fields. COHERENCE requires named pairs. CAUSAL GAP requires verbatim absence phrase. No blocking verdicts anywhere.

---

### Recommended Criteria — Common Evaluation

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | STALENESS applies named concrete age threshold | PASS | PASS | PASS | PASS | PASS |
| C-07 | Every flagged issue includes next action | PASS | PASS | PASS | PASS | PASS |
| C-08 | Report opens with readiness summary | PASS | PASS | PASS | PASS | PASS |

**Evidence:** STALENESS instructs "name the threshold: signals older than [N] days are stale because [reason]." Action field required when STATUS is FLAG or OPEN. READINESS SUMMARY section explicitly placed first in final artifact.

---

### Aspirational Criteria — Full Criterion-by-Criterion

#### C-09: Cross-dimension patterns named (v1)
All pass. CROSS-ITEM PATTERNS section present in all variations with explicit shared-root detection instructions and `/namespace:skill` action requirement.

#### C-10: Missing signals by namespace + specific skill (v1)
All pass. MISSING SIGNAL GUIDE section collates gaps with one line per gap in `/namespace:skill` format.

#### C-11: All skill references in `/namespace:skill` format (EX-01)
All pass. Rule 2 enforces this explicitly across all output locations in all variations.

#### C-12: Terminal MISSING SIGNAL GUIDE section (EX-02)
All pass. Final analysis section present and correctly titled in all variations.

#### C-13: Absent evidence declared explicitly (EX-03)
All pass. Rule 1 (ABSENCE MUST BE DECLARED) plus verbatim phrases per dimension enforce this in all variations.

#### C-14: Named STANDING RULES block precedes all inventory and analysis (EX-04)
All pass. STANDING RULES block present at top of all variations, before GATHER YOUR SIGNALS and all analysis.

#### C-15: Each dimension specifies required verbatim absence phrases (EX-05)
All pass. All four dimensions carry inline "Required verbatim absence phrase for this item:" blocks with exact mandated wording. Point-of-use placement confirmed.

#### C-16: Every constraint enumerates all output locations it governs (EX-06)
All pass. Rules 1 and 2 carry "Applies to:" lines listing all seven governed locations. Rule 3 in all variations also carries an "Applies to:" line (self-referential or enumerated). C-16 is satisfied by location-complete annotations; C-20 then tests whether the enumeration extends to future rules.

#### C-17: Verbatim absence phrases embedded at point of use (R3-EX-01)
All pass. Each dimension block contains the absence phrase inline — not only in a reference table. Satisfying C-17 implies C-15; confirmed here.

#### C-18: Advisory register carried structurally through framing vocabulary (R3-EX-02)
All pass. "THE PREFLIGHT CHECK", "READINESS SUMMARY", "pilot briefing — not a verdict", STATUS values (OK/FLAG/OPEN vs. PASS/FAIL) all carry advisory framing structurally. Register sustained throughout without reliance on a single top-of-file disclaimer.

#### C-19: Triple enforcement stack declared as unit with interdependency named (R3-EX-03)
All pass. All variations include ENFORCEMENT STACK NOTE declaring that the three rules "form a coordinated enforcement stack," that they "address independent failure modes," and that "no rule substitutes for another." The note names the stack explicitly and states the interdependency condition. Rule 3 = C-16 functional equivalent; Rule 1 = absence enforcement (C-13/C-14); Rule 2 = format enforcement (C-11). Functional equivalents accepted per rubric.

---

#### C-20: Location-enumeration requirement expressed as named meta-rule (R4-EX-01)

**Pass condition:** Rule 3 expressed as self-applying meta-rule governing all rule declarations *including itself* and future additions — not only as "Applies to: Rule 1, Rule 2."

| V | Rule 3 key text | C-20 verdict | Evidence |
|---|-----------------|--------------|---------|
| V-01 | "self-applying: it covers Rule 3 itself and any Rule added in the future. Applies to: all Rule declarations in this STANDING RULES block, present and future." | **PASS** | Explicit self-application + prospective coverage named. Self-reference ("Rule 3 itself") present. "Present and future" removes scope ambiguity. |
| V-02 | "Applies to: Rule 1, Rule 2." | **FAIL** | Enumerates only existing rules — omits Rule 3 itself and any future additions. Satisfies C-16 (location-complete for the rules it names) but not C-20 (no meta-rule property). |
| V-03 | "Applies to: Rule 1, Rule 2." | **FAIL** | Identical to V-02 on Rule 3. Same gap. |
| V-04 | "Applies to: all Rule declarations in this STANDING RULES block." | **PASS** | "All Rule declarations" is a universal quantifier covering Rule 3 itself (by membership) and future rules (they'd be in the block when added). Compact but sufficient for the meta-rule property. |
| V-05 | "Any rule added to this STANDING RULES block must declare all output locations it governs before becoming active. This requirement self-applies: Rule 3 itself declares its scope below. Applies to: all Rule declarations in this STANDING RULES block, including Rule 3 itself and any rule added in the future." | **PASS** | Most explicit form: self-application declared in rule body, self-reference to Rule 3, and prospective coverage all present. "Before becoming active" makes forward-compatibility operational. |

---

#### C-21: Each rule in the enforcement stack assigned a named failure class (R4-EX-02)

**Pass condition:** ENFORCEMENT STACK NOTE assigns a named failure class to each of the three rules — making the stack a diagnostic taxonomy, not just a prohibition list.

| V | Stack note failure-class content | C-21 verdict | Evidence |
|---|----------------------------------|--------------|---------|
| V-01 | "The three rules address independent failure modes: satisfying any two does not cover the failure addressed by the third." No per-rule labels. | **FAIL** | Declares independence and interdependency correctly (C-19 passes). But no named failure class assigned per rule. A reviewer cannot classify a violation by failure mode without reading the full rule body. |
| V-02 | "Rule 1 (absence declaration) — failure class: absence drift. Rule 2 (skill format) — failure class: reference ambiguity. Rule 3 (location scope) — failure class: unverifiable constraint." | **PASS** | Each rule carries a named failure class in "failure class: X" format. Taxonomy is complete and independently referable. |
| V-03 | Generic interdependency statement only. No per-rule failure-class labels. | **FAIL** | Same gap as V-01 — interdependency declared (C-19 passes) but no failure taxonomy. |
| V-04 | "Rule 1 — prevents silent omissions: outputs that appear complete but contain no evidence for missing dimensions. Rule 2 — prevents reference ambiguity: bare names or imprecise references block automated and human consumers from resolving skills. Rule 3 — prevents constraint scope gaps: a rule without explicit location scope cannot be verified without a full-output scan." | **PASS** | "Prevents X" format names the failure mode per rule ("silent omissions", "reference ambiguity", "constraint scope gaps"). The failure class is derivable from the rule entry alone without reading the full rule body. C-21 pass condition satisfied. |
| V-05 | "Rule 1 — failure class: omission failure. Rule 2 — failure class: resolution failure. Rule 3 — failure class: scope inheritance failure." With descriptions per class. | **PASS** | Explicit "failure class:" labels. Alternative vocabulary ("omission failure" / "resolution failure" / "scope inheritance failure") satisfies C-21 equally — class names are a taxonomy, not a fixed vocabulary. |

---

### Aspirational Summary Table

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | Cross-dimension patterns | PASS | PASS | PASS | PASS | PASS |
| C-10 | Missing signals by ns+skill | PASS | PASS | PASS | PASS | PASS |
| C-11 | /namespace:skill format | PASS | PASS | PASS | PASS | PASS |
| C-12 | Terminal MISSING SIGNAL GUIDE | PASS | PASS | PASS | PASS | PASS |
| C-13 | Absent evidence declared explicitly | PASS | PASS | PASS | PASS | PASS |
| C-14 | Named STANDING RULES block | PASS | PASS | PASS | PASS | PASS |
| C-15 | Verbatim absence phrases specified | PASS | PASS | PASS | PASS | PASS |
| C-16 | Constraints location-complete | PASS | PASS | PASS | PASS | PASS |
| C-17 | Verbatim phrases at point of use | PASS | PASS | PASS | PASS | PASS |
| C-18 | Advisory register structural | PASS | PASS | PASS | PASS | PASS |
| C-19 | Triple stack declared as unit | PASS | PASS | PASS | PASS | PASS |
| **C-20** | **Meta-rule self-applies** | **PASS** | **FAIL** | **FAIL** | **PASS** | **PASS** |
| **C-21** | **Named failure classes** | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** |
| **Aspirational** | | **12/13** | **12/13** | **11/13** | **13/13** | **13/13** |

---

## Composite Scores

```
composite = 90 + (aspirational_pass / 13) * 10
```

| V | Essential | Recommended | Aspirational | Composite | Golden? |
|---|-----------|-------------|--------------|-----------|---------|
| V-01 | 5/5 | 3/3 | 12/13 | **99.23** | YES |
| V-02 | 5/5 | 3/3 | 12/13 | **99.23** | YES |
| V-03 | 5/5 | 3/3 | 11/13 | **98.46** | YES |
| V-04 | 5/5 | 3/3 | 13/13 | **100.00** | YES |
| V-05 | 5/5 | 3/3 | 13/13 | **100.00** | YES |

**All 5 variations pass the Golden threshold (all essential pass + composite >= 80).**

---

## Research Question Resolutions

**RQ1 — C-20 alone (V-01):** CONFIRMED. Self-application framing satisfies C-20 independently of failure-class vocabulary. V-01 scores 99.23 (12/13), failing only C-21.

**RQ2 — C-21 alone (V-02):** CONFIRMED. Named failure-class labels satisfy C-21 independently of whether Rule 3 self-applies. V-02 scores 99.23 (12/13), failing only C-20.

**RQ3 — C-20/C-21 independence (V-01 vs. V-02 vs. V-03):**
- V-03: 11/13 (baseline — both absent)
- V-01: 12/13 (C-20 added, exactly +1 above V-03)
- V-02: 12/13 (C-21 added, exactly +1 above V-03)
- CONFIRMED: zero overlap. The two criteria are orthogonal. Each adds exactly one point independently.

**RQ4 — Phrasing-agnosticism (V-05):** CONFIRMED for both C-20 and C-21. Alternative C-20 forms ("RULE DECLARATIONS ARE SELF-SCOPING" / "before becoming active") and alternative C-21 vocabulary ("omission failure / resolution failure / scope inheritance failure") both pass. R6 phrasing-agnosticism criterion is not needed.

---

## Excellence Signals (Top Scorers: V-04, V-05)

**V-04 patterns:**
- Universal quantifier for C-20 — "all Rule declarations in this STANDING RULES block" achieves self-application concisely without needing to name Rule 3 explicitly. Future rules are covered by set membership.
- "Prevents X" framing satisfies C-21 — the failure type is named even without an explicit "failure class:" label. The diagnostic function is preserved.

**V-05 patterns (stronger form of both criteria):**
- Rule title encodes the property: "RULE DECLARATIONS ARE SELF-SCOPING" makes the meta-rule purpose visible at the heading, before the rule body is read.
- Explicit self-declaration anchor: "This requirement self-applies: Rule 3 itself declares its scope below" creates a reading-order guarantee — the self-application is visible before the "Applies to:" line.
- "Before becoming active" operationalizes forward-compatibility: future rules must declare scope at authoring time, not retroactively.
- Explicit "failure class:" labels (V-05) are more diagnostic-taxonomy-readable than "prevents X" (V-04) — class names appear as a lookup key.
- "Scope inheritance failure" as the Rule 3 failure class captures the mechanism more precisely than "constraint scope gaps" — it names what propagates incorrectly across additions, not just that a gap exists.

---

## Scorecard

| Rank | Variation | Composite | C-20 | C-21 | Note |
|------|-----------|-----------|------|------|------|
| 1 | V-04 | 100.00 | PASS | PASS | R4 V-05 verbatim — ceiling confirmed at 13/13 under v5 denominator |
| 1 | V-05 | 100.00 | PASS | PASS | Alternative phrasing — phrasing-agnosticism confirmed for both C-20 and C-21 |
| 3 | V-01 | 99.23 | PASS | FAIL | C-20 single-axis isolation confirmed |
| 3 | V-02 | 99.23 | FAIL | PASS | C-21 single-axis isolation confirmed |
| 5 | V-03 | 98.46 | FAIL | FAIL | R4 V-04 baseline — v5 denominator floor confirmed at 11/13 |

---

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["C-20 is phrasing-agnostic: self-application property satisfied by universal-quantifier scope ('all Rule declarations in this STANDING RULES block') or explicit self-declaration ('This requirement self-applies: Rule 3 itself declares its scope below') or forward-compatibility framing ('before becoming active') -- all three forms pass", "C-21 is phrasing-agnostic: failure-class assignment satisfied by 'prevents X' format (V-04) or explicit 'failure class: X' label (V-05) -- specific class vocabulary (absence drift / omission failure) does not discriminate; named-failure-mode per rule is the pass condition", "V-05 rule-title encoding: placing the meta-rule property in the rule name ('RULE DECLARATIONS ARE SELF-SCOPING') makes the self-scoping purpose visible before the rule body is read -- no scoring impact at R5 but identified as the canonical form for Rule 3 going forward"]}
```
