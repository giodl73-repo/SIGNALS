Now I have everything. Let me write the scorecard.

---

# signal-check Scorecard — R6 (2026-03-18)

**Rubric version**: v6  
**Criteria under test**: C-22 (temporal activation gate), C-23 (meta-rule self-application in rule body)  
**Composite denominator**: 15 aspirational criteria  
**Formula**: `composite = 90 + (aspirational_pass / 15) * 10`

---

## Variation Scoring

### V-01: C-22 PASS / C-23 FAIL — Temporal gate only

**Rule 3 key text**: `"governs before becoming active."` / `"Applies to: ... including Rule 3 itself."` (no body self-declaration)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All four dimensions present | PASS | SEQUENCE, COHERENCE, STALENESS, CAUSAL GAP all present |
| C-02 | SEQUENCE grounded in artifact dates | PASS | Artifact-date comparison structure present |
| C-03 | COHERENCE names specific signal pairs | PASS | Named pair structure required |
| C-04 | CAUSAL GAP states mechanism or absence | PASS | Verbatim absence phrase specified |
| C-05 | Advisory/coaching register throughout | PASS | Preflight framing throughout |
| C-06 | STALENESS applies named age threshold | PASS | Named threshold instruction present |
| C-07 | Every flagged issue includes next action | PASS | Action field required for FLAG/OPEN |
| C-08 | Readiness summary before dimension analysis | PASS | Written last, placed first instruction present |
| C-09 | Cross-dimension patterns named | PASS | CROSS-ITEM PATTERNS section present with shared-root examples |
| C-10 | Missing signals identified by namespace + skill | PASS | MISSING SIGNAL GUIDE with /namespace:skill format |
| C-11 | All skill references use /namespace:skill format | PASS | Rule 2 enforces this; examples correct |
| C-12 | Terminal MISSING SIGNAL GUIDE section | PASS | Dedicated final section present |
| C-13 | Absent evidence declared explicitly | PASS | Verbatim absence phrases required in each dimension |
| C-14 | Named STANDING RULES block precedes all analysis | PASS | STANDING RULES block with three named rules present |
| C-15 | Each dimension specifies required verbatim absence phrases | PASS | Required verbatim phrases embedded at each item |
| C-16 | Every constraint enumerates all output locations | PASS | Rule 1 and Rule 2 each carry full "Applies to:" lists |
| C-17 | Verbatim absence phrases embedded at point of use | PASS | Phrases appear inline within each dimension block |
| C-18 | Advisory register carried structurally | PASS | Preflight/pilot framing in headings and structure |
| C-19 | Triple enforcement stack declared as unit with interdependency | PASS | ENFORCEMENT STACK NOTE names all three and states "no rule substitutes for another" |
| C-20 | Location-enumeration expressed as named meta-rule | PASS | Rule 3 governs all Rule declarations via universal quantifier |
| C-21 | Each rule assigned a named failure class | PASS | Parenthetical labels present: (absence declaration), (skill format), (location enumeration); each describes failure mode |
| **C-22** | **Meta-rule includes temporal activation gate** | **PASS** | `"governs before becoming active"` — obligation is a precondition, not retroactive policy |
| **C-23** | **Self-application in rule body, not solely location annotation** | **FAIL** | Self-reference is only `"including Rule 3 itself"` in Applies-to line; rule body contains no self-application statement — reader must infer Rule 3 is a Rule declaration to recover self-application |

**Aspirational pass**: 14/15  
**Composite**: 90 + (14/15) × 10 = **99.33**  
**All essential pass**: YES  
**Golden**: YES

---

### V-02: C-22 FAIL / C-23 PASS — Body self-application only

**Rule 3 key text**: `"This requirement self-applies: Rule 3 itself declares its scope below."` (body) / no temporal gate

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-21 | (same as V-01 base) | PASS | Identical structure to V-01 except Rule 3 wording |
| **C-22** | **Temporal activation gate** | **FAIL** | Rule 3 body omits "before becoming active"; obligation reads as standing policy, not precondition — a rule could be considered in force before its scope is declared |
| **C-23** | **Self-application in rule body** | **PASS** | `"This requirement self-applies: Rule 3 itself declares its scope below."` appears in rule body text — self-reference parseable without inspecting Applies-to line; no inferential step required |

**Aspirational pass**: 14/15  
**Composite**: 90 + (14/15) × 10 = **99.33**  
**All essential pass**: YES  
**Golden**: YES

---

### V-03: C-22 FAIL / C-23 FAIL — R5 V-04 verbatim (v6 floor)

**Rule 3 key text**: `"Every Rule in this STANDING RULES block explicitly names all output locations it governs"` / `"Applies to: all Rule declarations in this STANDING RULES block."` (no gate, no body self-ref)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-21 | (same as V-01/V-02 base) | PASS | R5 V-04 passed all 13 aspirational through C-21; denominator change only affects ceiling |
| **C-22** | **Temporal activation gate** | **FAIL** | No "before becoming active" or equivalent temporal condition; location-scope obligation is stated as a standing description, not a rule-validity precondition |
| **C-23** | **Self-application in rule body** | **FAIL** | Applies-to uses universal quantifier (`"all Rule declarations"`) which covers Rule 3 implicitly but requires inference; rule body contains no explicit self-application statement |

**Aspirational pass**: 13/15  
**Composite**: 90 + (13/15) × 10 = **98.67**  
**All essential pass**: YES  
**Golden**: YES

---

### V-04: C-22 PASS / C-23 PASS — Compact minimal diff

**Rule 3 key text**: `"governs before becoming active. This requirement self-applies: Rule 3 itself declares its scope below."` (two additions to V-03 base)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-21 | (same as V-03 base) | PASS | All 13 prior aspirational criteria satisfied; V-03 base unchanged |
| **C-22** | **Temporal activation gate** | **PASS** | `"governs before becoming active"` — makes location-scope declaration a precondition for rule validity; a rule cannot be operative until scope is discharged |
| **C-23** | **Self-application in rule body** | **PASS** | `"This requirement self-applies: Rule 3 itself declares its scope below."` appears in rule body — self-reference explicit and parseable without inspecting Applies-to; no inference required |

**Aspirational pass**: 15/15  
**Composite**: 90 + (15/15) × 10 = **100.00**  
**All essential pass**: YES  
**Golden**: YES

---

### V-05: C-22 PASS / C-23 PASS — R5 V-05 verbatim (ceiling confirmation)

**Rule 3 key text**: Rule renamed "RULE DECLARATIONS ARE SELF-SCOPING"; `"governs before becoming active. This requirement self-applies: Rule 3 itself declares its scope below."` + future-proofing language; Applies-to includes "any rule added in the future"

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-21 | (same as V-03/V-04 base) | PASS | Confirmed by R5 scoring; R5 V-05 was the top scorer before C-22/C-23 were formalized |
| **C-22** | **Temporal activation gate** | **PASS** | `"governs before becoming active"` — identical phrasing to V-04; temporal precondition explicit |
| **C-23** | **Self-application in rule body** | **PASS** | `"This requirement self-applies: Rule 3 itself declares its scope below."` in rule body — body-level self-declaration identical to V-04; satisfies C-23 on property, not vocabulary |

**Aspirational pass**: 15/15  
**Composite**: 90 + (15/15) × 10 = **100.00**  
**All essential pass**: YES  
**Golden**: YES

---

## Variation Ranking

| Rank | Var | C-22 | C-23 | Asp. | Composite | Golden |
|------|-----|------|------|------|-----------|--------|
| 1 (tied) | V-04 | PASS | PASS | 15/15 | 100.00 | YES |
| 1 (tied) | V-05 | PASS | PASS | 15/15 | 100.00 | YES |
| 3 (tied) | V-01 | PASS | FAIL | 14/15 | 99.33 | YES |
| 3 (tied) | V-02 | FAIL | PASS | 14/15 | 99.33 | YES |
| 5 | V-03 | FAIL | FAIL | 13/15 | 98.67 | YES |

All five variations are golden. The rubric correctly separates C-22 and C-23 — V-01 and V-02 isolate each criterion cleanly, confirming they are independent properties.

---

## Excellence Signals

### From V-04 vs V-03 (minimal diff — what each criterion actually requires)

**C-22 mechanism**: "before becoming active" does not need to appear as a standalone sentence — appending it to the obligation clause (`"must declare ... governs before becoming active"`) is sufficient. The temporal gate is a property of the obligation, not a separate rule annotation.

**C-23 mechanism**: The body self-declaration is a single sentence that functions independently of the Applies-to line. `"This requirement self-applies: Rule 3 itself declares its scope below."` can be parsed without knowing the Applies-to contents. V-04 confirms C-23 is property-level: vocabulary may differ as long as the self-reference appears in the rule body.

### From V-05 vs V-04 (above the current ceiling — potential R7 signals)

Two patterns in V-05 score the same 100.00 as V-04 but are structurally stronger:

1. **Rule name as function declaration**: V-05 renames Rule 3 to "RULE DECLARATIONS ARE SELF-SCOPING" — the rule's purpose is encoded in the heading. A reader can recover the meta-rule's class from its name alone without reading the body. V-04 retains "CONSTRAINTS ARE LOCATION-COMPLETE," which describes the obligation without naming the meta-rule's structural role.

2. **Forward-scoping Applies-to clause**: V-05's Applies-to reads `"including Rule 3 itself and any rule added in the future"` — the scope declaration self-extends to future rules without amendment. V-04's Applies-to is `"all Rule declarations in this STANDING RULES block"` — future rules are covered by the universal quantifier but only implicitly; the future-scoping intent is not stated.

Neither pattern currently differentiates under v6. If a future variation tests a case where Rule 4 is added without an Applies-to line, the forward-scoping language in V-05 would make the violation more immediately detectable. These are candidates for C-24 and C-25.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Rule name as function declaration: encoding the meta-rule class in the rule heading makes the structural role recoverable from the name alone without reading the body", "Forward-scoping Applies-to clause: explicitly naming future rules in the Applies-to line makes scope self-extension stated rather than inferred from the universal quantifier"]}
```
